# Chi phí khi dùng thật — dự toán từ simulate-2

## 1. Dữ liệu thực đo và phạm vi

- Theo lựa chọn của Nghĩa, **dùng lại 50 phiên đã có**, không gọi API và không tạo lượt `simulate-N` mới. Nguồn bất biến: `cost/simulate-2.csv`, `traces/simulate-2.jsonl`.
- Run ID `simulate-2@20261128-113825`; 50 phiên, 0 lỗi, seed 42; **124,723 token vào**, **86,354 token ra**, đo bằng **deepseek-flash**.
- Tỉ lệ đạt lấy đúng `eval/run-2.csv`, run ID `run-2@20261128-092542`: **19/22 = 86.363636…%**, cũng dùng deepseek-flash. Không làm tròn tỉ lệ thành 86% trước khi tính.
- Persona giữ cấu hình của lượt đo: ít 0.62 × 2 phiên/tháng × 1 lượt/phiên; vừa 0.23 × 4.5 × 2; nhiều 0.15 × 13.5 × 2. Nguồn tần suất là câu 3 CP2; số lượt/phiên vẫn là giả định. Không thay bằng số CP3 chưa chuẩn hoá.
- Cơ cấu 50 phiên thực đo: ít 32, vừa 13, nhiều 5. Chi phí mỗi phiên lấy trung bình 50 phiên; chi phí/tháng dùng trọng số persona cấu hình và tần suất riêng, không nhân đơn giản một mức chi phí chung với mọi người.

## 2. Quy mô có nguồn và ba kịch bản

