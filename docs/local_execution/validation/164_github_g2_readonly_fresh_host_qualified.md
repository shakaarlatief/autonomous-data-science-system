# Validation 164: GitHub G2 Read-Only Fresh-Host Qualified

**Date:** 2026-09-09
**Status:** PASS / ELEVEN-ACTION G2 FRESH-HOST GATE CLOSED / ALL REMAINING READ-ONLY NEXT
**Research:** Research 123
**Scope:** Preserve fresh-host projection, bounded schema inspection and exactly-once live read-only qualification of the eleven preview.31 G2 GitHub actions.

## 1. Starting boundary

Validation 163 / Checkpoint 406 had already established live Runtime Bridge preview.31 with 86 public tools, 22 GitHub read-only actions, zero postactivation source mismatches and healthy protected GitHub authorization. The only remaining G2 gate was fresh ChatGPT host projection plus live read use.

## 2. Fresh-host projection and schema gate

The owner supplied the completed disposable-chat qualification with final marker:

```text
GITHUB_G2_READONLY_FRESH_HOST=PASS
```

All eleven exact G2 actions projected in the fresh host:

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

All eleven host-visible schemas were judged suitably bounded for the intended read-only GitHub surface. None exposed caller-selected GitHub credentials, access/refresh tokens, client secrets, Authorization headers, arbitrary HTTP methods or headers, arbitrary GraphQL documents, permission profiles or non-GitHub transport authority.

`github.fetch` is the only generic URL-shaped input. Its projected/runtime contract remains GET-only and restricted to allowlisted GitHub repository resource URL families.

## 3. Repository-first authority reconstruction

The disposable qualification first reconstructed `docs/CONTINUITY.md` from exact public commit:

```text
d7bd603e4e2abe1b91aea45523ef6e26dd1be3b8
```

That is the public `Activate G2 GitHub read-only preview` boundary from Checkpoint 406. A separately discovered September 8 GitHub qualification branch was divergent from that commit and was not treated as current project-development authority. No project-development state was changed in the disposable chat.

## 4. Live read-only qualification

All eleven actions were invoked exactly once and all eleven returned successful application results. No retry occurred.

`github.fetch_blob` used blob SHA:

```text
7c364b2ca8f1efa8ad575e0b3e3a50b7dd60375b
```

which was obtained from the preceding canonical `docs/CONTINUITY.md` read rather than guessed.

The installed-repository streaming search explicitly disabled search-index enrichment, and installed-repository v2 used `include_search_index_status=false`, preserving the known fail-closed native-enrichment boundary.

The live result summary is:

```text
github.compare_commits                         PASS
github.fetch                                   PASS
github.fetch_blob                              PASS
github.fetch_commit                            PASS
github.fetch_file                              PASS
github.search                                  PASS
github.search_branches                         PASS
github.search_commits                          PASS
github.search_installed_repositories_streaming PASS
github.search_installed_repositories_v2        PASS
github.search_repositories                     PASS
```

`github.search` returned a valid successful response with zero matches and `incompleteResults=true`; it was not retried. `github.search_commits` likewise completed successfully with zero matches. These are valid bounded application responses, not tool or transport failures.

Unrelated installed/private repository names were omitted from the preserved result.

## 5. Secret and mutation boundary

No credential or secret value appeared. Public historical source material returned through commit comparison contained ordinary credential-related identifiers such as variable/header names, but no token, credential or secret value was exposed.

No GitHub mutation action was invoked and no project-development mutation occurred in the disposable qualification.

## 6. Combined read-only capability disposition

G1 and G2 are now both fresh-host-qualified:

```text
G1 public read-only tools                 11
G1 fresh-host live coverage               11 / 11 PASS
G2 public read-only tools                 11
G2 fresh-host live coverage               11 / 11 PASS
combined live github.* read-only tools    22
combined fresh-host-qualified tools       22
```

The native GitHub connector inventory contains 48 read actions total. Therefore 26 native read actions remain unimplemented. Because the GitHub authority, protected authorization, installation scope, MCP projection, release lifecycle and two representative read-only families are now repeatedly qualified, Research 123 may safely increase implementation batch size.

The next implementation phase should target all 26 remaining read-only actions in one larger read-only release family, while still preserving domain-specific tests and fail-closed treatment of hidden native semantics. Mutation actions remain a separate later risk boundary.

Exact native-wrapper parity remains conservatively `0 / 89` because hidden native output envelopes and unresolved option semantics are still not inferred.

```text
VALIDATION164=PASS
GITHUB_G2_READONLY_FRESH_HOST=PASS
G2_FRESH_HOST_PROJECTION=PASS_11_OF_11
G2_FRESH_HOST_SCHEMA_BOUNDEDNESS=PASS_11_OF_11
G2_FRESH_HOST_LIVE_READS=PASS_11_OF_11
G1_PLUS_G2_FRESH_HOST_QUALIFIED=22
NATIVE_READ_ACTIONS_TOTAL=48
NATIVE_READ_ACTIONS_REMAINING=26
SECRETS_EXPOSED=false
GITHUB_MUTATION_OCCURRED=false
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
NEXT=ALL_REMAINING_GITHUB_READONLY_IMPLEMENTATION
```
