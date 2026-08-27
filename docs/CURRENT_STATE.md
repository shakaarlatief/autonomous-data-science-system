# Current State

**Checkpoint:** 234  
**Date:** 2026-08-27  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration branch base:** `v1-frontend-spike` at Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at feature-promotion head `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C browser-rendered Project Cockpit design evaluation. P7 Neutral Tag + Tone remains accepted as the current project-disposition visual direction. The stronger current-process focus lens is accepted in principle, and the active gate now tests user-curated focus membership so individual work units can be added to or removed from the current focus set without deleting them or changing disposition.  
**Latest specification:** Specification 024 remains accepted. Specification 008 remains the promoted V1 Project Cockpit interaction architecture.  
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no scientific comparison may be inferred from that run.

## Active interaction context

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-08
Conversation title       08 - Project Cockpit Design Exploration
Primary collaborator     ChatGPT
```

Repository artifacts remain authoritative across chats and models.

---

# Current active boundary

Primary route:

```text
docs/checkpoints/234_user_curated_current_process_focus_set_review_opened.md
docs/research/063_user_curated_current_process_focus_membership.md
docs/research/062_current_process_focus_lens_and_context_suppression_experiment.md
frontend/design-lab/work-unit-process-focus.html
frontend/design-lab/work-unit-process-focus.css
frontend/design-lab/work-unit-process-focus.js
```

Current local URL:

```text
http://localhost:5173/design-lab/work-unit-process-focus.html
```

Exact current browser implementation target:

```text
da115b74de526fca05ed6f468bef39bdb801355c
```

---

# Held Cockpit controls

```text
G4 Adaptive Hybrid                  SELECTED / provisionally settled
Dark mode                           CURRENT design baseline
H4 generic hover/world response     SELECTED / sufficiently settled
Reduced in-box resting light        SELECTED preferred working baseline
```

Current work-unit category marker mapping:

```text
Question / Blocker        circle
Investigation             square
Validation / Analysis     triangle
Model Work                diamond
Evaluation                plus
```

Foundation 023 preserves:

```text
ADS owns semantic meaning
+
user controls approved non-semantic work-unit appearance dimensions
```

Current proven appearance dimensions:

```text
Box shape       Normal / Subtle shapes
Micro design    None / Micro material / Micro light
```

Foundation 024 preserves connector treatment, hover/focus behavior and semantic directionality as separate dimensions.

Current connector treatments:

```text
Clean
Micro dots
Frame sockets
Direction arrows
```

Accepted direction grammar:

```text
D0  Undirected      no arrow
D1  Forward         arrow at B
D2  Reverse         same arrow at A
D3  Bidirectional   same arrow at both endpoints
```

Accepted directionality implementation:

```text
07d573b6569b9f09a3b7e00936f3eadecee721b3
```

Relation-class visual carrier remains:

```text
E5  Hue + Tag
    SELECTED / sufficiently settled for current Phase C
```

Latest accepted relation-class implementation:

```text
497e81f06ba1f9901511449237d1bb9f96b2d108
```

Stroke rhythm remains preserved for a different future line-level semantic dimension and has no semantic assignment yet.

---

# Project-disposition result

The practical mixed-category review showed that persistent disposition coloring competes with category identity.

Human-selected direction:

```text
P7  Neutral Tag + Tone

REST
    category color remains dominant
    disposition tag visible but neutral
    Completed / Deferred / Future retain selective tonal recession

HOVER
    disposition tag reveals its state-specific color
    normal H4 hover behavior remains
```

The project owner accepted this practical result as the current project-disposition visual direction for Phase C.

The final project-disposition ontology remains unfrozen.

Primary evidence:

```text
docs/research/059_work_unit_project_disposition_visual_grammar_experiment.md
docs/research/060_disposition_hybrid_refinement_and_mixed_category_practical_comparison.md
docs/research/061_project_disposition_neutral_tag_tone_convergence_refinement.md
frontend/design-lab/work-unit-disposition-grammar.html
```

Latest accepted P7 implementation before the focus-lens slice:

```text
fac1db37af4225927d6c799e37418a3ad9c42c13
```

P4 State Rhythm remains preserved as standalone visual evidence and is not part of P7.

---

# Active Slice 02G: current-process focus lens and editable focus set

The current design requirement is separate from project disposition.

Binding semantic separation:

```text
WORK-UNIT EXISTENCE
    whether the work unit exists in the project

PROJECT DISPOSITION
    where the work unit stands in the project

CURRENT-FOCUS MEMBERSHIP
    whether the work unit belongs to the process set emphasized by the current focus lens

VIEW EMPHASIS
    how strongly work outside the current focus is visually suppressed
```

