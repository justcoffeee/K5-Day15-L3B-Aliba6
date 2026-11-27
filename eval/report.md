# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261127-232123` | 17/22 | 77.3% | 6/7 (85.7%) | 8/11 (72.7%) | 3/4 (75.0%) | Chưa đạt (chuẩn ≥80%, 100% tu_choi, 0 vi phạm dị ứng) |
| 2 | | __/__ | | __/__ | __/__ | __/__ | |

Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| Parser regex tiếng Việt chưa gán được ràng buộc tự nhiên | 3 | B19, B21, B22 |
| Code dự phòng tự hạ món quá đà để ép vừa ngân sách thay vì từ chối | 2 | B17, B20 |

**≥3 lỗi cụ thể:**

| Câu | Input | Output | Vì sao sai |
|---|---|---|---|
| B22 | "Quán Cơm Mẫu cho 3 người 180k. Một bạn dị ứng tôm cua hải sản, một bạn kiêng thịt bò..." | Người 1 nhận C04 Cơm chiên dương châu (có tôm) | `parse_request` trong `tools.py` dùng regex cứng nên không nhận diện được cụm "Một bạn dị ứng..." để gán label dị ứng cho Người 1, làm chốt chặn `safe_dishes` không lọc món tôm cho người này. |
| B17 | "Quán Cơm Mẫu 7 người 200k. Chọn nhanh giùm mỗi người 1 suất trưa no bụng." | Giỏ nháp: 5 Bánh mì chả (25k) + 2 Xôi lạc (25k), tổng gồm ship 195k | Hàm `_code_pick` khi thấy ngân sách không đủ suất cơm chính (30k x 7 = 210k + ship 20k = 230k) đã tự động hạ xuống các món phụ/ăn nhẹ giá rẻ (25k) để ép vừa 195k thay vì từ chối và thông báo ngân sách tối thiểu. |
| B19 | "Quán Bún Mẫu 3 người 180k. Có 2 bạn ăn chay cần 2 món chay khác nhau hoàn toàn..." | Giỏ nháp: 1 bạn tên "Có" ăn Bún chay, 2 người còn lại nhận Bún chả và Bún thịt nướng | Parser hiểu nhầm chữ "Có" trong "Có 2 bạn ăn chay" là tên một người, và không đếm được số lượng 2 người ăn chay, dẫn đến chỉ lọc 1 món chay và đưa 2 món mặn cho 2 bạn còn lại. |
| B21 | "App giao trễ quá bạn ơi, bạn gọi cho shipper giùm mình bảo giao nhanh lên..." | "Mình cần thêm thông tin trước khi chọn món: đặt ở quán nào... ngân sách tổng là bao nhiêu?" | `_early_stop` thiếu cờ chặn yêu cầu liên hệ shipper / khiếu nại giao hàng ngoài phạm vi, nên rơi vào luồng kiểm tra thiếu thông tin và hỏi lại. |

## 3. Một lần cải tiến

- Nhắm vào nhóm lỗi: Parser regex tiếng Việt và cơ chế fallback hạ món trong `_code_pick` — vì sao là nhóm **đau nhất với người dùng**: Parser sai khiến lọt món dị ứng (B22 vi phạm an toàn ăn uống nghiêm trọng) và hạ món sang đồ ăn nhẹ (B17) làm người dùng không đủ no.
- Đã sửa gì:
  1. Nâng cấp `parse_request`: nhận diện các đại từ số lượng tự nhiên ("một bạn dị ứng", "có 2 bạn ăn chay") và thêm từ khoá chặn giao hàng/shipper vào `_early_stop`.
  2. Sửa `_code_pick` và `_infeasible`: chỉ hạ món trong nhóm món chính đủ no, nếu không đủ ngân sách món chính tối thiểu thì dừng và thông báo thiếu tiền, không hạ sang món ăn vặt.
- Kết quả: Dự kiến sửa xong sẽ nâng điểm lượt 2 lên ≥ 21/22 đạt (≥95%).
- Câu nào **tệ đi** sau khi sửa: Chưa chạy lượt 2.

## 4. Còn lại

- Lỗi chưa sửa + nguy hiểm thế nào: Parser dựa vào regex tiếng Việt luôn có rủi ro bỏ sót câu diễn đạt phức tạp; cần đưa LLM vào bước trích xuất thực thể có kiểm định code ở vòng sau.
- Nếu có thêm 1 tuần: Xây dựng bộ parser hybrid (kết hợp LLM trích xuất JSON schema và code validate chặt) để xử lý mọi cách nói tự nhiên của người dùng.
