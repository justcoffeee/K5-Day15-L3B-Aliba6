# Tóm tắt mô phỏng simulate-2@20261128-113825

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dat_ho_it | 32 | 1 | 1829 | 1274 | 0.8 | 13.5 |
| dat_ho_vua | 13 | 2 | 3707 | 2551 | 1.8 | 26.9 |
| dat_ho_nhieu | 5 | 2 | 3602 | 2483 | 1.8 | 26.8 |

Tỉ lệ đạt dùng để tính: 19/22 (86%) — lượt run-2@20261128-092542

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (1.000 người) | Chi phí / tháng — cơ sở (5.000 người) | Chi phí / tháng — cao (20.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| deepseek-flash (vào 0.3 · ra 1.2 $/1M) | $0.0028 | $0.0033 | $0.0024 | $15.12 | $75.59 | $302.34 | $0.0151 |
| deepseek-v4-pro (vào 1.32 · ra 3.96 $/1M) | $0.0101 | $0.0117 | $0.0086 | $54.31 | $271.54 | $1,086.15 | $0.0543 |
| claude-haiku-5-5 (vào 0.1 · ra 0.5 $/1M) | $0.0011 | $0.0013 | $0.00095 | $5.96 | $29.82 | $119.28 | $0.0060 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.4) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: deepseek-flash. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
