# Current State

**Checkpoint:** 217  
**Date:** 2026-08-26  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration branch base:** `v1-frontend-spike` at Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at feature-promotion head `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C browser-rendered Project Cockpit design evaluation. G4 is provisionally settled as the grid/world direction. H4 Integrated Response rest/hover interaction lighting is sufficiently settled after final human approval. The active design question is now work-unit category/silhouette visual grammar. The permanent source-vault bootstrap remains deliberately paused.  
**Latest specification:** Specification 024 remains accepted. Specification 008 remains the promoted V1 Project Cockpit interaction architecture.  
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no scientific comparison may be inferred from that run.

## Active interaction context

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-08
Conversation title       08 - Project Cockpit Design Exploration
Primary collaborator     ChatGPT
```

Previous ChatGPT conversation is `chatgpt-07 / 07 - Project Cockpit Design Exploration` and ended unexpectedly at the product context limit. Repository-only reconstruction succeeded because the substantive H4 correction had already been preserved.

Current Claude collaboration session remains `claude-01 / 01 - ADS Development Review & Collaboration`.
Repository artifacts remain authoritative across chats and models.

---

# Current active boundary

Primary route:

```text
docs/checkpoints/217_h4_interaction_lighting_settled_work_unit_visual_grammar_opened.md
docs/research/046_work_unit_category_and_silhouette_visual_grammar_experiment.md
```

Expected next design-lab surface:

```text
frontend/design-lab/work-unit-grammar.html
frontend/design-lab/work-unit-grammar.css
frontend/design-lab/work-unit-grammar.js
```

## Provisionally settled grid/world direction

```text
G4 Adaptive Hybrid                  SELECTED
Dark mode                           CURRENT design baseline
Light mode                          DEFERRED
Travelling grid currents            KEEP
Current distribution                RANDOMIZED across visible 20 px grid lines
Current cadence                     LIVELY preferred
Intersection glints                 KEEP
Glint location                      100 px MAJOR-GRID INTERSECTIONS ONLY
Glint cadence                       APPROXIMATELY QUIET / INDEPENDENT
Slow ambient light drift            KEEP
Localized semantic activity         KEEP
Fixed authored ambient coordinates  REJECTED
```

This layer is provisionally settled, not permanently frozen. Later integrated evidence may still justify adjustment.

Decorative/ambient visual behavior remains explicitly legitimate when it improves polish, atmosphere and product character while staying visually subordinate enough that it cannot be mistaken for semantic project/runtime state.

## Work-unit interaction lighting: sufficiently settled

Human review selected:

```text
H4 Integrated Response  SELECTED
```

Current retained treatment:

```text
REST
    accepted clean localized/asymmetric in-box illumination
    accepted narrow asymmetric outward world spill through the accent/left side
    no broad circular halo

HOVER
    full node-colored halo
    pointer-following hotspot
    local grid/world illumination
    immediate connector emphasis
    one restrained perimeter sweep on hover entry
    small depth lift
    fast entry + smoother slower release
```

Final human disposition:

```text
resting in-box illumination        ACCEPTED
outward left-side resting spill   ACCEPTED
broad circular resting halo       REJECTED
hover-entry timing                ACCEPTED
hover-release timing              ACCEPTED
```

No further generic lighting-only variant is currently justified.

Later selected/focused, running/waiting, blocked/approval and other semantic states may reuse or modify lighting, but those belong to their own integrated design slices.

Primary completed lighting evidence:

```text
docs/research/044_work_unit_interaction_lighting_hover_response_exploration.md
docs/research/045_h4_resting_node_light_world_spill_refinement.md
docs/checkpoints/215_grid_world_provisionally_settled_work_unit_lighting_review_opened.md
docs/checkpoints/216_h4_selected_resting_world_spill_human_review_opened.md
frontend/design-lab/work-unit-lighting.html
```

---

# Active slice: work-unit category / silhouette visual grammar

Research 037 and Research 038 identified a shared current weakness: most meaningful work units still collapse into one generic rounded-card grammar, with category identity carried too heavily by text, icon and color.

Research 046 now isolates:

```text
WHAT IS THIS?
    category / work-unit kind
```

from:

```text
project disposition
runtime state
importance / methodological priority
```

First-round browser directions:

```text
W1  Unified Precision Frame
W2  Edge-Signature Grammar
W3  Structural Silhouette Family
W4  Hybrid Semantic Instrument
```

The comparison should preserve G4 and H4 and use both a neutral category strip and a small realistic project scene.

Representative design-fixture categories:

```text
Question / Blocker
Investigation
Validation / Analysis work
Model work
Evaluation / Decision-relevant work
```

These are not a frozen production taxonomy.

---

# Important non-decisions

Still unresolved:

```text
final work-unit taxonomy
final work-unit silhouette/category grammar
final semantic colors and status palette
multi-axis project-disposition treatment
selected/focused persistent treatment
runtime / waiting / blocked / approval treatment
final node dimensions and typography
final semantic connector vocabulary
semantic zoom
2.5D focus/depth system
production motion implementation/library
Conversation Workspace composition
large-project layout/grouping/command architecture
final design system
```

Only isolated `frontend/design-lab/**` artifacts are authorized for the current experiment. The production `/cockpit` remains the control baseline.

---

# MC-0004 evidence

```text
Phase A  Claude independent proposal  cd2e12f2c79ee3b2f205457c5940eb2022b4631a  BLIND_TO_CANDIDATE
Phase B  Claude comparative review    d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce  COMPARATIVE_ONLY
Phase C  browser-rendered design evaluation; current actor human/ChatGPT
```

Generated-image UI concepts are not part of the preferred Cockpit evaluation workflow. Real browser-rendered experiments and real external references are preferred.

No pending Claude review obligation exists at the current boundary.

---

# Source Universe deployment

```text
source-vault bootstrap
    PAUSED
    not cancelled
    not rejected
    not superseded
    accepted architecture/runbook unchanged
```

Course 2 remains blocked until the permanent recovery-integrity gate succeeds.

---

## Exact continuation

```text
1. use Checkpoint 217 and v1-cockpit-design-exploration
2. preserve G4 as the provisionally settled world substrate
3. preserve H4 generic rest/hover interaction lighting as sufficiently settled
4. use Research 046 as the active design brief
5. build W1-W4 under frontend/design-lab/**
6. keep category separate from project disposition, runtime state and importance
7. expose a neutral category strip and one realistic project scene
8. let the project owner compare the browser-rendered variants
9. record prefer/reject/combine/refine evidence
10. keep production Cockpit untouched until later integrated evidence warrants promotion
11. keep source-vault deployment paused until explicitly resumed
```
