# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Mạnh nhất: đào data ra insight → hỏi người dùng để kiểm lại (hoặc ngược lại).

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☐ | `evidence/data-mining.md` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | Đã nhận 3 ghi chép; Nghĩa xác nhận ngoài nhóm, đủ điều kiện đặt hộ; chờ bổ sung ngày giờ/hình thức cuộc hỏi | `evidence/interviews/P1.md`, `P2.md`, `P3.md` |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☑ 22 phiếu (đếm lần 1, 18:05 27/11) — 13 người đúng người dùng (đã đặt hộ nhóm trong tháng) | `evidence/survey/results.csv` · cách đếm: `evidence/survey/count.py` |

## 2. Số chính

- Đào data: __/__ (__%) …
- Phỏng vấn (ghi chép của Nghĩa): **P1, P2 gặp pain; P3 không báo sự cố**. Mô tả cả ba hồ sơ: **2/3** ghi nhận pain, không phải tỷ lệ đại diện cho một nhóm vai đồng nhất. Theo vai: **sinh viên 1/2**, **admin văn phòng 1/1**. Tần suất P1 khoảng 6, P2 3, P3 khoảng 4 lần/tháng. Gom món: P1 khoảng 20 phút; P2 khoảng 12 phút; P3 khoảng 3 phút sau khi chọn quán, chưa có tổng thời gian chọn quán đến đặt. Ngày giờ, hình thức và người hỏi còn cần bổ sung; chưa đối chiếu bản ghi gốc.
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
| P1 | Sinh viên năm cuối, đặt cơm nhóm lab 6 người | Có: khoảng 20 phút gom món | Khoảng 6 | Khoảng 20 phút gom món | Gom qua Zalo, tách đơn chay; thêm 18.000đ ship, phần chay chậm 15 phút |
| P2 | Admin văn phòng, đặt xế/trà sữa cho 8 người | Có: nhầm đồ uống kiêng sữa, vượt quỹ | 3 | Khoảng 12 phút gom món | Giỏ nhóm GrabFood + chat; vượt quỹ 65.000đ, đặt bù 55.000đ do người đặt trả |
| P3 | Sinh viên ký túc xá, đặt ăn đêm cho 4 người | Không báo nhầm món/vượt tiền; cần làm rõ thời gian chọn quán | Khoảng 4 | Khoảng 3 phút sau khi chọn quán | Hỏi trực tiếp trong phòng, quán quen; ghi chú không hành |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. "Món bị sai, bạn tôi không chịu ăn và thanh toán món đấy" — phiếu khảo sát dòng 10 (`results.csv`)
2. "mình bị người khác lấy nhầm suất ăn và phải nhận 1 suất đồ ăn khác" — phiếu khảo sát dòng 3 (`results.csv`)
3. "Đơn vị không giao hàng" — phiếu khảo sát dòng 9 (`results.csv`) *(lỗi phía giao hàng, ngoài lát cắt)*
4. "Ức chế nhất là hỏi thì bảo ăn gì cũng được, đến lúc mình bấm đặt xong xuôi rồi lại nhắn 'cho tao đổi sang cơm gà nhé'." — P1, ghi chép phỏng vấn của Nghĩa (`interviews/P1.md`)
5. "Mình tưởng dùng giỏ nhóm là xong, ai ngờ người ta vẫn nhắn ghi chú kiêng sữa ở bên Zalo, mình lỡ tay bấm đặt luôn thế là phải tự bỏ tiền túi mua lại cốc khác." — P2, ghi chép phỏng vấn của Nghĩa (`interviews/P2.md`)
6. "Khó mỗi cái là không biết ăn gì, chứ chốt được quán rồi thì bấm 3 phút là xong đơn." — P3, trường hợp ngược giả thuyết (`interviews/P3.md`)

*Mục 4–6 được giữ nguyên theo ghi chép của Nghĩa, chưa đối chiếu ghi âm. Không dùng: phiếu dòng 17 (câu đùa); phiếu dòng 21 chỉ tick ô "không biết thành phần", không có lời kể nên không phải trích dẫn.*

## 4. Các nguồn có khớp nhau không

