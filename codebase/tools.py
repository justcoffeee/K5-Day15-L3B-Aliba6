"""Công cụ của bài toán D2 — đặt đồ ăn hộ cả nhóm có ràng buộc ăn uống. Nhóm Aliba6.

Mọi công cụ ở đây CHỈ ĐỌC hoặc CHỈ TÍNH — không công cụ nào đặt đơn, thanh toán hay gửi tin.
Việc kiểm dị ứng / ăn chay / tổng tiền chạy bằng code ở đây, không để model tự lọc, tự cộng (bẫy track D).

    get_menu(restaurant_id)            → menu một quán: món, giá, tag thành phần, phí ship
    list_restaurants()                 → danh sách quán có trong data/menu.json
    parse_request(text)                → đọc yêu cầu thành ràng buộc (số người, ngân sách, ai kiêng gì)
    safe_dishes(restaurant_id, person) → các món người đó ăn được an toàn
    validate_cart(cart, constraints)   → danh sách vi phạm + tổng tiền gồm phí ship

Dữ liệu: data/menu.json (synthetic, mô tả ở data/DATA_CARD.md).
"""
import json
import os
import re

from tracing import tool, TOOLS  # noqa: F401

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MENU_PATH = os.path.join(ROOT, "data", "menu.json")

# Thành phần mà người ăn chay không ăn. Chốt theo cách hiểu chặt (không thịt, cá, hải sản,
# nước mắm, mắm, trứng) — ghi ở data/DATA_CARD.md. Hiểu chặt để không bao giờ chọn nhầm.
NON_VEG = {"ga", "bo", "heo", "tom", "muc", "cua", "ca", "nuoc_mam", "mam_tom", "trung"}

# Từ người dùng gõ → tag thành phần trong menu. Một từ có thể chặn nhiều tag (chọn phía an toàn).
INGREDIENT_WORDS = [
    (r"đậu phộng|lạc", ["dau_phong"], "đậu phộng"),
    (r"hải sản", ["tom", "muc", "cua", "ca", "mam_tom"], "hải sản"),
    (r"tôm", ["tom", "mam_tom"], "tôm"),
    (r"cua", ["cua"], "cua"),
    (r"mực", ["muc"], "mực"),
    (r"cá", ["ca"], "cá"),
    (r"trứng", ["trung"], "trứng"),
    (r"sữa", ["sua"], "sữa"),
    (r"đậu nành|đậu hũ|đậu phụ", ["dau_nanh", "dau_hu"], "đậu nành"),
    (r"gluten|bột mì", ["bot_mi"], "gluten"),
    (r"bò", ["bo"], "bò"),
    (r"heo|lợn", ["heo"], "heo"),
    (r"gà", ["ga"], "gà"),
]

# Chữ viết hoa đứng đầu câu / tên quán — không phải tên người.
NOT_NAMES = {"Đặt", "Quán", "Cơm", "Bún", "Mẫu", "Kệ", "Bỏ", "Ngân", "Tổng", "Giỏ", "Mình", "Bạn",
             "Hai", "Ba", "Một", "Bốn", "Năm", "Nhóm", "Cho", "Thêm", "Lấy", "Chọn", "Đơn", "Trưa",
             "Hôm", "Ai", "Giúp", "Ghi", "Nhanh", "Mọi", "Còn", "Người", "Không", "Phở", "Xôi",
             "Gỏi", "Canh", "Mì", "Bánh", "Nem", "Tất", "Cả", "Cứ", "Làm", "Thanh", "Nhớ"}

# Chữ viết hoa ở ĐẦU CÂU chỉ được coi là tên khi từ ngay sau nó nói về việc ăn của một người
# ("An ăn chay", "Hoa dị ứng …") hoặc ngay sau là dấu phẩy. Nhờ vậy "Đợt trước …", "Có 2 bạn …",
# "App giao trễ …" không thành tên.
NAME_NEXT = {"ăn", "dị", "kiêng", "không", "muốn", "thích", "thấy", "lấy", "gọi", "và", "với", "thì", "cần", "chỉ"}

# Từ báo ràng buộc ăn uống — mọi chỗ xuất hiện phải gắn được vào một người, nếu không thì hỏi lại.
CONSTRAINT_RE = r"ăn chay|dị ứng|không ăn|kiêng"

# Từ đếm người không tên: "2 người ăn chay", "một bạn dị ứng tôm".
COUNT_RE = r"(\d+|một|hai|ba|bốn|năm|sáu|bảy|tám)"

