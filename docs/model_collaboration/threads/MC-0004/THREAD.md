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

The current semantic separation remains:

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

Initial disposition research:

```text
docs/research/059_work_unit_project_disposition_visual_grammar_experiment.md
```

The first browser exposed:

```text
P0  Neutral Control
P1  Disposition Hue
P2  Explicit Tag
P3  Tonal Hierarchy
P4  State Rhythm
P5  Hue + Tag
P6  Restrained Hybrid
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

## Human refinement after first disposition review

The project owner requested:

```text
P6
    remove state rhythm

new candidate
    colored disposition tag + tone
    no disposition-colored perimeter

practical check
    show both candidates with multiple work-unit categories
    judge whether category and disposition become confusing together
```

The active convergence candidates are therefore:

```text
P6  Hue + Colored Tag + Tone
    disposition perimeter hue
    colored tag
    selective tone
    no rhythm

P7  Colored Tag + Tone
    no disposition perimeter hue
    colored tag
    same selective tone
    no rhythm
```

P4 State Rhythm remains preserved as standalone experiment evidence.

## Practical mixed-category comparison

Research:

```text
docs/research/060_disposition_hybrid_refinement_and_mixed_category_practical_comparison.md
```

Checkpoint:

```text
docs/checkpoints/231_disposition_hybrid_refined_mixed_category_comparison_opened.md
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
87927bef327be0a0cc9ccf9fb153aa0c7b226e92
```

The browser renders the same practical project fixture twice, once with P6 and once with P7, using multiple category identities:

```text
Question / Blocker
Investigation
Validation / Analysis
Model Work
Evaluation
```

and representative dispositions:

```text
Blocked
Active
Recommended
Completed
Deferred
Future
```

Neutral connectors are dynamically attached to rendered work-unit geometry. The connector geometry chooses horizontal or vertical attachment from actual card separation and follows H4 hover lift, preventing connector defects from contaminating the disposition comparison.

## Dependency-bound ideas

```text
C4 Port Grammar
    matured into connector-treatment / hover / directionality architecture

C5 Internal Layout Grammar
    remains deferred to semantic zoom / information-density slice
```

## Current gate

```text
human compares P6 vs P7 in controlled rows
+
human compares P6 vs P7 in practical mixed-category scenes
-> determine whether disposition perimeter hue adds clarity or category-color confusion
-> determine whether colored tag + tone alone is sufficiently clear
-> prefer / reject / combine / refine
-> do not freeze the final disposition ontology
```

Runtime-state and priority/importance visual grammars remain separate future slices.

## Production boundary

Production `/cockpit` remains untouched. No graph/canvas dependency, final project-disposition ontology, runtime-state grammar, importance grammar, production appearance persistence, motion library or final visual-system freeze is authorized by this thread.
