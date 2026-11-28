# Reflection — Cấn Xuân Nghĩa

> Làm ở guide bước 5.3. Hạn: **23:59 Thứ Bảy 28/11**.
> *Nháp do Huy + Claude Code soạn từ commit của Nghĩa và `docs/ai-usage.md`. Nghĩa đọc lại, sửa thành lời mình và viết dòng "Mình học được" ở mục 3 — reflection là bài cá nhân, phải giải thích được từng câu. Xong thì xoá dòng này.*

1. **Vai trò + phần mình làm:**
   Thành viên Aliba6, cặp Y (bằng chứng người dùng) đến CP3, phần chi phí ở CP4.
   - Nghiên cứu nguồn công khai: `evidence/secondary-research.md` (commit `8fe3bd1`), ghi đơn vị công bố, thời gian, cỡ mẫu, link gốc.
   - Phỏng vấn P1–P3 ngày 27/11, trực tuyến, mình hỏi và ghi (`evidence/interviews/P1.md`–`P3.md`, commit `48e58ea`, `d113a16`).
   - Khảo sát CP3: số tổng hợp `evidence/survey/counts-cp3-20261128.json`, script `count_cp3.py`, giữ bản từng phiếu ngoài repo (commit `071c20e`).
   - CP4: dự toán chi phí `cost/cost-estimate.md`, `cost/personas.yaml`, script `cost/reprice_existing.py` (tính lại giá trên 50 phiên `simulate-2` có sẵn, không gọi API), quy mô từ Vietdata 12 triệu × 13/22, `spec.md` §8 (commit `147dac9`).

2. **AI hỗ trợ mình thế nào:**
   Dùng Claude Code soạn nháp câu hỏi phỏng vấn / khảo sát theo Mom Test; dùng Codex tìm và tổng hợp nguồn công khai, biên tập cấu trúc ba ghi chép phỏng vấn từ nội dung mình cung cấp, viết script đếm khảo sát và script tính lại chi phí. Chỗ mình phải tự quyết / kiểm: xác nhận người trả lời ngoài nhóm và không trùng; không dùng câu 3 CP3 chưa chuẩn hoá; chọn dùng lại 50 phiên `simulate-2` thay vì chạy lượt mới; ghi rõ thấp / cao theo Wilson chỉ là độ nhạy trên mẫu thuận tiện và giá `deepseek-v4-pro` chỉ là quy đổi trên token flash. Ba trích dẫn phỏng vấn chưa xác nhận được nên `evidence/summary.md` quay về trích dẫn công khai.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   *(Gợi ý dữ kiện, Nghĩa chọn một câu)* Lượt 2 trượt 3 câu: B17 (expected viết sai — menu có món 25k nên giỏ 200k là hợp lệ), B19 (Quán Bún Mẫu chỉ có 1 món chay, 2 bạn ăn chay nhận cùng Bún chay, không gợi ý đổi quán), B21 (nhờ gọi shipper, hệ thống hỏi thiếu thông tin thay vì từ chối). Liên quan phần chi phí: tỉ lệ đạt 19/22 đi thẳng vào "chi phí / task thành công", nên mỗi câu trượt làm chi phí / task tăng.
   Mình học được: ___
