from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected exactly one anchor, found {count}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")


old_readme = '''```text
checkpoint            186
active branch         v1-methodological-navigation-coverage-review
active PR             #67
promoted V1 head      ef6b45a84f43a5dfe33cf5c13351cb1235e6e661
current boundary      Question A architecture/evaluation review completed; Specification 022 not frozen
latest experiment     Specification 021
outcome               FAIL
next                  align on Research 031 and Checkpoint 186;
                      then design Specification 022 prospectively
```'''
new_readme = '''```text
checkpoint            187
active branch         v1-methodological-navigation-coverage-diagnostic
active PR             #68
promoted V1 head      0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e
current boundary      Question A diagnostic design choices resolved; Specification 022 not frozen
latest experiment     Specification 021
outcome               FAIL
next                  validate this design boundary, then freeze the exact
                      Specification 022 contract before implementation
```'''
replace_once("README.md", old_readme, new_readme)
replace_once(
    "README.md",
    "Checkpoint 186     methodological-navigation / coverage architecture and evaluation review completed; Specification 022 not frozen",
    "Checkpoint 186     methodological-navigation / coverage architecture and evaluation review completed; Specification 022 not frozen\nCheckpoint 187     project-state methodological coverage diagnostic design choices resolved; Specification 022 still not frozen",
)

old_current_header = '''**Checkpoint:** 186  
**Date:** 2026-08-24  
**Active development branch:** `v1-methodological-navigation-coverage-review`  
**Active PR:** #67  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ef6b45a84f43a5dfe33cf5c13351cb1235e6e661`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted project/object, persistence, methodological knowledge, retrieval/Horizon/selective-context, real-reasoning, dependency-backed sequencing, Project Cockpit, runtime, governed autonomous live-experiment launch, and machine-checkable current-routing consistency seams. Specification 021 remains frozen `FAIL` evidence. Research 031 / Checkpoint 186 complete the first deliberate architecture/evaluation review of the still largely untested state-driven methodological-navigation and coverage value proposition. Specification 022 is not frozen.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** align on the Research 031 evaluation architecture and resolve the open benchmark/oracle/condition/metric design choices before prospectively freezing any successor experiment.'''
new_current_header = '''**Checkpoint:** 187  
**Date:** 2026-08-24  
**Active development branch:** `v1-methodological-navigation-coverage-diagnostic`  
**Active PR:** #68  
**Promoted V1 integration branch:** `v1-frontend-spike` at `0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted project/object, persistence, methodological knowledge, retrieval/Horizon/selective-context, real-reasoning, dependency-backed sequencing, Project Cockpit, runtime, governed autonomous live-experiment launch, and machine-checkable current-routing consistency seams. Specification 021 remains frozen `FAIL` evidence. Research 031 / Checkpoint 186 moved the next evaluation upstream to state-driven methodological navigation and coverage. Research 032 / Checkpoint 187 resolve the principal design choices for the first project-state-to-methodological-horizon coverage diagnostic. Specification 022 is not frozen.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** validate the Checkpoint 187 design boundary, then prospectively freeze the exact Specification 022 treatment universe, episodes, hidden oracle, representation map, runtime treatment, metrics, thresholds, seeds, and advancement gates before implementation.'''
replace_once("docs/CURRENT_STATE.md", old_current_header, new_current_header)

old_cont = '''```text
1. validate the Checkpoint 186 review branch and routing
2. align on Research 031's state-to-methodological-horizon architecture/evaluation decomposition
3. resolve its open project-state projection, controlled-universe, hidden-oracle, condition, semantic-matching, noise, repetition, and gate questions
4. only then prospectively freeze Specification 022
5. do not rerun the same supplied-action benchmark merely to seek a SELECTIVE win
6. do not modify or rescore Specifications 015-021
```'''
new_cont = '''```text
1. validate the exact Checkpoint 187 / PR #68 reconciled design head
2. prospectively author and freeze Specification 022 with exact universe, episodes, hidden oracle, representation map, runtime treatment, metrics, thresholds, seeds, and gates
3. only after that frozen contract is green, implement provider-free experiment machinery and integrity tests
4. do not authorize a provider-backed run until a later exact live-capable source is separately frozen and authorized through Specification 018
5. do not rerun the supplied-action benchmark merely to seek a SELECTIVE win
6. do not modify or rescore Specifications 015-021
```'''
replace_once("docs/CURRENT_STATE.md", old_cont, new_cont)

