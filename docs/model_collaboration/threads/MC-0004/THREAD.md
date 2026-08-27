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

The final disposition ontology remains unfrozen. `Current` is the project-disposition concept; `Running` is reserved for runtime.

## Current-process focus result

Research 062 separated project disposition, current-process membership and view emphasis.

The project owner accepted:

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

Research 064 audited repository-preservation health under rapid small visual iterations.

Result:

```text
repository architecture        SOUND
structural overhaul            NOT WARRANTED
new knowledge subsystem        NOT JUSTIFIED
checkpoint metadata drift      FOUND AND REPAIRED
checkpoint granularity         HARDENED
validation closure             HARDENED
active-branch routing guard    HARDENED
```

Checkpoints 223-234 were repaired to the provider-neutral metadata contract without rewriting substantive historical conclusions.

Verified global metadata validation after repair:

```text
d2541418a68b9bfd244ec89e4e951e630b3bb61b
    validate  SUCCESS
```

Micro-refinements inside one review gate remain in Git plus active research evidence. A new checkpoint is warranted when the semantic/review/routing boundary changes.

## Slice 02H: runtime semantic correction

Research 065 initially compared:

```text
R0  Neutral Control
R1  Status Lamp
R2  Activity Rail
R3  Runtime Tag
R4  Instrument Cell
R5  Motion Signal
R6  Restrained Hybrid
```

Human review challenged the assumption that every project work unit always has a runtime state.

Checkpoint 236 corrected the model to:

```text
PROJECT DISPOSITION
    where does this work stand in the project?

RUNTIME
    if a meaningful current execution/work episode exists,
    what is happening in that episode?
```

Runtime is optional / episode-scoped.

```text
No runtime
    no current execution/work episode exists

Idle runtime
    a runtime episode exists but is currently doing nothing
```

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

This remains a working interpretation rather than a frozen compatibility matrix. Historical execution evidence is separate from current runtime.

Exact corrected runtime-browser target:

```text
dfcb89c15a23486d3fb9b4947b6a1d7cf3ac8b95
```

## Checkpoint 237: runtime-carrier convergence

Human review found that R1 Status Lamp and R5 Motion Signal looked effectively the same for the live non-failure states.

Implementation verification established:

```text
R1
    status lamp only

R5
    same status lamp
    + low-salience motion ring
```

The difference existed technically but not strongly enough perceptually. This remains negative design evidence.

The project owner also rejected simultaneous dot-plus-runtime-tag composition and proposed exactly one switchable runtime carrier per live-runtime node.

Accepted carrier architecture:

```text
Dot + dynamic ring
or
Runtime tag

GLOBAL
    change every live-runtime work unit together
    clear local overrides

LOCAL
    click the visible runtime carrier
    switch only that work unit

No runtime
    no runtime carrier
```

Initial switchable-carrier browser target:

```text
3a862c659e60e53832eaa5940ddb60d05734cd7d
```

## Research 068: runtime-tag motion convergence

The runtime-tag carrier then underwent a focused motion refinement.

Evidence sequence:

```text
rotating conic-gradient
    lively but visually exposed rotating/clipped inner geometry

short perimeter tracer
    geometrically clean but too literal / sparse

first T7
    thicker blurred dash
    still looked effectively like T5 Long Glide

second T7
    replaced travelling dash with fixed-mask conic shade field
    initially rendered static because the animated typed custom property did not inherit into pseudo-elements

repaired T7
    inherits: true
    broad shade field becomes visibly dynamic
```

After the repair, the project owner responded:

```text
Perfect. Proceed.
```

Accepted runtime-tag mechanism:

```text
T7 Soft Shade Flow
    stationary tag geometry
    stationary text
    stationary border mask
    broad soft shade field flows through perimeter
    no travelling dash as dominant read
    no rotating inner rectangle
```

Exact accepted T7 motion-browser target:

```text
08534f94c2f272f969159087de2797a23e36b330
```

Exact switchable-runtime browser with T7 integrated:

