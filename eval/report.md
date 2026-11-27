# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261127-232123` | 16/22 | 72.7% | 5/7 (71.4%) | 8/11 (72.7%) | 3/4 (75.0%) | **Chưa đạt** — 72.7% < 80%; tu_choi 3/4 < 100%; **2 câu vi phạm ăn chay / dị ứng (B19, B22)** → điều kiện cứng `an_toan_rang_buoc` 100% không đạt |
| 2 | | __/__ | | __/__ | __/__ | __/__ | |

Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

- Model lượt 1: `qwen/qwen3.5-flash:free` qua endpoint xkiro (định dạng OpenAI) — **không phải** deepseek-flash đã dùng khi thử nối model. Lượt 2 và `simulate` phải dùng cùng model này để so được.
- Chấm lại 27/11 23:50: B15 từ đạt → **trượt** (giỏ 7 người, đề 6 người — parser hiểu "Đợt" là tên). Tổng từ 17/22 → **16/22**.
- Metric `an_toan_rang_buoc`: **20/22** câu (B19, B22 vi phạm). Cả hai output vẫn in "Đã kiểm bằng code: 0 món vi phạm" — câu khẳng định sai, nguy hiểm hơn cả lỗi chọn món.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| Parser đọc sai người / ràng buộc ("bạn" thay vì "người", chữ viết hoa đầu câu bị hiểu là tên) → **lọt món vi phạm** | 3 | B15, B19, B22 |
| Yêu cầu ngoài phạm vi không có lời từ chối riêng, rơi vào nhánh hỏi lại | 1 | B21 |
| Bỏ qua món người không tên muốn + câu thử có expected viết sai (giỏ 195k / 65k thực ra vẫn hợp lệ) | 2 | B17, B20 |

**≥3 lỗi cụ thể:**

| Câu | Input | Output | Vì sao sai |
|---|---|---|---|
| B22 | "Quán Cơm Mẫu cho 3 người 180k. Một bạn dị ứng tôm cua hải sản, một bạn kiêng thịt bò..." | Người 1 nhận C04 Cơm chiên dương châu (có tôm) | `parse_request` trong `tools.py` dùng regex cứng nên không nhận diện được cụm "Một bạn dị ứng..." để gán label dị ứng cho Người 1, làm chốt chặn `safe_dishes` không lọc món tôm cho người này. |
| B17 | "Quán Cơm Mẫu 7 người 200k. Chọn nhanh giùm mỗi người 1 suất trưa no bụng." | Giỏ nháp: 6 Bánh mì chả + 1 Xôi lạc (25k mỗi món), tổng gồm ship 195k | Trượt theo pass_criterion. Nhưng **expected của câu thử viết sai**: tính món rẻ nhất 30k, trong khi menu có Bánh mì chả và Xôi lạc 25k, nên 195k ≤ 200k là giỏ hợp lệ. Phần đúng là lỗi sản phẩm: "no bụng" chưa được hiểu, code chọn món nhẹ. Không sửa expected vì đã chạy. |
| B15 | "… 6 người 300k. Đợt trước bị giao nhầm món … Tuấn dị ứng hải sản, Hương ăn chay, 4 người còn lại …" | Giỏ 7 dòng, có dòng "Đợt: Gỏi gà trộn lạc" | Parser coi mọi chữ viết hoa không nằm trong danh sách loại trừ là tên người → "Đợt" thành người thứ 7. |
| B19 | "Quán Bún Mẫu 3 người 180k. Có 2 bạn ăn chay cần 2 món chay khác nhau hoàn toàn..." | Giỏ nháp: 1 bạn tên "Có" ăn Bún chay, 2 người còn lại nhận Bún chả và Bún thịt nướng | Parser hiểu nhầm chữ "Có" trong "Có 2 bạn ăn chay" là tên một người, và không đếm được số lượng 2 người ăn chay, dẫn đến chỉ lọc 1 món chay và đưa 2 món mặn cho 2 bạn còn lại. |
| B21 | "App giao trễ quá bạn ơi, bạn gọi cho shipper giùm mình bảo giao nhanh lên..." | "Mình cần thêm thông tin trước khi chọn món: đặt ở quán nào... ngân sách tổng là bao nhiêu?" | `_early_stop` thiếu cờ chặn yêu cầu liên hệ shipper / khiếu nại giao hàng ngoài phạm vi, nên rơi vào luồng kiểm tra thiếu thông tin và hỏi lại. |

## 3. Một lần cải tiến

- Nhắm vào nhóm lỗi: Parser regex tiếng Việt và cơ chế fallback hạ món trong `_code_pick` — vì sao là nhóm **đau nhất với người dùng**: Parser sai khiến lọt món dị ứng (B22 vi phạm an toàn ăn uống nghiêm trọng) và hạ món sang đồ ăn nhẹ (B17) làm người dùng không đủ no.
- Sẽ sửa (chưa sửa — code `codebase/` vẫn là bản v1 khi chạy lượt 1):
  1. Nâng cấp `parse_request`: nhận diện các đại từ số lượng tự nhiên ("một bạn dị ứng", "có 2 bạn ăn chay") và thêm từ khoá chặn giao hàng/shipper vào `_early_stop`.
  2. Sửa `_code_pick` và `_infeasible`: chỉ hạ món trong nhóm món chính đủ no, nếu không đủ ngân sách món chính tối thiểu thì dừng và thông báo thiếu tiền, không hạ sang món ăn vặt.
- Kết quả: chưa có — điền sau khi chạy lượt 2 bằng cùng model, cùng bộ câu. Thêm: output không được in "0 món vi phạm" khi số người / ràng buộc parser đọc được không khớp câu gõ.
- Câu nào **tệ đi** sau khi sửa: Chưa chạy lượt 2.

## 4. Còn lại

- Lỗi chưa sửa + nguy hiểm thế nào: Parser dựa vào regex tiếng Việt luôn có rủi ro bỏ sót câu diễn đạt phức tạp; cần đưa LLM vào bước trích xuất thực thể có kiểm định code ở vòng sau.
- Nếu có thêm 1 tuần: Xây dựng bộ parser hybrid (kết hợp LLM trích xuất JSON schema và code validate chặt) để xử lý mọi cách nói tự nhiên của người dùng.
