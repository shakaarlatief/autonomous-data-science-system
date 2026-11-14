"""Experimental admission contract for copied GitHub-native CI read results.

Research 512 section 9 owns natural J2 fact kinds; Research 673 owns the
prospective scientific method; Research 676 binds four accepted experimental
J1 effects. Research 681 and Checkpoint 942 observed actual GitHub native CI
outcomes for two distinct commits.

This verifier is deliberately offline. It can re-check local Git object
ancestry, exact source snapshot bytes and the internal structural consistency
of copied GitHub API results. It CANNOT independently authenticate the GitHub
API transport, native provider execution, originating model, owner identity,
or live/current CI outcome. Every decision is explicitly UNQUALIFIED_OFFLINE.
No source copy may become an authenticated provider credential or governing
J2 RELATIONAL claim.

The exact eight-check comparator set is a frozen, exploratory case-local
diagnostic. It is not a proposed universal required-check policy or a formal
R0-P03 experiment.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from hashlib import sha256
import json
from pathlib import Path
import subprocess
from typing import Any, Mapping

from experiments.r0_p03_navigation_probe import (
    v03_typed_j2_assurance_port_v01 as j2,
)

ROOT = Path(__file__).resolve().parents[2]
SNAPSHOT = Path(__file__).with_name("v03_provider_ci_receipt_source_snapshot_v01.json")
OUTPUT = Path(__file__).with_name("v03_provider_ci_receipt_admission_result_v01.json")
SNAPSHOT_SHA256 = "cd37b2222f9efd1e10ba0c884f2fe27af63209abf7605015b7267f265de610bd"
REPO = "shakaarlatief/autonomous-data-science-system"
OLD = "511224a037bf63031ead0eda61754702361eebd7"
NEW = "e29329b3097b593a917a386d33f900a3cf97b193"
PARENTS = {
    OLD: "5304f10d5c2943fcca50303c3282ad56b1b519d8",
    NEW: "36ab6cd33a31d579c68b6b814ca70b1fae59fc40",
}
SOURCE_ROLE = "DERIVED_EXPOSED_MODEL_TRANSCRIPTION_OF_GITHUB_APP_API_READS"
EXPECTED_CHECK_TO_WORKFLOW = {
    "validate-collaboration-state (ubuntu-latest)": "Model collaboration state",
    "validate-collaboration-state (windows-latest)": "Model collaboration state",
    "repository-integrity (ubuntu-latest)": "Repository integrity",
    "repository-integrity (windows-latest)": "Repository integrity",
    "validate-current-routing (ubuntu-latest)": "Current routing consistency",
    "validate-current-routing (windows-latest)": "Current routing consistency",
    "validate": "Checkpoint metadata",
    "validate-knowledge-map": "Knowledge map integrity",
}
CHECK_FIELDS = frozenset({
    "id", "name", "head_sha", "workflow_run_id", "status",
    "conclusion", "app_slug", "app_id",
})
WORKFLOW_FIELDS = frozenset({
    "id", "name", "head_sha", "event", "attempt", "status",
    "conclusion", "actor_login",
})
CASE_FIELDS = frozenset({
    "commit_sha", "run_created_at_utc", "git_commit_signature",
    "check_runs", "workflow_runs",
})
TOP_FIELDS = frozenset({
    "schema_version", "record_class", "offline_provider_authentication",
    "source_provider", "repository_full_name", "inspection_date",
    "observation_methods", "source_assurance_limit",
    "qualified_j2_relational_claims",
    "not_a_governing_effect_or_formal_p03_task", "source_relative_cases",
})


class Diagnostic(str, Enum):
    STRUCTURALLY_GREEN_UNAUTHENTICATED_REPLAY = (
        "STRUCTURALLY_GREEN_UNAUTHENTICATED_REPLAY"
    )
    STRUCTURALLY_RED_UNAUTHENTICATED_REPLAY = (
        "STRUCTURALLY_RED_UNAUTHENTICATED_REPLAY"
    )
    HOLD_SOURCE_SHA_MISMATCH = "HOLD_SOURCE_SHA_MISMATCH"
    HOLD_INCOMPLETE_OR_MISSING = "HOLD_INCOMPLETE_OR_MISSING"
    REJECT_UNTRUSTED_COPY = "REJECT_UNTRUSTED_COPY"


@dataclass(frozen=True)
class Assessment:
    """An offline structural decision is never a governing proof."""

    diagnostic: Diagnostic
    target_sha: str
    presented_sha: str
    success_count: int
    failure_count: int
    missing_count: int
    genuine_provider_authentication: bool = False
    model_or_connector_identity_authenticated: bool = False
    qualified_j2_relational: bool = False
    eligible_for_j3_completion: bool = False


def _fields(obj: Any, expected: frozenset[str], kind: str) -> None:
    if not isinstance(obj, dict) or set(obj) != expected:
        raise ValueError(f"RECEIPT_{kind}_SCHEMA_OR_AUTHORITY_INJECTION")


def _commit_sha(sha: Any) -> bool:
    return isinstance(sha, str) and len(sha) == 40 and all(
        char in "0123456789abcdef" for char in sha
    )


def _integer(value: Any) -> bool:
    return type(value) is int and value > 0


def _git(*args: str) -> str:
    process = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if process.returncode:
        raise ValueError("RECEIPT_ORIGINAL_GIT_SOURCE_UNAVAILABLE")
    return process.stdout.strip()


def verified_local_git_ancestry() -> dict[str, str]:
    """Verify only locally reproducible commit/parent facts, not CI transport."""
    observed: dict[str, str] = {}
    for sha, parent in PARENTS.items():
        if _git("rev-parse", f"{sha}^{{commit}}") != sha:
            raise ValueError("RECEIPT_SOURCE_COMMIT_ID_CONTRADICTION")
        observed_parent = _git("show", "-s", "--format=%P", sha)
        if observed_parent != parent:
            raise ValueError("RECEIPT_SOURCE_COMMIT_PARENT_CONTRADICTION")
        observed[sha] = observed_parent
    return observed


def original_snapshot() -> dict[str, Any]:
    """Freeze transcription, never infer source authenticity from its digest."""
    data = SNAPSHOT.read_bytes()
    if sha256(data).hexdigest() != SNAPSHOT_SHA256:
        raise ValueError("RECEIPT_SOURCE_TRANSCRIPTION_BYTES_DRIFT")
    value = json.loads(data)
    validate_snapshot(value)
    return value


def validate_snapshot(value: Mapping[str, Any]) -> None:
    """Validate schema, exact source scope, run/check binding and status coherence.

    This accepts a well-formed *copy*, not independently verified GitHub data.
    A malicious actor who rewrites both the copy and expected digest can still
    forge a structurally green observation. Real admission requires a trusted
    provider adapter and an explicit accepted-effect evidence policy.
    """
    _fields(value, TOP_FIELDS, "TOP")
    if (
        value["schema_version"] != 1
        or value["record_class"] != SOURCE_ROLE
        or value["offline_provider_authentication"] is not False
        or value["source_provider"] != "github.com"
        or value["repository_full_name"] != REPO
        or value["inspection_date"] != "2026-11-14"
        or value["observation_methods"] != [
            "github_list_check_runs_for_ref", "github_get_workflow_run",
            "github_fetch_git_commit",
        ]
        or not isinstance(value["source_assurance_limit"], str)
        or "not a signed response" not in value["source_assurance_limit"]
        or value["qualified_j2_relational_claims"] != 0
        or value["not_a_governing_effect_or_formal_p03_task"] is not True
    ):
        raise ValueError("RECEIPT_UNTRUSTED_COPY_ATTEMPTS_AUTHORITY_UPGRADE")
    cases = value["source_relative_cases"]
    if not isinstance(cases, list) or len(cases) != 2:
        raise ValueError("RECEIPT_EXACT_TWO_SOURCE_CASES_REQUIRED")
    if [case.get("commit_sha") for case in cases if isinstance(case, dict)] != [OLD, NEW]:
        raise ValueError("RECEIPT_SOURCE_CASE_ORDER_OR_SHA_CHANGED")
    for case in cases:
        validate_case(case)


def validate_case(case: Mapping[str, Any]) -> None:
    """A hard negative case cannot be hidden by a matching successful job."""
    _fields(case, CASE_FIELDS, "CASE")
    sha = case["commit_sha"]
    if sha not in PARENTS or not _commit_sha(sha):
        raise ValueError("RECEIPT_CASE_SHA_NOT_ORIGINAL")
    if (
        not isinstance(case["run_created_at_utc"], str)
        or not case["run_created_at_utc"].endswith("Z")
        or len(case["run_created_at_utc"]) != 20
    ):
        raise ValueError("RECEIPT_RUN_CREATED_AT_INVALID")
    _fields(case["git_commit_signature"], frozenset({"verified", "reason"}), "SIGNATURE")
    if case["git_commit_signature"] != {"verified": False, "reason": "unsigned"}:
        raise ValueError("RECEIPT_UNSIGNED_COMMIT_FALSE_IDENTITY_PROOF")
    checks, runs = case["check_runs"], case["workflow_runs"]
    if not isinstance(checks, list) or not isinstance(runs, list):
        raise ValueError("RECEIPT_CHECKS_OR_RUNS_NOT_ARRAY")
    if len(checks) != 8 or len(runs) != 5:
        raise ValueError("RECEIPT_INCOMPLETE_RUN_OR_CHECK_SET")
    if {r["name"] for r in runs if isinstance(r, dict)} != set(EXPECTED_CHECK_TO_WORKFLOW.values()):
        raise ValueError("RECEIPT_EXPECTED_WORKFLOW_SET_CHANGED")
    if {c["name"] for c in checks if isinstance(c, dict)} != set(EXPECTED_CHECK_TO_WORKFLOW):
        raise ValueError("RECEIPT_EXPECTED_CHECK_SET_CHANGED")
    if len({c["name"] for c in checks}) != len(checks):
        raise ValueError("RECEIPT_DUPLICATE_CHECK_NAME")
    if len({c["id"] for c in checks}) != len(checks):
        raise ValueError("RECEIPT_DUPLICATE_CHECK_ID")
    if len({r["id"] for r in runs}) != len(runs):
        raise ValueError("RECEIPT_DUPLICATE_WORKFLOW_ID")
    indexed: dict[int, Mapping[str, Any]] = {}
    for run in runs:
        _fields(run, WORKFLOW_FIELDS, "RUN")
        if not _integer(run["id"]) or not _integer(run["attempt"]):
            raise ValueError("RECEIPT_INVALID_RUN_ID_OR_ATTEMPT")
        if run["attempt"] != 1 or run["head_sha"] != sha or run["event"] != "push":
            raise ValueError("RECEIPT_WRONG_RUN_ATTEMPT_EVENT_OR_SHA")
        if run["actor_login"] != "shakaarlatief":
            raise ValueError("RECEIPT_GITHUB_ACCOUNT_IS_NOT_MODEL_IDENTITY")
        if run["status"] != "completed" or run["conclusion"] not in ("success", "failure"):
            raise ValueError("RECEIPT_INCOMPLETE_RUN_RESULT")
        indexed[run["id"]] = run
    by_run: dict[int, list[str]] = {key: [] for key in indexed}
    for check in checks:
        _fields(check, CHECK_FIELDS, "CHECK")
        if not _integer(check["id"]) or not _integer(check["workflow_run_id"]):
            raise ValueError("RECEIPT_CHECK_ID_INVALID")
        if check["head_sha"] != sha or check["workflow_run_id"] not in indexed:
            raise ValueError("RECEIPT_CROSS_SHA_OR_MISSING_RUN")
        if check["app_slug"] != "github-actions" or check["app_id"] != 15368:
            raise ValueError("RECEIPT_PROVIDER_APP_NOT_MATCHED")
        if check["name"] not in EXPECTED_CHECK_TO_WORKFLOW:
            raise ValueError("RECEIPT_UNKNOWN_CHECK_NAME")
        linked = indexed[check["workflow_run_id"]]
        if linked["name"] != EXPECTED_CHECK_TO_WORKFLOW[check["name"]]:
            raise ValueError("RECEIPT_CHECK_NOT_BELONGING_TO_WORKFLOW")
        if check["status"] != "completed" or check["conclusion"] not in ("success", "failure"):
            raise ValueError("RECEIPT_INCOMPLETE_CHECK_RESULT")
        by_run[check["workflow_run_id"]].append(check["conclusion"])
    for run_id, reported in by_run.items():
        if not reported:
            raise ValueError("RECEIPT_ORPHAN_WORKFLOW_WITHOUT_CHECK")
        aggregate = "failure" if "failure" in reported else "success"
        if indexed[run_id]["conclusion"] != aggregate:
            raise ValueError("RECEIPT_WORKFLOW_CHECK_OUTCOME_CONTRADICTION")


def assess(
    case: Mapping[str, Any], target_sha: str,
) -> Assessment:
    """Reject cross-SHA reuse; return only unqualified replay diagnostics."""
    if not _commit_sha(target_sha):
        raise ValueError("RECEIPT_TARGET_SHA_INVALID")
    presented = case.get("commit_sha") if isinstance(case, Mapping) else None
    if presented != target_sha:
        return Assessment(
            Diagnostic.HOLD_SOURCE_SHA_MISMATCH,
            target_sha, presented if isinstance(presented, str) else "",
            success_count=0, failure_count=0, missing_count=8,
        )
    try:
        validate_case(case)
    except (ValueError, TypeError, KeyError):
        return Assessment(
            Diagnostic.REJECT_UNTRUSTED_COPY,
            target_sha, presented, success_count=0, failure_count=0, missing_count=8,
        )
    successes = sum(c["conclusion"] == "success" for c in case["check_runs"])
    failures = sum(c["conclusion"] == "failure" for c in case["check_runs"])
    status = (
        Diagnostic.STRUCTURALLY_GREEN_UNAUTHENTICATED_REPLAY
        if failures == 0
        else Diagnostic.STRUCTURALLY_RED_UNAUTHENTICATED_REPLAY
    )
    return Assessment(
        status, target_sha, presented,
        success_count=successes, failure_count=failures, missing_count=0,
    )


def build() -> dict[str, Any]:
    snapshot = original_snapshot()
    observed_git = verified_local_git_ancestry()
    source_context = j2.actual_source_context()
    if source_context.accepted_effects != j2.accepted.EXPECTED_EFFECT_IDS:
        raise ValueError("RECEIPT_ACCEPTED_J1_SOURCE_DRIFT")
    if source_context.natural_owner_authenticator_available:
        raise ValueError("RECEIPT_FALSE_NATURAL_OWNER_AUTHENTICATOR")
    if source_context.provider_native_receipt_verifier_available:
        raise ValueError("RECEIPT_FALSE_SOURCE_PORT_PROVIDER_VERIFIER")

    assessments = [
        assess(case, case["commit_sha"])
        for case in snapshot["source_relative_cases"]
    ]
    if [
        (a.diagnostic, a.success_count, a.failure_count, a.missing_count)
        for a in assessments
    ] != [
        (Diagnostic.STRUCTURALLY_RED_UNAUTHENTICATED_REPLAY, 6, 2, 0),
        (Diagnostic.STRUCTURALLY_GREEN_UNAUTHENTICATED_REPLAY, 8, 0, 0),
    ]:
        raise ValueError("RECEIPT_HISTORICAL_SOURCE_CASE_RESULT_DRIFT")
    return {
        "schema_version": 1,
        "research_scope": "R0_P03_V2_EXPOSED_UNSCORED_RECEIPT_TRUST_ROOT_PROTOCOL",
        "source_copy_sha256": SNAPSHOT_SHA256,
        "source_class": SOURCE_ROLE,
        "source_git_parent_reverified": observed_git,
        "cases": [
            {
                "head_sha": a.target_sha,
                "diagnostic": a.diagnostic.value,
                "source_replay_succeeded_check_count": a.success_count,
                "source_replay_failed_check_count": a.failure_count,
                "missing_count": a.missing_count,
                "independently_authenticated_provider_receipt_offline":
                    a.genuine_provider_authentication,
                "independently_authenticated_model_or_connector":
                    a.model_or_connector_identity_authenticated,
                "qualified_j2_relational": a.qualified_j2_relational,
                "j3_completion_admissible": a.eligible_for_j3_completion,
            }
            for a in assessments
        ],
        "operationally_observed_online": {
            "github_provider_api_was_actually_called_in_exposed_interaction": True,
            "online_source_results_transcribed_into_this_untrusted_copy": True,
            "this_program_can_requery_provider_api": False,
            "this_file_is_signed_by_github": False,
            "copy_can_serve_as_independent_provider_authentication": False,
            "real_time_current_head_ci_pass_proven_by_this_file": False,
            "bridge_authenticated_app_source_adapter_is_a_future_integration_candidate": True,
        },
        "trust_root_requirements_for_future_qualified_provider_adapter": [
            "Explicit allowlisted provider account and repository binding",
            "Server-owned authenticated read with no caller-selected token or host",
            "Native check-run and workflow-run ID with exact commit SHA and attempt",
            "Provider-owned status and issuer app identity from a live response",
            "Re-query/reconciliation for retries, reruns, missing checks and stale results",
            "Source-owner/actor authentication verified independently from Git authorship",
            "Accepted J1 component semantic match and explicit J2 fact-class qualification",
            "No promotion of a copied JSON envelope or derived index to source authority",
        ],
        "qualification": {
            "original_accepted_experiment_only_j1_count": len(source_context.accepted_effects),
            "new_accepted_j1": 0,
            "new_qualified_relational_j2": 0,
            "independently_verified_original_d1_connector_transport": False,
            "historical_e01_j3": "HOLD",
            "new_j3_completion_certified": False,
            "formal_r0_p03_score": None,
            "physical_architecture_selected": False,
            "current_branch_prepush_ci_enforced": "NOT_ESTABLISHED",
        },
        "next": "INTEGRATE_REAL_TRUSTED_PROVIDER_SOURCE_ADAPTER_AND_OWNER_AUTHENTICATION_WITHOUT_SELF_CERTIFICATION",
    }


def main() -> None:
    result = build()
    text = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if OUTPUT.exists():
        if OUTPUT.read_text("utf8") != text:
            raise RuntimeError("RECEIPT_RESULT_IMMUTABLE_SOURCE_DRIFT")
    else:
        with OUTPUT.open("x", encoding="utf8", newline="\n") as stream:
            stream.write(text)
    print(json.dumps({
        "status": result["research_scope"],
        "historical_ci_failure_count": result["cases"][0]["source_replay_failed_check_count"],
        "later_ci_success_count": result["cases"][1]["source_replay_succeeded_check_count"],
        "provider_receipt_authenticated_by_program": False,
        "new_qualified_j2": result["qualification"]["new_qualified_relational_j2"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
