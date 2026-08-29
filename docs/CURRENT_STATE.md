# Current State

**Checkpoint:** 265  
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

Checkpoint 265 is a development-method and knowledge-routing reconciliation, not a Cockpit product decision.

Research 103 found:

```text
substantive knowledge durability
    strong
    no major evidence of lost ADS knowledge

global discoverability
    degraded
    KNOWLEDGE_MAP had become current-Cockpit-heavy and no longer served
    its original broad topic-library role reliably

checkpoint granularity
    governing policy was sound
    recent frontend practice became too checkpoint-heavy

Cockpit verification
    complete 78-test gate was being run too often during tiny iterations
```

The response is Development Method v0.6.

### Development Method v0.6

```text
V0  documentation / provenance validators
V1  targeted regression
V2  subsystem regression
V3  full integrated gate
V4  promotion / release gate
```

Rules:

```text
unknown/shared blast radius -> V3
small isolated iteration -> V1/V2
low-risk visual tuning -> narrow deterministic check, then human review
meaningful acceptance closure -> broader/full gate required by the boundary
promotion/release -> V4
V1/V2 evidence must never be described as a complete Cockpit pass
```

Small implementation refinements within the same open human-review question should normally be aggregated inside that boundary rather than creating a new numbered checkpoint per commit.

### Knowledge routing

`docs/KNOWLEDGE_MAP.md` now has two explicit layers:

```text
Current continuation route
Evergreen topic library
```

The evergreen library restores project-wide topic discovery across canonical docs, foundations, research, specifications, checkpoints and specialized indexes.

Structural protection:

```text
scripts/check_knowledge_map.py
.github/workflows/knowledge-map-integrity.yml
```

Cockpit verification selection:

```text
scripts/select_cockpit_verification.py
.github/workflows/cockpit-reintegration-fidelity.yml
```

The selector narrows only high-confidence local changes and falls back to full V3 for mixed/shared/unknown changes. Obsolete same-branch runs are cancelled through CI concurrency control.

## Current Cockpit product boundary remains Checkpoint 264

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

Governing evidence:

```text
docs/checkpoints/264_project_general_footprint_and_selection_frame_human_recheck_opened.md
docs/research/102_project_general_box_footprint_and_selection_frame_alignment.md
```

Normal route:

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

## Verification status

Last complete Cockpit gate before the v0.6 workflow change:

```text
implementation/test target  9881efe313b8cf04d9521c0464050b30b29944c1
workflow run                33251166351
job                         99096968925
browser tests               78 / 78 passing
```

Checkpoint 265 changes the verification workflow itself, so one fresh full V3 Cockpit run is required before the method checkpoint closes. The commit introducing v0.6 explicitly requests that gate with `[full-cockpit]`.

Required repository validators for closure:

```text
Knowledge map integrity
Current routing consistency
Checkpoint metadata
full Cockpit V3 reintegration fidelity
```

## Held product decisions

No Cockpit semantic/product decision is reopened by Checkpoint 265. The held source-faithful Phase-C mechanism set, Quiet Graphite Conversation model, Boxes/Text navigation, A6, current-process Focus, Grid/X5/Deep Dive access, state preservation, L0 provisional status, semantic-zoom deferral and exact implementation-provenance architecture remain unchanged.

Implementation provenance remains governed by:

```text
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
```

The failed holistic browser at `8e554d847bb3b6318db432abcb5dff742f0fa523` remains diagnostic evidence only.

Source-vault bootstrap remains PAUSED, not cancelled. The Course 2 source-universe gate is unchanged.

Production `/cockpit` remains untouched.

## Exact next step

First close Checkpoint 265's method validation gates.

Then the next product actor is still the human reviewer:

```text
pull latest v1-cockpit-design-exploration
hard-refresh
open http://localhost:4173/design-lab/cockpit-reintegration.html
switch between General project discussion and WorkUnit conversations
confirm equal visible footprint and correct selected-surface frame
```

If correct, resume the Adaptive Conversation Dock review immediately.
