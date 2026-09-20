"""G014 deterministic CLI qualification over the accepted G009-G013 substrate."""

import json
import os
from pathlib import Path
import subprocess
import sys

import pytest

from tests.unit.test_project_knowledge_current_state_core import ACTIVE, ROOT, core_repo
from tests.unit.test_project_knowledge_views import commit, deterministic_json, git, write


PERSISTENT_VIEW_IDS = (
    "authority_index",
    "current_state_core",
    "current_state_core_markdown",
    "identity_index",
    "risk_obligation_index",
    "source_catalog",
    "subject_index",
    "workstream_graph",
)

PERSISTENT_VIEW_PATHS = {
    "docs/project_knowledge/generated/source_catalog.json",
    "docs/project_knowledge/generated/identity_index.json",
    "docs/project_knowledge/generated/authority_index.json",
    "docs/project_knowledge/generated/workstream_graph.json",
    "docs/project_knowledge/generated/subject_index.json",
    "docs/project_knowledge/generated/risk_obligation_index.json",
    "docs/project_knowledge/generated/current_state_core.json",
    "docs/project_knowledge/generated/CURRENT_STATE_CORE.md",
}


CLI_FILES = (
    "tools/project_knowledge/__main__.py",
    "tools/project_knowledge/cli.py",
    "tools/project_knowledge/identity.py",
    "tools/project_knowledge/view_definitions/__init__.py",
    "tools/project_knowledge/workstreams.py",
    "tools/project_knowledge/adapters/generated_io.py",
    "tools/project_knowledge/services/cli_ops.py",
    "tools/project_knowledge/services/refresh.py",
    "tools/project_knowledge/services/semantic_validation.py",
)


@pytest.fixture
def cli_repo(core_repo):
    for path in CLI_FILES:
        write(core_repo, path, (ROOT / path).read_bytes())
    commit(core_repo)
    return core_repo


def run_cli(root, *args):
    return subprocess.run(
        [sys.executable, "-B", "-m", "tools.project_knowledge", *args, "--root", str(root)],
        cwd=root, capture_output=True, text=True,
    )


def payload(process):
    assert process.stdout.strip(), process.stderr
    return json.loads(process.stdout)


def generated_paths(result):
    return {
        path
        for view in result["views"]
        for path in (view["view_path"], view["manifest_path"])
    }


def test_rebuild_is_deterministic_staged_read_only_and_machine_stable(cli_repo):
    before = git(cli_repo, "status", "--porcelain")
    parent_stages_before = {
        path.name for path in cli_repo.parent.glob(".project-knowledge-stage-*")
    }
    first = run_cli(cli_repo, "rebuild")
    second = run_cli(cli_repo, "rebuild", "--ref", "HEAD")
    assert first.returncode == second.returncode == 0, first.stderr + first.stdout
    assert first.stdout == second.stdout
    result = payload(first)
    assert result["ok"] and result["staging_mode"] == "TEMPORARY_DIFF"
    assert result["materialized"] is False
    assert tuple(view["view_id"] for view in result["views"]) == PERSISTENT_VIEW_IDS
    assert {view["view_path"] for view in result["views"]} == PERSISTENT_VIEW_PATHS
    assert {view["view_status_before"] for view in result["views"]} == {"MISSING"}
    assert {view["manifest_status_before"] for view in result["views"]} == {"MISSING"}
    assert all(len(view["view_digest"]) == len(view["manifest_digest"]) == 64 for view in result["views"])
    assert git(cli_repo, "status", "--porcelain") == before
    assert not any(path.name.startswith(".project-knowledge-stage-") for path in cli_repo.iterdir())
    assert {
        path.name for path in cli_repo.parent.glob(".project-knowledge-stage-*")
    } == parent_stages_before
    assert str(cli_repo.resolve()) not in first.stdout


def test_explicit_write_materializes_only_generated_outputs_and_freshness_passes(cli_repo):
    rebuilt = run_cli(cli_repo, "rebuild", "--ref", "HEAD", "--write")
    assert rebuilt.returncode == 0, rebuilt.stderr + rebuilt.stdout
    result = payload(rebuilt)
    assert result["materialized"] is True
    paths = generated_paths(result)
    assert paths and all(path.startswith("docs/project_knowledge/generated/") for path in paths)
    assert all((cli_repo / path).is_file() for path in paths)

    fresh = run_cli(cli_repo, "check-freshness")
    repeated = run_cli(cli_repo, "check-freshness", "--ref", "HEAD")
    assert fresh.returncode == repeated.returncode == 0
    assert fresh.stdout == repeated.stdout
    checked = payload(fresh)
    assert checked["ok"]
    assert {view["status"] for view in checked["views"]} == {"FRESH"}

    diff = run_cli(cli_repo, "rebuild", "--ref", "HEAD")
    assert diff.returncode == 0
    assert {view["view_status_before"] for view in payload(diff)["views"]} == {"MATCH"}
    assert {view["manifest_status_before"] for view in payload(diff)["views"]} == {"MATCH"}


