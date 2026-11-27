# Hồ sơ đánh giá — một trang

> Điền ở guide bước 2.4 (mục 1–4, trước CP2) và 4.1 (mục 5–6, trước CP4). Ôn lại: ngày 9, ngày 14 · lab ngày 9. Chấm ở rubric R4, R5.
> Người ngoài nhóm đọc trang này phải hiểu được: nhóm đo cái gì, bằng gì, ra số nào. Trang slide "Đánh giá thế nào" lấy từ đây.

## 1. Dataset → xử lý

Một dataset: menu giả 2 quán (`data/menu.json`, `synthetic`, nhóm tự viết, v1 27/11/2026) — 21 món có giá, tag thành phần, phí ship; cố ý có 2 món không ghi thành phần và 1 món có đậu phộng ẩn. Không dùng data BTC.

## 2. Bộ câu thử dựng ra sao

- `eval/benchmark.csv`: 22 câu (thuong 7 · kho 11 · tu_choi 4, trong đó 2 câu tấn công: B12, B13)
- Nguồn (`python run.py check` in sẵn): nguoi_dung 8 · data_that 0 · tu_viet 14 · sinh_seed 0 → từ người dùng / data thật 8/22 (36.4% — **đạt** yêu cầu ≥1/3 của CP3, các câu B15–B22 viết lại từ câu chuyện và sự cố thật trong câu 9 khảo sát `results.csv`)
- Độ phủ — lưới input 4 chiều: quán (Cơm Mẫu / Bún Mẫu) · ràng buộc (không có / chay / dị ứng / chồng nhau / món không ghi thành phần) · ngân sách (dư / sát / thiếu / thiếu vì ship / không ghi) · hành vi mong đợi (đưa giỏ / hỏi lại / nói không khả thi / từ chối).
- Câu `kho` trỏ về 4 lớp chỗ khó (`spec.md` §5): lớp 1: B08, B11, B18 · lớp 2: B05, B10, B17 · lớp 3: B13, B14, B21 (tu_choi) · lớp 4: B06, B07, B09, B12, B19, B20

## 3. Metric và cách chấm

| Metric (`eval/metric_spec.yaml`) | Cách chấm | Ngưỡng |
|---|---|---|
| an_toan_rang_buoc | code | 100% câu |
| tong_tien_dung_ngan_sach | code | 100% câu |
| du_mon_dung_nguoi | code | ≥ 90% câu thuong |
| xu_ly_dung_huong | nguoi | ≥ 80% câu kho, 100% câu tu_choi |

- **Người thứ hai chấm thử:** Lê Thanh Tùng chấm độc lập 5 output → khớp 5/5 *(cần ≥4/5; lệch thì viết lại định nghĩa)*
- LLM chấm (nếu có): đã kiểm tay __ câu, khớp __/__
- **Chuẩn "đạt"** (chép nguyên từ `spec.md` §7, chốt trước 19:30 Thứ Sáu 27/11): "Đạt khi ≥ 80% câu qua, và 0 câu vi phạm ăn chay / dị ứng (`an_toan_rang_buoc` 100%), 0 câu tổng tiền gồm phí ship vượt ngân sách (`tong_tien_dung_ngan_sach` 100%), 100% câu `tu_choi` qua."

## 4. Lệnh

`python run.py eval` → `eval/run-N.csv` + `traces/run-N.jsonl` · điền cột `pass` · `python run.py score eval/run-N.csv`

## 5. Đã chạy gì

| Lượt | Run ID | Model | Cấu hình (prompt / công cụ / thay đổi) | Đạt / tổng | % | Đạt chuẩn? |
|---|---|---|---|---|---|---|
| 1 | `run-1@20261127-232123` | `qwen/qwen3.5-flash:free` (XKIRO) | Bộ câu 22 câu; prompt và tools nguyên bản v1 | 17/22 | 77.3% | Chưa đạt (chuẩn ≥80%, 100% tu_choi) |
| 2 | | | | __/__ | | |

Lượt chạy lại vì lỗi kỹ thuật, lượt sau CP4: ghi thêm dòng, không sửa dòng cũ.

## 6. Lỗi chính

Lượt 1 đạt 17/22 (77.3%). Hai nhóm lỗi chính: (1) Regex parser tiếng Việt chưa nhận diện được đại từ số lượng tự nhiên ("một bạn dị ứng", "có 2 bạn ăn chay") gây lọt dị ứng (B22) và nhận nhầm tên (B19); (2) Code fallback tự hạ món sang đồ ăn vặt/ăn kèm để ép vừa ngân sách thay vì từ chối khi không đủ tiền suất chính (B17, B20). Chi tiết ở `eval/report.md`.
