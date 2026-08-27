# Current State

**Checkpoint:** 233  
**Date:** 2026-08-27  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration branch base:** `v1-frontend-spike` at Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at feature-promotion head `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C browser-rendered Project Cockpit design evaluation. P7 Neutral Tag + Tone is accepted as the current project-disposition visual direction. The active gate is a new current-process focus-lens experiment that more strongly suppresses contextual work while keeping it available for inspection.  
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
docs/checkpoints/233_p7_disposition_accepted_current_process_focus_lens_review_opened.md
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
b311796f86ff577354a2bfe14b850bd6a49a9c06
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

Latest accepted P7 implementation before the new slice:

```text
fac1db37af4225927d6c799e37418a3ad9c42c13
```

P4 State Rhythm remains preserved as standalone visual evidence and is not part of P7.

---

# Active Slice 02G: current-process focus lens

The new design requirement is separate from project disposition.

Binding semantic separation:

```text
PROJECT DISPOSITION
    where a work unit stands in the project

CURRENT-PROCESS MEMBERSHIP
    whether a work unit belongs to the currently emphasized process path / horizon

VIEW EMPHASIS
    how strongly contextual work is visually suppressed in the current Cockpit lens
```

The browser deliberately does not infer current-process membership from disposition. The fixture assigns it explicitly for visual testing.

Representative fixture membership:

```text
CURRENT PROCESS
    Question / Blocker      BLOCKED
    Investigation           ACTIVE
    Validation / Analysis   NEXT

CONTEXT / NOT CURRENT
    Model Work              DONE
    Evaluation              DEFER
    Investigation           FUTURE
```

Available lens modes:

```text
Context visible
    accepted P7 treatment remains fully readable

Focus current process
    current-process nodes remain full salience
    contextual nodes become dramatically quieter
    contextual connector segments also recede
    contextual nodes partially recover on hover for inspection
```

The focus lens is presentation-only and does not mutate project semantics or delete nodes.

Current human review questions:

```text
Does the stronger suppression make the current process immediately dominant?
Is the suppression aesthetically coherent rather than looking disabled or broken?
Does hover recovery make context inspectable without equalizing salience?
Do context connector segments recede appropriately?
Should this remain a binary lens or later support additional user-adjustable levels?
```

---

# MC-0004 collaboration state

```text
Phase A  Claude independent proposal  cd2e12f2c79ee3b2f205457c5940eb2022b4631a  BLIND_TO_CANDIDATE
Phase B  Claude comparative review    d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce  COMPARATIVE_ONLY
Phase C  browser-rendered design evaluation
Latest Claude contribution            faf18ed9932d60a24dd80589b0ec0ba71c5940fd
Current                               current-process focus-lens human review
```

There is no pending Claude obligation.

C5 Internal Layout Grammar remains deferred to semantic zoom / information-density work.

---

# Important non-decisions

Still unresolved:

```text
final current-process-membership semantics
whether current-process focus is binary or supports additional levels
production persistence of focus-lens preference
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
1. use Checkpoint 233 and v1-cockpit-design-exploration
2. pull the latest branch locally
3. open http://localhost:5173/design-lab/work-unit-process-focus.html
4. compare Context visible vs Focus current process
5. hover the suppressed context nodes and inspect partial recovery
6. judge whether context connectors recede appropriately
7. refine / accept / reject the focus lens without changing disposition semantics
8. keep production Cockpit untouched
9. keep source-vault deployment paused until explicitly resumed
```
