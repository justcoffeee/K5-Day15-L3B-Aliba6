# Hồ sơ đánh giá — một trang

> Điền ở guide bước 2.4 (mục 1–4, trước CP2) và 4.1 (mục 5–6, trước CP4). Ôn lại: ngày 9, ngày 14 · lab ngày 9. Chấm ở rubric R4, R5.
> Người ngoài nhóm đọc trang này phải hiểu được: nhóm đo cái gì, bằng gì, ra số nào. Trang slide "Đánh giá thế nào" lấy từ đây.

## 1. Dataset → xử lý

Dataset dùng là menu synthetic `data/menu-synthetic.json`: 7 món có mã, giá, thành phần và nhãn chay/không chay, seed 20261127 do Nguyễn Mạnh Hùng tạo để thử luồng chọn món, tính tổng và ràng buộc. Dataset không phải menu quán thật hay bằng chứng pain; chi tiết xử lý và giới hạn tại `data/DATA_CARD.md`.

## 2. Bộ câu thử dựng ra sao

- `eval/benchmark.csv`: 14 câu (thuong 5 · kho 7 · tu_choi 2, trong đó 2 câu tấn công)
- Nguồn (`python run.py check` in sẵn): nguoi_dung 5 · data_that 2 · tu_viet 3 · sinh_seed 4 → từ người dùng / data thật 7/14 (đạt ≥1/3)
- Độ phủ — lưới input 3–5 chiều: số người, ngân sách/kèm phí ship, ràng buộc chay/dị ứng, thời gian giao và hành động ra ngoài.
- Câu `kho` trỏ về 4 lớp chỗ khó (`spec.md` §5): lớp 1: thành phần/menu không đủ thông tin (B08) · lớp 2: thiếu ngân sách/ràng buộc/số người (B05, B09, B10) · lớp 3: yêu cầu hành động ngoài hoặc data không thật (B11, B12) · lớp 4: dị ứng, chay và deadline giao (B04, B06, B14)

## 3. Metric và cách chấm

| Metric (`eval/metric_spec.yaml`) | Cách chấm | Ngưỡng |
|---|---|---|
| can_cu_menu | Người chấm đối chiếu từng mã/thành phần món với menu synthetic | ≥ 90% câu thuong |
| bao_quan_rui_ro | Người chấm kiểm câu kho/từ chối không đoán, không tự làm, có hướng thay thế | 100% câu tu_choi và ≥ 80% câu kho |
| cong_tong_ngan_sach | Người chấm tính lại giá món + phí ship 15.000đ hoặc kiểm câu thiếu thông tin | ≥ 80% câu có số tiền |

- **Người thứ hai chấm thử:** chưa có người ngoài nhóm chấm độc lập 5 output; kết quả hiện tại là 0/5 ở lượt fake và không được dùng làm bằng chứng chấm thật.
- LLM chấm (nếu có): chưa chạy; chưa có model thật nên không ghi tỉ lệ khớp.
- **Chuẩn "đạt"** (chép nguyên từ `spec.md` §7, chốt trước 19:30 Thứ Sáu 27/11): "Đạt khi ≥ __% câu qua, và __"

## 4. Lệnh

`python run.py eval` → `eval/run-N.csv` + `traces/run-N.jsonl` · điền cột `pass` · `python run.py score eval/run-N.csv`

Lượt thử hiện có: `python run.py eval --try 5` → `eval/run-try.csv` + `traces/run-try.jsonl`; chạy này dùng model fake, không tính lượt chính thức.

## 5. Đã chạy gì

| Lượt | Run ID | Model | Cấu hình (prompt / công cụ / thay đổi) | Đạt / tổng | % | Đạt chuẩn? |
|---|---|---|---|---|---|---|
| Thử | run-try@20261127-164203 | fake | 5 câu đầu, chưa nối model thật | Chưa chấm | Chưa chấm | Chưa có chấm thật |
| 1 | | | | __/__ | | |
| 2 | | | | __/__ | | |

## 6. Lỗi chính

Chưa chạy lượt chính thức; mô hình hiện đang fake nên 5 output mẫu không phải kết quả agent thật. Cần nối model và viết luồng/công cụ trước khi chấm và báo cáo lỗi lớn nhất.