def test_persistent_stale_manifests_are_visible_but_do_not_block_rebuild_repair(cli_repo):
    initial = run_cli(cli_repo, "rebuild", "--ref", "HEAD", "--write")
    assert initial.returncode == 0, initial.stderr + initial.stdout
    commit(cli_repo)

    active = json.loads((cli_repo / ACTIVE).read_bytes())
    active["objective"] = "Updated canonical objective after persistent view publication"
    write(cli_repo, ACTIVE, deterministic_json(active))
    commit(cli_repo)

    full_validation = run_cli(
        cli_repo,
        "validate",
        "--snapshot-mode",
        "COMMIT_SNAPSHOT",
        "--ref",
        "HEAD",
        "--durable-evidence",
    )
    assert full_validation.returncode == 1
    assert "SOURCE_DIGEST_MISMATCH" in {
        item["code"] for item in payload(full_validation)["diagnostics"]
    }

    stale = run_cli(cli_repo, "check-freshness", "--ref", "HEAD")
    assert stale.returncode == 1
    stale_payload = payload(stale)
    assert not stale_payload["ok"]
    assert {view["status"] for view in stale_payload["views"]} == {"STALE"}

    staged = run_cli(cli_repo, "rebuild", "--ref", "HEAD")
    assert staged.returncode == 0, staged.stderr + staged.stdout
    staged_payload = payload(staged)
    assert staged_payload["ok"] and staged_payload["materialized"] is False
    assert "DIFF" in {view["manifest_status_before"] for view in staged_payload["views"]}

    repaired = run_cli(cli_repo, "rebuild", "--ref", "HEAD", "--write")
    assert repaired.returncode == 0, repaired.stderr + repaired.stdout
    repaired_payload = payload(repaired)
    assert repaired_payload["ok"] and repaired_payload["materialized"] is True

    fresh = run_cli(cli_repo, "check-freshness", "--ref", "HEAD")
    assert fresh.returncode == 0, fresh.stderr + fresh.stdout
    assert {view["status"] for view in payload(fresh)["views"]} == {"FRESH"}


def test_explicit_write_accepts_git_clean_line_ending_materialization(cli_repo):
    git(cli_repo, "config", "core.autocrlf", "true")

    target = cli_repo / ACTIVE
    target.unlink()
    git(cli_repo, "checkout", "--", ACTIVE)

    materialized = target.read_bytes()
    assert b"\r\n" in materialized
    assert git(cli_repo, "status", "--porcelain") == b""

    rebuilt = run_cli(cli_repo, "rebuild", "--ref", "HEAD", "--write")
    assert rebuilt.returncode == 0, rebuilt.stderr + rebuilt.stdout
    result = payload(rebuilt)
    assert result["ok"] and result["materialized"] is True
    assert {view["view_status_before"] for view in result["views"]} == {"MISSING"}


def test_check_freshness_missing_stale_and_invalid_are_nonzero(cli_repo):
    missing = run_cli(cli_repo, "check-freshness", "--ref", "HEAD")
    assert missing.returncode == 1
    missing_payload = payload(missing)
    assert not missing_payload["ok"]
    assert {view["status"] for view in missing_payload["views"]} == {"MISSING"}

    assert run_cli(cli_repo, "rebuild", "--ref", "HEAD", "--write").returncode == 0
    core = next(view for view in payload(run_cli(cli_repo, "rebuild", "--ref", "HEAD"))["views"]
                if view["view_id"] == "current_state_core")
    write(cli_repo, core["view_path"], (cli_repo / core["view_path"]).read_bytes() + b" ")
    stale = run_cli(cli_repo, "check-freshness", "--ref", "HEAD")
    assert stale.returncode == 1
    stale_result = payload(stale)
    core_state = next(view for view in stale_result["views"] if view["view_id"] == "current_state_core")
    assert core_state["status"] == "STALE"
    assert {item["code"] for item in core_state["diagnostics"]} == {"STALE_VIEW_CONTENT"}

    write(cli_repo, core["manifest_path"], b'{"profile":"derived_view_manifest.v1"')
    invalid = run_cli(cli_repo, "check-freshness", "--ref", "HEAD")
    assert invalid.returncode == 1
    invalid_result = payload(invalid)
    core_state = next(view for view in invalid_result["views"] if view["view_id"] == "current_state_core")
    assert core_state["status"] == "INVALID"
    assert core_state["diagnostics"]


