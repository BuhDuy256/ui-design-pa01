# Slide Content — Strava (CSC13112 · PA1)

> **Cấu trúc bám theo deck Garmin của bạn cùng nhóm** (để đồng bộ). Mỗi use case = 8 slide, lặp y hệt:
>
> 1. **Overview** — tên use case + tóm tắt + ảnh sản phẩm
> 2. **User Interaction Context** — bối cảnh + cách tương tác
> 3. **Human Capabilities** — 4 ô: Vision & Attention · Touch & Motor · Audio & Haptic Feedback · Memory & Cognition (Benefits/Drawbacks). *Đã chỉnh cho app điện thoại: "Hearing" → "Audio & Haptic Feedback".*
> 4. **User Mental Model** — Benefits/Drawbacks
> 5. **Interaction Metaphors** — Benefits/Drawbacks
> 6. **Usability** — Learnability · Efficiency · Errors · Satisfaction
> 7. **Different User Types & Contexts** — Beginners · Experienced · Elderly · Disabilities · Environmental
> 8. **HCI Solutions** — giải pháp gắn với drawback
>
> Slide content: **English**. Ghi chú/ảnh: tiếng Việt.
> **Header mọi slide:** badge cam `Use Case N` (trái) · tiêu đề navy · `STRAVA` (phải trên) — giống template Garmin.
>
> ⚠️ **Số slide:** 8 × 4 = 32 (+ intro/kết ≈ 36). Nếu quá giờ: với UC3 (nội dung Human Capability mỏng) gộp slide 3+4+5 thành 1 slide "HCI Analysis". Chỗ nào report không có dữ liệu, mình ghi rõ "not a major factor" — **không bịa finding**.

---

## INTRO

### Slide — Title
- **STRAVA** — Product Research
- CSC13112 · UI/UX Design · PA1
- [Họ tên – MSSV]

**Ảnh:** logo Strava / 1 ảnh app mờ làm nền. *Lý do:* slide mở sạch.

