# Current State

**Checkpoint:** 216  
**Date:** 2026-08-26  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration branch base:** `v1-frontend-spike` at Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at feature-promotion head `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C browser-rendered Project Cockpit design evaluation. G4 is provisionally settled as the grid/world direction. H4 Integrated Response is selected as the current work-unit interaction-lighting direction. The active question is the amount and shape of resting node-colored light projected into the surrounding grid. The permanent source-vault bootstrap remains deliberately paused.  
**Latest specification:** Specification 024 remains accepted. Specification 008 remains the promoted V1 Project Cockpit interaction architecture.  
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no scientific comparison may be inferred from that run.

## Active interaction context

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-07
Conversation title       07 - Project Cockpit Design Exploration
Primary collaborator     ChatGPT
```

Previous ChatGPT conversation remains `chatgpt-06 / 06 - Methodological Knowledge Universe Construction`.
Current Claude collaboration session remains `claude-01 / 01 - ADS Development Review & Collaboration`.
Repository artifacts remain authoritative across chats and models.

---

# Current active boundary

Primary route:

```text
docs/checkpoints/216_h4_selected_resting_world_spill_human_review_opened.md
docs/research/045_h4_resting_node_light_world_spill_refinement.md
frontend/design-lab/work-unit-lighting.html
frontend/design-lab/work-unit-lighting.css
frontend/design-lab/work-unit-lighting.js
```

Expected local URL:

```text
http://localhost:5173/design-lab/work-unit-lighting.html
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

## Selected work-unit lighting direction

Human review selected:

```text
H4 Integrated Response  SELECTED
```

Currently retained H4 mechanisms:

```text
REST
    localized/asymmetric node-colored light
    persistent but quiet illumination

HOVER
    full node-colored halo
    pointer-following hotspot
    local grid/world illumination
    immediate connector emphasis
    one restrained perimeter sweep on hover entry
    small depth lift
```

Representative node colors remain provisional and are not yet a final semantic palette.

## Current refinement: stronger resting world spill

The newer H4 node light was judged attractive inside the work-unit box, but too much of the resting light remained contained near the card compared with the earlier G4 treatment.

The desired synthesis is:

```text
keep the cleaner newer in-box illumination
+
project more of the same node color into the surrounding grid at rest
+
keep that resting spill asymmetric and soft
+
keep hover visibly richer than rest
```

The H4 experiment now uses two complementary resting layers:

```text
near-node rest light
    stronger around the semantic accent side
    preserves the newer close/in-box treatment

broader world bleed
    lower-opacity colored field extending farther into the grid
    strongest near the accent side
    visible without cursor interaction
```

Current review questions:

```text
Does H4 now project enough colored light into the grid at rest?
Does the node itself retain the cleaner newer illumination?
Is the resting spill soft enough to avoid a neon-card look?
Does hover remain clearly richer than rest?
```

---

# Important non-decisions

Still unresolved:

```text
final work-unit silhouette / category grammar
final semantic colors and status palette
selected-state lighting
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
1. use Checkpoint 216 and v1-cockpit-design-exploration
2. preserve the current G4 world provisionally
3. preserve H4 Integrated Response as selected interaction-lighting direction
4. pull latest branch locally
5. refresh http://localhost:5173/design-lab/work-unit-lighting.html
6. inspect H4 at rest and on hover
7. refine resting world spill only if needed
8. once interaction lighting is sufficiently settled, continue into deeper work-unit visual grammar
9. keep production Cockpit untouched until later integrated evidence warrants promotion
10. keep source-vault deployment paused until explicitly resumed
```
