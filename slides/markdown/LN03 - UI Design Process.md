# UI Design Processes

## Overview
This lecture covers *how* UI design work is organized over time. It defines design, contrasts several software-process models (Waterfall, Shneiderman's interactive-systems lifecycle, Iterative, Spiral), and argues that **User-Centered Design (UCD)** — an iterative, spiral, user-involving process — is the preferred approach for interactive systems. It then restates the design principles (skill levels, task types, interaction styles, error prevention) and Shneiderman's Eight Golden Rules, and maps the abstract process onto the concrete PA1–PA6 project deliverables used in the course.

## Learning Objectives
After this lecture you should be able to:
- Define "design" and distinguish design from art.
- Explain the strengths and weaknesses of Waterfall, Iterative, and Spiral models for UI work.
- Describe Shneiderman's 8-stage interactive-systems lifecycle.
- Explain User-Centered / Participatory Design, its advantages and pitfalls.
- Apply UI design principles: skill levels, task frequency, interaction styles, error prevention.
- Map a real project onto an iterative user-centered process with prototypes and evaluation.

## Core Concepts

### What is design?
> **Design** is the "process of creating or shaping tools or artifacts for direct human use."

Design is characterized as:
- **A process/methods** — reliant on repeatable process, not just inspiration.
- **A creative endeavor** — envisioning new possibilities and outcomes among infinite options.
- **Producing things** — outputs are tangible artifacts.
- **Human-centered** — keeps humans as the central actors "in the loop."
- **A conversation with materials** — communicative and social.

### Design vs Art
Art is expressive (an artistic mug prioritizes aesthetic statement); good design is *functional for human use* (a good design as a mug prioritizes serving its purpose). Design must satisfy users' needs, not just the creator's expression.

## Frameworks

### Process models compared
| Model | Structure | Strength | Key weakness for UI |
|-------|-----------|----------|---------------------|
| **Waterfall** | Linear phases, each completed before the next | Simple, orderly; fine when requirements are stable | Users not involved until acceptance testing; late-discovered UI problems force costly requirement/design rework |
| **Shneiderman's lifecycle** | 8 named stages for interactive systems | Tailored to interactive systems; ongoing user involvement | Still fairly heavyweight/sequential |
| **Iterative** | Repeating Design→Implement→Evaluate cycles, a release per cycle | Feedback folded into next release | Repeatedly using customer time is expensive; customers may be unavailable |
| **Spiral** | Iteration + explicit risk assessment each loop | Risks resolved throughout; cheap early prototypes | More complex to manage |
| **User-Centered (UCD)** | Iterative+spiral focused on users & tasks, users involved throughout | Accurate info, buy-in, better fit | Users unavailable/expensive; users aren't designers |

### Waterfall Model
Phases: **Requirements definition → System & software design → Implementation & unit testing → Integration & system testing → Operation & maintenance.**
- **Core disadvantage:** difficult to handle changes.
- **UI-specific problems:** users aren't involved until acceptance testing; UI problems then ripple back into requirements and design, wasting earlier effort; rigid phase partitioning can't absorb changing requirements; only appropriate when requirements are well understood — and few business systems have stable requirements.

### Shneiderman's Interactive Systems Lifecycle (8 stages)
1. **Collect information** — organize the design team; get management & customer participation; interview users; questionnaires; estimate development/training/usage/maintenance costs; schedule with milestones and reviews.
2. **Define requirements and semantics** — high-level goals & mid-level requirements; consider task-flow sequencing alternatives; create task objects and actions; get management/customer agreement.
3. **Design syntax and support facilities** — compare display formats; design informative feedback per operation; review/evaluate/revise specs; run paper-and-pencil pilot tests or field studies with mock-ups/prototypes.
4. **Specify physical devices** — choose hard/softcopy devices; select audio/graphics/peripherals; account for environment (noise, lighting, table space); further pilot tests.
5. **Develop software** — use appropriate tools; write code; unit test.
6. **Integrate system and disseminate to users** — ensure user involvement at every stage; acceptance tests and fine-tuning; user documentation and training.
7. **Nurture the user community** — user support; monitor usage and measurement.
8. **Prepare an evolutionary plan** — plan for the system's future.

### Iterative Design
A repeating loop: **Design → Implement → Evaluate.**
- Each cycle is one iteration; a release is produced at the end of each.
- Customer feedback/evaluation feeds the next release.
- **Problems:** expensive to use customer time to test; customers may be unavailable; if customers don't like it, they don't buy.

### Spiral Model (Boehm, 1988)
- The process is a **spiral**, not a linear sequence with backtracking.
- Each loop = one phase; there are **no fixed phases** — loops are chosen by what is required.
- **Risks are explicitly assessed and resolved** throughout.
- **For UI design** (an improvement on plain iterative design):
  - Early cycles use **cheap prototypes**: paper prototypes, on-screen sketches, quick prototyping tools.
  - Provide **multiple prototype alternatives** (parallel prototyping).
  - Later cycles are better than earlier ones; only mature later releases go to users.

### User-Centered Design (UCD) / Participatory Design
- A type of iterative design with spiral structure, **focusing on users and tasks**:
  - **User analysis:** who uses the system.
  - **Task analysis:** what users need to do.
- **Users are involved throughout** — as evaluators, consultants, and sometimes designers — with **constant evaluation** of prototypes and releases.
- **Advantages:** accurate information and useful suggestions; opportunity to argue over design decisions; increased ego-involvement in the system's success (buy-in).
- **Potential problems:** users not always available; their time may be expensive; users aren't UI designers; users have strong egos/preferences; designers may over-obey user preferences.

## Process / Workflow

### The course's project process (maps to PA deliverables)
0. **Propose project** → **PA1**
1. **Perform user and task analysis** → **PA2**
2. Initially design sketches
3. Initially prototype
4. **Evaluate prototype** → **PA3**
5. Detail the prototype
6. **Evaluate prototype** → **PA4**
7. Implement
8. **Perform user testing** → **PA5, PA6**

This is a concrete instance of iterative user-centered design: analyze → sketch → prototype → evaluate → refine → implement → test.

### Applying UCD inside the class
- Students are themselves potential users of the proposed apps.
- Users help identify problems: other groups review a group's proposal; collect feedback from potential users; observe existing users' actions.
- Users review and give feedback at each milestone (cross-group review).
- User evaluation: by the end, everyone reviews another group's design.

### Design principles for interactive systems
**1. Determine users' skill levels:** novice/first-time; knowledgeable intermittent; expert/frequent.
**2. Identify the tasks by frequency:** frequent; less frequent; infrequent actions.
**3. Choose appropriate interaction styles:**
- Direct manipulation
- Menu selection
- Form fill-in
- Command language
- Natural language

**4. Apply Shneiderman's Eight Golden Rules** (see below).

**5. Prevent errors:**
- Constructive, informative error messages.
- Organize screens and menus functionally.
- Provide feedback about interface state.
- Guide to correct actions (e.g., **grayed-out** menu items).
- Support complete sequences (e.g., wizards offering both **Next** and **Finish**).

**6. Increase automation while preserving human control:** auto-suggestion, auto-completion — but always allow users to change/override.

### Shneiderman's Eight Golden Rules
1. Strive for consistency
2. Cater to universal usability
3. Offer informative feedback
4. Design dialogs to yield closure
5. Prevent errors, enable rapid recovery
6. Permit easy reversal of actions
7. Support user control
8. Reduce (short-term) memory load

### Succeeding in teamwork
- Define clear goals and expectations.
- Assign clear responsibilities/tasks to everyone.
- Talk about **accountability** — who is responsible when things go wrong.
- Meet **weekly** to review status even with nothing due; record meeting minutes.
- Work early rather than late.
- Understand teammates' motivation, commitment, and capability.

## Examples
- **Apple's design questions:** a lightweight critique lens — *What do you like about it? What do you not like? What is missing? What is superfluous?* — usable at any evaluation milestone.
- **Chindogu (Japan):** deliberately "useless inventions" — used to encourage free idea generation without prematurely judging feasibility ("Let your ideas flow").
- **Stage-goals diagram (design lifecycle):** early stages learn about stakeholders, discover goals/needs, ask "how is it done now? what is wanted? what else has been tried?"; middle stages generate many ideas and produce tangible artifacts to uncover subtleties; evaluation stages discover problems, assess progress, and determine next steps; final stages build the product and ramp up marketing/support/maintenance.

## Common Mistakes
- **Using Waterfall for interactive systems** — defers user contact to the end, guaranteeing expensive late rework.
- **Skipping user involvement** — designing from assumptions instead of evidence.
- **Polishing prototypes too early** — spend cheap paper/sketch prototypes first; save fidelity for later cycles.
- **Over-obeying user preferences** — users provide problems and feedback, not authoritative designs.
- **Ignoring skill-level differences and task frequency** when choosing interaction styles.
- **Weak teamwork discipline** — no clear ownership, no weekly cadence, no accountability.

## Practical Checklist
- [ ] Is the process iterative with real user involvement (UCD), not linear Waterfall?
- [ ] Have user analysis and task analysis been done before designing?
- [ ] Are early prototypes cheap (paper/sketch) and are alternatives explored in parallel?
- [ ] Is every prototype evaluated before proceeding?
- [ ] Are risks explicitly assessed each cycle (spiral thinking)?
- [ ] Are skill levels and task frequencies identified and matched to interaction styles?
- [ ] Are errors prevented (informative messages, grayed items, complete sequences)?
- [ ] Is automation balanced with user control/override?
- [ ] Does the design pass all Eight Golden Rules?
- [ ] Team: clear goals, ownership, accountability, weekly meetings, minutes, early work?

## Key Takeaways
- **Design is a human-centered, process-reliant creative endeavor** producing usable artifacts — distinct from art's self-expression.
- **Waterfall fails interactive systems** because it involves users too late; changes are then ruinously expensive.
- **Iterative → Spiral → User-Centered Design** is the progression: repeat cycles, add explicit risk handling, then center everything on users and tasks with continuous evaluation.
- **UCD is the preferred process** and the one used in this course, realized through the PA1–PA6 deliverables (propose → analyze → sketch → prototype → evaluate → refine → implement → user-test).
- Choose **interaction styles** by user skill level and task frequency; prevent errors; automate while preserving control.
- **Shneiderman's Eight Golden Rules** remain the portable design checklist.
- Good teamwork (clear ownership, accountability, weekly cadence) is part of the process, not separate from it.