def test_commit_validate_binds_schema_to_selected_commit_not_worktree(cli_repo):
    baseline = run_cli(
        cli_repo, "validate", "--snapshot-mode", "COMMIT_SNAPSHOT", "--ref", "HEAD"
    )
    assert baseline.returncode == 0

    schema = cli_repo / "schemas/project_knowledge/semantic_source.v1.schema.json"
    original = schema.read_bytes()
    write(cli_repo, "schemas/project_knowledge/semantic_source.v1.schema.json", b"{not-json")

    committed = run_cli(
        cli_repo, "validate", "--snapshot-mode", "COMMIT_SNAPSHOT", "--ref", "HEAD"
    )
    assert committed.returncode == 0, committed.stderr + committed.stdout
    assert committed.stdout == baseline.stdout
    assert payload(committed)["ok"]

    local = run_cli(cli_repo, "validate", "--snapshot-mode", "WORKTREE_SNAPSHOT")
    assert local.returncode == 1
    assert payload(local)["error"]["code"] == "INVALID_OPERATION"
    assert schema.read_bytes() != original


def test_commit_validate_rejects_partial_committed_schema_closure(cli_repo):
    missing = "schemas/project_knowledge/semantic_source.v1.schema.json"
    git(cli_repo, "rm", missing)
    commit(cli_repo)

    validated = run_cli(
        cli_repo, "validate", "--snapshot-mode", "COMMIT_SNAPSHOT", "--ref", "HEAD"
    )
    assert validated.returncode == 1
    result = payload(validated)
    assert result["error"]["code"] == "MISSING_SCHEMA_DEPENDENCY"


def test_validate_durable_evidence_rejects_worktree_snapshot(cli_repo):
    process = run_cli(
        cli_repo, "validate", "--snapshot-mode", "WORKTREE_SNAPSHOT", "--durable-evidence"
    )
    assert process.returncode == 1
    result = payload(process)
    assert "NON_COMMITTED_EVIDENCE" in {
        item["code"] for item in result["diagnostics"]
    }


def test_validate_rejects_duplicate_current_semantic_identity(cli_repo):
    active = json.loads((cli_repo / ACTIVE).read_bytes())
    write(cli_repo, "docs/duplicate-current-id.json", deterministic_json({
        "schema_version": "1",
        "profile": "semantic_source.v1",
        "kind": "DUPLICATE_OWNER",
        "authority_class": "canonical",
        "semantic_id": active["semantic_id"],
    }))
    commit(cli_repo)

    validated = run_cli(
        cli_repo, "validate", "--snapshot-mode", "COMMIT_SNAPSHOT", "--ref", "HEAD"
    )
    assert validated.returncode == 1
    result = payload(validated)
    assert "DUPLICATE_CURRENT_IDENTITY" in {
        item["code"] for item in result["diagnostics"]
    }


def test_validate_rejects_duplicate_procedure_constraint_identity(cli_repo):
    path = "docs/procedure.json"
    value = json.loads((cli_repo / path).read_bytes())
    value["mandatory_constraints"].append({
        "constraint_id": value["mandatory_constraints"][0]["constraint_id"],
        "requirement": "A distinct requirement cannot reuse the same constraint identity",
    })
    write(cli_repo, path, deterministic_json(value))
    commit(cli_repo)

    validated = run_cli(
        cli_repo, "validate", "--snapshot-mode", "COMMIT_SNAPSHOT", "--ref", "HEAD"
    )
    assert validated.returncode == 1
    result = payload(validated)
    assert "DUPLICATE_CONSTRAINT_ID" in {
        item["code"] for item in result["diagnostics"]
    }


