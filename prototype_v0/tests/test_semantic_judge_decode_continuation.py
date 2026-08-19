from __future__ import annotations

from ads_v0 import semantic_judge_decode as decode


def _group(*, targeted: float, strong: int, critical: int, completed: int, exhausted: int, tokens: float = 100.0):
    return {
        "n": 10,
        "semantic_mean": {f"S{i}": 1.0 for i in range(1, 11)},
        "targeted_architecture_mean": targeted,
        "strong_targeted_pass_count": strong,
        "semantic_critical_SC1_count": 0,
        "semantic_critical_SC2_count": 0,
        "critical_failure_runs": critical,
        "critical_failure_events": critical,
        "completed_count": completed,
        "completed_within_budget_count": completed,
        "budget_exhausted_count": exhausted,
        "final_report_count": completed,
        "resource_medians": {
            "total_tokens": tokens,
            "model_calls": 10.0,
            "python_execution_attempts": 4.0,
        },
        "resource_means": {
            "total_tokens": tokens,
            "model_calls": 10.0,
            "python_execution_attempts": 4.0,
        },
    }


def test_material_reliability_is_registered_A_or_B_not_A_and_B() -> None:
    b0 = _group(targeted=1.0, strong=0, critical=0, completed=10, exhausted=0)
    b1 = _group(targeted=1.5, strong=0, critical=2, completed=10, exhausted=0)
    # P0 passes branch A by having two fewer critical failures, but does not pass
    # branch B because its targeted score does not exceed B1 by 0.30.
    p0 = _group(targeted=1.5, strong=0, critical=0, completed=10, exhausted=0)
    summaries = {
        "pooled": {"B0": b0, "B1": b1, "P0": p0},
        "by_variant": {
            "H1": {"B0": b0, "B1": b1, "P0": p0},
            "H2": {"B0": b0, "B1": b1, "P0": p0},
        },
    }

    result = decode._registered_comparison_facts(summaries)
    details = result["continuation_component_details_resolved_from_common_evidence"]
    mandatory = result["continuation_mandatory_resolved_components"]

    assert details["material_reliability_A"] is True
    assert details["material_reliability_B"] is False
    assert details["material_reliability_A_or_B"] is True
    assert mandatory["material_reliability_A_or_B"] is True
    assert result["continuation_signal_already_impossible_from_resolved_components"] is False