The focus set is not inferred from disposition in this browser. The fixture begins with an example focus set, but the user can edit it directly.

Initial example membership:

```text
IN CURRENT FOCUS
    Question / Blocker      BLOCKED
    Investigation           ACTIVE
    Validation / Analysis   NEXT

OUTSIDE CURRENT FOCUS
    Model Work              DONE
    Evaluation              DEFER
    Investigation           FUTURE
```

Available lens modes:

```text
Context visible
    accepted P7 treatment remains readable for all work

Focus current process
    current-focus nodes remain full salience
    work outside the focus set becomes dramatically quieter
    connector segments involving outside-focus work also recede
    suppressed nodes partially recover on hover
```

## User-curated membership

The browser now also exposes:

```text
Edit focus set
Reset example
```

When edit mode is active, each work unit exposes a compact membership control:

```text
+ FOCUS
    add this work unit to the current focus set

- FOCUS
    remove this work unit from the current focus set
```

This explicitly does not delete the work unit and does not modify its disposition.

Membership changes immediately update:

```text
node focus membership
focus membership count
strong suppression behavior
connector current/context classification
```

If either endpoint of a connector lies outside the focus set, that connector is treated as contextual for the focus lens.

While Edit focus set is active, strongly suppressed context is temporarily raised to a more operable salience so controls remain usable. Leaving edit mode restores the stronger suppression.

The design-lab browser uses `localStorage` only as prototype convenience so the edited focus set survives a refresh. Production persistence semantics remain open.

Current human review questions:

```text
Is Edit focus set clear and unobtrusive?
Do + FOCUS / - FOCUS clearly mean focus membership rather than deletion?
Does Focus current process update immediately when membership changes?
Do connector segments follow the edited focus set correctly?
Is temporary edit-mode recovery strong enough for comfortable editing without losing hierarchy?
Should production focus membership be project-level, view-specific, user-specific, system-suggested with overrides, or some combination?
```

---

# MC-0004 collaboration state

```text
Phase A  Claude independent proposal  cd2e12f2c79ee3b2f205457c5940eb2022b4631a  BLIND_TO_CANDIDATE
Phase B  Claude comparative review    d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce  COMPARATIVE_ONLY
Phase C  browser-rendered design evaluation
Latest Claude contribution            faf18ed9932d60a24dd80589b0ec0ba71c5940fd
Current                               user-curated current-process focus-set human review
```

There is no pending Claude obligation.

C5 Internal Layout Grammar remains deferred to semantic zoom / information-density work.

---

# Important non-decisions

Still unresolved:

```text
final current-focus membership semantics
whether system reasoning can suggest focus membership and how human overrides interact
whether multiple named focus sets / lenses exist
production ownership and persistence of focus sets
whether focus suppression supports more than the current binary lens
final project-disposition ontology
runtime / queued / waiting / failed / waiting-for-human visual grammar
importance / priority / relevance visual grammar
final semantic relation taxonomy
production relation colors / labels
semantic zoom behavior for relation tags
large-project label-density management
semantic assignment of connector stroke rhythm
runtime-flow connector behavior
selected/focused persistent treatment
production appearance persistence
final work-unit taxonomy
final node dimensions and typography
semantic zoom
C5 Internal Layout Grammar
2.5D focus/depth system
Conversation Workspace composition
large-project layout/grouping/command architecture
final production design system
```

Only isolated `frontend/design-lab/**` artifacts are authorized for the current experiment. Production `/cockpit` remains the control baseline.

---

# Source Universe deployment

```text
source-vault bootstrap
    PAUSED
    not cancelled
    not rejected
    not superseded
```

Course 2 remains blocked until the permanent recovery-integrity gate succeeds.

---

## Exact continuation

```text
1. use Checkpoint 234 and v1-cockpit-design-exploration
2. pull the latest branch locally
3. open http://localhost:5173/design-lab/work-unit-process-focus.html
4. switch Edit focus set on
5. add and remove several work units with + FOCUS / - FOCUS
6. switch between Context visible and Focus current process
7. verify connector suppression follows the edited focus set
8. verify edit-mode recovery keeps contextual nodes operable
9. verify refresh preserves the prototype focus set and Reset example restores the fixture
10. record prefer / reject / refine evidence
11. keep production Cockpit untouched
12. keep source-vault deployment paused until explicitly resumed
```