### Slide — Product & Users
- **What:** GPS activity tracker + social layer (record → review → share)
- **Core goal:** record an activity, see basic stats — distance, time, pace
- **Primary users:** health-focused active people (93% cite health, not competition)
- **Secondary:** walkers (#2 activity), cyclists, swimmers, club/social users
- **Platform:** iOS / Android / web — **this study: iPhone, Free tier, first-time user**

**Ảnh:** `IMG_0521` (activity detail). *Lý do:* cho thấy dữ liệu thật.

---
---

# USE CASE 1 — Record, Finish, and Save an Outdoor Walk

### UC1 · Slide 1 — Overview
- Record a walk with GPS, then save it as a permanent record
- Core loop: **Start → Pause → Resume → Finish**
- Live stats while moving: time, distance, speed
- First-ever activity for this user

**Ảnh:** `IMG_0514` (recording screen). *Lý do:* ảnh "anh hùng" cho use case, thấy loop đang chạy.

### UC1 · Slide 2 — User Interaction Context
- **While Recording (outdoors)**
  - Outdoor street, early morning (~06:09)
  - One-handed touch, walking — not seated
  - Eyes split between the path ahead and the screen
- **At Finish (still standing)**
  - Taps Finish expecting the task to end
  - Wants an accurate saved record; sharing = optional

**Ảnh:** `IMG_0515` (Stopped — Resume/Finish). *Lý do:* neo khoảnh khắc trước khi bấm Finish.

### UC1 · Slide 3 — Human Capabilities
- **Vision & Attention**
  - *Benefit:* Large, high-contrast central numbers readable in a quick glance (foveal focus)
  - *Drawback:* Black recording screen is glare-prone in direct sunlight (potential)
- **Touch & Motor**
  - *Benefit:* Wide Pause/Resume/Finish bar = large targets, easy one-handed
  - *Drawback:* Tapping while walking raises mis-tap risk
- **Audio & Haptic Feedback**
  - *Drawback:* No audio or haptic confirmation — Start/Pause/Finish rely on sight only, while eyes are on the path
- **Memory & Cognition**
  - *Benefit:* Core loop matches a known routine → low memory load
  - *Drawback:* Post-Finish flow adds steps to process when task felt done

**Ảnh:** không (4 ô chữ, giống slide Garmin). Tùy chọn: crop cụm số từ `IMG_0515`.

### UC1 · Slide 4 — User Mental Model
- *Benefit:* Start → Pause/Resume → Finish maps to "go, then stop" — no new model needed
- *Drawback:* User expects **Finish = done**; system inserts **5 screens** (Save → "Nice work!" → Achievement → Share sheet) before it ends
- Quote: *"It shows a screen to share the walk — felt strange."*

**Ảnh:** `IMG_0522` (Share sheet, tự bật). *Lý do:* bằng chứng "Finish ≠ done".

### UC1 · Slide 5 — Interaction Metaphors
- *Benefit:* ▶ / ❚❚ borrowed from media players; 🏁 checkered flag from racing → understood instantly
- *Drawback:* None observed — metaphors work well here

**Ảnh:** crop nút Resume/Finish từ `IMG_0515`. *Lý do:* cho thấy icon quen thuộc.

### UC1 · Slide 6 — Usability
- **Learnability:** High — first-timer completed the loop with no help
- **Efficiency:** Good while recording; drops after Finish (4 extra screens)
- **Errors:** None during recording
- **Satisfaction:** Forced share prompt felt "strange"

**Ảnh:** flow diagram `Finish → Save → Nice work → Achievement → Share` (node cuối tô cam).

### UC1 · Slide 7 — Different User Types & Contexts
- **Beginners:** directly represented — loop learned instantly
- **Experienced:** anticipate the Save→Share sequence; extra taps still remain
- **Elderly:** large buttons help; not tested
- **Disabilities:** visual-only feedback risky for screen-reader / low-vision users
- **Environmental:** daylight OK; glare on black screen + GPS drift = potential risks

**Ảnh:** không (slide chữ).

### UC1 · Slide 8 — HCI Solutions
- One **closure screen** after Finish: "Saved. View now · Share later" — sharing optional
- Add **haptic buzz** on Start / Pause / Finish → eyes stay on the road
- *Principle:* Golden Rule #4 (closure) + #7 (user control); multi-channel feedback

**Ảnh:** mockup màn "Saved · View / Share later". *Lý do:* minh hoạ giải pháp.

---
---

# USE CASE 2 — Reviewing Post-Activity Stats

### UC2 · Slide 1 — Overview
- Understand how the finished walk went
- Metrics: distance, pace, elevation, splits
- Screens: Activity detail → Workout Analysis → Elevation → Pace

**Ảnh:** `IMG_0521` (activity detail). *Lý do:* ảnh mở của luồng xem lại.

### UC2 · Slide 2 — User Interaction Context
- **Post-Walk Review (still / seated)**
  - Same session, opening the saved activity on the iPhone
  - Scroll & tap through a single-column stats screen
  - Goal: quickly read how the walk went

**Ảnh:** `IMG_0525` (Workout Analysis). *Lý do:* thể hiện màn phân tích.

### UC2 · Slide 3 — Human Capabilities
- **Vision & Attention**
  - *Benefit:* Big stat blocks & charts, high contrast — easy to scan
  - *Drawback:* Four near-identical labels sit close → hard to tell apart at a glance
- **Touch & Motor**
  - *Not a primary channel* — simple scroll & tap, single column
- **Audio & Haptic Feedback**
  - *Not a primary channel* — read-only visual screen
- **Memory & Cognition**
  - *Benefit:* Chunking — grouped stat blocks cut scanning load
  - *Drawback:* Ambiguous labels force recalling meanings → higher load

**Ảnh:** không. Tùy chọn: crop 4 nhãn từ `IMG_0527`.

### UC2 · Slide 4 — User Mental Model
- *Drawback:* Avg Pace · Avg Elapsed Pace · Moving Time · Elapsed Time — no cue to tell apart → forces **recall**, not **recognition**
- *Drawback:* Near-duplicate wording reads as jargon, not plain language
- Quote: *"I don't understand what they're for."*

**Ảnh:** `IMG_0527` (Pace screen) — **khoanh đỏ 4 nhãn**. *Lý do:* vấn đề nằm ở chính nhãn.

### UC2 · Slide 5 — Interaction Metaphors
- *Benefit:* Line / area charts use familiar data-viz conventions → no learning needed
- *Drawback:* None observed on this screen

**Ảnh:** `IMG_0526` (Elevation chart). *Lý do:* biểu đồ quen thuộc.

### UC2 · Slide 6 — Usability
- **Learnability:** Low for this screen — labels not understood without help
- **Efficiency:** Guessing slows down reading
- **Errors:** Read-only, but risk of misreading Moving vs Elapsed Time
- **Satisfaction:** Confusion, not failure

**Ảnh:** không.

### UC2 · Slide 7 — Different User Types & Contexts
- **Beginners:** hit the confusion directly
- **Experienced:** know Moving vs Elapsed Time; "Elapsed Pace" still Strava-specific
- **Elderly / Disabilities / Environmental:** not tested

**Ảnh:** không.

### UC2 · Slide 8 — HCI Solutions
- **Info icon + one-line definition** next to each ambiguous metric, shown on first view, dismissible
- Converts a **recall** task into a **recognition** task
- *Principle:* recognition over recall; speak the user's language

**Ảnh:** mockup nhãn "Moving Time ⓘ" + tooltip. *Lý do:* giải pháp tại đúng vị trí.

---
---

# USE CASE 3 — Exploring the Maps Tab (Segments)

### UC3 · Slide 1 — Overview
- Discover nearby routes / segments to run or walk later
- Maps tab: Routes sub-view + Segments sub-tab
- Goal: understand "Segment" vs "Route"

**Ảnh:** `IMG_0529` (Maps · Routes). *Lý do:* điểm xuất phát của tab Maps.

### UC3 · Slide 2 — User Interaction Context
- **Exploring (first-time, curious)**
  - Same first-time session
  - Tapping between sub-tabs (Segments / Length / Elevation / Surface)
  - By **trial and error**, not by reading labels

**Ảnh:** `IMG_0530` (Segments tab). *Lý do:* màn hình chính của use case.

### UC3 · Slide 3 — Human Capabilities
- **Vision & Attention**
  - *Minor:* dense segment pins & labels crowd the map (mild)
- **Touch & Motor**
  - *Not a primary channel* — normal tapping
- **Audio & Haptic Feedback**
  - *Not a primary channel*
- **Memory & Cognition**
  - *Drawback:* "Segment" jargon with no cue increases load — user must hold in mind what each tab does

> 🗒️ *Ghi chú (VN):* report ghi rõ UC3 "không có ràng buộc vision/motor/hearing đặc biệt" — đây là use case mỏng nhất về capability, trọng tâm nằm ở Mental Model + Metaphors. Nếu cần cắt giờ, **gộp slide 3+4+5 thành một slide "HCI Analysis"**.

**Ảnh:** không.

### UC3 · Slide 4 — User Mental Model
- *Drawback:* "Segment" is Strava-specific jargon with no in-context definition → no existing model to map onto
- *Drawback:* Learned **by trying** (trial-and-error) = least efficient learning mode
- Quote: *"I had to tap several tabs before I understood."*

**Ảnh:** `IMG_0530` — khoanh chữ "Segments". *Lý do:* thuật ngữ không được giải thích.

### UC3 · Slide 5 — Interaction Metaphors
- *Drawback:* **Affordance without meaning** — Segments / Length / Elevation / Surface share identical pill styling
- Equal look suggests equal difficulty, but only "Segments" needs prior knowledge

**Ảnh:** crop hàng tab từ `IMG_0530`. *Lý do:* cho thấy các tab giống hệt nhau.

### UC3 · Slide 6 — Usability
- **Learnability:** Low — understood only after tapping around
- **Efficiency:** Trial-and-error wastes time
- **Errors / Satisfaction:** Confusion, mild frustration

**Ảnh:** không.

### UC3 · Slide 7 — Different User Types & Contexts
- **Beginners:** exact confusion observed
- **Experienced (Zwift / Garmin):** recognize "segment" immediately — shared convention
- **Elderly / Disabilities / Environmental:** not tested

**Ảnh:** không.

### UC3 · Slide 8 — HCI Solutions
- **One-line subtitle** under "Segments" on first open
- e.g., *"Segments: timed sections other athletes compete on"*
- Turns trial-and-error into a quick read
- *Principle:* speak the user's language; recognition over recall

**Ảnh:** mockup tab "Segments" + phụ đề. *Lý do:* giải pháp ngay trên tab.

---
---

# USE CASE 4 — Exploring Groups (Challenges & Clubs)

### UC4 · Slide 1 — Overview
- Explore the Groups tab: Active · Challenges · Clubs
- Challenges = curiosity; **Clubs = real goal** (find a nearby running club)
- Cards with a prominent **Join** button

**Ảnh:** `IMG_0532` (Groups · Active). *Lý do:* giới thiệu không gian Groups.

### UC4 · Slide 2 — User Interaction Context
- **Exploring (separate session)**
  - Deliberately testing features, not an urgent task
  - Eye jumps straight to the bright **Join** button
  - Taps it **without reading** the label first

**Ảnh:** `IMG_0533` (Challenge card + Join). *Lý do:* thẻ trung tâm của use case.

### UC4 · Slide 3 — Human Capabilities
- **Vision & Attention**
  - *Drawback:* Bright orange Join button = strongest contrast → pulls the eye before the card is read (peripheral attention)
- **Touch & Motor**
  - *Drawback:* User taps the salient button reflexively, without reading
- **Audio & Haptic Feedback**
  - *Drawback:* Join only changes color silently; no audio/haptic cue, and "view details" gives no feedback in any channel
- **Memory & Cognition**
  - *Drawback:* One tap target doing two jobs adds confusion; no cue for "view details"

**Ảnh:** `IMG_0533` — vòng sáng quanh nút Join. *Lý do:* thể hiện nút hút mắt.

### UC4 · Slide 4 — User Mental Model
- *Drawback:* Conceptual model = "tap the prominent element → see detail"
- Reality = "tap Join → toggle state only, nothing opens"
- Quote: *"Nothing happens… I expect it jumps into more detail."*

**Ảnh:** `IMG_0533` + mũi tên "tap → nothing opens (✕)". *Lý do:* diễn tả kỳ vọng vs thực tế.

### UC4 · Slide 5 — Interaction Metaphors
- *Drawback:* **Consistency & affordance** — Join (state toggle) and "open detail" (navigation) share one surface
- No distinct affordance separates the two different actions

**Ảnh:** crop thẻ `IMG_0533`. *Lý do:* một bề mặt gánh hai hành động.

### UC4 · Slide 6 — Usability
- **Learnability:** Low — never found the detail view
- **Feedback / Visibility:** Join toggle has feedback; "view details" has **none** → invisible action
- **Satisfaction:** "felt normal" (testing mindset) — would frustrate a real goal
- **Task gap (Clubs):** goal "find a nearby running club" unmet — only "Create your own" + official club

**Ảnh:** `IMG_0534` (Clubs tab). *Lý do:* cho thấy không có lối "tìm club gần nhà".

### UC4 · Slide 7 — Different User Types & Contexts
- **Beginners:** first exposure — hit the trap
- **Experienced:** card-app convention might help, but Strava doesn't separate the actions
- **Elderly / Disabilities / Environmental:** not tested

**Ảnh:** không.

### UC4 · Slide 8 — HCI Solutions
- Make the **card body tappable** = open details; shrink Join into a **separate, smaller** button
- After Join: *"Joined! Tap here to see details"*
- Add **"Find a club near you"** entry on the Clubs tab
- *Principle:* different things should look different; feedback & visibility; task-to-feature mapping

**Ảnh:** mockup thẻ tách hai hành động. *Lý do:* minh hoạ giải pháp affordance.

---
---

## CLOSING

### Slide — What We Learned
- Core recording loop: easy, matches expectations ✓
- Around it: jargon · no closure · unclear taps ✗
- Fixes are small & in-context: **clear endings · plain language · one job per tap**

**Ảnh:** không (2 cột ✓ / ✗).

### Slide — Thank You / Q&A
- Thank you — Questions?
- CSC13112 · PA1 · Strava · [Họ tên – MSSV]

**Ảnh:** không.

---
---

## Tổng hợp ảnh

**Bắt buộc (6):** `IMG_0514` · `IMG_0521` · `IMG_0522` · `IMG_0527` · `IMG_0530` · `IMG_0533`
**Phụ / tùy chọn (6):** `IMG_0515` · `IMG_0525` · `IMG_0526` · `IMG_0529` · `IMG_0532` · `IMG_0534`

## Quy ước highlight (nhất quán cả deck)
- **Vòng / viền cam** = chỗ có vấn đề (nút Join, tab Segments, 4 nhãn Pace).
- **Viền xanh** = chỗ làm tốt / giải pháp.
- Ảnh điện thoại: tỉ lệ 9:16, bo góc, viền mảnh.

## Human Capabilities — đã chỉnh cho Strava (app điện thoại)
4 ô dùng chung cả deck: **Vision & Attention · Touch & Motor · Audio & Haptic Feedback · Memory & Cognition**
- Đổi "Hearing" (của deck Garmin, hợp đồng hồ có audio) → **Audio & Haptic Feedback**, vì vấn đề thật của Strava là xác nhận thao tác **chỉ bằng thị giác**, thiếu audio/haptic.
- Gộp attention vào **Vision & Attention** để chứa cả "đọc số vùng foveal" (UC1) lẫn "nút cam hút mắt" (UC4) — đúng phần Human vision trong LN02.
- Kênh nào report không quan sát được → ghi thẳng **"Not a primary channel"** (giữ khung 4 ô, không bịa finding).

**Bản đồ kênh chính theo use case** (✓✓ = trọng tâm, ✓ = có, – = không phải yếu tố):

| Use case | Vision & Attention | Touch & Motor | Audio & Haptic | Memory & Cognition |
|---|---|---|---|---|
| UC1 Record walk | ✓✓ | ✓ | ✓✓ | ✓ |
| UC2 Stats | ✓✓ | – | – | ✓✓ |
| UC3 Segments | ✓ | – | – | ✓ |
| UC4 Join | ✓✓ | ✓ | ✓✓ | ✓ |

## Tránh trùng lặp giữa 2 slide
- **Memory & Cognition (ô Human Capability):** năng lực thô — chunking, recall vs recognition, tải bộ nhớ.
- **User Mental Model (slide 4):** diễn giải kỳ vọng — "Finish = done", "tap nút → mở chi tiết".
