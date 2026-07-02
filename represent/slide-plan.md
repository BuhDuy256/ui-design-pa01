# Slide Plan — Kiến trúc bài thuyết trình Strava (CSC13112 · PA1)

> Tài liệu này giải thích **kiến trúc** của bài nói, không phải nội dung slide.
> Câu hỏi cốt lõi khi thiết kế: làm sao để khán giả **tự quan sát vấn đề trước**, rồi mới nghe lý thuyết HCI.

---

## Ý tưởng xuyên suốt (spine của cả bài)

Toàn bộ report có 4 use case, nhưng nếu trình bày lần lượt 4 use case thì bài nói sẽ rời rạc và giống "đọc lại report".

Thay vào đó, mình rút ra **một câu chuyện duy nhất** ẩn bên trong report:

> **Vòng lặp ghi hoạt động (core loop) được thiết kế cho người mới. Mọi thứ xung quanh nó lại giả định người dùng đã biết Strava.**

Cả 4 phát hiện đều là **một biểu hiện** của khoảng cách đó. Đây chính là "Overall Mental Model" mà report tự ghi nhận (core value dễ học; phần ngoại vi thì không).

Nhờ vậy, dòng chảy cảm xúc là: **khen core loop → cú lật (Finish ≠ Done) → 3 bức tường → chốt lại pattern → giải pháp**. Quan sát luôn đi trước lý thuyết.

---

## Bảng kiến trúc theo từng slide

### Slide 1 — Title
- **Tiêu đề:** What a first-time user really sees in Strava
- **Mục tiêu:** Mở bằng lời hứa (một nghiên cứu quan sát người mới), không mở bằng mô tả sản phẩm.
- **Khán giả phải hiểu:** Đây là nghiên cứu dựa trên quan sát thực tế, không phải review tính năng.
- **Vì sao slide này tồn tại:** Định khung "observation-first" ngay từ đầu.
- **Vì sao đặt ở đây:** Bắt buộc là slide đầu.
- **Takeaway:** "Chúng tôi quan sát người mới thật."
- **Thời lượng:** ~15s
- **Chuyển tiếp:** "Vậy người mới đó là ai, và chúng tôi quan sát thế nào?"

### Slide 2 — Context & Method
- **Tiêu đề:** Who we watched — and how
- **Mục tiêu:** Tạo độ tin cậy cho phương pháp: 1 người mới, 1 buổi walk thật, iPhone, free tier.
- **Khán giả phải hiểu:** Bài phân tích dựa trên hành vi thật, và ta nhìn theo góc người mới.
- **Vì sao tồn tại:** Không có context thì mọi phát hiện phía sau thành "ý kiến cá nhân".
- **Vì sao đặt ở đây:** Phải nạp bối cảnh trước khi quan sát.
- **Takeaway:** "Ta nghiên cứu con đường thật của người mới, không phải của chuyên gia."
- **Thời lượng:** ~40s
- **Chuyển tiếp:** "Việc đầu tiên người mới làm là ghi một buổi đi bộ — và nó chạy tốt."

### Slide 3 — The Core Loop Works (Baseline)
- **Tiêu đề:** The core loop just works
- **Mục tiêu:** Thiết lập **mốc so sánh tích cực**. Khen thật lòng để lát nữa vấn đề "đau" hơn.
- **Khán giả phải hiểu:** Start → Pause → Resume → Finish rất dễ, người mới làm được ngay.
- **Vì sao tồn tại:** Nếu không có baseline này, cú lật ở Slide 4 mất sức nặng.
- **Vì sao đặt ở đây:** Ngay trước cú lật — tạo tương phản.
- **Takeaway:** "Core loop miễn nhiễm với người mới. Hãy nhớ điều này."
- **Thời lượng:** ~40s
- **Chuyển tiếp:** "Nhưng đúng ở bước cuối cùng — bước Finish — mọi thứ đổi."

