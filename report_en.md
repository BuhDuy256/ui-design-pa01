# I. Strava

## 1. Introduction

### a. Product Introduction

Strava is a GPS-based activity tracking app (walking, running, cycling) with a social layer on top: sharing activities, Kudos, clubs, and challenges.

This report is based on a real first-time session using the app, on the free plan, on an iPhone: one walk recorded from start to finish, followed by exploring the Maps and Groups tabs.

### b. User Goals

Within the scope of this session, the core value observed for a first-time user was "tap Start, Stop, Resume, Finish while walking" — recording an activity and viewing basic stats (distance, time, speed) right after. Other features — detailed analysis, route exploration, clubs, challenges — were explored only out of curiosity while testing the app, not because they were an original need.

### c. Primary Users

According to Strava's trend data, running is still the most tracked sport on the platform, and cycling is growing. However, most users are not competitive athletes: 93% say their main motivation is health, not competition. The primary user group is therefore closer to "people who want to stay active and track personal progress" than to "serious competitive athletes."

### d. Secondary Users

- Walkers — the second most recorded activity on Strava, right after running. The walker in this project's session represents a large, normal user segment, not a rare case.
- Cyclists, swimmers, hikers, triathletes.
- Competitive users who care about segment leaderboards and structured training data.
- Social-focused users who join clubs and challenges — this group leans toward younger users (Gen Z).
- Multi-sport users: 54% track more than one type of activity, 96% participate in more than one sport — switching between activities is common.

### e. Device and Knowledge Requirements

**Device**: iOS/Android phone, or the strava.com website; this session used an iPhone. Strava also supports Wear OS, activity recording on Apple Watch, and syncing from Garmin, Wahoo, Suunto, Polar, Fitbit, and Coros.

**Account plan**: the Free plan (used in this project) includes activity recording, community participation, and safety features. The paid plan unlocks custom routes, offline maps, full training history, more detailed analysis, goal tracking, segment leaderboards, and a fitness score. Upgrade prompts ("Start a free trial" / "Subscribe") appear repeatedly across many screens: the Maps tab, Workout Analysis, You/Progress, You/Workouts, and the Groups tab.

**Prior knowledge required**: none for the core loop. The sequence Start → Pause/Resume → Finish was completed on the very first attempt without hesitation — consistent with novice / first-time user behavior. However, the secondary analysis screens, which are locked behind the paid plan, are not immediately clear on first viewing.

---

## 2. Use Case 1: Record, Finish, and Save an Outdoor Walk

### a. Use Case 1 Analysis

**Goal**: track distance, time, and speed in real time, then save the result as a permanent record.
**Precondition**: logged into a Strava account; GPS access has been granted to the app (implied by the fact that the map and location data worked throughout the session).
**Trigger**: open the Record tab, tap Start.
**Observed steps**:
1. In-progress recording screen — live map and stats (Time/Distance/Speed), Pause button.
![In-progress recording screen](strava-images/IMG_0514.PNG)
*IMG_0514 — In-progress recording screen: live map with Time/Distance/Speed and the Pause button.*
2. Tap Pause → Stopped screen — large stats (Distance, Avg Speed), Resume/Finish buttons.
![Stopped screen](strava-images/IMG_0515.PNG)
*IMG_0515 — Stopped screen: large Distance/Avg Speed stats with Resume/Finish buttons.*
3. Tap Finish → Save Activity screen 1 (title, description, activity type, map preview, tags).
![Save Activity screen 1](strava-images/IMG_0517.PNG)
*IMG_0517 — Save Activity screen 1: title/description, Walk type, map preview.*
4. Scroll down to Save Activity screen 2 ("How did that feel?", private notes, gear, Visibility, Mute Activity, Save Activity button).
![Save Activity screen 2](strava-images/IMG_0518.PNG)
*IMG_0518 — Save Activity screen 2: How did that feel, Visibility, Mute Activity, Save button.*
5. Tap Save Activity → "Nice work!" transition animation.
![Nice work transition screen](strava-images/IMG_0519.PNG)
*IMG_0519 — "Nice work!" transition animation.*
6. → "Welcome to the team, Duy!" first-activity achievement popup (View Activity / View in Trophy Case).
![First-activity achievement popup](strava-images/IMG_0520.PNG)
*IMG_0520 — First-activity achievement popup.*
7. → Share Activity sheet opens automatically (map + stats card, Share to Message / Strava Post / Copy Link / More).
![Share Activity sheet](strava-images/IMG_0522.PNG)
*IMG_0522 — Share Activity sheet.*

That is **5 separate screens between tapping Finish and reaching a stable state** — not a single confirmation.

