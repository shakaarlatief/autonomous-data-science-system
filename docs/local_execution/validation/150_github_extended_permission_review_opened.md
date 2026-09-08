# Validation 150: GitHub Extended Permission Review Opened

**Date:** 2026-09-08
**Status:** PASS / PARITY-ONLY APP CREATION PAUSED / EXTENDED CAPABILITY INVENTORY OPEN
**Research:** Research 123
**Scope:** Preserve the project-owner clarification that Codexless Runtime Bridge should exceed the native ChatGPT GitHub connector where useful, pause the seven-permission parity-only App creation instruction before any GitHub App is created, and establish the official current permission inventory/recommendation framework for an extended developer superset.

## 1. Scope clarification

The project owner explicitly wants Codexless Runtime Bridge to support capabilities that the provider-owned ChatGPT GitHub integration does not expose, including repository creation/administration and other useful GitHub operations available through a project-owned GitHub App.

This changes the product target from:

```text
native GitHub connector parity only
```

to:

```text
native parity
+
selected GitHub extensions
=
maximum useful professional developer capability
```

No GitHub App has yet been created, so permission expansion can be designed before first registration rather than immediately triggering an installed-App permission upgrade cycle.

## 2. Native provider app versus project-owned App

The existing ChatGPT GitHub integration remains provider-owned. The project cannot change that app's GitHub permission grant or native tool surface merely by packaging/orchestrating it with Codexless.

The dedicated `Codexless Runtime Bridge` GitHub App is project-owned and can request additional GitHub permission families. Runtime Bridge can then expose new bounded semantic actions on top of those permissions.

## 3. Official permission inventory baseline

Current GitHub documentation classifies App permissions as repository, organization, account/user, and enterprise permissions. The main current permission reference enumerates:

```text
31 established repository permission headings
31 organization permission headings
14 account/user permission headings
2 enterprise permission headings
```

The live GitHub registration UI supplied by the owner additionally exposes newer preview permission families such as `Agent tasks`; GitHub documents Agent tasks separately and currently supports GitHub App user access tokens for those endpoints.

`GITHUB_APP_EXTENDED_PERMISSION_REVIEW.md` now preserves the full established heading inventory, the live/preview reconciliation boundary, and capability-oriented recommendations.

## 4. High-value extension finding

Repository `Administration = Read & write` is the strongest immediate extension candidate because GitHub documents it as covering repository creation/deletion/settings/teams/collaborators and related administrative endpoints. It directly supports the owner's requested capabilities such as creating repositories and managing repository settings/collaborators.

The same permission materially changes organization installation policy: an organization repository admin cannot independently install an App requesting repository Administration; organization-owner approval is required. This tradeoff is now explicit.

Other strong extension candidates identified for detailed selection include:

```text
Checks(write)
Commit statuses(write)
Deployments(write)
Environments(write)
Variables(write)
Code scanning alerts(write)
Dependabot alerts(write)
Secret scanning alerts(write)
Attestations(write)
Agent tasks(write, preview)
Agent variables(write)
Codespaces families where desired
Pages(write) where desired
Custom properties(write) where desired
```

## 5. Secret and webhook authority is deliberately not auto-selected

For maximum **useful** capability, the review distinguishes broad developer authority from unrelated/high-risk authority.

Secret-bearing families such as repository/Dependabot/Codespaces/agent secrets are deferred until Codexless has a secure secret-value transport and mutation contract. Repository Webhooks(write) is also deferred because it can create arbitrary external destinations and therefore needs explicit destination-bounding architecture rather than blanket selection.

This is not a rejection of those future capabilities; it is a sequencing requirement.

## 6. Personal installation scope correction

The owner clarified that Codexless should access all repositories available under the relevant installation, like the normal connector rather than remaining permanently restricted to the ADS repository.

Therefore the intended personal-account installation target is now:

```text
shakaarlatief
All repositories
```

rather than the Checkpoint 392 first-installation instruction `Only select repositories -> autonomous-data-science-system`.

Organization repositories still require installing/approving the same public App on the relevant organization/account and remain constrained by installation scope plus the authorizing user's own access.

## 7. Checkpoint 391/392 disposition

Checkpoints 391 and 392 remain valid historical evidence of the parity-derived manifest and registration preflight, but the instruction to create the App immediately with only seven repository permissions is now **superseded and paused**.

Do not create the App from the old Checkpoint 392 prefill while this review is active.

## 8. Next boundary

The immediate next task is to capture/reconcile the complete live GitHub registration permission surface for this account against the official docs, including preview/live-only categories, then freeze a broad professional developer-superset selection.

The final decision should optimize:

```text
maximum useful GitHub development capability
bounded/designed destructive authority
broad personal repository coverage
realistic organization-installation approval
no speculative secret/exfiltration authority
```

```text
VALIDATION150=PASS
PARITY_ONLY_APP_CREATION=PAUSED
EXTENDED_PERMISSION_REVIEW=ACTIVE
REPOSITORY_ADMINISTRATION=STRONG_CANDIDATE
PERSONAL_INSTALL_SCOPE=ALL_REPOSITORIES
GITHUB_APP_REGISTERED=false
GITHUB_APP_CLIENT_ID_CONFIGURED=false
LIVE_GITHUB_AUTH=NOT_STARTED
NEXT=CAPTURE_AND_RECONCILE_COMPLETE_LIVE_PERMISSION_UI
```