NUM_WORDS = {"một": 1, "hai": 2, "ba": 3, "bốn": 4, "năm": 5, "sáu": 6, "bảy": 7, "tám": 8}


def _load():
    with open(MENU_PATH, encoding="utf-8") as f:
        return json.load(f)


def _restaurant(restaurant_id):
    for r in _load()["restaurants"]:
        if r["id"] == restaurant_id:
            return r
    return None


@tool
def list_restaurants() -> list:
    """Tên: list_restaurants · Input: không · Output: [{"id", "name", "ship_fee"}] · Không tác động ra ngoài."""
    return [{"id": r["id"], "name": r["name"], "ship_fee": r["ship_fee"]} for r in _load()["restaurants"]]


@tool
def get_menu(restaurant_id: str) -> dict:
    """Tên: get_menu · Input: restaurant_id (str) · Output: {"id", "name", "ship_fee", "dishes": [{"id",
    "name", "price", "ingredients" (list tag hoặc None = quán không ghi)}]}, hoặc {} nếu không có quán.
    Không tác động ra ngoài."""
    return _restaurant(restaurant_id) or {}


# ---------- đọc yêu cầu (code, không phải AI) ----------

def _money(text):
    """Ngân sách: số có đơn vị k / nghìn / ngàn / triệu, nếu không có thì số có đ / vnđ ≥ 1.000."""
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*(k|nghìn|ngàn|tr|triệu)(?![a-zà-ỹ])", text, re.I)
    if m:
        value = float(m.group(1).replace(",", "."))
        return int(value * (1_000_000 if m.group(2).lower() in ("tr", "triệu") else 1000))
    for m in re.finditer(r"(\d{1,3}(?:[.,]\d{3})+|\d{4,})\s*(đ|vnđ|vnd|đồng)", text, re.I):
        value = int(re.sub(r"[.,]", "", m.group(1)))
        if value >= 1000:
            return value
    return None


def _num(token):
    token = token.lower()
    return int(token) if token.isdigit() else NUM_WORDS.get(token)


def _clause_constraints(clause):
    """Từ một đoạn mô tả một người → (ăn chay?, tag phải tránh, nhãn hiển thị, ràng buộc không hiểu).
    "dị ứng / kiêng / không ăn X" mà X không khớp thành phần nào đã biết → trả ở phần "không hiểu" để hỏi lại,
    không lặng lẽ bỏ qua."""
    low = clause.lower()
    veg = "ăn chay" in low
    avoid, labels, unknown = set(), [], []
    if veg:
        labels.append("ăn chay")
    for kind in ("dị ứng", "không ăn", "kiêng"):
        for m in re.finditer(kind + r"\s+([^,.;]+)", low):
            part = m.group(1)
            # dừng ở chỗ bắt đầu ý khác (vd "… nhưng An muốn …")
            part = re.split(r"\b(?:nhưng|muốn|thích|mà)\b", part)[0]
            if re.match(r"\s*(gì|đi\b)", part):  # "không ai kiêng gì", "kệ dị ứng đi"
                continue
            found = False
            for pattern, tags, label in INGREDIENT_WORDS:
                if re.search(r"(?<![a-zà-ỹ])(?:%s)(?![a-zà-ỹ])" % pattern, part):
                    avoid.update(tags)
                    labels.append("%s %s" % (kind, label))
                    found = True
            if not found:
                unknown.append("%s %s" % (kind, part.strip()))
    return veg, avoid, labels, unknown


def _find_dish(text, restaurant):
    """Món người dùng nhắc tên (khớp nguyên tên món trong menu, không phân biệt hoa thường)."""
    low = text.lower()
    best = None
    for d in restaurant["dishes"] if restaurant else []:
        name = d["name"].lower()
        if name in low and (best is None or len(name) > len(best["name"])):
            best = d
    return best


