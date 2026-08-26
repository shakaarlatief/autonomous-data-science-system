# Current State

**Checkpoint:** 218  
**Date:** 2026-08-26  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration branch base:** `v1-frontend-spike` at Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at feature-promotion head `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C browser-rendered Project Cockpit design evaluation. G4 is provisionally settled as the grid/world direction. H4 Integrated Response rest/hover interaction lighting is sufficiently settled after final human approval. The first W1-W4 work-unit category/silhouette visual-grammar browser experiment is now implemented and awaiting human review. The permanent source-vault bootstrap remains deliberately paused.  
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
docs/checkpoints/218_work_unit_visual_grammar_browser_experiment_human_review_opened.md
docs/research/046_work_unit_category_and_silhouette_visual_grammar_experiment.md
frontend/design-lab/work-unit-grammar.html
frontend/design-lab/work-unit-grammar.css
frontend/design-lab/work-unit-grammar.js
```

Expected local URL:

```text
http://localhost:5173/design-lab/work-unit-grammar.html
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

---

# Active slice: work-unit category / silhouette visual grammar

Research 037 and Research 038 identified a shared current weakness: most meaningful work units still collapse into one generic rounded-card grammar, with category identity carried too heavily by text, icon and color.

Research 046 isolates:

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

The first browser comparison is now implemented:

```text
W1  Unified Precision Frame
W2  Edge-Signature Grammar
W3  Structural Silhouette Family
W4  Hybrid Semantic Instrument
```

Two comparison modes are available:

```text
Category strip
    isolates category recognition in a neutral comparison context

Project scene
    tests the same grammar inside realistic G4/H4 composition with connectors
```

Representative design-fixture categories:

```text
Question / Blocker
Investigation
Validation / Analysis
Model Work
Evaluation
```

These are not a frozen production taxonomy.

A Reduced motion control is included as a secondary accessibility check.

Current evidence status:

```text
research brief       complete for first round
browser implementation complete for first round
human browser review OPEN
production promotion not authorized
```

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
Phase C  browser-rendered design evaluation; current actor human
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
1. use Checkpoint 218 and v1-cockpit-design-exploration
2. pull the latest branch locally
3. keep the existing Vite dev server running
4. open http://localhost:5173/design-lab/work-unit-grammar.html
5. compare W1-W4 first in Category strip view
6. compare W1-W4 again in Project scene view
7. hover representative nodes to confirm the accepted H4 treatment still works visually
8. use Reduced motion only as a secondary accessibility check
9. report prefer/reject/combine/refine judgment
10. keep production Cockpit untouched until later integrated evidence warrants promotion
11. keep source-vault deployment paused until explicitly resumed
```
