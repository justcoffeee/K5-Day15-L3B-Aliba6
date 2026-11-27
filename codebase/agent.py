"""Luồng chính — đặt đồ ăn hộ cả nhóm có ràng buộc ăn uống (Track D2). Nhóm Aliba6.

Hình dạng: WORKFLOW CỐ ĐỊNH, AI làm đúng một bước (chọn món). Sơ đồ ở spec.md §4.

    1. parse_request   (code)  đọc số người, ngân sách, quán, ai ăn chay / dị ứng gì, cờ rủi ro
    2. chặn sớm        (code)  cấp cứu → chuyển 115 · hỏi thuốc → từ chối · thiếu thông tin → hỏi lại
    3. get_menu + safe_dishes (code)  lọc món an toàn cho từng người
    4. kiểm khả thi    (code)  có người không có món an toàn / ngân sách không đủ → nói thẳng, đề xuất nới
    5. chọn món        (AI)    model chọn 1 món / người trong danh sách an toàn, theo ý thích, vừa ngân sách
    6. validate_cart   (code)  kiểm lại giỏ; sai → cho model sửa 1 lần → vẫn sai thì code tự chọn
    7. trả giỏ NHÁP    (code)  món nào cho ai, giá, phí ship, tổng — người đặt tự bấm đặt trên app

Model không bao giờ tự lọc dị ứng, tự cộng tiền hay tự đặt đơn.
"""
import json
import re

from ai import call_model
from tools import get_menu, list_restaurants, parse_request, safe_dishes, validate_cart
from tracing import note

SYSTEM = """Bạn giúp một người đặt đồ ăn hộ cả nhóm chọn món.
Mỗi người đã có sẵn danh sách món AN TOÀN (code đã lọc dị ứng, ăn chay). Chỉ được chọn trong danh sách đó.
Chọn đúng 1 món cho mỗi người, theo thứ tự ưu tiên:
1. Món người đó muốn ("muon"), nếu có trong danh sách của họ.
2. Món chính đủ no cho một bữa (cơm, bún, phở, mì, xôi); tránh món ăn kèm như nem, canh nếu còn món chính.
3. Món có ghi thành phần ("co_thanh_phan": true); món không ghi thành phần chỉ chọn khi không còn món khác.
4. Mỗi người khoảng (ngân sách - phí ship) / số người; không cần chọn món rẻ nhất, không cần tiêu hết tiền.
5. Đổi món giữa các người không ràng buộc cho đa dạng.
Tổng tiền món + phí ship không được vượt ngân sách. Không bịa món, không đổi giá.
Chỉ trả về JSON, không viết gì khác:
{"cart": [{"person": "<tên đúng như input>", "dish_id": "<mã món>", "ly_do": "<tối đa 12 chữ>"}]}"""

MAX_FIX = 1  # số lần cho model sửa giỏ sau khi validate_cart báo lỗi


def vnd(n):
    return "{:,}".format(int(n)).replace(",", ".") + "đ"


def _who(p):
    return "%s (%s)" % (p["name"], ", ".join(p["labels"])) if p["labels"] else p["name"]


# ---------- bước 2: chặn sớm ----------

def _early_stop(req):
    flags = req["flags"]
    if "cap_cuu" in flags:
        note("dừng: dấu hiệu cấp cứu")
        return ("Đây có thể là phản ứng dị ứng nghiêm trọng. Gọi cấp cứu 115 hoặc đưa bạn ấy tới cơ sở y tế gần nhất "
                "ngay bây giờ. Mình không tư vấn y tế và tạm dừng việc đặt món.")
    if "hoi_y_te" in flags and req["restaurant_id"] is None:
        note("dừng: hỏi y tế, ngoài phạm vi")
        return ("Mình chỉ giúp chọn món an toàn theo menu, không tư vấn thuốc hay điều trị dị ứng. "
                "Bạn hỏi bác sĩ hoặc dược sĩ nhé. Nếu đang khó thở, sưng môi họng: gọi 115 ngay.")
    missing = [m for m in req["missing"] if m != "so_nguoi_khong_khop"]
    if missing:
        names = ", ".join(r["name"] for r in list_restaurants())
        ask = {"quan": "đặt ở quán nào (đang có: %s)" % names,
               "ngan_sach": "ngân sách tổng là bao nhiêu (đã gồm phí ship)",
               "so_nguoi": "nhóm có mấy người"}
        note("dừng: thiếu %s → hỏi lại" % ", ".join(missing))
        return "Mình cần thêm thông tin trước khi chọn món: " + "; ".join(ask[m] for m in missing) + "?"
    return None


