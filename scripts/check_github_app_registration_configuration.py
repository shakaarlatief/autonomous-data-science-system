#!/usr/bin/env python3

import json
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "docs/research/github_app_registration_configuration.json"
PERMISSIONS = ROOT / "docs/research/github_app_permission_manifest.json"
DOC = ROOT / "docs/research/GITHUB_APP_REGISTRATION_CONFIGURATION.md"

EXPECTED_PERMISSIONS = {
    "actions": "write",
    "contents": "write",
    "issues": "write",
    "metadata": "read",
    "pull_requests": "write",
    "statuses": "read",
    "workflows": "write",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    cfg = load(CONFIG)
    perms = load(PERMISSIONS)
    assert cfg["schemaVersion"] == 1
    assert cfg["status"] == "FROZEN_OWNER_UI_REGISTRATION_REQUIRED"
    assert cfg["registrationOwner"] == {
        "accountType": "personal",
        "login": "shakaarlatief",
        "basis": cfg["registrationOwner"]["basis"],
    }
    ident = cfg["appIdentity"]
    assert ident["requestedName"] == "Codexless Runtime Bridge"
    assert ident["requestedNameLength"] == len(ident["requestedName"]) == 24
    assert ident["maxGitHubNameLength"] == 34
    assert ident["uniquenessMustBeConfirmedByGitHubAtCreation"] is True
    assert ident["homepageUrl"] == "https://github.com/shakaarlatief/autonomous-data-science-system"

    auth = cfg["authorizationSettings"]
    assert auth["enableDeviceFlow"] is True
    assert auth["requestUserAuthorizationDuringInstallation"] is False
    assert auth["expireUserAuthorizationTokens"] is True
    assert auth["callbackUrls"] == []
    assert auth["setupUrl"] is None
    assert auth["redirectOnUpdate"] is False
    assert auth["clientSecretRequiredForSelectedDeviceFlow"] is False
    assert auth["privateKeyRequiredForSelectedUserTokenDeviceFlow"] is False
    assert auth["generatePrivateKeyDuringBootstrap"] is False

    install = cfg["installationSettings"]
    assert install["visibility"] == "public"
    assert install["githubUiChoice"] == "Any account"
    assert install["initialQualificationInstallAccount"] == "shakaarlatief"
    assert install["initialRepositoryAccessPolicy"] == "only_selected_repositories"
    assert install["initialSelectedRepositories"] == ["shakaarlatief/autonomous-data-science-system"]

    webhook = cfg["webhookSettings"]
    assert webhook == {"active": False, "url": None, "secret": None, "events": []}
    assert cfg["permissions"] == EXPECTED_PERMISSIONS == perms["registrationPermissionManifest"]["repositoryPermissions"]
    assert cfg["organizationPermissions"] == {}
    assert cfg["accountPermissions"] == {}
    assert cfg["enterprisePermissions"] == {}

    parsed = urlparse(cfg["prefillRegistrationUrl"])
    assert parsed.scheme == "https"
    assert parsed.netloc == "github.com"
    assert parsed.path == "/settings/apps/new"
    q = parse_qs(parsed.query, keep_blank_values=True)
    expected_q = {
        "name": ["Codexless Runtime Bridge"],
        "description": [ident["description"]],
        "url": [ident["homepageUrl"]],
        "request_oauth_on_install": ["false"],
        "public": ["true"],
        "webhook_active": ["false"],
        **{key: [value] for key, value in EXPECTED_PERMISSIONS.items()},
    }
    assert q == expected_q

    checklist = cfg["manualCreationChecklist"]
    assert any("Enable Device Flow" in item for item in checklist)
    assert any("Expire user authorization tokens" in item for item in checklist)
    assert any("Do not generate a private key" in item for item in checklist)
    assert any("Only select repositories" in item for item in checklist)

    doc = DOC.read_text(encoding="utf-8")
    for token in (
        "GITHUB_APP_REGISTRATION_CONFIGURATION=FROZEN",
        "GITHUB_APP_VISIBILITY=ANY_ACCOUNT_PUBLIC",
        "DEVICE_FLOW=ENABLED",
        "REQUEST_OAUTH_ON_INSTALL=DISABLED",
        "EXPIRE_USER_AUTH_TOKENS=ENABLED",
        "WEBHOOKS=DISABLED",
        "REPOSITORY_PERMISSION_COUNT=7",
        "INITIAL_INSTALL_SCOPE=ONLY_SELECTED_REPOSITORIES",
        "PRIVATE_KEY_BOOTSTRAP=NOT_USED",
    ):
        assert token in doc

    print("GITHUB_APP_REGISTRATION_CONFIGURATION=PASS")
    print("GITHUB_APP_REGISTRATION_OWNER=shakaarlatief")
    print("GITHUB_APP_REGISTRATION_VISIBILITY=ANY_ACCOUNT_PUBLIC")
    print("GITHUB_APP_INITIAL_INSTALL_SCOPE=ONE_SELECTED_REPOSITORY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
