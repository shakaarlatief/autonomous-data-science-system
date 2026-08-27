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

## Work-unit grammar result

Rejected or retired:

```text
bare Q / I / V / M / E letters
G2 Compact Marker Rail
S3 Inner Instrument Architecture
G1 Instrument Glyph comparator after scientific-marker selection
```

Positive mechanisms:

```text
scientific markers
Reduced in-box light
M1 micro-material family
Evaluation-like micro-light character
subtle true-shape family
```

Foundation 023 promotes the durable split between semantic work-unit meaning and approved user-configurable appearance.

## Connector / Port Grammar history

The generic connector browser tested:

```text
K0  Clean Curve
K1  Micro Dots
K2  Frame Sockets
K3  Target Cue
K4  Hover Ports
```

Important refinements:

```text
rendered-edge relation geometry
curve under node / endpoint overlay above node where appropriate
K2 sockets restored to frame-integrated treatment
hover geometry follows H4 node lift / release
K1/K4 dots moved mostly outside the perimeter
K2 active socket outline / glow adopts relation color
```

Exact retained refinement commits:

```text
42ec63d17095753dc4ab97628cd859473cbdf5e8
183264bdd07783eaa2354894592f2cf4a076b6ec
```

## Connector treatment and hover architecture

Human review first rejected the need for one universal connector-style winner, then clarified the composition model further.

Current connector treatments:

```text
Clean
Micro dots
Frame sockets
Direction arrows
```

Current interaction rule:

```text
one terminal treatment normally active at a time
+
hover / focus is an orthogonal reveal or emphasis mechanism
```

Therefore hover is not another connector terminal that must be combined with dots, sockets or arrows.

Unnecessary mixed terminal stacks are not the default product direction:

```text
arrow + dot
arrow + socket
socket + dot
```

Foundation 024 now records this refined architecture while preserving system-owned relation semantics.

## Current Slice 02D: simplified connector directionality

The first directionality browser exposed Clean / Micro dots / Frame sockets alongside persistent direction cues as compatibility controls.

The project owner then clarified that this made the directionality question more complicated than necessary.

The browser now isolates the original preferred edge-connected K3-style arrow only.

Research:

```text
docs/research/056_directionality_arrow_grammar_and_hover_separation_refinement.md
```

Checkpoint:

```text
docs/checkpoints/227_directionality_arrow_grammar_simplified_human_review_opened.md
```

Browser route:

```text
frontend/design-lab/connector-directionality.html
frontend/design-lab/connector-directionality.css
frontend/design-lab/connector-directionality.js
```

Local URL:

```text
http://localhost:5173/design-lab/connector-directionality.html
```

Exact browser implementation target:

```text
07d573b6569b9f09a3b7e00936f3eadecee721b3
```

Direction states:

```text
D0  Undirected      A - B
    no arrow

D1  Forward         A -> B
    arrow tip docked directly to B

D2  Reverse         A <- B
    exact same arrow tip docked directly to A

D3  Bidirectional   A <-> B
    same arrow at both endpoints
```

Arrow geometry intentionally reuses the earlier K3 treatment:

```text
arrow tip
    exact rendered work-unit edge

arrow arms
    outside the box
```

The connector curve remains beneath work-unit bodies and follows H4 hover lift / release through rendered-edge geometry updates.

## Dependency-bound ideas

```text
C4 Port Grammar
    matured into connector-treatment / hover / directionality architecture

C5 Internal Layout Grammar
    remains deferred to semantic zoom / information-density slice
```

## Current gate

```text
human verifies D0-D3 simplified arrow grammar
-> if accepted, treat directionality as sufficiently converged
-> then explore semantic relation classes
```

## Production boundary

Production `/cockpit` remains untouched. No graph/canvas dependency, final semantic relation taxonomy, production appearance persistence, motion library or final visual-system freeze is authorized by this thread.
