# Tóm tắt mô phỏng simulate-1@20261128-095850

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dat_ho_it | 32 | 1 | 2295 | 139 | 1.1 | 13.6 |
| dat_ho_vua | 12 | 2 | 5144 | 305 | 2.3 | 27.6 |
| dat_ho_nhieu | 5 | 2 | 4841 | 284 | 2.4 | 27.2 |

Tỉ lệ đạt dùng để tính: 19/22 (86%) — lượt run-2@20261128-092542

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from). ⚠️ Lượt này chạy bằng deepseek-flash, mô phỏng đo trên qwen/qwen3.5-flash:free — khác model.

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (1.000 người) | Chi phí / tháng — cơ sở (5.000 người) | Chi phí / tháng — cao (20.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| deepseek-flash (vào 0.3 · ra 1.2 $/1M) | $0.0012 | $0.0014 | $0.0010 | $6.67 | $33.34 | $133.38 | $0.0067 |
| deepseek-v4-pro (vào 1.32 · ra 3.96 $/1M) | $0.0051 | $0.0059 | $0.0044 | $27.94 | $139.69 | $558.75 | $0.0279 |
| claude-haiku-5-5 (vào 0.1 · ra 0.5 $/1M) | $0.00042 | $0.00049 | $0.00036 | $2.33 | $11.65 | $46.59 | $0.0023 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.3) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: qwen/qwen3.5-flash:free. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 1/50.
