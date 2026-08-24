from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected exactly one anchor, found {count}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


replace_once(
    "README.md",
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
    '''```text
checkpoint            189
active branch         v1-methodological-navigation-coverage-diagnostic
active PR             #68
promoted V1 head      0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e
current boundary      Specification 022 provider-free implementation gate passed; live-capable source next
latest specification  Specification 022
latest experiment     Specification 021
outcome               FAIL
next                  implement and validate the exact frozen dense/runtime
                      live-capable path; do not authorize provider execution yet
```''',
)
replace_once(
    "README.md",
    "Checkpoint 188     exact Specification 022 fixtures, runtime treatment, metrics, thresholds, seed, and gates frozen; no provider call authorized",
    "Checkpoint 188     exact Specification 022 fixtures, runtime treatment, metrics, thresholds, seed, and gates frozen; no provider call authorized\nCheckpoint 189     Specification 022 provider-free implementation and integrity gate passed cross-platform; no provider call authorized",
)
replace_once(
    "README.md",
    '''docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json
docs/checkpoints/186_methodological_navigation_coverage_review_completed.md''',
    '''docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json
docs/checkpoints/189_specification_022_provider_free_implementation_gate_passed.md
docs/checkpoints/188_specification_022_project_state_methodological_coverage_contract_frozen.md
docs/specifications/022_v1_project_state_methodological_horizon_coverage_diagnostic.md
docs/research/032_project_state_to_methodological_horizon_coverage_diagnostic_design.md
docs/checkpoints/186_methodological_navigation_coverage_review_completed.md''',
)

replace_once(
    "docs/CURRENT_STATE.md",
    '''**Checkpoint:** 188  
**Date:** 2026-08-24  
**Active development branch:** `v1-methodological-navigation-coverage-diagnostic`  
**Active PR:** #68  
**Promoted V1 integration branch:** `v1-frontend-spike` at `0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted project/object, persistence, methodological knowledge, retrieval/Horizon/selective-context, real-reasoning, dependency-backed sequencing, Project Cockpit, runtime, governed autonomous live-experiment launch, and machine-checkable current-routing consistency seams. Specification 021 remains the latest completed experiment and remains frozen `FAIL` evidence. Research 031 / Checkpoint 186 moved the next evaluation upstream to state-driven methodological navigation and coverage. Research 032 / Checkpoint 187 resolved the principal design choices. Specification 022 / Checkpoint 188 now freeze the exact first project-state-to-methodological-horizon coverage diagnostic contract before implementation.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** validate the exact Checkpoint 188 frozen-contract head, then implement provider-free Specification 022 machinery and integrity tests without changing the frozen fixtures, thresholds, treatment, seed, or gates.''',
    '''**Checkpoint:** 189  
**Date:** 2026-08-24  
**Active development branch:** `v1-methodological-navigation-coverage-diagnostic`  
**Active PR:** #68  
**Promoted V1 integration branch:** `v1-frontend-spike` at `0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted project/object, persistence, methodological knowledge, retrieval/Horizon/selective-context, real-reasoning, dependency-backed sequencing, Project Cockpit, runtime, governed autonomous live-experiment launch, and machine-checkable current-routing consistency seams. Specification 021 remains the latest completed experiment and remains frozen `FAIL` evidence. Research 031 / Checkpoint 186 moved the next evaluation upstream to state-driven methodological navigation and coverage. Research 032 / Checkpoint 187 resolved the principal design choices. Specification 022 / Checkpoint 188 froze the exact first project-state-to-methodological-horizon coverage diagnostic contract before implementation. Checkpoint 189 now records a cross-platform-green provider-free implementation and integrity boundary without changing the frozen scientific contract.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** implement and validate the exact frozen FastEmbed dense-retrieval adapter plus provider-facing reasoner/judge execution path, then freeze an exact live-capable source before any separate provider authorization.''',
)
replace_once(
    "docs/CURRENT_STATE.md",
    '''```text
1. validate the exact Checkpoint 188 / PR #68 frozen-contract head
2. implement provider-free Specification 022 experiment machinery and contract/integrity tests only after that head is green
3. preserve the exact frozen universe, episodes, hidden oracle, representation map, runtime treatment, metrics, thresholds, seed, and gates unchanged during implementation
4. freeze a later exact live-capable source only after provider-free cross-platform validation
5. do not authorize a provider-backed run until a separate one-shot Specification-018 authorization exists
6. do not modify or rescore Specifications 015-021
```''',
    '''```text
1. preserve Checkpoint 189 as the provider-free-green Specification 022 implementation boundary
2. implement the exact frozen FastEmbed 0.8.0 / BAAI/bge-small-en-v1.5 dense adapter and provider-facing reasoner/judge runner without changing the scientific contract
3. add provider-free/mocked tests for the live-capable path, including role treatment, retry accounting, blinding, and raw-before-interpretation
4. validate the exact live-capable candidate cross-platform together with all inherited V1 regressions
5. only then freeze a dedicated exact live-capable source SHA
6. do not authorize a provider-backed run until a separate one-shot Specification-018 authorization and owner launch request exist
7. do not modify or rescore Specifications 015-021
```''',
)
replace_once(
    "docs/CURRENT_STATE.md",
    '''docs/current_routing.json
docs/checkpoints/188_specification_022_project_state_methodological_coverage_contract_frozen.md''',
    '''docs/current_routing.json
docs/checkpoints/189_specification_022_provider_free_implementation_gate_passed.md
docs/checkpoints/188_specification_022_project_state_methodological_coverage_contract_frozen.md''',
)
replace_once(
    "docs/CURRENT_STATE.md",
    "The successor experiment now begins from Foundation-018-aligned evolving project state without supplying the reasoner with oracle methodological keys, explicit requested reasoning functions, or a candidate action menu. Specification 022 / Checkpoint 188 freeze four evolving episode families, 12 scored snapshots, a 28-asset controlled benchmark universe, 33 hidden oracle items, two intentional catalog gaps, an evaluator-only representation map, GENERIC / ADS_HORIZON / ORACLE_HORIZON conditions, matched one-call reasoner treatment, blinded semantic matching, exact runtime settings, seed 2026082403, MN-G01 through MN-G15 gates, and MN-P01 through MN-P05 positive signals. No provider call is authorized at this boundary.",
    "The successor experiment now begins from Foundation-018-aligned evolving project state without supplying the reasoner with oracle methodological keys, explicit requested reasoning functions, or a candidate action menu. Specification 022 / Checkpoint 188 freeze four evolving episode families, 12 scored snapshots, a 28-asset controlled benchmark universe, 33 hidden oracle items, two intentional catalog gaps, an evaluator-only representation map, GENERIC / ADS_HORIZON / ORACLE_HORIZON conditions, matched one-call reasoner treatment, blinded semantic matching, exact runtime settings, seed 2026082403, MN-G01 through MN-G15 gates, and MN-P01 through MN-P05 positive signals. Checkpoint 189 records that the provider-free contract, navigation composition, request construction, blinded-judge construction, scoring, outcome classification, retry accounting, and raw-before-interpretation safeguards are now cross-platform green at implementation head `af9ad9d39379e7e268920c307c22bf4b23780cee`. Specification 022 remains scientifically unexecuted and no provider call is authorized at this boundary.",
)

