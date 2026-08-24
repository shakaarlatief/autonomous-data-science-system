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


def append_once(relative: str, marker: str, addition: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    if marker in text:
        return
    path.write_text(text.rstrip() + "\n\n" + addition.rstrip() + "\n", encoding="utf-8")


replace_once(
    "README.md",
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
    """```text
checkpoint            186
active branch         v1-methodological-navigation-coverage-review
active PR             #67
promoted V1 head      ef6b45a84f43a5dfe33cf5c13351cb1235e6e661
current boundary      Question A architecture/evaluation review completed; Specification 022 not frozen
latest experiment     Specification 021
outcome               FAIL
next                  align on Research 031 and Checkpoint 186;
                      then design Specification 022 prospectively
```""",
)

replace_once(
    "README.md",
    """Checkpoint 185     preservation merged, failed implementation closed, Question A architecture/evaluation review ready""",
    """Checkpoint 185     preservation merged, failed implementation closed, Question A architecture/evaluation review ready
Checkpoint 186     methodological-navigation / coverage architecture and evaluation review completed; Specification 022 not frozen""",
)

replace_once(
    "README.md",
    """docs/checkpoints/185_specification_021_negative_result_preserved_and_architecture_review_ready.md
docs/checkpoints/183_specification_021_architectural_interpretation_boundary_clarified.md
docs/research/030_methodological_navigation_vs_downstream_recommendation_calibration.md""",
    """docs/checkpoints/186_methodological_navigation_coverage_review_completed.md
docs/research/031_methodological_navigation_coverage_architecture_and_evaluation_review.md
docs/checkpoints/185_specification_021_negative_result_preserved_and_architecture_review_ready.md
docs/research/030_methodological_navigation_vs_downstream_recommendation_calibration.md""",
)

replace_once(
    "README.md",
    """```text
1. validate this exact v1-frontend-spike Checkpoint 185 reconciliation
2. perform the architecture/evaluation review of methodological navigation / coverage from realistic evolving project state
3. distinguish path discovery/coverage, applicability/relevance, option generation, prioritization/disposition, and model-facing context value
4. do not freeze Specification 022 until that review is aligned
5. do not modify or rescore Specifications 015-021
```""",
    """```text
1. validate the Checkpoint 186 review branch and canonical routing
2. align on Research 031's state-to-methodological-horizon evaluation architecture
3. resolve the still-open benchmark/oracle/condition/metric design questions recorded there
4. only then prospectively freeze Specification 022
5. do not rerun the supplied-action benchmark merely to seek a SELECTIVE win
6. do not modify or rescore Specifications 015-021
```""",
)

append_once(
    "README.md",
    "## Methodological navigation coverage review",
    """## Methodological navigation coverage review

Research 031 and Checkpoint 186 move the successor evaluation boundary upstream from supplied-action disposition calibration.

The recommended decomposition is:

```text
UNIVERSE COVERAGE
    -> NAVIGATION / PATH COVERAGE
    -> APPLICABILITY / MISSING CONTEXT
    -> CONCRETE OPTION GENERATION
    -> PRIORITIZATION / DISPOSITION
    -> MODEL-FACING CONTEXT VALUE
```

A methodological-universe gap, a navigation gap, and a downstream reasoning/use gap are separate failure classes. The proposed first successor experiment class is a bounded project-state-to-methodological-horizon coverage diagnostic focused primarily on path discovery and applicability/missing-context handling. Specification 022 is not frozen.""",
)

replace_once(
    "docs/CURRENT_STATE.md",
    """**Checkpoint:** 185  
**Date:** 2026-08-24  
**Active development branch:** `v1-frontend-spike`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ef6b45a84f43a5dfe33cf5c13351cb1235e6e661`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted project/object, persistence, methodological knowledge, retrieval/Horizon/selective-context, real-reasoning, dependency-backed sequencing, Project Cockpit, runtime, governed autonomous live-experiment launch, and machine-checkable current-routing consistency seams. Specification 021 completed with frozen outcome `FAIL`; its negative evidence and architectural interpretation were preserved through PR #66, while failed implementation PR #55 was closed without merge.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** perform an architecture/evaluation review of the still largely untested methodological-navigation and coverage value proposition before freezing any successor experiment.""",
    """**Checkpoint:** 186  
**Date:** 2026-08-24  
**Active development branch:** `v1-methodological-navigation-coverage-review`  
**Active PR:** #67  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ef6b45a84f43a5dfe33cf5c13351cb1235e6e661`  
**Development stage:** Prototype V0 complete; bounded V1 has accepted project/object, persistence, methodological knowledge, retrieval/Horizon/selective-context, real-reasoning, dependency-backed sequencing, Project Cockpit, runtime, governed autonomous live-experiment launch, and machine-checkable current-routing consistency seams. Specification 021 remains frozen `FAIL` evidence. Research 031 / Checkpoint 186 complete the first deliberate architecture/evaluation review of the still largely untested state-driven methodological-navigation and coverage value proposition. Specification 022 is not frozen.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** align on the Research 031 evaluation architecture and resolve the open benchmark/oracle/condition/metric design choices before prospectively freezing any successor experiment.""",
)

replace_once(
    "docs/CURRENT_STATE.md",
    """```text
1. validate this exact Checkpoint 185 v1-frontend-spike reconciliation
2. review architecture/evaluation for Question A: methodological navigation / coverage from realistic evolving project state
3. distinguish path discovery/coverage, applicability/relevance, concrete option generation, prioritization/disposition, and model-facing context value
4. do not freeze Specification 022 or rerun the same supplied-action benchmark merely to seek a SELECTIVE win
5. do not modify or rescore Specifications 015-021
```""",
    """```text
1. validate the Checkpoint 186 review branch and routing
2. align on Research 031's state-to-methodological-horizon architecture/evaluation decomposition
3. resolve its open project-state projection, controlled-universe, hidden-oracle, condition, semantic-matching, noise, repetition, and gate questions
4. only then prospectively freeze Specification 022
5. do not rerun the same supplied-action benchmark merely to seek a SELECTIVE win
6. do not modify or rescore Specifications 015-021
```""",
)

replace_once(
    "docs/CURRENT_STATE.md",
    """docs/checkpoints/185_specification_021_negative_result_preserved_and_architecture_review_ready.md
docs/checkpoints/183_specification_021_architectural_interpretation_boundary_clarified.md
docs/research/030_methodological_navigation_vs_downstream_recommendation_calibration.md""",
    """docs/checkpoints/186_methodological_navigation_coverage_review_completed.md
docs/research/031_methodological_navigation_coverage_architecture_and_evaluation_review.md
docs/checkpoints/185_specification_021_negative_result_preserved_and_architecture_review_ready.md
docs/research/030_methodological_navigation_vs_downstream_recommendation_calibration.md""",
)

append_once(
    "docs/CURRENT_STATE.md",
    "## Question A architecture/evaluation review",
    """## Question A architecture/evaluation review

Research 031 establishes the next evaluation decomposition:

```text
UNIVERSE COVERAGE
    -> NAVIGATION / PATH COVERAGE
    -> APPLICABILITY / MISSING CONTEXT
    -> CONCRETE OPTION GENERATION
    -> PRIORITIZATION / DISPOSITION
    -> MODEL-FACING CONTEXT VALUE
```

The first successor experiment class should move upstream and begin from Foundation-018-aligned evolving project state without supplying the reasoner with oracle methodological keys, explicit requested reasoning functions, or a candidate action menu. The leading candidate is a bounded project-state-to-methodological-horizon coverage diagnostic focused on Layers A and B. The exact Specification 022 contract remains open.""",
)

replace_once(
    "docs/KNOWLEDGE_MAP.md",
    """**Current checkpoint:** 185  
**Active development branch:** `v1-frontend-spike`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ef6b45a84f43a5dfe33cf5c13351cb1235e6e661`""",
    """**Current checkpoint:** 186  
**Active development branch:** `v1-methodological-navigation-coverage-review`  
**Active PR:** #67  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ef6b45a84f43a5dfe33cf5c13351cb1235e6e661`""",
)

replace_once(
    "docs/KNOWLEDGE_MAP.md",
    """active branch                  v1-frontend-spike
active PR                      none""",
    """active branch                  v1-methodological-navigation-coverage-review
active PR                      #67""",
)

replace_once(
    "docs/KNOWLEDGE_MAP.md",
    """Specification 021 preserve PR  #66 merged at ef6b45a84f43a5dfe33cf5c13351cb1235e6e661
main                           governed live-launch control plane; zero active Specification 021 authorization""",
    """Specification 021 preserve PR  #66 merged at ef6b45a84f43a5dfe33cf5c13351cb1235e6e661
Question A architecture PR     #67 active draft review; Specification 022 not frozen
main                           governed live-launch control plane; zero active Specification 021 authorization""",
)

replace_once(
    "docs/KNOWLEDGE_MAP.md",
    """Checkpoint 185
    PR #66 merged, PR #55 closed without merge, Specification 021 FAIL preserved, and methodological-navigation / coverage architecture-evaluation review is the next legitimate boundary
```""",
    """Checkpoint 185
    PR #66 merged, PR #55 closed without merge, Specification 021 FAIL preserved, and methodological-navigation / coverage architecture-evaluation review is the next legitimate boundary

Research 031 / Checkpoint 186 / PR #67
    state-driven methodological-navigation / coverage architecture and evaluation review completed; successor experiment class identified; Specification 022 not frozen
```""",
)

replace_once(
    "docs/KNOWLEDGE_MAP.md",
    """docs/research/028_system_identity_methodological_navigation_and_knowledge_universe_construction.md
```""",
    """docs/research/028_system_identity_methodological_navigation_and_knowledge_universe_construction.md
docs/research/030_methodological_navigation_vs_downstream_recommendation_calibration.md
docs/research/031_methodological_navigation_coverage_architecture_and_evaluation_review.md
```""",
)

append_once(
    "docs/OPEN_QUESTIONS.md",
    "## Checkpoint 186 methodological-navigation coverage reconciliation",
    """## Checkpoint 186 methodological-navigation coverage reconciliation

Research 031 sharpens Q-005, Q-006, Q-037, Q-044, and Q-045 without resolving them.

The next evaluation boundary separates:

```text
universe coverage
navigation / path coverage
applicability / missing context
concrete option generation
prioritization / disposition
model-facing context value
```

A methodological-universe gap, a navigation gap, and a downstream reasoning/use gap are distinct failure classes. The leading successor experiment class is a project-state-to-methodological-horizon coverage diagnostic using evolving Foundation-018-aligned state and withholding explicit reasoning-function/action menus from the main reasoner. Exact Specification 022 cases, universe size, oracle, conditions, semantic matching, metrics, thresholds, and advancement outcomes remain open.""",
)

append_once(
    "docs/MAJOR_CHANGES.md",
    "## 2026-08-24: Question A methodological-navigation coverage review",
    """## 2026-08-24: Question A methodological-navigation coverage review

Research 031 and Checkpoint 186 move the next evaluation boundary upstream from supplied-action recommendation calibration to state-driven methodological path discovery and coverage. The review distinguishes universe gaps, navigation gaps, and downstream reasoning/use gaps; recommends evolving project-state episodes with a hidden coverage oracle; preserves a strong generic control and open-world escape hatch; and identifies a project-state-to-methodological-horizon coverage diagnostic as the leading successor experiment class. Specification 022 remains not frozen.""",
)

routing = {
    "schema_version": 1,
    "current_checkpoint": 186,
    "active_development_branch": "v1-methodological-navigation-coverage-review",
    "active_pr": 67,
    "promoted_integration_branch": "v1-frontend-spike",
    "promoted_integration_sha": "ef6b45a84f43a5dfe33cf5c13351cb1235e6e661",
    "latest_specification": "021",
    "latest_experiment_outcome": "FAIL",
    "current_boundary": "question-a-architecture-review-completed-spec022-not-frozen",
}
(ROOT / "docs/current_routing.json").write_text(json.dumps(routing, indent=2) + "\n", encoding="utf-8")
