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

**Cách sinh:** soạn tay cùng coding agent (Claude Code), không dùng seed. Người phụ trách: Nguyễn Mạnh Hùng *(cặp Y)* · người kiểm lại tag từng món: Lê Thanh Tùng *(cặp X)* — đã kiểm 21/21 món *(đạt chuẩn 100% đối chiếu với NON_VEG và INGREDIENT_WORDS)*.

### Kết quả kiểm định 21 món của Lê Thanh Tùng:
- **Quán Cơm Mẫu (`com_mau` - 14 món):**
  - **Món chay (4 món an toàn):** `C05` Cơm đậu hũ sốt cà (35k), `C06` Cơm rau xào nấm (35k), `C08` Xôi lạc (25k), `C10` Mì xào chay (40k).
  - **Món mặn (9 món):** `C01` Cơm gà xối mỡ, `C02` Cơm sườn nướng, `C03` Cơm bò lúc lắc, `C04` Cơm chiên dương châu (có trứng, tôm), `C07` Gỏi gà trộn lạc (có đậu phộng), `C09` Cơm cá kho, `C12` Canh chua tôm, `C13` Cơm trứng ốp la, `C14` Bánh mì chả.
  - **Món không rõ thành phần (`null` - 1 món):** `C11` Cơm đặc biệt của quán (55k) — đúng thiết kế để loại bỏ khi người dùng có ràng buộc ăn kiêng.
- **Quán Bún Mẫu (`bun_mau` - 7 món):**
  - **Món chay (1 món an toàn):** `B04` Bún chay (40k - bún, đậu hũ, nấm, rau).
  - **Món mặn (5 món):** `B01` Bún chả, `B02` Bún thịt nướng (chứa `dau_phong` dù tên không lộ), `B03` Bún bò Huế (có `mam_tom`), `B05` Phở gà, `B06` Bún riêu cua (`cua`, `mam_tom`).
  - **Món không rõ thành phần (`null` - 1 món):** `B07` Nem rán (20k - `ingredients: null`).

**Quy ước "ăn chay"** (chốt chặt để không chọn nhầm): không thịt, cá, hải sản, nước mắm, mắm tôm, trứng. Người "ăn chay có trứng" hiện bị coi như ăn chay chặt — an toàn hơn, chỉ ít lựa chọn hơn.

**Bảng từ → tag dị ứng / kiêng** nằm ở `codebase/tools.py` (`INGREDIENT_WORDS`): vd "hải sản" chặn cả `tom, muc, cua, ca, mam_tom`; "đậu nành" chặn cả `dau_nanh, dau_hu`. Khi không chắc, chặn rộng hơn.

**Không phải bằng chứng pain.** Data này chỉ để chạy thử và chấm; bằng chứng pain nằm ở `evidence/`.

## Dataset 2 · Câu trả lời khảo sát (`evidence/survey/results.csv`) — chưa có

Sẽ điền khi chốt khảo sát: số phiếu, giờ mở / chốt, đã xoá cột liên hệ và dấu thời gian. Câu 9 (chuyện trục trặc) là nguồn để viết lại thành câu thử `nguoi_dung` cho `eval/benchmark.csv`. Bản gốc `raw-*.csv` không commit.
