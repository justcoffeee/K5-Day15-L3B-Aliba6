# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Mạnh nhất: đào data ra insight → hỏi người dùng để kiểm lại (hoặc ngược lại).

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☐ | `evidence/data-mining.md` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☐ | `evidence/interviews/P1.md`… |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☑ 22 phiếu (đếm lần 1, 18:05 27/11) — 13 người đúng người dùng (đã đặt hộ nhóm trong tháng) | `evidence/survey/results.csv` · cách đếm: `evidence/survey/count.py` |

## 2. Số chính

- Đào data: __/__ (__%) …
- Phỏng vấn: __/3 người gặp *(n nhỏ không ghi %)* · số lần / tháng: P1 __, P2 __, P3 __ · mỗi lần mất __–__ phút
- Khảo sát (đếm lần 1, bản xuất 18:05 27/11/2026, chạy lại: `python evidence/survey/count.py`): **N = 22**
  - Từng đặt hộ nhóm ≥3 người trong 1 tháng qua: **13/22 (59.1%)** — giả thuyết ≥50%: đạt.
  - Trong 13 người đó, gặp ≥1 sự cố (nhầm món cho người ăn chay / dị ứng · vượt dự tính · thiếu / phải đổi món): **7/13 (53.8%)** — giả thuyết ≥1/3: đạt.
  - Tách theo loại sự cố (trên 13): thiếu món / phải đổi món **6/13** · vượt dự tính (phí ship, phí dịch vụ) **2/13** · không biết thành phần món **1/13** · phải chọn lại quán **1/13** · **chọn nhầm món cho người ăn chay / dị ứng / kiêng: 0/13** · không gặp chuyện nào 6/13.
  - Nhóm lần gần nhất có người không ăn được một số món: **3/13** có · 7/13 không · 3/13 không rõ.
  - Mất >10 phút từ chọn quán đến bấm đặt: **5/13** (4 người 10–20 phút, 1 người >20 phút).
  - Cách gom (chọn nhiều): mỗi người tự chọn trên giỏ nhóm của app 7/13 · gửi menu vào nhóm chat 7/13 · hỏi từng người qua chat 4/13 · tự chọn hộ luôn 0/13.
  - Vai: 9 học viên L3B · 5 L3A · 2 lớp khác · 1 lab coach / TA · 5 "khác". Câu 3 (số lần / tháng) ghi tay, từ 1 đến 20 lần.

Phỏng vấn nhiều vai thì đếm theo từng vai, không cộng chung.

| | Vai | Gặp pain? | Số lần / 1 tháng qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | | | | | |
| P2 | | | | | |
| P3 | | | | | |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. "Món bị sai, bạn tôi không chịu ăn và thanh toán món đấy" — phiếu khảo sát dòng 10 (`results.csv`)
2. "mình bị người khác lấy nhầm suất ăn và phải nhận 1 suất đồ ăn khác" — phiếu khảo sát dòng 3
3. "Đơn vị không giao hàng" — phiếu khảo sát dòng 9 *(lỗi phía giao hàng, ngoài lát cắt)*
4.
5.

## 4. Các nguồn có khớp nhau không

Data nói __; người dùng nói __. Khớp / lệch ở đâu, vì sao: __

## 5. Kết luận

Giả thuyết ở `evidence/hypothesis.md` (đếm lần 1, N = 22): **đạt hai ngưỡng đã viết trước** (59.1% từng đặt hộ ≥ 50%; 53.8% gặp sự cố ≥ 1/3), **nhưng lệch ở nguyên nhân**: sự cố hay gặp nhất là *thiếu món / phải đổi món* (6/13) và *vượt dự tính* (2/13); **không ai** chọn *nhầm món cho người ăn chay / dị ứng* (0/13), và chỉ 3/13 nhóm có người kiêng. Phần lớn đã dùng giỏ nhóm của app hoặc gửi menu vào chat (7/13 mỗi cách). Điều vẫn chưa biết: sự cố "thiếu / đổi món" do người đặt chọn sai hay do quán làm sai; mẫu còn nhỏ và là bạn cùng khoá — cần phỏng vấn ≥3 người để hỏi vì sao.

## Lịch hẹn (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| | | |

## 6. Nguồn khảo sát công khai bổ sung — phần Cấn Xuân Nghĩa

Báo cáo [nghiên cứu nguồn công khai](secondary-research.md) ghi rõ hai khảo sát do **ezCater** công bố năm **2023** và **2024**, mẫu người thường đặt đồ ăn cho nơi làm việc, vị trí trang và URL báo cáo gốc. Đây là số liệu bên ngoài, **không** phải khảo sát của nhóm và không cộng vào mẫu số của nhóm. Năm ví dụ công khai có trích dẫn và ngữ cảnh riêng; không phải người Aliba6 đã phỏng vấn.
