import json
from collections import Counter
from pathlib import Path
import evaluator_a
import evaluator_b

ROOT = Path(__file__).resolve().parent

def aggregate(outputs):
    states = Counter(x["state"] for x in outputs)
    gaps = Counter(x["next_gap"] for x in outputs if x["state"] == "OPEN")
    attention = sorted(x["requirement_id"] for x in outputs if x["state"] == "REVIEW_REQUIRED")
    return {
        "state_counts": dict(sorted(states.items())),
        "open_gap_counts": dict(sorted(gaps.items())),
        "attention_required_ids": attention,
    }

def main():
    payload = json.loads((ROOT / "fixtures.json").read_text(encoding="utf-8"))
    rows = []
    outputs_a = []
    outputs_b = []

    for fixture in payload["fixtures"]:
        a = evaluator_a.evaluate(fixture)
        b = evaluator_b.evaluate(fixture)
        outputs_a.append(a)
        outputs_b.append(b)
        expected = fixture["expected"]
        rows.append({
            "fixture_id": fixture["fixture_id"],
            "expected": expected,
            "evaluator_a": a,
            "evaluator_b": b,
            "a_matches_expected": a == expected,
            "b_matches_expected": b == expected,
            "evaluators_agree": a == b,
        })

    aggregate_a = aggregate(outputs_a)
    aggregate_b = aggregate(outputs_b)
    expected_aggregate = payload["expected_aggregate"]

    all_match = all(
        r["a_matches_expected"] and r["b_matches_expected"] and r["evaluators_agree"]
        for r in rows
    )
    aggregate_matches = aggregate_a == expected_aggregate and aggregate_b == expected_aggregate
    bogus = next(r for r in rows if r["fixture_id"] == "O11_BOGUS_REPORTED_OPERATIONAL")
    reported_state_ignored = (
        bogus["evaluator_a"]["state"] == "OPEN"
        and bogus["evaluator_a"]["next_gap"] == "COVERAGE"
        and bogus["evaluator_b"] == bogus["evaluator_a"]
    )

    outcome = "C8_ORIENTATION_MECHANISM_PLAUSIBLE" if (
        all_match and aggregate_matches and reported_state_ignored
    ) else "C8_AMEND"

    result = {
        "probe_id": "HYBRID_C8_ORIENTATION_V01",
        "rows": rows,
        "aggregate_expected": expected_aggregate,
        "aggregate_a": aggregate_a,
        "aggregate_b": aggregate_b,
        "summary": {
            "fixture_total": len(rows),
            "all_match": all_match,
            "evaluators_agree_all": all(r["evaluators_agree"] for r in rows),
            "aggregate_matches": aggregate_matches,
            "reported_state_ignored": reported_state_ignored,
            "outcome": outcome,
        },
    }
    (ROOT / "result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], sort_keys=True))

if __name__ == "__main__":
    main()
