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

## Bổ sung 27/11/2026 — nghiên cứu nguồn công khai

- Cấn Xuân Nghĩa phụ trách; Codex hỗ trợ tìm kiếm, đọc và tổng hợp nguồn công khai tại `evidence/secondary-research.md`.
- Báo cáo ghi đơn vị thực hiện/công bố, thời gian khảo sát, cỡ mẫu, trang và link gốc; giữ trích dẫn công khai cùng ngữ cảnh và giới hạn.
- Không tạo phản hồi khảo sát, người phỏng vấn hoặc số liệu nội bộ. Chưa xác minh bộ dữ liệu khảo sát/phỏng vấn mà thành viên khác đã cập nhật. Nghĩa cần kiểm nguồn và giải thích được các mẫu số trước khi dùng báo cáo.

## Bổ sung 28/11/2026 — biên tập ba ghi chép phỏng vấn

- Cấn Xuân Nghĩa cung cấp nội dung P1–P3, số liệu và hai câu trích mỗi người, đồng thời xác nhận cả ba ngoài nhóm Aliba6. Codex biên tập cấu trúc theo GUIDE, giữ trích dẫn, tách số nghe được với phép tính và tổng hợp theo vai.
- Không lấy nội dung từ ba kịch bản luyện tập trước đó để bổ sung lời kể. Các biên bản mới thay hồ sơ ứng viên, chưa xác nhận ánh xạ với dòng Google Form.
- Chưa nhận/nghe bản ghi âm; ngày giờ, hình thức và người hỏi chưa được cung cấp. Người phụ trách kiểm lại: Cấn Xuân Nghĩa.
