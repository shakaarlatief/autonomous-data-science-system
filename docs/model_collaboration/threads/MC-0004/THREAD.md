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

### Work-unit category / silhouette grammar

Governing research:

```text
docs/research/046_work_unit_category_and_silhouette_visual_grammar_experiment.md
docs/research/047_work_unit_grammar_h4_control_correction_and_inbox_light_comparison.md
```

First browser candidates:

```text
W1  Unified Precision Frame
W2  Edge-Signature Grammar
W3  Structural Silhouette Family
W4  Hybrid Semantic Instrument
```

The first implementation received a strongly positive preliminary human reaction, but the human project owner judged the candidate space too narrow for convergence.

Human browser review exposed control/implementation problems before Claude should inspect the design:

```text
Project Scene and Category strip could render together
accepted H4 in-box resting light was accidentally suppressed by the grammar DOM
resting light stayed left-biased even when signature bars moved to top/bottom/right
partial top/bottom signatures still produced edge-centered light after the first side-aware correction
```

These were corrected before the Claude task was triggered.

The corrected browser experiment exposes an intentional secondary comparison:

```text
In-box light
    H4 baseline   default restored control
    Reduced       intentional lower-light alternative
```

The outward resting spill and generic H4 hover response remain held.

Signature-anchored resting light now follows:

```text
signature edge
+
signature position along that edge
```

Thus a left-biased top signature produces top-left-biased resting light rather than top-centered light. W3 has no explicit signature bar and retains the accepted left-biased H4 baseline for now.

Current corrected exact experiment target:

```text
304db34d6482320b317db97277148bc129d07372
```

## Current gate: human verification, then Claude divergent work-unit grammar ideation

Before Claude is triggered, the human project owner should verify the corrected browser rendering:

```text
Project Scene switches cleanly
H4 baseline restores the intended in-box light
Reduced is visibly quieter and intentional
W2/W4 top/bottom/right signatures move their resting light accordingly
partial top/bottom signature light aligns to the actual bar position rather than edge center
hover remains the accepted H4 behavior
```

After that verification, the human request is to obtain additional Claude ideas and inspiration before selecting or combining the current W1-W4 directions.

Detailed request:

```text
docs/model_collaboration/threads/MC-0004/messages/003_chatgpt_work_unit_grammar_divergent_ideation_request.md
```

Classification:

```text
COMPARATIVE_ONLY / DIVERGENT_IDEATION
```

Expected Claude output:

```text
docs/model_collaboration/threads/MC-0004/messages/004_claude_work_unit_grammar_divergent_ideation.md
```

Claude is asked to broaden the design space rather than merely rank W1-W4.

There is no artificial candidate-count cap. Preserve all genuinely distinct and worthwhile candidates. Browser testing may be organized into multiple batches if needed, but batching is not rejection.

Claude write scope remains:

```text
docs/model_collaboration/threads/MC-0004/messages/**
```

ChatGPT retains target-state write ownership.

## Scope discipline

The active work-unit grammar question is primarily:

```text
WHAT IS THIS WORK UNIT?
```

Keep it distinct from:

```text
project disposition
runtime state
importance / recommendation strength
```

The H4 baseline-vs-Reduced in-box-light control is an explicit secondary comparison, not a redefinition of category semantics.

Do not silently solve connector semantics, semantic zoom or the whole Cockpit in this slice.

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
1. human verifies the corrected browser experiment on v1-cockpit-design-exploration
2. after verification, Claude reads Message 003
3. Claude evaluates exact target 304db34d6482320b317db97277148bc129d07372
4. Claude writes only Message 004
5. ChatGPT synthesizes all genuinely worthwhile new/combined ideas
6. build as many browser variants as evidence justifies, organized into batches if useful
7. return to human comparison before selection
```

Machine-readable authoritative coordination state is in `STATE.json`; pending routing is also visible in `docs/model_collaboration/REVIEW_INBOX.md`.