### b. Context and Interaction Method

- **Where / When**: outdoors, on a real street; early morning, around 06:09–06:15.
- **Situation**: actively walking, moving continuously, not sitting still. This was the first activity on the account, confirmed by the "Kudos on your first activity!" badge and the "Welcome to the team, Duy!" popup.
- **Interaction method**: one-handed tap; attention split between watching the path ahead and glancing down at the phone to check speed and duration.
- **Expected outcome**: an accurate record (distance, time, route), saved for later viewing. Sharing was expected to be optional, not automatic.

### c. Applying HCI Principles

**Human Senses and Motor System**

**Benefit.** Time/Distance/Speed are placed in the center of the screen as large, high-contrast numbers, aligned with the foveal vision region — where the eye sees detail most clearly — so one quick glance while walking is enough to read them.

**Drawback.** Confirmation of Pause/Resume/Finish relies only on the visual channel (color/label change on the button); a haptic signal (vibration) would be more suitable here because the eyes are busy watching the path.

---

**Mental Model and Interaction Metaphor**

**Benefit.** Start → Pause/Resume → Finish matches a familiar mental model ("walk and then stop"); the ▶/❚❚ icons and the checkered flag are interaction metaphors borrowed from music players and racing, requiring no separate learning.

**Drawback.** The expectation "Finish = done" is not met: four more screens (Save, "Nice work!", achievement popup, Share) appear before reaching a stable state — showing that the flow does not follow Shneiderman Rule #4 (design dialogs to yield closure).

---

**Usability**

**Benefit.** Learnability was high in this session — the core loop was performed correctly on the first try, with no instructions needed. Errors did not occur during the activity recording phase.

**Drawback.** Efficiency was good during recording, but dropped noticeably right after Finish due to four unrequested additional screens.

### d. Different User Types and Contexts

- **Novice user**: matches this session — no prior Strava experience, and the core loop was understood on the very first attempt with no guidance.
- **Experienced user**: likely already familiar with the Finish → Save → Share sequence from repeated use, so the surprise factor described above will decrease over time — but the extra taps remain, so the efficiency cost still exists even after the surprise is gone.
- **Older users**: the wide Pause/Resume/Finish button bar provides a large tap target — consistent with Fitts's Law, which benefits users with less precise motor control.
- **Users with disabilities**: without haptic or audio feedback, users who rely on a screen reader may have difficulty knowing when state changes occur (Paused, Resumed, Finished), unless screen-reader-specific labels handle this — something that was not directly verified in this session.
- **Environmental constraints**: the recording session took place outdoors during the day with a stable signal, so glare and GPS drift were not actually observed. However, two potential risks are worth noting: the dark background of the recording screen can cause more glare under direct sunlight than a light background; and distance/speed data depends entirely on GPS signal, which is often weaker in dense urban areas where tall buildings block satellite coverage.

### e. Design Recommendations Based on HCI Principles

- **Observed problem**: Finish is followed by four non-optional screens before reaching a stable state, breaking the expectation that "Finish = done."
  **Relevant HCI principles**: Shneiderman Rule #4 (design dialogs to yield closure) and Rule #7 (support user control).
  **Why this solution works**: a clear stopping point right after Finish restores the sense of closure the user expects at that moment, and lets them choose whether to continue to sharing or not.
  **Solution**: immediately after Finish, show a single lightweight screen — "Activity saved. View it now, or share later?" — with two clear buttons. Move the achievement popup and the Share sheet into the "share later" branch instead of showing them automatically.

- **Observed problem**: Pause/Resume/Finish confirmation is visual only, requiring the user to look at the screen while walking and watching the path.
  **Relevant HCI principles**: feedback should use a channel that fits the situation, and eye movement should be minimized when attention is needed elsewhere.
  **Why this solution works**: a short vibration can be felt without looking, so the user gets confirmation without taking their eyes off the path.
  **Solution**: add a short vibration at each state change (Start, Pause, Resume, Finish).

---

## 3. Use Case 2: Reviewing Stats After an Activity

### a. Use Case 2 Analysis

**Goal**: understand the activity just completed — distance, speed, elevation, splits.
**Precondition**: an activity has been recorded and saved successfully (the result of Use Case 1).
**Trigger**: open the saved activity, scroll through the detail and analysis screens.
**Screens observed**:
- Activity detail (Distance/Moving Time/Elevation Gain, Kudos banner).
![Activity detail screen](strava-images/IMG_0521.PNG)
*IMG_0521 — Activity detail screen.*
- Workout Analysis (Laps, flyover map).
![Workout Analysis screen](strava-images/IMG_0525.PNG)
*IMG_0525 — Workout Analysis screen.*
- Elevation chart (Elevation Gain, Max Elevation).
![Elevation chart](strava-images/IMG_0526.PNG)
*IMG_0526 — Elevation chart.*
- Pace chart (Avg Pace, Moving Time, Avg Elapsed Pace, Elapsed Time, Fastest Split).
![Pace chart screen](strava-images/IMG_0527.PNG)
*IMG_0527 — Pace chart screen.*

