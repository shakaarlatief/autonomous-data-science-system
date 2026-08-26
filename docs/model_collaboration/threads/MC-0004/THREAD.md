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

Run a broad next-generation Project Cockpit design exploration while preserving Specification 008 unless new evidence justifies revision. Phase C uses browser-rendered experiments, selective external references, continuous human review and selective cross-model contributions before any production visual replacement is authorized.

## Preserved collaboration history

```text
Phase A
    Claude independent proposal
    message 001
    commit cd2e12f2c79ee3b2f205457c5940eb2022b4631a
    classification BLIND_TO_CANDIDATE

Phase B
    Claude comparative review
    message 002
    commit d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce
    classification COMPARATIVE_ONLY

ChatGPT comparative synthesis
    docs/research/038_mc0004_comparative_cockpit_design_synthesis_and_mockup_direction_set.md
```

Historical Phase-A independence remains valid. All later Claude work is comparative because candidate exposure is allowed.

## Phase C method

Governing protocol:

```text
docs/research/039_phase_c_browser_rendered_design_experiment_protocol_and_grid_world_slice.md
```

Preferred loop:

```text
bounded design question
-> browser variants
-> human comparison
-> selective refinement / additional research / model contribution
-> integrate only surviving mechanisms
```

Generated-image UI concepts are not part of the preferred workflow.

## Phase C results so far

### Grid/world

```text
G4 Adaptive Hybrid  SELECTED / provisionally settled
```

Retained direction includes dark-first design, randomized grid currents, quiet major-grid glints, ambient drift and localized semantic activity. Decorative ambient behavior is allowed when it remains subordinate and cannot be mistaken for semantic state.

### Generic work-unit rest/hover lighting

```text
H4 Integrated Response  SELECTED / sufficiently settled
```

Accepted treatment includes clean asymmetric resting illumination, narrow outward resting spill, full hover halo, pointer hotspot, local world illumination, connector emphasis, one restrained perimeter sweep, small lift, fast entry and smoother release. The broad circular resting halo was rejected.

### First work-unit grammar round

Research:

```text
docs/research/046_work_unit_category_and_silhouette_visual_grammar_experiment.md
docs/research/047_work_unit_grammar_h4_control_correction_and_inbox_light_comparison.md
```

Candidates:

```text
W1  Unified Precision Frame
W2  Edge-Signature Grammar
W3  Structural Silhouette Family
W4  Hybrid Semantic Instrument
```

Human review judged the first implementation positively but the design space too narrow for convergence.

Before Claude was triggered, the browser target was corrected for:

```text
Project Scene overlap
accidental H4 in-box-light suppression
fixed-left lighting despite moved signature edges
edge-centered lighting despite partial top/bottom bars being left-biased
```

The corrected control now preserves:

```text
H4 baseline vs Reduced in-box light
signature edge + along-edge position -> resting-light origin
```

Corrected exact target reviewed by Claude:

```text
304db34d6482320b317db97277148bc129d07372
```

## Claude Phase-C divergent ideation: completed

Request:

```text
docs/model_collaboration/threads/MC-0004/messages/003_chatgpt_work_unit_grammar_divergent_ideation_request.md
```

Response:

```text
docs/model_collaboration/threads/MC-0004/messages/004_claude_work_unit_grammar_divergent_ideation.md
```

Claude response commit:

```text
faf18ed9932d60a24dd80589b0ec0ba71c5940fd
```

Classification:

```text
COMPARATIVE_ONLY / DIVERGENT_IDEATION
```

Claude proposed eight materially distinct concept families:

```text
C1  Instrument Glyph Family
C2  Structural Topology Family
C3  Material Language Family
C4  Port Grammar
C5  Internal Layout Grammar
C6  Aspect & Proportion Family
C7  Compact Marker Rail
C8  Scientific Marker Family
```

No artificial candidate-count cap was applied.

Claude also diagnosed that the first W1-W4 round underexplored:

```text
true non-text category marks
genuine topology change
surface material
inner layout
connector ports
richer signature vocabulary
```

## ChatGPT synthesis and expanded round

Synthesis:

```text
docs/research/048_claude_work_unit_grammar_synthesis_and_expanded_browser_round.md
```

ChatGPT preserved Claude's immediate candidates and added:

```text
C9 Inner Instrument Architecture
```

This isolates inner frame architecture without introducing live-looking category content.

Dependency-bound candidates remain preserved:

```text
C4 Port Grammar             -> connector-semantics slice
C5 Internal Layout Grammar  -> semantic zoom / information-density slice
```

New browser route:

```text
frontend/design-lab/work-unit-grammar-expanded.html
frontend/design-lab/work-unit-grammar-expanded.css
frontend/design-lab/work-unit-grammar-expanded.js
```

Exact implementation head before routing-only documentation:

```text
32883ada35506a713a7c780beca08f363ba29fab
```

Expanded candidate matrix:

```text
Batch A · Glyph strategy
    G0 Letter Control
    G1 Instrument Glyph Family
    G2 Compact Marker Rail
    G3 Scientific Marker Family

Batch B · Structural grammar
    S0 Chamfer Control
    S1 Structural Topology Family
    S2 Aspect & Proportion Family
    S3 Inner Instrument Architecture

Batch C · Material channel
    M0 Plain Surface Control
    M1 Material Language Family

Batch D · Integrated candidates
    I0 Current W4 Hybrid Control
    I1 W4 + Instrument Glyph
    I2 W4 + Scientific Marker
```

Total executable variants:

```text
13
```

Batching is presentation and causal organization only:

```text
batching != rejection
```

## Current gate: human expanded-browser review

Current local route:

```text
http://localhost:5173/design-lab/work-unit-grammar-expanded.html
```

Current controls:

```text
View
    Category strip
    Project scene

In-box light
    H4 baseline
    Reduced

Family filter
    All
    Glyph
    Structure
    Surface
    Integrated

Reduced motion
```

G4, accepted H4 hover behavior and position-aware resting light remain held.

The family filter only changes presentation. Hidden candidates remain active.

## Scope discipline

The active work-unit grammar question remains primarily:

```text
WHAT IS THIS WORK UNIT?
```

Keep it distinct from:

```text
project disposition
runtime state
importance / recommendation strength
```

The H4 baseline-vs-Reduced in-box-light control remains an explicit secondary comparison.

Do not silently solve connector semantics or semantic zoom inside this slice. C4 and C5 are preserved specifically for those dependency-aligned slices.

## Authority

```text
accepted specifications / decisions
>
current canonical project state
>
this collaboration thread
>
raw model proposals
```

Multi-model agreement does not itself promote a visual concept.

## Production boundary

No production `/cockpit` replacement, new graph/canvas dependency, new motion library or final visual-system freeze is authorized by this thread.

## Current continuation

```text
1. human reviews the expanded 13-variant browser round
2. human may prefer, reject, combine, refine or request additional candidates
3. ChatGPT records the human evidence
4. decide whether another work-unit grammar round is warranted
5. only later promote a grammar if integrated evidence supports it
```

Machine-readable authoritative coordination state is in `STATE.json`; `docs/model_collaboration/REVIEW_INBOX.md` currently shows no pending model obligation.
