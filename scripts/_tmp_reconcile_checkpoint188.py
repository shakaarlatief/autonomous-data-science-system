from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected one exact anchor, found {count}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")


replace_once(
    "README.md",
    '''```text
checkpoint            187
active branch         v1-methodological-navigation-coverage-diagnostic
active PR             #68
promoted V1 head      0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e
current boundary      Question A diagnostic design choices resolved; Specification 022 not frozen
latest experiment     Specification 021
outcome               FAIL
next                  validate this design boundary, then freeze the exact
                      Specification 022 contract before implementation
```''',
    '''```text
checkpoint            188
active branch         v1-methodological-navigation-coverage-diagnostic
active PR             #68
promoted V1 head      0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e
current boundary      Specification 022 scientific contract frozen; provider-free implementation next
latest specification  Specification 022
latest experiment     Specification 021
outcome               FAIL
next                  validate the exact frozen-contract head, then implement
                      provider-free Specification 022 machinery and integrity tests
```''',
)
replace_once(
    "README.md",
    "Checkpoint 187     project-state methodological coverage diagnostic design choices resolved; Specification 022 still not frozen",
    "Checkpoint 187     project-state methodological coverage diagnostic design choices resolved\nSpecification 022  project-state-to-methodological-horizon coverage diagnostic contract frozen\nCheckpoint 188     exact Specification 022 fixtures, runtime treatment, metrics, thresholds, seed, and gates frozen; no provider call authorized",
)

replace_once(
    "docs/CURRENT_STATE.md",
    '''**Checkpoint:** 187  
**Date:** 2026-08-24  
**Active development branch:** `v1-methodological-navigation-coverage-diagnostic`  
**Active PR:** #68  
**Promoted V1 integration branch:** `v1-frontend-spike` at `0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted project/object, persistence, methodological knowledge, retrieval/Horizon/selective-context, real-reasoning, dependency-backed sequencing, Project Cockpit, runtime, governed autonomous live-experiment launch, and machine-checkable current-routing consistency seams. Specification 021 remains frozen `FAIL` evidence. Research 031 / Checkpoint 186 moved the next evaluation upstream to state-driven methodological navigation and coverage. Research 032 / Checkpoint 187 resolve the principal design choices for the first project-state-to-methodological-horizon coverage diagnostic. Specification 022 is not frozen.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** validate the Checkpoint 187 design boundary, then prospectively freeze the exact Specification 022 treatment universe, episodes, hidden oracle, representation map, runtime treatment, metrics, thresholds, seeds, and advancement gates before implementation.''',
    '''**Checkpoint:** 188  
**Date:** 2026-08-24  
**Active development branch:** `v1-methodological-navigation-coverage-diagnostic`  
**Active PR:** #68  
**Promoted V1 integration branch:** `v1-frontend-spike` at `0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted project/object, persistence, methodological knowledge, retrieval/Horizon/selective-context, real-reasoning, dependency-backed sequencing, Project Cockpit, runtime, governed autonomous live-experiment launch, and machine-checkable current-routing consistency seams. Specification 021 remains the latest completed experiment and remains frozen `FAIL` evidence. Research 031 / Checkpoint 186 moved the next evaluation upstream to state-driven methodological navigation and coverage. Research 032 / Checkpoint 187 resolved the principal design choices. Specification 022 / Checkpoint 188 now freeze the exact first project-state-to-methodological-horizon coverage diagnostic contract before implementation.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** validate the exact Checkpoint 188 frozen-contract head, then implement provider-free Specification 022 machinery and integrity tests without changing the frozen fixtures, thresholds, treatment, seed, or gates.''',
)
replace_once(
    "docs/CURRENT_STATE.md",
    '''```text
1. validate the exact Checkpoint 187 / PR #68 reconciled design head
2. prospectively author and freeze Specification 022 with exact universe, episodes, hidden oracle, representation map, runtime treatment, metrics, thresholds, seeds, and gates
3. only after that frozen contract is green, implement provider-free experiment machinery and integrity tests
4. do not authorize a provider-backed run until a later exact live-capable source is separately frozen and authorized through Specification 018
5. do not rerun the supplied-action benchmark merely to seek a SELECTIVE win
6. do not modify or rescore Specifications 015-021
```''',
    '''```text
1. validate the exact Checkpoint 188 / PR #68 frozen-contract head
2. implement provider-free Specification 022 experiment machinery and contract/integrity tests only after that head is green
3. preserve the exact frozen universe, episodes, hidden oracle, representation map, runtime treatment, metrics, thresholds, seed, and gates unchanged during implementation
4. freeze a later exact live-capable source only after provider-free cross-platform validation
5. do not authorize a provider-backed run until a separate one-shot Specification-018 authorization exists
6. do not modify or rescore Specifications 015-021
```''',
)
replace_once(
    "docs/CURRENT_STATE.md",
    "docs/checkpoints/187_project_state_methodological_coverage_design_choices_resolved.md\ndocs/research/032_project_state_to_methodological_horizon_coverage_diagnostic_design.md",
    "docs/checkpoints/188_specification_022_project_state_methodological_coverage_contract_frozen.md\ndocs/specifications/022_v1_project_state_methodological_horizon_coverage_diagnostic.md\ntests/fixtures/methodological_navigation/spec022_contract_fixture_manifest_v1.json\ndocs/checkpoints/187_project_state_methodological_coverage_design_choices_resolved.md\ndocs/research/032_project_state_to_methodological_horizon_coverage_diagnostic_design.md",
)
replace_once(
    "docs/CURRENT_STATE.md",
    "The first successor experiment class should move upstream and begin from Foundation-018-aligned evolving project state without supplying the reasoner with oracle methodological keys, explicit requested reasoning functions, or a candidate action menu. Research 032 / Checkpoint 187 now resolve the leading diagnostic design as four evolving episode families, a controlled 28-asset benchmark universe, separate hidden oracle and evaluator-only representation map, GENERIC / ADS_HORIZON / ORACLE_HORIZON conditions, matched one-call reasoner treatment, explicit catalog-gap accounting, blinded semantic matching, and reliability/noise metrics. The exact Specification 022 payloads, thresholds, runtime settings, seed, and gates remain to be frozen prospectively.",
    "The successor experiment now begins from Foundation-018-aligned evolving project state without supplying the reasoner with oracle methodological keys, explicit requested reasoning functions, or a candidate action menu. Specification 022 / Checkpoint 188 freeze four evolving episode families, 12 scored snapshots, a 28-asset controlled benchmark universe, 33 hidden oracle items, two intentional catalog gaps, an evaluator-only representation map, GENERIC / ADS_HORIZON / ORACLE_HORIZON conditions, matched one-call reasoner treatment, blinded semantic matching, exact runtime settings, seed 2026082403, MN-G01 through MN-G15 gates, and MN-P01 through MN-P05 positive signals. No provider call is authorized at this boundary."
)

