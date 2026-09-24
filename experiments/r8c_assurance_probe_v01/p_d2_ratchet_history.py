from __future__ import annotations

import argparse
import copy
import hashlib
import inspect
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIXTURE_PATH = "experiments/r8c_assurance_probe_v01/p_d2_history_labels.json"
HARNESS_PATHS = [
    "experiments/r8c_assurance_probe_v01/README.md",
    "experiments/r8c_assurance_probe_v01/p_d2_ratchet_history.py",
]
EXPECTED_FIXTURE_SHA256 = "be70e8c3aa5f4dea2b9f2680ebaae1b4c09b1733a6f8a22da4edeb93d3f86072"
EXPECTED_COVERAGE = {
    "tightening",
    "weakening",
    "rename_move",
    "split_merge",
    "test_deletion",
    "input_scope_narrowing",
    "dependency_lock_change",
    "neutral_refactor",
}


class ProbeFailure(RuntimeError):
    pass


def git_bytes(*args: str) -> bytes:
    cp = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, check=False)
    if cp.returncode:
        raise ProbeFailure(
            "git failed: " + " ".join(args) + "\n" + cp.stderr.decode("utf-8", errors="replace")
        )
    return cp.stdout


def blob(commit: str, path: str) -> bytes:
    return git_bytes("show", f"{commit}:{path}")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def harness_binding(commit: str) -> dict[str, object]:
    return {
        "hash_basis": "GIT_BLOB_BYTES_AT_COMMIT",
        "commit": commit,
        "files": {path: sha256(blob(commit, path)) for path in HARNESS_PATHS},
    }


def patch_for(case: dict[str, object]) -> bytes:
    return git_bytes(
        "diff",
        "--binary",
        "--find-renames=50%",
        str(case["parent_commit"]),
        str(case["head_commit"]),
        "--",
        *[str(path) for path in case["selected_paths"]],
    )


def verify_history_case(case: dict[str, object]) -> dict[str, object]:
    parents = git_bytes("show", "-s", "--format=%P", str(case["head_commit"])).decode().strip().split()
    if parents != [case["parent_commit"]]:
        raise ProbeFailure(f"{case['case_id']} parent mismatch: {parents}")

    patch = patch_for(case)
    if not patch:
        raise ProbeFailure(f"{case['case_id']} selected patch is empty")
    if sha256(patch) != case["selected_patch_sha256"]:
        raise ProbeFailure(f"{case['case_id']} selected patch digest mismatch")
    if len(patch) != case["selected_patch_bytes"]:
        raise ProbeFailure(f"{case['case_id']} selected patch byte-count mismatch")

    text = patch.decode("utf-8", errors="replace")
    lines = text.splitlines()
    for marker in case["evidence_markers"]["added"]:
        if not any(line.startswith("+") and marker in line for line in lines):
            raise ProbeFailure(f"{case['case_id']} added evidence marker missing: {marker}")
    for marker in case["evidence_markers"]["removed"]:
        if not any(line.startswith("-") and marker in line for line in lines):
            raise ProbeFailure(f"{case['case_id']} removed evidence marker missing: {marker}")

    return {
        "case_id": case["case_id"],
        "patch_sha256": sha256(patch),
        "patch_bytes": len(patch),
        "binding_valid": True,
    }


def classifier_input(case: dict[str, object]) -> dict[str, object]:
    allowed = {
        "case_id",
        "head_commit",
        "parent_commit",
        "selected_patch_sha256",
        "policy_delta",
    }
    result = {key: copy.deepcopy(value) for key, value in case.items() if key in allowed}
    if "independent_label" in result or "label_rationale" in result:
        raise ProbeFailure("label leakage into classifier input")
    return result


def classify_case(case: dict[str, object]) -> str:
    delta = case["policy_delta"]

    if delta["claim_requirement"] == "REMOVED":
        return "WEAKEN"
    if delta["consequence_floor"] in {"LOWER", "WEAKER"}:
        return "WEAKEN"
    if delta["threshold"] in {"LOWER", "WEAKER"}:
        return "WEAKEN"
    if delta["trust_floor"] == "WEAKER":
        return "WEAKEN"
    if delta["verifier_coverage"] in {"NARROWER", "REMOVED"}:
        return "WEAKEN"
    if delta["witness_strength"] == "WEAKER":
        return "WEAKEN"
    if delta["waiver_authority"] == "WIDER":
        return "WEAKEN"
    if delta["input_scope"] == "NARROWER":
        return "REVIEW"

    lineage = delta["lineage_operation"]
    if lineage in {"RENAME_MOVE", "SPLIT", "MERGE", "RETIRE_REPLACE", "REFACTOR"}:
        if not delta["base_witness_carry_forward"]:
            return "REVIEW"
        return "NEUTRAL"

    strengthening = any(
        (field, value) in {
            ("claim_requirement", "ADDED"),
            ("consequence_floor", "HIGHER"),
            ("threshold", "HIGHER"),
            ("trust_floor", "STRONGER"),
            ("input_scope", "WIDER"),
            ("verifier_coverage", "WIDER"),
            ("witness_strength", "STRONGER"),
            ("waiver_authority", "NARROWER"),
        }
        for field, value in delta.items()
        if field != "base_witness_carry_forward"
    )
    return "STRENGTHEN" if strengthening else "NEUTRAL"


