"""Đếm khảo sát theo đúng "Cách đếm" viết trước ở evidence/survey/questions.md.

Chạy:  python evidence/survey/count.py evidence/survey/raw-<...>.csv
  → ghi evidence/survey/results.csv (đổi tên cột q1…q10, không có cột liên hệ) và in số đếm.
Chạy lại trên results.csv cũng ra đúng số đó:  python evidence/survey/count.py evidence/survey/results.csv
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
COLS = ["timestamp", "q1_vai", "q2_dat_ho_1_thang", "q3_so_lan", "q4_so_nguoi", "q5_rang_buoc",
        "q6_cach_gom", "q7_thoi_gian", "q8_su_co", "q9_ke_lai", "q10_san_long_hoi_them"]

SU_CO = ["Chọn nhầm món cho người ăn chay / dị ứng / kiêng",
         "Tổng tiền vượt dự tính",
         "Có người bị thiếu món hoặc phải đổi món"]
KHAC_Q8 = ["Không biết món có thành phần gì", "Phải chọn lại quán"]


def load(path):
    with open(path, encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    return [dict(zip(COLS, r)) for r in rows[1:] if any(c.strip() for c in r)]


def pct(x, n):
    return "%d/%d" % (x, n) if n < 10 else "%d/%d (%.1f%%)" % (x, n, 100.0 * x / n)


def has(cell, label):
    return label.lower() in cell.lower()


def contradictory_q8(r):
    """Câu 8 vừa chọn "Không gặp chuyện nào" vừa chọn ô khác — form đã dặn không chọn thêm.
    Không dùng câu 8 của phiếu này (phiếu và các câu khác vẫn giữ). Luật này có từ lượt CP3."""
    cell = r["q8_su_co"]
    return has(cell, "Không gặp chuyện nào") and any(has(cell, s) for s in SU_CO + KHAC_Q8)


def main(path, out=None):
    rows = load(path)
    if os.path.basename(path).startswith("raw-"):
        # raw-20261127-1805.csv (CP2) → results.csv; bản xuất sau → results-<tên>.csv hoặc tên truyền vào
        out = out or os.path.join(HERE, "results.csv" if "20261127-1805" in path else "results-cp3.csv")
        with open(out, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=COLS)
            w.writeheader()
            w.writerows(rows)
        print("Đã ghi", os.path.relpath(out, HERE))
    n = len(rows)
    yes = [r for r in rows if r["q2_dat_ho_1_thang"].strip() == "Có"]
    y = len(yes)
    print("Phiếu: %d · giờ phiếu đầu %s · phiếu cuối %s" % (n, rows[0]["timestamp"], rows[-1]["timestamp"]))
    print("Vai (q1):", {v: sum(r["q1_vai"] == v for r in rows) for v in sorted({r["q1_vai"] for r in rows})})
    print("Từng đặt hộ nhóm ≥3 người trong 1 tháng (q2 = Có): %s   [giả thuyết ≥50%%]" % pct(y, n))
    bad = [r for r in yes if contradictory_q8(r)]
    usable = [r for r in yes if not contradictory_q8(r)]
    u = len(usable)
    print("Câu 8 mâu thuẫn, không dùng cho chỉ số câu 8: %d phiếu → mẫu số câu 8 = %d" % (len(bad), u))
    inc = [r for r in usable if any(has(r["q8_su_co"], s) for s in SU_CO)]
    print("Gặp ≥1 sự cố trong 3 ô (q8) / câu 8 dùng được: %s   [giả thuyết ≥1/3]" % pct(len(inc), u))
    for s in SU_CO + KHAC_Q8 + ["Không gặp chuyện nào"]:
        print("   q8 · %s: %s" % (s, pct(sum(has(r["q8_su_co"], s) for r in usable), u)))
    print("Đồng ý hỏi thêm (q10) / q2=Có: %s" % pct(sum(r["q10_san_long_hoi_them"].startswith("Có") for r in yes), y))
    slow = sum(r["q7_thoi_gian"] in ("10–20 phút", "Trên 20 phút") for r in yes)
    print("Mất >10 phút (q7) / q2=Có: %s · không nhớ: %d" % (pct(slow, y), sum(r["q7_thoi_gian"] == "Không nhớ" for r in yes)))
    for v in ("Có", "Không", "Không rõ, mình không hỏi"):
        print("Có ràng buộc ăn uống (q5 = %s) / q2=Có: %s" % (v, pct(sum(r["q5_rang_buoc"] == v for r in yes), y)))
    print("Cách gom (q6), chọn nhiều:")
    for v in ("Hỏi từng người qua chat", "Mỗi người tự chọn trên link chia sẻ", "Gửi menu vào nhóm chat", "Mình tự chọn hộ"):
        print("   %s: %s" % (v, pct(sum(has(r["q6_cach_gom"], v) for r in yes), y)))
    print("Số lần / tháng (q3, ghi tay, đọc nguyên văn):", [r["q3_so_lan"] for r in yes])
    print("Kể lại (q9) không trống:")
    for i, r in enumerate(rows, start=2):
        if r["q9_ke_lai"].strip():
            print("   dòng %d: %s" % (i, r["q9_ke_lai"].strip()))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "results.csv"), sys.argv[2] if len(sys.argv) > 2 else None)
