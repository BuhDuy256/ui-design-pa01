# Assets Plan — Hình ảnh, icon, mũi tên, highlight cho từng slide

> Mỗi mục ghi rõ **cần gì** và **vì sao cần** (lý do phục vụ câu chuyện, không chỉ trang trí).
> Tất cả ảnh nằm trong thư mục `strava-images/`. Trong `slides.html` đang để placeholder dạng `[IMG_xxxx]`; khi dựng lại trên Canva thì thay bằng ảnh thật.

---

## Slide 1 — Title
- **Ảnh:** không cần (hoặc 1 ảnh phone mờ làm nền, tuỳ chọn).
- **Icon:** không.
- **Highlight/annotation:** không.
- **Animation:** tiêu đề fade-in nhẹ (đã có sẵn).
- **Lý do:** Slide mở phải "sạch". Đưa ảnh thao tác vào đây sẽ tiết lộ vấn đề quá sớm, phá thế "observation-first".

## Slide 2 — Context & Method
- **Ảnh:** không bắt buộc. Nếu muốn, dùng **IMG_0521** (activity detail) thu nhỏ ở góc để gợi "buổi walk thật".
- **Icon:** iPhone, người đi bộ, đồng hồ (6 AM) — dạng line icon đơn sắc.
- **Highlight:** làm nổi câu quote "Start, Stop, Resume, Finish".
- **Lý do:** Slide này bán **độ tin cậy của phương pháp**, nên icon giúp nhớ nhanh "1 người / 1 walk / iPhone / free". Quote là bằng chứng người mới tự định nghĩa core value → chuẩn bị cho baseline.

## Slide 3 — The Core Loop Works
- **Ảnh (bắt buộc):**
  - **IMG_0514** — màn hình đang ghi (live map + nút Pause).
  - **IMG_0515** — màn hình Stopped (nút Resume / Finish).
- **Icon:** ▶ (play), ❚❚ (pause), 🏁 (checkered flag) — để nối với "metaphor quen thuộc".
- **Mũi tên:** flow ngang Start → Pause → Resume → Finish.
- **Highlight:** khoanh nút Pause (0514) và cụm Resume/Finish (0515).
- **Lý do:** Phải cho khán giả **thấy** loop đơn giản thế nào thì lời khen "beginner-proof" mới có sức. Hai ảnh cạnh nhau = hai trạng thái của cùng một loop.

## Slide 4 — Finding 1: Finish ≠ Done
- **Ảnh (bắt buộc):** **IMG_0522** — Share sheet tự bật lên.
- **Ảnh phụ (tuỳ chọn, nếu còn chỗ):** IMG_0517 / IMG_0519 / IMG_0520 để minh hoạ chuỗi màn hình.
- **Mũi tên:** flow Finish → Save form → "Nice work!" → Achievement → **Share sheet** (node cuối tô đỏ).
- **Highlight:** node "Share sheet" tô cam/đỏ + số **"5 screens"** phóng to.
- **Annotation:** dán câu quote ngay cạnh ảnh Share sheet.
- **Animation (hữu ích):** cho 5 node của flow xuất hiện **lần lượt** — mỗi lần bấm thêm 1 màn, khán giả "chịu đựng" cùng người dùng. Đây là slide đáng đầu tư animation nhất.
- **Lý do:** Cảm giác "sao mãi chưa xong" phải được **trải nghiệm bằng mắt**. IMG_0522 là bằng chứng share bị ép, đúng câu quote.

## Slide 5 — Finding 1: Why + Fix
- **Ảnh:** không cần ảnh mới (slide lý thuyết + giải pháp). Giữ text/diagram để mắt nghỉ sau slide 4 dày ảnh.
- **Icon:** khoá closure (dấu ✓ trong vòng tròn), rung (haptic).
- **Chip HCI:** "Mental model", "Golden Rule #4 — closure", "Golden Rule #7 — control".
- **Callout FIX:** 2 hộp xanh (màn chốt + haptic).
- **Lý do:** Có chủ đích **không** để ảnh — nhịp thị giác cần một slide "thở" sau slide cao trào, và để nhấn rằng đây là phần suy luận.

## Slide 6 — Transition
- **Ảnh:** không.
- **Icon:** không (hoặc 3 icon nhỏ đại diện 3 phát hiện: bảng số / thẻ tab / con trỏ bấm).
- **Mũi tên:** hàng ngang "2 · Stats — 3 · Segment — 4 · Join".
- **Animation:** 3 node preview xuất hiện lần lượt.
- **Lý do:** Slide bản lề cần **trống thoáng** để tạo khoảng lặng và báo hiệu chuyển chương. Ảnh sẽ làm loãng chức năng "hinge".