def _joint_value(semantic_id, domain, action="ACT"):
    return {
        "schema_version": "1",
        "profile": "joint_authority.v1",
        "kind": "JOINT_AUTHORITY",
        "authority_class": "canonical",
        "semantic_id": semantic_id,
        "state": "ACTIVE",
        "scope": {"domain": domain},
        "members": ["MEMBER:A", "MEMBER:B"],
        "combination_semantics": "Both members govern together",
        "governed_action_classes": [action],
        "admission": {
            "overlapping_current_canonical_sources": True,
            "ordinary_relations_insufficient": True,
            "irreducible_set_fact": True,
            "independently_activated": True,
            "review_evidence": ["review:joint"],
            "duplicate_ownership_rejected": True,
        },
        "provenance": ["docs/joint-review.md"],
    }


def _write_joint_members(root):
    for semantic_id in ("MEMBER:A", "MEMBER:B"):
        write(root, f"docs/{semantic_id.replace(':', '-').lower()}.json", deterministic_json({
            "schema_version": "1",
            "profile": "semantic_source.v1",
            "kind": "JOINT_MEMBER",
            "authority_class": "canonical",
            "semantic_id": semantic_id,
        }))


def test_validate_allows_same_joint_members_when_scopes_are_disjoint(cli_repo):
    _write_joint_members(cli_repo)
    write(cli_repo, "docs/joint-a.json", deterministic_json(_joint_value("JOINT:A", "alpha")))
    write(cli_repo, "docs/joint-b.json", deterministic_json(_joint_value("JOINT:B", "beta")))
    commit(cli_repo)

    validated = run_cli(
        cli_repo, "validate", "--snapshot-mode", "COMMIT_SNAPSHOT", "--ref", "HEAD"
    )
    assert validated.returncode == 0, validated.stdout
    assert "DUPLICATE_JOINT_AUTHORITY_SET" not in {
        item["code"] for item in payload(validated)["diagnostics"]
    }


def test_validate_rejects_joint_member_set_when_scope_action_and_time_overlap(cli_repo):
    _write_joint_members(cli_repo)
    write(cli_repo, "docs/joint-a.json", deterministic_json(_joint_value("JOINT:A", "alpha")))
    write(cli_repo, "docs/joint-b.json", deterministic_json(_joint_value("JOINT:B", "alpha")))
    commit(cli_repo)

    validated = run_cli(
        cli_repo, "validate", "--snapshot-mode", "COMMIT_SNAPSHOT", "--ref", "HEAD"
    )
    assert validated.returncode == 1
    assert "DUPLICATE_JOINT_AUTHORITY_SET" in {
        item["code"] for item in payload(validated)["diagnostics"]
    }


def test_validate_and_rebuild_fail_nonzero_on_query_independent_semantic_defect(cli_repo):
    write(cli_repo, "docs/dangling-relation.json", deterministic_json({
        "schema_version": "1",
        "profile": "semantic_source.v1",
        "kind": "NOTE",
        "authority_class": "canonical",
        "semantic_id": "RELATION:OWNER",
        "relations": [{"mode": "SUPPLEMENT", "target": "RELATION:MISSING"}],
    }))
    commit(cli_repo)

    validated = run_cli(
        cli_repo, "validate", "--snapshot-mode", "COMMIT_SNAPSHOT", "--ref", "HEAD"
    )
    assert validated.returncode == 1
    result = payload(validated)
    assert not result["ok"]
    assert "DANGLING_RELATION_TARGET" in {item["code"] for item in result["diagnostics"]}

    rebuilt = run_cli(cli_repo, "rebuild", "--ref", "HEAD")
    assert rebuilt.returncode == 1
    result = payload(rebuilt)
    assert "DANGLING_RELATION_TARGET" in {item["code"] for item in result["diagnostics"]}
    assert not (cli_repo / "docs/project_knowledge/generated").exists()


def test_validate_reuses_g008_workstream_closure_without_inventing_route(cli_repo):
    value = json.loads((cli_repo / ACTIVE).read_bytes())
    value["depends_on"] = ["WORKSTREAM:MISSING"]
    write(cli_repo, ACTIVE, deterministic_json(value))
    commit(cli_repo)

    validated = run_cli(
        cli_repo, "validate", "--snapshot-mode", "COMMIT_SNAPSHOT", "--ref", "HEAD"
    )
    assert validated.returncode == 1
    result = payload(validated)
    assert "DANGLING_WORKSTREAM_DEPENDENCY" in {
        item["code"] for item in result["diagnostics"]
    }


