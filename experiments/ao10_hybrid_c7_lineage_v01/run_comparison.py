import json
from pathlib import Path
import evaluator_a
import evaluator_b

ROOT = Path(__file__).resolve().parent

def main():
    payload = json.loads((ROOT / "fixtures.json").read_text(encoding="utf-8"))
    rows = []
    for fixture in payload["fixtures"]:
        a = evaluator_a.evaluate(fixture)
        b = evaluator_b.evaluate(fixture)
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

    all_match = all(
        row["a_matches_expected"] and row["b_matches_expected"] and row["evaluators_agree"]
        for row in rows
    )
    required_negative_ids = {
        "L7_UNMAPPED_LIVE_PREDECESSOR",
        "L8_COMPETING_OUTGOING_RELATIONS",
        "L9_CYCLE",
        "L10_UNAUTHORIZED_RELATION",
        "L11_STALE_EFFECTIVE_BOUNDARY",
        "L12_INVALID_CARRY_FORWARD_DIGEST",
    }
    negative_controls_visible = all(
        row["evaluator_a"]["review_required"]
        for row in rows
        if row["fixture_id"] in required_negative_ids
    )
    split = next(row for row in rows if row["fixture_id"] == "L3_ONE_TO_MANY_SPLIT")
    merge = next(row for row in rows if row["fixture_id"] == "L4_MANY_TO_ONE_MERGE")
    nm_targets_correct = (
        split["evaluator_a"]["current_targets_by_predecessor"] == {"P1":["S1","S2"]}
        and merge["evaluator_a"]["current_targets_by_predecessor"] == {"P1":["S1"],"P2":["S1"]}
    )
    outcome = "C7_LINEAGE_MECHANISM_PLAUSIBLE" if (
        all_match and negative_controls_visible and nm_targets_correct
    ) else "C7_AMEND"
    result = {
        "probe_id": "HYBRID_C7_LINEAGE_V01",
        "rows": rows,
        "summary": {
            "fixture_total": len(rows),
            "all_match": all_match,
            "evaluators_agree_all": all(row["evaluators_agree"] for row in rows),
            "negative_controls_visible": negative_controls_visible,
            "nm_targets_correct": nm_targets_correct,
            "outcome": outcome,
        },
    }
    (ROOT / "result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], sort_keys=True))

if __name__ == "__main__":
    main()
