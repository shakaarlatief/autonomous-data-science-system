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

The project owner accepted the practical convergence direction:

```text
P7  Neutral Tag + Tone

REST
    category hue remains the dominant persistent color
    explicit disposition tag remains neutral
    selective tonal recession remains for Completed / Deferred / Future
    no disposition perimeter hue
    no rhythm

HOVER
    tag border/text reveal the state-specific hue
```

Latest accepted P7 implementation before the next slice:

```text
fac1db37af4225927d6c799e37418a3ad9c42c13
```

The final disposition ontology remains unfrozen.

P4 State Rhythm and the earlier colored alternatives remain preserved as experiment/history evidence.

## New human requirement: stronger contextual suppression

After accepting P7, the project owner identified a separate map-level need:

```text
keep future / contextual boxes in the Cockpit
+
provide a more dramatic suppression mode
+
make the actual current process remain visually dominant
```

This is not represented as another project-disposition state.

## Active Slice 02G: current-process focus lens

Binding separation:

```text
PROJECT DISPOSITION
    semantic state of the work unit

CURRENT-PROCESS MEMBERSHIP
    whether it belongs to the currently emphasized process path / horizon

VIEW EMPHASIS
    how strongly contextual work is visually suppressed in the current lens
```

Research:

```text
docs/research/062_current_process_focus_lens_and_context_suppression_experiment.md
```

Checkpoint:

```text
docs/checkpoints/233_p7_disposition_accepted_current_process_focus_lens_review_opened.md
```

Browser route:

```text
frontend/design-lab/work-unit-process-focus.html
frontend/design-lab/work-unit-process-focus.css
frontend/design-lab/work-unit-process-focus.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-process-focus.html
```

Exact browser implementation target:

```text
b311796f86ff577354a2bfe14b850bd6a49a9c06
```

The browser exposes:

```text
Context visible
    accepted P7 presentation remains readable

Focus current process
    current-process fixtures remain full salience
    contextual fixtures are strongly suppressed
    contextual connector segments recede
    contextual nodes partially recover on hover for inspection
```

Current-process membership is explicit fixture metadata and is not inferred from disposition.

## Dependency-bound ideas

```text
C4 Port Grammar
    matured into connector-treatment / hover / directionality architecture

C5 Internal Layout Grammar
    remains deferred to semantic zoom / information-density slice
```

## Current gate

```text
human compares Context visible vs Focus current process
-> judge strength and aesthetics of contextual suppression
-> judge partial hover recovery
-> judge contextual connector suppression
-> refine / accept / reject the focus lens
-> do not freeze final current-process-membership semantics
```

Runtime-state and priority/importance visual grammars remain separate future slices.

## Production boundary

Production `/cockpit` remains untouched. No graph/canvas dependency, final current-process-membership semantics, final project-disposition ontology, runtime-state grammar, importance grammar, production appearance persistence, motion library or final visual-system freeze is authorized by this thread.
