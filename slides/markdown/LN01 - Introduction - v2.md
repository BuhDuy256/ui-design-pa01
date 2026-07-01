# Introduction to User Interface Design & Usability

## Overview
This lecture opens a specialization course on User Interface (UI) Design within Software Engineering. Beyond course logistics, its core knowledge content introduces **Human–Computer Interaction (HCI)** and **usability**: what usability means, the dimensions used to measure it, why it matters commercially and ethically, the problems that make UI development hard, and the human factors that constrain every design decision.

## Learning Objectives
After this lecture you should be able to:
- Define UI, usability, and UX using their ISO definitions, and distinguish the three.
- List and explain the five usability dimensions and know which user type each serves.
- Explain why usability is a business/survival concern, not a cosmetic one.
- Locate usability within the broader hierarchy of system acceptability.
- Identify the human factors (memory, error tendency, diversity) that shape UI design.
- Critique a UI against the usability dimensions ("Hall of Fame or Shame").

## Core Concepts

### Human–Computer Interaction (HCI)
The field studying how people interact with computers/machines. It is referred to by many interchangeable names — the variety of terms signals that the concern is broader than "graphics on a screen."

### The UI ⊃ Usability ⊃ UX relationship
- **UI** is the concrete set of components (controls + information) a user touches.
- **Usability** measures *how well* users operate that UI to reach goals.
- **UX** is the *subjective, holistic* perception and emotional response before, during, and after use. Good usability is usually necessary but not sufficient for good UX.

### Usability as one attribute among many
Usability is not the whole picture. In Nielsen's model it sits under *usefulness*, which sits under *practical acceptability*, which combines with *social acceptability* to form overall **system acceptability**. A usable system can still fail if it lacks utility, costs too much, or is socially unacceptable.

## Definitions
Official ISO definitions (preserve verbatim):

| Term | Definition | Source |
|------|-----------|--------|
| **User Interface (UI)** | "all components of an interactive system that provide information and controls for the user to accomplish specific tasks with the interactive system" | ISO 9241-110:2006 |
| **Usability** | "extent to which a system, product or service can be used by specified users to achieve specified goals with **effectiveness, efficiency and satisfaction** in a specified context of use" | ISO 9241-11:1998 |
| **User Experience (UX)** | "person's perceptions and responses resulting from the use and/or anticipated use of a product, system or service" | ISO 9241-210:2010 |

Working definition used in class: **Usability = how well users can use the system's functionality.**

## Principles
- **Usability is a condition for survival.** Products with poor usability are abandoned.
- **Users judge a system by its interface, not its functionality.** The interface *is* the product to the user.
- **A poor interface can cause catastrophic errors** — in life-critical systems this is not hyperbole.
- **User's time doesn't follow Moore's Law.** Hardware gets cheaper; human time does not. Saving user time and error-recovery time is a direct, compounding cost saving.

## Frameworks

### The Five Usability Dimensions (Nielsen)
| Dimension | Question it answers | Primarily serves |
|-----------|--------------------|------------------|
| **Learnability** | How easy is it to learn and start using? | Novice / first-time users |
| **Efficiency** | How quickly can tasks be performed once learned? | Expert / frequent users |
| **Memorability** | How easily is proficiency re-established after time away? | Infrequent / returning users |
| **Errors** | How often do errors happen; how easy is recovery? | All users |
| **Satisfaction** | Are users subjectively pleased with the UI? | All users |

**Key insight:** the *importance* of each dimension varies by audience. A tool for daily experts should optimize efficiency; a rarely-used kiosk should optimize learnability and memorability.

### What makes a user "novice" or "expert"
Expertise is not a single trait; it is layered:
- **Domain experience** — knowledge of the problem area.
- **Application experience** — familiarity with this specific software.
- **Feature experience** — familiarity with the specific feature being used.
A person can be an expert in the domain yet a novice in the application.

### System Acceptability hierarchy (Nielsen, 1994)
```
System acceptability
├── Social acceptability
└── Practical acceptability
    ├── Cost
    ├── Compatibility
    ├── Reliability
    ├── ... (etc.)
    └── Usefulness
        ├── Utility        (does it do what's needed?)
        └── Usability      (can it be used well?)
```

