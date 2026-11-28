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

## Rà soát trước CP3 — 28/11/2026

- Nghĩa xác nhận ngày phỏng vấn 27/11/2026, hình thức trực tuyến, Nghĩa hỏi và ghi cho cả ba hồ sơ. Codex chỉ điền những thông tin đã được cung cấp, không tự gán giờ hoặc trả lời thay người tham gia.
- Các điểm chưa có phản hồi bổ sung được ghi rõ trạng thái trong P1–P3. Theo yêu cầu của Nghĩa, trích dẫn chưa xác nhận trong `evidence/summary.md` quay về nguồn công khai W02/W04/W03; chưa chốt kết quả 2/3 phỏng vấn.

## Bổ sung 28/11/2026 — khảo sát CP3

- Codex đọc bảng phản hồi kết nối, giữ bản từng phiếu trên máy, xuất JSON chỉ gồm số tổng hợp, viết script đếm lại từ bản nội bộ và cập nhật summary/canvas. Không tạo hoặc sửa câu trả lời.
- Nghĩa xác nhận toàn bộ người trả lời ngoài nhóm và không trùng. Không gắn nhãn riêng từng phiếu; câu 8 mâu thuẫn không dùng cho riêng chỉ số câu 8, các câu khác giữ nguyên. Không dùng câu 3 chưa xác minh để tính trung bình.


## Bổ sung 28/11/2026 — nguồn quy mô và dự toán chi phí

- Codex tìm nguồn công khai Vietdata và giá chính thức DeepSeek; bổ sung phép ngoại suy và giới hạn trong `cost/cost-estimate.md`, sửa `cost/personas.yaml` và spec §8.
- Nghĩa chọn dùng 50 phiên simulate-2 đã có. Script `cost/reprice_existing.py` kiểm token/model/tỉ lệ 19/22, tính lại giá không gọi API, ghi băm kiểm tra kết quả gốc. Không tạo phiên, token hay tỉ lệ đạt mới; không sửa CSV/trace đã chạy.
- Thấp/cao là độ nhạy tham chiếu theo công thức Wilson trên mẫu thuận tiện, không phải khảo sát đại diện. Quy đổi pro dùng token và tỉ lệ đạt của flash, không khẳng định đã đo model pro. Người kiểm báo cáo: Cấn Xuân Nghĩa.