replace_once(
    "docs/KNOWLEDGE_MAP.md",
    "**Current checkpoint:** 187  ",
    "**Current checkpoint:** 188  ",
)
replace_once(
    "docs/KNOWLEDGE_MAP.md",
    "Question A diagnostic design PR #68 active draft; Specification 022 not frozen",
    "Question A diagnostic PR        #68 active draft; Specification 022 contract frozen; provider-free implementation next",
)
replace_once(
    "docs/KNOWLEDGE_MAP.md",
    "Research 032 / Checkpoint 187 / PR #68\n    first project-state methodological coverage diagnostic design choices resolved; Specification 022 not frozen",
    "Research 032 / Checkpoint 187 / PR #68\n    first project-state methodological coverage diagnostic design choices resolved\n\nSpecification 022 / Checkpoint 188 / PR #68\n    exact project-state-to-methodological-horizon coverage diagnostic contract frozen before implementation or provider execution",
)
replace_once(
    "docs/KNOWLEDGE_MAP.md",
    "docs/research/032_project_state_to_methodological_horizon_coverage_diagnostic_design.md",
    "docs/research/032_project_state_to_methodological_horizon_coverage_diagnostic_design.md\ndocs/specifications/022_v1_project_state_methodological_horizon_coverage_diagnostic.md\ndocs/checkpoints/188_specification_022_project_state_methodological_coverage_contract_frozen.md",
)

routing = {
    "schema_version": 1,
    "current_checkpoint": 188,
    "active_development_branch": "v1-methodological-navigation-coverage-diagnostic",
    "active_pr": 68,
    "promoted_integration_branch": "v1-frontend-spike",
    "promoted_integration_sha": "0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e",
    "latest_specification": "022",
    "latest_experiment_outcome": "FAIL",
    "current_boundary": "spec022-contract-frozen-provider-free-implementation-next",
}
(ROOT / "docs/current_routing.json").write_text(json.dumps(routing, indent=2) + "\n", encoding="utf-8")
