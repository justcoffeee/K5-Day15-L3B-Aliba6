# Tổng hợp bằng chứng pain

> Cập nhật CP2 (27/11/2026) · Nhóm Aliba6 · Track D2.

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☑ Đạt (N = 24 người ngoài nhóm) | `evidence/survey/results.csv` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☑ Đạt (3/3 người ngoài nhóm: P1, P2, P3) | `evidence/interviews/P1.md`, `P2.md`, `P3.md` |

## 2. Số chính

- **Khảo sát:**
  - Quy mô mẫu: **N = 24** học viên L3A, L3B ngoài nhóm Aliba6.
  - Tỉ lệ từng đặt hộ nhóm ≥3 người trong 1 tháng qua: **24/24 (100%)**.
  - Tỉ lệ trong nhóm có người ăn chay / dị ứng / kiêng: **18/24 (75.0%)**.
  - Tỉ lệ từng gặp sự cố (nhầm món, vượt tiền, thiếu món): **20/24 (83.3%)** — vượt xa giả thuyết ban đầu (≥1/3).
  - Tỉ lệ mất thời gian gom món > 10 phút: **18/24 (75.0%)**, trong đó 5/24 mất > 20 phút.
  - Phân phối tần suất đặt hộ/tháng: Ít (1–3 lần): 11 người (45.8%) · Vừa (4–5 lần): 9 người (37.5%) · Nhiều (≥6 lần): 4 người (16.7%).
- **Phỏng vấn:**
  - **3/3 người** đều gặp sự cố nghiêm trọng (nhầm chất dị ứng đậu phộng/hải sản, vượt ngân sách phải bù tiền túi, mất 18–28 phút/đơn).

| | Vai | Gặp pain? | Số lần / 1 tháng qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | Học viên L3B, đặt cơm cho nhóm lab 5 người | Có | 6 lần | 25 phút | Nhắn tin Zalo rồi tự nhẩm cộng tiền |
| P2 | Học viên L3A, đặt cơm nhóm Capstone 4 người | Có | 4 lần | 18 phút | Dò từng dòng mô tả món trên app |
| P3 | Học viên L3B, đặt cơm nhóm học dồn 6 người | Có | 8 lần | 28 phút | Giỏ nhóm app Grab/ShopeeFood |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (từ khảo sát và phỏng vấn)

1. *"Nhóm có bạn dị ứng lạc nặng, mình đặt bún thịt nướng tưởng an toàn ai ngờ quán rắc đầy đậu phộng vụn lên trên, bạn ấy phải nhịn trưa ăn bánh mì ngọt."* — P1 & Phiếu khảo sát #2
2. *"Một bạn dị ứng hải sản dặn không tôm mực, quán làm món có tôm khô băm nhỏ bên trong, bạn ấy ăn một miếng bị ngứa cổ họng ngay lập tức."* — P2 & Phiếu khảo sát #19
3. *"Nhóm 6 người có 2 bạn ăn chay trường, tìm quán cơm thì không có đồ chay, sang quán chay thì mấy bạn nam kêu ăn không no, cãi nhau mất gần nửa tiếng trưa."* — P3 & Phiếu khảo sát #14
4. *"Lúc tính tiền món thì vừa khít ngân sách 180k, đến lúc bấm thanh toán app cộng thêm tiền ship 28k với phụ phí làm mình toàn phải tự bù tiền túi."* — P1 & Phiếu khảo sát #1
5. *"Mỗi lần nhận trách nhiệm đặt cơm trưa cho team là stress vì người ăn kiêng keto, người ăn chay, người dị ứng, vừa tính tiền vừa sợ nhầm."* — Phiếu khảo sát #20

## 4. Các nguồn có khớp nhau không

- Khảo sát định lượng (N=24) và phỏng vấn định tính (P1–P3) **khớp nhau hoàn toàn**:
  - Hơn 83% người đặt hộ từng gặp sự cố và 75% tốn >10 phút.
  - Cả hai nguồn đều chỉ ra 2 rủi ro nhức nhối nhất: (1) Rủi ro sức khỏe do **thành phần ẩn trong món ăn** (đậu phộng trong bún thịt nướng, tôm khô trong cơm rang) mà người đặt không lường trước được; (2) Rủi ro tài chính do **quên tính phí ship** dẫn đến vượt ngân sách nhóm.

## 5. Kết luận

- Giả thuyết ở `evidence/hypothesis.md`: **ĐÚNG VÀ NGHIÊM TRỌNG HƠN DỰ KIẾN.**
- Tỉ lệ gặp sự cố thực tế đạt **83.3%** (so với giả thuyết ≥33.3%).
- Điều này củng cố tính cấp thiết của giải pháp Track D2: Dùng code để tự động lọc sạch các món nguy hiểm trước khi AI chọn món và kiểm tra cứng tổng tiền gồm phí ship bằng code.

## 6. Nguồn khảo sát công khai bổ sung — phần Cấn Xuân Nghĩa

Báo cáo [nghiên cứu nguồn công khai](secondary-research.md) ghi rõ hai khảo sát do **ezCater** công bố năm **2023** và **2024**, mẫu người thường đặt đồ ăn cho nơi làm việc, vị trí trang và URL báo cáo gốc. Các tỷ lệ trong báo cáo bổ sung là số liệu bên ngoài, không cộng vào N=24 của nhóm. Năm ví dụ công khai có trích dẫn và ngữ cảnh riêng; không phải người Aliba6 đã phỏng vấn. Đợt nghiên cứu nguồn công khai này chưa xác minh nguồn gốc của dữ liệu khảo sát/phỏng vấn nội bộ ở các mục trên.
