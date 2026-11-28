"""Đếm bản chụp khảo sát CP3; không sửa dữ liệu.
Hiển thị số tổng hợp: python evidence/survey/count_cp3.py
Đếm lại bản nội bộ trên máy: python evidence/survey/count_cp3.py <local-snapshot.json>
"""
import json
import sys
from pathlib import Path

COUNTS = Path(__file__).with_name("counts-cp3-20261128.json")
ISSUES = (
    "Chọn nhầm món cho người ăn chay / dị ứng / kiêng",
    "Tổng tiền vượt dự tính",
    "Có người bị thiếu món hoặc phải đổi món",
)
OTHER = ("Không biết món có thành phần gì", "Phải chọn lại quán", "Không gặp chuyện nào")


def count(data):
    rows = data["responses"]
    eligible = [r for r in rows if r["q2_ordered"].strip() == "Có"]
    usable = [
        r for r in eligible
        if not (
            "Không gặp chuyện nào" in r["q8_issues"]
            and "," in r["q8_issues"]
        )
    ]
    return {
        "total": len(rows),
        "eligible": len(eligible),
        "q8_usable": len(usable),
        "q8_not_used": len(eligible) - len(usable),
        "incidents": sum(any(s in r["q8_issues"] for s in ISSUES) for r in usable),
        "q8": {s: sum(s in r["q8_issues"] for r in usable) for s in ISSUES + OTHER},
        "dietary": {s: sum(r["q5_dietary"] == s for r in eligible)
                    for s in ("Có", "Không", "Không rõ, mình không hỏi")},
        "duration": {s: sum(r["q7_duration"] == s for r in eligible)
                     for s in ("Dưới 5 phút", "5–10 phút", "10–20 phút", "Trên 20 phút", "Không nhớ")},
        "followup_eligible": sum(r["q10_followup"].startswith("Có") for r in eligible),
    }


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) > 1:
        # Bản chụp từng phiếu là dữ liệu nội bộ, người chạy cung cấp ở máy mình.
        with Path(sys.argv[1]).open(encoding="utf-8") as handle:
            result = count(json.load(handle))
    else:
        # Không có bản gốc: chỉ hiển thị số tổng hợp đã công bố, không giả vờ đếm lại.
        with COUNTS.open(encoding="utf-8") as handle:
            result = {"mode": "published_aggregate", "counts": json.load(handle)["counts"]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
