# Validation 159: GitHub Read-Only Foundation Fresh-Host Qualified

**Date:** 2026-09-09
**Status:** PASS / FOUR GITHUB READ-ONLY FOUNDATION ACTIONS FRESH-HOST QUALIFIED
**Research:** Research 123
**Scope:** Preserve the refreshed fresh-disposable-ChatGPT host projection and exactly four live read-only Runtime Bridge GitHub calls after the local MCP foundation qualification of Validation 157.

## 1. Evidence boundary

The project owner supplied the completed fresh disposable ChatGPT qualification result after refreshing/rescanning the existing `Codexless Runtime Bridge` Plugin. The disposable qualification final marker is:

```text
GITHUB_READONLY_FOUNDATION_FRESH_HOST=PASS
```

The owner supplied the live-result and final-qualification sections in the persistent project conversation. Those sections establish that all four exact action names projected, their host-visible schemas remained bounded, and all four authorized read-only calls succeeded. The exact field-by-field Part A host-schema transcript was not recopied into this persistent conversation. Therefore this validation does not invent or reconstruct verbatim Part A details. Validation 157 remains the exact local MCP serialized-schema evidence; Validation 159 owns fresh-host action presence, boundedness and live read behavior.

## 2. Exact fresh-host action set

All four expected actions projected:

```text
github.get_profile
github.get_user_login
github.list_installations
github.list_repositories_by_installation
```

The supplied fresh-host qualification reports that the first two expose no caller input and the installation actions expose only the bounded filter/installation/pagination fields already expected from the foundation contract. It reports no caller-selected token, credential, GitHub host, URL, REST endpoint, GraphQL document, HTTP method, HTTP header, permission profile or equivalent arbitrary transport authority.

## 3. Exactly four live read-only calls

The calls ran in the required order and all succeeded.

### Call 1: `github.get_profile`

Bounded result:

```text
schemaVersion          codexless.github-readonly.v1
login                  shakaarlatief
databaseId             285787094
nodeId                 U_kgDOEQjD1g
name                   Shakaar Latief
company                null
location               null
bio                    empty string
htmlUrl                public GitHub profile URL
avatarUrl              public GitHub avatar URL
publicRepositoryCount  12
followerCount          0
followingCount         0
surfaceVersion         codexless-public-preview-v2
```

No credential or secret material was returned.

### Call 2: `github.get_user_login`

```text
schemaVersion   codexless.github-readonly.v1
login           shakaarlatief
surfaceVersion  codexless-public-preview-v2
```

The authenticated login agrees exactly with Call 1.

### Call 3: `github.list_installations(manageable_only=false)`

```text
installation count    1
account login         shakaarlatief
account type          User
repositorySelection   all
surfaceVersion        codexless-public-preview-v2
```

The result also carried bounded GitHub App permission metadata. The installation ID is intentionally not reproduced in this public validation. No token or credential was exposed.

### Call 4: `github.list_repositories_by_installation`

The call used exactly the installation ID returned by Call 3 with:

```text
page_size    20
page_offset  0
```

Result:

```text
totalCount  12
count       12
hasMore     false
canonical public ADS repository present  true
```

The canonical repository `shakaarlatief/autonomous-data-science-system` is inside the installation-authorized set. Unrelated private repository names are intentionally not enumerated.

## 4. Secret and mutation boundary

The supplied fresh-host qualification explicitly reports that none of the following appeared in host projection or live results:

```text
access token
refresh token
device code
client secret
Authorization header
credential-store payload
other credential secret
```

Exactly four GitHub calls were made and all four were read-only foundation actions. No GitHub mutation occurred.

## 5. Parity interpretation

This closes the Checkpoint 400/401 fresh-host projection gate. It does not close the known native-wrapper option gap:

```text
github.list_installations(manageable_only=true)
    -> exact managed-setup-account filter semantics remain unqualified
```

Only `manageable_only=false` was exercised. No claim is made that the native `manageable_only=true` behavior has been reproduced.

The native host also still hides machine-readable output schemas behind `any` across the 89-action baseline. Accordingly, exact native-wrapper wire parity remains conservatively `0 / 89`. The four foundation actions are now qualified as live Runtime Bridge capabilities across both local MCP and fresh ChatGPT host projection, but this validation does not redefine the project's exact-parity metric.

## 6. Continuation

Research 123 may now advance from the four-action foundation to the remaining G1 read-only identity/account/repository discovery and permission actions. The known `manageable_only=true` gap remains independently targeted and must not block unrelated read-only expansion.

```text
VALIDATION159=PASS
GITHUB_READONLY_FOUNDATION_FRESH_HOST=PASS
FRESH_HOST_ACTIONS_PROJECTED=4_OF_4
FRESH_HOST_LIVE_READS=4_OF_4_PASS
AUTHENTICATED_LOGIN=shakaarlatief
INSTALLATION_COUNT=1
INSTALLATION_ACCOUNT_TYPE=User
PERSONAL_INSTALLATION_REPOSITORY_SELECTION=all
CANONICAL_ADS_REPOSITORY_IN_SCOPE=true
SECRETS_EXPOSED=false
GITHUB_MUTATION_OCCURRED=false
MANAGEABLE_ONLY_TRUE=NOT_QUALIFIED
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
NEXT=G1_IDENTITY_ACCOUNT_REPOSITORY_PERMISSION_READONLY_EXPANSION
```
