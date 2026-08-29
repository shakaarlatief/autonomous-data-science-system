# Project Cockpit Implementation Provenance

**Status:** Current Phase-C implementation-fidelity governance surface  
**Authority:** Specialized integration contract beneath accepted specifications, canonical decisions and foundations. It does not replace their semantic authority.  
**Current branch:** `v1-cockpit-design-exploration`  
**Current checkpoint:** 260  
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

For the current boundary, the latest routed pair is:

```text
docs/checkpoints/260_conversation_boxes_row_owned_spacing_human_recheck_opened.md
docs/research/099_conversation_boxes_visible_separation_human_retest_and_row_owned_geometry_recovery.md
```

Checkpoint 258 / Research 097 remain the still-open Adaptive Conversation Dock product-design pair underneath this temporary integrity recheck.

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

Later source-recovery and whole-product studies, Research 089 onward, are preserved through their own research records, checkpoints and current routing. Do not silently reinterpret the ledger as covering later research numbers it does not claim to cover.

### `ACCEPTED_IMPLEMENTATION_MANIFEST.md`

Human-readable integration contract for mechanisms that must survive holistic composition.

For each item it records:

```text
semantic decision
maturity
origin evidence
exact target SHA
exact implementation source files
invariants
allowed integration adaptations
fixture caveats
verification method
```

### `accepted_implementation_manifest.json`

Machine-readable counterpart used by deterministic checks and future integration tooling.

Current coverage:

```text
23 total entries
19 MUST_PORT / MUST_PRESERVE
4 non-promotable entries
```

### `scripts/check_cockpit_implementation_manifest.py`

Structural and historical validator for the machine-readable manifest. It guards against missing required integration items, invalid target identities, missing source paths, accidental promotion of deferred/provisional material and incomplete verification metadata.

### `.github/workflows/cockpit-implementation-provenance.yml`

Durable exact-history gate:

```text
python scripts/check_cockpit_implementation_manifest.py --verify-git-history
```

First exact-history run:

```text
workflow run 33156357834
entries=23 required=19 non_promotable=4
exact historical source verification PASS
```

### `.github/workflows/cockpit-reintegration-fidelity.yml`

Whole-product browser gate for the source-faithful integrated Cockpit.

Current complete result:

```text
implementation target  29419f7a1ccbd3cbcdc98f333e1b594c01d63fb1
workflow run           33241369935
job                    99071179670
browser tests          74 / 74 passing
```

The current gate contains all prior source-faithful mechanism coverage, Adaptive Conversation Dock isolation/state-preservation coverage, Focus lifecycle/remount synchronization coverage and the new Conversation Boxes legacy-artifact/user-like-viewport spacing regression.

## Human evidence can invalidate a green visual assumption

Checkpoint 260 records an important governance lesson.

The previous 73/73 gate passed, but the project owner's local screenshots still showed Conversation WorkUnit artifacts visibly joined. The deterministic gate therefore did not prove the visible defect was closed.

The correct response was to strengthen the implementation and the test contract rather than treating the test as more authoritative than direct visual evidence.

Current Conversation spacing implementation now owns the accepted separation at the thread rows rather than at the parent grid, and it applies to every non-Text Boxes/artifact state.

The current 74/74 result proves the encoded row-owned contract. Human recheck is still required before the visual issue is closed.

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

Establishes:

```text
manifest structure is valid
all required mechanism records exist
all exact historical commits resolve
all declared source paths exist at those exact commits
non-promotable entries remain non-promotable
failed holistic source remains excluded
```

Current status:

```text
PASS
```

### Integrated fidelity gate

Establishes:

```text
required mechanisms are present
geometry/visual invariants survive encoded regression states
interaction behavior survives
semantic meaning is unchanged
known fixture defects are not reintroduced
provisional glue remains separately identifiable
rejected/deferred candidates are not accidentally revived
```

Current status:

```text
PASS for the current covered implementation
74 / 74 browser tests at 29419f7a1ccbd3cbcdc98f333e1b594c01d63fb1
```

A deterministic pass is not human aesthetic/product-design approval and does not overrule direct local visual evidence. Checkpoint 260 remains under human spacing recheck. Checkpoint 258's Adaptive Conversation Dock remains under human product review once that recheck closes.

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