### Slide 4 — Finding 1: Finish ≠ Done (Cú lật)
- **Tiêu đề:** They tapped "Finish" — expecting it to end
- **Mục tiêu:** Cho khán giả **cảm nhận** vấn đề trước khi nghe lý thuyết. Đây là điểm cao trào.
- **Khán giả phải hiểu:** Người dùng bấm Finish mong "xong", nhưng bị đẩy qua 5 màn hình.
- **Vì sao tồn tại:** Đây là phát hiện mạnh nhất, dùng làm ca "deep-dive" điển hình.
- **Vì sao đặt ở đây:** Ngay sau baseline để tạo cú lật; mở đầu chuỗi phát hiện.
- **Takeaway:** "Finish không kết thúc tác vụ — nó bắt đầu một tác vụ mới."
- **Thời lượng:** ~55s
- **Chuyển tiếp:** "Vì sao điều này khiến người dùng thấy lạ?"

### Slide 5 — Finding 1: Why + Fix
- **Tiêu đề:** The task never reached "closure"
- **Mục tiêu:** Bây giờ **mới** đưa lý thuyết, vì khán giả đã tự cảm nhận vấn đề.
- **Khán giả phải hiểu:** Mental model (Finish = done) + Golden Rule #4 (closure) + #7 (control). Giải pháp: màn hình chốt + haptic.
- **Vì sao tồn tại:** Hoàn thành chuỗi Observe → Reasoning → Solution cho ca điển hình.
- **Vì sao đặt ở đây:** Ngay sau khi khán giả "thấy đau" ở Slide 4.
- **Takeaway:** "Cho tác vụ một điểm kết thúc rõ ràng mà người dùng kiểm soát."
- **Thời lượng:** ~50s
- **Chuyển tiếp:** "Đó mới chỉ là bước cuối của core loop. Ra khỏi nó thì sao?"

### Slide 6 — Transition / Pattern set-up
- **Tiêu đề:** The core loop was built for a beginner. The rest was not.
- **Mục tiêu:** Slide bản lề — zoom out, gieo pattern, preview 3 phát hiện còn lại.
- **Khán giả phải hiểu:** Ba phát hiện tiếp theo cùng một dạng "bức tường".
- **Vì sao tồn tại:** Tránh cảm giác "liệt kê 3 lỗi rời rạc"; tạo mạch.
- **Vì sao đặt ở đây:** Chuyển từ deep-dive (1 ca) sang quét nhanh (3 ca).
- **Takeaway:** "Một con đường được đánh bóng, xung quanh là lãnh địa của chuyên gia."
- **Thời lượng:** ~25s (bản lề, nói nhanh)
- **Chuyển tiếp:** "Bức tường thứ nhất: những con số không đọc nổi."

### Slide 7 — Finding 2: Unreadable stats
- **Tiêu đề:** Numbers the user couldn't read
- **Mục tiêu:** Quan sát trước (ảnh Pace) → nhãn gần trùng nhau → recall vs recognition → fix.
- **Khán giả phải hiểu:** 4 nhãn na ná nhau buộc người dùng đoán nghĩa.
- **Vì sao tồn tại:** Minh hoạ nguyên tắc "recognition over recall" + "speak the user's language".
- **Vì sao đặt ở đây:** Bức tường #1 trong bộ ba; ngay sau slide bản lề.
- **Takeaway:** "Nhãn na ná nhau buộc phải đoán, không phải đọc."
- **Thời lượng:** ~45s
- **Chuyển tiếp:** "Nếu con số khó, thì từ ngữ còn khó hơn."

### Slide 8 — Finding 3: "Segment"?
- **Tiêu đề:** "Segment"? — learned by trial and error
- **Mục tiêu:** Thuật ngữ lạ + các tab trông giống hệt nhau → học bằng cách bấm thử.
- **Khán giả phải hiểu:** "Segment" vô nghĩa với người mới; giao diện không giải thích.
- **Vì sao tồn tại:** Củng cố pattern "jargon" bằng một ca khác vị trí (Maps).
- **Vì sao đặt ở đây:** Bức tường #2; nối tiếp chủ đề ngôn ngữ từ Slide 7.
- **Takeaway:** "Các tab trông giống nhau che giấu độ khó rất khác nhau."
- **Thời lượng:** ~45s
- **Chuyển tiếp:** "Hai cái trên là hiểu sai chữ. Cái tiếp theo là hiểu sai hành động."

