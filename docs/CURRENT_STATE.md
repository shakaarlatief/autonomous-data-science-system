# Current State

**Checkpoint:** 215  
**Date:** 2026-08-26  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration branch base:** `v1-frontend-spike` at Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at feature-promotion head `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C browser-rendered Project Cockpit design evaluation. The current G4 grid/world treatment is provisionally settled for now; dark mode remains the design baseline; the active bounded slice is work-unit interaction lighting. The permanent source-vault bootstrap remains deliberately paused.  
**Latest specification:** Specification 024 remains accepted with outcome `COLLABORATION_STATE_GUARD_ACCEPTED`. Specification 008 remains the promoted V1 Project Cockpit interaction architecture.  
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

# Current active boundary: work-unit interaction lighting review

Primary route:

```text
docs/checkpoints/215_grid_world_provisionally_settled_work_unit_lighting_review_opened.md
docs/research/044_work_unit_interaction_lighting_hover_response_exploration.md
frontend/design-lab/work-unit-lighting.html
frontend/design-lab/work-unit-lighting.css
frontend/design-lab/work-unit-lighting.js

docs/checkpoints/214_g4_major_grid_glints_quiet_cadence_human_review_opened.md
docs/research/043_g4_major_grid_glints_and_decoupled_ambient_cadence.md
frontend/design-lab/grid-dynamics-combined.html
```

Expected local review URL:

```text
http://localhost:5173/design-lab/work-unit-lighting.html
```

## Grid/world disposition

The grid/world layer is now **provisionally settled**, not permanently frozen.

Current retained direction:

```text
G4 Adaptive Hybrid                  SELECTED grid/world substrate
Dark mode                           CURRENT design baseline
Light mode                          DEFERRED until dark Cockpit is substantially settled
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

The project owner explicitly said this treatment can remain for now while preserving the ability to adjust or add details later.

## Motion model remains

```text
AMBIENT MOTION
    decorative / atmospheric
    may exist simply because it looks polished and alive
    lower semantic authority

SEMANTIC MOTION
    represents actual changing project/runtime state
    higher semantic authority
    should remain interpretable as project state
```

---

# Work-unit lighting Slice 02A

The project owner strongly liked the colored lighting around work units and proposed richer color-specific hover response.

Current hypothesis:

```text
REST
    localized / asymmetric colored atmosphere
    quiet enough for long sessions

HOVER
    fuller node-specific colored light
    responsive and visibly interactive

SELECTED
    later persistent focus treatment

ACTIVE / RUNNING
    later semantic state-bearing light behavior
```

Representative category colors in this lab are not yet a final semantic palette.

## H1 Full Halo

```text
localized asymmetric rest glow
-> full colored perimeter halo on hover
-> slightly brighter accent edge
-> ~2 px depth lift
```

Purpose: establish the simplest responsive-light baseline.

## H2 Cursor Edge

```text
H1
+ pointer-following/specular hotspot
```

Purpose: test whether pointer proximity makes the node feel tactile/premium rather than merely highlighted.

## H3 World Spill

```text
full hover light
+ faint node-colored illumination in nearby grid
+ immediate connected paths become clearer
```

Purpose: test whether nodes should feel embedded in the G4 world rather than simply layered above it.

## H4 Integrated Response

```text
localized rest light
full hover halo
pointer-following hotspot
local grid spill
connector emphasis
one restrained perimeter sweep on hover entry
small depth lift
```

Purpose: test the richest plausible combination before deciding which individual mechanisms deserve to survive.

The perimeter sweep is one-shot on hover entry, not a continuous loop.

## Current human review questions

```text
should full-perimeter colored hover light survive?
is pointer-following light attractive or distracting?
should nearby grid geometry inherit faint node color on hover?
should immediate connectors become clearer on hover?
should the one-time perimeter sweep survive?
should resting light remain asymmetric/localized?
```

The project owner may combine mechanisms rather than selecting H1-H4 literally.

---

# Important non-decisions

This slice does **not** freeze:

```text
final work-unit silhouette / shape grammar
final semantic category colors
final status palette
final selected-state treatment
final active/running/waiting treatment
final blocked-state treatment
final node dimensions
final typography
final semantic connector vocabulary
final 2.5D depth system
production animation implementation
production motion library
```

Those remain later design questions.

---

# Production boundary

Only isolated `frontend/design-lab/**` artifacts are authorized for the current visual experiment.

The promoted production `/cockpit` implementation remains the control baseline.

Still not authorized:

```text
replacement of production Cockpit components
production route migration
new graph/canvas library adoption
new motion-library adoption
final semantic-zoom architecture
final semantic connector architecture
final conversation persistence model
final visual-system freeze
full 3D
```

---

# MC-0004 evidence remains preserved

```text
Phase A
    Claude independent proposal
    commit cd2e12f2c79ee3b2f205457c5940eb2022b4631a
    BLIND_TO_CANDIDATE

Phase B
    Claude comparative review
    commit d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce
    COMPARATIVE_ONLY

Phase C
    browser-rendered design evaluation
    current actor: human
```

Generated-image UI concepts are not part of the preferred Cockpit evaluation workflow. Real browser-rendered experiments and real external references are preferred.

---

# Remaining major Cockpit design questions

After interaction lighting is refined, major unresolved areas still include:

```text
work-unit category / silhouette visual grammar
multi-axis status treatment
semantic connector styling and relation vocabulary
semantic zoom thresholds / representations
stage / orientation treatment
Conversation Workspace composition
conversation + analytical coexistence
information-density lenses
runtime / waiting / approval visualization
selection / focus depth and transitions
command architecture at medium / large project scale
large-project grouping / aggregation / layout
final design system
```

The command-architecture question remains gated by medium/large project evidence rather than preference.

---

# Specification 008 remains the promoted interaction baseline

The current design exploration does not supersede Specification 008. Final visual identity, graph/canvas technology, semantic zoom/grouping, auto-layout, stage treatment, ambient styling and other still-unfrozen choices remain open until later evidence supports promotion.

---

# Permanent Source Universe deployment remains preserved and paused

```text
source-vault bootstrap
    PAUSED
    not cancelled
    not rejected
    not superseded
    accepted architecture/runbook unchanged
    no real permanent deployment yet
```

Course 2 remains blocked until the permanent compare, reviewed ingestion, working-store audit, independent backup, clean restore and restored audit succeed.

The methodological knowledge-universe program remains the larger V1 objective and is not superseded by the current Cockpit subtrack.

---

## Exact continuation

```text
1. use Checkpoint 215 and v1-cockpit-design-exploration as the current route
2. keep the current G4 grid/world treatment provisionally settled
3. preserve dark-first sequencing and current ambient behavior
4. pull the latest branch locally
5. open http://localhost:5173/design-lab/work-unit-lighting.html
6. hover the same colored work units across H1-H4
7. record keep/reject/combine/refine feedback for halo, cursor light, world spill, connector response, sweep and rest asymmetry
8. refine once if useful
9. then continue into deeper work-unit visual grammar
10. keep production Cockpit implementation untouched until later integrated evidence warrants promotion
11. keep source-vault deployment paused until the project owner chooses to resume it
```
