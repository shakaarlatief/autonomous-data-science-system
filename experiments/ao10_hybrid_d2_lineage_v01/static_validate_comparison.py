import ast
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent

EXPECTED = {
    "evaluator_chatgpt_a.py": "26b63dcc0968b73927145bdd495865091a5ef1847feb28213549d7eb6c914e6f",
    "evaluator_claude_b.py": "b4c8ff134ce51f7c833600a8e87849205cf1f2554102314f5ff1ea30aba3ee3b",
    "reviewer_fixtures.json": "46b2ef98fde976f3659884e0de91e120d580ddfeeacdab9c983a5f55bd7cf464",
    "evaluator_contract.json": "bb5125eed59a432d0d7f22e7db4b66350d1f56dc2da8a19c3039c090caec1989",
    "evaluator_key.json": "3306aa976671768aaa8ba974eb206c131392b81b2cb86171b3edf9c7a286c11f",
}

def main():
    for name, expected in EXPECTED.items():
        actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        assert actual == expected, (name, actual, expected)
    ast.parse((ROOT / "run_two_model_comparison.py").read_text(encoding="utf-8"))
    assert not (ROOT / "result.json").exists()
    print("HYBRID_D2_COMPARISON_STATIC_VALIDATION=PASS")

if __name__ == "__main__":
    main()
