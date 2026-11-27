# Khảo sát — đặt đồ ăn hộ cả nhóm

> Nguồn bằng chứng chính của nhóm Aliba6 (guide 1.2). Ngưỡng: **≥20 người ngoài nhóm, đúng người dùng**. Giả thuyết đã chốt trước ở `evidence/hypothesis.md`.
> Chép sang Google Form đúng nguyên câu chữ dưới đây. Form **không thu** email, tên, mã học viên (Google Form: Cài đặt → Câu trả lời → *Thu thập địa chỉ email: Không thu thập*; tắt "Giới hạn 1 câu trả lời" để không bắt đăng nhập).
> Kết quả: xuất CSV, **xoá mọi cột nhận ra người trả lời** (cột liên hệ ở câu 10, dấu thời gian nếu cần) → lưu `evidence/survey/results.csv`. Bản gốc không commit (đặt tên `raw-*.csv` — đã có trong `.gitignore`).

## Thông tin gửi

- Kênh đã gửi: __ (vd nhóm Zalo lớp L3B, Discord kênh chung, hỏi trực tiếp giờ nghỉ)
- Giờ mở: __ · giờ chốt: __ (chốt trước khi tổng hợp, ghi lại để không bị nói "đếm lúc nào cũng được")
- Người trong nhóm Aliba6 **không trả lời** form này.

**Tin nhắn gửi kèm (không giới thiệu sản phẩm, tránh dẫn dắt):**
> Chào mọi người, nhóm mình đang tìm hiểu cách mọi người đặt đồ ăn chung cho cả nhóm. Form 2 phút, 10 câu, không hỏi tên hay email. Cảm ơn nhiều! [link]

## Câu hỏi

**Phần 1 · Lọc người dùng**

| # | Câu hỏi | Kiểu trả lời |
|---|---|---|
| 1 | Bạn là: | Chọn một: học viên L3A · học viên L3B · học viên lớp khác · lab coach / TA · khác |
| 2 | Trong **1 tháng qua**, bạn có **đặt đồ ăn qua app hộ cho một nhóm từ 3 người trở lên** (bạn trả hoặc đặt rồi chia tiền) không? | Chọn một: Có · Không |

*Chọn "Không" ở câu 2 → chuyển thẳng tới câu 10 (Google Form: "Chuyển đến phần dựa trên câu trả lời").*

**Phần 2 · Lần gần nhất bạn đặt hộ nhóm** *(chỉ người trả lời "Có" ở câu 2)*

| # | Câu hỏi | Kiểu trả lời |
|---|---|---|
| 3 | Trong 1 tháng qua, bạn đặt hộ nhóm khoảng **mấy lần**? | Số |
| 4 | **Lần gần nhất**, nhóm có bao nhiêu người? | Chọn một: 3 · 4–5 · 6–8 · trên 8 |
| 5 | Lần gần nhất đó, trong nhóm có ai **không ăn được một số món** không? (ăn chay, dị ứng, kiêng — không cần nói là ai, bị gì) | Chọn một: Có · Không · Không rõ, mình không hỏi |
| 6 | Lần gần nhất đó, bạn **gom món cho mọi người bằng cách nào**? | Chọn nhiều: hỏi từng người qua chat rồi tự chọn · mỗi người tự chọn trên link chia sẻ / giỏ nhóm của app · gửi menu vào nhóm chat cho mọi người tự ghi · mình tự chọn hộ luôn · khác |
| 7 | Từ lúc bắt đầu chọn quán đến lúc bấm đặt, lần đó mất khoảng **bao lâu**? | Chọn một: dưới 5 phút · 5–10 phút · 10–20 phút · trên 20 phút · không nhớ |
| 8 | Trong **1 tháng qua**, khi đặt hộ nhóm, bạn đã gặp chuyện nào dưới đây **ít nhất một lần**? | Chọn nhiều: chọn nhầm món cho người ăn chay / dị ứng / kiêng · không biết món có thành phần gì nên phải hỏi quán hoặc đoán · tổng tiền vượt dự tính (vd quên phí ship, phí dịch vụ) · có người bị thiếu món hoặc phải đổi món · phải chọn lại quán vì không đủ món hợp với mọi người · không gặp chuyện nào |
| 9 | Kể ngắn **lần gần nhất** việc đặt hộ nhóm bị trục trặc: chuyện gì xảy ra, bạn xử lý thế nào? (không ghi tên ai) | Đoạn văn |

**Phần 3 · Kết thúc**

| # | Câu hỏi | Kiểu trả lời |
|---|---|---|
| 10 | (Tuỳ chọn) Bạn có sẵn lòng cho nhóm hỏi thêm 10 phút về chuyện này không? | Chọn một: Có — để lại cách liên hệ (không bắt buộc) · Không |

## Cách đếm — viết trước khi mở kết quả

- **Mẫu số chung N** = số phiếu hợp lệ, **trừ** người trong nhóm Aliba6 và phiếu trùng rõ ràng. Báo cáo cả N lẫn số người trả lời "Có" ở câu 2.
- **Tỉ lệ có đặt hộ nhóm** = số "Có" ở câu 2 / N. *(Giả thuyết: ≥50%)*
- **Tỉ lệ gặp sự cố** = số người (trong nhóm "Có") chọn **ít nhất một** trong ba ô ở câu 8: *nhầm món cho người ăn chay / dị ứng / kiêng* · *vượt dự tính* · *có người thiếu / phải đổi món* — chia cho **số "Có" ở câu 2** (không chia cho N). *(Giả thuyết: ≥1/3)*
- **Mất >10 phút** = số chọn "10–20 phút" hoặc "trên 20 phút" ở câu 7 / số "Có" ở câu 2. "Không nhớ" vẫn tính trong mẫu số, ghi riêng.
- **Có ràng buộc ăn uống** = số "Có" ở câu 5 / số "Có" ở câu 2.
- **Tần suất cho persona chi phí** (`cost/personas.yaml`): phân phối câu 3 → chia ít · vừa · nhiều.
- Câu 9: đọc hết, gắn nhãn theo các ô của câu 8, chọn **≥3 câu trả lời nguyên văn** (tối đa 2 câu mỗi phiếu, bỏ chi tiết nhận ra người) → `evidence/summary.md`.
- Dưới khoảng 10 người ở một mẫu số thì chỉ ghi x/n, không ghi %.
- **Giới hạn đã biết:** mẫu là bạn cùng khoá, trẻ, rành app; người đặt hộ hay gặp sự cố có thể dễ trả lời hơn. Ghi rõ khi kết luận.
