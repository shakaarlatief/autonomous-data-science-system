# Autonomous Data Science System

## Overview

This repository is the persistent development home of the Autonomous Data Science System (ADS).

ADS is being developed as a rigorous, adaptive, semi-autonomous environment for data-science projects in which a strong LLM is one flexible reasoning component inside a wider system that owns project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

> **The chat is where we think. The repository is where the system remembers.**

## Current development stage

```text
checkpoint            262
active branch         v1-cockpit-design-exploration
active PR             none
promoted V1 head      ed5b60bdc882bed0799ce55228ce8187f9c55aa1
latest specification  Specification 024
Cockpit baseline      Specification 008
current boundary      Conversation Boxes grid-track spacing human recheck
source-vault          PAUSED, preserved, Course 2 gate unchanged
```

Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no scientific `GENERIC` / `ADS_HORIZON` / `ORACLE_HORIZON` comparison may be inferred from that run.

## Current interaction continuity

The active ChatGPT interaction is:

```text
interaction session  chatgpt-10
conversation title   10 - Project Cockpit Design Exploration
```

Checkpoint 261 records the repaired conversation boundary after the preceding ChatGPT conversation reached its length limit. Pre-boundary ChatGPT-09 provenance remains historical and unchanged.

## Current Cockpit status

The source-faithful integrated Cockpit is the protected whole-product design substrate.

Primary browser:

```text
frontend/design-lab/cockpit-reintegration.html
```

Normal current substrate:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html
```

Adaptive Conversation Dock review route:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html?conversation=adaptive-dock
```

### Conversation Boxes integrity

Checkpoint 262 supersedes the failed Checkpoint 260 row-owned-margin implementation.

The project owner's live Chrome measurements established the exact failure:

```text
WorkUnit row height           54.0px
computed bottom margin       16px
row-to-row distance          16.0px
painted WorkUnit overflow    ~20.8px below row
visible surface gap          ~1.9px
```

The problem was CSS Grid track sizing, not stale Git state or missing CSS. The grid accounted for the item margin by shrinking the WorkUnit row while the transformed, overflow-visible canonical WorkUnit continued painting outside that row.

Research 100 therefore restores explicit inter-track spacing and prevents row shrinkage from consuming the accepted breathing room:

```text
thread-list row-gap          16px
project row margin            0px
WorkUnit row margin           0px
WorkUnit padding              6px top / 6px bottom
wide WorkUnit min-height     78px
responsive <=1450 min-height 73px
canonical WorkUnit           unchanged
```

The spacing contract still applies to all non-Text Boxes/artifact-compatible rail states.

### Current-process Focus integrity

No Focus implementation changed in Checkpoint 262.

Research 098's DOM-independent membership and remount synchronization recovery remains current, and the project owner's latest retest reports Focus working as far as tested.

Focus should not be reopened without a new concrete reproduction.

Latest complete Cockpit fidelity workflow:

```text
implementation/test target  b8a2d095214c3417f95180ca519c7b6224739181
workflow run                33247046868
job                         99086212488
browser tests               76 / 76 passing
```

The strengthened gate explicitly covers 1600px desktop, 1100px responsive and 760px narrow spacing, legacy `artifact` compatibility, actual visible surface-to-surface separation, Adaptive Dock presentation transitions and all prior source-faithful mechanisms.

The Adaptive Conversation Dock remains an opt-in product-design candidate. Its design judgment resumes only after the project owner confirms the Boxes rail now visibly separates the conversation objects locally.

Production `/cockpit` remains untouched.

## Critical integration history

The first holistic integrated Cockpit browser at:

```text
8e554d847bb3b6318db432abcb5dff742f0fa523
```

is **not an accepted Cockpit baseline**.

Human review exposed major fidelity failures against previously accepted Phase-C designs. The repository had preserved exact accepted target SHAs and executable artifacts, but integration manually reimplemented them from textual summaries instead of faithfully reusing or porting those exact artifacts.

The failed browser remains diagnostic evidence only and is excluded from the replacement source graph.

## Implementation-provenance recovery

The Cockpit provenance layer remains authoritative:

```text
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
scripts/check_cockpit_implementation_manifest.py
.github/workflows/cockpit-implementation-provenance.yml
```

Manifest coverage:

```text
23 total entries
19 MUST_PORT / MUST_PRESERVE
4 deliberately non-promotable entries
```

First exact-history proof:

```text
workflow run 33156357834
commit       2127563c0ed980f7bf6fad36e36b11e76500c59b
result       PASS
```

The rule remains:

```text
accepted implementation exists
    -> reuse or port exact implementation
    -> preserve accepted geometry / behavior / hierarchy
    -> adapt only inside the recorded boundary
    -> verify against exact source evidence
```

## Held Phase-C decisions remain intact

The held mechanism set still includes G4, H4, scientific WorkUnit grammar, E5, D0-D3, P7, current-process focus, runtime/T7, BLOCKED/FAIL, A3, SEL2, X5, Z7, Quiet Graphite, Boxes/Text, A6 and Conversation access across Grid and Deep Dive.

L0 remains provisional. Semantic zoom remains deferred with S0 as the geometric working default.

Checkpoint 262 changes only the implementation mechanism that guarantees the already-reviewed Conversation separation. It does not reopen the spacing target, M09 Focus semantics, Quiet Graphite, Boxes/Text, A6, conversation scope/access, source-state preservation or the Adaptive Conversation Dock composition question.

`docs/cockpit/PHASE_C_DECISION_LEDGER.md` remains the exhaustive disposition ledger for Research 037-088. Later source-recovery and whole-product studies are routed through Research 089 onward, checkpoints and current-state records.

## Repository preservation model

```text
semantic/product authority
    + design disposition
    + exact implementation provenance
    + deterministic historical-source verification
    + integrated implementation-fidelity verification
    + explicit current routing
    + human product-design gates
```

## Start here

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json

docs/checkpoints/262_conversation_boxes_grid_track_spacing_human_recheck_opened.md
docs/research/100_conversation_boxes_css_grid_track_absorption_and_live_geometry_recovery.md

docs/checkpoints/261_chatgpt_10_interaction_provenance_reconciliation.md

docs/checkpoints/260_conversation_boxes_row_owned_spacing_human_recheck_opened.md
docs/research/099_conversation_boxes_visible_separation_human_retest_and_row_owned_geometry_recovery.md

docs/checkpoints/259_cockpit_presentation_state_integrity_recovery.md
docs/research/098_intermittent_cockpit_presentation_state_integrity_recovery.md

docs/checkpoints/258_adaptive_conversation_dock_human_review_opened.md
docs/research/097_professional_conversation_copresence_and_adaptive_dock_study.md

docs/cockpit/README.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json

# collaboration state
docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/REVIEW_INBOX.md
```
