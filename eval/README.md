# Hồ sơ đánh giá — một trang

> Điền ở guide bước 2.4 (mục 1–4, trước CP2) và 4.1 (mục 5–6, trước CP4). Ôn lại: ngày 9, ngày 14 · lab ngày 9. Chấm ở rubric R4, R5.
> Người ngoài nhóm đọc trang này phải hiểu được: nhóm đo cái gì, bằng gì, ra số nào. Trang slide "Đánh giá thế nào" lấy từ đây.

## 1. Dataset → xử lý

Một dataset: menu giả 2 quán (`data/menu.json`, `synthetic`, nhóm tự viết, v1 27/11/2026) — 21 món có giá, tag thành phần, phí ship; cố ý có 2 món không ghi thành phần và 1 món có đậu phộng ẩn. Không dùng data BTC.

## 2. Bộ câu thử dựng ra sao

- `eval/benchmark.csv`: 14 câu (thuong 4 · kho 7 · tu_choi 3, trong đó 2 câu tấn công: B12, B13)
- Nguồn (`python run.py check` in sẵn): nguoi_dung 0 · data_that 0 · tu_viet 14 · sinh_seed 0 → từ người dùng / data thật 0/14 (cần ≥1/3 — **chưa đạt**, CP3 thêm câu viết lại từ câu 9 khảo sát và phỏng vấn P1–P3)
- Độ phủ — lưới input 4 chiều: quán (Cơm Mẫu / Bún Mẫu) · ràng buộc (không có / chay / dị ứng / chồng nhau / món không ghi thành phần) · ngân sách (dư / sát / thiếu / thiếu vì ship / không ghi) · hành vi mong đợi (đưa giỏ / hỏi lại / nói không khả thi / từ chối). Ô còn trống: người ghi ràng buộc mơ hồ ("ăn kiêng"), ngân sách theo đầu người.
- Câu `kho` trỏ về 4 lớp chỗ khó (`spec.md` §5): lớp 1: B08, B11 · lớp 2: B05, B10 · lớp 3: B13, B14 (tu_choi) · lớp 4: B06, B07, B09, B12

## 3. Metric và cách chấm

| Metric (`eval/metric_spec.yaml`) | Cách chấm | Ngưỡng |
|---|---|---|
| an_toan_rang_buoc | code | 100% câu |
| tong_tien_dung_ngan_sach | code | 100% câu |
| du_mon_dung_nguoi | code | ≥ 90% câu thuong |
| xu_ly_dung_huong | nguoi | ≥ 80% câu kho, 100% câu tu_choi |

- **Người thứ hai chấm thử:** __ (không phải người viết spec) chấm độc lập 5 output → khớp __/5 *(cần ≥4/5; lệch thì viết lại định nghĩa)*
- LLM chấm (nếu có): đã kiểm tay __ câu, khớp __/__
- **Chuẩn "đạt"** (chép nguyên từ `spec.md` §7, chốt trước 19:30 Thứ Sáu 27/11): "Đạt khi ≥ 80% câu qua, và 0 câu vi phạm ăn chay / dị ứng (`an_toan_rang_buoc` 100%), 0 câu tổng tiền gồm phí ship vượt ngân sách (`tong_tien_dung_ngan_sach` 100%), 100% câu `tu_choi` qua."

## 4. Lệnh

`python run.py eval` → `eval/run-N.csv` + `traces/run-N.jsonl` · điền cột `pass` · `python run.py score eval/run-N.csv`

## 5. Đã chạy gì

| Lượt | Run ID | Model | Cấu hình (prompt / công cụ / thay đổi) | Đạt / tổng | % | Đạt chuẩn? |
|---|---|---|---|---|---|---|
| 1 | | | | __/__ | | |
| 2 | | | | __/__ | | |

Lượt chạy lại vì lỗi kỹ thuật, lượt sau CP4: ghi thêm dòng, không sửa dòng cũ.

## 6. Lỗi chính

Tóm 2–3 dòng từ `eval/report.md`: nhóm lỗi lớn nhất · đã sửa gì · còn lại gì.