def test_validate_temporal_workstream_still_rejects_missing_dependency(cli_repo):
    value = json.loads((cli_repo / ACTIVE).read_bytes())
    value["effective_from"] = "2026-01-01T00:00:00Z"
    value["depends_on"] = ["WORKSTREAM:MISSING"]
    write(cli_repo, ACTIVE, deterministic_json(value))
    commit(cli_repo)

    validated = run_cli(
        cli_repo, "validate", "--snapshot-mode", "COMMIT_SNAPSHOT", "--ref", "HEAD"
    )
    assert validated.returncode == 1
    result = payload(validated)
    codes = {item["code"]: item["severity"] for item in result["diagnostics"]}
    assert codes["DANGLING_WORKSTREAM_DEPENDENCY"] == "ERROR"
    assert codes["TEMPORAL_WORKSTREAM_GRAPH_DEFERRED"] == "INFO"


def test_validate_temporal_workstream_still_rejects_completed_resume_target(cli_repo):
    value = json.loads((cli_repo / ACTIVE).read_bytes())
    value.update({
        "state": "PAUSED",
        "expected_to_resume": True,
        "pause_reason": "Waiting for prerequisite",
        "return_condition": "Prerequisite becomes available",
        "resume_target": "WORKSTREAM:COMPLETED",
        "effective_from": "2026-01-01T00:00:00Z",
    })
    write(cli_repo, ACTIVE, deterministic_json(value))
    write(cli_repo, "docs/work/completed-target.json", deterministic_json({
        "schema_version": "1",
        "profile": "workstream.v1",
        "kind": "COMPLETED_WORKSTREAM",
        "authority_class": "canonical",
        "semantic_id": "WORKSTREAM:COMPLETED",
        "state": "COMPLETED",
        "objective": "Already completed work",
    }))
    commit(cli_repo)

    validated = run_cli(
        cli_repo, "validate", "--snapshot-mode", "COMMIT_SNAPSHOT", "--ref", "HEAD"
    )
    assert validated.returncode == 1
    result = payload(validated)
    codes = {item["code"]: item["severity"] for item in result["diagnostics"]}
    assert codes["INVALID_WORKSTREAM_RESUME_TARGET"] == "ERROR"
    assert codes["TEMPORAL_WORKSTREAM_GRAPH_DEFERRED"] == "INFO"


def test_validate_temporal_workstream_rejects_superseded_context(cli_repo):
    value = json.loads((cli_repo / ACTIVE).read_bytes())
    value["effective_from"] = "2026-01-01T00:00:00Z"
    value["parent"] = "CONTEXT:SUPERSEDED"
    write(cli_repo, ACTIVE, deterministic_json(value))
    write(cli_repo, "docs/work/superseded-context.json", deterministic_json({
        "schema_version": "1",
        "profile": "semantic_source.v1",
        "kind": "WORKSTREAM_CONTEXT",
        "authority_class": "canonical",
        "semantic_id": "CONTEXT:SUPERSEDED",
        "state": "SUPERSEDED",
    }))
    commit(cli_repo)

    validated = run_cli(
        cli_repo, "validate", "--snapshot-mode", "COMMIT_SNAPSHOT", "--ref", "HEAD"
    )
    assert validated.returncode == 1
    result = payload(validated)
    codes = {item["code"]: item["severity"] for item in result["diagnostics"]}
    assert codes["INVALID_WORKSTREAM_CONTEXT"] == "ERROR"
    assert codes["TEMPORAL_WORKSTREAM_GRAPH_DEFERRED"] == "INFO"


def test_validate_checks_all_temporal_identity_states_without_guessing_now(cli_repo):
    for path, start, end in (
        ("docs/temporal-a.json", "2026-01-01T00:00:00Z", "2026-02-01T00:00:00Z"),
        ("docs/temporal-b.json", "2026-02-01T00:00:00Z", "2026-03-01T00:00:00Z"),
    ):
        write(cli_repo, path, deterministic_json({
            "schema_version": "1",
            "profile": "semantic_source.v1",
            "kind": "TEMPORAL_NOTE",
            "authority_class": "canonical",
            "semantic_id": "TEMPORAL:OWNER",
            "effective_from": start,
            "effective_to": end,
        }))
    commit(cli_repo)

    validated = run_cli(
        cli_repo, "validate", "--snapshot-mode", "COMMIT_SNAPSHOT", "--ref", "HEAD"
    )
    assert validated.returncode == 0, validated.stdout
    result = payload(validated)
    codes = {item["code"]: item["severity"] for item in result["diagnostics"]}
    assert result["deferred_checks"] == []
    assert "DUPLICATE_CURRENT_IDENTITY" not in codes
    assert "TEMPORAL_IDENTITY_CLOSURE_DEFERRED" not in codes


