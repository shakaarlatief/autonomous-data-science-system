from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

EXPECTED_ACTION_COUNT = 89
EXPECTED_GROUP_COUNTS = {
    "issues": 17,
    "pull-requests-reviews": 32,
    "repository-git": 29,
    "content-download": 1,
    "actions-ci": 9,
    "permissions": 1,
}
INVENTORY = Path("docs/research/github_connector_89_action_inventory.json")


def fail(message: str) -> None:
    print(f"ERROR {message}")
    raise SystemExit(1)


def main() -> int:
    data = json.loads(INVENTORY.read_text(encoding="utf-8"))
    if data.get("schemaVersion") != 2:
        fail("schemaVersion must equal 2")
    if data.get("actionCount") != EXPECTED_ACTION_COUNT:
        fail(f"actionCount must equal {EXPECTED_ACTION_COUNT}")
    if data.get("negativeChallengeNewActions") != 0:
        fail("negativeChallengeNewActions must equal 0 for the frozen 2026-09-08 baseline")

    actions = data.get("actions")
    if not isinstance(actions, list) or len(actions) != EXPECTED_ACTION_COUNT:
        fail(f"actions must contain exactly {EXPECTED_ACTION_COUNT} entries")

    ordinals = [item.get("ordinal") for item in actions]
    if ordinals != list(range(1, EXPECTED_ACTION_COUNT + 1)):
        fail("ordinals must be contiguous 1..89 in preserved qualification order")

    expected_projected_order = [line.strip() for line in """
GitHub.add_comment_to_issue
GitHub.add_issue_assignees
GitHub.add_issue_labels
GitHub.add_reaction_to_issue_comment
GitHub.add_reaction_to_pr
GitHub.add_reaction_to_pr_review_comment
GitHub.add_review_to_pr
GitHub.compare_commits
GitHub.convert_pull_request_to_draft
GitHub.create_blob
GitHub.create_branch
GitHub.create_commit
GitHub.create_file
GitHub.create_issue
GitHub.create_pull_request
GitHub.create_tree
GitHub.delete_file
GitHub.dismiss_pull_request_review
GitHub.download_user_content
GitHub.download_workflow_artifact
GitHub.enable_auto_merge
GitHub.fetch
GitHub.fetch_blob
GitHub.fetch_commit
GitHub.fetch_commit_workflow_runs
GitHub.fetch_file
GitHub.fetch_issue
GitHub.fetch_issue_comments
GitHub.fetch_pr
GitHub.fetch_pr_comments
GitHub.fetch_pr_file_patch
GitHub.fetch_pr_patch
GitHub.fetch_workflow_job_logs
GitHub.fetch_workflow_job_steps
GitHub.fetch_workflow_run_artifacts
GitHub.fetch_workflow_run_jobs
GitHub.get_commit_combined_status
GitHub.get_issue_comment_reactions
GitHub.get_pr_diff
GitHub.get_pr_info
GitHub.get_pr_reactions
GitHub.get_pr_review_comment_reactions
GitHub.get_profile
GitHub.get_repo
GitHub.get_repo_collaborator_permission
GitHub.get_user_login
GitHub.get_users_recent_prs_in_repo
GitHub.label_pr
GitHub.list_installations
GitHub.list_installed_accounts
GitHub.list_pr_changed_filenames
GitHub.list_pull_request_review_threads
GitHub.list_pull_request_reviews
GitHub.list_recent_issues
GitHub.list_repositories
GitHub.list_repositories_by_affiliation
GitHub.list_repositories_by_installation
GitHub.list_user_org_memberships
GitHub.list_user_orgs
GitHub.lock_issue_conversation
GitHub.mark_pull_request_ready_for_review
GitHub.merge_pull_request
GitHub.remove_issue_assignees
GitHub.remove_issue_label
GitHub.remove_pull_request_reviewers
GitHub.remove_reaction_from_issue_comment
GitHub.remove_reaction_from_pr
GitHub.remove_reaction_from_pr_review_comment
GitHub.reply_to_review_comment
GitHub.request_pull_request_reviewers
GitHub.rerun_failed_workflow_run_jobs
GitHub.rerun_workflow_job
GitHub.resolve_review_thread
GitHub.search
GitHub.search_branches
GitHub.search_commits
GitHub.search_installed_repositories_streaming
GitHub.search_installed_repositories_v2
GitHub.search_issues
GitHub.search_prs
GitHub.search_repositories
GitHub.unlock_issue_conversation
GitHub.unresolve_review_thread
GitHub.update_file
GitHub.update_issue
GitHub.update_issue_comment
GitHub.update_pull_request
GitHub.update_ref
GitHub.update_review_comment
""".splitlines() if line.strip()]

    native = [item.get("nativeAction") for item in actions]
    target = [item.get("targetAction") for item in actions]
    if native != expected_projected_order:
        fail("nativeAction order/content must equal the fresh 89-action projected inventory")
    if "GitHub.download_user_content" not in native or "GitHub.add_issue_comment" in native:
        fail("fresh projection correction is not preserved")
    if len(set(native)) != EXPECTED_ACTION_COUNT:
        fail("nativeAction values must be unique")
    if len(set(target)) != EXPECTED_ACTION_COUNT:
        fail("targetAction values must be unique")
    if any(not isinstance(value, str) or not value.startswith("GitHub.") for value in native):
        fail("every nativeAction must begin with GitHub.")
    if any(not isinstance(value, str) or not value.startswith("github.") for value in target):
        fail("every targetAction must begin with github.")
    for native_name, target_name in zip(native, target):
        if native_name.split(".", 1)[1] != target_name.split(".", 1)[1]:
            fail(f"target action suffix drift: {native_name} -> {target_name}")

    counts = Counter(item.get("domain") for item in actions)
    if dict(counts) != EXPECTED_GROUP_COUNTS:
        fail(f"domain counts drifted: {dict(counts)}")

    required_fields = {
        "ordinal", "nativeAction", "targetAction", "domain", "mutability",
        "currentRuntimeBridgeParity", "reuseBasis", "targetTransport",
    }
    for item in actions:
        if set(item) != required_fields:
            fail(f"entry {item.get('ordinal')} has wrong field set")
        if item["mutability"] not in {"read", "write"}:
            fail(f"entry {item['ordinal']} has invalid mutability")
        for field in required_fields - {"ordinal"}:
            if not isinstance(item[field], str) or not item[field]:
                fail(f"entry {item['ordinal']} has an empty string field: {field}")

    print("GITHUB_CONNECTOR_89_ACTION_INVENTORY=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
