from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load_json(name: str):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def rank(order, value):
    try:
        return order.index(value)
    except ValueError:
        return -1


def evaluate(policy: dict, request: dict, *, faulty: bool = False) -> dict:
    # Policy, never AO request shaping, owns the mandatory claim set.
    if faulty:
        effective_claims = set(request.get("requested_claims", []))
    else:
        effective_claims = set(policy["required_claims"])

    for extra in request.get("extra_checks", []):
        mapped = policy["governed_extra_checks"].get(extra)
        if mapped:
            effective_claims.add(mapped)

    reasons = []
    decision = "ADMIT"

    if request.get("subject_id") != policy["subject_id"] or request.get("subject_revision") != policy["subject_revision"]:
        decision = "REFUSE"
        reasons.append("SUBJECT_REVISION_MISMATCH")

    if request.get("base_revision") != policy["required_base_revision"]:
        decision = "REFUSE"
        reasons.append("BASE_REVISION_MISMATCH")

    consequence = request.get("intended_consequence")
    if rank(policy["consequence_order"], consequence) < rank(policy["consequence_order"], policy["consequence_floor"]):
        decision = "REFUSE"
        reasons.append("CONSEQUENCE_BELOW_POLICY_FLOOR")

    profile = request.get("profile_hint")
    if profile not in policy["known_profiles"] and decision == "ADMIT":
        decision = "REVIEW_REQUIRED"
        reasons.append("UNKNOWN_PROFILE_HINT")

    trust = request.get("trust_context", {}).get("level")
    if rank(policy["trust_order"], trust) < rank(policy["trust_order"], policy["required_trust_level"]):
        if decision != "REFUSE":
            decision = "REVIEW_REQUIRED"
        reasons.append("TRUST_REQUIREMENT_UNSATISFIED")

    age = request.get("evidence_age_seconds")
    if age is None or age > policy["freshness_max_age_seconds"]:
        decision = "REFUSE"
        reasons.append("FRESHNESS_REQUIREMENT_UNSATISFIED")

    required = set(policy["required_claims"])
    missing_policy_claims = sorted(required - effective_claims)
    if missing_policy_claims:
        decision = "REFUSE"
        reasons.append("POLICY_REQUIRED_CLAIM_SUPPRESSED")

    return {
        "decision": decision,
        "effective_claims": sorted(effective_claims),
        "missing_policy_claims": missing_policy_claims,
        "reasons": reasons,
        "subject_id": request.get("subject_id"),
        "subject_revision": request.get("subject_revision"),
        "base_revision": request.get("base_revision"),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    policy = load_json("policy.json")
    cases = load_json("cases.json")

    results = []
    pass_count = 0
    required = set(policy["required_claims"])

    for case in cases:
        actual = evaluate(policy, case["request"])
        expected_extra = set(case.get("expected_extra_claims", []))
        claim_ok = required.issubset(set(actual["effective_claims"]))
        extra_ok = expected_extra.issubset(set(actual["effective_claims"]))
        decision_ok = actual["decision"] == case["expected_decision"]
        ok = claim_ok and extra_ok and decision_ok
        pass_count += int(ok)
        results.append({
            "id": case["id"],
            "ok": ok,
            "expected_decision": case["expected_decision"],
            "actual": actual,
            "required_claims_preserved": claim_ok,
            "expected_extra_claims_preserved": extra_ok,
        })

    # Seeded-violation witness: a faulty normalizer that trusts requested_claims
    # must lose policy claims on omission cases and therefore be detected.
    faulty_witnesses = []
    for case_id in ("C02_omit_one_claim", "C03_omit_multiple_claims"):
        case = next(c for c in cases if c["id"] == case_id)
        faulty = evaluate(policy, case["request"], faulty=True)
        caught = bool(faulty["missing_policy_claims"]) and faulty["decision"] == "REFUSE"
        faulty_witnesses.append({"id": case_id, "caught": caught, "faulty_result": faulty})

    faulty_caught = all(w["caught"] for w in faulty_witnesses)
    all_pass = pass_count == len(cases) and faulty_caught

    result = {
        "probe": "DRP-09",
        "protocol": "AO10-DRP-V01",
        "case_count": len(cases),
        "case_pass_count": pass_count,
        "faulty_normalizer_witness_caught": faulty_caught,
        "all_pass": all_pass,
        "cases": results,
        "faulty_witnesses": faulty_witnesses,
    }

    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    (out / "result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({
        "probe": "DRP-09",
        "cases": len(cases),
        "passed": pass_count,
        "faulty_witness_caught": faulty_caught,
        "all_pass": all_pass,
    }, sort_keys=True))
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