## Slide 7 — Finding 2: Unreadable stats
- **Ảnh (bắt buộc):** **IMG_0527** — màn Pace (Avg Pace / Moving Time / Avg Elapsed Pace / Elapsed Time / Fastest Split).
- **Highlight (quan trọng):** khoanh đỏ **4 nhãn gần trùng** trực tiếp trên ảnh; nối 2 cặp "Pace ↔ Elapsed Pace", "Moving ↔ Elapsed Time".
- **Chip HCI:** "Recall > Recognition", "Speak the user's language".
- **Callout FIX:** info icon tap-to-define.
- **Lý do:** Vấn đề nằm ở **chính các nhãn** — phải khoanh trên ảnh thật thì khán giả mới "thấy" sự na ná, thay vì nghe kể.

## Slide 8 — Finding 3: "Segment"?
- **Ảnh (bắt buộc):** **IMG_0530** — tab Segments (pin trên bản đồ + list Popular segments).
- **Ảnh phụ (tuỳ chọn):** IMG_0529 (Routes) để đối chiếu "cùng kiểu tab".
- **Highlight:** node "Segments" tô đỏ trong hàng tab; các tab còn lại để xám → cho thấy "trông giống nhau nhưng độ khó khác nhau".
- **Chip HCI:** "Jargon", "Learned by trying", "Affordance".
- **Callout FIX:** subtitle 1 dòng dưới "Segments".
- **Lý do:** Cần cho thấy **các tab đồng nhất về hình thức** — đó chính là cái bẫy affordance. Khoanh tab Segments để mắt biết nhìn đâu.

## Slide 9 — Finding 4: The Join trap
- **Ảnh (bắt buộc):** **IMG_0533** — thẻ July 5K Challenge với **nút Join cam**.
- **Highlight (quan trọng):** vòng sáng quanh nút Join cam để tái hiện "mắt nhảy tới đây trước".
- **Mũi tên:** mũi tên từ "mắt/ngón tay" → nút Join; kèm dấu ✕ hoặc "no navigation" để thể hiện bấm xong không đi đâu.
- **Chip HCI:** "Conceptual-model mismatch", "One tap = two jobs".
- **Callout FIX:** thẻ bấm mở chi tiết + nút Join nhỏ tách riêng.
- **Lý do:** Bản chất phát hiện là **độ tương phản màu hút mắt** + **không có phản hồi cho hành động xem chi tiết**. Vòng sáng quanh nút cam kể được cả hai điều này bằng hình.

## Slide 10 — The Pattern
- **Ảnh:** không (slide tổng hợp bằng chữ, đối lập 2 cột).
- **Icon:** ✓ xanh cho "Core loop", ✗ cam cho "Everything around it".
- **Layout:** 2 card so sánh trái/phải.
- **Lý do:** Đây là **luận điểm**, không phải bằng chứng — dùng tương phản hai cột để khán giả "chốt" bằng cấu trúc, không cần ảnh.

## Slide 11 — Takeaways / Solutions
- **Ảnh:** không.
- **Icon:** 3 số lớn (1,2,3) đã có; có thể thêm icon nhỏ: dấu ✓ closure / bong bóng chữ (language) / hai ô tách biệt (affordance).
- **Lý do:** Danh sách hành động cần **đọc lướt nhanh**; ảnh sẽ làm chậm. Mỗi giải pháp có ghi "(Finding x)" để truy vết ngược.

## Slide 12 — Thank you / Q&A
- **Ảnh:** không.
- **Lý do:** Kết sạch, chỉ còn câu thesis. Mắt khán giả nên dừng ở một câu duy nhất khi chuyển sang hỏi đáp.

---

## Ghi chú chung về visual
- **Bảng màu:** nền trắng, mực đậm `#1a1a1a`, xám phụ `#6b7280`, **cam Strava `#FC4C02` chỉ dùng để nhấn** (KEY pill, node xấu, highlight). Không lạm dụng cam.
- **Highlight nhất quán:** luôn dùng **vòng/viền cam** để chỉ "chỗ có vấn đề", **viền xanh** cho "chỗ làm tốt / giải pháp".
- **Ảnh điện thoại:** để tỉ lệ dọc 9:16, bo góc, viền mảnh — trông giống mockup thiết bị.
- **Ảnh bắt buộc tối thiểu (7 tấm):** IMG_0514, IMG_0515, IMG_0522, IMG_0527, IMG_0530, IMG_0533 — và IMG_0521 (tuỳ chọn cho slide 2). Các ảnh khác chỉ là phụ.
