# User Research & Task Analysis

## Overview
This lecture covers the *front end* of user-centered design: understanding **who** the users are (user analysis), **what** they need to do (task analysis), and the **data model** behind their work (domain analysis). It presents the data-gathering techniques (observation, interviews, questionnaires), the critical caveat that *what users say ≠ what users do*, the Hierarchical Task Analysis (HTA) method for decomposing tasks, personas for communicating user understanding, and the structure of the resulting requirements document. It closes with UI-quality anti-patterns (over-design, inconsistency).

## Learning Objectives
After this lecture you should be able to:
- Perform user analysis: identify and describe target users and their characteristics.
- Perform task analysis: capture goals, preconditions, and subtasks; rank by frequency/importance.
- Choose appropriate data-gathering techniques and understand their trade-offs.
- Explain why observation is often more reliable than self-report, and design interviews accordingly.
- Build a Hierarchical Task Analysis (HTA) decomposition.
- Conduct domain analysis to produce object/data models.
- Create a persona and assemble a complete requirements document.

## Core Concepts

### User analysis
> **User analysis** — the process of identifying and describing the users who use the system.

Capture target-user **characteristics**: age, gender, culture, language; computer experience; domain & application experience; usage frequency; physical limitations; education; motivation; work environment; user relationships; social status/role/position.

A user **description** documents:
- General information
- User characteristics (above)
- **User environment** — where tasks are performed
- **Major goals of the job** — what is the end result?
- **User roles** (e.g., buyer, seller), if any
- **User preferences**
- **Relationships among users**, if any

Users can be segmented **by role** and **by language/culture**.

### Task analysis
> **Task analysis** — the process of analyzing and documenting the tasks the system may provide to users.

For each task capture:
- **Goal** — what needs to be done.
- **Precondition** — what conditions must hold to do it.
- **Subtasks** — what steps are taken.

Each task is usually a **goal to achieve**. Task analysis is an early UI-design step that provides the basis for **UI design, UI evaluation/improvement, and user documentation.**

### Domain analysis
> **Domain analysis** — the process of identifying data models for the system domain: the people and things, and how they are related.

Outputs: **object/class models** (UML class diagram) and **data models** (Entity-Relationship models). Example: HaiLua.com.vn's high-level class model relates *Admin, Farmer, Customer, Product, ShoppingCart* with multiplicities (e.g., a Customer has one ShoppingCart; Farmers post many Products).

### Why you cannot just ask users
- **People are notoriously bad at predicting** what they'd use or prefer hypothetically. They respond much better to **actual, concrete things or comparisons.** → This is the core argument for **observation and prototypes.**
- **Watch what users do, not (only) what they say.** Mismatches between saying and doing often hold the keys to new designs.
  - *Henry Ford (attrib.):* "If I had asked my customers what they wanted, they would have said a faster horse."
- **Users *can* reliably tell you**: what they are doing *right now*, how they feel *right now*, and what their goal is *right now*.
- **But you cannot only observe either:** looking alone won't reveal motivations, internal thought processes, or hidden motives; observation can be slow, hard to scale, and impossible in some settings (disaster, police work).

## Frameworks

### Data-gathering techniques (shared by user & task analysis)
| Technique | Notes |
|-----------|-------|
| **Data recording** | Documents/manuals/instructions; notes; audio; photographs; video; combinations |
| **Interviews** | Structured / unstructured / semi-structured (see below) |
| **Questionnaires** | Closed or open questions; scale to large populations |
| **Observation** | Direct or indirect (see below) |
| **Combination** | Mix the above |

**Obstacles:** designers and users are sometimes isolated; users get overlooked and designers make wrong assumptions; some users (executives, doctors, high-ranking people) are expensive/hard to reach.

### Interview types
| Type | Description | Trade-off |
|------|-------------|-----------|
| **Structured** | Tightly scripted, questionnaire-like | Replicable but may lack richness |
| **Unstructured** | No script | Rich but not replicable |
| **Semi-structured** | Script-guided, but interesting issues explored deeper | Best **balance** of richness and replicability |

