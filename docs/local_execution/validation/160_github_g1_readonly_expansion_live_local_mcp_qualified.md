# Validation 160: GitHub G1 Read-Only Expansion Live Local MCP Qualified

**Date:** 2026-09-09
**Status:** PASS / PREVIEW.30 LIVE / ELEVEN READ-ONLY GITHUB TOOLS LIVE LOCALLY / FRESH-HOST G1 QUALIFICATION NEXT
**Research:** Research 123
**Scope:** Publish and activate seven additional bounded G1 GitHub identity/account/repository-discovery/permission reads, prove the 75-tool active MCP surface, live-invoke all seven new actions read-only against the stored GitHub App user authorization, and preserve remaining native-wrapper option plus fresh-host projection gaps without claiming exact 89-action parity.

## 1. Starting boundary

Validation 159 / Checkpoint 402 had fresh-host-qualified the first four public GitHub read-only foundation actions. The next Research 123 slice was the remainder of G1 identity/account/repository-discovery/permission reads.

The seven new actions are:

```text
github.get_repo
github.get_repo_collaborator_permission
github.list_installed_accounts
github.list_repositories
github.list_repositories_by_affiliation
github.list_user_org_memberships
github.list_user_orgs
```

The four already-live foundation actions remain unchanged, so the target public GitHub read-only count becomes eleven.

## 2. Bounded implementation contract

The new actions reuse the server-owned GitHub App user-token authority and fixed GitHub REST transport. Repository reads are intersected with App installation-derived scope before repository-specific API calls or returned collections are accepted. Callers receive no token, credential, arbitrary host, arbitrary endpoint, HTTP method/header or permission-profile authority.

Two known native/platform gaps remain fail-closed rather than guessed:

```text
github.list_installations(manageable_only=true)
    -> still GITHUB_PARITY_OPTION_NOT_QUALIFIED

github.list_repositories(include_search_index_status=true)
    -> GITHUB_PARITY_OPTION_NOT_QUALIFIED because the native enrichment contract is hidden

github.get_repo(repository_url=<Enterprise host>)
    -> initial Runtime Bridge repository_url support remains github.com-only; Enterprise parity is separate
```

The ordinary `github.get_repo` full-name and numeric-ID selectors remain installation-scoped. `github.list_repositories_by_affiliation` uses GitHub's owner/collaborator/organization_member affiliation values and intersects the result with installation-authorized repositories.

## 3. Private runtime source and release

Private local-runtime head:

```text
7af8600dd2213d2fc2e5aca3b3ef32b8fafeacc6
```

Immutable release:

```text
releaseId               github-g1-readonly-expansion-v1
targetVersion           0.1.1-preview.30-github-g1-readonly
targetSurfaceVersion    codexless-public-preview-v2
targetToolCount         75
fileCount               9
runtimeDependencyCount  1
manifestSha256          32073454a400b62d7957f965de6624183bb220b21a5ccac5b9a10b244020595a
regressionCount         16
```

A first prepare attempt correctly failed because the candidate manifest declared 18 regressions while Runtime Release v2 bounds a bundle to at most 16. The release was corrected without widening the runtime-release contract, committed and pushed, and the new prepare succeeded.

A conservative private-runtime secret scanner also rejected an earlier synthetic test fixture whose string merely resembled a credential. The scanner was not weakened; the fixture was changed to a non-secret-safe synthetic value and private publication then passed normally. No real credential was involved.

## 4. Release publication and activation

Prepublication verification returned the expected source difference against the then-live preview.29 baseline:

```text
status         verification_failed
mismatchCount 9
```

This was the intended prepublication discriminator because all nine declared release targets differed from the current installed source.

Publication operation:

```text
operationId        rm_bc3ee2e4f09d12ed8f92af6686663961
requestId          r123.g1-readonly.publish.20260909.01
status             succeeded
errorCode           null
recoveryAttempted   false
```

Activation operation:

```text
operationId        rm_9c321da1381ec4ebd69657441d939be6
requestId          r123.g1-readonly.restart.20260909.01
status             succeeded
errorCode           null
recoveryAttempted   false
```

Fresh postactivation verification returned:

```text
status                   verified
targetVersion            0.1.1-preview.30-github-g1-readonly
targetToolCount          75
fileCount                9
runtimeDependencyCount   1
mismatchCount            0
```

## 5. Live process and protected authorization

Direct loopback health after activation returned:

```text
ok             true
service        codexless-public
transport      streamable-http
version        0.1.1-preview.30-github-g1-readonly
toolCount      75
surfaceVersion codexless-public-preview-v2
```

Postrestart GitHub authorization metadata reported:

```text
configured           true
initialized          false
authorized           true
storedAuthorization  true
accessExpired        false
refreshExpired       false
refreshRecommended   false
authMode             github-app-user-token-device-flow
host                 github.com
restApiVersion       2026-03-10
```

A subsequent live `github.get_profile` call succeeded and again resolved authenticated login `shakaarlatief`, proving the stored protected authorization remained usable after activation without exposing credential values.

## 6. Live local MCP tools/list qualification

A fresh stateless initialize/tools-list call against the active loopback MCP endpoint returned:

```text
serverVersion   0.1.1-preview.30-github-g1-readonly
totalToolCount  75
githubToolCount 11
```

The exact public GitHub action set is:

```text
github.get_profile
github.get_user_login
github.list_installations
github.list_repositories_by_installation
github.get_repo
github.get_repo_collaborator_permission
github.list_installed_accounts
github.list_repositories
github.list_repositories_by_affiliation
github.list_user_org_memberships
github.list_user_orgs
```

The seven new serialized schemas are strict bounded objects with no additional arbitrary transport fields. `github.get_repo` exposes only three optional repository selectors, `github.get_repo_collaborator_permission` requires repository full name plus username, `github.list_installed_accounts`/organization calls are empty-object reads, repository listing exposes bounded pagination/filter fields, and affiliation listing requires one affiliation string plus pagination.

## 7. Seven live GitHub G1 reads

The same active loopback MCP surface invoked every new action exactly once read-only using only canonical/public or count-level preserved output. The qualification deliberately did not print unrelated private repository names or any credential data.

Observed results:

```text
github.get_repo
    canonical repository             shakaarlatief/autonomous-data-science-system
    private                          false
    default branch                   main
    visibility                       public

github.get_repo_collaborator_permission
    repository                       canonical ADS repository
    username                         shakaarlatief
    permission                       admin
    roleName                         admin

github.list_installed_accounts
    count                            1
    authenticated personal account   present as User

github.list_repositories
    owner filter                     shakaarlatief
    includeSearchIndexStatus         false
    totalCount                       12
    count                            12
    hasMore                          false
    canonical ADS repository         present

github.list_repositories_by_affiliation
    affiliation                      owner
    totalCount                       12
    count                            12
    hasMore                          false
    canonical ADS repository         present

github.list_user_org_memberships
    count                            0

github.list_user_orgs
    count                            0
```

No GitHub mutation occurred. No access token, refresh token, device code, client secret, Authorization header or credential-store payload was printed or returned through the preserved qualification output.

## 8. Parity disposition

The Runtime Bridge now has eleven live read-only GitHub actions, consisting of the four fresh-host-qualified foundation actions plus seven newly local-live-qualified G1 actions. This is stronger capability evidence but does not change the project's conservative exact native-wrapper parity metric.

The native connector still hides machine-readable output schemas behind `any`, and known action-specific option/result semantics remain unresolved. Therefore:

```text
live public github.* read-only tools   11
foundation fresh-host qualified         4
new G1 local-live qualified              7
exact native parity rows closed          0
remaining exact native rows             89
```

## 9. Same-chat host projection and next gate

After preview.30 activation, the active loopback MCP tools list contained all eleven GitHub actions, but this persistent ChatGPT conversation's connector projection still exposed only the earlier four GitHub actions. A host-resource rediscovery query for the new repository actions did not project the seven new names. This is the established AB-008 same-conversation stale-projection behavior, not evidence that the live runtime publication failed.

The next gate is therefore one refreshed fresh disposable ChatGPT conversation that discovers the seven new names, records their host-visible schemas before invocation, and live-invokes all seven read-only without exposing unrelated private repository names.

```text
VALIDATION160=PASS
PRIVATE_RUNTIME_HEAD=7af8600dd2213d2fc2e5aca3b3ef32b8fafeacc6
LIVE_RUNTIME_VERSION=0.1.1-preview.30-github-g1-readonly
LIVE_MCP_TOOL_COUNT=75
LIVE_GITHUB_READONLY_TOOLS=11
G1_NEW_TOOLS=7
LOCAL_MCP_TOOLS_LIST=PASS
G1_LIVE_READS=7_OF_7_PASS
PROTECTED_AUTHORIZATION_PRESERVED=true
SECRETS_EXPOSED=false
GITHUB_MUTATION_OCCURRED=false
MANAGEABLE_ONLY_TRUE=NOT_QUALIFIED
INCLUDE_SEARCH_INDEX_STATUS_TRUE=NOT_QUALIFIED
ENTERPRISE_REPOSITORY_URL=NOT_QUALIFIED
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
SAME_CHAT_NEW_TOOL_PROJECTION=STALE
NEXT=FRESH_CHAT_GITHUB_G1_READONLY_SCHEMA_AND_LIVE_READ_QUALIFICATION
```