Khảo sát người dùng thật (N = 22, 13 người đặt hộ) cho thấy: 53.8% gặp sự cố khi đặt hộ nhóm (chủ yếu là thiếu món/đổi món 6/13 và vượt dự tính do quên phí ship 2/13).
Khớp và lệch so với giả định ban đầu:
- **Khớp:** Nhu cầu gom đơn đặt hộ là có thật và phổ biến (59.1% người khảo sát từng đặt hộ nhóm ≥3 người trong tháng qua); thời gian gom đơn tốn trung bình ~11 phút/đơn; việc nhầm suất ăn hay vượt ngân sách thực sự xảy ra và gây phiền toái cho người đặt.
- **Lệch:** Khảo sát cho thấy tỷ lệ nhầm món chay / dị ứng là 0/13. Nhóm **chưa biết** vì sao — một khả năng (chưa có dữ liệu): người đặt rất cẩn thận với dị ứng nên tốn thời gian hỏi lại thay vì chọn bừa; khả năng khác: chỉ 3/13 nhóm có người kiêng nên ít cơ hội nhầm. Phải hỏi trong phỏng vấn. Việc nhóm giữ chốt chặn an toàn (code rule engine) sẽ giải phóng thời gian tra cứu và rà soát thủ công này cho người đặt. Ghi chép P1 cho thấy chủ động tách đơn để tránh món không phù hợp, đổi lại phát sinh phí và chờ; P2 có yêu cầu kiêng sữa nằm ngoài giỏ nhóm nên bị bỏ sót; P3 không gặp sự cố khi nhóm nhỏ ngồi cùng phòng. Không coi một lời kể là nguyên nhân chung của toàn bộ khảo sát.

## 5. Kết luận

Giả thuyết ở `evidence/hypothesis.md` (đếm lần 1, N = 22): **đạt hai ngưỡng đã viết trước** (59.1% từng đặt hộ ≥ 50%; 53.8% gặp sự cố ≥ 1/3), **nhưng lệch ở nguyên nhân**: sự cố hay gặp nhất là *thiếu món / phải đổi món* (6/13) và *vượt dự tính* (2/13); **không ai** chọn *nhầm món cho người ăn chay / dị ứng* (0/13), và chỉ 3/13 nhóm có người kiêng. Phần lớn đã dùng giỏ nhóm của app hoặc gửi menu vào chat (7/13 mỗi cách). Điều vẫn chưa biết: sự cố "thiếu / đổi món" do người đặt chọn sai hay do quán làm sai; mẫu còn nhỏ và là bạn cùng khoá — đã bổ sung ba ghi chép phỏng vấn bên dưới; cần hoàn thiện metadata và xác minh các điểm chưa rõ.

## Lịch hẹn (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| | | |

## 6. Nguồn khảo sát công khai bổ sung — phần Cấn Xuân Nghĩa

Báo cáo [nghiên cứu nguồn công khai](secondary-research.md) ghi rõ hai khảo sát do **ezCater** công bố năm **2023** và **2024**, mẫu người thường đặt đồ ăn cho nơi làm việc, vị trí trang và URL báo cáo gốc. Đây là số liệu bên ngoài, **không** phải khảo sát của nhóm và không cộng vào mẫu số của nhóm. Năm ví dụ công khai có trích dẫn và ngữ cảnh riêng; không phải người Aliba6 đã phỏng vấn.
## 7. Đối chiếu ba cuộc hỏi — cập nhật từ ghi chép của Nghĩa

- P1 và P2 có chi phí phối hợp/chọn món, nhưng P1 tránh được nhầm món bằng cách tách đơn; P2 vẫn có lỗi yêu cầu riêng dù dùng giỏ nhóm.
- P3 là phản chứng cần giữ: nhóm nhỏ, ngồi cạnh nhau, quán quen không báo nhầm món hoặc vượt tiền. Không suy rộng cho mọi nhóm ≤4 người. Ba phút chưa bao gồm rõ thời gian chọn quán.
- Mốc 2/3 chỉ mô tả ba hồ sơ có vai khác nhau. Không cộng ba cuộc hỏi vào số phiếu khảo sát, chưa xác nhận họ tương ứng dòng nào trong Form.
- Metadata còn thiếu: ngày giờ, hình thức, người hỏi/ghi chép; cần xác nhận đồng ý ghi âm cho P1/P2. Ghi chép có mốc ngày tương đối, không tự quy đổi. Không có lịch hẹn mới hoặc tệp ghi âm đính kèm trong bản cập nhật này.
