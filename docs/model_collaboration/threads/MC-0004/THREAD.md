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

Detailed experiment evidence remains in the numbered research records and checkpoints. This thread preserves collaboration history, accepted/rejected design boundaries, exact refs and the current human gate.

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

Current scientific category mapping:

```text
Question / Blocker        circle / yellow
Investigation             square / green
Validation / Analysis     triangle / blue
Model Work                diamond / red
Evaluation                plus / purple
```

Foundation 023 preserves semantic meaning separately from approved user-configurable non-semantic appearance. Foundation 024 preserves connector treatment, hover/focus and semantic directionality as separate dimensions.

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

Changing focus membership does not delete work and does not change project disposition. Exact accepted editable-focus target:

```text
da115b74de526fca05ed6f468bef39bdb801355c
```

Final production ownership/persistence, automatic focus suggestions, multiple named lenses and exact membership semantics remain open.

## Preservation-method audit during Phase C

Research 064 audited repository-preservation health under rapid small visual iterations.

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

Deferred / Completed / Future
    normally no current runtime
```

Historical execution evidence remains separate from current runtime.

Exact corrected runtime-browser target:

```text
dfcb89c15a23486d3fb9b4947b6a1d7cf3ac8b95
```

## Checkpoint 237: runtime-carrier convergence

Human review found R1 Status Lamp and R5 Motion Signal perceptually too similar for live non-failure states.

Implementation verification established:

```text
R1
    status lamp only

R5
    same status lamp
    + low-salience motion ring
```

The technical difference was retained as negative design evidence because the perceptual differentiation was insufficient.

The project owner rejected simultaneous dot-plus-runtime-tag composition and proposed exactly one switchable runtime carrier per live-runtime node.

Accepted architecture:

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

The runtime-tag carrier underwent a focused motion refinement.

```text
rotating conic-gradient
    lively but exposed rotating/clipped inner geometry

short perimeter tracer
    clean but too literal / sparse

first T7
    thicker blurred dash
    still looked effectively like T5 Long Glide

second T7
    fixed-mask conic shade field
    initially static because typed custom property did not inherit

repaired T7
    inherits: true
    broad shade field visibly moves through stationary perimeter
```

The project owner accepted the repaired result.

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

Checkpoint 237 is closed as the current visual-carrier gate. Final runtime ontology, production default carrier, preference persistence and exact pacing remain unfrozen.

## Checkpoint 238: BLOCKED semantics and carrier refinement

The runtime correction exposed that `Blocked` may be orthogonal to project disposition.

Working separation:

```text
PROJECT DISPOSITION
    where does this work stand in the project?

PROGRESS CONSTRAINT
    can this work proceed?

RUNTIME
    if a meaningful current execution/work episode exists,
    what is happening in that episode?
```

The first browser compared dedicated BLOCKED treatments C0-C6 and deliberately contrasted:

```text
Current + Blocked + NONE
vs
Current + WAIT + unblocked
```

and:

```text
Question / Blocker category
vs
Blocked progress constraint
```

Exact first progress-constraint browser target:

```text
efd0d36ee4ccf4c5494220df54eb3e7f50995658
```

Research:

```text
docs/research/069_blocked_as_orthogonal_progress_constraint_visual_grammar_experiment.md
```

## Research 070: blocker cause, blocked effect and shared operational-status carrier

Human review then refined the model:

```text
BLOCKER
    cause / unresolved work or dependency preventing progress

BLOCKS
    relationship from blocker cause to affected work

BLOCKED
    current progress constraint on affected work

FAIL
    failed current execution attempt
```

A visible Question / Blocker can therefore be the cause-resolution work without itself being Blocked.

Example:

```text
[Resolve data contract]
Question / Blocker
CURRENT + HUMAN

        BLOCKS
           ↓

[Production missingness]
Investigation
CURRENT + BLOCKED
```

The visual carrier was simplified to one bottom-right operational-status presentation slot:

```text
live runtime state
or
BLOCKED progress constraint

