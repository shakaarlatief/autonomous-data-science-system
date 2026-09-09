# Validation 151: GitHub Live Permission UI 118-Option Reconciliation

**Date:** 2026-09-09
**Status:** PASS / COMPLETE LIVE UI INVENTORY / BROAD DEVELOPER-SUPERSET CANDIDATE READY
**Research:** Research 123
**Scope:** Reconcile the complete owner-supplied live GitHub App registration permission UI against current GitHub documentation and freeze a machine-validated broad permission-selection candidate before App creation.

The supplied screenshots cover all four live permission groups. The exact live count is:

```text
Repository permissions   40
Organization permissions 42
Account permissions      19
Enterprise permissions   17
Total                    118
```

The live UI is broader than the consolidated public permission index alone and contains current/preview surfaces such as Agent tasks, Discussions, License compliance alerts, Merge queues, Packages, Projects, secret-scanning request permissions, Models, Copilot context/settings permissions, organization credentials/security families, and expanded enterprise-preview permissions.

Machine artifacts:

```text
docs/research/github_app_live_permission_inventory_20260909.json
docs/research/GITHUB_APP_LIVE_PERMISSION_RECONCILIATION_20260909.md
scripts/check_github_app_live_permission_inventory.py
```

The candidate intentionally optimizes **maximum useful professional developer capability**, not maximum unchecked authority:

```text
repository enable/read candidate  34 / 40
organization enable/read candidate 30 / 42
account enable/read candidate      10 / 19
enterprise enable candidate         0 / 17
```

The six repository permissions kept off are:

```text
Agent secrets
Codespaces secrets
Dependabot secrets
Secrets
Single file
Webhooks
```

Secret-value families remain deferred until Codexless has a dedicated secure secret-value transport/mutation contract. `Single file` is redundant with broader Contents authority. Webhooks remain deferred because arbitrary external hook destinations create an exfiltration-capable surface that should be independently bounded.

Repository Administration(write) is retained as a core extension candidate because GitHub confirms it supports authenticated-user and organization repository creation plus broad repository settings/administration. Agent tasks are retained because GitHub currently supports them with GitHub App user access tokens, matching the selected authorization architecture.

Organization authority is broad but still excludes credential/secret/PAT/webhook/billing-oriented families that do not yet have a concrete safe workflow. Account permissions remain selective and developer-oriented. Enterprise permissions remain entirely off because there is no established enterprise target and some enterprise installation-management permissions constrain cross-enterprise installability.

The intended personal installation scope is now:

```text
shakaarlatief
All repositories
```

rather than the earlier one-repository qualification scope.

Validator result:

```text
GITHUB_APP_LIVE_PERMISSION_INVENTORY=PASS
GITHUB_APP_LIVE_PERMISSION_OPTION_COUNT=118
GITHUB_APP_BROAD_REPOSITORY_PERMISSION_ENABLE_COUNT=34
GITHUB_APP_BROAD_ORGANIZATION_PERMISSION_ENABLE_COUNT=30
GITHUB_APP_BROAD_ACCOUNT_PERMISSION_ENABLE_COUNT=10
GITHUB_APP_ENTERPRISE_PERMISSION_ENABLE_COUNT=0
```

No GitHub App has been created and no GitHub authorization has started.

```text
VALIDATION151=PASS
LIVE_PERMISSION_UI_CAPTURE=COMPLETE
LIVE_PERMISSION_OPTION_COUNT=118
BROAD_SUPERSET_CANDIDATE=READY
PARITY_ONLY_APP_CREATION=SUPERSEDED
PERSONAL_INSTALL_SCOPE=ALL_REPOSITORIES
GITHUB_APP_REGISTERED=false
LIVE_GITHUB_AUTH=NOT_STARTED
NEXT=FREEZE_EXTENDED_PERMISSION_MANIFEST_AND_REBUILD_REGISTRATION_PREFILL
```