[Vietdata, bài công bố 24/12/2023](https://www.vietdata.vn/post/ngành-giao-đồ-ăn-trực-tuyến-tại-việt-nam-baemin-rời-khỏi-thị-trường-sau-4-năm-thua-lỗ) nêu **hơn 12 triệu** người dùng nền tảng trung gian giao đồ ăn trong năm 2023. Dùng **12.000.000** làm mốc tròn tham chiếu, không gọi đây là thống kê mới nhất hoặc MAU.

**Cơ sở = 12.000.000 × 13/22 = 7.090.909 người**, làm tròn đến người. Tỉ lệ 13/22 lấy từ `evidence/survey/results.csv` của lượt CP2 theo yêu cầu; không lẫn với 20/34 của CP3.

Để tạo thấp/cao mà không gán tuỳ ý mức thâm nhập sản phẩm, dùng hai biên Wilson với z = 1.959963984540054 cho x=13, n=22: **0.3873481848** và **0.7674418380**. Công thức và phép làm tròn nằm trong `cost/reprice_existing.py`.

| Kịch bản | Tỉ lệ ngoại suy | Quy mô giả định |
|---|---:|---:|
| Thấp | 0.3873481848 | 4.648.178 |
| Cơ sở | 13/22 | 7.090.909 |
| Cao | 0.7674418380 | 9.209.302 |

**Cách hiểu:** đây là ba mức thử tải chi phí cho thị trường tiềm năng, với giả định mọi người trong quy mô ngoại suy đều dùng sản phẩm mỗi tháng. Không phải khách hàng thực tế, dự báo tăng trưởng hoặc cam kết đạt quy mô này. Mẫu 22 người là mẫu thuận tiện và khác tập người dùng app trong nguồn thị trường; biên Wilson chỉ minh hoạ độ nhạy do mẫu nhỏ, **không phải khoảng tin cậy đại diện cho Việt Nam**. Nguồn thị trường là năm 2023; không tự ngoại suy tăng trưởng tới 2026. Chưa áp tỉ lệ nhận dùng sản phẩm. Khi chỉ có U khách hàng hoạt động, chi phí/tháng = U × chi phí/người/tháng bên dưới.

## 3. Giá và công thức

Giá kiểm ngày 28/11/2026 từ [DeepSeek API Docs](https://api-docs.deepseek.com/quick_start/pricing/), USD/1 triệu token:

| Model | Vào, cache miss, peak | Ra, peak |
|---|---:|---:|
| deepseek-flash | 0.30 | 1.20 |
| deepseek-v4-pro | 1.32 | 3.96 |

Dùng giá peak/cache-miss làm dự toán thận trọng. Peak áp dụng thứ Hai–thứ Sáu vào 08:00–11:00 và 13:00–17:00 giờ Việt Nam, trừ ngày lễ Trung Quốc; cuối tuần là off-peak. Off-peak bằng nửa giá peak; token cache-hit có giá riêng thấp hơn. Bảng này không phải hoá đơn thực trả của lượt chạy thứ Bảy.

- Chi phí phiên i = (token vào_i × giá vào + token ra_i × giá ra) / 1.000.000.
- **Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ (19/22).**
- Chi phí/người/tháng = Σ [share_persona × uses_per_month_persona × chi phí phiên trung bình của persona].
- Chi phí/tháng ở kịch bản s = users_s × chi phí/người/tháng.

Tỉ lệ đạt đo theo **câu thử**, trong khi phiên có thể có nhiều lượt; vì vậy chi phí/task ở đây là chỉ số quy đổi theo yêu cầu, chưa phải tỉ lệ thành công đo trực tiếp ở cấp phiên.

## 4. Kết quả — ba kịch bản × hai mức model

| Model | Chi phí / phiên | Chi phí / task thành công | Chi phí / người / tháng |
|---|---:|---:|---:|
| deepseek-flash | $0.00282083 | $0.00326623 | $0.01511710 |
| deepseek-v4-pro | $0.01013192 | $0.01173170 | $0.05430762 |

| Kịch bản | Người dùng giả định mỗi tháng | Model | Chi phí model / tháng |
|---|---:|---|---:|
| Thấp | 4.648.178 | deepseek-flash | $70,266.96 |
| Thấp | 4.648.178 | deepseek-v4-pro | $252,431.51 |
| Cơ sở | 7.090.909 | deepseek-flash | $107,193.96 |
| Cơ sở | 7.090.909 | deepseek-v4-pro | $385,090.43 |
| Cao | 9.209.302 | deepseek-flash | $139,217.92 |
| Cao | 9.209.302 | deepseek-v4-pro | $500,135.32 |

**deepseek-v4-pro chỉ là quy đổi giá:** token vẫn đo trên flash và tạm giữ cùng tỉ lệ 19/22 để so sánh. Chưa chạy eval trên pro, chưa xác nhận pro có cùng tỉ lệ đạt hoặc số token. Bảng hai model không phải hai phép đo độc lập.

Bảng do `python cost/reprice_existing.py` sinh số tại `cost/reprice-simulate-2.json`; bảng khung tương ứng tại `cost/reprice-simulate-2.md`. Giữ nguyên `simulate-2.csv` và `simulate-2-summary.md` cũ, nên các tổng tháng ở bản cũ vẫn phản ánh quy mô cũ.

## 5. So với impact và kết luận

Theo §2, mức tham chiếu **khoảng 20 phút/người/tháng** là thời gian đang tốn, từ khoảng 2 đơn × khoảng 10 phút; phần số phút là tự ước tính, **chưa đo thời gian sản phẩm tiết kiệm**. Chi phí token/người/tháng lần lượt **$0.01512** và **$0.05431**. Không quy đổi phút thành tiền khi chưa có nguồn đơn giá thời gian.

**Kết luận:** chi phí token trên mỗi người thấp so với khối lượng công việc tham chiếu, nhưng quyết định triển khai còn phụ thuộc mức tiết kiệm thật, an toàn và khả năng có khách hàng hoạt động; quy mô ngoại suy toàn thị trường chỉ dùng thử tải ngân sách.

Chưa gồm máy chủ, lưu trữ, vận hành, thuế, phí thanh toán hay chi phí duy trì dữ liệu thành phần món. Không có tỷ giá được chốt nên giữ USD.

## 6. Kiểm tra và chạy lại

```text
python cost/reprice_existing.py
```

Lệnh trên chỉ đọc kết quả cũ, kiểm ≥50 phiên, token theo model, cùng model với run-2, tỉ lệ đạt và SHA-256 của CSV/trace trước–sau; không gọi API. Các tệp gốc và băm được ghi trong JSON.

Nếu sau này cần đo lượt mới và đã cấu hình API trên máy:

```text
python run.py simulate --rate-from eval/run-2.csv
```

Lệnh đó phải dùng `MODEL_NAME=deepseek-flash`, không thay thế bằng việc sửa CSV cũ.
