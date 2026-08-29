# Project Cockpit Implementation Provenance

**Status:** PAUSED / safely resumable next-generation Cockpit design and fidelity surface  
**Authority:** Specialized integration contract beneath accepted specifications, canonical decisions and foundations. It does not replace their semantic authority.  
**Frozen design branch:** `v1-cockpit-design-exploration`  
**Frozen frontend head:** `04f2a907094b8023ac7377c399a6eef1a6e1da99`  
**Current routing checkpoint:** 267  
**Last reconciled:** 2026-08-29

## Current pause boundary

The project owner explicitly paused the frontend Cockpit session at Checkpoint 267 and resumed the permanent Source Vault bootstrap.

The Cockpit is therefore:

```text
PAUSED
not rejected
not deleted
not production-promoted
exact implementation and verification state preserved
```

Production `/cockpit` remains untouched.

The exact future resume anchor is:

```text
branch   v1-cockpit-design-exploration
head     04f2a907094b8023ac7377c399a6eef1a6e1da99
workflow 33268350178
job      99142293330
gate     V3 full
browser  84 / 84 PASS
```

Do not advance the frozen Cockpit branch merely to record unrelated Source Universe work. The active continuation now lives on `v1-source-vault-bootstrap-resume`.

## Human-confirmed state at pause

The frontend session progressed beyond the older Checkpoint 264 recheck before it was paused.

Current preserved product state includes:

```text
Conversation WorkUnit spacing
    human-confirmed correct

General project discussion containment
    human-confirmed correct

General project footprint + selected-surface frame
    human-confirmed correct

Adaptive Conversation Dock
    resizable split-pane direction accepted for continuation
    direct co-present entry preferred
    Threads remains invoked in compact co-presence
    Project tools remain usable beside Conversation

Deep Dive + Conversation
    true split-workspace composition
    direct Deep Dive action from expanded WorkUnit
    Deep Dive typography moved away from micro-label fixture styling

keyboard contract
    Escape = application Back
    F = browser fullscreen toggle
    Shift+C = Conversation full-focus/co-present toggle
    T = Threads in co-present Conversation

Project tool rail beside Conversation
    56px flush full-height application-edge utility strip
    quieter graphite visual language
    196px labelled clarity expansion

normal Cockpit Project tool rail
    same 56px/quieter visual language adopted
    remains bounded and inset rather than full-height
    human response: positive / accepted for continuation
```

These refinements remain design-lab candidate behavior until separately promoted.

## Purpose of this directory

The next-generation Project Cockpit was designed through many bounded browser-rendered experiments. The first holistic reconstruction failed because semantic summaries were used as permission to redraw already accepted implementations.

This directory prevents that failure mode.

The governing rule is:

```text
semantic decision
    + exact implementation provenance
    + explicit maturity/disposition
    + allowed adaptation boundary
    + fidelity verification
```

A future integrator must not infer an implementation merely from labels such as `G4`, `H4`, `SEL2`, `X5`, `Quiet Graphite` or `A6`.

## Required reading order when Cockpit work resumes

```text
1. docs/checkpoints/267_cockpit_frontend_paused_source_vault_bootstrap_resumed.md
2. docs/CURRENT_STATE.md
3. docs/specifications/008_v1_project_cockpit_interaction_architecture.md
4. docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
5. docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
6. docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
7. docs/cockpit/PHASE_C_DECISION_LEDGER.md
8. docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
9. docs/cockpit/accepted_implementation_manifest.json
10. docs/research/088_integrated_cockpit_fidelity_failure_and_source_of_truth_recovery_audit.md
11. docs/research/089_cockpit_implementation_provenance_recovery_completion_and_exact_history_gate.md
12. docs/research/097_professional_conversation_copresence_and_adaptive_dock_study.md
13. docs/research/100_conversation_boxes_css_grid_track_absorption_and_live_geometry_recovery.md
14. docs/research/101_project_general_thread_short_viewport_containment_recovery.md
15. docs/research/102_project_general_box_footprint_and_selection_frame_alignment.md
```