# ---------- bước 4: kiểm khả thi ----------

def _cheapest_total(restaurant_id, people):
    """Tổng rẻ nhất có thể (món rẻ nhất an toàn cho từng người + ship). None nếu có người không có món."""
    menu = get_menu(restaurant_id)
    total = menu["ship_fee"]
    for p in people:
        options = safe_dishes(restaurant_id, p)
        if not options:
            return None
        total += options[0]["price"]
    return total


def _infeasible(req, menu, options):
    budget = req["budget"]
    no_dish = [p for p in req["people"] if not options[p["name"]]]
    others = []
    for r in list_restaurants():
        if r["id"] != menu["id"]:
            t = _cheapest_total(r["id"], req["people"])
            if t is not None:
                others.append((t, r["name"]))
    others.sort()
    alt = ""
    if others:
        t, name = others[0]
        alt = " Có thể đổi sang %s: đủ món an toàn cho cả nhóm, tổng thấp nhất %s%s." % (
            name, vnd(t), "" if t <= budget else " (vẫn vượt ngân sách)")
    if no_dish:
        note("dừng: không có món an toàn cho %s" % ", ".join(p["name"] for p in no_dish))
        return ("Không lập được giỏ ở %s: không có món nào an toàn cho %s (món không ghi thành phần cũng bị loại)."
                % (menu["name"], "; ".join(_who(p) for p in no_dish)) + alt +
                " Mình không chèn món không chắc an toàn.")
    floor = menu["ship_fee"] + sum(options[p["name"]][0]["price"] for p in req["people"])
    if floor > budget:
        note("dừng: ngân sách %d < tối thiểu %d" % (budget, floor))
        return ("Ngân sách %s không đủ cho %d người ở %s. Rẻ nhất đã là %s tiền món + %s phí ship = %s, "
                "thiếu %s. Bạn có thể: tăng ngân sách lên ít nhất %s, bớt người hoặc tách đơn.%s"
                % (vnd(budget), len(req["people"]), menu["name"], vnd(floor - menu["ship_fee"]),
                   vnd(menu["ship_fee"]), vnd(floor), vnd(floor - budget), vnd(floor), alt))
    return None


# ---------- bước 5: AI chọn món ----------

def _ask_model(req, menu, options, feedback=""):
    payload = {
        "quan": menu["name"], "phi_ship": menu["ship_fee"], "ngan_sach": req["budget"],
        "nguoi": [{"ten": p["name"], "rang_buoc": p["labels"], "muon": p["wants"],
                   "mon_an_toan": [{"id": d["id"], "ten": d["name"], "gia": d["price"],
                                    "co_thanh_phan": d["ingredients"] is not None} for d in options[p["name"]]]}
                  for p in req["people"]],
    }
    user = json.dumps(payload, ensure_ascii=False)
    if feedback:
        user += "\n\nGiỏ trước bị code kiểm ra lỗi, sửa lại:\n" + feedback
    reply = call_model(SYSTEM, user)
    m = re.search(r"\{.*\}", reply["text"], re.S)
    try:
        cart = json.loads(m.group(0))["cart"] if m else None
        return [{"person": c["person"], "dish_id": c["dish_id"], "ly_do": c.get("ly_do", "")} for c in cart]
    except (ValueError, KeyError, TypeError):
        return None


def _code_pick(req, menu, options):
    """Dự phòng khi model không trả giỏ hợp lệ: món người muốn nếu an toàn, không thì món gần mức chia đều."""
    share = (req["budget"] - menu["ship_fee"]) / len(req["people"])
    cart, used = [], set()
    for p in req["people"]:
        opts = options[p["name"]]
        wanted = [d for d in opts if d["id"] == p["wants"]]
        # ưu tiên món có ghi thành phần, chưa ai trong nhóm chọn, giá gần mức chia đều
        fit = sorted((d for d in opts if d["price"] <= share),
                     key=lambda d: (d["ingredients"] is not None, d["id"] not in used, d["price"]))
        dish = wanted[0] if wanted else (fit[-1] if fit else opts[0])
        used.add(dish["id"])
        cart.append({"person": p["name"], "dish_id": dish["id"], "ly_do": "code chọn dự phòng"})
    prices = {d["id"]: d["price"] for d in menu["dishes"]}
    total = lambda: menu["ship_fee"] + sum(prices[c["dish_id"]] for c in cart)  # noqa: E731
    while total() > req["budget"]:  # hạ món đắt nhất còn hạ được — luôn dừng vì đã kiểm khả thi
        best = None
        for c in cart:
            cheaper = [d for d in options[c["person"]] if d["price"] < prices[c["dish_id"]]]
            if cheaper and (best is None or prices[c["dish_id"]] > prices[best[0]["dish_id"]]):
                best = (c, cheaper[-1])
        if best is None:
            break
        best[0]["dish_id"], best[0]["ly_do"] = best[1]["id"], "hạ món cho vừa ngân sách"
    return cart


