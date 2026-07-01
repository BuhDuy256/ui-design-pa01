# Fundamental Concepts: Human Capabilities & Usability Dimensions

## Overview
This lecture builds the *scientific foundation* for UI design: it first surveys human perceptual, cognitive, and motor capabilities (and their limits), then shows how those limits translate into concrete design principles and quantitative laws. It expands each usability dimension — **Learnability, Efficiency, Memorability, Errors, Satisfaction** — into actionable heuristics, and closes with mental models, metaphors, conceptual models, and Shneiderman's Eight Golden Rules.

The through-line: **design decisions are constrained by how humans sense, think, and move. Know the human, and the interface rules follow.**

## Learning Objectives
After this lecture you should be able to:
- Describe the human sensory, cognitive, and motor systems and how their limits shape UIs.
- Apply memory concepts (short-term vs long-term, chunking, recognition vs recall) to design.
- List and apply the design qualities for good usability: visibility, accessibility, consistency, affordances, feedback, natural mapping.
- Use Fitts's Law and the Power Law of Practice to reason quantitatively about efficiency.
- Explain mental models, conceptual models, and interface metaphors, and their trade-offs.
- Recall and apply Shneiderman's Eight Golden Rules.

## Core Concepts

### The three human subsystems
Every interaction loops through three human systems; design must respect all three.
| System | Role | Design relevance |
|--------|------|-----------------|
| **Senses** | Detect changes/information (sight, hearing, touch primarily) | Determines what output the UI can use |
| **Cognition** | Process and interpret input | Determines memory load, learnability |
| **Motor system** | React (produce output) | Determines input methods, error rates |

Human abilities *and limitations* constrain the design space — the limitations are the design rules in disguise.

### Human vision
- **View frustum:** the eye sees a small region in high detail (fovea) and the periphery mostly detects *movement*, not detail. → Put detail where the eye focuses; use motion to attract peripheral attention.
- **Color perception:** two receptor types on the retina —
  - **Rods:** ~120 million, black/white, ~1000× more light-sensitive than cones (night/low-light, motion).
  - **Cones:** ~6–7 million, color; distribution ~60% Red, ~30% Green, ~10% Blue.
- **Color blindness:** ~7–8% of males and ~0.4% of females cannot distinguish red from green. → **Never encode critical information by color alone.**
- **Stereopsis (depth):** monocular cues (color, brightness, shape) + binocular cues (size, interposition, perspective, parallax).

### Human audition (hearing)
Perceptible attributes: **pitch** (frequency, 20–20,000 Hz), **loudness** (amplitude, 30–100 dB), **location** (source & stream separation), **timbre** (sound type). → Sound is useful for alerts and feedback but is transient and easily missed.

### Human touch
Three sensations via different receptors: **pressure** (normal), **intense pressure** (heat/pain), **temperature** (hot/cold). Relevant properties: sensitivity, dexterity, flexibility, speed. Important for mice, keyboards, buttons, VR, surgery.

### Motor system (human output)
Capabilities: range of movement, reach, speed, strength, dexterity, accuracy — these drive workstation and device design. The motor system is a frequent **source of errors**: wrong button, double- vs single-click confusion, undetected mid-air gestures. Principles: **feedback is important**, and **minimize eye movement**.

### Human memory
- **Short-term (working) memory:** small (~7 items/chunks), short-lived (~10 seconds). Repetition helps retain; distraction erases.
- **Long-term memory:** effectively unlimited size and duration.
- **Learning** = transferring information from short-term to long-term memory; **elaborative rehearsal** helps the transfer.

### Chunking
A **chunk** is a unit of memory/perception. How many chunks a display costs depends on presentation and on prior knowledge:
- `H A P P Y V A L E N T I N E` (spaced letters) = hard to remember (many chunks).
- `HAPPY VALENTINE` (words) = easy (few chunks).
- Phone numbers grouped `0888.247.247` are easier than `0888247247`.
→ **Group and format information to reduce chunk count.**

### Recognition vs Recall
- **Recognition:** remembering *with* a visible cue (you recognize a face). Easier.
- **Recall:** remembering *with no cue* (you must produce a name from memory). Harder.
- **Design implication:** prefer recognition over recall. Menus, icons, and visible options let users recognize; command lines force recall. This is why **direct manipulation and visual presentation are more learnable than command-line interfaces.**

