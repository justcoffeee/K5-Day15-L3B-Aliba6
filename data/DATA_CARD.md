# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6.
> Một trang. Mỗi dataset một mục.

## Dataset 1 · Menu synthetic đặt cơm hộ nhóm

| | |
|---|---|
| Dùng để làm gì | nguồn menu cho công cụ tra cứu · bộ câu thử evaluation · mô phỏng hành vi chọn món |
| Từ đâu | Nhóm tự sinh, dựa trên giả thuyết đặt cơm hộ trong `evidence/hypothesis.md` |
| Xử lý những bước gì | Dựng 7 món có mã, giá, thành phần, nhãn chay; lưu JSON; seed cố định 20261127 |
| Số dòng / số đoạn | 7 món |
| Phiên bản / ngày lấy | phiên bản 1 · 27/11/2026 |
| Nhãn | `synthetic` |
| Giới hạn | Không phải menu quán thật, không chứng minh pain, không có dữ liệu dị ứng hoặc giá real-time |

**Data `synthetic` (nhóm tự sinh):** file `data/menu-synthetic.json`, seed `20261127`, tạo và kiểm tay bởi Nguyễn Mạnh Hùng. Cách sinh: lập danh sách món mẫu có mã M01-M07, giá nội bộ VND, thành phần rõ ràng và nhãn chay. Hai món M02/M04 là chay; M06 có đậu phộng; M07 có mè. Đã kiểm tay 7/7 món có mã, giá, thành phần và nhãn nhất quán.
