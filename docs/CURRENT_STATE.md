# Current State

**Checkpoint:** 236  
**Date:** 2026-08-27  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration branch base:** `v1-frontend-spike` at Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C browser-rendered Project Cockpit design evaluation. P7 Neutral Tag + Tone, the stronger current-process focus lens and user-curated focus membership remain accepted current design directions. Human review of the first runtime-state fixture exposed a semantic correction: runtime is conditional on a meaningful current execution/work episode rather than universally populated on every work unit. The active product-design gate now reviews R1-R6 against that corrected model.  
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
docs/checkpoints/236_runtime_state_made_conditional_human_review_reopened.md
docs/research/066_conditional_runtime_state_and_project_disposition_semantic_correction.md
docs/research/065_work_unit_runtime_state_visual_grammar_experiment.md
frontend/design-lab/work-unit-runtime-grammar.html
frontend/design-lab/work-unit-runtime-grammar.css
frontend/design-lab/work-unit-runtime-grammar.js
```

Current local URL:

```text
http://localhost:5173/design-lab/work-unit-runtime-grammar.html
```

Exact current browser implementation target:

```text
dfcb89c15a23486d3fb9b4947b6a1d7cf3ac8b95
```

---

# Repository preservation health

The rapid-iteration preservation audit remains closed.

Result:

```text
repository preservation architecture   SOUND
structural overhaul                     NOT WARRANTED
new knowledge subsystem                 NOT JUSTIFIED
checkpoint metadata drift               FOUND AND REPAIRED
checkpoint granularity                  HARDENED
checkpoint validation closure           HARDENED
active-branch routing validation        HARDENED
```

Concrete repair:

```text
Checkpoints 223-234
    mandatory metadata / provider-neutral provenance repaired
    substantive historical bodies unchanged
```

Verified global checkpoint-metadata validation after repair:

```text
d2541418a68b9bfd244ec89e4e951e630b3bb61b
    Checkpoint metadata / validate
    SUCCESS
```

The current checkpoint contract keeps micro-refinements inside an already-open gate in Git plus the active research record, while requiring a new checkpoint when the semantic/review/routing boundary changes. A checkpoint-producing change is not operationally closed until metadata validation succeeds.

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

Human-selected current Phase-C direction:

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

Latest accepted P7 implementation:

```text
fac1db37af4225927d6c799e37418a3ad9c42c13
```

The final project-disposition ontology remains unfrozen.

A semantic correction from Checkpoint 236 now applies to interpretation:

```text
Current
    project disposition / present working frontier

Running
    runtime / current execution episode
```

The earlier shorthand `Active / Current` should not be used in this runtime slice because `Active` can imply execution.

---

# Current-process focus result

The project owner accepted both the stronger focus lens and direct user editing of the focus set.

Accepted current direction:

```text
Context visible
    wider project remains readable

Focus current process
    current-focus work remains full salience
    work outside current focus is strongly suppressed
    contextual connector segments recede
    contextual nodes remain hover-recoverable

Edit focus set
    user can add a work unit to focus
    user can remove a work unit from focus
    changing focus membership does not delete the work unit
    changing focus membership does not change project disposition
```

Exact accepted editable-focus implementation target:

```text
da115b74de526fca05ed6f468bef39bdb801355c
```

Browser-local persistence remains prototype convenience only. Final production ownership, persistence, automatic focus suggestions and multiple named lenses remain open.

---

# Active Slice 02H: conditional work-unit runtime state

The binding semantic separation is now:

```text
CATEGORY
    what is this work unit?

PROJECT DISPOSITION
    where does it stand in the project?

RUNTIME
    if a meaningful current execution/work episode exists,
    what is happening in that episode?

PRIORITY / RELEVANCE
    how important is it now?

CURRENT-FOCUS MEMBERSHIP
    is it in the emphasized process set?
```

Runtime is conditional.

A work unit may exist and have a project disposition while having no current runtime at all.

Critical distinction:

```text
No runtime
    no current execution/work episode exists

Idle runtime
    an execution episode exists but is currently doing nothing
