"""Adversarial source-relative tests of the native-CI receipt admission boundary.

The copied observations are not authenticated GitHub API responses in the
offline runtime. A structurally green copy must NEVER qualify governing J2,
actor identity, provider execution or J3 completion.
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import replace
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_provider_ci_admission_contract_v01 as port,
)


@pytest.fixture(scope="module")
def source():
    return port.original_snapshot()


@pytest.fixture(scope="module")
def decision():
    return port.build()


def alter(base, check_index=0, change=None):
    specimen = deepcopy(base)
    if change is not None:
        specimen["check_runs"][check_index].update(change)
    return specimen


def test_original_source_snapshot_is_pinned_not_authenticated(source):
    assert source["record_class"] == port.SOURCE_ROLE
    assert source["offline_provider_authentication"] is False
    assert "not a signed response" in source["source_assurance_limit"]
    assert source["qualified_j2_relational_claims"] == 0
    assert source["not_a_governing_effect_or_formal_p03_task"] is True
    assert port.SNAPSHOT_SHA256 != ""


def test_original_git_commits_reverified_but_not_ci(source, decision):
    assert port.verified_local_git_ancestry() == port.PARENTS
    assert decision["source_git_parent_reverified"] == port.PARENTS


def test_negative_941_two_real_windows_failures(source):
    case = source["source_relative_cases"][0]
    a = port.assess(case, port.OLD)
    assert a.diagnostic == port.Diagnostic.STRUCTURALLY_RED_UNAUTHENTICATED_REPLAY
    assert (a.success_count, a.failure_count, a.missing_count) == (6, 2, 0)
    failures = {x["name"] for x in case["check_runs"] if x["conclusion"] == "failure"}
    assert failures == {
        "validate-collaboration-state (windows-latest)",
        "repository-integrity (windows-latest)",
    }


def test_positive_942_all_eight_github_source_observations(source):
    case = source["source_relative_cases"][1]
    a = port.assess(case, port.NEW)
    assert a.diagnostic == port.Diagnostic.STRUCTURALLY_GREEN_UNAUTHENTICATED_REPLAY
    assert (a.success_count, a.failure_count, a.missing_count) == (8, 0, 0)
    assert a.genuine_provider_authentication is False
    assert a.qualified_j2_relational is False


@pytest.mark.parametrize("index", [0, 1])
def test_criticallly_same_github_account_is_not_model_identity(source, index):
    case = source["source_relative_cases"][index]
    assert {r["actor_login"] for r in case["workflow_runs"]} == {"shakaarlatief"}
    assert {c["app_slug"] for c in case["check_runs"]} == {"github-actions"}
    a = port.assess(case, case["commit_sha"])
    assert a.model_or_connector_identity_authenticated is False
    assert a.eligible_for_j3_completion is False


def test_old_green_checks_cannot_validate_new_sha(source):
    old = source["source_relative_cases"][0]
    new = source["source_relative_cases"][1]
    assert port.assess(new, port.OLD).diagnostic == port.Diagnostic.HOLD_SOURCE_SHA_MISMATCH
    assert port.assess(old, port.NEW).diagnostic == port.Diagnostic.HOLD_SOURCE_SHA_MISMATCH


@pytest.mark.parametrize("value", ["", "123", "F" * 40, "x" * 40])
def test_invalid_target_sha_fails(value, source):
    with pytest.raises(ValueError, match="TARGET_SHA_INVALID"):
        port.assess(source["source_relative_cases"][1], value)


@pytest.mark.parametrize("field,replacement", [
    ("head_sha", port.OLD),
    ("app_id", 99999),
    ("app_slug", "fake-provider"),
    ("workflow_run_id", 101),
    ("status", "queued"),
    ("conclusion", "neutral"),
    ("id", 0),
])
def test_forged_or_incomplete_check_fields_rejected(source, field, replacement):
    modified = alter(source["source_relative_cases"][1], change={field: replacement})
    assert port.assess(modified, port.NEW).diagnostic == port.Diagnostic.REJECT_UNTRUSTED_COPY


@pytest.mark.parametrize("field,replacement", [
    ("head_sha", port.OLD),
    ("attempt", 2),
    ("event", "workflow_dispatch"),
    ("status", "queued"),
    ("conclusion", "failure"),
    ("id", -1),
    ("actor_login", "claude-signer"),
])
def test_forged_or_replayed_workflow_fields_rejected(source, field, replacement):
    copy = deepcopy(source["source_relative_cases"][1])
    copy["workflow_runs"][0][field] = replacement
    assert port.assess(copy, port.NEW).diagnostic == port.Diagnostic.REJECT_UNTRUSTED_COPY


def test_missing_check_is_not_a_pass(source):
    copy = deepcopy(source["source_relative_cases"][1])
    copy["check_runs"].pop()
    assert port.assess(copy, port.NEW).diagnostic == port.Diagnostic.REJECT_UNTRUSTED_COPY


def test_extra_check_is_not_automatically_required_and_cannot_be_smuggled(source):
    copy = deepcopy(source["source_relative_cases"][1])
    fake = deepcopy(copy["check_runs"][0])
    fake.update(id=234567, name="invented-check")
    copy["check_runs"].append(fake)
    assert port.assess(copy, port.NEW).diagnostic == port.Diagnostic.REJECT_UNTRUSTED_COPY


def test_duplicate_check_name_and_id_rejected(source):
    original = source["source_relative_cases"][1]
    copy = deepcopy(original)
    copy["check_runs"][0]["name"] = copy["check_runs"][1]["name"]
    assert port.assess(copy, port.NEW).diagnostic == port.Diagnostic.REJECT_UNTRUSTED_COPY
    copy = deepcopy(original)
    copy["check_runs"][0]["id"] = copy["check_runs"][1]["id"]
    assert port.assess(copy, port.NEW).diagnostic == port.Diagnostic.REJECT_UNTRUSTED_COPY


def test_workflow_link_to_wrong_named_run_rejected(source):
    copy = deepcopy(source["source_relative_cases"][1])
    original_run = copy["check_runs"][0]["workflow_run_id"]
    alternative = next(r["id"] for r in copy["workflow_runs"] if r["id"] != original_run)
    copy["check_runs"][0]["workflow_run_id"] = alternative
    assert port.assess(copy, port.NEW).diagnostic == port.Diagnostic.REJECT_UNTRUSTED_COPY


def test_provider_workflow_conclusion_must_consistently_reflect_check_outcomes(source):
    copy = deepcopy(source["source_relative_cases"][1])
    copy["check_runs"][0]["conclusion"] = "failure"
    assert port.assess(copy, port.NEW).diagnostic == port.Diagnostic.REJECT_UNTRUSTED_COPY


def test_unsupported_signed_commit_claim_not_authentication(source):
    copy = deepcopy(source["source_relative_cases"][1])
    copy["git_commit_signature"] = {"verified": True, "reason": "valid"}
    assert port.assess(copy, port.NEW).diagnostic == port.Diagnostic.REJECT_UNTRUSTED_COPY


@pytest.mark.parametrize("new_key,value", [
    ("provider_authenticated", True),
    ("source_owner_verified", True),
    ("qualified_relational_j2", True),
    ("new_j1_accepted", True),
    ("j3_satisfied", True),
])
def test_top_level_claim_cannot_smuggle_proof(source, new_key, value):
    copy = deepcopy(source)
    copy[new_key] = value
    with pytest.raises(ValueError, match="SCHEMA_OR_AUTHORITY_INJECTION"):
        port.validate_snapshot(copy)


def test_copied_source_cannot_promote_self_declared_trust_root(source):
    copy = deepcopy(source)
    copy["offline_provider_authentication"] = True
    with pytest.raises(ValueError, match="UNTRUSTED_COPY_ATTEMPTS_AUTHORITY_UPGRADE"):
        port.validate_snapshot(copy)


def test_adding_false_owner_relation_for_historical_e01_is_rejected(source):
    copy = deepcopy(source)
    copy["qualified_j2_relational_claims"] = 1
    with pytest.raises(ValueError, match="UNTRUSTED_COPY_ATTEMPTS_AUTHORITY_UPGRADE"):
        port.validate_snapshot(copy)


def test_adding_owner_identity_to_source_claim_schema_rejected(source):
    copy = deepcopy(source["source_relative_cases"][1])
    copy["check_runs"][0]["model_actor_proven"] = "ChatGPT"
    assert port.assess(copy, port.NEW).diagnostic == port.Diagnostic.REJECT_UNTRUSTED_COPY


def test_forged_fully_consistent_green_copy_is_still_unqualified(source):
    """A self-consistent forgery can fool structural checks, not gain authority."""
    copy = deepcopy(source["source_relative_cases"][0])
    for check in copy["check_runs"]:
        check["conclusion"] = "success"
    for run in copy["workflow_runs"]:
        run["conclusion"] = "success"
    a = port.assess(copy, port.OLD)
    assert a.diagnostic == port.Diagnostic.STRUCTURALLY_GREEN_UNAUTHENTICATED_REPLAY
    assert a.genuine_provider_authentication is False
    assert a.model_or_connector_identity_authenticated is False
    assert a.qualified_j2_relational is False
    assert a.eligible_for_j3_completion is False


def test_real_original_source_still_distinguishes_forgery_from_recorded_failures(source):
    copy = deepcopy(source)
    for check in copy["source_relative_cases"][0]["check_runs"]:
        check["conclusion"] = "success"
    for run in copy["source_relative_cases"][0]["workflow_runs"]:
        run["conclusion"] = "success"
    port.validate_snapshot(copy)  # structural validity alone is not authenticity
    assert port.assess(
        port.original_snapshot()["source_relative_cases"][0], port.OLD
    ).failure_count == 2


def test_immutable_original_snapshot_bytes_must_not_drift(monkeypatch):
    original = port.SNAPSHOT_SHA256
    monkeypatch.setattr(port, "SNAPSHOT_SHA256", "0" * 64)
    with pytest.raises(ValueError, match="TRANSCRIPTION_BYTES_DRIFT"):
        port.original_snapshot()
    assert original != "0" * 64


def test_result_stays_two_source_cases_and_all_unqualified(decision):
    assert decision["research_scope"] == "R0_P03_V2_EXPOSED_UNSCORED_RECEIPT_TRUST_ROOT_PROTOCOL"
    assert [c["source_replay_failed_check_count"] for c in decision["cases"]] == [2, 0]
    assert [c["source_replay_succeeded_check_count"] for c in decision["cases"]] == [6, 8]
    assert all(c["j3_completion_admissible"] is False for c in decision["cases"])
    assert all(c["independently_authenticated_provider_receipt_offline"] is False
               for c in decision["cases"])
    assert all(c["independently_authenticated_model_or_connector"] is False
               for c in decision["cases"])


def test_source_relative_currentness_not_just_old_success(decision):
    current = decision["operationally_observed_online"]
    assert current["this_program_can_requery_provider_api"] is False
    assert current["real_time_current_head_ci_pass_proven_by_this_file"] is False
    assert current["copy_can_serve_as_independent_provider_authentication"] is False


def test_existing_accepted_effects_and_original_j3_not_affected(decision):
    q = decision["qualification"]
    assert q["original_accepted_experiment_only_j1_count"] == 4
    assert q["new_accepted_j1"] == 0
    assert q["new_qualified_relational_j2"] == 0
    assert q["independently_verified_original_d1_connector_transport"] is False
    assert q["historical_e01_j3"] == "HOLD"
    assert q["new_j3_completion_certified"] is False
    assert q["formal_r0_p03_score"] is None
    assert q["physical_architecture_selected"] is False
    assert q["current_branch_prepush_ci_enforced"] == "NOT_ESTABLISHED"


def test_frozen_result_is_reproducible_and_not_provider_signed(decision):
    assert json.loads(port.OUTPUT.read_text("utf8")) == decision
    assert decision["operationally_observed_online"]["this_file_is_signed_by_github"] is False


def test_exact_two_cases_without_expanding_to_new_scored_task(source):
    assert source["not_a_governing_effect_or_formal_p03_task"] is True
    assert [c["commit_sha"] for c in source["source_relative_cases"]] == [port.OLD, port.NEW]
    assert len(source["source_relative_cases"]) == 2


def test_malformed_schema_rejected_at_source_snapshot_boundary(source):
    mutated = deepcopy(source)
    mutated.pop("source_provider")
    with pytest.raises(ValueError, match="TOP_SCHEMA"):
        port.validate_snapshot(mutated)


def test_foreign_repo_copy_rejected(source):
    mutated = deepcopy(source)
    mutated["repository_full_name"] = "different/account"
    with pytest.raises(ValueError, match="UNTRUSTED_COPY_ATTEMPTS_AUTHORITY_UPGRADE"):
        port.validate_snapshot(mutated)


def test_unexpected_workflow_name_rejected(source):
    modified = deepcopy(source["source_relative_cases"][1])
    modified["workflow_runs"][0]["name"] = "unknown-workflow"
    assert port.assess(modified, port.NEW).diagnostic == port.Diagnostic.REJECT_UNTRUSTED_COPY


def test_no_claim_as_signed_payload_or_source_owner_authentication(decision):
    requirements = decision["trust_root_requirements_for_future_qualified_provider_adapter"]
    assert len(requirements) >= 7
    assert any("Server-owned authenticated read" in x for x in requirements)
    assert any("Source-owner/actor authentication" in x for x in requirements)


def test_pinned_provider_source_and_derived_receipt_have_platform_neutral_bytes():
    """Exact pinned evidence blobs must never depend on Windows CRLF checkout.

    This checks the declared Git checkout rule and the actual raw working
    bytes. The source's cryptographic digest detects content drift; its
    .gitattributes -text binding stops cross-platform encoding drift.
    """
    from hashlib import sha256
    import subprocess

    for artifact in (port.SNAPSHOT, port.OUTPUT):
        relative = artifact.relative_to(port.ROOT).as_posix()
        attribute = subprocess.check_output(
            ["git", "check-attr", "text", "--", relative],
            cwd=port.ROOT, text=True, encoding="utf8",
        ).strip()
        assert attribute == f"{relative}: text: unset"
        assert b"\r\n" not in artifact.read_bytes()
    assert sha256(port.SNAPSHOT.read_bytes()).hexdigest() == port.SNAPSHOT_SHA256