shared visual carrier
    !=
merged ontology
```

Tag mode reuses T7 Soft Shade with explicit state text.

The final compact red mapping was explicitly selected by the project owner:

```text
BLOCKED
    red core dot
    sharper non-circular dynamic ring

FAIL
    red core dot
    smoother circular dynamic ring
```

Exact accepted shared BLOCKED/status visual target:

```text
88fd3c3cfe7a1eff4664afde06341b7b654c97f4
```

The project owner then responded:

```text
Perfect. Proceed.
```

Checkpoint 238 is therefore closed as the current BLOCKED visual gate. Final progress-constraint ontology, blocker taxonomy, many-to-many representation and state-transition rules remain unfrozen.

## Work-unit detail expansion idea preserved

During the same review the project owner proposed:

```text
compact map work unit
    -> expanded contextual/detail card
    -> full specialist workspace / deep focus
```

Specification 008 already promotes selection into full specialist/deep-work content. The intermediate expanded-card level remains deliberately deferred to semantic zoom, C5 Internal Layout Grammar, information-density and selected/focused-treatment work.

## Checkpoint 239: attention priority review

The next bounded node-level question is:

```text
ATTENTION PRIORITY
    among visible work, which work deserves more attention now?
```

This is explicitly separated from:

```text
category
project disposition
progress constraint
runtime / operational status
current-process focus membership
```

The experiment does not assume:

```text
priority == relevance
priority == scheduling order
priority == current-focus membership
priority == operational urgency
```

Controlled fixture:

```text
Investigation
CURRENT
RUN
HIGH attention
```

`HIGH` is a provisional binary test fixture rather than a frozen priority scale.

Candidate visual treatments:

```text
A0  Neutral Control
A1  Twin Tick
A2  Top Rail
A3  Signal Bars
A4  Side Bracket
A5  HIGH Tag
A6  Beacon
A7  Luminance Lift
A8  Rail + Tag
```

Browser:

```text
http://localhost:5173/design-lab/work-unit-attention-priority.html
```

Exact browser implementation target:

```text
767c66f76974d3c0a851de0dfa17c502817a4b12
```

Research:

```text
docs/research/071_work_unit_attention_priority_visual_grammar_experiment.md
```

Checkpoint:

```text
docs/checkpoints/239_shared_blocked_carrier_accepted_attention_priority_review_opened.md
```

Practical fixture:

```text
Question / Blocker    CURRENT + HUMAN      HIGH
Investigation         CURRENT + BLOCKED    HIGH
Validation            NEXT + NONE          normal
Model Work            CURRENT + FAIL       HIGH
Investigation         CURRENT + RUN        normal
Evaluation            DEFER + NONE         normal
```

The yellow Question / Blocker node deliberately tests whether the provisional warm attention tone remains distinct from category color.

## Dependency-bound ideas

```text
C4 Port Grammar
    matured into connector-treatment / hover / directionality architecture

C5 Internal Layout Grammar
    remains deferred to semantic zoom / information-density slice
```

## Current gate

```text
human compares A1-A8 against A0
human judges structural priority cues versus explicit HIGH text
human rejects treatments that resemble status, connector ports, focus or hover
human inspects mixed categories and especially yellow Question / Blocker
human prefers / rejects / combines / refines
-> do not freeze final priority / relevance / scheduling ontology yet
```

## Production boundary

Production `/cockpit` remains untouched. No graph/canvas dependency, final runtime-state ontology, production runtime/status-carrier default/persistence model, final project-disposition ontology, final progress-constraint ontology, final BLOCKS relation semantics, final attention-priority ontology, priority/relevance/scheduling relationship, priority provenance/override/persistence model, production priority carrier, execution-history interface, runtime-flow connector grammar, automatic focus-selection algorithm, final focus-set ownership/persistence model, work-unit inline expansion behavior, semantic zoom, C5 Internal Layout Grammar, motion library or final visual-system freeze is authorized by this thread.