## Definitions
- **Usability** — how well users can use the system's functionality (dimensions: learnability, efficiency, memorability, errors, satisfaction).
- **Mental model** (Craik, 1943) — "internal constructions of some aspect of the external world enabling predictions to be made." Users build one through learning and using a system: *how to use it* (what to do next) and *how it works* (for unfamiliar/unexpected situations). Can be **deep or shallow** (e.g., how to drive a car vs. how the engine works).
- **Interface/interaction metaphor** — "a set of user interface visuals, actions and procedures that exploit specific knowledge that users already have of other domains," giving users instantaneous knowledge of how to interact. Designed to resemble physical entities while having their own properties.
- **Conceptual model** — the mental model people carry of *how something should be done*; described in terms of **core activities, objects, and interface metaphors**.
- **Chunk** — a unit of memory or perception.

## Principles

### Four pillars of designing for good usability
1. **Visibility** — operations should be visible to users.
2. **Accessibility** — reachable/usable by the range of users.
3. **Consistency** — similar things behave similarly.
4. **Affordances** — the object's appearance suggests how to use it (which one is a button?).

Plus **feedback**, **natural mapping**, and **platform standards** below.

### Visibility
- Make operations visible. Unix commands are very *invisible*; Windows menus are visible. Right-click menus and drag-drop are less visible (a reason iOS limits right-click) — though drag-drop is a valuable direct-manipulation style mirroring the real world.
- **Trade-off: Visibility vs Simplicity** — more visible options can reduce simplicity. Balance them.

### Feedback
Actions should have **immediate effects** (buttons, scroll bars, cursor changes). Feedback channels: **audio, visual, haptic** (e.g., vibration).

### Natural mapping
Physical arrangement of controls should match the arrangement of the things they control (light switches, car turn signals). Map directly where possible — but it doesn't *always* have to be literal.

### Consistency
- **Similar things should work similarly** (fonts, colors, icons, layouts); **different things should look different**.
- Three types: **Internal** (within the system), **External** (across systems), **Metaphorical** (reflecting real-world objects, e.g., a printer icon for print).
- **Speak the user's language:** common words, avoid slang/jargon — but also avoid wordiness.

### Platform standards
Follow platform guidelines (MS Windows UI guidelines, Apple UX guidelines), follow framework look-and-feel conventions, and learn from existing applications.

### Metaphor trade-offs
| Advantages | Problems |
|-----------|----------|
| Highly learnable | Hard to design an appropriate metaphor |
| Connects to existing mental model | Potentially deceptive/misleading |
| | May be applied inconsistently |
| | Culturally dependent (localization) |

## Frameworks

### Usability goals & measurable targets
Each dimension maps to a measurement and a direction (increase/reduce):
| Usability goal | Measure | Target |
|----------------|---------|--------|
| Time to learn | How long to learn the actions for a task set | Reduce |
| Speed of performance | Time to carry out benchmark tasks | Reduce (increase speed) |
| Rate of errors | Number/kind of errors on benchmark tasks | Reduce |
| Retention over time | Knowledge retained after an hour/day/week | Increase (memorability) |
| Subjective satisfaction | How much users liked the interface | Increase |

### UX vs Usability
- Usability = evaluation of understandability; UX = holistic design and feeling.
- "Designing it right" (usability) vs. "the right design" (UX).
- Poor usability *often* leads to bad UX — **but not necessarily**.

### Shneiderman's Eight Golden Rules
1. Strive for consistency
2. Cater to universal usability
3. Offer informative feedback
4. Design dialogs to yield closure
5. Prevent errors, enable rapid recovery
6. Permit easy reversal of actions
7. Support user (internal locus of) control
8. Reduce short-term memory load

## Quantitative Laws (Efficiency)

### Fitts's Law
Time **T** to move the hand to a target of size **S** at distance **D** from the pointer:
```
T = a + b * log2(D/S + 1)
```
- `a`, `b` are empirical constants.
- `log(D/S + 1)` is the **index of difficulty** — bigger/closer targets are faster.

**Implications:**
- Group similar targets together.
- Screen **edges and corners** are easy to hit (effectively infinite size — the pointer stops there).
- **Pie (circular) menus** are ~15–20% faster than linear menus (Callahan et al., 1991) and support spatial memory.
- Avoid lengthy menus.
- Make often-used targets **big**.

