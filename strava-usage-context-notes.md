# Strava — First-Hand Usage Context Notes

> First-hand account from the group member who captured the screenshots. This is a **first-time user** exploring Strava (see CLAUDE.md Scope) — not habitual/expert usage. Use this to fill the Context fields (Where/When/User Situation/Interaction Method) in report.md; do not infer these from screenshots alone.

## Device & Account

- Device: iPhone (exact iOS/app version not confirmed)
- Account: **Free tier**, first time installing and opening Strava
- This resolves the two open items in `strava-platform-info.md` ("Still Not Covered"): device is iPhone, account is free tier — consistent with the repeated "Start a free trial" prompts seen in the screenshots.

## Use Case: Record → Finish → Save a Walk

**Where / When / Situation:**
- Outdoors, while actually walking (not sitting at a desk).
- Interacting with the phone while walking: one-handed touch, eyes alternating between watching the path ahead and checking the phone for stats (pace, duration).

**Interaction method:**
- One-hand tap. Divided attention between walking and glancing at the screen.

**Breakdown observed — mental model mismatch (Finish → Share screen):**
> "Trong suy nghĩ hơi khác của tôi là sau khi ấn Finish (walk) thì nó hiện ra phần share buổi đi bộ => Kiểu hơi lạ."

Expected flow: tap Finish → land in activity history, with a share option available *if wanted*.
Actual flow: tap Finish → immediately shown a share/save screen.
Not a blocking problem ("cũng được"), but it is a **measurable mismatch between the user's mental model and the system's actual flow** — worth citing directly as a concrete HCI observation (User Mental Model / expectation violation), not a generic "confusing UI" claim.

## Use Case: Reviewing Post-Walk Stats (Pace screen)

Screenshot: `strava-images/IMG_0527.PNG` (Pace chart, Avg Pace, Moving Time, Avg Elapsed Pace, Elapsed Time, Fastest Split)

**Confusion reported:**
> "Có mấy cái như Avg Elapsed Time + Elapsed Time + Fastest Split là tôi không hiểu làm gì?"

The user could not distinguish between multiple similar-sounding pace/time metrics shown together (Avg Pace vs. Avg Elapsed Pace, Moving Time vs. Elapsed Time). This is a concrete **learnability/terminology problem** — several closely-named metrics presented without explanation, forcing the user to guess rather than recognize. Good candidate for a specific drawback citation (ties to "speak the user's language" / jargon-overload principles from LN02).

## Subscription Prompts

User confirmed the repeated "Start a free trial" prompts (seen on Maps, Workout Analysis, You/Progress screens) were noticed and registered as upsell pressure — consistent with satisfaction-dimension friction, though not described as strongly negative.

## Overall Mental Model (core value vs. peripheral features)

> "Kiểu trong đầu tôi core value của cái app là ấn nút theo dõi và theo dõi chỉ số thôi. Thì các tính năng nằm ngoài nó tôi ko quen và ấn thử để test xem nó đang làm cái gì."
> "Core value => Ấn Start, Stop, Resume, Finish Walk."

The user's mental model of Strava's core value is narrow: **start/stop/resume/finish tracking + checking basic stats.** Everything else (Segments, Routes, subscription features, detailed pace breakdowns) was explored only as deliberate testing, not organic need — i.e., **secondary/discoverable features, not core to the first-time mental model.** This is useful framing for the report: the core recording loop is highly learnable; everything surrounding it is not, for a first-time user.
