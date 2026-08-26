# Current State

**Checkpoint:** 212  
**Date:** 2026-08-26  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration branch base:** `v1-frontend-spike` at Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at feature-promotion head `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C browser-rendered Project Cockpit design evaluation. G4 Adaptive Hybrid is selected as the grid/world substrate, dark mode is the current visual-design baseline, all tested ambient grid mechanisms are retained, and the active question is their combined intensity/frequency. The permanent source-vault bootstrap remains deliberately paused.  
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

# Current active boundary: combined G4 ambient intensity review

Primary route:

```text
docs/checkpoints/212_combined_g4_ambient_intensity_human_review_opened.md
docs/research/041_combined_g4_ambient_motion_intensity_tuning.md
frontend/design-lab/grid-dynamics-combined.html
frontend/design-lab/grid-dynamics-combined.css
frontend/design-lab/grid-dynamics-combined.js

docs/checkpoints/211_g4_selected_dark_first_ambient_dynamics_review_opened.md
docs/research/040_grid_world_g4_selection_dark_first_and_ambient_dynamics_exploration.md
frontend/design-lab/grid-dynamics.html

docs/checkpoints/210_grid_world_design_lab_browser_verified_human_review_opened.md
docs/research/039_phase_c_browser_rendered_design_experiment_protocol_and_grid_world_slice.md
frontend/design-lab/grid-world.html
```

## Preserved human design decisions

```text
G4 Adaptive Hybrid                  SELECTED grid/world substrate
Dark mode                           CURRENT design baseline
Light mode                          DEFERRED until dark Cockpit is substantially settled
Travelling grid currents            KEEP
Intersection glints                 KEEP
Slow ambient light drift            KEEP
Localized semantic activity         KEEP
Initial D1-D4 ambient frequency      TOO SUBTLE
```

The project owner explicitly prefers combining the ambient mechanisms rather than choosing one.

## Motion model

The current design distinguishes:

```text
AMBIENT MOTION
    decorative / atmospheric
    may exist purely to make the Cockpit feel polished and alive
    lower semantic authority

SEMANTIC MOTION
    represents actual project/runtime activity
    higher semantic authority
    should remain interpretable as project state
```

Decorative motion is allowed. The requirement is that it remain visually subordinate enough not to impersonate or obscure semantic state.

## Combined intensity experiment

The new browser design lab retains all ambient mechanisms and exposes three presets:

```text
Quiet
    all mechanisms survive
    long quiet gaps

Balanced
    default
    clearly more frequent than the first D1-D4 round
    still retains quiet intervals

Lively
    more continuous ambient life
    intended to test the upper comfortable range without rapid/random motion
```

Expected local URL:

```text
http://localhost:5173/design-lab/grid-dynamics-combined.html
```

Current human question:

```text
Is Balanced active enough?
Is Lively preferable?
Would a custom level between them be best?
Do individual currents/glints need brightness or length tuning in addition to frequency?
```

---

# Production boundary

Only isolated `frontend/design-lab/**` artifacts are being changed for this visual experiment.

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

After the grid/world slice is provisionally settled:

```text
work-unit visual grammar
semantic connector styling and relation vocabulary
semantic zoom thresholds/representations
stage/orientation treatment
Conversation Workspace composition
conversation + analytical coexistence
information-density lenses
runtime/waiting/approval visualization
selection/focus depth and transitions
command architecture at medium/large project scale
large-project grouping/aggregation/layout
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
1. use Checkpoint 212 and v1-cockpit-design-exploration as the current route
2. preserve G4 as the selected grid/world substrate
3. preserve dark-first sequencing and defer light mode
4. preserve all four ambient mechanisms
5. pull the latest branch locally
6. inspect http://localhost:5173/design-lab/grid-dynamics-combined.html
7. compare Quiet / Balanced / Lively in motion
8. tune frequency, brightness or trace length from human feedback if necessary
9. provisionally close the grid/world slice when its character is sufficiently settled
10. then open the next bounded design slice, likely work-unit visual grammar
11. keep production Cockpit implementation untouched until later evidence warrants promotion
12. keep source-vault deployment paused until the project owner chooses to resume it
```
