# Current State

**Checkpoint:** 266  
**Date:** 2026-08-29  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Latest specification:** Specification 024 remains accepted. Specification 008 remains the promoted V1 Project Cockpit interaction architecture.  
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no GENERIC / ADS_HORIZON / ORACLE_HORIZON comparison may be inferred from that run.

## Active interaction context

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-10
Conversation title       10 - Project Cockpit Design Exploration
Primary collaborator     ChatGPT
Collaboration thread     MC-0004
```

Repository artifacts remain authoritative across chats and models.

## Current Level-2 boundary

Checkpoint 266 refines the repository information architecture after the broader preservation audit at Research 103 / Checkpoint 265.

The substantive project knowledge remains preserved. The scaling problem was **discoverability and ownership of navigation responsibilities**, not missing storage.

Development Method v0.7 now separates six concerns explicitly:

```text
README.md              stable repository landing page
docs/README.md         repository/documentation structure and artifact roles
CURRENT_STATE.md       sole human-readable live project state
current_routing.json   sole machine-readable live routing pointer
KNOWLEDGE_MAP.md       evergreen subject -> knowledge library
CONTINUITY.md          reconstruction/recovery procedure
DEVELOPMENT_METHOD.md  method used to build, verify and preserve ADS
```

The Knowledge Map no longer duplicates current checkpoint, branch, CI or next-step state. It is an evergreen semantic library with exhaustive routing for every numbered Foundation, Specification and Research record. Every numbered checkpoint is also assigned to one or more subjects through validated semantic checkpoint ranges, while important checkpoints remain directly linked.

`docs/README.md` is now the answer to “what kinds of files do we have and what is each one for?”

### Development Method v0.7 verification model

The v0.6 risk-scaled verification ladder remains:

```text
V0  documentation / provenance validators
V1  targeted regression
V2  subsystem regression
V3  full integrated gate
V4  promotion / release gate
```

Unknown/shared blast radius still escalates to V3. Micro-iterations inside one open review question still aggregate rather than creating a checkpoint per tiny commit.

Checkpoint 266 additionally corrects the v0.6 full-Cockpit workflow invocation so a requested full gate actually expands and runs the complete Cockpit test family rather than a quoted literal glob.

## Checkpoint 266 validation status

This information-architecture transition changes validation/routing machinery, so final validation is open until the following evidence is green:

```text
Knowledge map integrity
    exhaustive Foundation / Specification / Research routing
    checkpoint semantic-range coverage
    path integrity
    no live-state leakage back into KNOWLEDGE_MAP

Current routing consistency
    current_routing.json agrees with CURRENT_STATE.md

Checkpoint metadata
    Checkpoints 263 and 264 metadata-only repair accepted
    current Checkpoint 266 contract valid

Cockpit reintegration fidelity
    one genuine full V3 run after correcting the full-suite invocation
```

The previously reported v0.6 run that executed only 16 tests is not accepted as a V3 pass.

## Current Cockpit product boundary remains Checkpoint 264

Checkpoint 266 is a Level-2 repository/development-method change. It does not reopen or change the Cockpit product design.

Latest human-confirmed state:

```text
Conversation WorkUnit spacing
    correct

General project discussion containment
    correct

current-process Focus
    working as far as tested
```

Still awaiting human visual confirmation:

```text
General project discussion visible footprint
    matches WorkUnit box footprint

Boxes selected-state frame
    frames the actual visible selected project/WorkUnit object
    no oversized structural row frame
```

Governing product evidence:

```text
docs/checkpoints/264_project_general_footprint_and_selection_frame_human_recheck_opened.md
docs/research/102_project_general_box_footprint_and_selection_frame_alignment.md
```

Normal review route:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html
```

If Checkpoint 264 is visually confirmed, close the Conversation presentation-integrity interruption and resume the Adaptive Conversation Dock review from:

```text
docs/checkpoints/258_adaptive_conversation_dock_human_review_opened.md
docs/research/097_professional_conversation_copresence_and_adaptive_dock_study.md
```

Adaptive route:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html?conversation=adaptive-dock
```

## Held product/scientific decisions

No Cockpit semantic/product decision is reopened by this repository architecture work. The held source-faithful Phase-C mechanism set, Quiet Graphite Conversation model, Boxes/Text navigation, A6, current-process Focus, Grid/X5/Deep Dive access, state preservation, L0 provisional status, semantic-zoom deferral and exact implementation-provenance architecture remain unchanged.

Implementation provenance remains governed by:

```text
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
```

The failed holistic browser at `8e554d847bb3b6318db432abcb5dff742f0fa523` remains diagnostic evidence only.

Source-vault bootstrap remains PAUSED, not cancelled. The Course 2 source-universe gate is unchanged.

Production `/cockpit` remains untouched.

## Exact next step

First close Checkpoint 266's validation gates.

Then the next product actor remains the human reviewer:

```text
pull latest v1-cockpit-design-exploration
hard-refresh
open http://localhost:4173/design-lab/cockpit-reintegration.html
switch between General project discussion and WorkUnit conversations
confirm equal visible footprint and correct selected-surface frame
```

If correct, resume the Adaptive Conversation Dock review immediately.
