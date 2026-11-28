# Reflection — Nguyễn Mạnh Hùng

> Làm ở guide bước 5.3. Hạn: **23:59 Thứ Bảy 28/11**.
> *Nháp do Huy + Claude Code soạn từ commit của Hùng và `docs/ai-usage.md`. Hùng đọc lại, sửa thành lời mình (nhất là mục 2: công cụ AI dùng ở CP4) và viết dòng "Mình học được" ở mục 3 — reflection là bài cá nhân, phải giải thích được từng câu. Xong thì xoá dòng này.*

1. **Vai trò + phần mình làm:**
   Thành viên Aliba6, cặp Y đến CP2, cặp 2 cùng Tùng ở CP4.
   - CP2: data card `data/DATA_CARD.md`, menu giả, bộ câu thử `eval/benchmark.csv`, `eval/metric_spec.yaml`, `eval/README.md` (commit `9e44c91`); chấm cột A của bản chấm thử 5 câu `eval/cham-thu-5.md` (commit `95fbda1`).
   - CP3: cùng Tùng mở rộng benchmark lên 22 câu, 8 câu lấy từ khảo sát (commit `4a4988d`).
   - CP4 (commit `9c035e1`): cho 3 học viên ngoài nhóm dùng thử, ghi `validation/log.md` (bonus); sửa `parse_request` trong `codebase/tools.py` để tách người không tên khi gõ liền không dấu phẩy ("1 người ăn chay 1 người dị ứng đậu phộng"), lỗi phát hiện ngay trong lúc thử; thêm biến `OPENAI_*` và thử lại khi lỗi 429 trong `codebase/ai.py`.

2. **AI hỗ trợ mình thế nào:**
   Dùng Claude Code viết nháp 14 câu `tu_viet` theo tình huống khó của track D2 và menu giả `data/menu.json`; mình kiểm `expected` / `pass_criterion` của từng câu với menu, câu `nguoi_dung` lấy từ khảo sát, không để AI viết. *(Hùng bổ sung: công cụ AI dùng khi sửa `tools.py` / `ai.py` ở CP4 và chỗ phải sửa lại output của AI.)* Lúc cho người dùng thử, mình chạy bằng `gpt-4o-mini` trên máy mình, khác model nhóm dùng (`deepseek-flash`).

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   *(Gợi ý dữ kiện, Hùng chọn một câu)* B17 (Quán Cơm Mẫu, 7 người, 200k): `expected` ghi "món rẻ nhất 30k × 7 + ship = 230k, không đủ tiền", nhưng menu có món 25k (C08, C14) nên 7 × 25k + 20k = 195k là giỏ hợp lệ. Câu trượt ở cả hai lượt vì `expected` viết sai so với menu, nhóm giữ nguyên không sửa sau khi đã chạy. Hoặc: lỗi gõ liền không dấu phẩy mình gặp khi cho người dùng thử — 22 câu benchmark không có câu nào như vậy.
   Mình học được: ___