### Observation
- **Direct observation** — in the field or controlled environments; use structuring frameworks and the **think-aloud protocol** (person narrates what they're doing while doing it; observer asks probe questions). Caveat: probing and thinking aloud *affect* performance.
- **Indirect observation** — tracking activities: physical location/movement, interaction logging, timers.

**What observers look for:** opportunities for new designs, **breakdowns**, **workarounds**, and **mismatches between what users say and do** — each is a design opportunity (workarounds and unexpected/customized uses reveal unmet needs).

**Ways to look at what users really do:** Behavioral Archaeology, Behavioral Mapping, Fly on the Wall, Guided Tours, Personal Inventory, Rapid Ethnography, Shadowing, Social Network Mapping, Still-Photo Survey, Time-Lapse Video.

### Questionnaires (deeper)
- Disseminate by paper, email, web; questions **closed** (easier to analyze, computer-scorable) or **open**.
- Scale to large populations; **sampling is a problem when population size is unknown** (common online).
- **Online questionnaires** — advantages: fast responses, direct-to-database collection, reduced analysis time, easy error correction, many tools (e.g., SurveyMonkey). Problems: sampling if population unknown; preventing duplicate responses; delayed response.

### Hierarchical Task Analysis (HTA)
- **Task decomposition** aims to: describe the actions people do, describe the order of subtasks, and structure them in a **task–subtask hierarchy**.
- **HTA** — introduced by **Annett and Duncan (1967)** to evaluate an organization's training needs; now widely used in interface design. It breaks tasks into subtasks and operations/actions, represented in a **structure chart**.
- Includes: identifying/categorizing tasks, identifying subtasks, and checking the model's overall accuracy.
- **Value:** lets designers envision the goals, tasks, subtasks, operations, and plans essential to users' activities.

### Personas
A **persona** is a concrete, fictional-but-evidence-based archetype of a user, drawn from user research, used to communicate and keep the team focused on real user needs. Course exercise: interview the person who knows most about your users, then **draw a persona** and describe the user.

## Process / Workflow

### Task analysis procedure (two steps)
1. **Model tasks**
   - Gather information.
   - Describe tasks into requirements.
   - Concretely: create a list of all user tasks → rank by **frequency of use and importance** → gather detailed info per task → model relationships (e.g., use-case model) between tasks & users and among tasks → present tasks as documents/diagrams.
2. **Evaluate and refine requirements**
   - Review and update requirements; simplify and fix issues.
   - **Evaluation techniques:** walk-through, formal review/inspection, offline review, online review.

### Generating an HTA hierarchy
1. Start from the **overall goal** (e.g., "clean the house").
2. Get the list of tasks.
3. Break down into **numbered sub-tasks**; group into higher-level tasks; decompose the lowest-level tasks further.
4. Describe each sub-task.
   - **Stopping rule:** stop when a subtask is simple enough (e.g., is "empty the dust bag" atomic enough?). Judgment call — decompose until further detail adds no design value.

**Example HTA (HaiLua.com.vn "Buy product"):**
```
1. Buy product
   1.1 Search products
       1.1.1 View products
             1.1.1.1 Add to shopping cart
             1.1.1.2 Remove products from cart
             1.1.1.3 Edit shopping cart
             1.1.1.4 Check out
                     1.1.1.4.1 Provide credit card information
                     1.1.1.4.2 Provide shipping information
                     1.1.1.4.3 Submit order
                               1.1.1.4.3.1 View confirmation
                               1.1.1.4.3.2 View receipt
                               1.1.1.4.3.3 Receive product
   1.2 Compare products
```

### The requirements document
Assembles the outputs of all three analyses:
- **User analysis** — description of target users (general info, characteristics, environment, major job goals, roles, preferences, relationships).
- **Task analysis** — for *each task*: goal/precondition/subtasks; **where** performed (internet/desktop/mobile, kiosk/workstation); **how often** (per hour/day/month); **resource constraints** (1 second / 1 minute / unconstrained); **how it's learned** (training, install-and-use, by trying, by watching others); **task exceptions** and how they're handled; **who else** is involved.
- **Models** — use-case model (user & task analysis); object model and ER model (domain analysis).

## Examples
- **HaiLua.com.vn:** a web app for buying/selling farming products (post to sell, search, buy, compare prices/characteristics, rate sellers/buyers, comment/feedback). Users segmented by role (Buyers/Customers, Sellers = farmers & traders, Administrator) and by language/culture (Vietnamese farming products). Runs through the whole lecture as the worked example (user analysis → HTA → class model).
- **The taxi driver interview** (key teaching case): asked directly "how do you start your day?", the driver gave a useless vague answer ("I just start my taxi and look for passengers"). Re-framed as *"teach me to drive your taxi tomorrow while you're away,"* he produced a rich, ordered procedure: wind up the meter (new people forget; a stopped meter loses money), check fuel level to the halfway mark (shared taxi handover rule), check oil (indicator broken, must open the bonnet)... — **Lesson: framing the question as teaching/role-play unlocks tacit, step-by-step task knowledge that direct questioning misses.**
- **Jofish Kaye (Yahoo Research) wallet study:** to understand personal financial practices, had people empty their wallets and talk through the contents — a **Personal Inventory** technique that surfaces real behavior via concrete artifacts.

### UI quality anti-patterns (critique examples)
- **Over-design:** overblown visuals vs. a clean, functional design — decoration that harms usability.
- **iPhone Mail vs. Yahoo Finance:** consistent design makes touchable/untouchable elements obvious; inconsistent design confuses which elements are interactive.
- **Notepad++ Preferences dialog:** inconsistent grouping — two top groups have only one item each, and "Show status bar" belongs to no group.
- **MS PowerPoint vs. Notepad++ toolbars:** large labeled buttons (learnable) vs. small unlabeled buttons (cryptic).

## Common Mistakes
- **Relying on what users say** rather than what they do — self-report is unreliable for hypotheticals.
- **Asking vague, direct questions** ("describe your day") instead of concrete/role-play framings that elicit tacit steps.
- **Skipping observation** — missing breakdowns, workarounds, and say/do mismatches that reveal opportunities.
- **Designers making assumptions about users** they never actually studied.
- **Unknown-population sampling** and **duplicate responses** in questionnaires.
- **Over-decorating UIs** and **inconsistent grouping/labeling** — hurting learnability and clarity.
- **Decomposing HTA endlessly** past the point of design usefulness (or stopping too early).

## Practical Checklist
**User analysis**
- [ ] Target users identified and described (characteristics, environment, goals, roles, preferences, relationships)?
- [ ] Users segmented by role and by language/culture where relevant?

**Data gathering**
- [ ] Chosen technique(s) fit the constraints; observation included, not just interviews/surveys?
- [ ] Interviews semi-structured for balance; think-aloud used where appropriate?
- [ ] Questions framed concretely / as role-play to surface tacit knowledge?
- [ ] Questionnaire sampling and duplicate-response risks addressed?

**Task analysis**
- [ ] All tasks listed and ranked by frequency and importance?
- [ ] Each task has goal, precondition, subtasks, location, frequency, constraints, learning method, exceptions, other actors?
- [ ] HTA hierarchy built, numbered, and decomposed to a sensible stopping point?
- [ ] Requirements evaluated and refined (walk-through/review)?

**Domain analysis**
- [ ] Object/class model and ER model produced for the domain?

**Communication**
- [ ] Persona(s) created to represent key users?
- [ ] Complete requirements document assembled (user + task + domain, with use-case/object/ER models)?

## Key Takeaways
- **User-centered design starts with research:** user analysis (who), task analysis (what/how), domain analysis (data model).
- **Observe more than you ask** — users can't reliably predict preferences, but can report their current activity, feelings, and goals; watch for say/do mismatches, breakdowns, and workarounds.
- **Reframe questions concretely** (the taxi-driver lesson) to extract tacit, step-by-step procedures.
- **Semi-structured interviews** best balance richness and replicability; **think-aloud** reveals in-the-moment reasoning.
- **HTA (Annett & Duncan, 1967)** decomposes goals into numbered subtasks/operations in a structure chart — the backbone of task documentation.
- **Personas** turn research into a shared, memorable representation of users.
- The **requirements document** consolidates everything (per-task: goal, precondition, subtasks, where, how often, constraints, learning, exceptions, actors) plus use-case, object, and ER models.
- Watch for UI anti-patterns: **over-design** and **inconsistency**.
