# Người dùng thử *(bonus)*

> Điền ở guide bước 4.3 — 2–3 người ngoài nhóm, ~10 phút / người, theo 5 nhịp: làm quen · bối cảnh · giao việc · quan sát · hỏi sau. Ôn lại: ngày 5, ngày 13. Chấm ở rubric Bonus.
> Không ghi tên: ghi vai. Hành vi quan sát được nặng hơn lời nói; toàn lời khen = phiên chưa đạt, giao việc khó hơn.
> Người dùng thử **không thay được** bằng chứng pain ở `evidence/`.

| Người thử (vai) | Việc giao (theo kết quả, không theo nút) | Quan sát (làm gì đầu tiên, chỗ do dự, chỗ hiểu sai) | Trích nguyên văn | Mức nghiêm trọng (cao / vừa / thấp) |
|---|---|---|---|---|
| Học viên 1 (Lớp L3B) | Lập giỏ trưa ở Quán Cơm Mẫu cho 4 người, tổng 220k, có 1 người ăn chay và 1 người dị ứng đậu phộng | Gõ: *"lập giỏ trưa ở Quán Cơm Mẫu cho 4 người, tổng 220k, có 1 người ăn chay và 1 người dị ứng đậu phộng"*. Trả giỏ đúng món, đúng ràng buộc. *(Trong lúc chạy thử thực tế với câu gõ liền không dấu phẩy `1 người ăn chay 1 người dị ứng đậu phộng`, phát hiện parser gộp nhầm 2 ràng buộc vào 1 người → đã sửa ngay trong `tools.py`.)* | "món ok đúng với yêu cầu" | Thấp *(Cao khi gõ không dấu phẩy trước lúc sửa)* |
| Học viên 2 (Lớp L3B) | Đặt món quán bún cho 3 người, 150k, 1 người vừa ăn chay vừa dị ứng đậu phộng | Lần đầu gõ tắt: *"bún, 3 người, 150k, 1 người vừa ăn chay vừa dị ứng đậu phộng"*. Hệ thống không nhận ra chữ "bún" là `Quán Bún Mẫu` nên hỏi lại quán chứ chưa trả món. Người thử hiểu, gõ lại đầy đủ tên quán thì ra giỏ đúng. | *(chưa ghi câu nhận xét nguyên văn; người thử đặt lại nói rõ tên quán thì được)* | Vừa |
| Học viên 3 (Lớp L3B) | Đặt giỏ ở Quán Cơm Mẫu cho 3 người, ngân sách 150k (không chỉ định món) | Gõ: *"quán cơm mẫu ,3 người, ngân sách 150k"*. Hệ thống tự chọn đủ món phù hợp ngân sách. | "ok lúc k biết ăn gì sẽ tự chọn món" | Thấp |

Câu hỏi sau: *"Nếu mai không được dùng nữa, bạn thấy: rất tiếc / hơi tiếc / không sao?"* → 1 / 2 / 0 *(rất tiếc: 1 · hơi tiếc: 2 · không sao: 0)*

## Tổng hợp

- Chủ đề lặp nhiều nhất: Người dùng có thói quen gõ tắt hoặc viết liền không dấu phẩy (vd gõ `"bún"` thay vì `"Quán Bún Mẫu"`, hoặc gõ liền `"1 người ăn chay 1 người dị ứng..."`).
- Sửa gì trước demo (ghi `spec.md` §10): Đã sửa `parse_request` trong `codebase/tools.py` để tách riêng từng người không tên khi không có dấu phẩy; thêm retry `HTTP 429` và hỗ trợ biến `OPENAI_*` trong `codebase/ai.py`.
- Giữ gì và vì sao: Giữ cơ chế hỏi lại khi thiếu/chưa rõ quán (`_early_stop`, Học viên 2 tự sửa được ngay ở lần nhập lại) và giữ khả năng tự chọn món vừa ngân sách (Học viên 3 đánh giá hữu ích khi không biết ăn gì).
- Để dành sau: Hỗ trợ khớp tên quán viết tắt / từ khoá gần đúng (vd `"bún"` → `Quán Bún Mẫu` nếu chỉ có 1 quán bún).

## Ghi chú kiểm lại (28/11 ~13:10, Huy + Claude Code)

- Ba phiên dùng thử chạy bằng `gpt-4o-mini` (máy Hùng, biến `OPENAI_*`), **không phải `deepseek-flash`** — model nhóm dùng cho lượt 2 và mô phỏng chi phí. Code lọc / kiểm giỏ giống nhau, phần chọn món do model khác làm.
- Học viên 2: câu *"Quán Bún Mẫu, 3 người, 150k, 1 người vừa ăn chay vừa dị ứng đậu phộng"* với code hiện tại **không ra giỏ** mà hỏi lại (chưa hiểu "vừa … vừa …", ràng buộc chưa rõ → không lập giỏ). **Hùng cần ghi đúng câu người thử gõ lại và hệ thống trả gì**; nếu là hỏi lại thì sửa cột quan sát cho đúng.
- Học viên 1: lỗi gõ liền không dấu phẩy được sửa trong lúc thử (`spec.md` §10, ~12:55) — code demo khác code lượt 2; đọc lại 22 câu thử sau khi sửa: không câu nào đổi.