### Human factors that constrain UI design
- **Limited short-term memory** — people hold ~7 items; presenting more induces mistakes.
- **Error cascades** — once people make a mistake, they tend to make more.
- **People differ** — varying physical capabilities.
- **Different preferences** — some prefer pictures, some prefer text.

## Process / Workflow

### Why HCI matters — motivating domains
- **Life-critical systems:** hospitals/ER, nuclear reactors, air traffic control, 911 dispatch, fire/police.
- **High-volume commercial systems:** banking, insurance, reservations, credit cards, inventory/sales/billing.
- **Diverse population, limited training:** office automation, home/personal/educational computing.
- **Enhancing human intellect:** creative/movie-effects workstations, decision-support/expert systems, information retrieval, simulation and training.

### Why UI development is hard (project reality)
- UI consumes a large share of lifecycle cost — a common split: application algorithms ~40%, dialogue management ~40%, presentation ~20% (i.e., ~60% of code is interface-related).
- UI development is extremely labor-intensive.
- UIs need frequent, extensive modification.
- Modifications are hard when UI and application logic are tightly interwoven (argues for separating presentation from logic).

## Examples

### "Is this easy to learn?" — the bare terminal
A macOS bash terminal prompt teaches the **learnability** concept: it is maximally *efficient* for experts but has near-zero learnability for a novice — nothing on screen tells you what to do. Demonstrates that efficiency and learnability can trade off.

### UI Hall of Fame or Shame (critique exercises)
A recurring exercise: critique real UIs against the five dimensions. Examples shown and what each teaches:
- **"Language Switch → OK" dialog:** an OK button with no visible cancel/decline forces a choice — poor error prevention and control.
- **"Account does not exist" registration flow:** confusing/negative feedback during signup — hurts satisfaction and error recovery.
- **MS Word Options dialog with many tabs / Eclipse Preferences tree:** feature overload strains short-term memory and learnability.
- **Clippy ("It looks like you're writing a letter"):** intrusive, low-satisfaction assistance — a classic shame example.
- **Vnexpress.net "then vs. now":** cluttered legacy layout vs. cleaner modern one shows visual simplicity improving usability over time.
- **Physical example (building stairs):** the "Hall of Fame or Shame" idea applies to physical design too — affordances exist in the real world.

### BMW Natural Interaction / Microsoft Vision 2030 (videos)
Illustrate emerging interaction modes (gesture, voice, natural interaction) beyond the mouse/keyboard GUI.

## Common Mistakes
- **Treating UI as cosmetic polish** added at the end, rather than a survival-level concern.
- **The designer assuming they are the user.** A software engineer is trained to communicate with engineers, but the UI must communicate with users.
- **Overloading working memory** by presenting far more than ~7 items at once.
- **Tightly coupling UI and application logic**, making later UI changes expensive.
- **Blindly obeying "the user is always right."** Consistent user errors *do* signal a wrong interface — but users are not designers, so their stated solutions aren't authoritative.

## Practical Checklist
When evaluating or designing a UI, ask:
- [ ] Who are the users, and where do they sit on domain/application/feature experience?
- [ ] Which usability dimension matters most for *this* audience?
- [ ] Learnability: can a first-timer figure out what to do with no training?
- [ ] Efficiency: can a returning expert act quickly (shortcuts, grouping)?
- [ ] Memorability: after a week away, is proficiency easy to recover?
- [ ] Errors: are errors prevented, and is recovery easy and non-destructive?
- [ ] Satisfaction: is the interaction pleasant, not intrusive?
- [ ] Are more than ~7 items shown at once without grouping?
- [ ] Is presentation separated from application logic to ease future change?

## Key Takeaways
- Usability = effectiveness + efficiency + satisfaction, for *specified users, goals, and context* (ISO 9241-11).
- Remember the five dimensions: **Learnability, Efficiency, Memorability, Errors, Satisfaction** — and that their weight depends on the user.
- UI ⊂ Usability ⊂ UX: components → measured quality of use → subjective whole experience.
- Usability is a business survival factor: users judge products by their interface, and their time is expensive.
- Design around human limits: ~7-item memory, error cascades, and human diversity.
- Recommended classic readings: *Usability Engineering* (Nielsen, 1994) and *The Design of Everyday Things* (Norman, 2013).
