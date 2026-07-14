# Strava — Screenshot Inventory (all 28 images)

> All 28 files in `strava-images/` reviewed. Captured in one continuous session, 06:11–06:15, single "test" Walk activity. Grouped by flow/feature below, not by filename order, since several files capture the same screen at different scroll positions.

## Flow 1: Record → Finish → Save Activity (first-time recording)

- **In-progress recording**: live map with route line, Time/Distance/Speed stats, Pause button; then Stopped state with big-number stat display and Resume/Finish buttons. (`IMG_0513`, `0514`, `0515`)
- **Save Activity, screen 1**: title field ("test"), description field ("test"), activity type dropdown ("Walk"), map preview placeholder, Add Photos/Video, Change Map Type, Activity Tag. (`IMG_0517`)
- **Save Activity, screen 2** (scrolled down): "How did that activity feel?", private notes, Add new gear, Visibility → Who can view (Everyone), Hidden Details, Mute Activity checkbox, Discard Activity, Save Activity button. (`IMG_0518`)
- **"Nice work!" transition screen** — brief animated confirmation. (`IMG_0519`)
- **"Welcome to the team, Duy!"** — first-activity achievement popup, View Activity / View in Trophy Case buttons. (`IMG_0520`)
- **Share Activity sheet** — two template pages (map+stats card with Strava logo; transparent overlay card), Share to: Message / Strava Message / Strava Post / Copy Link / More, plus Copy to Clipboard / Save. (`IMG_0522`, `0523`)

**Use case this supports:** the complete first-time "record → finish → save → (forced) share prompt" flow — this is your strongest, most fully-documented use case.

## Flow 2: Activity Detail & Post-Activity Analysis

- **Activity detail page**: profile header (Duy Bảo, location, timestamp), title/description, "Kudos on your first activity!" banner, Distance/Moving Time/Elevation Gain, "With someone who didn't record? → Add Others", source tag "Strava App", like/comment/share icon row, "Get smarter insights for faster progress" (Athlete Intelligence) paywall. (`IMG_0521`, `0524`)
- **Workout Analysis**: Laps list, Flyover map, "Start a free trial" prompt, Results section, Elevation chart intro. (`IMG_0525`)
- **Elevation chart**: Elevation Gain, Max Elevation, chart with drag tooltip; Pace chart begins. (`IMG_0526`)
- **Pace chart** (continued): Avg Pace, Moving Time, Avg Elapsed Pace, Elapsed Time, Fastest Split, "Problem with your location data? → Report". (`IMG_0527`)

**Use case this supports:** reviewing a completed activity's stats. Also the source of the confirmed confusion point in `strava-usage-context-notes.md` (Avg Pace vs. Avg Elapsed Pace vs. Elapsed Time terminology).

## Flow 3: Achievements

- **Trophy Case**: Milestones grid — First Activity (unlocked), Third/Fifth/10th/20th/30th Activity (locked). Reached from Home tab. (`IMG_0526` region / one of the mid-sequence files — confirm exact filename before citing)

## Flow 5: Groups Tab

- **Active sub-tab**: "Design Your Own Challenge" paywall + joined/active challenges with progress bars (July 5K / 800K Ride / 100K Gran Fondo).
- **Challenges sub-tab**: Strava banner, "July 5K Challenge" card + Join button, "Recommended For You" (400-minute Runna Challenge, Virtual TCS New York City Marathon). Confirmed as `IMG_0532`/`0533`.
- **Clubs sub-tab**: "Create Your Own Strava Club" promo, Get Started button, "The Strava Club" banner.

**Note:** two of the Groups screenshots (Active tab) look near-identical, and likewise for Clubs — possibly duplicate/retake captures. Worth a quick manual check of the exact files before citing a specific one in the report.

## Flow 6: You Tab

- **Progress sub-tab**: "This week" stats (Walk filter), Past 12 weeks chart, July calendar with streak tracking ("Your Streak: 1 Week"), "Unlock your full potential" paywall, Best Efforts (5K PR: 26:54), Goals (Weekly Run Goal 1/4), Relative Effort, Training Log bar chart, Data Sources (Strava App — last used 3 minutes ago; Connect a new device), Give Feedback link.
- **Workouts sub-tab**: "Your focus: Staying active", Easier/Steady/Harder/Variety toggle, suggested workout card ("Progressive Run" — 40m, Moderate), Subscribe button.
- **Activities sub-tab**: search/filter bar, activity list (the one test Walk, with map thumbnail).
- **Settings** (gear icon): Subscriptions (Strava + Runna, 60% off), Your Strava Subscription, Training Plans, Account email, Connect an app/device, Manage Apps & Devices, Restore Purchases, Change Email, Phone Number, Help.

## Recurring Pattern: Subscription Upsells

Paywall / "Start a free trial" / "Subscribe" prompts recur across nearly every tab: Maps (routes/heatmaps), Workout Analysis, Activity detail (Athlete Intelligence), You/Progress (twice), You/Workouts, Groups/Active. This repetition is itself a concrete, citable UX observation — worth analyzing under the Satisfaction usability dimension (matches what you already confirmed feeling in `strava-usage-context-notes.md`, Q9).

## Not Captured — Gaps to Be Aware Of

Before writing use cases, note these are **not** in the 28 screenshots:
- The Home tab's actual activity feed (scrollable posts from other athletes) — only the Home tab icon appears highlighted en route to Trophy Case; the feed content itself wasn't captured.
- Kudos-giving or commenting in action (tapping the buttons, not just seeing them).
- Notifications inbox.
- Search results / athlete search.
- Segment detail page (only the list view exists).
- Onboarding/sign-up flow — screenshots start already logged in as a new account.
- Device/sensor pairing flow in detail.
- Any second activity — all data comes from the single "test" walk.

If your use cases need any of the above, you'd need new screenshots, not re-analysis of what's already here.