### b. Context and Interaction Method

Same session as the recorded walk, reviewing the saved activity on the same iPhone. Interaction method: scrolling and tapping through a single-column stats screen. Expected outcome: quickly understand how the activity went by reading the numbers shown.

### c. Applying HCI Principles

**Chunking**

**Benefit.** Data is shown as separate blocks of large numbers and individual charts (the elevation chart is separate from the pace chart) rather than one dense table — each main stat (Distance, Moving Time, Elevation Gain) stands alone, making it easy to scan when checking a specific number.

**Drawback.** Within the same display block, some stats with similar names are placed next to each other with no visual separator — Avg Pace and Avg Elapsed Pace, Moving Time and Elapsed Time — creating a recognition burden in the very area that is otherwise well organized.

---

**Recognition vs Recall**

**Benefit.** All data is shown directly on screen — no commands to remember, no extra navigation needed; the user just reads what is displayed. This is, in principle, a recognition-supporting design.

**Drawback.** When labels with similar names are placed next to each other — Avg Pace / Avg Elapsed Pace, Moving Time / Elapsed Time — the user cannot tell them apart by looking at the label alone; they must recall the meaning of each term instead of recognizing it from the interface. This goes against the principle of preferring recognition, in a section that otherwise has the advantage of doing so.

---

**Usability**

**Benefit.** The screen is read-only, so no operational errors occur. Learnability is high for the familiar main stats (Distance, Moving Time, Elevation Gain) because they are short and displayed large enough to read easily.

**Drawback.** Learnability is low specifically for the similar-label group: it is not possible to tell Avg Pace from Avg Elapsed Pace, or Moving Time from Elapsed Time, without outside help — and the risk of confusing these two when comparing sessions is real.

### d. Different User Types and Contexts

- **Novice user**: matches this session — the confusion occurred on the very first encounter with the screen.
- **Experienced user**: someone familiar with other fitness tracking apps is likely already aware of the difference between "moving time" and "elapsed time," since this pair of terms is common across the fitness app industry — meaning these labels cause fewer problems for them. However, the similar phrasing of "Pace" vs. "Elapsed Pace" is specific to Strava and is still likely to cause confusion regardless of experience.

### e. Design Recommendations Based on HCI Principles

- **Observed problem**: it is not possible to tell Avg Pace / Avg Elapsed Pace / Moving Time / Elapsed Time apart on the pace chart screen.
  **Relevant HCI principle**: recognition over recall.
  **Why this solution works**: placing an explanation exactly where the user is looking turns something they have to guess into something they can simply recognize, with no need to remember.
  **Solution**: add a small information icon next to each of these four labels, showing a one-line definition when tapped (for example: "Elapsed Time: total time including stops. Moving Time: time actually spent moving"). Show it automatically the first time the screen is opened, then allow it to be dismissed on later visits.

---

## 4. Use Case 3: Exploring Groups — Motivation, Competition, and Community

### a. Use Case 3 Analysis

**Goal**: evaluate how the Groups tab supports motivation, competition, and continued engagement — through four observed mechanisms: Challenges, progress bars, achievements (observed in Use Case 1), and Clubs. For Clubs specifically, there was an additional concrete goal: find an active running club in the local area.
**Precondition**: logged into a Strava account; on the home screen, able to tap the Groups tab from the bottom navigation bar.
**Trigger**: tap the Groups tab from the bottom navigation bar.
**Observed steps**:
1. Active tab — "Design Your Own Challenge" paid-plan banner, plus progress bars for joined challenges.
![Groups Active tab](strava-images/IMG_0532.PNG)
*IMG_0532 — Groups Active tab: Design Your Own Challenge banner and progress bars for joined challenges.*
2. Challenges tab, cards with a Join button ("July 5K Challenge", "Recommended For You" list).
![Challenges tab, Join button](strava-images/IMG_0533.PNG)
*IMG_0533 — Challenges tab: July 5K Challenge card with Join button and Recommended For You list.*
3. Tap Join on a challenge card → button changes state, but the screen does not change.
4. Clubs tab — "Create Your Own Strava Club" banner and "The Strava Club."
![Clubs tab](strava-images/IMG_0534.PNG)
*IMG_0534 — Clubs tab: Create Your Own Strava Club banner and The Strava Club.*