def policy_diff_payload(cases: list[dict[str, object]]) -> list[dict[str, object]]:
    return [
        {
            "case_id": case["case_id"],
            "parent_commit": case["parent_commit"],
            "head_commit": case["head_commit"],
            "selected_patch_sha256": case["selected_patch_sha256"],
            "policy_delta": case["policy_delta"],
        }
        for case in cases
    ]


def policy_diff_digest(cases: list[dict[str, object]]) -> str:
    return sha256(canonical_json_bytes(policy_diff_payload(cases)))


def bind_owner_batch(cases: list[dict[str, object]]) -> dict[str, object]:
    return {
        "policy_diff_digest": policy_diff_digest(cases),
        "case_ids": [case["case_id"] for case in cases],
        "decision_semantics": "One owner disposition may bind exactly this policy-diff digest.",
    }


def owner_batch_matches(binding: dict[str, object], cases: list[dict[str, object]]) -> bool:
    return binding.get("policy_diff_digest") == policy_diff_digest(cases)


def label_criterion(expected: str, observed: str) -> bool:
    if expected == "WEAKEN":
        return observed in {"WEAKEN", "REVIEW"}
    if expected == "REVIEW":
        return observed in {"REVIEW", "WEAKEN"}
    if expected == "NEUTRAL_LINEAGE":
        return observed in {"NEUTRAL", "STRENGTHEN"}
    if expected == "NEUTRAL":
        return observed == "NEUTRAL"
    if expected == "STRENGTHEN":
        return observed == "STRENGTHEN"
    raise ProbeFailure(f"unknown independent label: {expected}")


def load_and_validate_fixture(selection_commit: str) -> tuple[dict[str, object], list[dict[str, object]], dict[str, str], list[dict[str, object]]]:
    raw = blob(selection_commit, FIXTURE_PATH)
    if sha256(raw) != EXPECTED_FIXTURE_SHA256:
        raise ProbeFailure("frozen P-D2 fixture SHA-256 mismatch")
    fixture = json.loads(raw)
    if fixture.get("probe") != "P-D2" or fixture.get("status") != "FROZEN_BEFORE_CLASSIFIER":
        raise ProbeFailure("unexpected P-D2 fixture identity/status")
    if fixture.get("classifier_authored") is not False:
        raise ProbeFailure("selection fixture does not preserve pre-classifier boundary")

    cases = fixture.get("cases")
    if not isinstance(cases, list) or len(cases) != 10:
        raise ProbeFailure("expected exactly ten frozen history cases")
    ids = [case.get("case_id") for case in cases]
    if len(set(ids)) != len(ids):
        raise ProbeFailure("duplicate P-D2 history case IDs")

    coverage = {tag for case in cases for tag in case["coverage_tags"]}
    if not EXPECTED_COVERAGE.issubset(coverage):
        raise ProbeFailure(f"required historical coverage missing: {sorted(EXPECTED_COVERAGE - coverage)}")

    bindings = [verify_history_case(case) for case in cases]
    labels = {str(case["case_id"]): str(case["independent_label"]) for case in cases}
    sanitized = [classifier_input(case) for case in cases]
    for row in sanitized:
        if set(row) & {"independent_label", "label_rationale"}:
            raise ProbeFailure("independent labels leaked into classifier inputs")
    return fixture, sanitized, labels, bindings


