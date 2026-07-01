# I. Strava

## 1. Introduction

### a. Product Introduction

Strava is a mobile and web platform for tracking, analyzing, and sharing physical activity — a hybrid of a GPS activity tracker and a social network for active people. Its own homepage describes it as offering "Community-Powered Motivation" and calls itself "the social network for those who strive." It is officially categorized as **Health & Fitness** on the App Store, and supports 50+ activity types (walking, running, cycling, swimming, hiking, indoor training, etc.).

Functionally, Strava combines three layers:
- **Recording**: GPS-based tracking of distance, time, pace/speed, and elevation for an activity.
- **Review**: post-activity analytics (laps, pace chart, elevation chart, personal records).
- **Social/competitive layer**: activity feed, kudos, comments, segments (timed sections of road/trail with leaderboards), clubs, and challenges.

Sources: strava.com homepage, App Store listing (see `strava-product-description.md` for verified quotes).

### b. User Goal

The core goal a user comes to Strava for is to **record a physical activity with minimal effort and see basic performance data afterward** (distance, time, pace). This project's own first-hand test confirms this narrow "core value" mental model directly: *"Core value => Ấn Start, Stop, Resume, Finish Walk"* (see `strava-usage-context-notes.md`). Beyond that core loop, Strava also supports secondary goals — reviewing detailed performance trends over time, discovering routes/segments, and connecting socially through kudos, clubs, and challenges — but these were only explored as deliberate testing, not as an organic first-time need.

### c. Primary Users