### Power Law of Practice
Time **Tn** to perform a task the nth time:
```
Tn = T1 * n^(-a)          (a typically 0.2–0.6)
```
**Implications:** with practice, novices improve rapidly at first, then performance flattens (matching Nielsen's learning curve). Design should reward repeated use.

## Process / Workflow

### Formulating a conceptual model
Ask, in order:
1. What will users be doing when carrying out their tasks?
2. How will the system support these?
3. What interface metaphor fits?
4. What interaction modes and styles to use?

### Principles to improve efficiency (checklist form below)
Make targets big; group targets used together; put often-used menu items on top; use screen corners/edges; provide keyboard shortcuts and accelerators; predefine style groups; aggregate and preselect the most common choices by default; keep history (recent files); auto-completion, auto-suggestion, and anticipation of the next action.

## Examples
- **Mini memory experiment:** students try to memorize a scattered list of ~15 items; recall improves when items are familiar, funny, attention-grabbing, related, or repeated — demonstrating chunking and rehearsal.
- **Recognition vs recall in the real world:** you recognize a friend's face instantly but may fail to recall their name; you don't recall every item in Notepad's File menu but recognize each function on sight.
- **Ballot example (write-in vs. checkbox):** a "write the candidate's name" ballot demands *recall*; a checklist of names supports *recognition* — the latter is more usable.
- **Glanceable UIs / iOS shortcuts / Mr. Porter:** show recognition-supporting, low-memory-load design.
- **Delete "keymap.txt":** command line requires remembering exact syntax (recall); direct manipulation (select + delete) requires only recognition — more learnable.
- **Circular menus (Autodesk SketchBook, Nokia Lumia camera):** shorter average acquisition time and spatial-memory support, illustrating Fitts's Law in production apps.
- **Gmail's discarded "Discard" button / mobile dropdown history:** evolution of menu/efficiency patterns over time.
- **Lyft's unconventional search bar:** research-driven deviation from Material/iOS defaults — standards are a starting point, not a cage.

## Common Mistakes
- **Encoding meaning by color alone** — fails ~8% of male users (red/green color blindness).
- **Forcing recall when recognition would do** — hidden commands, memorized syntax, invisible gestures.
- **Overloading short-term memory** — more than ~7 chunks at once.
- **Inconsistent behavior** — similar controls acting differently, or unrelated controls looking identical.
- **Bad or missing feedback** — actions with no immediate visible/audible/haptic response.
- **Poor metaphors** — misleading, culturally-specific, or inconsistently applied.
- **Conflicting with the user's mental model** — designs that fight what users already expect.
- **Lengthy linear menus / tiny scattered targets** — violate Fitts's Law.
- **Bad grouping** (e.g., Acrobat Reader for Mac menus) hurting efficiency.

## Practical Checklist
Design/evaluation checklist distilled from this lecture:
- [ ] Detail placed where the eye focuses; motion used for peripheral alerts.
- [ ] Critical info never relies on color alone.
- [ ] Information grouped/formatted to minimize chunks (≤ ~7 at a time).
- [ ] Recognition favored over recall (visible options, icons, menus).
- [ ] Every action gives immediate feedback (visual/audio/haptic).
- [ ] Controls map naturally to what they affect.
- [ ] Consistent internally, externally, and metaphorically; user's language used.
- [ ] Platform/framework guidelines followed.
- [ ] Frequent targets are big, grouped, and near edges/corners (Fitts's Law).
- [ ] Shortcuts, defaults, history, and auto-completion provided for experts.
- [ ] Design aligns with users' existing mental models.
- [ ] Cross-check against Shneiderman's Eight Golden Rules.

## Key Takeaways
- **Design follows human limits:** ~7-item short-term memory, red/green color blindness, foveal vs peripheral vision, and motor-error tendencies are the real source of most UI rules.
- **Recognition beats recall** — the single strongest argument for visual, direct-manipulation interfaces over command lines.
- **Chunking** turns memory limits into a formatting/grouping strategy.
- **Fitts's Law** (`T = a + b·log2(D/S+1)`) and the **Power Law of Practice** (`Tn = T1·n^-a`) let you reason about efficiency quantitatively; corners, edges, big grouped targets, and pie menus win.
- **Visibility, accessibility, consistency, affordances, feedback, natural mapping** are the concrete qualities of a usable interface.
- **Mental models, metaphors, and conceptual models** connect the interface to knowledge users already have — powerful but culturally and cognitively delicate.
- **Shneiderman's Eight Golden Rules** are the portable summary to memorize.
