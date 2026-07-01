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

- **Benefit — foveal vision** (*LN02, "Human vision"*: "the eye sees a small region in high detail (fovea)... put detail where the eye focuses"): the in-progress and Stopped screens place Time/Distance/Speed as large, high-contrast numerals centered on screen — exactly where a brief downward glance's fovea lands, appropriate given the user's gaze had to stay mostly on the path ahead.
- **Drawback — feedback channel** (*LN02, "Feedback"*: "actions should have immediate effects... feedback channels: audio, visual, haptic"; *LN02, "Motor system"*: "feedback is important... minimize eye movement"): Pause/Resume/Finish confirmation is delivered only through the **visual** channel (button color/label change). This conflicts with the "minimize eye movement" principle for a user who must keep their eyes mostly forward while walking — a haptic or audio channel would confirm the action without requiring a look.

#### ii. User mental model

- **Benefit — mental model match** (*LN02 definition*: "mental model... internal constructions... enabling predictions to be made... how to use it"): Start → Pause/Resume → Finish maps directly onto the real-world action "go for a walk, then stop." No new mental model was required — confirmed directly: *"Core value => Ấn Start, Stop, Resume, Finish Walk."*
- **Drawback — mental model violation, no closure** (*LN02 mental model definition*; *Shneiderman's Golden Rule #4, "Design dialogs to yield closure," LN02/LN03*; *LN03, "Prevent errors"*: "support complete sequences, e.g., wizards offering both Next and Finish"): the user's mental model predicted Finish = "done, land on activity view." Instead, the system inserted 4 more screens (Save form → "Nice work!" → achievement popup → Share sheet) before reaching a stable state — a sequence that does not "yield closure" at the point the user expected it, and does not offer a "Finish-only" path the way LN03's complete-sequence principle recommends. Quoted directly: *"Trong suy nghĩ hơi khác của tôi là sau khi ấn Finish (walk) thì nó hiện ra phần share buổi đi bộ."*

#### iii. Interaction metaphors

- **Benefit — familiar metaphor** (*LN02 definition*: "a set of user interface visuals, actions and procedures that exploit specific knowledge users already have of other domains"): Resume/Pause icons (▶ / ❚❚) and the checkered-flag "Finish" icon borrow directly from media-player and racing domains the user already knows, requiring no Strava-specific learning to operate.

#### iv. Usability

- **Learnability** (*LN01/LN02 usability dimension*): High — a genuine first-time user with no prior Strava exposure operated the core loop without hesitation.
- **Efficiency** (*LN02, "Usability goals & measurable targets"*: "Speed of performance — time to carry out benchmark tasks — reduce"): minimal taps for the core recording loop, but efficiency drops sharply after Finish — 4 extra, un-requested screens before a stable end state, directly working against the "reduce time to complete" goal for what the user considered a finished task.
- **Errors**: none reported during the recording portion itself.

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

- **Reasoning chain**: Observed issue — Finish is followed by 4 non-optional screens → Concept — this violates Shneiderman's Golden Rule #4 "design dialogs to yield closure" and Golden Rule #7 "support user control" (*LN02/LN03*), and breaks the user's mental model of Finish = done (*LN02*) → Design implication — the sequence needs an explicit closure point that the user controls → **Solution**: insert a lightweight, skippable confirmation immediately after Finish (e.g., "Activity saved. View it now, or share later?"), giving the flow an actual closure point matching the user's mental model, while keeping sharing as an optional, user-controlled step rather than a forced one.
- **Reasoning chain**: Observed issue — Pause/Finish confirmation is visual-only → Concept — this conflicts with *LN02*'s motor-system principle to "minimize eye movement" for a user in motion, and underuses the available feedback channels (audio/visual/haptic, *LN02 "Feedback"*) → Design implication — confirmation should not require looking at the screen → **Solution**: add a short haptic pulse on each state change (Start/Pause/Resume/Finish), so confirmation doesn't rely solely on a glance while the user is walking.

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

- **Benefit — chunking** (*LN02, "Chunking"*: "group and format information to reduce chunk count"): data is presented as large-number stat blocks and charts (Elevation, Pace) rather than dense tables, reducing the visual/cognitive scanning effort.
- **Drawback**: multiple similarly-named metrics are shown close together with no inline explanation — see mental model section below for the specific confirmed confusion.

#### ii. User mental model

- **Drawback — recognition vs. recall** (*LN02 core concept*: "Recognition: remembering with a visible cue... Recall: remembering with no cue... prefer recognition over recall"; *LN02, Common Mistakes*: "forcing recall when recognition would do"): **Avg Pace, Avg Elapsed Pace, Moving Time, and Elapsed Time** are shown with no visible cue distinguishing their meaning, forcing the user into a recall-like guessing process instead of recognition. Quoted directly: *"Có mấy cái như Avg Elapsed Time + Elapsed Time + Fastest Split là tôi không hiểu làm gì?"*
- **Drawback — consistency / user's language** (*LN02, "Consistency"*: "speak the user's language: common words, avoid slang/jargon"): "Elapsed Pace" alongside "Pace" and "Elapsed Time" alongside "Moving Time" reads as near-duplicate jargon rather than plain, distinguishable language — this is a specific, concrete instance of the "speak the user's language" principle being violated, not a generic complaint.

#### iii. Interaction metaphors

Charts (elevation profile, pace-over-distance) use familiar line/area-chart conventions from general data visualization — no Strava-specific interaction metaphor issue was observed here.

#### iv. Usability

- **Learnability** (*LN02, "Usability goals & measurable targets"*: "time to learn — how long to learn the actions for a task set — reduce"): Low for this specific screen — confirmed the user could not interpret several metric labels without external help, working against the "reduce time to learn" goal.
- **Errors** (*Shneiderman's Golden Rule #5, "prevent errors," LN02/LN03*): none observed directly (this is a read-only review screen), but misreading a stat (e.g., confusing Moving Time with Elapsed Time) is a plausible downstream error risk created by the labeling confusion, though not directly observed in this session.

### d. Different User Types and Contexts

#### i. Beginners

Directly represented — this is the exact confusion a first-time user hit.

#### ii. Experienced users

Likely already know the difference between "moving time" (time actually in motion) and "elapsed time" (total time including pauses) from prior fitness-tracking experience — but this is an inference, not tested in this project.

#### iii–v. Elderly / disabilities / environmental constraints

Not tested in this project.

### e. Propose specific HCI-based solutions

- **Reasoning chain**: Observed issue — user cannot distinguish Avg Pace/Avg Elapsed Pace/Moving Time/Elapsed Time → Concept — labels force **recall** instead of **recognition** (*LN02*), and violate "speak the user's language" (*LN02, Consistency*) by using near-duplicate jargon → Design implication — give the user a visible cue at the point of reading, not require prior domain knowledge → **Solution**: add a brief inline info icon/definition directly next to each ambiguous metric (Moving Time vs. Elapsed Time; Avg Pace vs. Avg Elapsed Pace) on first view. This converts a recall task into a recognition task and satisfies Shneiderman's Golden Rule #3, "offer informative feedback" (*LN02/LN03*).

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

- **Drawback — no existing mental model + consistency/jargon** (*LN02, "Consistency"*: "speak the user's language: common words, avoid slang/jargon"; *LN02 mental model definition*): "Segment" is Strava-specific terminology with no in-context definition. The user had no existing mental model to map it onto, and the interface built none — confirmed directly: *"Ko, tôi chả hiểu lắm... Tôi phải ấn thử nhiều tab mới hiểu."*
- **Drawback — recognition vs. recall, learned by trying** (*LN02*: "prefer recognition over recall"; *LN04, "requirements document / task analysis"*: task descriptions should record "how it's learned — training, install-and-use, by trying, by watching others"): with no visible cue explaining "Segment," the user had to learn its meaning **by trying** (trial-and-error tapping) — per LN04's own framework, "by trying" is a less efficient learning mode than a label being recognizable at a glance.

#### iii. Interaction metaphors

- **Drawback — affordance without meaning** (*LN02, "Affordances"*: "the object's appearance suggests how to use it — which one is a button?"): the tab bar (Segments / Length / Elevation / Surface / Difficulty) gives all tabs identical pill-button styling — equal affordance — but only some tabs (Length, Elevation, Surface) are self-explanatory filters, while "Segments" requires prior domain knowledge. Identical affordance across tabs of unequal difficulty misleads the user into expecting them to be equally easy to understand.

#### iv. Usability

- **Learnability** (*LN02, "Usability goals & measurable targets"*: "time to learn — reduce"): Low for a first-time user — confirmed only understood after actively tapping through multiple tabs, not from reading labels alone, working against the "reduce time to learn" goal.

### d. Different User Types and Contexts

#### i. Beginners

Directly represented — this is the exact use case observed.

#### ii–v. Experienced / elderly / disabilities / environmental constraints

Not tested in this project. An experienced runner already familiar with the "segment" concept from other platforms (e.g., Zwift, Garmin Connect) would likely not face the same confusion — but this is an inference based on general fitness-app conventions, not directly tested here.

### e. Propose specific HCI-based solutions

- **Reasoning chain**: Observed issue — "Segments" is not understood on first sight, learned only "by trying" → Concept — this violates "speak the user's language" (*LN02, Consistency*), gives no visible cue for **recognition** (*LN02*), and matches LN04's least-efficient learning mode ("by trying") rather than being learnable at a glance → Design implication — the label needs a visible, in-context definition → **Solution**: add a one-line explanatory subtitle under the "Segments" tab label the first time a user opens Maps (e.g., "Segments: timed sections other athletes compete on"), turning a trial-and-error task into a recognition task and shortening the "time to learn" usability goal (*LN02*).

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

- **Drawback — foveal attention capture** (*LN02, "Human vision"*: "the eye sees a small region in high detail (fovea)... put detail where the eye focuses"): the Join button's high-contrast orange, primary-CTA styling is the most visually salient element on the card, capturing the user's foveal fixation and directing action there first, at the expense of reading the surrounding card text. Confirmed directly: *"When i see a club card or challenge card, i will focus to button and enter it without reading 'join'..."*

#### ii. User mental model

- **Drawback — conceptual model mismatch** (*LN02 definition*: conceptual model = "the mental model people carry of how something should be done... described in core activities, objects, and interface metaphors"): the user's conceptual model was "tap the prominent element on a card → see more detail." The system's actual model was "tap Join → toggle local state only, no navigation." Quoted directly: *"Nothing happens, the button just change the status. What I expect is it jump into the more detail."* *"I refuse in finding out how can i see the detail by focusing into button without reading and thinking the feature of button."* This is a specific conceptual-model mismatch, not a vague "confusing card" complaint.

#### iii. Interaction metaphors

- **Drawback — consistency and affordances** (*LN02, "Consistency"*: "similar things should work similarly; different things should look different"; *LN02, "Affordances"*: "the object's appearance suggests how to use it — which one is a button?"): Join (a state-toggle action) and "open detail" (a navigation action) are two different operations overlapping on the same card surface with no distinct visual affordance separating them — a direct violation of the "different things should look different" principle.

#### iv. Usability

- **Learnability**: Low — the user never discovered the detail view in this session, despite repeated exposure to challenge/club cards.
- **Feedback / Visibility** (*LN02, "Feedback"*: "actions should have immediate effects"; *LN02, "Visibility"*: "operations should be visible to users"; *Shneiderman's Golden Rule #3, "offer informative feedback," LN02/LN03*): the button-label change is adequate feedback for the Join toggle itself, but the interface gives **no feedback and no visibility at all** for the separate operation of viewing details — that operation effectively doesn't exist from the user's point of view.
- **Satisfaction** (*LN01/LN02 usability dimension*): the user reported feeling "normal" about the mismatch, attributing this to an exploratory/testing mindset rather than genuine investment in the outcome — confirmed directly: *"No. I feel normal. Maybe because I just wanna test."* This suggests the same visibility/feedback gap could register as more frustrating for a user with a real, urgent goal.

**For Clubs specifically — task analysis gap** (*LN04, "Task analysis"*: each task's analysis should capture its **goal** and the **user environment** where it's performed; the requirements document should map real user goals to supporting features): the user's actual goal — finding a running club active in their own running area — was **not fulfilled** (confirmed: answered "No" when asked if they left feeling they'd accomplished something). What was shown instead was a generic "Create Your Own Strava Club" promo and "The Strava Club" (Strava's own official club), with no location- or activity-based club discovery visible in the screenshots reviewed. Per LN04, a properly captured task analysis for "find a club" should record the user's goal and environment explicitly — the absence of a corresponding entry point is evidence this goal wasn't matched to a discoverable feature (or the feature exists but wasn't surfaced), not proof the feature is entirely absent from the app.

### d. Different User Types and Contexts

#### i. Beginners

Directly represented — this is the user's own first exposure to Groups/Challenges/Clubs.

#### ii. Experienced users

Not tested. A user already familiar with card-based social apps (e.g., event or group-listing apps) might already expect a "tap card body vs. tap button" convention — but this is an inference, not confirmed data.

#### iii–v. Elderly / disabilities / environmental constraints

Not tested in this project.

### e. Propose specific HCI-based solutions

- **Reasoning chain**: Observed issue — Join and "open detail" share one tap target with no distinction → Concept — this violates Consistency ("different things should look different") and Affordances (*LN02*) → Design implication — the two operations need separate, visually distinct affordances → **Solution**: add a distinct "View Details" affordance (e.g., a chevron icon, or making the full card body tappable with a separate, visually smaller Join button), restoring both consistency and visibility.
- **Reasoning chain**: Observed issue — after tapping Join, the only feedback is the button's own label change → Concept — this satisfies "immediate effect" (*LN02, Feedback*) for the toggle itself, but leaves the "view details" operation entirely without feedback or visibility (*LN02, Visibility*; Shneiderman's Golden Rule #3) → Design implication — pair the state-change feedback with an explicit next step → **Solution**: show a brief confirmation with a direct link, e.g., "Joined! Tap here to see challenge details."
- **Reasoning chain**: Observed issue — the user's real goal (finding a nearby running club) had no visible entry point → Concept — this is a task-analysis gap (*LN04*: task analysis should capture user goals and environment, and map them to supporting features) → Design implication — a common, confirmed user goal should have a direct feature behind it → **Solution**: if location- or activity-based club discovery exists elsewhere in the app, surface a "Find a club near you" or "Find a Walk/Run club" entry point directly on the Clubs tab's landing view, rather than only showing "Create your own" and the single official Strava Club; if no such feature exists at all, this task-analysis gap is itself the finding.

---

## Notes on Scope and Evidence

- Per project scope (see `CLAUDE.md`), this document covers **Product 1 (Strava) only**. Product 2 is a teammate's responsibility.
- Use cases above are limited to the flows with **confirmed first-hand context** (`strava-usage-context-notes.md`). Other observed flows (You/Workouts, Settings) are cataloged in `strava-screenshot-inventory.md` but not yet written up as full use cases, pending first-hand context — **before adding any new use case, the group should be interviewed with targeted context questions first, not assumed.**
- Each use case's "e. Propose specific HCI-based solutions" subsection is Requirement 2 content, kept inline in this same document per the assignment template — both requirements live together in `report.md`.
- HCI reasoning in sections "c" and "e" of every use case is grounded in specific concepts from the course slides: `LN02 - Fundamental Concepts - Usability Dimensions.md` (feedback channels, visibility, affordances, consistency, recognition vs. recall, mental model, conceptual model, interface metaphor, chunking, usability goals), `LN03 - UI Design Process.md` (Shneiderman's Eight Golden Rules, error prevention/complete sequences), and `LN04 - Task Analysis.md` (task analysis fields — goal, user environment, how a task is learned). Concepts not present in these slides (e.g., "signifier," "Gulf of Execution/Evaluation") were deliberately not cited, since they weren't confirmed as part of this course's material.
