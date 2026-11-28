# Reflection — Lê Thanh Tùng

> Làm ở guide bước 5.3. Hạn: **23:59 Thứ Bảy 28/11**.

1. **Vai trò + phần mình làm:**
   Thành viên nhóm Aliba6, track D2 (Đặt đồ ăn hộ nhóm có ràng buộc ăn uống). 
   - Đến CP2: làm Cặp X cùng Huy, phụ trách viết và kiểm thử các hàm logic lõi trong `codebase/tools.py` (`get_menu`, `safe_dishes`, `validate_cart`), rà soát 21 món ăn trong `data/menu.json` và `data/DATA_CARD.md`. Thực hiện chấm thử độc lập 5 câu ở CP2 (`eval/cham-thu-5.md` khớp 5/5).
   - Đến CP4: làm Cặp 2 cùng Hùng, phụ trách khâu đo lường và đánh giá: chạy Lượt 1 (`eval/run-1.csv`), chấm chéo độc lập toàn bộ 22 câu Lượt 2 (`eval/run-2.csv`, đạt độ khớp 22/22 100% với Huy), viết toàn diện báo cáo so sánh cải tiến kỹ thuật tại `eval/report.md`. Thực hiện chạy mô phỏng chi phí 50 phiên (`cost/simulate-1.csv`), tính toán 3 kịch bản người dùng và hoàn thiện `cost/cost-estimate.md`, `spec.md` §8 và dàn slide 6–7 tại `slides/outline.md`.

2. **AI hỗ trợ mình thế nào:**
   Mình dùng Antigravity và Claude Code để hỗ trợ viết nhanh các hàm kiểm tra ràng buộc ăn uống, phân tích cú pháp regex tiếng Việt, dựng khung báo cáo đánh giá và script tính toán mô phỏng chi phí. Tuy nhiên, mình luôn kiểm duyệt chặt chẽ từng output của AI: phát hiện và loại bỏ các con số bịa không có nguồn khảo sát, sửa lỗi regex khi AI bắt nhầm chữ hoa đầu câu ("Đợt") thành tên người ở B15, và tự tay chấm độc lập từng dòng kết quả benchmark thay vì để AI tự chấm, bảo đảm tính khách quan và trung thực tuyệt đối của dữ liệu.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   Câu B19 ở Lượt 2 (Quán Bún Mẫu, 4 người 250k, có 2 bạn ăn chay): Sau khi sửa parser, code đã hết vi phạm dị ứng (2 bạn đều nhận món chay B04 an toàn), nhưng câu vẫn bị tính trượt vì Quán Bún Mẫu chỉ có đúng 1 món chay nên cả 2 bạn phải ăn trùng món, và hệ thống chưa chủ động đề xuất đổi sang Quán Cơm Mẫu (nơi có 3 món chay phong phú hơn). Bài học: Một hệ thống đặt hộ thông minh không chỉ dừng lại ở việc "không vi phạm an toàn" và "vừa tiền", mà còn phải biết đánh giá độ phong phú của menu theo ràng buộc của nhóm để đưa ra tư vấn đổi quán kịp thời trước khi chốt giỏ.