replace_once(
    "docs/CURRENT_STATE.md",
    "docs/checkpoints/186_methodological_navigation_coverage_review_completed.md\ndocs/research/031_methodological_navigation_coverage_architecture_and_evaluation_review.md",
    "docs/checkpoints/187_project_state_methodological_coverage_design_choices_resolved.md\ndocs/research/032_project_state_to_methodological_horizon_coverage_diagnostic_design.md\ndocs/checkpoints/186_methodological_navigation_coverage_review_completed.md\ndocs/research/031_methodological_navigation_coverage_architecture_and_evaluation_review.md",
)
replace_once(
    "docs/CURRENT_STATE.md",
    "The first successor experiment class should move upstream and begin from Foundation-018-aligned evolving project state without supplying the reasoner with oracle methodological keys, explicit requested reasoning functions, or a candidate action menu. The leading candidate is a bounded project-state-to-methodological-horizon coverage diagnostic focused on Layers A and B. The exact Specification 022 contract remains open.",
    "The first successor experiment class should move upstream and begin from Foundation-018-aligned evolving project state without supplying the reasoner with oracle methodological keys, explicit requested reasoning functions, or a candidate action menu. Research 032 / Checkpoint 187 now resolve the leading diagnostic design as four evolving episode families, a controlled 28-asset benchmark universe, separate hidden oracle and evaluator-only representation map, GENERIC / ADS_HORIZON / ORACLE_HORIZON conditions, matched one-call reasoner treatment, explicit catalog-gap accounting, blinded semantic matching, and reliability/noise metrics. The exact Specification 022 payloads, thresholds, runtime settings, seed, and gates remain to be frozen prospectively."
)

old_km_header = '''**Current checkpoint:** 186  
**Active development branch:** `v1-methodological-navigation-coverage-review`  
**Active PR:** #67  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ef6b45a84f43a5dfe33cf5c13351cb1235e6e661`'''
new_km_header = '''**Current checkpoint:** 187  
**Active development branch:** `v1-methodological-navigation-coverage-diagnostic`  
**Active PR:** #68  
**Promoted V1 integration branch:** `v1-frontend-spike` at `0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e`'''
replace_once("docs/KNOWLEDGE_MAP.md", old_km_header, new_km_header)
replace_once(
    "docs/KNOWLEDGE_MAP.md",
    '''promoted integration head      a639cfc570290a2169425f43078bbb242fa398e9
active branch                  v1-methodological-navigation-coverage-review
active PR                      #67''',
    '''promoted integration head      0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e
active branch                  v1-methodological-navigation-coverage-diagnostic
active PR                      #68''',
)
replace_once(
    "docs/KNOWLEDGE_MAP.md",
    "Question A architecture PR     #67 active draft review; Specification 022 not frozen",
    "Question A architecture PR     #67 merged at 0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e\nQuestion A diagnostic design PR #68 active draft; Specification 022 not frozen",
)
replace_once(
    "docs/KNOWLEDGE_MAP.md",
    "Research 031 / Checkpoint 186 / PR #67\n    state-driven methodological-navigation / coverage architecture and evaluation review completed; successor experiment class identified; Specification 022 not frozen",
    "Research 031 / Checkpoint 186 / PR #67\n    state-driven methodological-navigation / coverage architecture and evaluation review completed and promoted through PR #67\n\nResearch 032 / Checkpoint 187 / PR #68\n    first project-state methodological coverage diagnostic design choices resolved; Specification 022 not frozen",
)
replace_once(
    "docs/KNOWLEDGE_MAP.md",
    "docs/research/031_methodological_navigation_coverage_architecture_and_evaluation_review.md",
    "docs/research/031_methodological_navigation_coverage_architecture_and_evaluation_review.md\ndocs/research/032_project_state_to_methodological_horizon_coverage_diagnostic_design.md",
)

routing = {
    "schema_version": 1,
    "current_checkpoint": 187,
    "active_development_branch": "v1-methodological-navigation-coverage-diagnostic",
    "active_pr": 68,
    "promoted_integration_branch": "v1-frontend-spike",
    "promoted_integration_sha": "0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e",
    "latest_specification": "021",
    "latest_experiment_outcome": "FAIL",
    "current_boundary": "question-a-diagnostic-design-resolved-spec022-not-frozen",
}
(ROOT / "docs/current_routing.json").write_text(json.dumps(routing, indent=2) + "\n", encoding="utf-8")
