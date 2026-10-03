import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def main():
    definitions = json.loads((ROOT / "definitions.json").read_text(encoding="utf-8"))
    fixtures = json.loads((ROOT / "fixtures.json").read_text(encoding="utf-8"))
    assert definitions["probe_id"] == "HYBRID_C8_ORIENTATION_V01"
    assert definitions["top_level_states"] == ["REVIEW_REQUIRED", "DEFERRED", "OPEN", "SATISFIED"]
    assert len(fixtures["fixtures"]) == 11
    assert len({x["fixture_id"] for x in fixtures["fixtures"]}) == 11
    for filename in ("evaluator_a.py", "evaluator_b.py", "run_comparison.py"):
        ast.parse((ROOT / filename).read_text(encoding="utf-8"), filename=filename)
    assert not (ROOT / "result.json").exists()
    print("HYBRID_C8_STATIC_VALIDATION=PASS")

if __name__ == "__main__":
    main()