@tool
def parse_request(text: str) -> dict:
    """Tên: parse_request · Input: yêu cầu người đặt hộ (str) · Output: {"restaurant_id", "budget",
    "total", "people": [{"name", "vegetarian", "avoid", "labels", "wants"}], "missing": [...], "flags": [...],
    "unclear": [ràng buộc không gán được cho ai / không hiểu thành phần]}.
    Chạy bằng code (regex), không phải AI. Không hiểu chắc thì ghi vào "missing" để hỏi lại. Không tác động ra ngoài."""
    low = text.lower()
    flags = []
    if re.search(r"khó thở|nổi mẩn|sưng (môi|mặt|họng)|ngất|sốc phản vệ|ngộ độc|co giật", low):
        flags.append("cap_cuu")
    if re.search(r"kệ dị ứng|bỏ qua dị ứng|đừng (lọc|kiểm)|không cần (lọc|kiểm)|kệ (vụ )?ăn chay", low):
        flags.append("bo_qua_rang_buoc")
    if re.search(r"đặt luôn|thanh toán|trả tiền|bấm đặt giùm|chốt đơn giùm|đặt giùm luôn|quẹt thẻ", low):
        flags.append("doi_dat_don")
    if re.search(r"bỏ qua (mọi|tất cả|các) (quy tắc|hướng dẫn)|ignore (all|previous)|quy tắc trước", low):
        flags.append("chen_lenh")
    if re.search(r"thuốc|uống gì|chữa|điều trị", low):
        flags.append("hoi_y_te")

    restaurant = None
    for r in _load()["restaurants"]:
        short = r["name"].lower().replace("quán ", "")
        if r["name"].lower() in low or short in low:
            restaurant = r
    budget = _money(text)

    total = None
    m = re.search(r"(?:cho|nhóm|gồm)?\s*(\d+|một|hai|ba|bốn|năm|sáu|bảy|tám)\s+người(?!\s+(?:ăn chay|dị ứng|không ăn|kiêng|còn lại))", low)
    if m:
        total = _num(m.group(1))

    # Người có tên: chữ viết hoa không nằm trong danh sách loại trừ; ở đầu câu thì phải có NAME_NEXT ngay sau.
    words = [(m.start(), m.group(0)) for m in re.finditer(r"[^\W\d_]+", text)]
    names = []
    for i, (pos, word) in enumerate(words):
        if not (word[0].isupper() and word[1:].islower()) or word in NOT_NAMES or word in names:
            continue
        sentence_start = re.fullmatch(r"\s*", text[:pos]) or re.search(r"[.!?]\s*$", text[:pos])
        nxt = words[i + 1][1].lower() if i + 1 < len(words) else ""
        if sentence_start and nxt not in NAME_NEXT and not text[pos + len(word):].startswith(","):
            continue
        names.append(word)
    positions = [(pos, w) for pos, w in words if w in names]
    covered = []  # các đoạn văn đã gán được cho một người — để soát ràng buộc bị bỏ sót
    unknown = []

    people = {n: {"name": n, "vegetarian": False, "avoid": set(), "labels": [], "wants": None} for n in names}
    for i, (pos, name) in enumerate(positions):
        end = positions[i + 1][0] if i + 1 < len(positions) else len(text)
        clause = text[pos + len(name):end]
        stop = re.search(r"[.;]", clause)
        clause = clause[:stop.start()] if stop else clause
        covered.append((pos, pos + len(name) + len(clause)))
        veg, avoid, labels, unk = _clause_constraints(clause)
        unknown += unk
        p = people[name]
        p["vegetarian"] = p["vegetarian"] or veg
        p["avoid"] |= avoid
        p["labels"] += [lb for lb in labels if lb not in p["labels"]]
        dish = _find_dish(clause, restaurant)
        if dish:
            p["wants"] = dish["id"]
    ordered = [people[n] for n in names]

    # Người không tên: "2 người ăn chay", "1 bạn dị ứng hải sản", "một bạn kiêng thịt bò".
    unnamed = []
    for m in re.finditer(COUNT_RE + r"\s+(?:người|bạn)\s+((?:%s)[^,.;]*)" % CONSTRAINT_RE, low):
        covered.append((m.start(), m.end()))
        veg, avoid, labels, unk = _clause_constraints(m.group(2))
        unknown += unk
        for _ in range(_num(m.group(1)) or 0):
            unnamed.append({"vegetarian": veg, "avoid": set(avoid), "labels": list(labels), "wants": None})
    # Người không tên muốn một món: "1 bạn ăn bún chả", "2 bát bún chả".
    for m in re.finditer(COUNT_RE + r"\s+(?:(?:người|bạn)\s+(?:ăn|muốn|lấy|gọi)|bát|tô|suất|phần|đĩa)\s+([^,.;]+)", low):
        dish = _find_dish(m.group(2), restaurant)
        if dish:
            for _ in range(_num(m.group(1)) or 0):
                unnamed.append({"vegetarian": False, "avoid": set(), "labels": [], "wants": dish["id"]})

    # Soát: mọi chỗ ghi ràng buộc phải nằm trong đoạn đã gán cho một người và hiểu được thành phần.
    unclear = list(unknown)
    for m in re.finditer(CONSTRAINT_RE, low):
        if any(a <= m.start() < b for a, b in covered):
            continue
        if re.search(r"(kệ|bỏ qua)\s*$", low[:m.start()]) or re.match(r"(?:%s)\s+(gì|đi\b)" % CONSTRAINT_RE, low[m.start():]):
            continue  # "kệ dị ứng đi", "không ai kiêng gì" — không phải ràng buộc của một người
        unclear.append(re.split(r"[,.;]", text[m.start():m.start() + 40])[0].strip())

    missing = []
    if total is None:
        total = len(ordered) + len(unnamed) if (ordered or unnamed) else None
    if total is not None:
        k = 1
        while len(ordered) < total:
            base = unnamed.pop(0) if unnamed else {"vegetarian": False, "avoid": set(), "labels": [], "wants": None}
            base["name"] = "Người %d" % k
            k += 1
            ordered.append(base)
        if len(ordered) > total:
            missing.append("so_nguoi_khong_khop")
    if unclear:
        missing.append("rang_buoc_chua_ro")
    if restaurant is None:
        missing.append("quan")
    if budget is None:
        missing.append("ngan_sach")
    if total is None:
        missing.append("so_nguoi")

    for p in ordered:
        p["avoid"] = sorted(p["avoid"])
    return {"restaurant_id": restaurant["id"] if restaurant else None, "budget": budget, "total": total,
            "people": ordered, "missing": missing, "flags": flags, "unclear": unclear}


