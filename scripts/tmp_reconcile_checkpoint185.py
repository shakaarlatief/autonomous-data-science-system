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


replace_once(
    "README.md",
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
    """```text
checkpoint            185
active branch         v1-frontend-spike
active PR             none
promoted V1 head      ef6b45a84f43a5dfe33cf5c13351cb1235e6e661
current boundary      Specification 021 negative result preserved; architecture review ready
latest experiment     Specification 021
outcome               FAIL
next                  review methodological-navigation / coverage architecture and evaluation;
                      do not freeze Specification 022 until aligned
```""",
)

replace_once(
    "README.md",
    """Checkpoint 184     preservation-only promotion candidate for Specification 021 evidence and interpretation""",
    """Checkpoint 184     preservation-only promotion candidate for Specification 021 evidence and interpretation
Checkpoint 185     preservation merged, failed implementation closed, Question A architecture/evaluation review ready""",
)

replace_once(
    "README.md",
    """docs/checkpoints/184_specification_021_negative_result_preservation_promotion_candidate.md
docs/checkpoints/183_specification_021_architectural_interpretation_boundary_clarified.md""",
    """docs/checkpoints/185_specification_021_negative_result_preserved_and_architecture_review_ready.md
docs/checkpoints/183_specification_021_architectural_interpretation_boundary_clarified.md""",
)

replace_once(
    "README.md",
    """```text
1. validate preservation-only PR #66 on its exact head
2. merge PR #66 only if the evidence/history-only boundary remains clean and green
3. close rejected Specification 021 implementation PR #55 without merge
4. reconcile v1-frontend-spike to the preserved Specification 021 FAIL boundary
5. before any Specification 022 freeze, review how to test methodological navigation / coverage from realistic evolving project state
6. do not modify or rescore Specifications 015-021
```""",
    """```text
1. validate this exact v1-frontend-spike Checkpoint 185 reconciliation
2. perform the architecture/evaluation review of methodological navigation / coverage from realistic evolving project state
3. distinguish path discovery/coverage, applicability/relevance, option generation, prioritization/disposition, and model-facing context value
4. do not freeze Specification 022 until that review is aligned
5. do not modify or rescore Specifications 015-021
```""",
)

replace_once(
    "docs/CURRENT_STATE.md",
    """**Checkpoint:** 184  
**Date:** 2026-08-24  
**Active development branch:** `v1-spec021-negative-result-preservation`  
**Active PR:** #66  
**Promoted V1 integration branch:** `v1-frontend-spike` at `a639cfc570290a2169425f43078bbb242fa398e9`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted project/object, persistence, methodological knowledge, retrieval/Horizon/selective-context, real-reasoning, dependency-backed sequencing, Project Cockpit, runtime, governed autonomous live-experiment launch, and machine-checkable current-routing consistency seams. Specification 021 completed with frozen outcome `FAIL`; its negative evidence and architectural interpretation are now in a preservation-only promotion candidate while its failed recommendation implementation remains rejected.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** validate and merge preservation-only PR #66, close rejected implementation PR #55 without merge, reconcile `v1-frontend-spike`, then perform an architecture/evaluation review of the still largely untested methodological-navigation and coverage value proposition before freezing any successor experiment.""",
    """**Checkpoint:** 185  
**Date:** 2026-08-24  
**Active development branch:** `v1-frontend-spike`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ef6b45a84f43a5dfe33cf5c13351cb1235e6e661`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted project/object, persistence, methodological knowledge, retrieval/Horizon/selective-context, real-reasoning, dependency-backed sequencing, Project Cockpit, runtime, governed autonomous live-experiment launch, and machine-checkable current-routing consistency seams. Specification 021 completed with frozen outcome `FAIL`; its negative evidence and architectural interpretation were preserved through PR #66, while failed implementation PR #55 was closed without merge.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** perform an architecture/evaluation review of the still largely untested methodological-navigation and coverage value proposition before freezing any successor experiment.""",
)

replace_once(
    "docs/CURRENT_STATE.md",
    """```text
1. validate preservation-only PR #66 on its exact head
2. merge PR #66 only if the negative-evidence boundary remains clean and green
3. close rejected Specification 021 implementation PR #55 without merge
4. reconcile v1-frontend-spike to the preserved Specification 021 FAIL boundary
5. review architecture/evaluation for Question A: methodological navigation / coverage from realistic evolving project state
6. do not freeze Specification 022 or rerun the same supplied-action benchmark merely to seek a SELECTIVE win
7. do not modify or rescore Specifications 015-021
```""",
    """```text
1. validate this exact Checkpoint 185 v1-frontend-spike reconciliation
2. review architecture/evaluation for Question A: methodological navigation / coverage from realistic evolving project state
3. distinguish path discovery/coverage, applicability/relevance, concrete option generation, prioritization/disposition, and model-facing context value
4. do not freeze Specification 022 or rerun the same supplied-action benchmark merely to seek a SELECTIVE win
5. do not modify or rescore Specifications 015-021
```""",
)

replace_once(
    "docs/CURRENT_STATE.md",
    """docs/checkpoints/184_specification_021_negative_result_preservation_promotion_candidate.md
docs/checkpoints/183_specification_021_architectural_interpretation_boundary_clarified.md""",
    """docs/checkpoints/185_specification_021_negative_result_preserved_and_architecture_review_ready.md
docs/checkpoints/183_specification_021_architectural_interpretation_boundary_clarified.md""",
)

replace_once(
    "docs/KNOWLEDGE_MAP.md",
    """**Current checkpoint:** 184  
**Active development branch:** `v1-spec021-negative-result-preservation`  
**Active PR:** #66  
**Promoted V1 integration branch:** `v1-frontend-spike` at `a639cfc570290a2169425f43078bbb242fa398e9`""",
    """**Current checkpoint:** 185  
**Active development branch:** `v1-frontend-spike`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ef6b45a84f43a5dfe33cf5c13351cb1235e6e661`""",
)

replace_once(
    "docs/KNOWLEDGE_MAP.md",
    """Specification 021 impl PR      #55 open but rejected for promotion; close without merge after preservation
Specification 021 preserve PR  #66 active preservation-only candidate""",
    """Specification 021 impl PR      #55 closed without merge; failed implementation rejected
Specification 021 preserve PR  #66 merged at ef6b45a84f43a5dfe33cf5c13351cb1235e6e661""",
)

replace_once(
    "docs/KNOWLEDGE_MAP.md",
    """Checkpoint 184 / PR #66
    preservation-only promotion candidate carrying Specification 021 evidence/history without the rejected implementation""",
    """Checkpoint 184 / PR #66
    preservation-only promotion candidate carrying Specification 021 evidence/history without the rejected implementation

Checkpoint 185
    PR #66 merged, PR #55 closed without merge, Specification 021 FAIL preserved, and methodological-navigation / coverage architecture-evaluation review is the next legitimate boundary""",
)

routing = {
    "schema_version": 1,
    "current_checkpoint": 185,
    "active_development_branch": "v1-frontend-spike",
    "active_pr": None,
    "promoted_integration_branch": "v1-frontend-spike",
    "promoted_integration_sha": "ef6b45a84f43a5dfe33cf5c13351cb1235e6e661",
    "latest_specification": "021",
    "latest_experiment_outcome": "FAIL",
    "current_boundary": "spec021-negative-result-preserved-question-a-architecture-review-ready",
}
(ROOT / "docs/current_routing.json").write_text(json.dumps(routing, indent=2) + "\n", encoding="utf-8")
