# Project Cockpit Implementation Provenance

**Status:** Current Phase-C implementation-fidelity governance surface  
**Authority:** Specialized integration contract beneath accepted specifications, canonical decisions and foundations. It does not replace their semantic authority.  
**Current branch:** `v1-cockpit-design-exploration`  
**Current checkpoint:** 251

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
```

## Artifact roles

### `PHASE_C_DECISION_LEDGER.md`

Exhaustive disposition ledger for the new-Cockpit Phase-C design sequence.

It records not only selections, but also:

```text
SELECTED / HELD
PROVISIONAL WORKING DEFAULT
DEFERRED / PRESERVED
REJECTED
HISTORICAL / DIAGNOSTIC EVIDENCE
```

This distinction is essential. "We explored it" does not mean "implement it."

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

Structural and historical validator for the machine-readable manifest. It guards against missing required integration items, invalid target identities, missing source paths, accidental promotion of deferred/provisional material, and incomplete verification metadata.

### `.github/workflows/cockpit-implementation-provenance.yml`

Durable CI gate. It checks out full repository history and runs:

```text
python scripts/check_cockpit_implementation_manifest.py --verify-git-history
```

The first exact-history run passed:

```text
workflow run 33156357834
entries=23 required=19 non_promotable=4
exact historical source verification: PASS
```

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
keep it visually subordinate to accepted components
record it before it can become a new baseline
```

## Two fidelity gates

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

After the replacement browser is composed, establish:

```text
required mechanism is present
geometry/visual invariants survive
interaction behavior survives
semantic meaning is unchanged
known fixture defects were not reintroduced
provisional glue is separately identified
rejected/deferred candidates were not accidentally revived
```

Current status:

```text
OPEN / NOT YET PASSED
```

Visual comparison must use the exact accepted target as the reference, not prose alone.

## Failed integration

The browser at:

```text
8e554d847bb3b6318db432abcb5dff742f0fa523
```

is diagnostic evidence only and must never be used as a visual source of truth or as the parent source of the replacement browser.

Production `/cockpit` remains untouched during the current source-faithful reintegration phase.
