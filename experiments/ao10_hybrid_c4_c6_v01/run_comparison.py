"""Single execution harness for HYBRID_C4_C6_V01."""

import json
from pathlib import Path

import evaluator_a as a
import evaluator_b as b

ROOT = Path(__file__).resolve().parent

def main():
    granularity = json.loads((ROOT / "granularity_fixtures.json").read_text(encoding="utf-8"))
    completion = json.loads((ROOT / "completion_fixtures.json").read_text(encoding="utf-8"))

    granularity_rows = []
    for fixture in granularity["fixtures"]:
        result_a = a.evaluate_granularity(fixture)
        result_b = b.evaluate_granularity(fixture)
        granularity_rows.append({
            "fixture_id": fixture["fixture_id"],
            "expected": fixture["expected"],
            "evaluator_a": result_a,
            "evaluator_b": result_b,
            "a_matches_expected": result_a == fixture["expected"],
            "b_matches_expected": result_b == fixture["expected"],
            "evaluators_agree": result_a == result_b,
        })

    completion_rows = []
    for fixture in completion["fixtures"]:
        result_a = a.evaluate_completion(fixture)
        result_b = b.evaluate_completion(fixture)
        completion_rows.append({
            "fixture_id": fixture["fixture_id"],
            "expected": fixture["expected"],
            "evaluator_a": result_a,
            "evaluator_b": result_b,
            "a_matches_expected": result_a == fixture["expected"],
            "b_matches_expected": result_b == fixture["expected"],
            "evaluators_agree": result_a == result_b,
        })

    all_granularity = all(
        x["a_matches_expected"] and x["b_matches_expected"] and x["evaluators_agree"]
        for x in granularity_rows
    )
    all_completion = all(
        x["a_matches_expected"] and x["b_matches_expected"] and x["evaluators_agree"]
        for x in completion_rows
    )
    self_cert_case = next(
        x for x in completion_rows
        if x["fixture_id"] == "P4_SELF_CERTIFIED_FULL_MISSING_COMPONENT"
    )
    self_certification_blocked = (
        self_cert_case["evaluator_a"]["coverage_complete"] is False
        and self_cert_case["evaluator_b"]["coverage_complete"] is False
    )

    negative_visible = (
        next(x for x in granularity_rows if x["fixture_id"] == "G2_TWO_INDEPENDENT_EFFECTS_SAME_SOURCE")["evaluator_a"]["outcome"] == "SPLIT_REQUIRED"
        and next(x for x in completion_rows if x["fixture_id"] == "P5_REALIZER_SUPPLIED_CRITERION")["evaluator_a"]["review_required"]
        and next(x for x in completion_rows if x["fixture_id"] == "P7_STALE_CRITERION_REVISION")["evaluator_a"]["review_required"]
        and next(x for x in completion_rows if x["fixture_id"] == "P9_UNKNOWN_COMPONENT")["evaluator_a"]["review_required"]
    )

    outcome = "C4_C6_MECHANISM_PLAUSIBLE" if (
        all_granularity
        and all_completion
        and self_certification_blocked
        and negative_visible
    ) else "C4_C6_AMEND"

    result = {
        "probe_id": "HYBRID_C4_C6_V01",
        "granularity_rows": granularity_rows,
        "completion_rows": completion_rows,
        "summary": {
            "granularity_total": len(granularity_rows),
            "granularity_all_match": all_granularity,
            "completion_total": len(completion_rows),
            "completion_all_match": all_completion,
            "self_certification_blocked": self_certification_blocked,
            "negative_controls_visible": negative_visible,
            "evaluators_agree_all": all(
                x["evaluators_agree"] for x in granularity_rows + completion_rows
            ),
            "outcome": outcome,
        },
    }
    (ROOT / "result.json").write_text(
        json.dumps(result, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result["summary"], sort_keys=True))

if __name__ == "__main__":
    main()