def evaluate(selection_commit: str, harness_commit: str) -> dict[str, object]:
    fixture, cases, labels, bindings = load_and_validate_fixture(selection_commit)

    classifier_source = inspect.getsource(classify_case)
    if "independent_label" in classifier_source or "label_rationale" in classifier_source:
        raise ProbeFailure("classifier source references frozen label fields")

    classifications = {str(case["case_id"]): classify_case(case) for case in cases}
    label_checks = {case_id: label_criterion(labels[case_id], classifications[case_id]) for case_id in labels}

    weakening_ids = [case_id for case_id, label in labels.items() if label == "WEAKEN"]
    material_weakening_detected = all(classifications[case_id] in {"WEAKEN", "REVIEW"} for case_id in weakening_ids)

    lineage_ids = [case_id for case_id, label in labels.items() if label == "NEUTRAL_LINEAGE"]
    lineage_not_owner_gated = all(classifications[case_id] not in {"WEAKEN", "REVIEW"} for case_id in lineage_ids)

    witness_control = copy.deepcopy(next(case for case in cases if case["case_id"] == "PD2-H03"))
    witness_control["policy_delta"]["base_witness_carry_forward"] = False
    witness_control_result = classify_case(witness_control)
    witness_removal_blocked = witness_control_result in {"WEAKEN", "REVIEW"}

    binding = bind_owner_batch(cases)
    exact_batch_accepts_original = owner_batch_matches(binding, cases)
    digest_mutant = copy.deepcopy(cases)
    digest_mutant[0]["policy_delta"]["threshold"] = "LOWER"
    digest_changes_on_material_delta = policy_diff_digest(digest_mutant) != binding["policy_diff_digest"]
    stale_batch_rejected = not owner_batch_matches(binding, digest_mutant)

    patch_control = copy.deepcopy(fixture["cases"][0])
    patch_control["selected_patch_sha256"] = "0" * 64
    try:
        verify_history_case(patch_control)
    except ProbeFailure:
        patch_drift_rejected = True
    else:
        patch_drift_rejected = False

    criteria = {
        "all_frozen_labels_satisfy_preregistered_criteria": all(label_checks.values()),
        "every_material_weakening_detected": material_weakening_detected,
        "lineage_preserving_changes_not_owner_gated": lineage_not_owner_gated,
        "required_base_witness_removal_cannot_pass": witness_removal_blocked,
        "owner_batch_binds_one_exact_policy_diff_digest": exact_batch_accepts_original,
        "material_policy_mutation_changes_digest": digest_changes_on_material_delta,
        "stale_owner_batch_digest_rejected": stale_batch_rejected,
        "classifier_input_excludes_frozen_labels": all(
            "independent_label" not in row and "label_rationale" not in row for row in cases
        ),
        "historical_patch_drift_negative_control_rejected": patch_drift_rejected,
    }

    result = "PASS" if all(criteria.values()) else "AMEND"
    return {
        "probe": "P-D2",
        "protocol": "Research 277",
        "selection_freeze": "Research 294",
        "candidate": "WARRANT-F V0.2",
        "result": result,
        "harness_binding": harness_binding(harness_commit),
        "selection_binding": {
            "commit": selection_commit,
            "fixture_path": FIXTURE_PATH,
            "fixture_sha256": EXPECTED_FIXTURE_SHA256,
        },
        "history_bindings": bindings,
        "classifications": [
            {
                "case_id": case_id,
                "expected_independent_label": labels[case_id],
                "observed_ratchet_classification": classifications[case_id],
                "criterion_satisfied": label_checks[case_id],
            }
            for case_id in labels
        ],
        "negative_controls": {
            "removed_required_base_witness": {
                "source_case": "PD2-H03",
                "classification": witness_control_result,
                "blocked": witness_removal_blocked,
            },
            "historical_patch_digest_drift_rejected": patch_drift_rejected,
        },
        "policy_diff_binding": {
            **binding,
            "material_delta_mutant_digest": policy_diff_digest(digest_mutant),
            "digest_changed": digest_changes_on_material_delta,
            "stale_original_binding_rejected_for_mutant": stale_batch_rejected,
        },
        "criteria": criteria,
        "interpretation": {
            "material_weakening_can_be_detected": material_weakening_detected,
            "lineage_preserving_evolution_can_remain_non_reviewing": lineage_not_owner_gated,
            "self_removal_of_required_base_witness_is_blocked": witness_removal_blocked,
            "owner_batch_can_bind_exact_policy_diff": exact_batch_accepts_original and stale_batch_rejected,
            "target_architecture_amendment_required": result != "PASS",
            "physical_migration_authorized": False,
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selection-commit", required=True)
    ap.add_argument("--harness-commit", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    payload = evaluate(args.selection_commit, args.harness_commit)
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "probe": payload["probe"],
        "result": payload["result"],
        "history_cases": len(payload["classifications"]),
        "criteria_passed": sum(payload["criteria"].values()),
        "criteria_total": len(payload["criteria"]),
        "policy_diff_digest": payload["policy_diff_binding"]["policy_diff_digest"],
    }, indent=2))
    return 0 if payload["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
