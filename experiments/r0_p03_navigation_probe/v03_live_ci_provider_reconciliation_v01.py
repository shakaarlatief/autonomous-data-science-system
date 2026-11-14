"""Live-source status reconciliation prototype over an actual GitHub App read.

Scope: Research 683, Checkpoint 944, under Research 512 J2 fact classification.
All source provider fields originate in a *derived relay* of a connected
GitHub App tool call. The copied JSON is NOT a signed provider receipt.
This code can verify the exact original Git source commit/parent and can
evaluate cross-endpoint coherence, but it cannot authenticate the connector
transport or the originating model from copied bytes.

The code deliberately distinguishes:
  (1) source status consistency among check, job, workflow and step records;
  (2) independently authenticated provider evidence (NOT implemented);
  (3) source-owner authenticated RELATIONAL coverage (NOT implemented);
  (4) governing J3 satisfaction (NOT implemented).

A parent workflow SUCCESS and completed steps do NOT override an individual
job reporting IN_PROGRESS with SUCCESS and a completion timestamp.
No existing or future GitHub workflow/check names are globally made required.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from hashlib import sha256
import json
from pathlib import Path
import subprocess
from typing import Any, Mapping

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).with_name("v03_live_ci_provider_conflict_source_v01.json")
RESULT = Path(__file__).with_name("v03_live_ci_provider_reconciliation_result_v01.json")
SOURCE_SHA256 = "1d968a4eb516780c70cfd70ae51a82eadbcad8e92e043b861a2a1f5b0c776bf2"
REPOSITORY = "shakaarlatief/autonomous-data-science-system"
COMMIT = "2a7f8fe3f170840262122296d9b7f3e54664bc39"
PARENT = "e29329b3097b593a917a386d33f900a3cf97b193"
CHECK_ID = 132565047313
RUN_ID = 43633469851
SOURCE_ROLE = "DERIVED_COORDINATOR_RELAY_OF_LIVE_CONNECTED_GITHUB_APP_READS"
EXPECTED_TOOLS = (
    "github_list_check_runs_for_ref",
    "github_get_check_run",
    "github_get_workflow_run",
    "github_fetch_workflow_run_jobs",
    "github_fetch_workflow_job_steps",
    "codex_github_authorization_metadata",
)


class Coherence(str, Enum):
    SOURCE_REPORTED_CONTRADICTION = "SOURCE_REPORTED_CONTRADICTION"
    SOURCE_REPORTED_COMPLETE_SUCCESS = "SOURCE_REPORTED_COMPLETE_SUCCESS"
    SOURCE_REPORTED_FAILURE = "SOURCE_REPORTED_FAILURE"
    HOLD_INCOMPLETE = "HOLD_INCOMPLETE"
    HOLD_MISSING = "HOLD_MISSING"
    REJECT_WRONG_SHA = "REJECT_WRONG_SHA"
    REJECT_UNTRUSTED_SOURCE_SHAPE = "REJECT_UNTRUSTED_SOURCE_SHAPE"


@dataclass(frozen=True)
class Assessment:
    coherence: Coherence
    target_sha: str
    checked_ref_count: int
    completed_success_count: int
    completed_failure_count: int
    conflicting_check_ids: tuple[int, ...]
    reasons: tuple[str, ...]
    independent_provider_authentication: bool = False
    model_or_connector_identity_authenticated: bool = False
    governing_j2_relational_qualified: bool = False
    governing_j3_complete: bool = False


def _schema(obj: Any, keys: frozenset[str], error: str) -> None:
    if not isinstance(obj, dict) or set(obj) != keys:
        raise ValueError(error)


TOP_KEYS = frozenset({
    "schema_version", "source_role", "source_authentication_from_copied_file",
    "record_is_governing", "source_observation_date_utc", "repository_full_name",
    "target_git_sha", "source_commit_parent", "provider_auth_mode_reported",
    "source_credential_server_owned", "provider_api_tools_used",
    "check_run", "workflow_run", "workflow_jobs", "steps", "ref_check_runs",
})
CHECK_KEYS = frozenset({
    "id", "name", "status", "conclusion", "head_sha", "check_suite_id",
    "started_at", "completed_at", "app_id", "app_slug", "annotations_count",
})
RUN_KEYS = frozenset({
    "id", "name", "workflow_id", "check_suite_id", "status", "conclusion",
    "head_sha", "event", "run_attempt", "actor_login",
})
JOB_KEYS = frozenset({
    "id", "run_id", "run_attempt", "name", "status", "conclusion",
    "started_at", "completed_at",
})
STEP_KEYS = frozenset({"number", "name", "status", "conclusion"})
REF_CHECK_KEYS = frozenset({
    "id", "name", "status", "conclusion", "head_sha", "app_id", "app_slug",
})


def recheck_real_git() -> dict[str, str]:
    """Git objects verify only exact ancestry, never remote workflow result."""
    actual = subprocess.run(
        ["git", "rev-parse", f"{COMMIT}^{{commit}}"],
        cwd=ROOT, capture_output=True, text=True, encoding="utf8",
    )
    parent = subprocess.run(
        ["git", "show", "-s", "--format=%P", COMMIT],
        cwd=ROOT, capture_output=True, text=True, encoding="utf8",
    )
    if (
        actual.returncode or parent.returncode
        or actual.stdout.strip() != COMMIT
        or parent.stdout.strip() != PARENT
    ):
        raise ValueError("LIVE_GIT_OBJECT_PARENT_NOT_VERIFIED")
    return {"commit": COMMIT, "parent": PARENT}


def source_relay() -> dict[str, Any]:
    """Pinned derived relay. SHA does not authenticate source provider."""
    raw = SOURCE.read_bytes()
    if sha256(raw).hexdigest() != SOURCE_SHA256:
        raise ValueError("LIVE_PROVIDER_RELAY_SOURCE_BYTE_DRIFT")
    obj = json.loads(raw)
    validate_schema(obj)
    return obj


def validate_schema(obj: Any) -> None:
    """Validate shape without promoting a model-authored source copy."""
    _schema(obj, TOP_KEYS, "LIVE_SOURCE_TOP_SCHEMA_OR_PROOF_INJECTION")
    if (
        type(obj["schema_version"]) is not int
        or obj["schema_version"] != 1
        or obj["source_role"] != SOURCE_ROLE
        or obj["source_authentication_from_copied_file"] is not False
        or obj["record_is_governing"] is not False
        or obj["source_observation_date_utc"] != "2026-11-14"
        or obj["repository_full_name"] != REPOSITORY
        or obj["source_commit_parent"] != PARENT
        or obj["provider_auth_mode_reported"] != "github-app-user-token-device-flow"
        or obj["source_credential_server_owned"] is not True
        or obj["provider_api_tools_used"] != list(EXPECTED_TOOLS)
    ):
        raise ValueError("LIVE_SOURCE_RELAY_SCOPE_OR_ASSURANCE_FALSIFIED")
    _schema(obj["check_run"], CHECK_KEYS, "LIVE_CHECK_RUN_SCHEMA")
    _schema(obj["workflow_run"], RUN_KEYS, "LIVE_WORKFLOW_RUN_SCHEMA")
    for key, keys, error in (
        ("workflow_jobs", JOB_KEYS, "LIVE_WORKFLOW_JOB_SCHEMA"),
        ("steps", STEP_KEYS, "LIVE_STEP_SCHEMA"),
        ("ref_check_runs", REF_CHECK_KEYS, "LIVE_REF_CHECK_SCHEMA"),
    ):
        if not isinstance(obj[key], list):
            raise ValueError(error)
        for row in obj[key]:
            _schema(row, keys, error)


def assess(source: Mapping[str, Any], target_sha: str) -> Assessment:
    """Return a source-status diagnosis with ZERO provider/actor admission.

    Invalid structure and cross-source IDs never yield a positive diagnosis.
    Source status conflicts are separated from completed provider-reported
    failures, pending results, and missing evidence.
    """
    if not isinstance(source, Mapping):
        return Assessment(Coherence.REJECT_UNTRUSTED_SOURCE_SHAPE, target_sha, 0, 0, 0, (), ("SOURCE_NOT_A_MAPPING",))
    if target_sha != COMMIT or source.get("target_git_sha") != target_sha:
        return Assessment(Coherence.REJECT_WRONG_SHA, target_sha, 0, 0, 0, (), ("EXACT_SOURCE_SHA_MISMATCH",))
    try:
        validate_schema(source)
    except (ValueError, TypeError, AttributeError):
        return Assessment(Coherence.REJECT_UNTRUSTED_SOURCE_SHAPE, target_sha, 0, 0, 0, (), ("SOURCE_SCHEMA_OR_AUTHORITY_BROKEN",))

    check, run = source["check_run"], source["workflow_run"]
    jobs, steps, refs = source["workflow_jobs"], source["steps"], source["ref_check_runs"]
    if (
        check["id"] != CHECK_ID or check["head_sha"] != target_sha
        or run["id"] != RUN_ID or run["head_sha"] != target_sha
        or run["event"] != "push" or run["run_attempt"] != 1
        or check["check_suite_id"] != run["check_suite_id"]
        or check["app_id"] != 15368 or check["app_slug"] != "github-actions"
        or not isinstance(run["actor_login"], str)
        or not run["actor_login"]
    ):
        return Assessment(Coherence.REJECT_UNTRUSTED_SOURCE_SHAPE, target_sha, 0, 0, 0, (), ("PROVIDER_OR_COMMIT_BINDING_INVALID",))

    if (
        not refs or len(refs) != 8
        or len({v["id"] for v in refs}) != 8
        or len({v["name"] for v in refs}) != 8
        or any(v["head_sha"] != target_sha or v["app_id"] != 15368
               or v["app_slug"] != "github-actions" for v in refs)
        or len(jobs) != 2 or len({j["id"] for j in jobs}) != 2
        or any(j["run_id"] != RUN_ID or j["run_attempt"] != 1 for j in jobs)
        or len(steps) != 5 or len({s["number"] for s in steps}) != 5
    ):
        return Assessment(Coherence.HOLD_MISSING, target_sha, len(refs), 0, 0, (), ("MISSING_OR_DUPLICATE_ACTUAL_SOURCE_RESOURCE",))

    named = {v["id"]: v for v in refs}
    named_jobs = {j["id"]: j for j in jobs}
    if CHECK_ID not in named or CHECK_ID not in named_jobs:
        return Assessment(Coherence.HOLD_MISSING, target_sha, len(refs), 0, 0, (), ("TARGET_CHECK_OR_JOB_NOT_RETURNED",))
    member = named[CHECK_ID]
    job = named_jobs[CHECK_ID]
    if (
        (member["name"] != check["name"] or member["status"] != check["status"]
         or member["conclusion"] != check["conclusion"])
        or (job["name"] != check["name"] or job["status"] != check["status"]
            or job["conclusion"] != check["conclusion"])
    ):
        return Assessment(
            Coherence.SOURCE_REPORTED_CONTRADICTION, target_sha, len(refs), 0, 0,
            (CHECK_ID,), ("SAME_CHECK_ID_CONTRADICTORY_ENDPOINT_FIELDS",),
        )

    successful = sum(x["status"] == "completed" and x["conclusion"] == "success" for x in refs)
    failures = sum(x["status"] == "completed" and x["conclusion"] == "failure" for x in refs)
    reasons: list[str] = []
    conflict_ids: list[int] = []
    for row in refs:
        if row["status"] not in {"completed", "in_progress", "queued"}:
            reasons.append("UNKNOWN_CHECK_STATUS")
            conflict_ids.append(row["id"])
        elif row["status"] != "completed" and row["conclusion"] is not None:
            reasons.append("NONTERMINAL_CHECK_WITH_TERMINAL_CONCLUSION")
            conflict_ids.append(row["id"])
        elif row["status"] == "completed" and row["conclusion"] not in {"success", "failure"}:
            reasons.append("TERMINAL_CHECK_WITH_MISSING_OR_UNSUPPORTED_CONCLUSION")
            conflict_ids.append(row["id"])
    if check["status"] == "in_progress" and check["completed_at"]:
        reasons.append("NONTERMINAL_CHECK_HAS_COMPLETED_AT")
        conflict_ids.append(CHECK_ID)
    if job["status"] == "in_progress" and job["completed_at"]:
        reasons.append("NONTERMINAL_JOB_HAS_COMPLETED_AT")
        conflict_ids.append(CHECK_ID)
    if (
        run["status"] == "completed" and job["status"] != "completed"
        and run["conclusion"] in {"success", "failure"}
    ):
        reasons.append("COMPLETED_WORKFLOW_CONFLICTS_WITH_NONTERMINAL_JOB")
        conflict_ids.append(CHECK_ID)
    if (
        run["status"] == "completed" and run["conclusion"] == "success"
        and any(x["id"] in named_jobs and x["status"] == "completed"
                and x["conclusion"] == "failure" for x in refs)
    ):
        reasons.append("SUCCESSFUL_WORKFLOW_HAS_FAILED_ASSOCIATED_CHECK")
        conflict_ids.append(CHECK_ID)
    if (
        job["status"] == "completed" and job["conclusion"] == "success"
        and any(s["status"] == "completed" and s["conclusion"] == "failure" for s in steps)
    ):
        reasons.append("SUCCESSFUL_JOB_HAS_FAILED_STEP")
        conflict_ids.append(CHECK_ID)
    if run["status"] != "completed" and run["conclusion"] is not None:
        reasons.append("NONTERMINAL_RUN_WITH_TERMINAL_CONCLUSION")
        conflict_ids.append(CHECK_ID)
    if reasons:
        return Assessment(
            Coherence.SOURCE_REPORTED_CONTRADICTION, target_sha,
            len(refs), successful, failures,
            tuple(sorted(set(conflict_ids))), tuple(dict.fromkeys(reasons)),
        )

    if failures:
        return Assessment(
            Coherence.SOURCE_REPORTED_FAILURE, target_sha,
            len(refs), successful, failures, (), ("REPORTED_CHECK_FAILURE",),
        )
    if (
        run["status"] != "completed" or run["conclusion"] != "success"
        or any(j["status"] != "completed" or j["conclusion"] != "success" for j in jobs)
        or any(s["status"] != "completed" or s["conclusion"] != "success" for s in steps)
        or successful != len(refs)
    ):
        return Assessment(
            Coherence.HOLD_INCOMPLETE, target_sha,
            len(refs), successful, failures, (),
            ("PROVIDER_SOURCE_NOT_FULLY_COMPLETED",),
        )
    return Assessment(
        Coherence.SOURCE_REPORTED_COMPLETE_SUCCESS, target_sha,
        len(refs), successful, failures, (),
        ("COPY_STRUCTURALLY_COHERENT_NOT_PROVIDER_AUTHENTICATED",),
    )


def build() -> dict[str, Any]:
    original = source_relay()
    git = recheck_real_git()
    evaluation = assess(original, COMMIT)
    if evaluation.coherence != Coherence.SOURCE_REPORTED_CONTRADICTION:
        raise RuntimeError("LIVE_SOURCE_CONFLICT_DISAPPEARED_FROM_PINNED_OBSERVATION")
    if evaluation.completed_success_count != 7 or CHECK_ID not in evaluation.conflicting_check_ids:
        raise RuntimeError("LIVE_SOURCE_CI_COUNT_OR_CONTRADICTION_CHANGED")
    return {
        "schema_version": 1,
        "world": "R0_P03_UNSCORED_SOURCE_RECONCILIATION",
        "source_role": SOURCE_ROLE,
        "source_sha256": SOURCE_SHA256,
        "verified_git": git,
        "target_commit": COMMIT,
        "conflicting_check_id": CHECK_ID,
        "workflow_run_id": RUN_ID,
        "source_status": evaluation.coherence.value,
        "source_reported_completed_success_count": evaluation.completed_success_count,
        "source_reported_completed_failure_count": evaluation.completed_failure_count,
        "source_reported_total_checks": evaluation.checked_ref_count,
        "conflict_reasons": list(evaluation.reasons),
        "all_five_steps_source_reported_complete_success": all(
            s["status"] == "completed" and s["conclusion"] == "success"
            for s in original["steps"]
        ),
        "parent_workflow_source_reported_completed_success": (
            original["workflow_run"]["status"] == "completed"
            and original["workflow_run"]["conclusion"] == "success"
        ),
        "connected_github_tool_was_used_in_exposed_interaction": True,
        "offline_copy_is_provider_signed": False,
        "independent_model_session_identity_authenticated": False,
        "self_authenticating_trust_root_created": False,
        "governing_j1_acceptances_added": 0,
        "governing_j2_relational_admissions_added": 0,
        "historical_e01_j3": "HOLD",
        "formal_r0_p03_score": None,
        "physical_target_selected": False,
        "suggested_next_step": "FINITELY_STOP_COPY_PROBES_AND_TEST_PROVIDER_OWNED_LIVE_COMPOSITE_READ_OR_SOURCE_OWNER_AUTHENTICITY",
    }


def main() -> None:
    outcome = build()
    content = json.dumps(outcome, sort_keys=True, ensure_ascii=False, indent=2) + "\n"
    if RESULT.exists():
        if RESULT.read_text("utf8") != content:
            raise RuntimeError("LIVE_RECONCILIATION_RESULT_IMMUTABLE_CONFLICT")
    else:
        with RESULT.open("x", encoding="utf8", newline="\n") as output:
            output.write(content)
    print(json.dumps({
        "source_status": outcome["source_status"],
        "completed_success": outcome["source_reported_completed_success_count"],
        "reported_total_checks": outcome["source_reported_total_checks"],
        "provider_authentication_from_copy": outcome["offline_copy_is_provider_signed"],
        "new_j2": outcome["governing_j2_relational_admissions_added"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
