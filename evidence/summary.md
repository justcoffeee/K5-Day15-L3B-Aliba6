# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Mạnh nhất: đào data ra insight → hỏi người dùng để kiểm lại (hoặc ngược lại).

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☐ | `evidence/data-mining.md` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | Chưa chốt đạt ngưỡng: có 3 ghi chép, đã xác nhận ngày 27/11/2026, trực tuyến, Nghĩa hỏi/ghi; còn các điểm nội dung cần xác nhận | `evidence/interviews/P1.md`, `P2.md`, `P3.md` |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☑ Lượt CP3: 34 phiếu ngoài nhóm, không trùng theo xác nhận của Nghĩa; **20 người đã đặt hộ nhóm** | `evidence/survey/counts-cp3-20261128.json` · `evidence/survey/count_cp3.py` |

## 2. Số chính

### Lượt cập nhật CP3 — chụp lúc 08:30 ngày 28/11/2026

- **N = 34** người ngoài nhóm, không trùng theo xác nhận của Nghĩa; **20/34 (58.8%)** từng đặt qua app hộ nhóm ≥3 người trong tháng qua. Đạt ngưỡng số lượng ≥20 người dùng theo câu sàng lọc.
- **9/19 (47.4%)** gặp ít nhất một trong ba sự cố câu 8: nhầm món / vượt dự tính / thiếu hoặc đổi món. Mẫu số là 19 câu 8 dùng được trong 20 người đặt hộ; không cộng số ô chọn thành số người. Một câu trả lời mâu thuẫn không dùng cho chỉ số câu 8, vẫn giữ phiếu và các câu khác.
- Theo loại sự cố trên 19 câu dùng được: nhầm món **1/19**; vượt dự tính **3/19**; thiếu/đổi món **6/19**. Các nhóm có thể trùng người.
- Ràng buộc ăn uống lần gần nhất: **4/20 (20.0%)** có; 11/20 không; 5/20 không rõ. Chưa có ≥20 người thuộc lát cắt hẹp nhóm có ràng buộc, nên không suy rộng tỷ lệ cho lát cắt này.
- Thời gian: 13/20 chọn 5–10 phút; 4/20 chọn 10–20 phút; 1/20 trên 20 phút; 2/20 không nhớ. Không coi khoảng 10–20 là chắc chắn >10 và không tính trung bình phút từ khoảng chọn.
- **8/20** người đủ điều kiện đồng ý hỏi thêm. Không có thông tin liên hệ trong form.
- Không tính trung bình tần suất câu 3 khi câu trả lời chưa được chuẩn hoá/xác minh. Không gắn nhãn riêng từng dòng hoặc sửa câu trả lời gốc.
- Nguồn: bảng phản hồi Google Sheets; `counts-cp3-20261128.json` chỉ lưu số tổng hợp. `python evidence/survey/count_cp3.py` hiển thị số đã công bố; để đếm lại cần bản chụp nội bộ trên máy và truyền đường dẫn cho script. Dữ liệu từng phiếu giữ riêng, không công khai. Kết quả CP2 dưới đây là lịch sử, không phải số mới nhất.

### Lịch sử CP2 — giữ số đã báo cáo

- Đào data: __/__ (__%) …
- Phỏng vấn: có 3 hồ sơ chờ xác nhận nội dung. Không dùng các số 2/3, 1/2 sinh viên hoặc 1/1 admin làm kết quả phỏng vấn đã chốt trước CP3. Ngày cuộc hỏi 27/11/2026, hình thức trực tuyến, Cấn Xuân Nghĩa hỏi và ghi đã được Nghĩa xác nhận; giờ cụ thể chưa cung cấp.
- Khảo sát (đếm lần 1, bản xuất 18:05 27/11/2026, chạy lại: `python evidence/survey/count.py`): **N = 22** — không phiếu nào của thành viên Aliba6 (đã hỏi lại cả nhóm), không phiếu trùng
  - Từng đặt hộ nhóm ≥3 người trong 1 tháng qua: **13/22 (59.1%)** — giả thuyết ≥50%: đạt.
  - Trong 13 người đó, gặp ≥1 sự cố (nhầm món cho người ăn chay / dị ứng · vượt dự tính · thiếu / phải đổi món): **7/13 (53.8%)** — giả thuyết ≥1/3: đạt.
  - Tách theo loại sự cố (trên 13): thiếu món / phải đổi món **6/13** · vượt dự tính (phí ship, phí dịch vụ) **2/13** · không biết thành phần món **1/13** · phải chọn lại quán **1/13** · **chọn nhầm món cho người ăn chay / dị ứng / kiêng: 0/13** · không gặp chuyện nào 6/13.
  - Nhóm lần gần nhất có người không ăn được một số món: **3/13** có · 7/13 không · 3/13 không rõ.
  - Mất >10 phút từ chọn quán đến bấm đặt: **5/13** (4 người 10–20 phút, 1 người >20 phút).
  - Cách gom (chọn nhiều): mỗi người tự chọn trên giỏ nhóm của app 7/13 · gửi menu vào nhóm chat 7/13 · hỏi từng người qua chat 4/13 · tự chọn hộ luôn 0/13.
  - Vai: 9 học viên L3B · 5 L3A · 2 lớp khác · 1 lab coach / TA · 5 "khác". Câu 3 (số lần / tháng) ghi tay, từ 1 đến 20 lần.

