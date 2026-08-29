# Autonomous Data Science System

## Overview

This repository is the persistent development home of the Autonomous Data Science System (ADS).

ADS is being developed as a rigorous, adaptive, semi-autonomous environment for data-science projects in which a strong LLM is one flexible reasoning component inside a wider system that owns project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

> **The chat is where we think. The repository is where the system remembers.**

## Current development stage

```text
checkpoint            263
active branch         v1-cockpit-design-exploration
active PR             none
promoted V1 head      ed5b60bdc882bed0799ce55228ce8187f9c55aa1
latest specification  Specification 024
Cockpit baseline      Specification 008
current boundary      project-general thread containment human recheck
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

Research 100's CSS Grid track-gap recovery is now human-confirmed for the WorkUnit spacing defect. The project owner's latest screenshot shows the dark breathing room between WorkUnits correctly restored.

The same screenshot exposed one narrower remaining issue: the General project discussion artifact could still be visually invaded by the first WorkUnit at a wide but vertically short browser viewport.

Research 101 preserves the accepted WorkUnit spacing contract and adds explicit containment for the project-general first row:

```text
thread-list row-gap          16px
project row min-height       74px
project row padding           7px top / 7px bottom
project artifact min-height  58px
WorkUnit row margin           0px
WorkUnit padding              6px top / 6px bottom
wide WorkUnit min-height     78px
responsive <=1450 min-height 73px
canonical artifacts          unchanged
```

The project artifact is not redesigned. The row that owns it now reserves enough track height before the existing 16px grid gap begins.

### Current-process Focus integrity

No Focus implementation changed in Checkpoint 263.

Research 098's DOM-independent membership and remount synchronization recovery remains current, and the project owner's latest retest reports Focus working as far as tested.

Focus should not be reopened without a new concrete reproduction.

Latest complete Cockpit fidelity workflow:

```text
implementation/test target  5913467cfffd535215da7ab2cb70bdeb2be9f2e9
workflow run                33247621778
job                         99087735314
browser tests               77 / 77 passing
```

The new regression explicitly exercises a `1776 x 766` short desktop viewport and requires General project discussion to remain a complete first artifact with at least 16px visible separation before the first WorkUnit. All previous spacing, Adaptive Dock, Focus and source-faithful mechanism coverage remains green.

The Adaptive Conversation Dock remains an opt-in product-design candidate. Its design judgment resumes after the project owner visually confirms this final base-rail containment correction.

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

Checkpoint 263 changes only the containment geometry of the project-general Conversation row at short viewports. It does not reopen the accepted WorkUnit spacing target, M09 Focus semantics, Quiet Graphite, Boxes/Text, A6, conversation scope/access, source-state preservation or the Adaptive Conversation Dock composition question.

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

docs/checkpoints/263_project_general_thread_containment_human_recheck_opened.md
docs/research/101_project_general_thread_short_viewport_containment_recovery.md

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