```text
fb847bd65ff6e5e4203a89ee2d4f74b7187c8359
```

Research:

```text
docs/research/067_switchable_runtime_carrier_convergence_and_r1_r5_verification.md
docs/research/068_runtime_tag_motion_clean_perimeter_alternatives.md
```

Checkpoint 237 is therefore closed as the current visual-carrier gate. The final runtime ontology, production default carrier, preference persistence and exact pacing remain unfrozen.

## Checkpoint 238: BLOCKED as progress constraint

The runtime semantic correction exposed that `Blocked` may be orthogonal to project disposition rather than a peer of Current / Next / Deferred / Completed / Future.

Working hypothesis:

```text
PROJECT DISPOSITION
    where does this work stand in the project?

PROGRESS CONSTRAINT
    can this work proceed?

RUNTIME
    if a meaningful current execution/work episode exists,
    what is happening in that episode?
```

This allows:

```text
Current + Blocked
Next + Blocked
```

without replacing the disposition value.

Two semantic contrasts are deliberately under direct review.

### Blocked versus WAIT runtime

```text
Blocked
    work cannot proceed until a constraint is resolved
    no live runtime episode is required

WAIT runtime
    a live work/execution episode exists
    that episode is presently waiting
```

The browser therefore includes:

```text
Current + Blocked + NONE
vs
Current + WAIT + unblocked
```

### Question / Blocker category versus Blocked constraint

```text
Question / Blocker
    work-unit category / kind

Blocked
    progress constraint on an affected work unit
```

A Question / Blocker work unit may itself be unblocked while resolving the condition that blocks another node.

Current visual candidates:

```text
C0  Neutral Control
C1  Explicit Tag
C2  Edge Clamp
C3  Stop Rail
C4  Barrier Seal
C5  Constraint Veil
C6  Tag + Clamp
```

Browser:

```text
http://localhost:5173/design-lab/work-unit-progress-constraint.html
```

Exact progress-constraint browser target:

```text
efd0d36ee4ccf4c5494220df54eb3e7f50995658
```

Research:

```text
docs/research/069_blocked_as_orthogonal_progress_constraint_visual_grammar_experiment.md
```

Checkpoint:

```text
docs/checkpoints/238_runtime_carrier_accepted_blocked_progress_constraint_review_opened.md
```

Practical fixture:

```text
Question / Blocker    CURRENT + HUMAN     unblocked
Investigation         CURRENT + BLOCKED   NONE
Validation            NEXT + BLOCKED      NONE
Model Work            CURRENT + RUN       unblocked
Investigation         CURRENT + WAIT      unblocked
Evaluation            DEFER + NONE        unblocked
Investigation         FUTURE + NONE       unblocked
```

## Dependency-bound ideas

```text
C4 Port Grammar
    matured into connector-treatment / hover / directionality architecture

C5 Internal Layout Grammar
    remains deferred to semantic zoom / information-density slice
```

## Current gate

```text
human judges whether Blocked belongs on an orthogonal progress-constraint axis
human verifies Question / Blocker category remains distinct from Blocked state
human verifies Current + Blocked + NONE remains distinct from Current + WAIT
human compares C1-C6 against C0
human judges explicit tag vs structural cue vs hybrid
human identifies treatments that resemble focus suppression / priority
-> prefer / reject / combine / refine
-> do not freeze final disposition / constraint / runtime ontology yet
```

Priority/importance visual grammar remains a separate future slice.

## Production boundary

Production `/cockpit` remains untouched. No graph/canvas dependency, final runtime-state ontology, production runtime-carrier default/persistence model, final project-disposition ontology, final progress-constraint ontology, final Blocked treatment, disposition/constraint/runtime compatibility matrix, blocker-cause navigation, execution-history interface, runtime-flow connector grammar, automatic focus-selection algorithm, final focus-set ownership/persistence model, importance grammar, production appearance persistence, motion library or final visual-system freeze is authorized by this thread.
