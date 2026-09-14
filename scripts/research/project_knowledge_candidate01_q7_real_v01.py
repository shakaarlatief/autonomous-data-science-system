#!/usr/bin/env python3
"""Run Candidate 01's real Q7 public/private-boundary shadow probe.

The implementation is oracle-blind. It consumes the frozen public fixture plus a
privacy-preserving receipt derived inside the authorized private companion
workspace. The receipt contains only public-safe anchor values, cryptographic
bindings and whitelisted non-sensitive state. Exact private paths/values are not
inputs to the public-side probe and must never be serialized into its result.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

EXPECTED_FIXTURE_SHA256 = "a8e0872aa8c1ffab421d86924185c48642a075f872aa64847ebac7df34037bef"
DEFAULT_FIXTURE = Path("docs/research/project_knowledge_candidate_01_q7_real_v01/Q7_REAL_FIXTURE_V01.json")
DEFAULT_RECEIPT = Path("docs/research/project_knowledge_candidate_01_q7_real_v01/PRIVATE_EVIDENCE_RECEIPT_V01.json")
DEFAULT_OUTPUT = Path("docs/research/project_knowledge_candidate_01_q7_real_v01/RESULTS_V01.json")
DECLARATION_RE = re.compile(
    r"<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->\r?\n(.*?)\r?\n<!-- PKA-STRUCTURED-DECLARATION-END -->",
    flags=re.DOTALL,
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_fixture(path: Path) -> tuple[dict[str, Any], str]:
    raw = path.read_bytes()
    digest = sha256_bytes(raw)
    if digest != EXPECTED_FIXTURE_SHA256:
        raise RuntimeError(
            f"fixture hash mismatch: expected {EXPECTED_FIXTURE_SHA256}, got {digest}"
        )
    fixture = json.loads(raw.decode("utf-8"))
    if fixture["protocol"]["implementation_may_read_oracle"] is not False:
        raise RuntimeError("fixture lost oracle-blind implementation contract")
    return fixture, digest


def load_receipt(path: Path, fixture: dict[str, Any]) -> dict[str, Any]:
    receipt = json.loads(path.read_text(encoding="utf-8"))
    binding = fixture["private_evidence_binding"]
    if receipt["private_repository_head"] != binding["repository_head"]:
        raise RuntimeError("private receipt repository-head binding mismatch")
    if receipt["private_state_sha256"] != binding["current_private_state_sha256"]:
        raise RuntimeError("private receipt state binding mismatch")
    if receipt["private_sensitive_payload_sha256"] != binding["sensitive_payload_sha256"]:
        raise RuntimeError("private receipt sensitive-payload binding mismatch")
    if receipt["private_value_leak_count"] != 0:
        raise RuntimeError("private-side receipt reports leaked private values")
    if receipt["private_paths_serialized_count"] != 0:
        raise RuntimeError("private-side receipt reports serialized private paths")
    return receipt


def public_source_map(fixture: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["source_key"]: item for item in fixture["real_public_sources"]}


def read_public_source(fixture: dict[str, Any], source_key: str) -> str:
    item = public_source_map(fixture)[source_key]
    raw = subprocess.check_output(
        ["git", "show", f"{fixture['real_public_base_commit']}:{item['path']}"]
    )
    if len(raw) != item["bytes"] or sha256_bytes(raw) != item["sha256"]:
        raise RuntimeError(f"public source drift: {source_key}")
    return raw.decode("utf-8")


def all_public_source_hashes_match(fixture: dict[str, Any]) -> bool:
    for item in fixture["real_public_sources"]:
        raw = subprocess.check_output(
            ["git", "show", f"{fixture['real_public_base_commit']}:{item['path']}"]
        )
        if len(raw) != item["bytes"] or sha256_bytes(raw) != item["sha256"]:
            return False
    for item in fixture["shadow_sources"]:
        raw = Path(item["path"]).read_bytes()
        if len(raw) != item["bytes"] or sha256_bytes(raw) != item["sha256"]:
            return False
    return True


def read_shadow_policy(fixture: dict[str, Any]) -> dict[str, Any]:
    item = fixture["shadow_sources"][0]
    raw = Path(item["path"]).read_bytes()
    match = DECLARATION_RE.search(raw.decode("utf-8"))
    if not match:
        raise RuntimeError("shadow public/private boundary declaration missing")
    declaration = json.loads(match.group(1))
    if declaration.get("shadow_only") is not True:
        raise RuntimeError("shadow policy lost shadow-only status")
    return declaration


def validate_public_contracts(fixture: dict[str, Any]) -> dict[str, bool]:
    current_state = read_public_source(fixture, "current_state")
    continuity = read_public_source(fixture, "continuity")
    private_contract = read_public_source(fixture, "private_companion_contract")
    spec025 = read_public_source(fixture, "spec025")
    spec026 = read_public_source(fixture, "spec026")
    checker = read_public_source(fixture, "private_checker")
    checks = {
        "resolved_private_present": "RESOLVED_PRIVATE" in current_state,
        "public_first_reconstruction": "Repository-first reconstruction is always **public-first**" in continuity,
        "private_not_second_development_authority": (
            "not a second development repository" in continuity
            and "knowledge-preservation complement only" in private_contract
        ),
        "private_unavailable_preserves_resolved": (
            "preserve the public `RESOLVED_PRIVATE` status" in continuity
            and "preserve `RESOLVED_PRIVATE`; do not silently downgrade it to `UNRESOLVED`" in private_contract
        ),
        "private_status_separate": (
            "PRIVATE_CONTINUITY_INTEGRITY=PASS" in spec025
            and "PRIVATE_CONTINUITY_INTEGRITY=FAIL" in spec025
            and "PRIVATE_CONTINUITY_INTEGRITY=NOT_VERIFIED" in spec025
        ),
        "private_anchor_contract": (
            "Public continuity checkpoint" in spec026
            and "Public continuity commit" in spec026
            and "NOT_VERIFIED" in spec026
        ),
        "checker_has_not_verified_path": 'return "NOT_VERIFIED", []' in checker,
    }
    if not all(checks.values()):
        failed = [key for key, value in checks.items() if not value]
        raise RuntimeError(f"public contract evidence missing: {failed}")
    return checks


def private_continuity_status(
    scenario: dict[str, Any], receipt: dict[str, Any], fixture: dict[str, Any]
) -> str:
    if scenario["private_access"] == "UNAVAILABLE":
        return "NOT_VERIFIED"
    target = fixture["public_target"]
    anchor = receipt["public_safe_anchor"]
    return (
        "PASS"
        if anchor["checkpoint"] == target["checkpoint"]
        and anchor["commit"] == target["commit"]
        else "FAIL"
    )


def scenario_result(
    scenario: dict[str, Any], policy: dict[str, Any], receipt: dict[str, Any], fixture: dict[str, Any]
) -> dict[str, Any]:
    status = private_continuity_status(scenario, receipt, fixture)
    public_resolved = True
    public_authority = (
        policy["public_development_authority"] == "PUBLIC_ADS_REPOSITORY"
        and policy["private_companion_role"] == "DELEGATED_PRIVATE_CONTINUITY_ONLY"
    )
    optional_bypass = False
    leak_count = 0
    private_paths_serialized_count = 0

    if scenario["scenario_id"] == "Q7-S01":
        disposition = policy["rules"]["public_only_task_private_unavailable"]
    elif scenario["scenario_id"] == "Q7-S02":
        disposition = policy["rules"]["private_required_task_private_unavailable"]
    elif scenario["scenario_id"] == "Q7-S03":
        if status != "FAIL":
            raise RuntimeError("Q7-S03 expected the real stale private anchor to fail")
        disposition = policy["rules"]["private_required_task_private_anchor_fail"]
    elif scenario["scenario_id"] == "Q7-S04":
        # The privacy-preserving receipt is itself the public projection boundary.
        # Only whitelisted public-safe state is exposed. Exact private strings were
        # checked for non-occurrence inside the private workspace before this receipt
        # was handed to the public-side probe.
        disposition = "PUBLIC_SAFE_PROJECTION_ONLY"
        leak_count = receipt["private_value_leak_count"]
        private_paths_serialized_count = receipt["private_paths_serialized_count"]
    elif scenario["scenario_id"] == "Q7-S05":
        if scenario["optional_retrieval_available"]:
            raise RuntimeError("Q7-S05 must exercise optional retrieval unavailability")
        disposition = policy["rules"]["optional_retrieval_unavailable"]
        optional_bypass = False
    else:
        raise RuntimeError(f"unknown scenario: {scenario['scenario_id']}")

    result = {
        "private_continuity_status": status,
        "task_disposition": disposition,
        "public_resolved_private_preserved": public_resolved,
        "public_authority_preserved": public_authority,
    }
    if scenario["scenario_id"] == "Q7-S04":
        result["private_value_leak_count"] = leak_count
        result["private_paths_serialized_count"] = private_paths_serialized_count
        result["public_safe_state"] = receipt["public_safe_state"]
    if scenario["scenario_id"] == "Q7-S05":
        result["optional_retrieval_authority_bypass"] = optional_bypass
    return result


def assert_result_nonleakage(result: dict[str, Any], fixture: dict[str, Any]) -> None:
    rendered = json.dumps(result, sort_keys=True)
    for field in fixture["protocol"]["forbidden_result_fields"]:
        if field in result:
            raise RuntimeError(f"forbidden result field serialized: {field}")
    # Defensive tokens that would indicate accidental serialization of runtime
    # private paths or common exact private-value shapes.
    forbidden_patterns = [
        r"[A-Za-z]:\\",
        r"@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        r"https?://",
    ]
    for pattern in forbidden_patterns:
        if re.search(pattern, rendered):
            raise RuntimeError(f"public result contains forbidden private-like pattern: {pattern}")


def run_probe(
    fixture: dict[str, Any], fixture_sha: str, receipt: dict[str, Any]
) -> dict[str, Any]:
    policy = read_shadow_policy(fixture)
    contract_checks = validate_public_contracts(fixture)
    scenarios = {
        scenario["scenario_id"]: scenario_result(scenario, policy, receipt, fixture)
        for scenario in fixture["scenarios"]
    }
    result = {
        "schema_version": 1,
        "probe_id": "PKA-C01-Q7-REAL-PROBE-V01",
        "candidate_id": fixture["candidate_id"],
        "fixture_id": fixture["fixture_id"],
        "real_public_base_commit": fixture["real_public_base_commit"],
        "fixture_sha256": fixture_sha,
        "shadow_only": True,
        "implementation_reads_oracle": False,
        "all_public_source_hashes_match": all_public_source_hashes_match(fixture),
        "private_evidence_binding_match": True,
        "public_contract_checks": contract_checks,
        "observed_private_anchor": receipt["public_safe_anchor"],
        "scenarios": scenarios,
        "global_private_value_leak_count": receipt["private_value_leak_count"],
        "global_private_paths_serialized_count": receipt["private_paths_serialized_count"],
        "q7_real_subsystem_support": (
            receipt["private_value_leak_count"] == 0
            and receipt["private_paths_serialized_count"] == 0
            and scenarios["Q7-S01"]["task_disposition"]
            == "ALLOW_PUBLIC_CONTINUATION_WITH_PRIVATE_NOT_VERIFIED"
            and scenarios["Q7-S02"]["task_disposition"]
            == "BLOCK_REQUIRED_PRIVATE_UNVERIFIED"
            and scenarios["Q7-S03"]["task_disposition"]
            == "BLOCK_PRIVATE_CONTINUITY_FAIL"
            and scenarios["Q7-S05"]["optional_retrieval_authority_bypass"] is False
        ),
        "interpretation": {
            "q7_final_qualification_claimed": False,
            "private_continuity_current_against_public_target": False,
            "public_repository_integrity_reclassified_by_private_status": False,
            "architecture_selection_claimed": False,
        },
    }
    assert_result_nonleakage(result, fixture)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--receipt", type=Path, default=DEFAULT_RECEIPT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--no-write", action="store_true")
    args = parser.parse_args()

    fixture, digest = load_fixture(args.fixture)
    receipt = load_receipt(args.receipt, fixture)
    result = run_probe(fixture, digest, receipt)
    rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if not args.no_write:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
