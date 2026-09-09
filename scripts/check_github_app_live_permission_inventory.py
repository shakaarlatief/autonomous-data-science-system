#!/usr/bin/env python3

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "docs/research/github_app_live_permission_inventory_20260909.json"
DOC = ROOT / "docs/research/GITHUB_APP_LIVE_PERMISSION_RECONCILIATION_20260909.md"

EXPECTED_COUNTS = {"repository": 40, "organization": 42, "account": 19, "enterprise": 17, "total": 118}
EXPECTED_CURRENT = {
    "Actions": "read_write",
    "Commit statuses": "read_only",
    "Contents": "read_write",
    "Issues": "read_write",
    "Metadata": "read_only_mandatory",
    "Pull requests": "read_write",
    "Workflows": "read_write",
}
EXPECTED_REPO_DEFER = {"Agent secrets", "Codespaces secrets", "Dependabot secrets", "Secrets", "Single file", "Webhooks"}

def main():
    d = json.loads(PATH.read_text(encoding="utf-8"))
    assert d["schemaVersion"] == 1
    assert d["status"] == "LIVE_UI_CAPTURE_COMPLETE_BROAD_SUPERSET_CANDIDATE"
    assert d["counts"] == EXPECTED_COUNTS
    sections = [
        ("repositoryPermissions", 40),
        ("organizationPermissions", 42),
        ("accountPermissions", 19),
        ("enterprisePermissions", 17),
    ]
    all_names = []
    for key, count in sections:
        rows = d[key]
        assert len(rows) == count
        assert len({row["name"] for row in rows}) == count
        all_names.extend((key, row["name"]) for row in rows)
    assert len(all_names) == 118

    repo = {row["name"]: row for row in d["repositoryPermissions"]}
    current = {name: row["currentlySelected"] for name, row in repo.items() if row["currentlySelected"] is not None}
    assert current == EXPECTED_CURRENT
    repo_defer = {row["name"] for row in repo.values() if row["recommendedAccess"] == "no_access"}
    assert repo_defer == EXPECTED_REPO_DEFER
    assert sum(row["recommendedAccess"] != "no_access" for row in repo.values()) == 34

    org = d["organizationPermissions"]
    assert sum(row["recommendedAccess"] != "no_access" for row in org) == 30
    acct = d["accountPermissions"]
    assert sum(row["recommendedAccess"] != "no_access" for row in acct) == 10
    ent = d["enterprisePermissions"]
    assert all(row["recommendedAccess"] == "no_access" for row in ent)

    policy = d["policy"]
    assert policy["personalInstallationScope"] == "all_repositories"
    assert "repository Single file is unnecessary because Contents(read/write) is broader" in policy["redundantFamilies"]
    assert "enterprise permissions" in policy["deferredSensitiveFamilies"]

    doc = DOC.read_text(encoding="utf-8")
    for token in [
        "LIVE_PERMISSION_OPTION_COUNT=118",
        "REPOSITORY_OPTIONS=40",
        "ORGANIZATION_OPTIONS=42",
        "ACCOUNT_OPTIONS=19",
        "ENTERPRISE_OPTIONS=17",
        "PERSONAL_INSTALL_SCOPE=ALL_REPOSITORIES",
        "SECRET_VALUE_PERMISSIONS=DEFER",
        "WEBHOOK_MANAGEMENT=DEFER",
    ]:
        assert token in doc

    print("GITHUB_APP_LIVE_PERMISSION_INVENTORY=PASS")
    print("GITHUB_APP_LIVE_PERMISSION_OPTION_COUNT=118")
    print("GITHUB_APP_BROAD_REPOSITORY_PERMISSION_ENABLE_COUNT=34")
    print("GITHUB_APP_BROAD_ORGANIZATION_PERMISSION_ENABLE_COUNT=30")
    print("GITHUB_APP_BROAD_ACCOUNT_PERMISSION_ENABLE_COUNT=10")
    print("GITHUB_APP_ENTERPRISE_PERMISSION_ENABLE_COUNT=0")

if __name__ == "__main__":
    main()
