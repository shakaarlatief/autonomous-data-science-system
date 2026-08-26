# Current State

**Checkpoint:** 214  
**Date:** 2026-08-26  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration branch base:** `v1-frontend-spike` at Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at feature-promotion head `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Development stage:** MC-0004 Phase C browser-rendered Project Cockpit design evaluation. G4 Adaptive Hybrid is selected as the grid/world substrate, dark mode is the current visual-design baseline, all tested ambient mechanisms are retained, Lively remains the preferred current cadence, and glints are now restricted to major-grid intersections with an approximately Quiet independent cadence. The permanent source-vault bootstrap remains deliberately paused.  
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

# Current active boundary: major-grid glints + quiet glint cadence review

Primary route:

```text
docs/checkpoints/214_g4_major_grid_glints_quiet_cadence_human_review_opened.md
docs/research/043_g4_major_grid_glints_and_decoupled_ambient_cadence.md
frontend/design-lab/grid-dynamics-combined.html
frontend/design-lab/grid-dynamics-combined.css
frontend/design-lab/grid-dynamics-combined.js

docs/checkpoints/213_g4_randomized_ambient_distribution_human_review_opened.md
docs/research/042_g4_randomized_ambient_distribution_and_grid_intersection_glints.md

docs/checkpoints/212_combined_g4_ambient_intensity_human_review_opened.md
docs/research/041_combined_g4_ambient_motion_intensity_tuning.md

docs/checkpoints/211_g4_selected_dark_first_ambient_dynamics_review_opened.md
docs/research/040_grid_world_g4_selection_dark_first_and_ambient_dynamics_exploration.md
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
Current cadence preference           LIVELY for currents / drift
Fixed authored ambient coordinates   REJECTED
Glint location                        100 px MAJOR-GRID INTERSECTIONS ONLY
Glint cadence                         APPROXIMATELY QUIET / INDEPENDENT
```

The project owner explicitly prefers combining all ambient mechanisms rather than choosing one.

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

## Randomized ambient distribution

### Travelling currents

```text
horizontal or vertical
random visible grid line
coordinates snapped to the 20 px G4 lattice
random start position
random direction
random travel distance
random segment length
random appearance time
```

Currents can therefore appear across essentially any visible row or column. The Quiet / Balanced / Lively selector continues to govern current cadence and concurrency, with Lively currently preferred.

### Major-grid glints

Glints are now deliberately different from currents:

```text
x coordinate chosen from 100 px major-grid lines
y coordinate chosen from 100 px major-grid lines
therefore every glint lands on the corner of a large visible grid box
random major intersection each event
approximately Quiet cadence regardless of current intensity preset
maximum two concurrent glints
```

The glint is an occasional punctuation mark, not a continuously active sparkle layer.

### Ambient drift

```text
random starting position
random size
random movement vector
random opacity within the active cadence preset
```

Drift remains atmospheric rather than grid-snapped.

## Intensity presets remain

```text
Quiet
Balanced
Lively
```

These primarily control travelling currents and ambient drift. Glints now use their own Quiet-like cadence.

Expected local URL:

```text
http://localhost:5173/design-lab/grid-dynamics-combined.html
```

Current human question:

```text
Do glints now land only on corners of the large 100 px grid boxes?
Are they rare enough?
Do Lively currents still feel right after this decoupling?
Does the combined world feel alive rather than sparkly?
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
1. use Checkpoint 214 and v1-cockpit-design-exploration as the current route
2. preserve G4 as the selected grid/world substrate
3. preserve dark-first sequencing and defer light mode
4. preserve all four ambient mechanisms
5. preserve Lively as the current preference for currents and drift
6. preserve approximately Quiet independent glints on 100 px major intersections
7. pull the latest branch locally
8. refresh http://localhost:5173/design-lab/grid-dynamics-combined.html
9. verify glint placement and cadence while currents remain Lively
10. tune again only if needed
11. provisionally close the grid/world slice when its character is sufficiently settled
12. then open the next bounded design slice, likely work-unit visual grammar
13. keep production Cockpit implementation untouched until later evidence warrants promotion
14. keep source-vault deployment paused until the project owner chooses to resume it
```
