# MC-0004: Next-Generation Project Cockpit Design Exploration

**Thread:** MC-0004  
**Status:** ACTIVE / PHASE C BROWSER DESIGN EVALUATION  
**Review mode:** `INDEPENDENT_THEN_COMPARATIVE`  
**Task owner:** ChatGPT  
**Target-state write owner:** ChatGPT  
**Independent reviewer / counter-designer:** Claude  
**Human project owner:** final arbiter of product-intent choices  
**Opened:** 2026-08-26

## Purpose

Run a deliberately broad next-generation Project Cockpit design exploration while preserving the promoted Specification 008 interaction architecture unless new evidence justifies revising it.

The task uses research, independent counter-design, comparative synthesis, bounded browser-rendered design experiments and human product review before any production frontend replacement is authorized.

Generated-image UI concepts are not part of the preferred Phase-C evidence workflow.

## Independent Phase A

The neutral problem statement is:

```text
docs/model_collaboration/threads/MC-0004/BRIEF.md
```

The exact immutable neutral-brief commit for Phase A is:

```text
bedbd23f5aa5f35c79892ae633ccbc6da6ef7d88
```

Claude reasoned from that exact ref and accepted pre-proposal repository material before seeing Research 037 or later ChatGPT candidate-design material.

Claude's frozen Phase-A proposal is:

```text
docs/model_collaboration/threads/MC-0004/messages/001_claude_independent_phase_a_proposal.md
commit cd2e12f2c79ee3b2f205457c5940eb2022b4631a
```

The preserved Phase-A classification is:

```text
BLIND_TO_CANDIDATE
known candidate exposures: none
```

The earlier manual catch-up attempt that landed on an older repository branch exposed only stale collaboration/routing state, not Research 037 or other candidate design content, so the independent design evidence remains valid.

## Comparative Phase B

Phase B is complete.

Claude's comparative review is:

```text
docs/model_collaboration/threads/MC-0004/messages/002_claude_comparative_review.md
commit d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce
```

Classification:

```text
COMPARATIVE_ONLY
```

A direct comparison against the preceding branch head confirmed Claude changed only the declared collaboration-message file.

The comparative review identified:

```text
strong independently reached convergence on current implementation gaps
semantic zoom as the highest-confidence first mechanism
semantic connector type + direction + liveness
scarce event-driven motion
full Conversation Workspace
Research 037 improvements: external research, lenses, multi-axis state separation, persistence caution
Claude improvements: forensic code specificity, falsifiable motion cap, recommendation/reversal discipline
one genuine unresolved disagreement: command architecture at scale
scope-creep risk from broad technology prototyping
```

## ChatGPT comparative synthesis

The synthesis is frozen as:

```text
docs/research/038_mc0004_comparative_cockpit_design_synthesis_and_mockup_direction_set.md
```

It preserves three useful integrated design hypotheses:

```text
M1  Living Precision Canvas          preferred integrated anchor
M2  Spatial Control Room             strongest integrated alternative
M3  Depth-Aware Analytical Workbench bounded high-upside alternative
```

These remain hypotheses, not promoted visual identities.

## Phase C protocol

Phase C is active and is governed by:

```text
docs/research/039_phase_c_browser_rendered_design_experiment_protocol_and_grid_world_slice.md
```

The project owner chose to replace generated-image UI mockups with a stronger design-question-first process:

```text
real external references where useful
    +
small browser-rendered design experiments
    +
continuous human comparison
    ->
progressively integrated Cockpit prototype
```

A generated screenshot is not treated as a prototype.

The provisional slice sequence is:

```text
Slice 1   grid / spatial world substrate
Slice 2   work-unit visual grammar
Slice 3   connector semantics and static relation language
Slice 4   semantic zoom / level of detail
Slice 5   liveness / motion budget
Slice 6   Conversation Workspace presentation
Slice 7   selection, focus and bounded 2.5D depth
Slice 8   information lenses and command/navigation treatment
Slice 9   integrated Cockpit candidate
Slice 10  medium / large project pressure test
```

The ordering may change when mechanisms need to be evaluated together.

## Current Phase-C gate: grid/world substrate

The first executable design-lab experiment is:

```text
frontend/design-lab/grid-world.html
frontend/design-lab/grid-world.css
frontend/design-lab/grid-world-overrides.css
frontend/design-lab/grid-world.js
```

Variants:

```text
G1  Precision Lines
G2  Dot Matrix
G3  Cross Lattice
G4  Adaptive Hybrid
```

The experiment was rendered in Chromium. It loaded without JavaScript page errors and the four variants plus appearance/scale controls rendered successfully.

Browser inspection exposed a real defect in the first G3 Cross Lattice implementation, which appeared as heavy repeated bands. That defect was corrected before human review.

The current checkpoint is:

```text
docs/checkpoints/210_grid_world_design_lab_browser_verified_human_review_opened.md
```

The next expected actor is the human project owner.

Valid human dispositions include:

```text
PREFER
REJECT
COMBINE
REFINE
UNRESOLVED
```

The human does not have to select one whole variant. Mechanisms may be combined across variants.

## Target-state scope

ChatGPT owns mutation of the bounded research/routing/design-lab surfaces for this exploration:

```text
docs/research/037_project_cockpit_next_generation_visual_interaction_design_exploration_map.md
docs/research/038_mc0004_comparative_cockpit_design_synthesis_and_mockup_direction_set.md
docs/research/039_phase_c_browser_rendered_design_experiment_protocol_and_grid_world_slice.md
docs/checkpoints/206_source_vault_paused_cockpit_design_exploration_opened.md
docs/checkpoints/207_mc0004_phase_a_frozen_comparative_design_opened.md
docs/checkpoints/208_mc0004_comparative_synthesis_phase_c_mockups_opened.md
docs/checkpoints/209_phase_c_browser_design_lab_grid_world_opened.md
docs/checkpoints/210_grid_world_design_lab_browser_verified_human_review_opened.md
frontend/design-lab/**
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json
README.md
this thread contract/state
```

Claude's declared secondary collaboration surface remains:

```text
docs/model_collaboration/threads/MC-0004/messages/**
```

The production `/cockpit` implementation is not part of the current Phase-C write scope.

## Collaboration phases

```text
PHASE A  COMPLETE
    Claude independent design proposal
    BLIND_TO_CANDIDATE

PHASE B  COMPLETE
    Claude comparative review after candidate exposure was allowed
    COMPARATIVE_ONLY
    ChatGPT comparative synthesis preserved as Research 038

PHASE C  ACTIVE
    bounded browser-rendered design experiments
    continuous human product review
    current gate: G1-G4 grid/world substrate

PHASE D
    progressively integrated prototype and bounded technical mechanism spikes
    separate production implementation specification only after evidence warrants it
```

## Independence rule

The preserved Phase-A independence classification applies only to message 001.

Phase B and later are `COMPARATIVE_ONLY` because candidate exposure is intentionally allowed. This does not alter the historical Phase-A result.

## Authority rule

```text
accepted repository specifications / decisions
    >
this collaboration thread
    >
raw model proposals
```

MC-0004 does not promote a visual concept merely because both models prefer it. Promotion still requires normal ADS evaluation and preservation.

## Human arbitration

The human project owner should decide genuine product-intent questions such as desired visual character, acceptable level of dynamism, conversation ergonomics, and preference among otherwise defensible browser-rendered alternatives.

Routine implementation details, source gathering, technical comparison and evidence synthesis should not be escalated merely because two models could make different stylistic choices.

## Deliberately unresolved questions

```text
command architecture at scale
conversation persistence/threading model
exact visual identity
exact work-unit silhouettes
exact connector styling
exact semantic-zoom thresholds
lens names/count
stage taxonomy/layout
auto-layout approach
final graph/canvas library
final motion library
production 2.5D use
full 3D
```

## Technology boundary

The current grid/world experiment adds no frontend dependency and uses isolated HTML/CSS/JS.

No broad technology bakeoff is authorized during Phase C.

If later evidence earns technical comparison, current priority is:

```text
current DOM/CSS/SVG control baseline
React Flow semantic topology/zoom/grouping comparator
Motion for React focus/conversation transition comparator if needed
```

GPU layers and full 3D remain out of scope unless a specific later problem requires them.

## Closure condition

MC-0004 can close when:

```text
Claude independent design is preserved
Claude comparative review is preserved
ChatGPT comparative synthesis is preserved
material disagreement is explicit
browser-rendered design mechanisms have received sufficient human evaluation
human product direction is recorded where needed
next integrated-prototype / technical boundary is clear
```

Closure does not require the final production Cockpit visual system to be frozen.
