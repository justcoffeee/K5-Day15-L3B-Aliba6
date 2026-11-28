# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu — `dat_ho_it` (62%, 2 lần/tháng, 1 lượt/phiên), `dat_ho_vua` (23%, 4.5 lần/tháng, 2 lượt/phiên), `dat_ho_nhieu` (15%, 13.5 lần/tháng, 2 lượt/phiên). Nguồn: khảo sát lượt CP2 (N=22), câu 3 trên 13 người trả lời Có ở câu 2 (`evidence/survey/results.csv`, `count.py`); số lượt / phiên *(tự ước tính)*. Lượt CP3 (20 người) chưa chuẩn hoá câu 3 nên chưa dùng.
- **Số người dùng thật** 3 kịch bản: thấp 1.000 · cơ sở 5.000 · cao 20.000 người / tháng — ***(tự ước tính)*, chưa có nguồn công khai có link**. Đây là chỗ yếu nhất của bảng: mọi con số "/ tháng" tỉ lệ thuận với số này.
- **Giá** (USD / 1 triệu token, chép từ `further-reading/model-prices.md` của repo đề, xem 25/11/2026): `deepseek-flash` vào 0.30 · ra 1.20 (giá cao điểm) — **model nhóm dùng**; `deepseek-v4-pro` vào 1.32 · ra 3.96 (mức model mạnh); `claude-haiku-5-5` vào 0.10 · ra 0.50 (tham khảo).
- **Tỉ lệ đạt** dùng để tính: **19/22 (86%)** — lượt `run-2@20261128-092542`, model `deepseek-flash`.
- **Đo token trên `deepseek-flash`** — cùng model với lượt 2. Giá của `deepseek-v4-pro` và `claude-haiku-5-5` tính trên token đo bằng `deepseek-flash`; model khác bộ tách token nên số thật có thể lệch.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-2.csv` · run ID `simulate-2@20261128-113825` · 50 phiên · seed 42 · 0 phiên lỗi · chép nguyên từ `cost/simulate-2-summary.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dat_ho_it | 32 | 1 | 1829 | 1274 | 0.8 | 13.5 |
| dat_ho_vua | 13 | 2 | 3707 | 2551 | 1.8 | 26.9 |
| dat_ho_nhieu | 5 | 2 | 3602 | 2483 | 1.8 | 26.8 |

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (1.000 người) | Chi phí / tháng — cơ sở (5.000 người) | Chi phí / tháng — cao (20.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| **deepseek-flash** (vào 0.3 · ra 1.2 $/1M) | $0.0028 | **$0.0033** | $0.0024 | $15.12 | **$75.59** | $302.34 | **$0.0151** |
| deepseek-v4-pro (vào 1.32 · ra 3.96 $/1M) | $0.0101 | $0.0117 | $0.0086 | $54.31 | $271.54 | $1,086.15 | $0.0543 |
| claude-haiku-5-5 (vào 0.1 · ra 0.5 $/1M) | $0.0011 | $0.0013 | $0.00095 | $5.96 | $29.82 | $119.28 | $0.0060 |

- **Chi phí / task thành công** = chi phí / phiên ÷ tỉ lệ đạt (86%) → **$0.0033 với `deepseek-flash`** (kịch bản cơ sở). Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.4) ÷ tỉ lệ đạt.
- Một phiên trung bình gọi model dưới 1 lần (0.8 với người đặt ít): các câu thiếu thông tin, ngân sách không đủ hoặc cấp cứu dừng bằng code, không gọi model.
- Lượt mô phỏng trước `simulate-1@20261128-095850` (`cost/simulate-1.csv`) đo token trên `qwen/qwen3.5-flash:free` — khác model lượt 2 nên **không dùng**; giữ file để không xoá lượt đã chạy. Token ra / phiên của `deepseek-flash` cao hơn qwen nhiều (1274 so với 139 ở `dat_ho_it`), nên chi phí tăng khoảng 2,3 lần so với bảng cũ.

## 3. So với impact

- **Impact / người đặt hộ / tháng** (`spec.md` §2): ~20 phút **đang tốn** để gom món (trung vị 2 lần / tháng × ~10 phút / lần, *tự ước tính* từ khoảng thời gian câu 7). Đây là thời gian đang tốn, chưa đo được sản phẩm tiết kiệm bao nhiêu trong số đó; sự cố (9/19 người gặp ≥1 lần) chưa quy ra tiền.
- **Chi phí model / người / tháng** (cơ sở, `deepseek-flash`): **$0.0151**. Kể cả model mạnh `deepseek-v4-pro`: $0.0543.
- **Kết luận một dòng — đáng làm không:** **Chi phí model không phải điểm nghẽn** — dưới 2 cent / người / tháng, nhỏ so với ~20 phút gom món mỗi tháng kể cả khi sản phẩm chỉ bớt được một phần nhỏ thời gian đó. Câu hỏi còn mở là sản phẩm có thật sự bớt được thời gian và lỗi không (chưa có người dùng thật thử trên menu thật) và quy mô người dùng thật (đang *tự ước tính*).

## 4. *(Muốn sâu hơn, không bắt buộc)*

- **Độ nhạy theo model** (từ bảng trên, cùng token đo bằng `deepseek-flash`): `claude-haiku-5-5` rẻ hơn `deepseek-flash` khoảng 2,5 lần ($0.0060 so với $0.0151 / người / tháng); `deepseek-v4-pro` đắt hơn khoảng 3,6 lần ($0.0543).
- **Độ nhạy theo số người dùng:** chi phí / tháng tỉ lệ thuận với số người dùng — gấp 4 lần người dùng (cơ sở → cao) thì gấp 4 lần chi phí; chi phí / người / tháng không đổi.
- **Chi phí ngoài model** (máy chủ, lưu menu, người cập nhật thành phần món): chưa ước tính — nhóm chưa có số có nguồn. Việc cập nhật thành phần món cho từng quán có thể tốn hơn chi phí model, vì an toàn dị ứng phụ thuộc menu ghi đúng.
