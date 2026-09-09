#!/usr/bin/env python3

import json
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/research/github_app_extended_permission_manifest.json"
REGISTRATION = ROOT / "docs/research/github_app_extended_registration_configuration.json"
LIVE = ROOT / "docs/research/github_app_live_permission_inventory_20260909.json"

EXPECTED_COUNTS = {"repository": 34, "organization": 30, "account": 10, "enterprise": 0, "total": 74}
EXPECTED_NO_ACCESS = {"repository": 6, "organization": 12, "account": 9, "enterprise": 17}
PARITY_REQUIRED = {
    "Actions": "write",
    "Contents": "write",
    "Issues": "write",
    "Metadata": "read",
    "Pull requests": "write",
    "Commit statuses": "write",
    "Workflows": "write",
}
REPO_OFF = {"Agent secrets", "Codespaces secrets", "Dependabot secrets", "Secrets", "Single file", "Webhooks"}

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def by_name(rows):
    return {r["displayName"]: r for r in rows}

def main():
    m = load(MANIFEST)
    r = load(REGISTRATION)
    live = load(LIVE)
    assert m["schemaVersion"] == 1
    assert m["status"] == "FROZEN_EXTENDED_DEVELOPER_SUPERSET"
    assert m["selectedCounts"] == EXPECTED_COUNTS
    assert m["liveOptionCounts"] == {"repository": 40, "organization": 42, "account": 19, "enterprise": 17, "total": 118}
    assert live["counts"] == m["liveOptionCounts"]

    repo = by_name(m["repositoryPermissions"])
    org = by_name(m["organizationPermissions"])
    acct = by_name(m["accountPermissions"])
    assert len(repo) == 34 and len(org) == 30 and len(acct) == 10
    for name, access in PARITY_REQUIRED.items():
        assert repo[name]["access"] == access
    assert repo["Administration"]["access"] == "write"
    assert repo["Checks"]["access"] == "write"
    assert repo["Projects"]["access"] == "admin"
    assert org["Custom properties"]["access"] == "admin"
    assert org["Projects"]["access"] == "admin"
    assert acct["Models"]["access"] == "read"

    for scope, count in EXPECTED_NO_ACCESS.items():
        values = m["explicitNoAccess"][scope]
        assert len(values) == count
        assert len(set(values)) == count
    assert set(m["explicitNoAccess"]["repository"]) == REPO_OFF
    assert all("secret" not in r["prefillParameter"].lower() for r in m["repositoryPermissions"] if r["prefillParameter"] and r["displayName"] != "Secret scanning alerts")
    assert "repository_hooks" not in {x["prefillParameter"] for x in m["repositoryPermissions"] if x["prefillParameter"]}
    assert "organization_hooks" not in {x["prefillParameter"] for x in m["organizationPermissions"] if x["prefillParameter"]}

    manual = m["prefill"]["manualLiveUiSelections"]
    assert m["prefill"]["documentedPermissionParameterCount"] == 56
    assert m["prefill"]["manualLiveUiPermissionCount"] == len(manual) == 18
    assert 56 + 18 == 74

    parsed = urlparse(m["prefill"]["url"])
    assert parsed.scheme == "https" and parsed.netloc == "github.com" and parsed.path == "/settings/apps/new"
    q = parse_qs(parsed.query)
    assert q["name"] == ["Codexless Runtime Bridge"]
    assert q["public"] == ["true"]
    assert q["webhook_active"] == ["false"]
    assert q["request_oauth_on_install"] == ["false"]
    permission_params = {
        row["prefillParameter"]: row["access"]
        for rows in (m["repositoryPermissions"], m["organizationPermissions"], m["accountPermissions"])
        for row in rows if row["prefillParameter"]
    }
    assert len(permission_params) == 56
    for key, value in permission_params.items():
        assert q[key] == [value], (key, q.get(key), value)
    assert set(q) == {"name","description","url","request_oauth_on_install","public","webhook_active",*permission_params.keys()}

    assert r["status"] == "FROZEN_EXTENDED_REGISTRATION_CONFIGURATION"
    assert r["selectedCounts"] == EXPECTED_COUNTS
    assert r["prefill"]["url"] == m["prefill"]["url"]
    assert r["visibility"] == {"githubUiChoice": "Any account", "public": True}
    assert r["authorizationSettings"]["enableDeviceFlow"] is True
    assert r["authorizationSettings"]["expireUserAuthorizationTokens"] is True
    assert r["authorizationSettings"]["requestUserAuthorizationDuringInstallation"] is False
    assert r["webhookSettings"] == {"active": False, "url": None, "secret": None, "events": []}
    assert r["installationSettings"]["initialRepositoryAccessPolicy"] == "all_repositories"
    assert r["bootstrapCredentials"]["privateKey"].startswith("do not generate/use")

    print("GITHUB_APP_EXTENDED_PERMISSION_MANIFEST=PASS")
    print("GITHUB_APP_EXTENDED_SELECTED_PERMISSION_COUNT=74")
    print("GITHUB_APP_EXTENDED_DOCUMENTED_PREFILL_COUNT=56")
    print("GITHUB_APP_EXTENDED_MANUAL_PERMISSION_COUNT=18")
    print("GITHUB_APP_EXTENDED_PERSONAL_INSTALL_SCOPE=ALL_REPOSITORIES")

if __name__ == "__main__":
    main()