# ---------- bước 7: trả giỏ nháp ----------

def _format(req, menu, cart, check, extra):
    dishes = {d["id"]: d for d in menu["dishes"]}
    by_name = {p["name"]: p for p in req["people"]}
    lines = ["Giỏ NHÁP — %s (chưa đặt; bạn kiểm rồi tự bấm đặt trên app):" % menu["name"]]
    for c in cart:
        d = dishes[c["dish_id"]]
        lines.append("- %s: %s [%s] — %s" % (_who(by_name[c["person"]]), d["name"], d["id"], vnd(d["price"])))
    lines.append("Tiền món %s + phí ship %s = TỔNG %s / ngân sách %s (còn %s)." % (
        vnd(check["food_total"]), vnd(check["ship_fee"]), vnd(check["total"]), vnd(req["budget"]),
        vnd(req["budget"] - check["total"])))
    lines.append("Đã kiểm bằng code: 0 món vi phạm ăn chay / dị ứng; món không ghi thành phần không chọn cho người có ràng buộc.")
    lines += extra
    lines.append("Thành phần lấy theo menu quán ghi. Người dị ứng nặng nên hỏi lại quán trước khi ăn.")
    return "\n".join(lines)


def answer(text: str) -> dict:
    req = parse_request(text)
    stop = _early_stop(req)
    if stop:
        return {"output": stop}

    extra = []
    if "bo_qua_rang_buoc" in req["flags"]:
        extra.append("Mình vẫn giữ lọc dị ứng / ăn chay — phần này không tắt được, kể cả khi bạn bảo bỏ qua.")
    if "doi_dat_don" in req["flags"] or "chen_lenh" in req["flags"]:
        extra.append("Mình không tự đặt đơn hay thanh toán, và không sửa giá / tổng tiền. Đây chỉ là giỏ nháp, tổng tính đúng theo menu.")
    if "so_nguoi_khong_khop" in req["missing"]:
        extra.append("Số tên bạn ghi nhiều hơn số người — mình lập giỏ theo đủ các tên đã ghi.")

    menu = get_menu(req["restaurant_id"])
    options = {p["name"]: safe_dishes(menu["id"], p) for p in req["people"]}
    for p in req["people"]:
        if p["wants"] and p["wants"] not in [d["id"] for d in options[p["name"]]]:
            wanted = next(d for d in menu["dishes"] if d["id"] == p["wants"])
            extra.append("%s muốn %s nhưng món này không hợp với %s, nên mình chọn món khác — %s xác nhận lại giúp nhé."
                         % (p["name"], wanted["name"], ", ".join(p["labels"]) or "ràng buộc đã ghi", p["name"]))
    stop = _infeasible(req, menu, options)
    if stop:
        return {"output": stop}

    constraints = {"restaurant_id": menu["id"], "budget": req["budget"], "people": req["people"]}
    cart, feedback = None, ""
    for attempt in range(1 + MAX_FIX):
        cart = _ask_model(req, menu, options, feedback)
        if cart is None:
            note("model không trả JSON giỏ hợp lệ (lần %d)" % (attempt + 1))
            break
        check = validate_cart(cart, constraints)
        if check["ok"]:
            break
        feedback = "\n".join(check["violations"])
        note("validate_cart lần %d: %s" % (attempt + 1, feedback))
        cart = None
    if cart is None:
        cart = _code_pick(req, menu, options)
        note("dùng giỏ code chọn dự phòng")
    check = validate_cart(cart, constraints)
    if not check["ok"]:  # không bao giờ đưa giỏ sai ra ngoài
        note("dừng: giỏ dự phòng vẫn lỗi: %s" % check["violations"])
        return {"output": "Mình chưa lập được giỏ an toàn và vừa ngân sách. Lỗi: " + "; ".join(check["violations"])}
    return {"output": _format(req, menu, cart, check, extra)}