### b. Context and Interaction Method

- **Context**: a separate session from the recorded walk.
- **Situation**: active exploration, no urgent task to complete. For Active/Challenges: curiosity; for Clubs: a concrete goal — find a running club near home.
- **Interaction method**: attention went straight to the Join button — the highest-contrast element on the card — before the rest of the card was read.
- **Expected outcome**: being able to track progress on a joined challenge; for Clubs, finding an active club in the local area.

### c. Applying HCI Principles

**Challenges and Progress Bars (Feedback)**

**Benefit.** First, the progress bars in the Active tab continuously show how far along each joined challenge is — one look is enough to know where you stand, no calculation needed; this is a clear and direct form of feedback. Second, the challenge card ("July 5K Challenge") presents a specific goal (name, distance, deadline) and a clearly recognizable Join button — the user does not need to set their own goal, just choose from the list provided.

**Drawback.** After tapping Join, there is no path to view details or progress for the challenge just joined — the only feedback is that the button label changes, and it is then unclear where to track it: the interface encourages joining well but does not support the next step of tracking. In addition, the "Design Your Own Challenge" button is visible on screen but leads to a screen requiring a paid subscription — the user can see the option but cannot use it.

---

**Achievements and Social (Feedback)**

**Benefit.** The achievement popup (observed in Use Case 1) and the Kudos banner (Use Case 2) are well-designed interface feedback elements — specific, appearing immediately after an activity, with direct named messages ("Welcome to the team, Duy!", "Kudos on your first activity!").

**Drawback.** In this session, no visible connection was found on the interface between those feedback elements and the Groups tab — personal achievements and community content appear to work as two separate flows.

---

**Community Discovery (Visibility)**

**Drawback.** The specific goal "find a club in the local area" has no entry point on the Clubs tab; only promotional content is shown (create your own club, "The Strava Club" official page). No location-based or activity-based discovery feature is visible, which reduces Visibility — the actions the user can take (search, filter, browse clubs) are not shown — right from the first screen.

---

**Join and Card Detail**

**Drawback.** Attention went to the Join button before the rest of the card was read; after tapping, only the button label changed — no detail view opened. This is a specific instance, at the scale of a single interaction, of the same feedback gap described above — it is not the central problem of the Groups tab.

---

**Overall Impression**: the Groups tab has some interface mechanisms that work well — progress bars are clearly visible, challenge cards are easy to recognize, and the achievement and Kudos system gives specific feedback after each activity. However, within the scope of this session, the two main goals — tracking a joined challenge and finding a club — were both not achieved, because the interface does not provide a clear next step after joining a challenge, and the Clubs tab does not have a location-based discovery feature.

### d. Different User Types and Contexts

- **Novice user**: matches this session — first contact with Groups, Challenges, and Clubs.
- **Experienced user**: someone familiar with other card-based social apps might expect to tap the card body to open details, with a separate button for a quick action — Strava's current layout does not separate these two, so the missing detail problem may still occur even for users familiar with card-based interfaces.

### e. Design Recommendations Based on HCI Principles

- **Observed problem**: after Join, there is no feedback or entry point to view challenge details or progress.
  **Relevant HCI principle**: Feedback (offer informative feedback).
  **Solution**: after Join, show a short confirmation with a direct link — "Joined! Tap here to see challenge details and progress."

- **Observed problem**: there is no entry point to find clubs by location or activity type on the Clubs tab.
  **Relevant HCI principle**: Visibility.
  **Solution**: add a search box or filter — "Find a club near you" — directly on the main Clubs tab screen.

---

## Notes on Scope and Evidence

This report covers Product 1 (Strava) only. Product 2 is the responsibility of another team member. The use cases above are limited to flows that were directly experienced and have matching screenshots: recording and saving a walk, reviewing its stats, and exploring the Groups tab. Other screens captured in the same session — the Maps tab, and the Workouts and Settings sub-tabs under the You tab — were viewed but have not been written up as full use cases in this report, and are therefore left out rather than analyzed from guesswork.

The HCI reasoning in each use case is based on concepts taught in the course: the three human subsystems (senses, cognition, motor system), the usability dimensions (learnability, efficiency, errors, satisfaction), chunking, recognition vs recall, mental model, interaction metaphor, feedback, visibility, Fitts's Law, and the relevant principles from Shneiderman's Eight Golden Rules; as well as the task analysis framework (goal, precondition, subtasks, context of use, how learned).
