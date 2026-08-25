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
    '''```text
checkpoint            190
active branch         v1-methodological-navigation-coverage-diagnostic
active PR             #68
promoted V1 head      0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e
current boundary      Specification 022 live-capable source frozen; separate authorization next
latest specification  Specification 022
latest experiment     Specification 021
outcome               FAIL
next                  validate the clean Checkpoint 190 head and stop before
                      any one-shot provider authorization at this boundary
```''',
)
replace_once(
    "README.md",
    "Checkpoint 189     Specification 022 provider-free implementation and integrity gate passed cross-platform; no provider call authorized",
    "Checkpoint 189     Specification 022 provider-free implementation and integrity gate passed cross-platform; no provider call authorized\nCheckpoint 190     exact Specification 022 live-capable source frozen at `cf5893d74fefa699296842b0a48326a9cb50161c`; no provider call authorized",
)
replace_once(
    "README.md",
    '''docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json
docs/checkpoints/189_specification_022_provider_free_implementation_gate_passed.md''',
    '''docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json
docs/checkpoints/190_specification_022_live_capable_source_frozen.md
docs/checkpoints/189_specification_022_provider_free_implementation_gate_passed.md''',
)

replace_once(
    "docs/CURRENT_STATE.md",
    '''**Checkpoint:** 189  
**Date:** 2026-08-24  
**Active development branch:** `v1-methodological-navigation-coverage-diagnostic`  
**Active PR:** #68  
**Promoted V1 integration branch:** `v1-frontend-spike` at `0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted project/object, persistence, methodological knowledge, retrieval/Horizon/selective-context, real-reasoning, dependency-backed sequencing, Project Cockpit, runtime, governed autonomous live-experiment launch, and machine-checkable current-routing consistency seams. Specification 021 remains the latest completed experiment and remains frozen `FAIL` evidence. Research 031 / Checkpoint 186 moved the next evaluation upstream to state-driven methodological navigation and coverage. Research 032 / Checkpoint 187 resolved the principal design choices. Specification 022 / Checkpoint 188 froze the exact first project-state-to-methodological-horizon coverage diagnostic contract before implementation. Checkpoint 189 now records a cross-platform-green provider-free implementation and integrity boundary without changing the frozen scientific contract.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** implement and validate the exact frozen FastEmbed dense-retrieval adapter plus provider-facing reasoner/judge execution path, then freeze an exact live-capable source before any separate provider authorization.''',
    '''**Checkpoint:** 190  
**Date:** 2026-08-25  
**Active development branch:** `v1-methodological-navigation-coverage-diagnostic`  
**Active PR:** #68  
**Promoted V1 integration branch:** `v1-frontend-spike` at `0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted project/object, persistence, methodological knowledge, retrieval/Horizon/selective-context, real-reasoning, dependency-backed sequencing, Project Cockpit, runtime, governed autonomous live-experiment launch, and machine-checkable current-routing consistency seams. Specification 021 remains the latest completed experiment and remains frozen `FAIL` evidence. Research 031 / Checkpoint 186 moved the next evaluation upstream to state-driven methodological navigation and coverage. Research 032 / Checkpoint 187 resolved the principal design choices. Specification 022 / Checkpoint 188 froze the exact first project-state-to-methodological-horizon coverage diagnostic contract. Checkpoint 189 closed its provider-free implementation gate. Checkpoint 190 now freezes the exact live-capable source `cf5893d74fefa699296842b0a48326a9cb50161c` at `v1-spec022-methodological-navigation-coverage-live-source`, still without provider authorization or execution.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** validate one clean post-reconciliation Checkpoint 190 head while keeping the frozen live-source ref fixed, then stop at the separate one-shot Specification-018 authorization boundary.''',
)
replace_once(
    "docs/CURRENT_STATE.md",
    '''```text
1. preserve Checkpoint 189 as the provider-free-green Specification 022 implementation boundary
2. implement the exact frozen FastEmbed 0.8.0 / BAAI/bge-small-en-v1.5 dense adapter and provider-facing reasoner/judge runner without changing the scientific contract
3. add provider-free/mocked tests for the live-capable path, including role treatment, retry accounting, blinding, and raw-before-interpretation
4. validate the exact live-capable candidate cross-platform together with all inherited V1 regressions
5. only then freeze a dedicated exact live-capable source SHA
6. do not authorize a provider-backed run until a separate one-shot Specification-018 authorization and owner launch request exist
7. do not modify or rescore Specifications 015-021
```''',
    '''```text
1. preserve Checkpoint 190 as the exact live-capable Specification 022 source boundary
2. keep `v1-spec022-methodological-navigation-coverage-live-source` fixed at `cf5893d74fefa699296842b0a48326a9cb50161c`
3. validate one clean post-reconciliation Checkpoint 190 head across Specification 022 and inherited V1 regressions
4. stop before creating a registry authorization at this boundary
5. any later provider-backed run requires a separate one-shot Specification-018 authorization and owner launch request
6. preserve the complete raw live artifact unchanged before any scientific interpretation
7. do not modify or rescore Specifications 015-021
```''',
)
replace_once(
    "docs/CURRENT_STATE.md",
    '''docs/current_routing.json
docs/checkpoints/189_specification_022_provider_free_implementation_gate_passed.md''',
    '''docs/current_routing.json
docs/checkpoints/190_specification_022_live_capable_source_frozen.md
docs/checkpoints/189_specification_022_provider_free_implementation_gate_passed.md''',
)
replace_once(
    "docs/CURRENT_STATE.md",
    "The successor experiment now begins from Foundation-018-aligned evolving project state without supplying the reasoner with oracle methodological keys, explicit requested reasoning functions, or a candidate action menu. Specification 022 / Checkpoint 188 freeze four evolving episode families, 12 scored snapshots, a 28-asset controlled benchmark universe, 33 hidden oracle items, two intentional catalog gaps, an evaluator-only representation map, GENERIC / ADS_HORIZON / ORACLE_HORIZON conditions, matched one-call reasoner treatment, blinded semantic matching, exact runtime settings, seed 2026082403, MN-G01 through MN-G15 gates, and MN-P01 through MN-P05 positive signals. Checkpoint 189 records that the provider-free contract, navigation composition, request construction, blinded-judge construction, scoring, outcome classification, retry accounting, and raw-before-interpretation safeguards are now cross-platform green at implementation head `af9ad9d39379e7e268920c307c22bf4b23780cee`. Specification 022 remains scientifically unexecuted and no provider call is authorized at this boundary.",
    "The successor experiment now begins from Foundation-018-aligned evolving project state without supplying the reasoner with oracle methodological keys, explicit requested reasoning functions, or a candidate action menu. Specification 022 / Checkpoint 188 freeze four evolving episode families, 12 scored snapshots, a 28-asset controlled benchmark universe, 33 hidden oracle items, two intentional catalog gaps, an evaluator-only representation map, GENERIC / ADS_HORIZON / ORACLE_HORIZON conditions, matched one-call reasoner treatment, blinded semantic matching, exact runtime settings, seed 2026082403, MN-G01 through MN-G15 gates, and MN-P01 through MN-P05 positive signals. Checkpoint 189 records the cross-platform-green provider-free implementation. Checkpoint 190 freezes the live-capable source `cf5893d74fefa699296842b0a48326a9cb50161c` at `v1-spec022-methodological-navigation-coverage-live-source`, including exact FastEmbed treatment, explicit two-stage blinded adjudication, full 216-call provider-free orchestration tests, and raw-before-interpretation execution safeguards. Specification 022 remains scientifically unexecuted, no registry authorization exists, and no provider call is authorized at this boundary.",
)

