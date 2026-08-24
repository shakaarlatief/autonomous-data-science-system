from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(relative: str, old: str, new: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{relative}: expected one exact anchor, found {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def append_once(relative: str, marker: str, block: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    if marker in text:
        return
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text + "\n" + block.rstrip() + "\n", encoding="utf-8")


replace_once(
    "README.md",
    """```text
checkpoint            172
active branch         v1-frontend-spike
active PR             none
promoted V1 head      a639cfc570290a2169425f43078bbb242fa398e9
current boundary      routing-consistency hardening promoted; final integration validation pending
latest experiment     Specification 020
outcome               BLOCKING_BOUNDARY_SUPPORTED
next                  require final integration routing validation,
                      then freeze a successor recommendation-value contract
```""",
    """```text
checkpoint            184
active branch         v1-spec021-negative-result-preservation
active PR             #66
promoted V1 head      a639cfc570290a2169425f43078bbb242fa398e9
current boundary      Specification 021 negative-result preservation promotion candidate
latest experiment     Specification 021
outcome               FAIL
next                  validate and merge preservation-only PR #66,
                      close rejected implementation PR #55 without merge,
                      then review methodological-navigation / coverage evaluation
```""",
)

replace_once(
    "README.md",
    """Specification 020  dependency-backed RECOMMENDED-vs-BLOCKING_REQUIRED boundary supported/promoted
Checkpoint 172     machine-checkable current-routing consistency guard green and promoted through PR #54""",
    """Specification 020  dependency-backed RECOMMENDED-vs-BLOCKING_REQUIRED boundary supported/promoted
Specification 021  complete supplied-action recommendation/disposition experiment FAIL; negative evidence preserved without implementation promotion
Checkpoint 183     clarified that supplied-action disposition calibration does not test open-world methodological navigation / coverage
Checkpoint 184     preservation-only promotion candidate for Specification 021 evidence and interpretation""",
)

replace_once(
    "README.md",
    """```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json
docs/checkpoints/172_machine_checkable_current_routing_consistency_guard_passed.md
docs/checkpoints/171_recommended_vs_blocking_required_calibration_boundary_supported.md
experiments/blocking_calibration/V1_BLOCKING_CALIBRATION_RESULT.md
```""",
    """```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json
docs/checkpoints/184_specification_021_negative_result_preservation_promotion_candidate.md
docs/checkpoints/183_specification_021_architectural_interpretation_boundary_clarified.md
docs/research/030_methodological_navigation_vs_downstream_recommendation_calibration.md
experiments/dependency_backed_recommendation_action_value/V1_DEPENDENCY_BACKED_RECOMMENDATION_ACTION_VALUE_RESULT.md
```""",
)

replace_once(
    "README.md",
    """```text
1. require current-routing consistency to pass on this routing-sensitive v1-frontend-spike reconciliation
2. close the Level-2 routing-consistency hardening boundary only if that exact integration head is green
3. then freeze a successor recommendation-value experiment
4. preserve system-owned provenance and clean relation-backed recommendation/blocking semantics
5. do not modify or rescore Specifications 015-020
```""",
    """```text
1. validate preservation-only PR #66 on its exact head
2. merge PR #66 only if the evidence/history-only boundary remains clean and green
3. close rejected Specification 021 implementation PR #55 without merge
4. reconcile v1-frontend-spike to the preserved Specification 021 FAIL boundary
5. before any Specification 022 freeze, review how to test methodological navigation / coverage from realistic evolving project state
6. do not modify or rescore Specifications 015-021
```""",
)

append_once(
    "README.md",
    "## Specification 021 interpretation boundary",
    """## Specification 021 interpretation boundary

The complete Specification 021 result is `FAIL`, but its scope is deliberately narrow. Every condition was already supplied with the explicit reasoning function, candidate action menu, requirements, downstream scopes, dependency/resolver relations, defer triggers, and sequencing relations. The experiment therefore tested downstream disposition calibration over an already-constructed decision space, not whether ADS can discover and surface the methodological option space from raw evolving project state.

Research 030 and Checkpoint 183 preserve the guardrail:

```text
methodological navigation / coverage
    !=
downstream disposition calibration over an already supplied action set
```

GENERIC remains an essential experimental control, not an architectural replacement for the methodological-navigation brain described by Foundations 006, 017, 019, 020 and Research 028.
""",
)

replace_once(
    "docs/CURRENT_STATE.md",
    """**Checkpoint:** 172  
**Date:** 2026-08-24  
**Active development branch:** `v1-frontend-spike`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `a639cfc570290a2169425f43078bbb242fa398e9`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted project/object, persistence, methodological knowledge, retrieval/Horizon/selective-context, real-reasoning, dependency-backed sequencing, Project Cockpit, runtime, governed autonomous live-experiment launch, and machine-checkable current-routing consistency seams. Specification 020 completed with `BLOCKING_BOUNDARY_SUPPORTED` and is promoted. PR #54 promoted the Level-2 routing-consistency hardening into the V1 integration branch.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** require the routing-consistency workflow to pass on this exact `v1-frontend-spike` reconciliation, then close the Level-2 hardening boundary and freeze the successor recommendation-value experiment.""",
    """**Checkpoint:** 184  
**Date:** 2026-08-24  
**Active development branch:** `v1-spec021-negative-result-preservation`  
**Active PR:** #66  
**Promoted V1 integration branch:** `v1-frontend-spike` at `a639cfc570290a2169425f43078bbb242fa398e9`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted project/object, persistence, methodological knowledge, retrieval/Horizon/selective-context, real-reasoning, dependency-backed sequencing, Project Cockpit, runtime, governed autonomous live-experiment launch, and machine-checkable current-routing consistency seams. Specification 021 completed with frozen outcome `FAIL`; its negative evidence and architectural interpretation are now in a preservation-only promotion candidate while its failed recommendation implementation remains rejected.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** validate and merge preservation-only PR #66, close rejected implementation PR #55 without merge, reconcile `v1-frontend-spike`, then perform an architecture/evaluation review of the still largely untested methodological-navigation and coverage value proposition before freezing any successor experiment.""",
)

replace_once(
    "docs/CURRENT_STATE.md",
    """    -> recommendation/blocking calibration diagnostic 020   [SUPPORTED, PROMOTED]
```""",
    """    -> recommendation/blocking calibration diagnostic 020   [SUPPORTED, PROMOTED]
    -> dependency-backed recommendation experiment 021        [FAIL, PRESERVATION ONLY]
```""",
)

replace_once(
    "docs/CURRENT_STATE.md",
    """whether explicit methodological knowledge adds recommendation/action value beyond a strong generic reasoner""",
    """whether and how methodological navigation / coverage reduces the human burden of surfacing important analytical paths across realistic evolving projects""",
)

replace_once(
    "docs/CURRENT_STATE.md",
    """```text
1. require current-routing consistency to pass on this exact v1-frontend-spike reconciliation
2. close the Level-2 routing-consistency hardening boundary only if that integration head is green
3. then freeze a successor recommendation-value contract
4. preserve system-owned provenance and clean relation-backed recommendation/blocking semantics
5. do not modify or rescore Specifications 015-020
```""",
    """```text
1. validate preservation-only PR #66 on its exact head
2. merge PR #66 only if the negative-evidence boundary remains clean and green
3. close rejected Specification 021 implementation PR #55 without merge
4. reconcile v1-frontend-spike to the preserved Specification 021 FAIL boundary
5. review architecture/evaluation for Question A: methodological navigation / coverage from realistic evolving project state
6. do not freeze Specification 022 or rerun the same supplied-action benchmark merely to seek a SELECTIVE win
7. do not modify or rescore Specifications 015-021
```""",
)

replace_once(
    "docs/CURRENT_STATE.md",
    """docs/checkpoints/171_recommended_vs_blocking_required_calibration_boundary_supported.md
docs/checkpoints/172_machine_checkable_current_routing_consistency_guard_passed.md
experiments/blocking_calibration/V1_BLOCKING_CALIBRATION_RESULT.md
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md""",
    """docs/checkpoints/184_specification_021_negative_result_preservation_promotion_candidate.md
docs/checkpoints/183_specification_021_architectural_interpretation_boundary_clarified.md
docs/research/030_methodological_navigation_vs_downstream_recommendation_calibration.md
experiments/dependency_backed_recommendation_action_value/V1_DEPENDENCY_BACKED_RECOMMENDATION_ACTION_VALUE_RESULT.md
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md""",
)

append_once(
    "docs/CURRENT_STATE.md",
    "## Specification 021 complete result and interpretation boundary",
    """## Specification 021 complete result and interpretation boundary

Specification 021 completed after the first live attempt was preserved as `INCOMPLETE` instrumentation evidence and the usage-serialization defect was repaired without changing the frozen scientific contract.

The complete replacement design produced:

```text
                         GENERIC        SELECTIVE       FULL_HORIZON
exact accuracy           1.000000       1.000000        1.000000
semantic score           0.958333       0.950000        0.950000
blocking false positives 0              0               0
pointer errors            0              0               0
```

Frozen outcome:

```text
DBRA-G08 SELECTIVE DBRA-01 semantic  0.800000 < 0.850000
positive SELECTIVE value signals     0
advancement outcome                  FAIL
```

The failed recommendation implementation is not promoted. PR #66 preserves the contract, fixture, raw evidence, stable result, research, and checkpoints only.

Research 030 / Checkpoint 183 additionally clarify that this supplied-action disposition experiment is not a test of the broader methodological-navigation and coverage capability. Question A remains largely untested end-to-end.
""",
)

replace_once(
    "docs/KNOWLEDGE_MAP.md",
    """**Current checkpoint:** 172  
**Active development branch:** `v1-frontend-spike`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `a639cfc570290a2169425f43078bbb242fa398e9`""",
    """**Current checkpoint:** 184  
**Active development branch:** `v1-spec021-negative-result-preservation`  
**Active PR:** #66  
**Promoted V1 integration branch:** `v1-frontend-spike` at `a639cfc570290a2169425f43078bbb242fa398e9`""",
)

replace_once(
    "docs/KNOWLEDGE_MAP.md",
    """routing consistency PR         #54 merged
main                           governed live-launch control plane; zero active Spec020 authorization""",
    """routing consistency PR         #54 merged
Specification 021 impl PR      #55 open but rejected for promotion; close without merge after preservation
Specification 021 preserve PR  #66 active preservation-only candidate
main                           governed live-launch control plane; zero active Specification 021 authorization""",
)

replace_once(
    "docs/KNOWLEDGE_MAP.md",
    """Checkpoint 172 / PR #54
    machine-readable current routing pointers + lightweight cross-platform contradiction validator green on exact final PR head and promoted into v1-frontend-spike""",
    """Checkpoint 172 / PR #54
    machine-readable current routing pointers + lightweight cross-platform contradiction validator green and promoted into v1-frontend-spike

Specification 021 / Checkpoints 174-182
    dependency-backed supplied-action recommendation experiment completed; frozen outcome FAIL; raw evidence and stable result preserved; failed implementation rejected

Research 030 / Checkpoint 183
    architectural interpretation clarified: methodological navigation / coverage is not equivalent to downstream disposition calibration over an already supplied action set

Checkpoint 184 / PR #66
    preservation-only promotion candidate carrying Specification 021 evidence/history without the rejected implementation""",
)

append_once(
    "docs/KNOWLEDGE_MAP.md",
    "## Specification 021 preservation and interpretation route",
    """## Specification 021 preservation and interpretation route

```text
docs/specifications/021_v1_dependency_backed_recommendation_action_value_vertical_slice.md
    frozen supplied-action experiment contract

docs/research/029_dependency_backed_recommendation_value_design.md
    prospective experiment rationale

docs/research/030_methodological_navigation_vs_downstream_recommendation_calibration.md
    architectural interpretation guardrail after the result

docs/checkpoints/182_specification_021_complete_live_result_failed.md
    frozen complete scientific FAIL boundary

docs/checkpoints/183_specification_021_architectural_interpretation_boundary_clarified.md
    Question A vs downstream disposition-calibration clarification

docs/checkpoints/184_specification_021_negative_result_preservation_promotion_candidate.md
    preservation-only promotion boundary

experiments/dependency_backed_recommendation_action_value/V1_DEPENDENCY_BACKED_RECOMMENDATION_ACTION_VALUE_RESULT.md
    stable interpreted result

experiments/dependency_backed_recommendation_action_value/results/
    immutable first incomplete and complete replacement raw evidence
```

The failed experiment implementation remains historical on PR #55 and is intentionally absent from the preservation branch.
""",
)

routing = {
    "schema_version": 1,
    "current_checkpoint": 184,
    "active_development_branch": "v1-spec021-negative-result-preservation",
    "active_pr": 66,
    "promoted_integration_branch": "v1-frontend-spike",
    "promoted_integration_sha": "a639cfc570290a2169425f43078bbb242fa398e9",
    "latest_specification": "021",
    "latest_experiment_outcome": "FAIL",
    "current_boundary": "spec021-negative-result-preservation-promotion-candidate",
}
(ROOT / "docs/current_routing.json").write_text(
    json.dumps(routing, indent=2) + "\n", encoding="utf-8"
)

append_once(
    "docs/OPEN_QUESTIONS.md",
    "## Specification 021 result: navigation value remains a distinct open question",
    """## Specification 021 result: navigation value remains a distinct open question

Specification 021 completed with frozen outcome `FAIL`, but the benchmark supplied the reasoning function, candidate actions, requirements, scopes, dependency/resolver relations, and defer relations to every condition. It therefore does not answer the system-level question of whether ADS can reduce the human burden of remembering and surfacing important methodological pathways from realistic evolving project state.

The next architecture/evaluation review should distinguish:

```text
path discovery / coverage
applicability / relevance
concrete option generation
prioritization / disposition
model-facing context value
```

Do not collapse these into one GENERIC-vs-SELECTIVE recommendation score.
""",
)

append_once(
    "docs/MAJOR_CHANGES.md",
    "## 2026-08-24: Specification 021 negative result preserved without architecture pivot",
    """## 2026-08-24: Specification 021 negative result preserved without architecture pivot

Specification 021 completed a relation-backed supplied-action recommendation/disposition experiment with frozen outcome `FAIL`. The deterministic disposition and pointer layer was perfect across GENERIC, SELECTIVE, and FULL_HORIZON, but one preregistered SELECTIVE per-case semantic floor failed and no prospectively frozen SELECTIVE recommendation-value signal was observed.

The failed recommendation implementation did not earn promotion. A preservation-only branch/PR carries the frozen contract, fixture, raw evidence, stable result, and historical checkpoints.

A subsequent architecture review clarified that the benchmark had already supplied much of the decision space and therefore did not test the broader ADS capability of discovering and surfacing methodological pathways from project state. Research 030 and Checkpoint 183 preserve that distinction. The core methodological-navigation vision remains open for direct system-level evaluation rather than being rejected on the downstream disposition result.
""",
)