def test_validate_temporal_identity_transition_still_checks_static_structure(cli_repo):
    for semantic_id in ("OLD:1", "OLD:2", "NEW:1"):
        write(cli_repo, f"docs/{semantic_id.replace(':', '-').lower()}.json", deterministic_json({
            "schema_version": "1",
            "profile": "semantic_source.v1",
            "kind": "IDENTITY_ENDPOINT",
            "authority_class": "canonical",
            "semantic_id": semantic_id,
        }))
    write(cli_repo, "docs/invalid-temporal-transition.json", deterministic_json({
        "schema_version": "1",
        "profile": "identity_transition.v1",
        "kind": "identity_transition",
        "authority_class": "canonical",
        "transition_class": "SUPERSEDE",
        "predecessors": ["OLD:1", "OLD:2"],
        "successors": ["NEW:1"],
        "provenance": ["docs/decision.md"],
        "resolution_behavior": "Supersede the prior identity",
        "effective_from": "2026-01-01T00:00:00Z",
        "effective_to": "2026-12-31T00:00:00Z",
    }))
    commit(cli_repo)

    validated = run_cli(
        cli_repo, "validate", "--snapshot-mode", "COMMIT_SNAPSHOT", "--ref", "HEAD"
    )
    assert validated.returncode == 1
    assert "INVALID_TRANSITION_MULTIPLICITY" in {
        item["code"] for item in payload(validated)["diagnostics"]
    }


def test_validate_rejects_overlapping_temporal_identity_claims(cli_repo):
    for path in ("docs/temporal-overlap-a.json", "docs/temporal-overlap-b.json"):
        write(cli_repo, path, deterministic_json({
            "schema_version": "1",
            "profile": "semantic_source.v1",
            "kind": "TEMPORAL_NOTE",
            "authority_class": "canonical",
            "semantic_id": "TEMPORAL:OVERLAP",
            "effective_from": "2026-01-01T00:00:00Z",
            "effective_to": "2026-03-01T00:00:00Z",
        }))
    commit(cli_repo)

    validated = run_cli(
        cli_repo, "validate", "--snapshot-mode", "COMMIT_SNAPSHOT", "--ref", "HEAD"
    )
    assert validated.returncode == 1
    assert "DUPLICATE_CURRENT_IDENTITY" in {
        item["code"] for item in payload(validated)["diagnostics"]
    }


def test_validate_rejects_inverted_temporal_interval(cli_repo):
    write(cli_repo, "docs/invalid-time.json", deterministic_json({
        "schema_version": "1",
        "profile": "semantic_source.v1",
        "kind": "TEMPORAL_NOTE",
        "authority_class": "canonical",
        "semantic_id": "TEMPORAL:INVALID",
        "effective_from": "2026-03-01T00:00:00Z",
        "effective_to": "2026-01-01T00:00:00Z",
    }))
    commit(cli_repo)

    validated = run_cli(
        cli_repo, "validate", "--snapshot-mode", "COMMIT_SNAPSHOT", "--ref", "HEAD"
    )
    assert validated.returncode == 1
    assert "INVALID_IDENTITY_TIME" in {
        item["code"] for item in payload(validated)["diagnostics"]
    }


def test_rebuild_hard_repository_defect_is_deterministic_nonzero(cli_repo):
    write(cli_repo, "docs/broken.json", b'{"profile":"semantic_source.v1"')
    commit(cli_repo)
    first = run_cli(cli_repo, "rebuild", "--ref", "HEAD")
    second = run_cli(cli_repo, "rebuild", "--ref", "HEAD")
    assert first.returncode == second.returncode == 1
    assert first.stdout == second.stdout
    result = payload(first)
    assert not result["ok"]
    codes = {item["code"] for item in result.get("diagnostics", ())}
    assert "MALFORMED_JSON" in codes or result["error"]["code"] == "INVALID_VIEW_INPUT"
    assert not (cli_repo / "docs/project_knowledge/generated").exists()


