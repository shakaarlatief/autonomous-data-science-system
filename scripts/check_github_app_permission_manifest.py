#!/usr/bin/env python3

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "docs/research/github_connector_89_action_inventory.json"
MANIFEST = ROOT / "docs/research/github_app_permission_manifest.json"
DOC = ROOT / "docs/research/GITHUB_APP_PERMISSION_MANIFEST.md"

EXPECTED_PERMISSIONS = {
    "actions": "write",
    "contents": "write",
    "issues": "write",
    "metadata": "read",
    "pull_requests": "write",
    "statuses": "read",
    "workflows": "write",
}

EXPECTED_GRAPHQL = {
    "GitHub.convert_pull_request_to_draft",
    "GitHub.dismiss_pull_request_review",
    "GitHub.enable_auto_merge",
    "GitHub.list_pull_request_review_threads",
    "GitHub.list_pull_request_reviews",
    "GitHub.mark_pull_request_ready_for_review",
    "GitHub.resolve_review_thread",
    "GitHub.unresolve_review_thread",
}

WORKFLOW_COVERAGE_ACTIONS = {
    "GitHub.create_branch",
    "GitHub.create_file",
    "GitHub.delete_file",
    "GitHub.update_file",
    "GitHub.update_ref",
}

NO_PERMISSION_ACTIONS = {
    "GitHub.get_profile",
    "GitHub.get_user_login",
    "GitHub.list_installations",
    "GitHub.list_installed_accounts",
    "GitHub.list_recent_issues",
    "GitHub.list_user_org_memberships",
    "GitHub.list_user_orgs",
}

LEVEL = {"read": 1, "write": 2}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    inventory = load(INVENTORY)
    manifest = load(MANIFEST)

    assert manifest["schemaVersion"] == 1
    assert manifest["targetActionCount"] == 89
    assert manifest["authorizationModel"] == "github-app-user-access-token-device-flow"
    assert manifest["githubComRestApiVersion"] == "2026-03-10"
    assert manifest["status"] == "REST_DERIVED_REGISTRATION_MANIFEST_FROZEN_GRAPHQL_SUFFICIENCY_PENDING_LIVE_PROBE"

    registration = manifest["registrationPermissionManifest"]
    assert registration["repositoryPermissions"] == EXPECTED_PERMISSIONS
    assert registration["organizationPermissions"] == {}
    assert registration["accountPermissions"] == {}
    assert registration["enterprisePermissions"] == {}
    assert registration["webhookActive"] is False
    assert registration["webhookEvents"] == []
    assert manifest["permissionCount"] == len(EXPECTED_PERMISSIONS) == 7

    disposition = manifest["permissionDisposition"]
    for forbidden in ("administration", "checks", "membersOrganization", "webhooksRepository"):
        assert disposition[forbidden] == "NO_ACCESS"
    assert disposition["organizationPermissions"] == "NONE"
    assert disposition["userAccountPermissions"] == "NONE"
    assert disposition["enterprisePermissions"] == "NONE"

    inv_actions = inventory["actions"]
    mapped = manifest["actions"]
    assert len(inv_actions) == len(mapped) == 89
    expected_pairs = [(a["ordinal"], a["nativeAction"], a["targetAction"]) for a in inv_actions]
    actual_pairs = [(a["ordinal"], a["nativeAction"], a["targetAction"]) for a in mapped]
    assert actual_pairs == expected_pairs
    assert len({a["nativeAction"] for a in mapped}) == 89

    graphql_actions = {a["nativeAction"] for a in mapped if a["graphqlPermissionSufficiencyProbeRequired"]}
    assert graphql_actions == EXPECTED_GRAPHQL
    graph = manifest["graphqlPermissionEvidence"]
    assert graph["officialExactPermissionMappingDocumented"] is False
    assert graph["candidatePermission"] == "pull_requests:write"
    assert graph["liveSufficiencyProbeRequiredBeforeDeviceFlowBroadQualification"] is True
    assert {a["nativeAction"] for a in graph["affectedActions"]} == EXPECTED_GRAPHQL

    workflow_actions = {a["nativeAction"] for a in mapped if a["mappingKind"] == "rest_conditional_workflows"}
    assert workflow_actions == WORKFLOW_COVERAGE_ACTIONS

    pure_none = {a["nativeAction"] for a in mapped if a["mappingKind"] == "rest_no_permission"}
    assert pure_none == NO_PERMISSION_ACTIONS

    assert manifest["searchPermissionEvidence"]["standaloneSearchPermissionExists"] is False
    assert manifest["fetchFacadeEvidence"]["addsPermission"] is False

    # Every declared requirement must be satisfied by the frozen manifest.
    # Alternative sets need at least one satisfiable branch; composite/single sets are
    # encoded as one or more explicit possible permission sets and checked the same way.
    for action in mapped:
        sets = action["requiredPermissionSets"]
        if not sets:
            continue
        satisfiable = False
        for req_set in sets:
            ok = True
            for req in req_set:
                selected = EXPECTED_PERMISSIONS.get(req["permission"])
                if selected is None or LEVEL[selected] < LEVEL[req["level"]]:
                    ok = False
                    break
            if ok:
                satisfiable = True
                break
        assert satisfiable, action["nativeAction"]

    # Permission necessity gates: these exact observed actions prevent accidental
    # weakening of the seven-permission manifest.
    by_name = {a["nativeAction"]: a for a in mapped}
    assert by_name["GitHub.rerun_failed_workflow_run_jobs"]["requiredPermissionSets"] == [[{"permission": "actions", "displayName": "Actions", "level": "write"}]]
    assert by_name["GitHub.rerun_workflow_job"]["requiredPermissionSets"] == [[{"permission": "actions", "displayName": "Actions", "level": "write"}]]
    assert by_name["GitHub.merge_pull_request"]["requiredPermissionSets"] == [[{"permission": "contents", "displayName": "Contents", "level": "write"}]]
    assert by_name["GitHub.create_issue"]["requiredPermissionSets"] == [[{"permission": "issues", "displayName": "Issues", "level": "write"}]]
    assert by_name["GitHub.create_pull_request"]["requiredPermissionSets"] == [[{"permission": "pull_requests", "displayName": "Pull requests", "level": "write"}]]
    assert by_name["GitHub.get_commit_combined_status"]["requiredPermissionSets"] == [[{"permission": "statuses", "displayName": "Commit statuses", "level": "read"}]]
    assert by_name["GitHub.get_repo_collaborator_permission"]["requiredPermissionSets"] == [[{"permission": "metadata", "displayName": "Metadata", "level": "read"}]]

    doc = DOC.read_text(encoding="utf-8")
    for token in (
        "actions=write", "contents=write", "issues=write", "metadata=read",
        "pull_requests=write", "statuses=read", "workflows=write",
        "GRAPHQL_LIVE_SUFFICIENCY_PROBE=REQUIRED",
        "ADMINISTRATION=NO_ACCESS", "CHECKS=NO_ACCESS", "MEMBERS=NO_ACCESS",
    ):
        assert token in doc

    print("GITHUB_APP_PERMISSION_MANIFEST=PASS")
    print("GITHUB_APP_PERMISSION_MANIFEST_ACTION_COUNT=89")
    print("GITHUB_APP_PERMISSION_MANIFEST_REPOSITORY_PERMISSION_COUNT=7")
    print("GITHUB_APP_GRAPHQL_PERMISSION_SUFFICIENCY=LIVE_PROBE_REQUIRED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
