# Final Slide Content — Strava (CSC13112 · PA1)

> **PRODUCT RESEARCH OVERVIEW — STRAVA APP**
> Synchronized with Group 03's Garmin Deck structure and UI/UX evaluation parameters.
> 
> **Design Specifications & Consistency Rules:**
> - Slide Content: **English**
> - Layout Structure: Follows Garmin's multi-slide diagnostic breakdown per Use Case.
> - Usability Framework: Strictly aligned to Garmin's 4 dimensions (*Learnability, Efficiency, Memorability, Error Recovery*).
> - Human Capabilities Grid: Normalized into 4 standard quadrants (*Vision & Attention*, *Touch & Motor*, *Audio & Haptic Feedback*, *Memory & Cognition*).

---

## INTRODUCTION & PRODUCT OVERVIEW

### Slide 1 — Title Slide
- **STRAVA** — Product Research & Interaction Analysis
- CSC13112 · UI/UX Design · Project Assignment 1 (PA1)
- Group 03 — FIT-HCMUS
- *Presenter:* [Your Name / Student ID]
- **Visual Asset:** High-resolution Strava Branding or blurred mobile dashboard application interface background layer.

### Slide 2 — Product & User Profile
- **What is Strava:** A multi-sport GPS-based fitness tracking platform with an integrated social ecosystem (Record → Analyze → Share).
- **Core User Goal:** Instantly record outdoor physiological activities and review basic athletic metrics (Distance, Moving Time, Average Pace) post-session.
- **Primary Audience:** Health-focused active individuals and recreational runners (93% track for personal wellness rather than competitive placement).
- **Secondary Segments:** Casual walkers (#2 activity type on platform), cyclists, multi-sport enthusiasts, and socially-driven Gen Z community challenge participants.
- **Evaluation Scope:** iOS Platform (iPhone), Free Tier Service Environment, First-Time User Experience.
- **Visual Asset:** `IMG_0521` (Activity Detail View) framed within a clean iPhone mobile mockup chassis.

### Slide 3 — Core Use Cases Index (Strava Application)
- **Use Case 1:** Recording, Finishing, and Saving an Outdoor Walk (The Core Workflow Loop).
- **Use Case 2:** Reviewing Post-Activity Statistical Performance Metrics.
- **Use Case 3:** Exploring Regional Routes and Spatial Segments via the Maps Interface.
- **Use Case 4:** Engaging with Community Infrastructure (Challenges & Club Spaces) via the Groups Tab.
- **Visual Asset:** Centralized multi-node diagram connecting the four interaction pathways to a single user avatar.

---

## USE CASE 1 — Record, Finish, and Save an Outdoor Walk

### UC1 · Slide 1 — Overview
- **Goal:** Capture precise spatio-temporal tracking data for an outdoor activity in real-time and commit it to permanent system memory.
- **The Core Loop:** Start → Pause → Resume → Finish.
- **Live Interface Displays:** Continuous tracking map view coupled with large-format numeric telemetry (Duration, Spaced Travel, Speed).
- **Visual Asset:** `IMG_0514` (In-progress tracking screen showing active spatial map data).

### UC1 · Slide 2 — User Interaction Context
- **Environmental State (During Active Recording):**
  - Location: Public outdoor urban street.
  - Lighting & Time: Early morning sunlight (~06:09 AM), prone to ambient screen glare.
  - User State: Dynamic walking motion, divided attention between forward physical pathway and screen observation.
  - Interaction Method: One-handed touch manipulation, quick downward glances.
- **System State (At Workflow Termination):**
  - Location: Stationary on public street corner.
  - User Intent: Tap "Finish" to conclude workout session, verify data accuracy, and safely put phone away.
  - Implicit Expectation: "Finish" should immediately execute data save and provide direct access to the stable workout record.
- **Visual Asset:** `IMG_0515` (Stopped state screen displaying high-contrast Resume and Finish button matrices).

### UC1 · Slide 3 — Use Case Interactions
- **Step 1:** Tap "Record" icon on the bottom persistent navigation tab layout bar.
- **Step 2:** Tap primary "Start" action anchor to initialize GPS data streams.
- **Step 3:** Tap large "Pause" button to transition system into temporary halted collection state.
- **Step 4:** Perform sustained hold/press sequence on the "Finish" flag icon component to trigger completion.
- **Step 5:** Scroll vertically through an extensive, multi-input secondary metadata form (Title, Description, Felt Score, Privacy).
- **Visual Asset:** Simplified sequential flowchart showing button touch points mapped to screen state transitions.

### UC1 · Slide 4 — Human Capabilities Matrix
- **Vision & Attention:**
  - *Benefit:* Telemetry values (Time, Distance, Speed) use large, bold typography centered on the screen grid, optimizing rapid foveal vision processing during split-second glances.
  - *Drawback:* Monolithic black dark-mode application background during active outdoor daytime recording enhances screen reflectivity and induces glare.
- **Touch & Motor Control:**
  - *Benefit:* The Pause, Resume, and Finish buttons use a wide, horizontally spanning container bar format, offering a generous touch target area suited for single-handed thumb interactions.
  - *Drawback:* Executing fine touch interactions on fields while maintaining a physical walking gait increases finger positional deviation and tap failure risk.
- **Audio & Haptic Feedback:**
  - *Drawback:* Transition states (Start, Pause, Resume, Finish) provide zero haptic vibrations or structural audio chime feedback channels. Users must looking down to verify state changes, which threatens situational awareness on active roads.
- **Memory & Cognition:**
  - *Benefit:* The primary operational sequence (Start → Pause → Finish) borrows directly from everyday stopwatch concepts, demanding near-zero cognitive overhead.
  - *Drawback:* The excessive post-workout sequence forces users to process multiple unexpected social prompts immediately after intense physical exertion.

### UC1 · Slide 5 — User Mental Model Analysis
- **Conceptual Metaphor Alignment:** The interface mapping perfectly replicates standard stopwatch behavior. The user summarized the workflow expectations simply: *"Press Start, Stop, Resume, Finish on a walk."*
- **The Operational Breakpoint:** A severe friction point emerges at the "Finish" boundary. While the user's mental model defines "Finish" as task completion, the system treats it as an entry gateway to an expansive five-stage social sharing workflow.
- **The System-User Gap:** System forces 5 separate modal screens (Save Form → "Nice Work!" Animation → First Activity Achievement Popup → Automatic System Share Sheet Overlay) before reaching a stable home dashboard.
- **User Voice:** *"What felt a bit different to me is that after I press Finish on a walk, it shows a screen to share the walk — that felt a bit strange."*
- **HCI Paradigm Breach:** Direct violation of Shneiderman’s Golden Rule #4 (Design dialogs to yield closure). The workflow artificially extends and postpones closure when the user expects a clean conclusion.
- **Visual Asset:** `IMG_0522` (Forced system share sheet view highlighting the unrequested UI overlay).

### UC1 · Slide 6 — Interaction Metaphors
- **Media Player Schemas:** Use of standard right-facing triangle (▶) for Resume and double vertical bars (❚❚) for Pause draws on cross-platform media navigation standards.
- **Athletic Schemas:** The checkered flag racing metaphor utilized on the Finish node links directly to the real-world concept of crossing a finish line.
- **Evaluation:** High semantic clarity. First-time users successfully translate these symbols into immediate action without external guidance or instructional scaffolding.
- **Visual Asset:** High-contrast isolated crops of the ▶, ❚❚, and checkered flag iconography from the Strava interface assets.

### UC1 · Slide 7 — Usability Diagnostic
- **Learnability:** Exceptionally High. A completely naive first-time user navigated the primary data-capturing workflow on their first attempt with absolute autonomy.
- **Efficiency:** Polarized performance. Highly efficient during the real-time active tracking phase (minimal actions required); highly inefficient post-finish, requiring multiple forced taps to dismiss unwanted social screens.
- **Memorability:** High retention characteristics. Because the system utilizes standard universal iconography and everyday media schemas, the operational sequence is easily remembered over time.
- **Error Recovery:** Adequate safety buffers during active tracking via wide target layouts. However, error recovery is poor during the post-finish phase, as there are no obvious shortcuts to bypass or undo the forced sharing flow.
- **Visual Asset:** Comparative timeline metric chart contrasting active efficiency (high) against post-workout efficiency (steep decline).

### UC1 · Slide 8 — Different User Types & Contexts
- **Beginners:** Directly validated by user testing. The core loop is intuitive, but the complex post-finish social loop causes immediate confusion.
- **Experienced Athletes:** Anticipate the multi-stage save sequence, yet the unnecessary multi-tap interaction tax remains an ongoing friction point.
- **Elderly Demographic:** Large, generous tap targets on the tracking buttons help users with lower fine motor skills, but the small typography on the multi-input save form hinders readability.
- **Users with Disabilities:** The visual-only feedback approach poses a high accessibility barrier. Low-vision users or screen-reader dependents receive no clear non-visual cues when states toggle between tracking and paused.
- **Environmental Constraints:** Daytime urban conditions introduce high sunlight glare risks against the dark mode screen layout. Additionally, dense high-rise architecture presents real risks of GPS signal degradation.
- **Visual Asset:** Multi-icon grid layout representing User Personas paired with clear checkmark/warning indicator badges.

### UC1 · Slide 9 — Proposed HCI Solutions
- **Solution A: Streamlined Task Closure Pattern**
  - *Action:* Introduce an explicit intermediate confirmation hub right after tapping "Finish": *"Activity Saved. View Activity Now | Share Later"*. 
  - *HCI Principle:* Restores Shneiderman’s Golden Rule #4 (Closure) and Golden Rule #7 (Internal locus of control) by treating social sharing as an optional, user-driven action.
- **Solution B: Multi-Channel State Feedback**
  - *Action:* Integrate unique, short haptic vibration pulses and clear audio chimes on every major state transition (Start, Pause, Resume, Finish).
  - *HCI Principle:* Diverts confirmation away from the overloaded visual channel, allowing users to verify state changes while keeping their eyes safely on the physical road.
- **Visual Asset:** Side-by-side design mockup contrasting the current multi-step layout with the proposed one-tap closure overlay.

---

## USE CASE 2 — Reviewing Post-Activity Stats

### UC2 · Slide 1 — Overview
- **Goal:** Comprehend workout performance data through aggregate physiological and spatio-temporal telemetry post-walk.
- **Data Layers Evaluated:** Core Activity Metrics Overview → Comprehensive Workout Analytics View → Vertical Elevation Performance Charts → Granular Pace/Split Breakdowns.
- **Visual Asset:** `IMG_0521` (Main post-activity summary detail dashboard screen layout).

### UC2 · Slide 2 — User Interaction Context
- **Environmental State:** Settled indoor domestic environment, seated or stationary posture.
- **User Attention:** High focal attention, low real-time environmental risk.
- **Interaction Method:** Vertical scrolling gestures and single-tap micro-interactions on a dense, single-column numeric interface array.
- **Implicit Goal:** Quickly interpret performance data to evaluate progress without needing to search for term definitions.
- **Visual Asset:** `IMG_0525` (Detailed Workout Performance Analytics display view).

### UC2 · Slide 3 — Use Case Interactions
- **Step 1:** Open the recorded activity log entry from the central user profile feed view.
- **Step 2:** Scroll vertically to review top-level aggregated data cards (Distance, Moving Time, Elevation Gain).
- **Step 3:** Tap sub-analysis panels to reveal deeper structural data layers (Laps, Chart Overlays).
- **Step 4:** Perform horizontal drag actions along chart lines to read specific data points across time intervals.
- **Visual Asset:** Schematic representation highlighting vertical scrolling paths and corresponding pop-out chart interactions.

### UC2 · Slide 4 — Human Capabilities Matrix
- **Vision & Attention:**
  - *Benefit:* Raw metrics are neatly isolated into clear, high-contrast data blocks and graphical charts, preventing visual clutter.
  - *Drawback:* Placing multiple similarly-named textual labels in close proximity creates visual confusion, making it difficult to differentiate metrics at a glance.
- **Touch & Motor Control:**
  - *Benefit:* Layout relies on simple, low-precision vertical scrolling gestures, making it highly accessible across user tiers.
  - *Drawback:* Interacting with interactive chart paths requires high-precision horizontal dragging, which can be frustrating on smaller mobile screen grids.
- **Audio & Haptic Feedback:**
  - *Status:* Not a primary communication channel. The read-only interface relies entirely on visual data presentation.
- **Memory & Cognition:**
  - *Benefit:* Employs information "chunking" design patterns; grouping related telemetry together lowers cognitive processing overhead.
  - *Drawback:* The lack of clear inline contextual definitions forces users to actively recall meanings, increasing memory load.

### UC2 · Slide 5 — User Mental Model Analysis
- **Recognition vs. Recall Failure:** The system presents similarly-named metrics (*Average Pace, Average Elapsed Pace, Moving Time, Elapsed Time*) close together without explaining what separates them.
- **The Cognitive Mismatch:** While a fitness system expects users to understand specialized training terms, a standard user expects plain language. Lacking visible cues, the interface forces *recall* over *recognition*, increasing cognitive friction.
- **User Voice:** *"Things like Avg Elapsed Time, Elapsed Time, and Fastest Split — I don't understand what they're for."*
- **HCI Guideline Violation:** Directly breaches the fundamental heuristic of keeping a *match between the system and the real world*. The interface prioritizes raw internal database labels over clear, user-friendly language.
- **Visual Asset:** `IMG_0527` (Pace Analysis Dashboard Screen) with a bright red callout box highlighting the confusing metric labels.

### UC2 · Slide 6 — Interaction Metaphors
- **Data Visualization Standards:** Elevation and pace metrics use standard, familiar line and area charts.
- **Evaluation:** High usability match. The user reads the charts easily based on prior exposure to everyday web graphics, without needing an app-specific learning curve.
- **Visual Asset:** `IMG_0526` (Elevation Profiling Area Chart Interface).

### UC2 · Slide 7 — Usability Diagnostic
- **Learnability:** Low. First-time users cannot reliably distinguish between "Moving Time" and "Elapsed Time" without looking up definitions externally.
- **Efficiency:** Weak. Ambiguous labels force users to pause and guess, slowing down data interpretation.
- **Memorability:** Low to Moderate. Users frequently forget the differences between near-duplicate terms between workout sessions, requiring repeated cognitive effort.
- **Error Recovery:** High operational safety since the view is read-only. However, it carries a high risk of data misinterpretation—users can easily misread total elapsed duration for actual active moving time.
- **Visual Asset:** Analytical grid highlighting the cognitive friction points within the data layout.

### UC2 · Slide 8 — Different User Types & Contexts
- **Beginners:** Encounter immediate confusion on the summary screens due to unexplained fitness jargon.
- **Experienced Athletes:** Easily parse the definitions, as they match standard terms used across other fitness ecosystems (e.g., Garmin Connect, Zwift).
- **Elderly Demographic:** Small typography within the dense sub-charts can make reading detailed numbers difficult.
- **Users with Disabilities:** Screen readers can easily process the clean, linear single-column layout, provided the accessibility labels are properly configured.
- **Visual Asset:** Comparative table contrasting data comprehension speed between Beginner and Experienced user types.

### UC2 · Slide 9 — Proposed HCI Solutions
- **Solution: Inline Progressive Disclosure Scaffolding**
  - *Action:* Add an info icon (ⓘ) next to ambiguous metric labels. Tapping it reveals a clear, one-line overlay definition (e.g., *"Moving Time: The time you were actively in motion. Elapsed Time: Your total duration from start to finish, including stops."*).
  - *HCI Principle:* Shifts the interface from a high-effort *recall* model to an effortless, context-rich *recognition* model.
- **Visual Asset:** UI design mockup showing an open tooltip providing clear metric explanations directly in context.

---

## USE CASE 3 — Exploring the Maps Tab (Segments)

### UC3 · Slide 1 — Overview
- **Goal:** Explore nearby geography to discover routes and highly trafficked competitive sections ("Segments") for future activities.
- **Interface Scope:** Maps Tab Dashboard → Suggested Regional Routes List → Popular Local Segments Map Overlay View.
- **Visual Asset:** `IMG_0529` (Maps landing tab view showcasing global filtering tools).

### UC3 · Slide 2 — User Interaction Context
- **Environmental State:** Relaxed indoor environment during trip planning or casual exploration.
- **User Attention:** Low-stress environment, open to exploratory interactions.
- **Interaction Method:** Multi-axis map panning, pinch-to-zoom map gestures, and horizontal sub-tab toggling.
- **Implicit Expectation:** The user expects to quickly understand map markers and filters without needing external explanation.
- **Visual Asset:** `IMG_0530` (Segments map interface displaying dense geolocated map pins).

### UC3 · Slide 3 — Use Case Interactions
- **Step 1:** Tap the central "Maps" icon on the bottom primary navigation bar.
- **Step 2:** Horizontal swipe across the top pill-button filter row to explore map criteria.
- **Step 3:** Tap the "Segments" tab button component to show crowd-sourced section rankings.
- **Step 4:** Perform standard pinch and drag actions to navigate map geography.
- **Visual Asset:** Interaction map diagram illustrating multi-axis map panning and tab selections.

### UC3 · Slide 4 — Human Capabilities Matrix
- **Vision & Attention:**
  - *Benefit:* Map view scales gracefully; pins dynamically cluster to prevent visual clutter at high zoom levels.
  - *Drawback:* The map view presents a high density of overlapping pins, route lines, and labels at low zoom levels, increasing visual search times.
- **Touch & Motor Control:**
  - *Benefit:* Employs standard, universally accepted map gestures (pinch-to-zoom, drag-to-pan), ensuring high accessibility.
  - *Drawback:* Tiny map pin targets require high precision to select, which can frustrate users with larger fingers or tremors.
- **Audio & Haptic Feedback:**
  - *Status:* Unused channel. Exploration relies entirely on real-time visual-spatial manipulation.
- **Memory & Cognition:**
  - *Drawback:* Introducing proprietary, app-specific terminology ("Segment") with zero onboarding explanations strains working memory.

### UC3 · Slide 5 — User Mental Model Analysis
- **The Jargon Barrier:** "Segment" is a proprietary term unique to the Strava ecosystem. To a novice user, the word lacks context and does not map onto existing mental models of general maps or geography.
- **Learning via High-Cost Trial & Error:** Lacking clean contextual hints, users must click through various sub-tabs recursively just to figure out what the feature does.
- **User Voice:** *"No, I really didn't understand it... I had to try tapping several tabs before I understood."*
- **HCI Paradigm Failure:** Breaches the usability goal of high *learnability*. Forcing a user to guess and experiment to decode basic interface labels indicates a broken conceptual model.
- **Visual Asset:** Map interface screenshot with a prominent question mark callout over the unexplained "Segments" sub-tab label.

### UC3 · Slide 6 — Interaction Metaphors
- **Affordance Mismatch:** The interface displays "Segments" in a horizontal row of pill-buttons right alongside "Length", "Elevation", and "Surface".
- **The Design Flaw:** While *Length, Elevation, and Surface* are self-explanatory map filters, *Segments* is a complex, data-heavy competitive community feature.
- **HCI Impact:** Giving these buttons identical visual styling incorrectly implies they are equally simple to understand, misleading users and complicating exploration.
- **Visual Asset:** Detailed close-up of the horizontal filter menu highlight bar.

### UC3 · Slide 7 — Usability Diagnostic
- **Learnability:** Poor. First-time users cannot understand the feature's core purpose from the label alone; understanding requires active experimentation.
- **Efficiency:** Low. The trial-and-error approach forces users to waste time tapping through multiple screens to find meaning.
- **Memorability:** Moderate. Once the user manually decodes the feature, the unique functionality maps reasonably well to long-term memory.
- **Error Recovery:** Adequate. Users can easily tap back to familiar filters (like Length) to recover from a confusing screen state.
- **Visual Asset:** Interaction graph mapping user confusion levels over time during map exploration.

### UC3 · Slide 8 — Different User Types & Contexts
- **Beginners:** Struggle immediately with the specialized terminology on the map interface.
- **Experienced Platform Users:** Navigate the view effortlessly, as they already understand the competitive leaderboard nature of local "segments".
- **Cross-App Transplants (e.g., Garmin/Zwift):** Easily recognize the term, as "segments" has become a shared design convention across modern fitness platforms.
- **Visual Asset:** User persona comparison matrix highlighting differences in term recognition.

### UC3 · Slide 9 — Proposed HCI Solutions
- **Solution: Contextual Dynamic Subtext Scaffolding**
  - *Action:* When a first-time user opens the Maps view, display a helpful one-line subtitle directly beneath the active tab: *"Segments: Popular timed road sections where you can compare times with other athletes."*
  - *HCI Principle:* Replaces blind trial-and-error with clear *recognition*, establishing an accurate mental model right from the first interaction.
- **Visual Asset:** Interface design mockup showcasing the clean implementation of introductory subtitle tooltips.

---

## USE CASE 4 — Exploring Groups (Challenges & Clubs)

### UC4 · Slide 1 — Overview
- **Goal:** Explore community features to find and join local clubs and fitness challenges.
- **The Interaction Paradox:** Users are highly motivated to find regional, real-world groups, but encounter major visual distractions and navigation blocks.
- **Visual Asset:** `IMG_0532` (Groups landing dashboard view showing active challenges).

### UC4 · Slide 2 — User Interaction Context
- **Environmental State:** Independent exploration session, stationary setting.
- **User Intent:** Locate an active running club in their local area (e.g., Ho Chi Minh City).
- **Observed Behavior:** The user's eye bypasses all descriptive card text and jumps straight to the brightest, highest-contrast element on the screen: the primary orange "Join" button.
- **User Voice:** *"When I see a club card or challenge card, I focus on the button and tap it without reading 'join'... and I assume I need to enter another space to see the detail page for this challenge."*
- **Visual Asset:** `IMG_0533` (Challenge card displaying the high-contrast Join call-to-action).

### UC4 · Slide 3 — Use Case Interactions
- **Step 1:** Tap the "Groups" icon on the main bottom tab navigation bar.
- **Step 2:** Toggle between the top "Challenges" and "Clubs" sub-tab views.
- **Step 3:** Tap directly on a Challenge or Club preview card to view details.
- **Step 4:** Tap the prominent orange button to join the community space.
- **Visual Asset:** Multi-step interface flow diagram tracking user tap points across the group cards.

### UC4 · Slide 4 — Human Capabilities Matrix
- **Vision & Attention:**
  - *Drawback:* The bright orange "Join" button creates intense color contrast against the dark background. This high visual salience instantly grabs peripheral vision (foveal pull), tricking users into tapping before they read the actual card text.
- **Touch & Motor Control:**
  - *Benefit:* Oversized rectangular button shapes provide massive, highly accessible touch target zones.
  - *Drawback:* High visual salience triggers an immediate touch reflex, causing users to tap the button prematurely without reviewing the card content.
- **Audio & Haptic Feedback:**
  - *Drawback:* Tapping the button changes its state silently without haptic or audio confirmation. Worse, the separate action for "view details" provides no visual hints, rendering it completely invisible.
- **Memory & Cognition:**
  - *Drawback:* The card forces a single touch surface to handle two completely different actions, overloading the user's focus and causing navigation errors.

### UC4 · Slide 5 — User Mental Model Analysis
- **The Expectation:** Based on standard card design conventions across modern mobile apps, users expect that tapping a card's primary call-to-action button will open a rich detail screen for that item.
- **The Reality:** Tapping the button instantly changes its state to "Joined" in-place on the feed, without navigating anywhere or opening further details.
- **User Voice:** *"Nothing happens, the button just changes status. What I expect is that it jumps into more detail... I got stuck trying to find the detail view by focusing on the button."*
- **HCI Heuristic Violation:** Severe mismatch with Shneiderman's Golden Rule #3 (Offer informative feedback). The system provides feedback for the state toggle but fails to support the user's primary goal: exploring details.
- **Visual Asset:** Graphical mockup showing a user tap on the button resulting in a dead-end "no navigation" error badge (✕).

### UC4 · Slide 6 — Interaction Metaphors
- **Affordance Blurring:** The card layout blends two distinct actions—*State Toggling* (joining a group) and *Navigation* (viewing group details)—into a single visual block.
- **HCI Structural Rule Failure:** Violates the core principle of *consistency and affordance*. Different actions should look distinctly different. Merging them onto one surface with no separation tricks users into unintended actions.
- **Visual Asset:** High-magnification interface teardown of the Group card components.

### UC4 · Slide 7 — Usability Diagnostic
- **Learnability:** Low. The user was unable to find the challenge detail screen during the testing session despite multiple attempts.
- **Efficiency:** Deeply compromised. Users waste time and clicks dealing with unintended group enrollments instead of viewing details.
- **Memorability:** Weak. The lack of distinct visual boundaries makes it consistently difficult to remember how to navigate the cards cleanly.
- **Error Recovery:** Poor. While users can tap the button again to leave a group, the interface offers no clear clues on how to successfully access the hidden details screen, leading to a navigation dead end.
- **Visual Asset:** Dynamic visual mapping tracking task failure rates during community discovery.

### UC4 · Slide 8 — Task Analysis Gap (Clubs Discovery)
- **The Stated User Goal:** *"Find an active running club near my location in Ho Chi Minh City."*
- **The Interface Failure:** The landing page displays a marketing promo for "Create Your Own Club" alongside a banner for the global official "Strava Club".
- **The Functional Deficit:** The tab lacks any location filters or local search tools on its main screen, making it impossible for users to find regional groups.
- **HCI Evaluation:** A major gap in task analysis. The interface fails to provide features to support a primary user goal, leading to a zero achievement rate.
- **Visual Asset:** `IMG_0534` (The localized Clubs exploration view showing the lack of local search tools).

### UC4 · Slide 9 — Proposed HCI Solutions
- **Solution A: Structural Affordance Separation (Card Redesign)**
  - *Action:* Change the card behavior so that tapping the card body opens the rich detail view (signaled by a clean right arrow icon). Shrink the "Join" option into a smaller, clearly separate button container.
  - *HCI Principle:* Uses clear, separate visual cues to match user expectations for distinct actions.
- **Solution B: Clear Direct Navigation Feedback**
  - *Action:* Right after a user taps "Join", display a brief confirmation message containing a direct link: *"Joined! Tap here to view challenge rules and details."*
- **Solution C: Goal-Driven Search Integration**
  - *Action:* Add a prominent "Find a Club Near You" search bar at the top of the Clubs tab, using automatic geolocation filters.
  - *HCI Principle:* Directly aligns the interface features with real-world user goals.
- **Visual Asset:** Comparative design mockup showing the current card layout next to the proposed redesigned card and search bar.

---

## CONCLUSION

### Slide — Key Strategic Takeaways
- **Core Recording Loop (Success):** The central tracking workflow (Start → Pause → Finish) is highly intuitive and easy to use for all experience levels ✓.
- **Supporting Workflows (Friction Points):** The features surrounding the core loop suffer from confusing fitness jargon, hidden navigation paths, and abrupt social popups ✕.
- **The Path Forward:** App usability can be dramatically improved through small, targeted UI changes: **clear task closure points, helpful inline definitions, and distinct buttons for distinct actions**.
- **Visual Asset:** Clean two-column summary layout summarizing strengths (✓) and areas for improvement (✕).

### Slide — Final Q&A Session
- **Thank You for Your Attention**
- Questions & Discussion
- UI/UX Product Research Report — Strava Platform
- CSC13112 · Group 03 · FIT-HCMUS
- **Visual Asset:** Clean closing graphic displaying group member names, student IDs, and contact info.