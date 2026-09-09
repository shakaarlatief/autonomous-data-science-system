# Validation 162: GitHub G1 Installed-Accounts Host Recheck Passed

**Date:** 2026-09-09
**Status:** PASS / TARGETED HOST RECHECK SUCCEEDED / G1 FRESH-HOST GATE CLOSED
**Research:** Research 123
**Scope:** Close the single unresolved fresh-host G1 read left by Validation 161 by preserving one separately authorized targeted invocation of `github.list_installed_accounts` after the original no-retry qualification failed at connector transport.

## 1. Starting boundary

Validation 161 / Checkpoint 404 preserved a seven-action G1 fresh-host qualification in which:

```text
all seven exact actions projected             PASS
all seven host-visible schemas bounded        PASS
six live read-only calls succeeded            PASS
github.list_installed_accounts                mcp_network_error / network_error / Connection failed.
retry inside original qualification           none
post-failure local action discriminator        PASS
protected authorization                       healthy
```

The remaining host gate was therefore exactly one read-only action.

## 2. Targeted host requalification

The same action remained projected in the disposable ChatGPT host:

```text
github.list_installed_accounts
```

A new, separately authorized targeted invocation was made exactly once with no input. It succeeded.

Returned bounded result:

```text
schemaVersion                    codexless.github-readonly.v1
account count                     1
shakaarlatief present as User     true
credential secret appeared        false
GitHub mutation occurred          false
```

No installation ID, repository inventory, unrelated account, token, Authorization header or credential-store payload was reproduced.

Final marker supplied by the owner:

```text
GITHUB_G1_INSTALLED_ACCOUNTS_HOST_RECHECK=PASS
```

## 3. Combined G1 host disposition

The seven-action host gate is now closed by composition of the preserved evidence:

```text
Validation 161
    host projection/bounded schemas        7 / 7 PASS
    initial live reads                     6 / 7 PASS
    one connector transport failure        preserved, no retry

Validation 162
    targeted unresolved host read          PASS

Combined G1 fresh-host live coverage       7 / 7 PASS
```

The original network failure is not erased or rewritten. It remains evidence of a transient/host-transport failure class. Validation 162 closes only the unresolved action gate by proving the same already-projected read succeeds on a later separately authorized attempt.

## 4. Safety boundary

No GitHub mutation occurred in either the original seven-call qualification or this targeted recheck. No access token, refresh token, device code, client secret, Authorization header or credential-store payload appeared. No Plugin rescan, Runtime Bridge restart, authorization refresh or authorization mutation was required for the successful recheck.

The known independent gaps remain unchanged:

```text
github.list_installations(manageable_only=true)             not qualified
github.list_repositories(include_search_index_status=true)  not qualified
Enterprise-host repository_url                              not qualified
hidden native output schemas                                unresolved
exact native-wrapper parity                                 0 / 89
```

## 5. Continuation

Research 123 may now leave G1 and begin G2 read-only repository fetch/search/branch/commit/file/blob/compare implementation. The intended G2 repository-git read set, excluding already-closed G1 and later issue/PR/Actions domains, is:

```text
github.compare_commits
github.fetch
github.fetch_blob
github.fetch_commit
github.fetch_file
github.search
github.search_branches
github.search_commits
github.search_installed_repositories_streaming
github.search_installed_repositories_v2
github.search_repositories
```

The exact native input contracts for those actions are already preserved by the Research 123 schema-capture artifacts. Output envelopes remain `any` and must not be invented as native parity.

```text
VALIDATION162=PASS
GITHUB_G1_INSTALLED_ACCOUNTS_HOST_RECHECK=PASS
G1_FRESH_HOST_PROJECTION=PASS_7_OF_7
G1_FRESH_HOST_LIVE_COVERAGE=PASS_7_OF_7
ORIGINAL_TRANSPORT_FAILURE_PRESERVED=true
SECRETS_EXPOSED=false
GITHUB_MUTATION_OCCURRED=false
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
NEXT=G2_FETCH_SEARCH_BRANCH_COMMIT_FILE_BLOB_COMPARE_READONLY_IMPLEMENTATION
```
