# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Claude Code (Opus 5.5) | Viết `codebase/agent.py`, `tools.py` (parse_request, safe_dishes, validate_cart) | Cặp X đọc từng hàm, chạy 14 câu thử ở chế độ giả, sửa chỗ hiểu sai | Phạm Hoàng Huy, Lê Thanh Tùng |
| Prompt / thiết kế lời gọi mô hình | Claude Code (Opus 5.5) | Viết nháp `SYSTEM` trong `agent.py` (bước chọn món) | Cặp X thử với model thật trước CP3 | Phạm Hoàng Huy |
| Đào data (viết script đếm, gợi ý nhãn) | | | Kiểm tay __ dòng, khớp __ | |
| Rà câu hỏi phỏng vấn / khảo sát | Claude Code (Opus 5.5) | Soạn nháp câu hỏi theo Mom Test, rà câu dẫn dắt | Cặp Y đọc lại, sửa câu chữ trước khi gửi | Cấn Xuân Nghĩa |
| Viết câu thử (benchmark) | Claude Code (Opus 5.5) | Viết nháp 14 câu `tu_viet` từ tình huống khó track D2 | Mỗi câu thử có `source`; cặp Y kiểm expected / pass_criterion với menu; câu `nguoi_dung` lấy từ khảo sát, phỏng vấn — không để AI viết | Nguyễn Mạnh Hùng |
| Sinh data `synthetic` (nếu có) | Claude Code (Opus 5.5) | Viết tay menu giả `data/menu.json` (không seed) | Seed: không dùng · kiểm tay __/21 món | Nguyễn Mạnh Hùng |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | | | | |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
