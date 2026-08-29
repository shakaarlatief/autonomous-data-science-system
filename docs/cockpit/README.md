# Project Cockpit Implementation Provenance

**Status:** Current Phase-C implementation-fidelity governance surface  
**Authority:** Specialized integration contract beneath accepted specifications, canonical decisions and foundations. It does not replace their semantic authority.  
**Current branch:** `v1-cockpit-design-exploration`  
**Current checkpoint:** 264  
**Last reconciled:** 2026-08-29

## Purpose

The next-generation Project Cockpit was designed through many bounded browser-rendered experiments. The first holistic reconstruction failed because semantic summaries were used as permission to redraw already accepted implementations.

This directory closes that gap.

The governing rule is:

```text
semantic decision
    + exact implementation provenance
    + explicit maturity/disposition
    + allowed adaptation boundary
    + fidelity verification
```

A future integrator must not infer an implementation merely from labels such as `G4`, `H4`, `SEL2`, `X5`, `Quiet Graphite` or `A6`.

## Required reading order for Cockpit integration

```text
1. docs/specifications/008_v1_project_cockpit_interaction_architecture.md
2. docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
3. docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
4. docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
5. docs/cockpit/PHASE_C_DECISION_LEDGER.md
6. docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
7. docs/cockpit/accepted_implementation_manifest.json
8. docs/research/088_integrated_cockpit_fidelity_failure_and_source_of_truth_recovery_audit.md
9. docs/research/089_cockpit_implementation_provenance_recovery_completion_and_exact_history_gate.md
10. docs/checkpoints/251_cockpit_implementation_provenance_recovered_and_reintegration_opened.md
11. docs/CURRENT_STATE.md
12. latest routed checkpoint + research record
```

For the current boundary:

```text
docs/checkpoints/264_project_general_footprint_and_selection_frame_human_recheck_opened.md
docs/research/102_project_general_box_footprint_and_selection_frame_alignment.md

docs/checkpoints/263_project_general_thread_containment_human_recheck_opened.md
docs/research/101_project_general_thread_short_viewport_containment_recovery.md

docs/checkpoints/262_conversation_boxes_grid_track_spacing_human_recheck_opened.md
docs/research/100_conversation_boxes_css_grid_track_absorption_and_live_geometry_recovery.md

docs/checkpoints/261_chatgpt_10_interaction_provenance_reconciliation.md
```

Checkpoint 258 / Research 097 remain the still-open Adaptive Conversation Dock product-design pair underneath the temporary Checkpoint 264 integrity recheck.

## Artifact roles

### `PHASE_C_DECISION_LEDGER.md`

The disposition ledger is exhaustive for its declared Research 037-088 design sequence.

It distinguishes:

```text
SELECTED / HELD
PROVISIONAL WORKING DEFAULT
DEFERRED / PRESERVED
REJECTED
HISTORICAL / DIAGNOSTIC EVIDENCE
```

Later source-recovery and whole-product studies, Research 089 onward, are preserved through their own research records, checkpoints and current routing.

### `ACCEPTED_IMPLEMENTATION_MANIFEST.md`

Human-readable integration contract for mechanisms that must survive holistic composition.

For each item it records semantic decision, maturity, origin evidence, exact target SHA, exact implementation source files, invariants, allowed integration adaptations, fixture caveats and verification method.

### `accepted_implementation_manifest.json`

Machine-readable counterpart used by deterministic checks and future integration tooling.

Current coverage:

```text
23 total entries
19 MUST_PORT / MUST_PRESERVE
4 non-promotable entries
```

### Provenance gate

```text
python scripts/check_cockpit_implementation_manifest.py --verify-git-history
```

First exact-history run:

```text
workflow run 33156357834
entries=23 required=19 non_promotable=4
exact historical source verification PASS
```

## Current whole-product fidelity gate

Current complete result:

```text
implementation/test target  9881efe313b8cf04d9521c0464050b30b29944c1
workflow run                33251166351
job                         99096968925
browser tests               78 / 78 passing
```

