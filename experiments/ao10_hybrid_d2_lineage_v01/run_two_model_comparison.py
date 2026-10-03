import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def semantic_view(obj):
    return {k: v for k, v in obj.items() if k != "reason_codes"}

def main():
    fixtures = json.loads((ROOT / "reviewer_fixtures.json").read_text(encoding="utf-8"))["fixtures"]
    key_rows = json.loads((ROOT / "evaluator_key.json").read_text(encoding="utf-8"))["expected"]
    key = {row["fixture_id"]: row for row in key_rows}

    evaluator_a = load_module("evaluator_chatgpt_a", ROOT / "evaluator_chatgpt_a.py")
    evaluator_b = load_module("evaluator_claude_b", ROOT / "evaluator_claude_b.py")

    rows = []
    for fixture in fixtures:
        fid = fixture["fixture_id"]
        expected = key[fid]
        a = evaluator_a.evaluate_fixture(fixture)
        b = evaluator_b.evaluate_fixture(fixture)

        a_sem = semantic_view(a)
        b_sem = semantic_view(b)
        key_sem = semantic_view(expected)

        rows.append({
            "fixture_id": fid,
            "expected": expected,
            "evaluator_a": a,
            "evaluator_b": b,
            "semantic": {
                "a_matches_key": a_sem == key_sem,
                "b_matches_key": b_sem == key_sem,
                "a_b_agree": a_sem == b_sem,
            },
            "full_object_diagnostic": {
                "a_matches_key": a == expected,
                "b_matches_key": b == expected,
                "a_b_agree": a == b,
            },
        })

    semantic_all = all(
        row["semantic"]["a_matches_key"]
        and row["semantic"]["b_matches_key"]
        and row["semantic"]["a_b_agree"]
        for row in rows
    )

    full_a_key = sum(row["full_object_diagnostic"]["a_matches_key"] for row in rows)
    full_b_key = sum(row["full_object_diagnostic"]["b_matches_key"] for row in rows)
    full_ab = sum(row["full_object_diagnostic"]["a_b_agree"] for row in rows)

    required_semantic = {
        "F01_CROSSING_REPARTITION_SYNC": lambda x: x["relation_valid"] and x["current_effect_ids"] == ["S1", "S2"],
        "F02_CROSSING_REPARTITION_STAGGERED_INVALID": lambda x: (not x["relation_valid"]) and x["review_required"],
        "F03_DISJOINT_REPARTITION_STAGED_VALID": lambda x: x["relation_valid"] and x["current_effect_ids"] == ["P2", "S1"],
        "F06_REINSTATE_NEW_ID": lambda x: x["relation_valid"] and x["current_effect_ids"] == ["R1"] and x["successor_initialization"][0]["mode"] == "OPEN_RESET",
        "F07_REINSTATE_REUSES_ID_INVALID": lambda x: (not x["relation_valid"]) and x["review_required"],
        "F08_REPLACE_DEFAULT_OPEN_RESET": lambda x: x["successor_initialization"][0]["mode"] == "OPEN_RESET",
        "F09_REPLACE_VALID_REALIZATION_CARRY": lambda x: x["successor_initialization"][0]["mode"] == "CARRY_FACTS_FOR_REVALIDATION",
        "F10_REPLACE_STALE_CARRY_FACTS": lambda x: x["relation_valid"] and x["review_required"] and x["successor_initialization"][0]["mode"] == "OPEN_RESET",
        "F11_REPLACE_INVALID_CARRY_AUTHORITY": lambda x: x["relation_valid"] and x["review_required"] and x["successor_initialization"][0]["mode"] == "OPEN_RESET",
        "F12_DEFERRAL_NOT_AUTO_CARRIED": lambda x: not x["successor_initialization"][0]["deferral_rebound"],
        "F13_DEFERRAL_EXPLICITLY_REBOUND": lambda x: x["successor_initialization"][0]["deferral_rebound"],
        "F14_CARRY_FORWARD_CONTINUITY": lambda x: x["relation_valid"] and x["successor_initialization"][0]["mode"] == "CONTINUITY",
    }

    by_id = {row["fixture_id"]: row for row in rows}
    fixture_conditions = {
        fid: fn(semantic_view(by_id[fid]["expected"]))
        for fid, fn in required_semantic.items()
    }
    substantive_conditions_pass = all(fixture_conditions.values())

    outcome = (
        "D2_LINEAGE_EXTENSION_PLAUSIBLE"
        if semantic_all and substantive_conditions_pass
        else "D2_AMEND"
    )

    result = {
        "probe_id": "HYBRID_D2_LINEAGE_EXTENSION_V01",
        "scoring_rule": "Research 486: semantic fields strict; reason_codes diagnostic only",
        "rows": rows,
        "substantive_fixture_conditions": fixture_conditions,
        "summary": {
            "fixture_total": len(rows),
            "semantic_a_matches_key": sum(row["semantic"]["a_matches_key"] for row in rows),
            "semantic_b_matches_key": sum(row["semantic"]["b_matches_key"] for row in rows),
            "semantic_a_b_agree": sum(row["semantic"]["a_b_agree"] for row in rows),
            "semantic_all_match": semantic_all,
            "full_object_a_matches_key": full_a_key,
            "full_object_b_matches_key": full_b_key,
            "full_object_a_b_agree": full_ab,
            "substantive_conditions_pass": substantive_conditions_pass,
            "outcome": outcome,
        },
    }
    (ROOT / "result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], sort_keys=True))

if __name__ == "__main__":
    main()
