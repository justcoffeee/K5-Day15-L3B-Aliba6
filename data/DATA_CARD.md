# Data card — dữ liệu bản chạy thử dùng

> Bản đầu CP2 (27/11/2026). Nhóm Aliba6 · Track D2. Đủ ở CP3.

## Dataset 1 · Menu giả 2 quán (`data/menu.json`)

| | |
|---|---|
| Dùng để làm gì | Nguồn cho công cụ `get_menu`, `safe_dishes`, `validate_cart` · căn cứ để chấm metric `an_toan_rang_buoc`, `tong_tien_dung_ngan_sach` |
| Từ đâu | **Nhóm tự viết tay.** Không chép menu quán thật nào. Tên món, giá phỏng theo mức giá cơm / bún văn phòng thông thường *(tự ước tính)* |
| Xử lý những bước gì | Viết tay → gắn tag thành phần bằng mã không dấu (`ga`, `dau_phong`, `nuoc_mam`…) → cố ý để 2 món `ingredients: null` (quán không ghi thành phần) và 1 món có đậu phộng mà tên không lộ (`B02 Bún thịt nướng`) để thử tình huống khó |
| Số dòng / số đoạn | 2 quán · 21 món (Quán Cơm Mẫu 14 món, ship 20.000đ · Quán Bún Mẫu 7 món, ship 25.000đ) · 5 món chay theo định nghĩa chặt |
| Phiên bản / ngày lấy | v1 · 27/11/2026 (ghi trong trường `phien_ban` của file) |
| Nhãn | `synthetic` |
| Giới hạn | Menu thật dài hơn, có topping, size, phí dịch vụ, khuyến mãi — chưa có. Tag thành phần giả định là đúng; ngoài đời quán có thể ghi thiếu (vì vậy output luôn nhắc người dị ứng nặng hỏi lại quán). Chỉ 2 quán nên đề xuất "đổi quán" rất hẹp |

**Cách sinh:** soạn tay cùng coding agent (Claude Code), không dùng seed. Người phụ trách: Nguyễn Mạnh Hùng *(cặp Y)* · người kiểm lại tag từng món: __ — đã kiểm __/21 món *(điền sau khi kiểm)*.

**Quy ước "ăn chay"** (chốt chặt để không chọn nhầm): không thịt, cá, hải sản, nước mắm, mắm tôm, trứng. Người "ăn chay có trứng" hiện bị coi như ăn chay chặt — an toàn hơn, chỉ ít lựa chọn hơn.

**Bảng từ → tag dị ứng / kiêng** nằm ở `codebase/tools.py` (`INGREDIENT_WORDS`): vd "hải sản" chặn cả `tom, muc, cua, ca, mam_tom`; "đậu nành" chặn cả `dau_nanh, dau_hu`. Khi không chắc, chặn rộng hơn.

**Không phải bằng chứng pain.** Data này chỉ để chạy thử và chấm; bằng chứng pain nằm ở `evidence/`.

## Dataset 2 · Câu trả lời khảo sát (`evidence/survey/results.csv`) — chưa có

Sẽ điền khi chốt khảo sát: số phiếu, giờ mở / chốt, đã xoá cột liên hệ và dấu thời gian. Câu 9 (chuyện trục trặc) là nguồn để viết lại thành câu thử `nguoi_dung` cho `eval/benchmark.csv`. Bản gốc `raw-*.csv` không commit.