Then inspect the frozen browser candidate directly from the exact branch head.

## Artifact roles

### `PHASE_C_DECISION_LEDGER.md`

Exhaustive disposition ledger for its declared Research 037-088 design sequence.

It distinguishes:

```text
SELECTED / HELD
PROVISIONAL WORKING DEFAULT
DEFERRED / PRESERVED
REJECTED
HISTORICAL / DIAGNOSTIC EVIDENCE
```

Research 089 onward is preserved through its own research records, checkpoints and current routing rather than retroactively rewriting the original ledger scope.

### `ACCEPTED_IMPLEMENTATION_MANIFEST.md`

Human-readable integration contract for mechanisms that must survive holistic composition.

For each entry it records semantic decision, maturity, origin evidence, exact target SHA, implementation source files, invariants, allowed integration adaptations, fixture caveats and verification method.

### `accepted_implementation_manifest.json`

Machine-readable counterpart used by deterministic checks and future integration tooling.

The manifest remains the implementation source-of-truth layer for accepted/held mechanisms. Later candidate presentation refinements do not silently rewrite manifest-bound history.

## Provenance gate

```text
python scripts/check_cockpit_implementation_manifest.py --verify-git-history
```

The exact-history gate establishes that required historical commits/source paths resolve and that rejected/non-promotable material is not silently elevated.

## Integrated fidelity gate

Latest complete frozen result:

```text
implementation/test target  04f2a907094b8023ac7377c399a6eef1a6e1da99
workflow run                33268350178
job                         99142293330
verification tier           V3 full
browser tests               84 / 84 PASS
```

A deterministic pass is not aesthetic approval. Human browser evidence remains authoritative for visible product fidelity and usability.

## Important recovered fidelity history

Research 100 established why Conversation WorkUnit margins could compute correctly while boxes still visually touched: CSS Grid auto-track sizing shrank structural rows while transformed overflow-visible WorkUnits painted beyond them. Explicit grid-track spacing plus sufficient row height repaired the actual rendered gap.

Research 101 added project-general containment after the first WorkUnit invaded the General project discussion row at a short desktop viewport.

Research 102 aligned the project-general visible artifact and selected-surface frame with canonical WorkUnit navigation geometry.

The project owner subsequently confirmed those presentation-integrity repairs before the Adaptive Dock practical-workbench review continued.

## Current adaptive-workbench direction

The opt-in route remains:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html?conversation=adaptive-dock
```

Normal integrated substrate:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html
```

The adaptive candidate currently explores:

```text
resizable Conversation secondary dock
direct co-present entry
invoked Threads navigation
Conversation + Deep Dive split workspace
layered Back/fullscreen keyboard contract
shared professional Project-tool visual language across normal and co-present states
```

The candidate remains unpromoted while paused.

## Integration policy

### Accepted implementation exists

```text
reuse or port exact source implementation
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
record it before it becomes a baseline
isolate it behind explicit review routes where practical
```

## Failed integration that must not become a source

The browser at:

```text
8e554d847bb3b6318db432abcb5dff742f0fa523
```

remains diagnostic evidence only and must never be used as a visual source of truth or parent implementation source.

## Resume rule

When the project owner chooses to return to frontend work:

```text
1. switch back to v1-cockpit-design-exploration
2. verify exact frozen head 04f2a907094b8023ac7377c399a6eef1a6e1da99 or explicitly create a continuation from it
3. read Checkpoint 267 + Research 097 + this README
4. inspect the current normal and adaptive routes in-browser
5. continue practical whole-product review from the preserved candidate
6. do not reopen already human-confirmed spacing/containment/selection fixes without new contrary evidence
7. keep production /cockpit untouched until a separate promotion boundary is earned
```
