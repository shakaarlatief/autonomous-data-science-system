from __future__ import annotations

import copy
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
FIXTURE_PATH = ROOT / "fixture.json"
ORACLE_PATH = ROOT / "oracle.json"
CANDIDATE_PATH = ROOT / "candidate.py"
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_candidate():
    if not CANDIDATE_PATH.exists():
        raise RuntimeError("candidate.py is missing")
    spec = importlib.util.spec_from_file_location("r0_p02_candidate", CANDIDATE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load candidate.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    fn = getattr(module, "evaluate_fixture", None)
    if not callable(fn):
        raise RuntimeError("candidate.py must expose evaluate_fixture(fixture)")
    return fn


def canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def validate_result(result: Any, fixture: dict[str, Any], oracle: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not isinstance(result, dict):
        return ["result must be an object"]
    if result.get("schema_version") != 1:
        errors.append("schema_version must equal 1")
    if result.get("protocol") != "R0-P02-V01":
        errors.append("protocol must equal R0-P02-V01")

    cases = result.get("cases")
    if not isinstance(cases, list):
        return errors + ["cases must be a list"]

    expected_cases = fixture["cases"]
    if len(cases) != len(expected_cases):
        errors.append(f"case count {len(cases)} != {len(expected_cases)}")
        return errors

    for i, (actual, spec_case) in enumerate(zip(cases, expected_cases)):
        prefix = f"case[{i}]"
        if not isinstance(actual, dict):
            errors.append(f"{prefix} must be an object")
            continue
        cid = spec_case["case_id"]
        if actual.get("case_id") != cid:
            errors.append(f"{prefix} case_id mismatch")
            continue
        expected = oracle["expected"][cid]
        if actual.get("outcome") != expected["outcome"]:
            errors.append(
                f"{cid} outcome {actual.get('outcome')!r} != {expected['outcome']!r}"
            )
        if actual.get("latestness") != expected["latestness"]:
            errors.append(
                f"{cid} latestness {actual.get('latestness')!r} != {expected['latestness']!r}"
            )
        for field in ("semantic_state_digest", "chain_head_digest"):
            value = actual.get(field)
            if value is not None and (not isinstance(value, str) or HEX64.fullmatch(value) is None):
                errors.append(f"{cid} {field} must be null or 64 lowercase hex")

    return errors


def remap_oracle_for_fixture(
    base_fixture: dict[str, Any],
    transformed_fixture: dict[str, Any],
    base_oracle: dict[str, Any],
) -> dict[str, Any]:
    transformed = {"schema_version": 1, "protocol": "R0-P02-V01", "expected": {}}
    for old, new in zip(base_fixture["cases"], transformed_fixture["cases"]):
        transformed["expected"][new["case_id"]] = copy.deepcopy(
            base_oracle["expected"][old["case_id"]]
        )
    return transformed


def main() -> int:
    fixture = load_json(FIXTURE_PATH)
    oracle = load_json(ORACLE_PATH)
    evaluate = load_candidate()

    errors: list[str] = []

    result_a = evaluate(copy.deepcopy(fixture))
    result_b = evaluate(copy.deepcopy(fixture))
    if canonical(result_a) != canonical(result_b):
        errors.append("candidate output is not deterministic across identical runs")
    errors.extend(validate_result(result_a, fixture, oracle))

    renamed = copy.deepcopy(fixture)
    for i, case in enumerate(renamed["cases"], start=1):
        case["case_id"] = f"META-{i:02d}"
    renamed_oracle = remap_oracle_for_fixture(fixture, renamed, oracle)
    renamed_result = evaluate(renamed)
    errors.extend(
        f"renamed-case metamorphic: {e}"
        for e in validate_result(renamed_result, renamed, renamed_oracle)
    )

    alternate = copy.deepcopy(fixture)
    alternate["project_id"] = "ADS-R0-P02-SYNTHETIC-ALT"
    alternate["wrong_project_id"] = "OTHER-PROJECT-SYNTHETIC-ALT"
    alternate["test_secret"] = "R0-P02-SYNTHETIC-ALT-ONLY-NOT-A-REAL-SECRET"
    alternate_result = evaluate(alternate)
    errors.extend(
        f"alternate-context metamorphic: {e}"
        for e in validate_result(alternate_result, alternate, oracle)
    )

    output = {
        "schema_version": 1,
        "protocol": "R0-P02-V01",
        "deterministic_core": "PASS" if not errors else "FAIL",
        "error_count": len(errors),
        "errors": errors,
        "case_count": len(fixture["cases"]),
        "metamorphic_checks": 2,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