### Slide 9 — Finding 4: The Join trap
- **Tiêu đề:** The "Join" trap
- **Mục tiêu:** Ca tương tác mạnh nhất: mắt nhảy tới nút cam, bấm, mong mở chi tiết — nhưng chỉ toggle im lặng.
- **Khán giả phải hiểu:** Một tap target đang gánh hai việc khác nhau (join vs xem chi tiết).
- **Vì sao tồn tại:** Chuyển pattern từ "ngôn ngữ" sang "conceptual model / affordance".
- **Vì sao đặt ở đây:** Bức tường #3 — đỉnh của bộ ba trước khi tổng hợp.
- **Takeaway:** "Một tap target đang làm hai việc khác nhau."
- **Thời lượng:** ~55s
- **Chuyển tiếp:** "Bốn phát hiện — nhưng thực ra chỉ là một câu chuyện."

### Slide 10 — The Pattern (Synthesis)
- **Tiêu đề:** One pattern behind all four findings
- **Mục tiêu:** Điểm chốt trí tuệ của bài. Gộp 4 phát hiện thành 1 câu.
- **Khán giả phải hiểu:** Core = ngôn ngữ của người mới; ngoại vi = giả định đã biết Strava.
- **Vì sao tồn tại:** Biến "danh sách lỗi" thành "một luận điểm nghiên cứu".
- **Vì sao đặt ở đây:** Sau khi đủ 4 bằng chứng; ngay trước giải pháp.
- **Takeaway:** "Strava onboard hành động, không onboard từ vựng."
- **Thời lượng:** ~40s
- **Chuyển tiếp:** "Vậy sửa thế nào — mà vẫn khả thi cho một team thật?"

### Slide 11 — Takeaways / Solutions
- **Tiêu đề:** Three cheap moves, all realistic
- **Mục tiêu:** Gom giải pháp thành 3 nhóm, mỗi nhóm gắn lại các phát hiện.
- **Khán giả phải hiểu:** Giải pháp rẻ, khả thi, không phải tính năng viển vông.
- **Vì sao tồn tại:** Người nghe (đặc biệt giảng viên) muốn thấy đề xuất có tính hành động.
- **Vì sao đặt ở đây:** Kết của mạch Problem → Solution ở cấp toàn bài.
- **Takeaway:** "Gợi ý nhỏ đặt đúng chỗ biến 'bấm thử' thành 'nhận ra'."
- **Thời lượng:** ~45s
- **Chuyển tiếp:** "Tóm lại trong một câu…"

### Slide 12 — Thank you / Q&A
- **Tiêu đề:** Strava onboards the action, not the vocabulary.
- **Mục tiêu:** Nhắc lại luận điểm một câu, mời hỏi.
- **Khán giả phải hiểu:** Đây là điều duy nhất cần nhớ nếu quên hết.
- **Vì sao tồn tại:** Đóng khung + mở Q&A.
- **Vì sao đặt ở đây:** Slide cuối.
- **Takeaway:** Câu thesis.
- **Thời lượng:** ~15s
- **Chuyển tiếp:** Kết thúc.

---

## Tổng thời lượng dự kiến
~8 phút 30 giây (nằm gọn trong khung 5–10 phút, còn dư biên cho Q&A và nhịp nói chậm).

## Nguyên tắc thiết kế đã áp dụng
- **Mỗi slide trả lời đúng 1 câu hỏi**, để lại đúng 1 takeaway (pill "KEY").
- **Quan sát trước, lý thuyết sau** — Finding 1 tách hẳn Observe (S4) và Why (S5) để làm gương mẫu cho phương pháp.
- **Deep-dive 1 ca + quét nhanh 3 ca** — tránh lặp cấu trúc 4 lần gây buồn ngủ.
- **Không có slide thừa** — slide bản lề (S6) và tổng hợp (S10) đều gánh nhiệm vụ dẫn dắt, không phải trang trí.