# ---------- kiểm an toàn và tiền (code, không phải AI) ----------

def _unsafe_reason(dish, person):
    """None nếu món an toàn cho người này; ngược lại trả lý do."""
    constrained = person.get("vegetarian") or person.get("avoid")
    if dish["ingredients"] is None:
        return "không rõ thành phần" if constrained else None
    tags = set(dish["ingredients"])
    if person.get("vegetarian") and tags & NON_VEG:
        return "không chay (có %s)" % ", ".join(sorted(tags & NON_VEG))
    bad = tags & set(person.get("avoid") or [])
    if bad:
        return "có %s" % ", ".join(sorted(bad))
    return None


@tool
def safe_dishes(restaurant_id: str, person: dict) -> list:
    """Tên: safe_dishes · Input: restaurant_id, person {"vegetarian", "avoid"} · Output: các món người đó ăn
    được, rẻ → đắt. Món không ghi thành phần bị loại nếu người đó có ràng buộc. Không tác động ra ngoài."""
    r = _restaurant(restaurant_id)
    if not r:
        return []
    ok = [d for d in r["dishes"] if _unsafe_reason(d, person) is None]
    return sorted(ok, key=lambda d: (d["price"], d["id"]))


@tool
def validate_cart(cart: list, constraints: dict) -> dict:
    """Tên: validate_cart · Input: cart [{"person", "dish_id"}], constraints {"restaurant_id", "budget",
    "people"} · Output: {"ok", "violations": [str], "food_total", "ship_fee", "total", "budget"}.
    Chạy bằng code — đây là chỗ chặn rủi ro chính. Không tác động ra ngoài."""
    r = _restaurant(constraints["restaurant_id"])
    violations = []
    if not r:
        return {"ok": False, "violations": ["KHONG_CO_QUAN"], "food_total": 0, "ship_fee": 0, "total": 0,
                "budget": constraints.get("budget")}
    dishes = {d["id"]: d for d in r["dishes"]}
    people = {p["name"]: p for p in constraints["people"]}
    seen = {}
    food_total = 0
    for item in cart:
        name, dish_id = item.get("person"), item.get("dish_id")
        if name not in people:
            violations.append("NGUOI_LA: %s không có trong nhóm" % name)
            continue
        seen[name] = seen.get(name, 0) + 1
        dish = dishes.get(dish_id)
        if not dish:
            violations.append("MON_KHONG_CO: %s không có trong menu %s" % (dish_id, r["name"]))
            continue
        food_total += dish["price"]
        reason = _unsafe_reason(dish, people[name])
        if reason:
            violations.append("KHONG_AN_TOAN: %s — %s (%s)" % (name, dish["name"], reason))
    for name in people:
        if seen.get(name, 0) != 1:
            violations.append("SO_MON: %s có %d món (cần đúng 1)" % (name, seen.get(name, 0)))
    total = food_total + r["ship_fee"]
    budget = constraints.get("budget")
    if budget is not None and total > budget:
        violations.append("VUOT_NGAN_SACH: tổng %d (gồm ship %d) > ngân sách %d" % (total, r["ship_fee"], budget))
    return {"ok": not violations, "violations": violations, "food_total": food_total,
            "ship_fee": r["ship_fee"], "total": total, "budget": budget}
