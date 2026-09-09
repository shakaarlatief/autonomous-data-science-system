# Validation 161: GitHub G1 Read-Only Fresh-Host Transport Failure Localized

**Date:** 2026-09-09
**Status:** FAIL / SEVEN-ACTION HOST PROJECTION PASS / SIX-OF-SEVEN LIVE READS PASS / SINGLE CONNECTOR NETWORK FAILURE LOCALIZED
**Research:** Research 123
**Scope:** Preserve the refreshed fresh-ChatGPT-host qualification of the seven preview.30 G1 read-only GitHub actions, including the single connector transport failure on `github.list_installed_accounts`, and discriminate that failure from the already-qualified active Runtime Bridge action without retrying the failed fresh-host call inside the original qualification.

## 1. Evidence boundary

The project owner supplied the completed disposable-chat qualification with final marker:

```text
GITHUB_G1_READONLY_FRESH_HOST=FAIL
```

All seven exact action names projected in the refreshed host and their schemas were reported as bounded. The owner supplied the complete Part B live-result and Part C qualification summary in the persistent project conversation. The field-by-field Part A schema transcript was not recopied into this persistent conversation, so this validation preserves host presence/boundedness without inventing missing verbatim schema text. Validation 160 remains the exact local MCP schema and local-live evidence for the same seven actions.

## 2. Fresh-host projection result

All seven expected preview.30 actions projected:

```text
github.get_repo
github.get_repo_collaborator_permission
github.list_installed_accounts
github.list_repositories
github.list_repositories_by_affiliation
github.list_user_org_memberships
github.list_user_orgs
```

The supplied qualification reports that the host-visible contracts remain specific semantic selector/filter/pagination objects and expose no caller-selected token, credential, GitHub host, arbitrary URL, REST endpoint, GraphQL document, HTTP method/header, permission profile or equivalent arbitrary transport authority.

Accordingly, the preview.30 host-projection gate itself passed at 7/7. The overall qualification failed only because one required live read did not return an application result.

## 3. Exactly seven attempted read-only calls

All seven calls were attempted exactly once in the required order. No retry occurred inside the qualification.

### Call 1: `github.get_repo`

Succeeded for the canonical repository:

```text
fullName       shakaarlatief/autonomous-data-science-system
owner          shakaarlatief
name           autonomous-data-science-system
id             1327144624
visibility     public
defaultBranch  main
archived       false
disabled       false
```

### Call 2: `github.get_repo_collaborator_permission`

Succeeded:

```text
repositoryFullName  shakaarlatief/autonomous-data-science-system
username            shakaarlatief
permission          admin
roleName            admin
```

### Call 3: `github.list_installed_accounts`

Did not return an application result. The single invocation failed at the connector transport layer:

```text
type     mcp_network_error
code     network_error
message  Connection failed.
```

Therefore the fresh-host installed-account count and authenticated-personal-User presence are unverified by this attempt. The call was not retried.

### Call 4: `github.list_repositories`

Succeeded with the requested owner filter and `include_search_index_status=false`:

```text
totalCount               12
returnedCount            12
hasMore                  false
canonical ADS repository present  true
```

Unrelated repository names were omitted.

### Call 5: `github.list_repositories_by_affiliation`

Succeeded with `affiliation=owner`:

```text
totalCount               12
returnedCount            12
hasMore                  false
canonical ADS repository present  true
```

Unrelated repository names were omitted.

### Calls 6 and 7: organization reads

Both succeeded:

```text
github.list_user_org_memberships  count=0
github.list_user_orgs             count=0
```

## 4. Secret and mutation boundary

The supplied fresh-host result reports no access token, refresh token, device code, client secret, Authorization header, credential-store payload or other credential secret in any schema, successful result or failure payload. No arbitrary GitHub request/credential surface was exposed. All attempted actions were read-only and no GitHub mutation occurred.

## 5. Post-failure local discriminator

After the owner supplied the failed fresh-host result, the persistent project conversation performed no host retry of the failed action. Instead it used the already-qualified active loopback MCP surface as a read-only discriminator.

Current authorization metadata remained healthy:

```text
configured           true
authorized           true
storedAuthorization  true
accessExpired        false
refreshExpired       false
refreshRecommended   false
```

A fresh stateless loopback MCP initialization then invoked exactly `github.list_installed_accounts` read-only. It succeeded immediately:

```text
schemaVersion          codexless.github-readonly.v1
count                  1
containsPersonalUser   true
```

The matching account is `shakaarlatief` with account type `User`. No installation ID, unrelated repository name or credential was printed.

This discriminator establishes that the preview.30 action itself and the stored GitHub authorization remained operational after the fresh-host failure. It does not prove the exact root cause of `mcp_network_error`. The failure is therefore localized conservatively to the fresh ChatGPT connector transport path for that invocation, or another transient layer before an application result was returned, rather than classified as a Runtime Bridge action-contract or authorization failure.

## 6. Qualification disposition

The complete seven-action fresh-host qualification remains FAIL because its contract required all seven live reads to succeed:

```text
fresh-host actions projected      7 / 7 PASS
fresh-host bounded schemas        7 / 7 PASS
fresh-host live reads succeeded   6 / 7
failed live action                github.list_installed_accounts
failure class                     connector network / no application result
post-failure local action         PASS
GitHub mutation                   none
secret exposure                   none
```

The six successful fresh-host live actions do not need to be discarded or blindly repeated. The unresolved host gate is now exactly one read-only action.

## 7. Next discriminator

Because the failed operation is read-only, returned no application result, and is independently healthy on the active local MCP surface, the smallest next experiment is one separately authorized host requalification of only:

```text
github.list_installed_accounts
```

The follow-up may use the same already-refreshed disposable conversation if that conversation still projects the action, because the purpose is now a new targeted retry after the original no-retry qualification has been durably preserved. A new disposable conversation is also valid if the old one is no longer available. No Plugin rescan or runtime publication is required before this discriminator because the seven actions already projected successfully and local preview.30 remains healthy.

If the one targeted host call succeeds and returns the already-expected bounded one-account result, Research 123 may close the G1 fresh-host gate without rerunning the other six successful actions. If it fails again, preserve the exact connector error and investigate the host/tunnel transport path before G2.

```text
VALIDATION161=FAIL
GITHUB_G1_READONLY_FRESH_HOST=FAIL
FRESH_HOST_G1_ACTIONS_PROJECTED=7_OF_7
FRESH_HOST_G1_SCHEMA_BOUNDEDNESS=PASS_7_OF_7
FRESH_HOST_G1_LIVE_READS=6_OF_7_PASS
FAILED_ACTION=github.list_installed_accounts
FAILED_ACTION_ERROR_TYPE=mcp_network_error
FAILED_ACTION_ERROR_CODE=network_error
FAILED_ACTION_ERROR_MESSAGE=Connection_failed
POST_FAILURE_LOCAL_LIST_INSTALLED_ACCOUNTS=PASS
PROTECTED_AUTHORIZATION_HEALTHY=true
SECRETS_EXPOSED=false
GITHUB_MUTATION_OCCURRED=false
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
NEXT=TARGETED_HOST_LIST_INSTALLED_ACCOUNTS_REQUALIFICATION
```
