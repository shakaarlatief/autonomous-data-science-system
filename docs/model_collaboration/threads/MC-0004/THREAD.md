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

Checkpoint 236 refines wording: `Current` is the project-disposition concept; `Running` is reserved for runtime. The earlier `Active / Current` shorthand should not be treated as a final ontology label.

## Current-process focus result

Research 062 separated project disposition, current-process membership and view emphasis.

The project owner accepted both the stronger focus lens and direct focus-set editing:

```text
Context visible
Focus current process
Edit focus set
Reset example
+ FOCUS
- FOCUS
```

Changing focus membership does not delete work and does not change project disposition. Membership changes immediately update node suppression and connector classification.

Exact accepted editable-focus target:

```text
da115b74de526fca05ed6f468bef39bdb801355c
```

Final production ownership/persistence, automatic focus suggestions, multiple named lenses and exact membership semantics remain open.

## Preservation-method audit during Phase C

After accepting editable focus membership, the project owner requested an audit of repository-preservation health under many rapid small changes.

Research:

```text
docs/research/064_rapid_iteration_repository_preservation_audit_and_checkpoint_hygiene.md
```

The architecture was judged sound. Checkpoints 223-234 had drifted from the provider-neutral metadata contract, so required metadata/provenance was repaired without rewriting substantive historical conclusions.

Verified global metadata validation after repair:

```text
d2541418a68b9bfd244ec89e4e951e630b3bb61b
    validate  SUCCESS
```

The checkpoint contract now explicitly keeps micro-refinements inside an already-open gate in Git plus active research evidence, while requiring checkpoint validation before operational closure.

## Slice 02H initial runtime experiment

Research 065 opened a visual-carrier comparison for:

```text
WHAT IS HAPPENING NOW?
    runtime / execution state
```

Initial carrier families:

```text
R0  Neutral Control
R1  Status Lamp
R2  Activity Rail
R3  Runtime Tag
R4  Instrument Cell
R5  Motion Signal
R6  Restrained Hybrid
```

The first fixture implicitly treated runtime as though every work unit always had one of several states. Human review challenged that assumption before visual convergence.

## Checkpoint 236 semantic correction: runtime is conditional

The project owner asked why Deferred, Future or otherwise non-current work would have runtime/status at all.

That exposed a genuine semantic conflation.

The corrected model is:

```text
PROJECT DISPOSITION
    where does this work stand in the project?

RUNTIME
    if a meaningful current execution/work episode exists,
    what is happening in that episode?
```

Runtime is therefore optional / episode-scoped.

The key distinction is:

```text
No runtime
    no current execution/work episode exists

Idle runtime
    a runtime episode exists but is currently doing nothing
```

The browser uses `NONE / No runtime` as its absence control. `Idle` is no longer used to mean absence.

Working interpretation:

```text
Current
    may have no runtime
    may be Queued / Running / Waiting / Waiting for Human / Failed current attempt

Recommended / Next
    normally no runtime
    may be Queued if explicitly scheduled

Deferred
    normally no current runtime

Completed
    normally no current runtime

Future
    normally no current runtime
```

This is not a frozen compatibility matrix.

Historical execution evidence remains separate from current runtime. A Deferred, Completed or Future node may retain previous attempt records without showing those old attempts as its current runtime.

## Blocked remains explicitly unresolved

The same semantic review exposed that `Blocked` may be orthogonal to lifecycle/disposition.

Potentially coherent examples:

```text
Current + Blocked
Next + Blocked
```

A later model may distinguish:

```text
project disposition
progress constraint
runtime
```

but no such final ontology is frozen at this checkpoint.

## Corrected conditional-runtime browser

Research:

```text
docs/research/066_conditional_runtime_state_and_project_disposition_semantic_correction.md
```

Checkpoint:

```text
docs/checkpoints/236_runtime_state_made_conditional_human_review_reopened.md
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

Exact corrected browser implementation target:

```text
dfcb89c15a23486d3fb9b4947b6a1d7cf3ac8b95
```

Controlled rows hold Current Investigation constant and vary:

```text
NONE    No runtime
QUEUE   Queued
RUN     Running
WAIT    Waiting
HUMAN   Waiting for Human
FAIL    Failed current attempt
```

For NONE, all R1-R6 runtime instrumentation is intentionally absent.

Practical scene:

```text
Question        CURRENT + HUMAN
Investigation   CURRENT + RUN
Validation      NEXT + QUEUE
Model Work      CURRENT + FAIL
Evaluation      DEFER + NONE
Investigation   FUTURE + NONE
```

This tests optional runtime against category and P7 disposition rather than pretending every project box has a dormant runtime process.

Reduced-motion mode removes runtime animation while preserving static state identity. NONE never animates.

## Checkpoint 237 runtime-carrier convergence

Human review of the corrected R0-R6 browser produced two new pieces of evidence.

First, the project owner observed that:

```text
R1 Status Lamp
R5 Motion Signal
```

looked effectively the same for Queued, Running, Waiting and Waiting for Human, with Failed showing the distinction more clearly.

Direct implementation inspection verified:

```text
R1
    status lamp only

R5
    same status lamp
    + motion ring
```

Therefore the two families were not literally identical in code. However, the ring was too subtle and too spatially coincident with the lamp for R5 to read as a genuinely different family at working scale. Failed was more visibly different because the ring changed to a sharper rotated shape.

This is accepted as negative design evidence:

```text
technical difference exists
perceptual differentiation is insufficient
```

Second, the project owner rejected the simultaneous dot-plus-runtime-tag composition as the active direction and proposed exactly one switchable runtime carrier per live-runtime work unit.

Current convergence candidates:

```text
Dot + dynamic ring
Animated runtime tag
```

The dot carrier uses a stronger state-colored outer ring with state-sensitive motion pacing so it no longer collapses into a static lamp.

The tag carrier uses explicit runtime text plus a state-colored perimeter with a circulating bright trace. It intentionally does not use the dot's expanding/breathing motion.

Switching operates at two scopes:

```text
GLOBAL
    change every live-runtime work unit together
    clear local per-box overrides

LOCAL
    click the visible runtime carrier
    switch only that work unit
```

Clicking the replacement carrier switches that box back. A node matching the global carrier is no longer considered a local override.

No-runtime work units render:

```text
no dot
no ring
no runtime tag
no carrier-switch target
```

Current browser:

```text
http://localhost:5173/design-lab/work-unit-runtime-carrier-switch.html
```

Exact browser implementation target:

```text
3a862c659e60e53832eaa5940ddb60d05734cd7d
```

Research:

```text
docs/research/067_switchable_runtime_carrier_convergence_and_r1_r5_verification.md
```

Checkpoint:

```text
docs/checkpoints/237_switchable_runtime_carrier_convergence_review_opened.md
```

The practical scene retains:

```text
Question        CURRENT + HUMAN
Investigation   CURRENT + RUN
Validation      NEXT + QUEUE
Model Work      CURRENT + FAIL
Evaluation      DEFER + NONE
Investigation   FUTURE + NONE
```

so the human can test global switching, local overrides and mixed carrier coexistence while preserving conditional runtime.

Reduced motion freezes both carrier animations while preserving static runtime identity.

## Dependency-bound ideas

```text
C4 Port Grammar
    matured into connector-treatment / hover / directionality architecture

C5 Internal Layout Grammar
    remains deferred to semantic zoom / information-density slice
```

## Current gate

```text
human compares Dot + dynamic ring with Animated runtime tag
human verifies the strengthened ring is visibly dynamic
human verifies the animated tag perimeter is clean and distinct
human uses the global switch in both directions
human creates and removes local per-box overrides
human inspects a mixed practical scene
human verifies NONE / DEFER + NONE / FUTURE + NONE have no runtime carrier
human compares normal vs Reduced motion
-> prefer / reject / combine / refine
-> do not freeze the final runtime/disposition/Blocked ontology yet
```

Priority/importance visual grammar remains a separate future slice.

## Production boundary

Production `/cockpit` remains untouched. No graph/canvas dependency, final runtime-state ontology, final runtime carrier, production runtime-carrier default/persistence model, final project-disposition ontology, final Blocked/progress-constraint semantics, execution-history interface, runtime-flow connector grammar, automatic focus-selection algorithm, final focus-set ownership/persistence model, importance grammar, production appearance persistence, motion library or final visual-system freeze is authorized by this thread.