Phỏng vấn nhiều vai thì đếm theo từng vai, không cộng chung.

| | Vai | Gặp pain? | Số lần / 1 tháng qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | Sinh viên năm cuối, nhóm lab | Chờ xác nhận nội dung | Chưa dùng để tổng hợp | Chưa dùng để tổng hợp | Xem hồ sơ và bảng xác nhận P1 |
| P2 | Admin văn phòng | Chờ xác nhận nội dung | Chưa dùng để tổng hợp | Chưa dùng để tổng hợp | Xem hồ sơ và bảng xác nhận P2 |
| P3 | Sinh viên ký túc xá | Chưa xác định đầy đủ thời gian chọn quán | Chưa dùng để tổng hợp | Chưa dùng để tổng hợp | Giữ trường hợp phản chứng trong hồ sơ, chưa chốt chỉ số |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. "Món bị sai, bạn tôi không chịu ăn và thanh toán món đấy" — phiếu khảo sát dòng 10 (`results.csv`)
2. "mình bị người khác lấy nhầm suất ăn và phải nhận 1 suất đồ ăn khác" — phiếu khảo sát dòng 3 (`results.csv`)
3. "Đơn vị không giao hàng" — phiếu khảo sát dòng 9 (`results.csv`) *(lỗi phía giao hàng, ngoài lát cắt)*
4. "I always end up getting the same 2 places since it's so tough to stay in budget and still cover everyone's dietary needs..." — **nguồn công khai**, [bình luận r/AdminAssistant](https://www.reddit.com/r/AdminAssistant/comments/1s1t9f0/comment/oc7pwxa/), W02 trong `secondary-research.md`; không phải người nhóm hỏi.
5. "The toughest part is definitely coordinating everyone's preferences and knowing exactly who’s in the office without a million messages back and forth." — **nguồn công khai**, [bình luận r/AdminAssistant](https://www.reddit.com/r/AdminAssistant/comments/1s1t9f0/comment/ock4uwt/), W04 trong `secondary-research.md`; không phải người nhóm hỏi.
6. "This is super easy and I don’t have to worry about preference or dietary restrictions." — **nguồn công khai**, [bình luận r/AdminAssistant](https://www.reddit.com/r/AdminAssistant/comments/1s1t9f0/comment/oc38bho/), W03 trong `secondary-research.md`; ngữ cảnh gửi link giỏ nhóm cho khoảng 10 người, cách hiện tại đã thuận tiện.

*Mục 4–6 quay về nguồn công khai trước CP3 vì P1–P3 còn điểm chưa xác nhận. Các trích dẫn trên web không tính thành phỏng vấn hoặc phản hồi khảo sát của nhóm. Nếu permalink lỗi, xem trang luồng và ngữ cảnh đã ghi trong `secondary-research.md`. Các trích dẫn P1–P3 được giữ trong hồ sơ riêng để đối chiếu, chưa dùng tại đây.*

## 4. Các nguồn có khớp nhau không

Khảo sát người dùng thật (N = 22, 13 người đặt hộ) cho thấy: 53.8% gặp sự cố khi đặt hộ nhóm (chủ yếu là thiếu món/đổi món 6/13 và vượt dự tính do quên phí ship 2/13).
Khớp và lệch so với giả định ban đầu:
- **Khớp:** Nhu cầu gom đơn đặt hộ là có thật và phổ biến (59.1% người khảo sát từng đặt hộ nhóm ≥3 người trong tháng qua); thời gian gom đơn tốn trung bình ~11 phút/đơn; việc nhầm suất ăn hay vượt ngân sách thực sự xảy ra và gây phiền toái cho người đặt.
- **Lệch:** Khảo sát cho thấy tỷ lệ nhầm món chay / dị ứng là 0/13. Nhóm **chưa biết** vì sao — một khả năng (chưa có dữ liệu): người đặt rất cẩn thận với dị ứng nên tốn thời gian hỏi lại thay vì chọn bừa; khả năng khác: chỉ 3/13 nhóm có người kiêng nên ít cơ hội nhầm. Phải hỏi trong phỏng vấn. Việc nhóm giữ chốt chặn an toàn (code rule engine) sẽ giải phóng thời gian tra cứu và rà soát thủ công này cho người đặt. P1–P3 còn chờ xác nhận nên chưa dùng để giải thích nguyên nhân khảo sát. Nguồn công khai W02/W04 minh hoạ khó khăn cân bằng nhu cầu và phối hợp; W03 cho thấy giỏ nhóm có thể đã đủ thuận tiện. Đây là các ví dụ chọn có chủ đích, không xác nhận tỷ lệ hoặc nguyên nhân tại Việt Nam.

## 5. Kết luận

**Cập nhật CP3:** khảo sát đạt ngưỡng số lượng 20 người tự khai đã đặt hộ nhóm, ngoài Aliba6 và không trùng theo xác nhận của Nghĩa. Có thể dùng khảo sát làm nguồn bằng chứng đạt ngưỡng; phần phỏng vấn vẫn chưa chốt. Kết quả 9/19 về sự cố dùng định nghĩa câu 8, không đồng nhất với mọi tiêu chí trong giả thuyết ban đầu. Không kết luận tỷ lệ cho toàn bộ Việt Nam hoặc riêng nhóm có ràng buộc từ mẫu nhỏ này.

**Kết luận đã ghi ở CP2 (lịch sử):**

Giả thuyết ở `evidence/hypothesis.md` (đếm lần 1, N = 22): **đạt hai ngưỡng đã viết trước** (59.1% từng đặt hộ ≥ 50%; 53.8% gặp sự cố ≥ 1/3), **nhưng lệch ở nguyên nhân**: sự cố hay gặp nhất là *thiếu món / phải đổi món* (6/13) và *vượt dự tính* (2/13); **không ai** chọn *nhầm món cho người ăn chay / dị ứng* (0/13), và chỉ 3/13 nhóm có người kiêng. Phần lớn đã dùng giỏ nhóm của app hoặc gửi menu vào chat (7/13 mỗi cách). Điều vẫn chưa biết: sự cố "thiếu / đổi món" do người đặt chọn sai hay do quán làm sai; mẫu còn nhỏ và là bạn cùng khoá — đã có ba ghi chép, thông tin cuộc hỏi được bổ sung, nhưng nội dung chưa xác nhận xong nên chưa chốt ngưỡng phỏng vấn.

## Lịch hẹn (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| | | |

## 6. Nguồn khảo sát công khai bổ sung — phần Cấn Xuân Nghĩa

Báo cáo [nghiên cứu nguồn công khai](secondary-research.md) ghi rõ hai khảo sát do **ezCater** công bố năm **2023** và **2024**, mẫu người thường đặt đồ ăn cho nơi làm việc, vị trí trang và URL báo cáo gốc. Đây là số liệu bên ngoài, **không** phải khảo sát của nhóm và không cộng vào mẫu số của nhóm. Năm ví dụ công khai có trích dẫn và ngữ cảnh riêng; không phải người Aliba6 đã phỏng vấn.
## 7. Trạng thái xác nhận trước CP3 10:00 ngày 28/11/2026

- Nghĩa xác nhận cả ba người ngoài nhóm; các cuộc hỏi ngày 27/11/2026, trực tuyến; Cấn Xuân Nghĩa vừa hỏi vừa ghi. Không suy ra giờ bắt đầu hoặc gọi thoại/video/chat cụ thể.
- P1: chưa làm rõ mốc ngày/lịch âm và đổi món trước hay sau đặt; P2: chưa làm rõ kênh chat, tổng sau mã và thành phần phí; P3: chưa làm rõ ngày đặt và toàn bộ thời gian chọn quán đến bấm đặt. P1/P2 chưa có xác nhận đồng ý ghi âm.
- Mục 3 đã dùng lại nguồn công khai cho các vị trí trước đó trích P1–P3. Không cộng nguồn ngoài vào mẫu số khảo sát, không tính thành người nhóm phỏng vấn.
- Chưa xác nhận đủ để chốt kết quả phỏng vấn; không báo 2/3 người gặp pain ở bản tổng hợp hiện tại. Giữ nội dung đã nhận trong P1–P3 và bảng trả lời từng điểm để tiếp tục đối chiếu.
## 8. Xác nhận mẫu khảo sát trước CP3

Nghĩa xác nhận toàn bộ người trả lời ngoài nhóm Aliba6 và không trùng người. Dữ liệu lượt CP3 gồm 34 phiếu, 20 người trả lời Có ở câu 2; giữ nguyên dữ liệu nhận được. Không xác nhận thay các điểm còn vướng trong hồ sơ P1–P3. Một câu 8 mâu thuẫn được bỏ khỏi riêng chỉ số câu 8; không loại cả người hoặc chỉnh đáp án để đạt ngưỡng.
