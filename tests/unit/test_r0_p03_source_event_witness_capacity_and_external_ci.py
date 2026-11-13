"""Original Git event-path and external workflow-evidence scope regression.

These tests verify genuine original Git witness identities and immutable
GitHub API observations. They do NOT prove source-subject correctness,
independent task gold, complete public CI coverage, or operative authority.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json

from experiments.r0_p03_navigation_probe.exploratory_r0_source_event_witness_capacity_v01 import (
    CLASSES, PIN, RESULT, category, git_history, rank_hash, run, select,
)

ROOT = RESULT.parent
EXTERNAL = ROOT / "exploratory_r0_source_event_external_ci_witness_result_v01.json"
STEPS = ROOT / "exploratory_r0_source_event_external_ci_step_witness_v01.json"
SOURCE_SIZE = 27509
SOURCE_HASH = "2c50e692a63f8542307fd325f987fc792a7a7cd9698f5c68885b01e120d11900"
EXTERNAL_SIZE = 30236
EXTERNAL_HASH = "a320ddea0a0905805dc2550661c54b17e9c1c08dc30288a1f584be54921aa65a"
STEPS_SIZE = 6624
STEPS_HASH = "654771d41ab68adecb4ec28f787579c9b7cd4a88aa0162d8573e9fc1dc14775d"


def check_bytes(path, size: int, digest: str) -> dict:
    raw = path.read_bytes()
    assert len(raw) == size
    assert sha256(raw).hexdigest() == digest
    assert raw.endswith(b"\n")
    assert b"\r\n" not in raw
    return json.loads(raw)


def test_path_categories_are_exclusive_and_do_not_claim_semantics() -> None:
    assert category([".github/workflows/ci.yml", "tests/test_smoke.py"]) == "WORKFLOW_CHANGE"
    assert category(["tests/test_smoke.py", "tools/main.py"]) == "TEST_CHANGE"
    assert category(["tools/project/identity.py", "docs/notes.md"]) == "IMPLEMENTATION_CHANGE"
    assert category(["docs/research/001.md", "docs/checkpoints/001.json"]) == "DOCUMENTATION_ONLY"
    assert category(["README.md"]) == "OTHER_OR_UNCLASSIFIED"
    assert category([]) == "OTHER_OR_UNCLASSIFIED"


def test_fixed_sample_exactly_reconstructed_from_all_3230_public_original_commits() -> None:
    old = git_history()
    assert len(old) == 3230
    chosen, counts = select(old)
    assert counts == {
        "DOCUMENTATION_ONLY": 2047,
        "IMPLEMENTATION_CHANGE": 615,
        "OTHER_OR_UNCLASSIFIED": 248,
        "TEST_CHANGE": 203,
        "WORKFLOW_CHANGE": 117,
    }
    data = check_bytes(RESULT, SOURCE_SIZE, SOURCE_HASH)
    assert data["historical_git_pin"] == PIN
    assert data["source_world"]["counts_by_exclusive_path_stratum"] == counts
    assert data["source_world"]["all_reachable_nonmerge_commits"] == 3230
    assert data["source_world"]["sampled_by_stratum"] == {k: 4 for k in CLASSES}
    cases = data["selected_source_event_witnesses"]
    assert len(cases) == 16
    assert [c["commit_sha"] for c in cases] == [
        sha for label in CLASSES for sha in chosen[label]
    ]
    for case in cases:
        sha = case["commit_sha"]
        assert case["changed_paths"] == old[sha]["changed_paths"]
        assert case["class_name"] == category(case["changed_paths"])
        assert case["ranked_priority_sha256"] == rank_hash(case["class_name"], sha)


def test_saved_source_result_reexecutes_from_git_original_tree_with_independent_diff() -> None:
    frozen = check_bytes(RESULT, SOURCE_SIZE, SOURCE_HASH)
    assert run() == frozen
    assert frozen["formal_r0_p03_scored"] is False
    assert frozen["source_status"]["github_actions_run_association"] == "NOT_QUERIED"
    for c in frozen["selected_source_event_witnesses"]:
        p = c["source_proof"]
        assert p["original_git_object_type"] == "commit"
        assert p["original_diff_tree_paths_verified"]
        assert p["reachable_in_exact_pin"]
        assert not p["source_file_contents_read"]
        assert not p["real_test_execution_proved_from_git_paths"]
        assert not p["owner_signed_governing_effect_proved_from_git_paths"]
        assert not p["operative_deployment_proved_from_git_paths"]


def test_external_github_run_receipt_matches_every_selected_original_commit() -> None:
    d = check_bytes(EXTERNAL, EXTERNAL_SIZE, EXTERNAL_HASH)
    src = check_bytes(RESULT, SOURCE_SIZE, SOURCE_HASH)
    sample = src["selected_source_event_witnesses"]
    cases = d["lookups"]
    assert len(cases) == len(sample) == 16
    assert [c["sha"] for c in cases] == [s["commit_sha"] for s in sample]
    assert [c["category"] for c in cases] == [s["class_name"] for s in sample]
    assert all(c["http_status"] == 200 and c["complete_single_page"] for c in cases)
    assert all(c["total_count"] == c["returned_count"] == len(c["runs"]) for c in cases)
    assert all(c["query_url"].endswith(f"head_sha={c['sha']}&per_page=100") for c in cases)
    assert all(r["head_sha"] == c["sha"] for c in cases for r in c["runs"])
    assert all(r["html_url"] == f"https://github.com/shakaarlatief/autonomous-data-science-system/actions/runs/{r['id']}"
               for c in cases for r in c["runs"])
    assert all(c["zero_runs_meaning"] == "NO_MATCHES_IN_QUERY_NOT_GLOBAL_ABSENCE" for c in cases)
    m = d["metrics"]
    assert m["sampled_commits"] == 16
    assert m["commits_with_reported_actions"] == 9
    assert m["commits_with_zero_results_in_exact_query"] == 7
    assert m["matched_workflow_runs"] == 27
    assert m["successful_run_conclusions"] == 25
    assert m["failed_run_conclusions"] == 2
    assert m["other_run_conclusions"] == 0
    assert not d["formal_r0_p03_scored"]


def test_workflow_success_and_failure_are_both_preserved_without_relabeling() -> None:
    d = check_bytes(EXTERNAL, EXTERNAL_SIZE, EXTERNAL_HASH)
    by_sha = {c["sha"]: c for c in d["lookups"]}
    mixed = by_sha["842676c04ce6d0305365de60bddec876a530e185"]
    assert len(mixed["runs"]) == 4
    assert Counter(x["conclusion"] for x in mixed["runs"]) == {"success": 3, "failure": 1}
    run_by_id = {x["id"]: x for c in d["lookups"] for x in c["runs"]}
    assert run_by_id[32356647189]["conclusion"] == "failure"
    assert run_by_id[32359491623]["conclusion"] == "failure"
    assert run_by_id[32356647199]["conclusion"] == "success"
    assert run_by_id[32356647189]["head_sha"] == mixed["sha"]
    assert d["metrics"]["job_detail_runs"] == 3
    assert d["metrics"]["job_detail_total_jobs"] == 15
    assert d["metrics"]["job_detail_success"] == 13
    assert d["metrics"]["job_detail_failure"] == 2
    for record in d["job_details"]:
        assert record["total_count"] == record["returned_count"] == len(record["jobs"])
        assert all(x["runId"] == record["run_id"] for x in record["jobs"])


def test_purposively_selected_job_step_witnesses_show_partial_success_not_global_pass() -> None:
    d = check_bytes(STEPS, STEPS_SIZE, STEPS_HASH)
    assert d["job_ids"] == [96387316689, 96395817325, 96387336750]
    by_job = {r["job_id"]: r for r in d["step_evidence"]}
    assert len(by_job) == 3
    assert all(len(x["steps"]) == x["step_count"] for x in by_job.values())
    failed_persistence = by_job[96387316689]
    assert any(x["name"] == "Persist successful interchange evidence"
               and x["conclusion"] == "failure" for x in failed_persistence["steps"])
    failed_diagnostic = by_job[96395817325]
    assert any(x["name"] == "Run and persist PostgreSQL diagnostic"
               and x["conclusion"] == "failure" for x in failed_diagnostic["steps"])
    passed_persistence = by_job[96387336750]
    assert any(x["name"] == "Persist successful evidence and lockfile"
               and x["conclusion"] == "success" for x in passed_persistence["steps"])
    assert d["selection"].startswith("AFTER_OBSERVING_")
    assert d["formal_r0_p03_scored"] is False


def test_external_provider_records_do_not_override_git_only_proof_boundary() -> None:
    source = check_bytes(RESULT, SOURCE_SIZE, SOURCE_HASH)
    receipt = check_bytes(EXTERNAL, EXTERNAL_SIZE, EXTERNAL_HASH)
    assert all(not c["source_proof"]["operative_deployment_proved_from_git_paths"]
               for c in source["selected_source_event_witnesses"])
    assert all(not c["source_proof"]["owner_signed_governing_effect_proved_from_git_paths"]
               for c in source["selected_source_event_witnesses"])
    assert any(x["total_count"] == 0 for x in receipt["lookups"])
    assert any(x["total_count"] > 0 for x in receipt["lookups"])
    assert any("not independently" in x.lower() or "not independent" in x.lower()
               for x in receipt["limitations"])
