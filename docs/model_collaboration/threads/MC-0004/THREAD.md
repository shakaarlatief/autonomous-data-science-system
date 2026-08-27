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

Relation-class visual encoding is sufficiently settled for the current Phase-C design phase:

```text
E5  Hue + Tag
```

Latest accepted relation-class target:

```text
497e81f06ba1f9901511449237d1bb9f96b2d108
```

Stroke rhythm remains preserved for a different future line-level semantic dimension and currently has no assigned meaning.

## Current Slice 02F: work-unit project disposition

The semantic separation remains:

```text
WHAT IS THIS?
    category / kind

WHAT IS ITS PROJECT DISPOSITION?
    current slice

WHAT IS HAPPENING NOW?
    runtime state, held out

HOW IMPORTANT IS IT NOW?
    priority / relevance, held out
```

Representative visual-test dispositions remain provisional:

```text
S0  Active / Current
S1  Recommended / Next
S2  Deferred
S3  Completed
S4  Blocked
S5  Future / Not yet active
```

Initial P0-P6 families and the mixed-category P6/P7 comparison remain preserved in Research 059 and 060.

## Latest human convergence evidence

The project owner reviewed the practical mixed-category scenes and found both persistent-color candidates somewhat confusing once category hue and disposition hue coexisted.

Human conclusion:

```text
best direction
    tag + tone

resting tag
    neutral / uncolored

hover
    tag reveals disposition color
```

The active convergence candidate is therefore:

```text
P7  Neutral Tag + Tone

REST
    category hue remains the dominant persistent color
    explicit disposition tag remains neutral
    selective tonal recession retained for Completed / Deferred / Future
    no disposition perimeter hue
    no rhythm

HOVER
    tag border/text reveal the state-specific hue
```

P4 State Rhythm and P6 Hue + Colored Tag + Tone remain preserved as experiment/history evidence.

## Current browser verification

Research:

```text
docs/research/061_project_disposition_neutral_tag_tone_convergence_refinement.md
```

Checkpoint:

```text
docs/checkpoints/232_disposition_neutral_tag_tone_refinement_review_opened.md
```

Browser route:

```text
frontend/design-lab/work-unit-disposition-grammar.html
frontend/design-lab/work-unit-disposition-grammar.css
frontend/design-lab/work-unit-disposition-grammar.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-disposition-grammar.html
```

Exact refined browser implementation target:

```text
fac1db37af4225927d6c799e37418a3ad9c42c13
```

The page opens directly in P7. The practical P7 scene keeps category color dominant at rest and reveals state hue only in the tag on hover.

## Dependency-bound ideas

```text
C4 Port Grammar
    matured into connector-treatment / hover / directionality architecture

C5 Internal Layout Grammar
    remains deferred to semantic zoom / information-density slice
```

## Current gate

```text
human verifies P7 neutral tag at rest
human verifies state hue appears only on hover
human verifies mixed-category scene is less confusing
human judges tonal recession separately from importance
-> if accepted, project-disposition visual carrier is sufficiently converged for current Phase C
-> final disposition ontology remains unfrozen
```

Runtime-state and priority/importance visual grammars remain separate future slices.

## Production boundary

Production `/cockpit` remains untouched. No graph/canvas dependency, final project-disposition ontology, runtime-state grammar, importance grammar, production appearance persistence, motion library or final visual-system freeze is authorized by this thread.
