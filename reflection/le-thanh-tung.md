# Reflection — Lê Thanh Tùng

> Làm ở guide bước 5.3. Hạn: **23:59 Thứ Bảy 28/11**.

1. **Vai trò + phần mình làm:**
   Thành viên nhóm Aliba6, track D2 (Đặt đồ ăn hộ nhóm có ràng buộc ăn uống). 
   - Đến CP2: làm Cặp X cùng Huy, phụ trách viết và kiểm thử các hàm logic lõi trong `codebase/tools.py` (`get_menu`, `safe_dishes`, `validate_cart`), rà soát 21 món ăn trong `data/menu.json` và `data/DATA_CARD.md`. Thực hiện chấm thử độc lập 5 câu ở CP2 (`eval/cham-thu-5.md` khớp 5/5).
   - Đến CP4: làm Cặp 2 cùng Hùng, phụ trách khâu đo lường và đánh giá: chạy Lượt 1 (`eval/run-1.csv`, mình chấm 17/22, sau chấm lại còn 16/22 vì B15 chấm nhầm), rà lại bản chấm 22 câu Lượt 2 của Huy (`eval/run-2.csv`) và đồng ý 22/22 — đây là rà lại, không phải chấm độc lập vì điểm của Huy đã có trên repo trước khi mình xem. Viết bản đầu `eval/report.md` (Huy sửa lại phần mô tả cách sửa parser). Chạy mô phỏng chi phí 50 phiên `cost/simulate-1.csv` và viết bản đầu `cost/cost-estimate.md`, `spec.md` §8, slide 6–7; lượt này đo token trên `qwen/qwen3.5-flash:free`, khác model lượt 2, nên nhóm chạy lại `simulate-2` bằng `deepseek-flash` và bản cuối của phần chi phí là của Nghĩa.

2. **AI hỗ trợ mình thế nào:**
   Mình dùng Antigravity và Claude Code để hỗ trợ viết nhanh các hàm kiểm tra ràng buộc ăn uống, phân tích cú pháp regex tiếng Việt, dựng khung báo cáo đánh giá và script tính toán mô phỏng chi phí. Tuy nhiên, mình luôn kiểm duyệt chặt chẽ từng output của AI: phát hiện và loại bỏ các con số bịa không có nguồn khảo sát, và tự chấm cột B của bản chấm thử 5 câu ở CP2 (khớp 5/5) thay vì để AI chấm. Chỗ mình chưa làm tốt: lần đầu chấm B15 ở Lượt 1 là đạt, trong khi parser hiểu chữ "Đợt" thành tên người (giỏ 7 người, đề là 6) — lỗi này Huy sửa ở commit `810e98e`; và chạy mô phỏng chi phí trên model khác với lượt 2 mà chưa để ý.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   Câu B19 ở Lượt 2 (Quán Bún Mẫu, 3 người 180k, 2 bạn ăn chay cần 2 món chay khác nhau): Lượt 1 parser không nhận "2 bạn ăn chay" nên 2 bạn nhận món mặn; sau khi sửa parser, Lượt 2 hết vi phạm (2 bạn đều nhận Bún chay B04), nhưng câu vẫn bị tính trượt vì Quán Bún Mẫu chỉ có đúng 1 món chay nên cả 2 bạn phải ăn trùng món, và hệ thống chưa chủ động đề xuất đổi sang Quán Cơm Mẫu (nơi có 4 món chay). Bài học: Một hệ thống đặt hộ thông minh không chỉ dừng lại ở việc "không vi phạm an toàn" và "vừa tiền", mà còn phải biết đánh giá độ phong phú của menu theo ràng buộc của nhóm để đưa ra tư vấn đổi quán kịp thời trước khi chốt giỏ.