replace_once(
    "docs/KNOWLEDGE_MAP.md",
    "**Last reviewed:** 2026-08-24  \n**Current checkpoint:** 189  ",
    "**Last reviewed:** 2026-08-25  \n**Current checkpoint:** 190  ",
)
replace_once(
    "docs/KNOWLEDGE_MAP.md",
    "Question A diagnostic PR        #68 active draft; Specification 022 provider-free implementation green; live-capable source next\nmain                           governed live-launch control plane; zero active Specification 021 authorization",
    "Question A diagnostic PR        #68 active draft; Specification 022 live-capable source frozen; separate authorization next\nmain                           governed live-launch control plane; no active Specification 022 authorization",
)
replace_once(
    "docs/KNOWLEDGE_MAP.md",
    '''Checkpoint 189 / PR #68
    provider-free Specification 022 contract/navigation/request/scoring/artifact machinery green cross-platform; scientific outcome remains unexecuted; no provider call authorized''',
    '''Checkpoint 189 / PR #68
    provider-free Specification 022 contract/navigation/request/scoring/artifact machinery green cross-platform; scientific outcome remains unexecuted; no provider call authorized

Checkpoint 190 / PR #68
    exact live-capable source `cf5893d74fefa699296842b0a48326a9cb50161c` frozen at `v1-spec022-methodological-navigation-coverage-live-source`; separate authorization remains required before provider execution''',
)
replace_once(
    "docs/KNOWLEDGE_MAP.md",
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
    '''## Current exact continuation

```text
A. preserve Checkpoint 190 as the exact live-capable Specification 022 source boundary
B. keep `v1-spec022-methodological-navigation-coverage-live-source` fixed at `cf5893d74fefa699296842b0a48326a9cb50161c`
C. validate one clean post-reconciliation Checkpoint 190 head across Specification 022 and inherited V1 regressions
D. stop before creating a registry authorization at this boundary
E. any later provider execution requires separate one-shot Specification-018 authorization plus an owner launch request
F. preserve raw artifact bytes unchanged before live scientific interpretation
G. do not modify or rescore Specifications 015-021
```

The live-capable engineering question is closed at Checkpoint 190. The next scientific question remains Specification 022 itself, which is still unexecuted. Provider execution is a separate governed boundary rather than an automatic consequence of freezing the source.''',
)
replace_once(
    "docs/KNOWLEDGE_MAP.md",
    "189  Specification 022 provider-free implementation gate passed cross-platform; no provider call authorized",
    "189  Specification 022 provider-free implementation gate passed cross-platform; no provider call authorized\n190  Specification 022 exact live-capable source frozen; no provider authorization or call",
)

routing = {
    "schema_version": 1,
    "current_checkpoint": 190,
    "active_development_branch": "v1-methodological-navigation-coverage-diagnostic",
    "active_pr": 68,
    "promoted_integration_branch": "v1-frontend-spike",
    "promoted_integration_sha": "0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e",
    "latest_specification": "022",
    "latest_experiment_outcome": "FAIL",
    "current_boundary": "spec022-live-capable-source-frozen-separate-authorization-next",
}
(ROOT / "docs/current_routing.json").write_text(
    json.dumps(routing, indent=2) + "\n",
    encoding="utf-8",
)