```

The current browser no longer uses Idle as the absence control. It uses:

```text
NONE    No runtime
QUEUE   Queued
RUN     Running
WAIT    Waiting
HUMAN   Waiting for Human
FAIL    Failed current attempt
```

Working compatibility interpretation:

```text
Current
    may have NONE / QUEUE / RUN / WAIT / HUMAN / FAIL

Recommended / Next
    normally NONE
    may be QUEUE if explicitly scheduled

Deferred
    normally NONE

Completed
    normally NONE

Future
    normally NONE
```

This is not a frozen state matrix.

Current runtime must also remain separate from historical execution provenance. A Deferred or Completed work unit may have prior failed/successful attempts without carrying that historical state as current runtime.

## Blocked remains unresolved

Checkpoint 236 also preserves a new ontology warning:

```text
Blocked
    may be an orthogonal progress constraint
    rather than a peer of Current / Next / Deferred / Completed / Future
```

Combinations such as `Current + Blocked` and `Next + Blocked` appear coherent. No final progress-constraint axis is promoted yet.

## Browser carrier families

The visual mechanisms remain:

```text
R0  Neutral Control
R1  Status Lamp
R2  Activity Rail
R3  Runtime Tag
R4  Instrument Cell
R5  Motion Signal
R6  Restrained Hybrid
```

The NONE row intentionally renders no runtime lamp, strip, badge, cell or motion ring under every R1-R6 encoding.

## Practical coexistence fixture

```text
Question        CURRENT + HUMAN
Investigation   CURRENT + RUN
Validation      NEXT + QUEUE
Model Work      CURRENT + FAIL
Evaluation      DEFER + NONE
Investigation   FUTURE + NONE
```

This tests optional runtime against real category/disposition coexistence instead of pretending that every box carries an execution process.

Semantic runtime motion must degrade to a static but still interpretable cue under Reduced motion. NONE must never animate.

The saved connector stroke-rhythm channel from Research 058 remains reserved for a future line-level semantic question and is not assigned by this node-level runtime experiment.

Current human gate:

```text
verify NONE looks like no runtime rather than an idle execution
compare R1-R6 on QUEUE / RUN / WAIT / HUMAN / FAIL
inspect mixed-category scene
inspect DEFER + NONE and FUTURE + NONE specifically
compare normal vs Reduced motion
judge runtime clarity
judge category/disposition competition
judge tag density
judge whether motion feels semantic rather than decorative
prefer / reject / combine / refine
```

---

# MC-0004 collaboration state

```text
Phase A  Claude independent proposal  cd2e12f2c79ee3b2f205457c5940eb2022b4631a  BLIND_TO_CANDIDATE
Phase B  Claude comparative review    d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce  COMPARATIVE_ONLY
Phase C  browser-rendered design evaluation
Latest Claude contribution            faf18ed9932d60a24dd80589b0ec0ba71c5940fd
Current                               conditional runtime-state visual-carrier human review
```

There is no pending Claude obligation.

C5 Internal Layout Grammar remains deferred to semantic zoom / information-density work.

---

# Important non-decisions

Still unresolved:

```text
final runtime / execution-state ontology
final runtime visual carrier
final project-disposition ontology
final Blocked / progress-constraint semantics
final compatibility matrix between disposition / constraints / runtime
historical execution-attempt presentation
runtime-flow connector behavior
final current-focus membership semantics
whether system reasoning can suggest focus membership and how human overrides interact
whether multiple named focus sets / lenses exist
production ownership and persistence of focus sets
importance / priority / relevance visual grammar
final semantic relation taxonomy
production relation colors / labels
semantic zoom behavior for relation tags
large-project label-density management
semantic assignment of connector stroke rhythm
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
1. use Checkpoint 236 and v1-cockpit-design-exploration
2. pull the latest branch locally
3. open http://localhost:5173/design-lab/work-unit-runtime-grammar.html
4. verify NONE has no runtime instrumentation under R1-R6
5. compare R1-R6 on the five live runtime states
6. inspect the mixed-category practical scene
7. inspect DEFER + NONE and FUTURE + NONE specifically
8. toggle Reduced motion and confirm runtime meaning remains legible
9. record prefer / reject / combine / refine evidence
10. do not freeze the final runtime/disposition/Blocked ontology merely from this visual slice
11. keep production Cockpit untouched
12. keep source-vault deployment paused until explicitly resumed
```