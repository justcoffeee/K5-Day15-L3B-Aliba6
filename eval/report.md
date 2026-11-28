# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261127-232123` | 16/22 | 72.7% | 5/7 (71.4%) | 8/11 (72.7%) | 3/4 (75.0%) | **Chưa đạt** — 72.7% < 80%; tu_choi 3/4 < 100%; **2 câu vi phạm ăn chay / dị ứng (B19, B22)** → điều kiện cứng `an_toan_rang_buoc` 100% không đạt |
| 2 | `run-2@20261128-092542` | 19/22 | 86.4% | 7/7 (100%) | 9/11 (81.8%) | 3/4 (75.0%) | **Chưa đạt** — Đạt 86.4% ≥ 80%, an toàn 0 vi phạm (100% đạt), ngân sách 0 vượt (100% đạt), nhưng tu_choi 3/4 < 100% (câu B21 trượt) |

Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

- Model lượt 1: `qwen/qwen3.5-flash:free` qua endpoint xkiro (định dạng OpenAI).
- Model lượt 2: `deepseek-flash` qua DeepSeek API. **Lượt 2 đổi cả code (sửa parser) lẫn model (qwen → deepseek-flash)**, nên không tách được bao nhiêu phần cải thiện do code, bao nhiêu do model. Phần an toàn (B19, B22) thì chắc do code: chạy bản sửa với model bị chặn (giỏ do code tự chọn) đã lọc đúng.
- Chấm lượt 2: Huy chấm cột `pass` (nháp Claude Code, Huy duyệt) và đẩy lên lúc 09:29; Tùng rà lại cả 22 dòng lúc 09:52 và đồng ý 22/22. Metric người chấm `xu_ly_dung_huong` chỉ áp cho 15 câu (11 `kho` + 4 `tu_choi`). **Lần rà này không tính là chấm độc lập** vì Tùng đã thấy điểm của Huy trên repo; lần chấm độc lập duy nhất của nhóm là bản chấm thử 5 câu ở CP2 (khớp 5/5, `eval/cham-thu-5.md`).
- Chấm lại lượt 1 (27/11 23:50): B15 từ đạt → **trượt** (giỏ 7 người, đề 6 người — parser hiểu "Đợt" là tên). Tổng từ 17/22 → **16/22**.
- Metric `an_toan_rang_buoc`: Lượt 1 bị 20/22 câu (B19, B22 vi phạm). Lượt 2 đạt **22/22 câu (100% an toàn, 0 vi phạm)**.

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

- **Nhắm vào nhóm lỗi:** Parser regex tiếng Việt đọc sai người và ràng buộc (B15, B19, B22, B20) — vì sao là nhóm **đau nhất với người dùng**: Parser sai khiến lọt món vi phạm dị ứng (B22) và ăn chay (B19), gây hại sức khoẻ không đảo ngược được.
- **Đã sửa gì (ở commit `810e98e`):**
  1. *Nhận tên người (`parse_request` trong `tools.py`):* chữ viết hoa **ở đầu câu** chỉ được coi là tên khi từ ngay sau nó nói về việc ăn của một người (`NAME_NEXT`: "ăn", "dị", "kiêng", "muốn"…) hoặc ngay sau là dấu phẩy. Không thêm từ nào vào danh sách loại trừ — "Đợt trước…", "Có 2 bạn…", "App giao…" tự bị loại theo luật này (B15, B19, B21).
  2. *Người không tên:* nhận "N bạn …" như "N người …" (`COUNT_RE`), nên "một bạn dị ứng tôm cua hải sản", "2 bạn ăn chay" được gán đúng ràng buộc (B22, B19).
  3. *Ràng buộc không rõ → hỏi lại:* mọi chỗ ghi "ăn chay / dị ứng / kiêng / không ăn" không gắn được vào ai, hoặc thành phần lạ (vd "dị ứng mè"), thì dừng và hỏi lại, không lập giỏ; số tên nhiều hơn số người → hỏi lại thay vì tự lập giỏ (`agent.py` `_early_stop`).
  4. *Món muốn của người không tên:* đọc "1 bạn ăn bún chả", "2 bát bún chả"; khi món muốn + ship vượt ngân sách thì nói rõ thiếu bao nhiêu (B20: 90k + 25k = 115k > 95k) rồi đổi món cho vừa.
  5. *Câu khẳng định an toàn (`_format`):* bỏ câu "0 món vi phạm" chung chung, chỉ ghi đã kiểm theo đúng ràng buộc in cạnh từng người, kèm nhắc sửa yêu cầu nếu thiếu.
- **Kết quả:**
  - Nhóm lỗi parser sai người / ràng buộc: **3/3 câu đã khắc phục được lỗi an toàn**.
  - Metric `an_toan_rang_buoc`: **0 câu vi phạm (từ 20/22 → 22/22 đạt 100%)**.
  - Điểm tổng: **từ 16/22 (72.7%) → 19/22 (86.4%)**, tăng **13,7 điểm %**. Lưu ý: đổi cả model, xem mục 1.
- **Câu nào tệ đi sau khi sửa:** Không có câu nào tệ đi. Mọi câu đạt ở lượt 1 vẫn giữ nguyên kết quả đạt ở lượt 2.

## 4. Còn lại

- **Lỗi chưa sửa + nguy hiểm thế nào:**
  - *B17 (kho):* Hệ thống vẫn chọn món ăn nhẹ (xôi lạc) để vừa ngân sách 200k cho 7 người thay vì từ chối khi không đủ tiền suất chính no bụng.
  - *B19 (kho):* Đã hết vi phạm an toàn (cả 2 bạn ăn chay đều nhận Bún chay B04 an toàn), nhưng chưa thông báo Quán Bún Mẫu chỉ có 1 món chay và chưa đề xuất đổi quán.
  - *B21 (tu_choi):* Yêu cầu liên hệ shipper vẫn rơi vào nhánh hỏi lại thiếu thông tin quán/ngân sách thay vì có câu từ chối riêng cho việc ngoài phạm vi.
  - *Đánh giá rủi ro:* Cả 3 lỗi còn lại đều không gây hại sức khoẻ (0 vi phạm dị ứng/chay) và không vượt tiền (0 vượt ngân sách), chủ yếu ảnh hưởng đến độ tiện lợi của người đặt.
- **Nếu có thêm 1 tuần:**
  - Xây dựng bộ parser hybrid (kết hợp LLM trích xuất JSON schema và code validate chặt) để xử lý triệt để mọi cách nói tự nhiên.
  - Thêm intent classification cho các yêu cầu ngoài phạm vi (khiếu nại shipper, đổi trả, y tế).
  - Tự động phát hiện quán không đủ món đa dạng theo ràng buộc và đề xuất đổi quán ngay từ bước kiểm tra khả thi.
