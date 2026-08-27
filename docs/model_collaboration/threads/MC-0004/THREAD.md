# MC-0004: Next-Generation Project Cockpit Design Exploration

**Thread:** MC-0004  
**Status:** ACTIVE / PHASE C BROWSER DESIGN EVALUATION  
**Review mode:** `INDEPENDENT_THEN_COMPARATIVE`  
**Task owner:** ChatGPT  
**Target-state write owner:** ChatGPT  
**Claude role:** independent reviewer / counter-designer / researcher  
**Human project owner:** final arbiter of product-intent choices  
**Opened:** 2026-08-26

## Purpose

Run a broad next-generation Project Cockpit design exploration while preserving Specification 008 unless new evidence justifies revision. Phase C uses browser-rendered experiments, continuous human review, selective external references and selective cross-model contributions before production visual replacement is authorized.

## Collaboration history

```text
Phase A
    Claude independent proposal
    message 001
    commit cd2e12f2c79ee3b2f205457c5940eb2022b4631a
    BLIND_TO_CANDIDATE

Phase B
    Claude comparative review
    message 002
    commit d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce
    COMPARATIVE_ONLY

Phase C divergent work-unit ideation
    ChatGPT request message 003
    Claude response message 004
    commit faf18ed9932d60a24dd80589b0ec0ba71c5940fd
    COMPARATIVE_ONLY / DIVERGENT_IDEATION
```

No Claude action is currently pending.

## Held controls

```text
G4 Adaptive Hybrid
    SELECTED / provisionally settled

H4 generic hover/outward-world response
    SELECTED / sufficiently settled

Reduced in-box resting light
    SELECTED preferred working baseline
```

Current scientific category-marker mapping:

```text
Question / Blocker        circle
Investigation             square
Validation / Analysis     triangle
Model Work                diamond
Evaluation                plus
```

Foundation 023 promotes the durable split between semantic work-unit meaning and approved user-configurable appearance.

Foundation 024 preserves connector treatment, hover/focus and semantic directionality as separate dimensions.

## Connector and relation results

Current connector treatments:

```text
Clean
Micro dots
Frame sockets
Direction arrows
```

Accepted directionality:

```text
D0  Undirected      no arrow
D1  Forward         arrow at B
D2  Reverse         same arrow at A
D3  Bidirectional   same arrow at both endpoints
```

Exact accepted directionality target:

```text
07d573b6569b9f09a3b7e00936f3eadecee721b3
```

Relation-class visual encoding remains sufficiently settled:

```text
E5  Hue + Tag
```

Latest accepted relation-class target:

```text
497e81f06ba1f9901511449237d1bb9f96b2d108
```

Stroke rhythm remains preserved for a different future line-level semantic dimension and currently has no assigned meaning.

## Project-disposition result

Research 059 through 061 explored disposition hue, tags, tone, rhythm and mixed-category interaction.

The project owner accepted:

```text
P7  Neutral Tag + Tone

REST
    category hue remains the dominant persistent color
    explicit disposition tag remains neutral
    selective tonal recession remains for Completed / Deferred / Future

HOVER
    tag border/text reveal the state-specific hue
```

Latest accepted P7 implementation:

```text
fac1db37af4225927d6c799e37418a3ad9c42c13
```

The final disposition ontology remains unfrozen.

## Current-process focus result

Research 062 separated project disposition, current-process membership and view emphasis.

The browser introduced:

```text
Context visible
    wider project remains readable

Focus current process
    current-focus work remains full salience
    outside-focus work is strongly suppressed
    contextual connector segments recede
    contextual nodes partially recover on hover
```

The project owner accepted this mechanism and then requested direct user control over membership.

Research 063 added:

```text
Edit focus set
Reset example
+ FOCUS
- FOCUS
```

Changing focus membership does not delete work and does not change project disposition. Membership changes immediately update node suppression and connector classification.

The project owner reviewed the editable result and concluded:

```text
It is perfect.
```

Exact accepted editable-focus target:

```text
da115b74de526fca05ed6f468bef39bdb801355c
```

Final production ownership/persistence, automatic focus suggestions, multiple named lenses and exact membership semantics remain open.

## Preservation-method audit during Phase C

After accepting editable focus membership, the project owner asked for an explicit audit of whether the repository-preservation architecture remained healthy under many rapid small changes.

Research:

```text
docs/research/064_rapid_iteration_repository_preservation_audit_and_checkpoint_hygiene.md
```

The architecture was judged sound, but the audit found Checkpoints 223-234 had drifted from the provider-neutral metadata contract.

Repair:

```text
required metadata/provenance backfilled
substantive historical bodies preserved
```

Verified global metadata validation after repair:

```text
d2541418a68b9bfd244ec89e4e951e630b3bb61b
    validate  SUCCESS
```

The checkpoint contract now makes two operating rules explicit:

```text
micro-refinements inside an already-open gate normally remain in Git + research evidence
+
a checkpoint is not operationally closed until its metadata validation succeeds
```

Current-routing consistency was also widened to all pushes that touch guarded routing surfaces.

This is bounded method hardening based on observed failure, not a new preservation architecture.

## Active Slice 02H: work-unit runtime state

The next semantic axis is:

```text
WHAT IS HAPPENING NOW?
    runtime / execution state
```

It remains separate from category, project disposition, priority/relevance and current-focus membership.

Research:

```text
docs/research/065_work_unit_runtime_state_visual_grammar_experiment.md
```

Checkpoint:

```text
docs/checkpoints/235_editable_focus_accepted_preservation_audit_closed_runtime_review_opened.md
```

Browser route:

```text
frontend/design-lab/work-unit-runtime-grammar.html
frontend/design-lab/work-unit-runtime-grammar.css
frontend/design-lab/work-unit-runtime-grammar.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-runtime-grammar.html
```

Exact browser implementation target:

```text
099e516bf9a7351a756bee00037edbcc731a2738
```

Provisional runtime fixtures:

```text
Idle
Queued
Running
Waiting
Waiting for Human
Failed
```

Encoding families:

```text
R0  Neutral Control
R1  Status Lamp
R2  Activity Rail
R3  Runtime Tag
R4  Instrument Cell
R5  Motion Signal
R6  Restrained Hybrid
```

The browser contains controlled same-category rows plus a mixed-category practical scene with P7 neutral disposition tags retained.

Reduced-motion mode removes runtime animation while preserving static runtime-state identity.

The saved connector stroke-rhythm channel remains unassigned and available for a future line-level semantic slice.

## Dependency-bound ideas

```text
C4 Port Grammar
    matured into connector-treatment / hover / directionality architecture

C5 Internal Layout Grammar
    remains deferred to semantic zoom / information-density slice
```

## Current gate

```text
human compares R0-R6
human inspects controlled rows and mixed-category scene
human compares normal vs Reduced motion
human judges runtime clarity, clutter and semantic competition
human judges whether motion reads as semantic rather than decorative
-> prefer / reject / combine / refine
-> do not freeze the final runtime ontology yet
```

Priority/importance visual grammar remains a separate future slice.

## Production boundary

Production `/cockpit` remains untouched. No graph/canvas dependency, final runtime-state ontology, runtime-flow connector grammar, automatic focus-selection algorithm, final focus-set ownership/persistence model, final project-disposition ontology, importance grammar, production appearance persistence, motion library or final visual-system freeze is authorized by this thread.
