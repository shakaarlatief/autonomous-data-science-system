"""Strict evidence classifier for the specific fake-only R0-P03 custody trial.

The classifier does not perform OS, path, secret, or agent-tool operations.
It prevents a workspace-root denial or platform-blocked call from being
misreported as Windows access denial or general gold custody qualification.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

EXPECTED_MARKER = "SYNTHETIC_ONLY_R0_P03_NO_REAL_GOLD"
PASS = "PASS"
OS_DENIED = "OS_ACCESS_DENIED"
PLATFORM_BLOCKED = "PLATFORM_SAFETY_BLOCKED_BEFORE_EXECUTION"
NOT_EXERCISED = "NOT_EXERCISED"
TOOL_ROOT_DENIED = "WORKSPACE_ROOT_REFUSAL"
READ_SUCCEEDED = "READ_SUCCEEDED"
MISSING = "NOT_FOUND"
ALLOWED_OS_STATUSES = frozenset({OS_DENIED, PLATFORM_BLOCKED, NOT_EXERCISED, READ_SUCCEEDED, MISSING})
REQUIRED_FIELDS = frozenset({
    "schema_version", "synthetic_marker", "owner_report", "bridge_observations",
    "research_boundary",
})


def classify(data: dict[str, Any]) -> dict[str, Any]:
    """Classify only observed synthetic data without claiming full Level B.

    The exact synthetic digest is public-verifiable test data, not a private
    answer commitment. Direct Windows identity/ACL tests must independently
    execute and return OS_ACCESS_DENIED to support a *target- and route-scoped*
    OS-denial statement. Tool-root refusal never substitutes for that result.
    """
    if not isinstance(data, dict) or set(data) != REQUIRED_FIELDS or data["schema_version"] != 1:
        raise ValueError("Invalid specific trial evidence schema")
    if data["synthetic_marker"] != EXPECTED_MARKER:
        raise ValueError("Real/non-synthetic evidence refused")
    owner = data["owner_report"]
    bridge = data["bridge_observations"]
    if not isinstance(owner, dict) or not isinstance(bridge, dict):
        raise ValueError("Missing owner or bridge evidence")
    if set(owner) != {
        "create_result", "new_process_readback", "case_distribution",
        "claimed_sha256", "real_gold_or_keys_used",
    }:
        raise ValueError("Unexpected owner evidence")
    if (owner["create_result"] != PASS
        or owner["new_process_readback"] != PASS
        or owner["case_distribution"] != {"legacy": 9, "primary": 12}
        or owner["real_gold_or_keys_used"] is not False):
        raise ValueError("Owner fake-only packet evidence incomplete")
    sha = owner["claimed_sha256"]
    if not isinstance(sha, str) or len(sha) != 64 or any(x not in "0123456789abcdef" for x in sha):
        raise ValueError("Missing or noncanonical fake-only packet digest")
    if set(bridge) != {"bounded_reader", "read_only_sandbox_open", "inherit_sandbox_open", "git_status_after"}:
        raise ValueError("Unexpected Bridge evidence")
    if bridge["bounded_reader"] != TOOL_ROOT_DENIED or bridge["git_status_after"] != PASS:
        raise ValueError("Bridge baseline or bounded reader evidence unqualified")
    read_only = bridge["read_only_sandbox_open"]
    inherited = bridge["inherit_sandbox_open"]
    if read_only not in ALLOWED_OS_STATUSES or inherited not in ALLOWED_OS_STATUSES:
        raise ValueError("Unsupported Windows access observation")
    if not isinstance(data["research_boundary"], str) or data["research_boundary"] != "R0_P03_UNSCORED_FAKE_C1_CUSTODY_ONLY":
        raise ValueError("Scope mismatch")
    observed_os_denial = read_only == inherited == OS_DENIED
    any_read = read_only == READ_SUCCEEDED or inherited == READ_SUCCEEDED
    if any_read:
        scoped_status = "OWNER_FAKE_PACKET_SAFETY_BARRIER_FAILED"
    elif observed_os_denial:
        scoped_status = "FAKE_C1_OWNER_READBACK_AND_TWO_SANDBOX_OS_DENIALS_OBSERVED"
    else:
        scoped_status = "FAKE_C1_OWNER_READBACK_AND_TOOL_SCOPE_ONLY_OS_DENIAL_UNVERIFIED"
    return {
        "scope": data["research_boundary"],
        "synthetic_complete_packet_owner_report": PASS,
        "bounded_reader_refusal": TOOL_ROOT_DENIED,
        "os_denial_both_sandbox_routes": PASS if observed_os_denial else NOT_EXERCISED,
        "scoped_status": scoped_status,
        "full_real_gold_custody_qualified": False,
        "real_r0_p03_score_authorized": False,
    }


def classify_file(path: Path) -> dict[str, Any]:
    return classify(json.loads(path.read_text(encoding="utf-8")))


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        raise SystemExit("usage: python -m experiments.r0_p03_navigation_probe.synthetic_custody_evidence_candidate EVIDENCE_JSON")
    print(json.dumps(classify_file(Path(sys.argv[1])), indent=2))