def test_materialization_refuses_uncommitted_canonical_source_drift(cli_repo):
    value = json.loads((cli_repo / ACTIVE).read_bytes())
    value["execution_anchor"]["checkpoint"] = 991
    write(cli_repo, ACTIVE, deterministic_json(value))

    staged = run_cli(cli_repo, "rebuild", "--ref", "HEAD")
    assert staged.returncode == 0
    assert payload(staged)["materialized"] is False

    refused = run_cli(cli_repo, "rebuild", "--ref", "HEAD", "--write")
    assert refused.returncode == 1
    result = payload(refused)
    assert result["error"]["code"] == "MATERIALIZATION_SOURCE_DRIFT"
    assert not (cli_repo / "docs/project_knowledge/generated").exists()


def test_materialization_refuses_uncommitted_historical_input_drift(cli_repo):
    path = "docs/history/accepted.json"
    write(cli_repo, path, deterministic_json({
        "schema_version": "1",
        "profile": "semantic_source.v1",
        "kind": "HISTORICAL_NOTE",
        "authority_class": "historical",
        "semantic_id": "HISTORY:ONE",
        "state": "SUPERSEDED",
    }))
    commit(cli_repo)

    value = json.loads((cli_repo / path).read_bytes())
    value["kind"] = "HISTORICAL_NOTE_CHANGED_LOCALLY"
    write(cli_repo, path, deterministic_json(value))

    refused = run_cli(cli_repo, "rebuild", "--ref", "HEAD", "--write")
    assert refused.returncode == 1
    result = payload(refused)
    assert result["error"]["code"] == "MATERIALIZATION_SOURCE_DRIFT"
    assert not (cli_repo / "docs/project_knowledge/generated").exists()


def test_refresh_cli_uses_g013_plan_and_same_staged_builds(cli_repo):
    previous = git(cli_repo, "rev-parse", "HEAD").decode().strip()
    value = json.loads((cli_repo / ACTIVE).read_bytes())
    value["execution_anchor"]["checkpoint"] = 777
    write(cli_repo, ACTIVE, deterministic_json(value))
    commit(cli_repo)

    first = run_cli(cli_repo, "refresh", "--changed-since", previous)
    second = run_cli(cli_repo, "refresh", "--changed-since", previous, "--ref", "HEAD")
    assert first.returncode == second.returncode == 0
    assert first.stdout == second.stdout
    result = payload(first)
    assert result["ok"] and not result["full_fallback"]
    assert tuple(result["affected_view_ids"]) == PERSISTENT_VIEW_IDS
    assert {view["view_id"] for view in result["views"]} == set(result["affected_view_ids"])
    assert not (cli_repo / "docs/project_knowledge/generated").exists()


def test_generated_materialization_replaces_hardlink_without_mutating_canonical(cli_repo):
    from tools.project_knowledge.adapters.generated_io import write_generated_bytes

    canonical = cli_repo / "docs/canonical-hardlink-target.txt"
    canonical.write_bytes(b"canonical\n")
    generated = cli_repo / "docs/project_knowledge/generated/hardlinked.json"
    generated.parent.mkdir(parents=True, exist_ok=True)
    try:
        os.link(canonical, generated)
    except OSError as error:
        pytest.skip(f"Hard links unavailable on this filesystem: {error}")

    write_generated_bytes(
        cli_repo,
        "docs/project_knowledge/generated/hardlinked.json",
        b'{"authority_class":"derived"}\n',
    )

    assert canonical.read_bytes() == b"canonical\n"
    assert generated.read_bytes() == b'{"authority_class":"derived"}\n'


def test_generated_materialization_adapter_cannot_write_canonical_paths(cli_repo):
    code = (
        "from pathlib import Path;"
        "from tools.project_knowledge.adapters.generated_io import write_generated_bytes;"
        "write_generated_bytes(Path.cwd(),'docs/CURRENT_STATE.md',b'x')"
    )
    process = subprocess.run([sys.executable, "-B", "-c", code], cwd=cli_repo, capture_output=True, text=True)
    assert process.returncode != 0
    assert not (cli_repo / "docs/CURRENT_STATE.md").exists()


def test_cli_argument_contract_keeps_parse_failures_distinct(cli_repo):
    missing_mode = subprocess.run(
        [sys.executable, "-B", "-m", "tools.project_knowledge", "validate", "--root", str(cli_repo)],
        cwd=cli_repo, capture_output=True, text=True,
    )
    assert missing_mode.returncode == 2
    missing_changed_since = run_cli(cli_repo, "refresh")
    assert missing_changed_since.returncode == 2
