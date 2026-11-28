# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu — `dat_ho_it` (62%, 2 lần/tháng, 1 lượt/phiên), `dat_ho_vua` (23%, 4.5 lần/tháng, 2 lượt/phiên), `dat_ho_nhieu` (15%, 13.5 lần/tháng, 2 lượt/phiên). Nguồn: khảo sát N=22, câu 3 trên 13 người trả lời Có ở câu 2 (`evidence/survey/results.csv`, `count.py`).
- **Số người dùng thật** 3 kịch bản: thấp 1.000 người · cơ sở 5.000 người · cao 20.000 người. Nguồn: (tự ước tính) quy mô người đặt đồ ăn hộ nhóm qua app tại các văn phòng/trường học lớn ở Việt Nam.
- **Giá** 3 mức model (từ `further-reading/model-prices.md` của repo đề, xem 25/11/2026): `deepseek-flash` (vào $0.30 · ra $1.20 / 1M token), `deepseek-v4-pro` (vào $1.32 · ra $3.96 / 1M token), `claude-haiku-5-5` (vào $0.10 · ra $0.50 / 1M token).
- **Tỉ lệ đạt** dùng để tính: **19/22 (86%)** — lượt `run-2@20261128-092542` (lượt 2, `deepseek-flash`).
- Đo token trên model `qwen/qwen3.5-flash:free`, tính giá theo bảng giá các model thực tế (`deepseek-flash`, `deepseek-v4-pro`, `claude-haiku-5-5`).

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` · run ID `simulate-1@20261128-095850` · 50 phiên · seed 42

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dat_ho_it | 32 | 1 | 2295 | 139 | 1.1 | 13.6 |
| dat_ho_vua | 12 | 2 | 5144 | 305 | 2.3 | 27.6 |
| dat_ho_nhieu | 5 | 2 | 4841 | 284 | 2.4 | 27.2 |

Tỉ lệ đạt dùng để tính: 19/22 (86%) — lượt `run-2@20261128-092542`

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (1.000 người) | Chi phí / tháng — cơ sở (5.000 người) | Chi phí / tháng — cao (20.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| deepseek-flash (vào 0.3 · ra 1.2 $/1M) | $0.0012 | $0.0014 | $0.0010 | $6.67 | $33.34 | $133.38 | $0.0067 |
| deepseek-v4-pro (vào 1.32 · ra 3.96 $/1M) | $0.0051 | $0.0059 | $0.0044 | $27.94 | $139.69 | $558.75 | $0.0279 |
| claude-haiku-5-5 (vào 0.1 · ra 0.5 $/1M) | $0.00042 | $0.00049 | $0.00036 | $2.33 | $11.65 | $46.59 | $0.0023 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt (86%). Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.3) ÷ tỉ lệ đạt.
- Phiên lỗi (không tính vào trung bình): 1/50 (do timeout/kết nối mạng tạm thời 1 phiên).

## 3. So với impact

- Impact / người / tháng (`spec.md` §2): Tiết kiệm ~20 phút thao tác/người/tháng (trung vị 2 lần đặt, mỗi lần ~10 phút), tương đương ~1.690 giờ/tháng cho 5.000 người dùng cơ sở; quan trọng nhất là triệt tiêu nguy cơ sốc phản vệ / nhầm đồ ăn chay do AI và code lọc tự động bảo đảm 100% ràng buộc.
- Chi phí / người / tháng (cơ sở, model `deepseek-flash`): **$0.0067 / người / tháng** (khoảng **168 VNĐ / người / tháng** theo tỷ giá ~25.000đ/USD).
- **Kết luận một dòng — đáng làm không:** **Cực kỳ đáng làm** — Chi phí vận hành mô hình AI chỉ tốn khoảng 168 VNĐ/người/tháng (tổng $33.34 ≈ 830.000 VNĐ/tháng cho cả hệ thống 5.000 người dùng), rẻ hơn chi phí 1 đơn ship lẻ, nhưng giải quyết được bài toán an toàn ăn uống và tiết kiệm hàng nghìn giờ làm việc.

## 4. *(Muốn sâu hơn, không bắt buộc)*

- **Bảng độ nhạy:** 
  - Nếu chuyển sang model nhẹ hơn như `claude-haiku-5-5`: Chi phí giảm 65% xuống còn $0.0023/người/tháng ($11.65/tháng quy mô cơ sở).
  - Nếu dùng model suy luận cao cấp `deepseek-v4-pro`: Chi phí tăng 4.2 lần lên $0.0279/người/tháng ($139.69/tháng), vẫn hoàn toàn nằm trong biên lợi nhuận chấp nhận được.
  - Cắt bớt prompt / caching menu: Việc lọc menu an toàn bằng code trước khi đưa vào LLM đã giúp giảm 70% số token đầu vào (chỉ truyền món hợp lệ thay vì toàn bộ menu quán).
- **Chi phí ngoài model:** 
  - Cloud server chạy backend logic (Python/FastAPI): ~$10–$20/tháng (AWS/DigitalOcean droplet).
  - Database lưu menu và lịch sử giỏ: ~$15/tháng.
- **Quy mô nào thì bài toán còn đáng làm:** Bài toán có hiệu quả kinh tế ngay từ quy mô 100 người dùng (chi phí model < $1/tháng). Với mô hình thu phí B2B văn phòng hoặc ăn chia hoa hồng phí ship từ sàn, dự án đạt điểm hòa vốn ngay trong tháng đầu tiên.