The gate contains all prior source-faithful mechanism coverage plus Adaptive Conversation Dock isolation/state-preservation, Focus lifecycle/remount synchronization, human-confirmed WorkUnit spacing protection, project-general short-height containment and the new project-general footprint/selected-surface alignment regression.

## Human evidence governs visible fidelity

The recent Conversation rail sequence records why deterministic tests and direct visual evidence must work together.

Research 100 established the exact reason WorkUnit margins could compute as 16px while the visible boxes still nearly touched: CSS Grid auto-track sizing shrank the structural row while transformed overflow-visible WorkUnits painted beyond it. Explicit grid-track spacing plus sufficient WorkUnit row height fixed that defect, and the project owner has now visually confirmed the WorkUnit spacing is correct.

Research 101 then added only project-general row containment after the first WorkUnit invaded General project discussion at a short desktop viewport. The latest screenshot confirms that containment is also correct.

Research 102 addresses the remaining small visual inconsistency:

```text
accepted WorkUnit rail slot
    232 x 74 px normal
    214 x 69 px responsive <=1450

project-general artifact
    now matches those exact visible dimensions

Boxes active row
    structural wrapper stays transparent

project selected surface
    visible project artifact

WorkUnit selected surface
    visible canonical WorkUnit node surface
```

Text mode retains its generic row selection because the row is the visible navigation object there.

The existing 16px grid spacing is not enlarged. At the short viewport, equal visible project/WorkUnit sizing produces a 15px painted project-to-first-WorkUnit gap while the structural row-gap remains 16px. WorkUnit-to-WorkUnit visible gaps remain protected at >=20px.

Checkpoint 264 requires one final human visual confirmation of this footprint and selected-frame alignment.

## Interaction provenance continuity

Checkpoint 261 records the current ChatGPT interaction as:

```text
interaction session  chatgpt-10
conversation title   10 - Project Cockpit Design Exploration
```

It corrects only post-boundary metadata after an unplanned conversation rotation. Pre-boundary ChatGPT-09 history remains unchanged.

## Integration policy

### Accepted implementation exists

```text
reuse or port the exact source implementation
preserve accepted geometry and behavior
adapt only inside the manifest's allowed boundary
verify against the exact target before human review
```

### Provisional working default exists

```text
carry only where needed to make the product operable
label it provisional
never let integration silently promote it
```

### Deferred, rejected or evidence-only candidate exists

```text
preserve it as design history
DO NOT implement it as accepted product behavior
```

### No accepted whole-product answer exists

```text
introduce minimum integration glue only
label the glue provisional
keep it subordinate to accepted components
record it before it can become a new baseline
isolate it behind an explicit review route when practical
```

The current `?conversation=adaptive-dock` study follows this policy: it changes co-present composition only, remains opt-in and leaves the accepted no-query Cockpit unchanged until human review.

## Fidelity gates

### Provenance gate

Current status:

```text
PASS
```

It establishes that manifest structure is valid, required mechanism records exist, exact historical commits and source paths resolve, non-promotable entries remain non-promotable and the failed holistic source remains excluded.

### Integrated fidelity gate

Current status:

```text
PASS for the current covered implementation
78 / 78 browser tests at 9881efe313b8cf04d9521c0464050b30b29944c1
```

A deterministic pass is not human aesthetic/product-design approval and does not overrule direct local visual evidence. Checkpoint 264 remains under human footprint/selection-frame recheck. Checkpoint 258's Adaptive Conversation Dock remains under human product review once that recheck closes.

## Failed integration

The browser at:

```text
8e554d847bb3b6318db432abcb5dff742f0fa523
```

is diagnostic evidence only and must never be used as a visual source of truth or as the parent source of the replacement browser.

## Current review isolation

Normal current whole-product substrate:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html
```

Adaptive Conversation candidate:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html?conversation=adaptive-dock
```

Production `/cockpit` remains untouched during the current whole-product design exploration.