Verified data (Strava's Year in Sport Trend Report, 2026) shows running remains the single most-tracked sport on the platform, with racing on the rise. However, the platform's primary audience is broader than a "competitive runner/cyclist" stereotype: **93% of users cite health as their primary motivator**, not competition.

### d. Secondary Users

- **Walking is the #2 most-recorded activity type** on Strava — meaning a casual walker (like the account used for this project) represents a large, mainstream segment, not an edge case.
- Cyclists, swimmers, hikers, and triathletes.
- Competitive/segment-focused athletes who rely on leaderboards and structured training data.
- Socially-driven users who join clubs and challenges (Gen Z is a growing segment here).
- 54% of users track multiple activity types; 96% participate in multiple sports — cross-activity use is the norm, not the exception.

Source: `strava-product-description.md` (verified via WebSearch, 2026-07-01).

### e. Device and Knowledge Requirements

**Device**: iOS or Android smartphone (this project's test account used an **iPhone**), or the web dashboard at strava.com. Strava also supports Wear OS, native Apple Watch recording, and third-party GPS device sync (Garmin, Wahoo, Suunto, Polar, Fitbit, Coros).

**Account tier**: Strava splits functionality into Free and Subscription tiers. The Free tier (used for this project) covers recording, community features, and safety features; Subscription unlocks route-building, offline routes, training history, advanced workout analysis, goal tracking, segment leaderboards, and fitness scoring (verified list in `strava-platform-info.md`). A first-time free-tier user will repeatedly hit paywall prompts while exploring — confirmed directly in this project's screenshots (recurring "Start a free trial"/"Subscribe" prompts across Maps, Workout Analysis, You/Progress, You/Workouts, and Groups screens).

**Prior knowledge required**: none to operate the core Start → Pause/Resume → Finish recording loop — this project's first-time user completed it without hesitation. However, secondary features (Segments, Route filters, subscription-gated analytics) were **not** understandable on first sight and required trial-and-error tapping to figure out (confirmed first-hand, see Use Case 3 below).

---

## 2. Use case 1: Record, Finish, and Save an Outdoor Walk

### a. Analyze use case 1

**Goal**: capture GPS-based distance/time/pace data for a walk in real time, then save it as a permanent record.
**Trigger**: user opens the Record tab and taps Start.
**Steps observed** (from screenshots, `strava-screenshot-inventory.md` Flow 1):
1. In-progress recording screen — live map, live stats (Time/Distance/Speed), Pause button.
2. Tap Pause → Stopped screen — large-number stat display (Distance, Avg Speed), Resume/Finish buttons.
3. Tap Finish → Save Activity, screen 1 (title, description, activity type dropdown, map preview, tags).
4. Scroll to Save Activity, screen 2 (How did that feel?, private notes, gear, Visibility settings, Mute Activity, Save Activity button).
5. Tap Save Activity → "Nice work!" transition animation.
6. → "Welcome to the team, Duy!" first-activity achievement popup (View Activity / View in Trophy Case).
7. → Share Activity sheet is auto-presented (map+stats card, Share to Message/Strava Message/Strava Post/Copy Link/More).

That is **5 distinct screens/steps between tapping Finish and reaching a stable end state** — not a single confirmation.

### b. Context and method users interaction with this use case via interface

#### i. Context 1

- **Where**: Outdoors, on a real street (An Loi Dong Ward, Ho Chi Minh City — per the activity's location metadata).
- **When**: Early morning, 06:09–06:15 (device clock, from screenshot timestamps).
- **User Situation**: Walking — body in motion, not seated. This was the account's **first-ever Strava activity** (confirmed by the "Kudos on your first activity!" badge and "Welcome to the team, Duy!" popup).
- **Interaction Method**: One-handed touch. Attention divided between watching the path ahead and glancing down at the phone to check pace/duration (confirmed first-hand: *"đi vừa nhìn phía trước vừa check chỉ số của walk session như pace, duration"*).
- **Expected Outcome**: An accurate record of the walk (distance, time, route), saved for later review — with sharing treated as optional, not automatic.

### c. Apply HCI principle (Benefit & Drawbacks)

#### i. Human capability

- **Benefit**: The in-progress and Stopped screens use large, high-contrast numerals for Time/Distance/Speed, readable via brief downward glances — appropriate for a user whose visual attention must stay mostly forward while walking, not fixed on the screen.
- **Drawback**: Pause/Resume/Finish confirmation is purely visual (large button, color change) with no confirmed audio or haptic cue. For a user glancing at the screen only briefly while moving, a visual-only confirmation is easier to miss than a spoken or vibration cue would be.

#### ii. User mental model

- **Benefit**: The Start → Pause/Resume → Finish sequence maps directly onto the real-world action of "going for a walk, then stopping." This required no learning — the user's own account confirms this is exactly their mental model of the app's entire purpose (*"Core value => Ấn Start, Stop, Resume, Finish Walk"*).
- **Drawback — confirmed mismatch**: Immediately after tapping Finish, the user expected to land in an activity history/detail view (with sharing available *if wanted*). Instead, the system moved directly into a Save Activity form, then an unrequested achievement popup, then an auto-presented Share Activity sheet. Quoted directly: *"Trong suy nghĩ hơi khác của tôi là sau khi ấn Finish (walk) thì nó hiện ra phần share buổi đi bộ => Kiểu hơi lạ."* This is a specific, observed violation of the user's expected system state, not a generic "confusing flow" claim.

#### iii. Interaction metaphors

- **Benefit**: Resume/Pause use standard media-player icons (▶ / ❚❚), and "Finish" uses a checkered-flag icon — both metaphors are borrowed from contexts (music/video players, racing) the user already knows, so no Strava-specific learning was needed to operate them.

#### iv. Usability

- **Learnability**: High for this specific loop. As a genuine first-time user with no prior Strava exposure, the Start/Pause/Resume/Finish sequence was operated without hesitation or reported errors.
- **Efficiency**: Minimal taps required for the core task (Start, optional Pause/Resume, Finish) — but efficiency drops after Finish, where 4 additional un-skippable-feeling screens appear before the user reaches a stable end state.
- **Errors**: No accidental taps were reported during the recording portion itself.

### d. Different User Types and Contexts

#### i. Beginners

Directly represented by this use case — confirmed learnable on first attempt with no training.

#### ii. Experienced users

Not tested in this project (only one first-time session was observed). It's reasonable to expect the Finish → Save → Share sequence would become a known, anticipated pattern with repeated use, reducing the mismatch described above — but this is an inference, not confirmed data.

#### iii. Elderly users

Not tested. Large button targets (the wide Pause/Resume/Finish bar) are favorable in principle, but no elderly user was involved in this session to confirm.

#### iv. Users with disabilities

Not tested — no screen-reader or accessibility settings were explored in this session.

#### v. Environmental constraints (sunlight, noise, movement, poor internet, etc.)

The observed session happened outdoors in daylight with a stable 4G signal throughout (visible in every screenshot's status bar). Direct sunlight glare on the app's black background, or GPS signal loss in denser urban areas, were **not** encountered or reported — these remain open, untested risks rather than confirmed drawbacks.

### e. Propose specific HCI-based solutions

- **For the Finish → Share mismatch**: insert a lightweight, skippable confirmation screen immediately after Finish (e.g., "Activity saved. View it now, or share later?") *before* the achievement popup and share sheet. This preserves the user's expected mental model (Finish = done) while still offering sharing as an optional next step instead of an automatic one.
- **For the visual-only Pause/Finish confirmation**: add a short haptic tap on state change (Start/Pause/Resume/Finish), so confirmation doesn't rely solely on a glance at the screen while the user is walking.

---

## 3. Use case 2: Reviewing Post-Activity Stats

### a. Analyze use case 2

**Goal**: understand how the just-completed activity went — distance, pace, elevation, splits.
**Trigger**: user opens the saved activity and scrolls through its detail/analysis screens.
**Screens observed** (`strava-screenshot-inventory.md` Flow 2): Activity detail (distance/moving time/elevation gain) → Workout Analysis (laps, flyover map) → Elevation chart → Pace chart (Avg Pace, Moving Time, Avg Elapsed Pace, Elapsed Time, Fastest Split).

### b. Context and method users interaction with this use case via interface

#### i. Context 1

- **Where / When / User Situation**: **Not explicitly confirmed** by the first-hand notes collected for this project — it is not stated whether this review happened immediately after finishing (still outdoors) or later while seated. This should be confirmed before final submission rather than assumed.
- **Interaction Method**: Scrolling and tapping through a single-column stats screen, on the same iPhone device.
- **Expected Outcome**: Quickly understand how the activity went, using the displayed metrics.

### c. Apply HCI principle (Benefit & Drawbacks)

#### i. Human capability

- **Benefit**: Data is presented as large-number stat blocks and charts (Elevation, Pace) rather than dense tables, reducing the visual/cognitive effort needed to scan results.
- **Drawback**: Multiple similarly-named metrics are shown close together with no inline explanation — see mental model section below for the specific confirmed confusion.

#### ii. User mental model

- **Drawback — confirmed confusion**: The user could not distinguish between **Avg Pace, Avg Elapsed Pace, Moving Time, and Elapsed Time** shown together on the same screen (`IMG_0527`). Quoted directly: *"Có mấy cái như Avg Elapsed Time + Elapsed Time + Fastest Split là tôi không hiểu làm gì?"* This is a concrete terminology/learnability problem, not a generic "confusing UI" claim — the user was forced to guess rather than recognize what each metric meant.

#### iii. Interaction metaphors

Charts (elevation profile, pace-over-distance) use familiar line/area-chart conventions from general data visualization — no Strava-specific interaction metaphor issue was observed here.

#### iv. Usability

- **Learnability**: Low for this specific screen — confirmed the user could not interpret several metric labels without external help.
- **Errors**: None observed (this is a read-only review screen), but misreading a stat (e.g., confusing Moving Time with Elapsed Time) is a plausible consequence of the labeling confusion, though not directly observed as a downstream error in this session.

### d. Different User Types and Contexts

#### i. Beginners

Directly represented — this is the exact confusion a first-time user hit.

#### ii. Experienced users

Likely already know the difference between "moving time" (time actually in motion) and "elapsed time" (total time including pauses) from prior fitness-tracking experience — but this is an inference, not tested in this project.

#### iii–v. Elderly / disabilities / environmental constraints

Not tested in this project.

### e. Propose specific HCI-based solutions

- Add a brief inline info icon (already present for "Pace" and "Elevation" section headers, per `IMG_0526`/`0527` — but its content was not opened/tested in this session) that explicitly defines Moving Time vs. Elapsed Time, and Avg Pace vs. Avg Elapsed Pace, directly next to the metric on first view, rather than requiring the user to seek out or already know the distinction.

---

## 4. Use case 3: Exploring the Maps Tab (Segments)

### a. Analyze use case 3

**Goal**: discover nearby routes/segments to run or walk in the future.
**Trigger**: user taps the Maps tab from the bottom navigation.
**Screens observed**: Routes sub-view (Length/Elevation/Surface/Difficulty filters, Create Route, Suggested Routes) and Segments sub-tab (map with segment pins, "Popular segments" list showing distance, grade, athlete/effort counts — `IMG_0530`).

### b. Context and method users interaction with this use case via interface

#### i. Context 1

- **Where / When / User Situation**: Continued from the same first-time exploration session as Use Case 1–2; **not explicitly confirmed** whether this specific step happened while still walking or after stopping.
- **Interaction Method**: Tapping between multiple sub-tabs (Segments, Length, Elevation, Surface) by trial and error rather than by understanding labels upfront — confirmed first-hand: *"Tôi phải ấn thử nhiều tab mới hiểu."*
- **Expected Outcome**: Understand what a "segment" is and how it differs from a "route" without needing outside help.

### c. Apply HCI principle (Benefit & Drawbacks)

#### i. Human capability

No specific vision/motor/hearing constraint was reported for this use case beyond normal touch/visual interaction with a map screen.

#### ii. User mental model

- **Drawback — confirmed confusion**: The user did not understand what "Segments" meant, or how it differed from the route-length/elevation/surface filters, on first sight. Quoted directly: *"Ko, tôi chả hiểu lắm... Tôi phải ấn thử nhiều tab mới hiểu."* This is a first-time user encountering Strava-specific jargon ("Segment" = a fixed, competitive timed section of road/trail with a leaderboard) with no in-context explanation on the tab itself.

#### iii. Interaction metaphors

The tab bar (Segments / Length / Elevation / Surface / Difficulty) uses generic pill-button styling with no icon or visual distinction to hint at what each does differently — the metaphor here is closer to a plain filter list than something self-explanatory, which likely contributed to the trial-and-error behavior observed.

#### iv. Usability

- **Learnability**: Low for a first-time user — confirmed only understood after actively tapping through multiple tabs, not from reading labels alone.

### d. Different User Types and Contexts

#### i. Beginners

Directly represented — this is the exact use case observed.

#### ii–v. Experienced / elderly / disabilities / environmental constraints

Not tested in this project. An experienced runner already familiar with the "segment" concept from other platforms (e.g., Zwift, Garmin Connect) would likely not face the same confusion — but this is an inference based on general fitness-app conventions, not directly tested here.

### e. Propose specific HCI-based solutions

- Add a one-line explanatory subtitle under the "Segments" tab label the first time a user opens Maps (e.g., "Segments: timed sections other athletes compete on") rather than relying on the label alone or requiring trial-and-error exploration to learn the term.

---

## 5. Use case 4: Exploring Groups — Challenges & Clubs

### a. Analyze use case 4

**Goal**: explore what the Groups tab offers (Active / Challenges / Clubs sub-tabs) — for Active/Challenges, this was open-ended curiosity rather than a pre-existing need; for Clubs specifically, the user had a genuine goal: find a running club active in their own running area.
**Trigger**: user taps the Groups tab from bottom navigation.
**Steps observed**: Active sub-tab ("Design Your Own Challenge" paywall + joined-challenge progress bars) → Challenges sub-tab ("July 5K Challenge" card, Join button, "Recommended For You") → tap Join on the challenge card → button changes state, no navigation occurs → Clubs sub-tab ("Create Your Own Strava Club" promo, "The Strava Club" banner).

### b. Context and method users interaction with this use case via interface

#### i. Context 1

- **Where / When**: A separate session from the recorded walk (not the same sitting).
- **User Situation**: Deliberately exploring/testing the app's features, not fulfilling an urgent task — self-described intent was curiosity for Active/Challenges; for Clubs, a real goal existed (finding a nearby running club).
- **Interaction Method**: Visual attention goes straight to the most prominent actionable element (the Join button) on each card; the user taps it directly without reading its label or pausing to consider what it does. Confirmed first-hand: *"When i see a club card or challenge card, i will focus to button and enter it without reading 'join'... and understand that I need to enter another space to open detail page of this challenge."*
- **Expected Outcome**: Tapping Join was expected to open a detail page for the challenge. For Clubs, the expectation was to discover a running club active near the user's own running location.

### c. Apply HCI principle (Benefit & Drawbacks)

#### i. Human capability

- **Drawback**: The Join button's high visual salience (bright orange, primary-CTA styling) draws the user's attention and hand directly to it, bypassing the surrounding card text. This is a specific case of visual salience overriding reading/comprehension — the user's own account confirms attention narrowed to the button and skipped past understanding what the button vs. the rest of the card each do.

#### ii. User mental model

- **Drawback — confirmed mismatch**: The user expected tapping Join to lead to a detail page. Instead, tapping only toggled the button's own state, with no navigation. Quoted directly: *"Nothing happens, the button just change the status. What I expect is it jump into the more detail."* The user never discovered that opening the card itself (elsewhere than the button) might reveal more detail, because attention stayed fixed on the button: *"I refuse in finding out how can i see the detail by focusing into button without reading and thinking the feature of button."* This is a discoverability failure caused by an ambiguous split between "tap the button" (a quick action) and "tap the card" (navigation) — the interface gives no visual cue that these are two different tap targets.

#### iii. Interaction metaphors

- **Drawback**: challenge/club cards mix two different metaphors on one surface — "card as a button" (tap to act, e.g. Join) and "card as a link" (tap to open detail) — with no visual distinction (like a chevron or "View Details" label) separating them. This ambiguity is exactly what produced the confirmed confusion above.

#### iv. Usability

- **Learnability**: Low for discovering the detail view — the user never found it in this session, despite repeated exposure to challenge/club cards.
- **Errors**: No destructive error occurred (tapping Join is reversible/harmless), but the user also never confirmed whether "Join" succeeded in any meaningful way beyond the button label changing — a visibility-of-system-status gap.
- **Satisfaction**: The user reported feeling "normal" about the mismatch, attributing this to their own exploratory/testing mindset rather than genuine investment in the outcome — confirmed directly: *"No. I feel normal. Maybe because I just wanna test."* This suggests the same mismatch could register as more frustrating for a user with a real, urgent goal, rather than someone deliberately testing the app.

**For Clubs specifically**: the user's actual goal — finding a running club active in their own running area — was **not fulfilled** (confirmed: answered "No" when asked if they left feeling they'd accomplished something). What was shown instead was a generic "Create Your Own Strava Club" promo and "The Strava Club" (Strava's own official club), with no location- or activity-based club search/discovery visible in the screenshots reviewed for this project. This should be read as "not found in this session," not as confirmed proof that no such feature exists elsewhere in the app.

### d. Different User Types and Contexts

#### i. Beginners

Directly represented — this is the user's own first exposure to Groups/Challenges/Clubs.

#### ii. Experienced users

Not tested. A user already familiar with card-based social apps (e.g., event or group-listing apps) might already expect a "tap card body vs. tap button" convention — but this is an inference, not confirmed data.

#### iii–v. Elderly / disabilities / environmental constraints

Not tested in this project.

### e. Propose specific HCI-based solutions

- Add a distinct "View Details" affordance (e.g., a chevron icon, or making the full card body tappable with a separate, visually smaller Join button) so joining and viewing details are spatially and visually distinguishable, instead of overlapping on the same tap target.
- After tapping Join, show a brief, explicit confirmation (e.g., "Joined! Tap here to see challenge details") so the state change is visible and immediately offers the path to detail the user was originally looking for.
- For Clubs: if location- or activity-based club discovery exists elsewhere in the app, surface a "Find a club near you" or "Find a Walk/Run club" entry point directly on the Clubs tab's landing view, rather than only showing "Create your own" and the single official Strava Club.

---

## Notes on Scope and Evidence

- Per project scope (see `CLAUDE.md`), this document covers **Product 1 (Strava) only**. Product 2 is a teammate's responsibility.
- Use cases above are limited to the flows with **confirmed first-hand context** (`strava-usage-context-notes.md`). Other observed flows (You/Workouts, Settings) are cataloged in `strava-screenshot-inventory.md` but not yet written up as full use cases, pending first-hand context.
- Each use case's "e. Propose specific HCI-based solutions" subsection is Requirement 2 content, kept inline in this same document per the assignment template — both requirements live together in `report.md`.