replace_once(
    "docs/KNOWLEDGE_MAP.md",
    "**Current checkpoint:** 188  ",
    "**Current checkpoint:** 189  ",
)
replace_once(
    "docs/KNOWLEDGE_MAP.md",
    "Question A diagnostic PR        #68 active draft; Specification 022 contract frozen; provider-free implementation next",
    "Question A diagnostic PR        #68 active draft; Specification 022 provider-free implementation green; live-capable source next",
)
replace_once(
    "docs/KNOWLEDGE_MAP.md",
    '''Specification 022 / Checkpoint 188 / PR #68
    exact project-state-to-methodological-horizon coverage diagnostic contract frozen before implementation or provider execution''',
    '''Specification 022 / Checkpoint 188 / PR #68
    exact project-state-to-methodological-horizon coverage diagnostic contract frozen before implementation or provider execution

Checkpoint 189 / PR #68
    provider-free Specification 022 contract/navigation/request/scoring/artifact machinery green cross-platform; scientific outcome remains unexecuted; no provider call authorized''',
)
replace_once(
    "docs/KNOWLEDGE_MAP.md",
    '''## Current exact continuation

```text
A. require current-routing consistency to pass on this exact v1-frontend-spike reconciliation
B. close the Level-2 routing-consistency hardening boundary only if that integration head is green
C. only then freeze a successor recommendation-value experiment
D. preserve system-owned provenance and clean relation-backed recommendation/blocking semantics
E. do not modify or rescore Specifications 015-020
```

The next scientific question remains whether selective explicit methodological knowledge improves recommendation/action quality beyond a strong generic reasoner when relation-backed semantics are cleanly constructed.''',
    '''## Current exact continuation

```text
A. preserve Checkpoint 189 as the provider-free-green Specification 022 implementation boundary
B. implement the exact frozen FastEmbed dense adapter and provider-facing reasoner/judge execution path without changing Specification 022 science
C. validate that live-capable path provider-free/mocked and cross-platform, including blinding, retry accounting, and raw-before-interpretation
D. freeze a dedicated exact live-capable source only after those checks pass
E. require separate one-shot Specification-018 authorization and owner launch request before any provider execution
F. do not modify or rescore Specifications 015-021
```

The next engineering question is whether the exact frozen Specification 022 treatment can be made live-capable without changing the prospectively frozen benchmark or compromising evaluator separation. The next scientific question remains Specification 022 itself and is still unexecuted.''',
)
replace_once(
    "docs/KNOWLEDGE_MAP.md",
    '''171  Specification 020 live diagnostic completed; BLOCKING_BOUNDARY_SUPPORTED
172  machine-checkable current-routing consistency guard passed; promoted through PR #54, final integration reconciliation pending validation''',
    '''171  Specification 020 live diagnostic completed; BLOCKING_BOUNDARY_SUPPORTED
172  machine-checkable current-routing consistency guard passed and promoted through PR #54
183  supplied-action disposition calibration separated explicitly from open-world methodological navigation / coverage
186  Question A methodological-navigation architecture/evaluation review completed and promoted through PR #67
187  first project-state methodological coverage diagnostic design choices resolved
188  Specification 022 exact scientific contract and fixtures frozen before implementation
189  Specification 022 provider-free implementation gate passed cross-platform; no provider call authorized''',
)

routing = {
    "schema_version": 1,
    "current_checkpoint": 189,
    "active_development_branch": "v1-methodological-navigation-coverage-diagnostic",
    "active_pr": 68,
    "promoted_integration_branch": "v1-frontend-spike",
    "promoted_integration_sha": "0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e",
    "latest_specification": "022",
    "latest_experiment_outcome": "FAIL",
    "current_boundary": "spec022-provider-free-implementation-green-live-capable-source-next",
}
(ROOT / "docs/current_routing.json").write_text(
    json.dumps(routing, indent=2) + "\n",
    encoding="utf-8",
)
