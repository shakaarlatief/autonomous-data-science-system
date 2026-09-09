# GitHub Connector 89-Action Parity Matrix

**Date:** 2026-09-09
**Status:** ACTIVE RESEARCH 123 / ALL 48 READS LIVE / FINAL 26-ACTION FRESH-HOST GATE NEXT
**Authority:** Specialized Research 123 parity/design artifact. Validation 128 remains authoritative for the two earlier 89-action qualification results and conservative negative-capability interpretation; Validation 130 owns the fresh exact-name correction; Validation 131 owns Batch 1; Validation 132 Batch 2; Validation 133 Batch 3; Validation 134 Batch 4; Validation 135 Batch 5; Validation 136 Batch 6; Validation 137 owns final reconciliation and gap disposition; Validation 157 owns the first live four-tool read-only Runtime Bridge foundation and its deliberately partial parity classification; Validation 159 owns the refreshed fresh-host four-action projection and live-read PASS; Validation 160 owns preview.30 publication/activation plus local-live qualification of the seven additional G1 reads; Validation 161 owns their fresh-host 7/7 projection, 6/7 live-read FAIL and post-failure local transport discriminator; Validation 162 owns the targeted installed-accounts host recheck that closes combined G1 host coverage at 7/7; Validation 163 owns preview.31 G2 implementation, publication, activation and same-chat stale-projection evidence; Validation 164 owns fresh-host G2 11/11 schema and live-read qualification; Validation 165 owns implementation and live activation of the final 26 read actions plus the preview.33 GitHub download resource-link correction and local-live qualification.
**Machine-readable inventory:** `docs/research/github_connector_89_action_inventory.json`
**Machine-readable native schema capture:** `docs/research/github_connector_native_schema_capture.json`

## Purpose and provenance

Research 123 requires every observed native GitHub connector action to be mapped before implementation begins.

Validation 128 preserved exactly 89 observed actions and zero newly discovered actions in the negative-capability challenge, but did not reproduce all 89 names and schemas. Checkpoint 372 reconstructed the exact names from prior qualification transcripts. The later fresh GitHub-only schema-capture conversation again projected exactly 89 actions with zero action invocations and exposed one Checkpoint 372 reconstruction defect:

```text
fresh projection only        GitHub.download_user_content
Checkpoint 372 inventory only GitHub.add_issue_comment
```

`GitHub.add_comment_to_issue` is present in the fresh projection; `GitHub.add_issue_comment` is not. Validation 130 / Checkpoint 373 classify this as `RECONSTRUCTION_DEFECT_NOT_CONNECTOR_DRIFT` and preserve the exact fresh projected order in the machine-readable inventory.

The complete native schemas, enum constraints and per-action pagination behavior remain under discovery-only capture in that same fixed fresh GitHub conversation. Implementation contracts remain blocked until the schema capture is reconciled.

The frozen baseline is:

```text
repository / installation / branch / commit / file / raw Git   29
issues                                                           17
content download                                                   1
Actions / CI                                                       9
pull requests / reviews                                           32
repository permission                                              1
TOTAL                                                              89
```

`python scripts/check_github_connector_parity_inventory.py` protects count, uniqueness, order, domain totals and native-to-target action-name correspondence.

## Mapping conclusion

Codexless Runtime Bridge now contains a live GitHub REST/GraphQL authority layer and all forty-eight captured native read action names as public `github.*` read-only tools. Validation 157/159 close the first four foundation reads, Validation 160-162 close the remaining seven G1 reads, and Validation 163/164 close the eleven G2 repository fetch/search/branch/commit/file/blob/compare reads in both runtime and fresh-host use. Validation 165 then implements the final twenty-six issue, PR/review, Actions/CI and content-download reads in one larger release family, activates preview.33 at 112 total tools / 48 GitHub reads, and locally live-qualifies twenty-five of those twenty-six new actions against canonical public fixtures. `github.download_user_content` remains positive-live-fixture-gated because no suitable authorized private-user-images URL exists in the canonical public evidence; its strict host allowlist and positive synthetic resource transfer are regression-qualified. Workflow artifact download is live-qualified as compact MCP `resource_link` plus separate `resources/read`, with no ZIP bytes/base64 embedded in the tool result. Fresh-host coverage is now 22/48 and the final 26-action host gate is next. Exact native parity remains `0 / 89`, because the project still refuses to infer hidden native output envelopes or unresolved option semantics. `github.list_installations(manageable_only=true)` remains unqualified; search-index enrichment remains fail-closed where the native enrichment contract is hidden; Enterprise-host repository URL routing remains separately unqualified; and conflicting hidden alias precedence is not guessed. The inventory therefore continues to use `currentRuntimeBridgeParity=MISSING` to mean that no fully qualified exact native-parity row is closed yet, not that no corresponding Runtime Bridge implementation exists.

Existing Runtime Bridge mechanisms remain reusable:

```text
workspace / authority discipline
server-owned host-process execution
semantic Git exact-HEAD, stale-state, non-force and postflight patterns
mutation uncertainty and no-blind-retry rules
model-free bounded reads
resource-link / file handoff
optimistic revision/hash state updates
repository-specific integrity policies
```

The local Git actions are not remote GitHub parity because they operate on registered local clones and do not provide installation discovery, GitHub repository search, REST/GraphQL objects, issues, PR review threads or Actions APIs.

## Family-level implementation map

| Family | Count | Current exact parity | Principal reuse | Required GitHub implementation |
|---|---:|---|---|---|
| Repository / installation / branch / commit / file / raw Git | 29 | 0 | bounded reads + semantic Git safety | GitHub App user auth + REST |
| Issues | 17 | 0 | mutation uncertainty + exact IDs | REST Issues / labels / assignees / reactions / lock |
| Content download | 1 | 0 | resource/file handoff | Pending exact native schema capture for `download_user_content` |
| Actions / CI | 9 | 0 | bounded reads + resource handoff | REST Actions + artifact handoff |
| Pull requests / reviews | 32 | 0 | mutation safety + exact object identity | REST + GraphQL for PR/review-thread state |
| Repository permission | 1 | 0 | authority/error patterns | REST collaborator permission |

The exact 89 row mappings, target `github.*` names, read/write class, reuse basis and target transport are canonical in `github_connector_89_action_inventory.json`.

## Authentication architecture

### Dedicated GitHub App with user access token

A normal Git transport credential or ordinary GitHub CLI OAuth token is insufficient for full parity because the observed surface contains installation-aware actions such as `list_installations` and `list_repositories_by_installation`. GitHub's official REST documentation states that the user-installation endpoints use a GitHub App user access token.

Selected architecture:

```text
ChatGPT
    -> Codexless Runtime Bridge github.* semantic action
        -> GitHubAuthority
            -> dedicated Codexless Runtime Bridge GitHub App
            -> GitHub device-flow user authorization
            -> short-lived GitHub App user access token
            -> server-owned refresh-token lifecycle
        -> GitHubApiTransport
            -> REST
            -> GraphQL where required
```

Official evidence:

```text
https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app
https://docs.github.com/en/rest/apps/installations
```

GitHub recommends device flow for headless/CLI-style applications. Current documentation states that, when expiration is enabled, user access tokens last 8 hours and refresh tokens last 6 months. A token obtained through device flow can be refreshed without requiring the app client secret. This fits a local Runtime Bridge with a non-secret client ID and no caller-visible token.

### Secret boundary

No GitHub access token, refresh token, client secret, private key or credential may appear in MCP inputs/outputs, public Git, either private Git repository, ordinary logs or error details.

Introduce a server-owned `GitHubSecretStore`. The Windows implementation must use an OS-protected mechanism; DPAPI / Windows Credential Manager are the preferred implementation family and require focused qualification. Plaintext JSON is rejected.

### Repository scope

Do not impose a second artificial repository whitelist merely to make the local implementation narrower. Default parity scope comes from the GitHub App installation itself:

```text
GitHub App installation selection
    -> repositories/accounts granted to the app
GitHub App user token
    -> intersection of app permissions and authenticated-user permissions
Runtime Bridge
    -> semantic action contract + mutation guards
```

Bind expected GitHub hostname, App client ID and authenticated login in server-owned authority state so account drift fails visibly.

## API transport architecture

Production uses an internal Node GitHub API client. Do not expose `gh api`, curl, arbitrary HTTP, arbitrary GraphQL, arbitrary headers or caller-selected endpoints.

The current machine has GitHub CLI 2.97.0, but `gh auth status` reports its API token is invalid. Existing semantic Git pushes still succeed through a different Git credential path. This proves Git transport authentication and GitHub API authentication are distinct contracts.

The internal transport owns hostname, method, endpoint template, headers, API version, authentication, pagination and response parsing. Current GitHub REST docs use API version `2026-03-10`; version selection remains server-owned and should be capability-probed.

## REST and GraphQL disposition

Most actions map to REST. GitHub's Git Database API directly supports blobs, trees, commits and references:

`https://docs.github.com/en/rest/git`

GraphQL is required or strongly preferred for PR state represented directly in the Pull Request GraphQL schema, including:

```text
convertPullRequestToDraft
enablePullRequestAutoMerge
markPullRequestReadyForReview
review-thread listing
resolveReviewThread
unresolveReviewThread
```

Official source: `https://docs.github.com/en/graphql/reference/pulls`

One semantic action may use both APIs internally when needed to preserve native information quality. The caller still sees one typed action.

## Pagination, search and errors

Pagination is action-specific, not one global toggle. GitHub REST uses `Link` headers and commonly supports `per_page`:

`https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api`

Each action freezes one of:

```text
ALL_PAGES
FIRST_PAGE_ONLY
BOUNDED_LIMIT
CURSOR_OR_CONTINUATION
NON_PAGINATED
```

The exact mode/limits come from the fresh native schema capture. Search results preserve source metadata such as `total_count` and `incomplete_results` where GitHub returns them.

Errors must preserve Runtime Bridge code, HTTP status, GitHub message, `documentation_url`, `X-GitHub-Request-Id`, rate-limit headers, GraphQL `errors[]`, and mutation-dispatch certainty when available.

Required categories:

```text
GITHUB_AUTH_UNAVAILABLE
GITHUB_AUTH_IDENTITY_MISMATCH
GITHUB_PERMISSION_DENIED
GITHUB_NOT_FOUND
GITHUB_VALIDATION_FAILED
GITHUB_CONFLICT
GITHUB_STALE_OBJECT
GITHUB_RATE_LIMITED
GITHUB_RESPONSE_INVALID
GITHUB_GRAPHQL_ERROR
GITHUB_RESULT_UNCERTAIN
GITHUB_API_ERROR
```

GitHub documents that insufficient permissions may surface as `403` or `404`; preserve actual HTTP evidence rather than claiming the bridge can always distinguish hidden from nonexistent resources. A valid empty collection remains success.

## Mutation contracts

### Files and raw Git

```text
create_file / update_file / delete_file
    -> Contents REST API
    -> expected source SHA where native contract requires it
    -> stale SHA fails visibly

create_blob / create_tree / create_commit
    -> Git Database REST API

create_branch / update_ref
    -> Git reference REST API
    -> no hidden force retry
```

The native qualification explicitly exercised `create_blob -> create_tree -> create_commit -> update_ref(force=false)`.

### Pull requests / reviews

PR/review mutations preserve exact PR, review, comment and thread identities. `merge_pull_request` preserves `merge | squash | rebase` plus optional `expected_head_sha`; stale expected head fails instead of silently merging a newer head. Review-thread resolve/unresolve uses the exact thread object.

### Issues

Comments, assignees, labels, reactions and lock state preserve exact GitHub IDs and structured validation errors.

### Actions

The parity baseline includes failed-run rerun and individual-job rerun, not whole-run rerun. GitHub's workflow-run REST docs require `Actions` repository permission `write` for reruns:

`https://docs.github.com/en/rest/actions/workflow-runs`

An uncertain rerun result is never automatically replayed.

### Artifacts

`github.download_workflow_artifact` reuses Runtime Bridge resource/file handoff; ZIP bytes/base64 must not be embedded in a giant text result.

## GitHub App permission policy

The App must receive every permission required by the observed 89-action set, but no unrelated administration merely for convenience. The exact permission manifest must be derived from official endpoint docs before app registration and preserved as Research 123 evidence.

Already verified examples:

```text
Metadata read    get repository / collaborator permission
Actions write    failed-run and individual-job rerun
```

Do not request Checks, Actions secrets/environments, webhooks, repository administration or branch-protection mutation just because GitHub supports them. Those families were not observed in the parity baseline. This is exact authority matching, not feature weakening.

## Public tool-surface strategy

Target full parity with one explicit Runtime Bridge action per observed native action:

```text
GitHub.get_user_login                   -> github.get_user_login
...
GitHub.get_repo_collaborator_permission -> github.get_repo_collaborator_permission
```

The Runtime Bridge currently exposes 63 tools. Full parity would add 89 and reach 152. The native GitHub-only connector already demonstrated 89-action projection, but a 152-tool developer-MCP surface is unqualified and AB-008 records projection/schema issues.

Do not weaken in advance. Qualify scaling empirically:

```text
release coherent slices
-> fresh-chat discovery after each expansion
-> verify count + schema fidelity
-> scale toward all 89
-> consider grouped fallback only if the host actually fails at combined scale
```

## Implementation slices

After native schema capture:

```text
G0  GitHub App / device-flow auth / secret store / API kernel
    no GitHub mutation
G1  identity + installations + repository discovery + permission lookup
    read-only
G2  fetch/search + branches/commits/files/blobs/compare
    read-only
G3  direct files + raw Git object/ref primitives
    disposable branch
G4  issues
    disposable issue fixture
G5  PRs / reviews / threads / reactions / merge guards
    disposable branch + draft PR
G6  Actions / logs / artifacts / exposed reruns
    dedicated safe workflow fixture
G7  complete 89-action fresh-chat projection + parity regression
```

Every slice must retain existing local Runtime Bridge capabilities.

## Mandatory native-schema gate

The exact fresh 89-action names/order are now durable after Validation 130 / Checkpoint 373, but complete native schemas were not preserved in Validation 128. The same fixed fresh GitHub-only conversation must now capture schemas for all 89 before implementation begins:

```text
exact action name
title / description
complete input schema
required / optional fields
enums
validation constraints
pagination / cursor / limit behavior
read vs mutation class
visible result/error contract details
```

That qualification is discovery-only and performs no GitHub mutation. The batching procedure is in `docs/research/GITHUB_CONNECTOR_SCHEMA_CAPTURE.md`.

Validation 131 / Checkpoint 374 preserve Batch 1 as `15 / 89`. All fifteen actions expose object input contracts, but all fifteen project return type `any`, no separate title metadata, and no machine-readable structured error schema. Several cross-field rules are descriptive rather than structurally encoded. This is now a first-class parity constraint: faithful input-schema reproduction can proceed from discovery, while exact normalized output-shape parity may require additional live-result evidence after the six discovery batches are reconciled.

Validation 132 / Checkpoint 375 advance the same fixed projection to `30 / 89`. Batch 2 confirms first-page-only versus internally-all-pages pagination asymmetry, genericizes `create_tree.tree_elements` to `{ [key: string]: any }[]`, resolves `download_user_content` to a narrowly allowlisted private-user-image URL download, and confirms workflow-artifact reusable file-reference semantics. `fetch_issue.repository_url` also exposes GitHub Enterprise Server / GHE.com selector examples, creating an explicit host-scope follow-up for final architecture reconciliation.

Validation 133 / Checkpoint 376 advance the fixed projection to `45 / 89`. Batch 3 provides the first concrete valid-empty versus 404 contract (`fetch_pr_file_patch`), including an explicit no-retry-other-paths rule after the documented 404. It further distinguishes all-pages PR patching, first-page-only workflow artifacts, latest-attempt/first-page workflow jobs, and explicit page/per_page reaction pagination. `get_pr_diff` exposes `diff | patch` with default `diff`; `get_profile` is zero-argument; `get_repo` repeats the Enterprise-aware selector XOR; collaborator-permission result values remain unprojected.

Validation 134 / Checkpoint 377 advance the fixed projection to `60 / 89`. Batch 4 captures installation/account discovery directly, confirms internal-final-limit, all-pages, until-limit-or-exhaustion and zero-based-offset pagination variants, and preserves review-thread/review/org-list pagination as unspecified. Four actions are true zero-argument calls. `lock_issue_conversation.lock_reason` is a genuine four-value enum, while recent-PR state and repository affiliation examples remain unrestricted strings.

Validation 135 / Checkpoint 378 advance the fixed projection to `75 / 89`. Batch 5 captures the exact PR merge-method enum plus `expected_head_sha` optimistic concurrency, reviewer-array ambiguity, top-level-only inline review replies, GitHub Actions write permission for both exposed rerun mutations, valid-empty empty-query search semantics, and an opaque cursor contract for branch search. Thirteen of the fifteen Batch 5 actions are mutations, which informs later fixture/risk qualification.

Validation 136 / Checkpoint 379 complete the six-batch discovery capture at `89 / 89`. Batch 6 adds qualifier-only commit-search rejection plus the narrow recent-commit empty-query exception, opaque next-token and 1-based-page repository search variants, sequential same-path file-write requirements with named `content_sha`, issue replacement-set semantics plus a milestone-clear gap, and branch-oriented `update_ref(force=false)` with no tag/ref namespace selector. The capture is complete but intentionally remains pending final same-conversation reconciliation before implementation contracts are frozen.

Validation 139 / Checkpoint 382 now preserve the first private G0 implementation at `3c5f3688ec578c0817953890dc69ecb7ce679153`: protected-token-store abstraction, device flow, single-flight refresh, fixed github.com REST transport, server-owned GraphQL registry, semantic errors and installation-derived authority. The focused suite passes 12/12 with no live GitHub/OS credential activity. The next gate is the concrete Windows keyring import and synthetic set/get/delete qualification before main-runtime integration.

Validation 140 / Checkpoint 383 close that Windows protected-store gate. Exact `@napi-rs/keyring@2.0.0` import/API compatibility passed on Windows x64 and one normal-user-session synthetic Credential Manager set/read-match/delete/verified-absence lifecycle passed. No GitHub token or GitHub network call was involved, the synthetic secret was not printed, and staging-only dependency/cache material was removed afterward. Main-runtime G0 integration is now next.
Validation 141 / Checkpoint 384 qualify the first main-runtime G0 source integration at private head `6ce0da8818a455731acc10ba231ef9f52c0c8206`. The lazy internal kernel preserves the 63-tool public surface and zero `github.*` actions, with 9/9 syntax and 4/4 integration tests passing. Runtime Release v1 cannot provision the required native keyring dependency because its bounded targets exclude package manifests and `node_modules`; deterministic dependency provisioning/rollback is now the next gate.
Validation 142 / Checkpoint 385 qualify immutable runtime dependency generations at private head `5b63371536fa2f09bb122ed09470ec5204f18d9b`. Real keyring generation preparation/loading and real Runtime Release v2 preparation both resolve the exact 10-file / 1,971,364-byte tree `abe67a212121747d57d1bb78cd7880e7e7bb29e1f44e2ba8ec5010e5f1e50858`. Windows `EPERM` on same-process deletion after native loading establishes immutable generation retention; release/rollback/restart/recovery switch exact worker bindings instead of mutating live `node_modules`. The combined suite passes 22/22 with zero public `github.*` actions.
Validation 143 / Checkpoint 386 live-qualify the source-only dependency-aware runtime bootstrap, then Validation 144 / Checkpoint 387 activate the exact `github-keyring-win32-x64` generation under Runtime Release v2. The replacement runtime reports one dependency, zero source mismatches, 63 public tools and zero public `github.*` actions. G0 storage/deployment is therefore live-capable; an explicit authorization-control support surface is the next gate before read-only parity actions.
Validation 145 / Checkpoint 388 then live-qualify one separate `codex.github_authorization` support tool at 64 public tools while exact `github.*` parity remains 0/89. The final fix2 release passes, direct local MCP discovery exposes the strict metadata/begin/status/poll/cancel/clear schema, and live metadata confirms no configured client ID or stored authorization. The current persistent ChatGPT projection remains stale, so fresh-chat support-tool schema/metadata qualification is next before any device flow or parity action publication.
Validation 146 / Checkpoint 389 capture the first fresh-host result: preview.24 exposes only a generic map for the local strict top-level authorization union and the one metadata attempt is host-safety-blocked before any Runtime Bridge payload. Preview.25 replaces the union with the previously qualified flat strict object pattern, passes all 16 release regressions, activates successfully, and serializes the bounded fields locally. Fresh-chat flat-schema + metadata requalification is now the only support-surface gate before client-ID/device-flow work.
Validation 147 / Checkpoint 390 close that discriminator: preview.25 projects as a structured flat bounded object in a fresh host, the exactly one metadata call succeeds and returns the expected unconfigured/unauthorized state, and no authorization mutation occurs. The current ChatGPT Plugin display name `Codexless Runtime Bridge` is also directly qualified from owner-supplied UI evidence. Authorization support is therefore host-ready; the exact GitHub App permission manifest becomes the immediate pre-registration gate.
Validation 148 / Checkpoint 391 then map all 89 actions to current official GitHub permission evidence and freeze seven repository permissions: Actions(write), Contents(write), Issues(write), Metadata(read), Pull requests(write), Commit statuses(read), and Workflows(write). Organization/account/enterprise permissions and webhooks remain absent; Administration/Checks/Members are explicitly excluded. GitHub does not publish an exact GraphQL App permission table, so eight PR/review GraphQL operations retain an empirical sufficiency probe under already-required Pull requests(write), with no speculative widening.
Validation 149 / Checkpoint 392 freeze the non-secret GitHub App registration around that manifest: personal owner `shakaarlatief`, canonical App name, Any account/public installability, device flow and expiring tokens enabled, install-time OAuth off, no callback/setup URL, webhooks disabled, no private-key bootstrap, and first installation limited to the canonical public ADS repository. The project is now at the owner-performed GitHub UI creation/install boundary.
Validation 150-152 / Checkpoints 393-395 then expand the product goal beyond parity before App creation. The complete live registration surface contains 118 permission rows; the frozen extended profile selects 74 (34 repository, 30 organization, 10 account, 0 enterprise), explicitly includes Repository Administration(write), and preserves connector parity as a subset. Fifty-six permission rows are reproducibly prefilled from independently documented parameter names; eighteen live/newer rows remain manual rather than guessed. Secret-value families and Webhooks stay off, while personal installation scope becomes All repositories.
Validation 153-156 / Checkpoints 396-399 then close the owner UI, App registration, installation, Client-ID correction and device-flow authorization sequence. The dedicated App is installed on the personal account with All repositories, the local bootstrap PEM has been deleted, no Client secret exists, and protected GitHub App user authorization is current and non-expired.
Validation 157 / Checkpoint 400 publish and locally live-qualify the first four `github.*` read-only foundation tools on preview.28. The fixed GraphQL viewer query resolves the authenticated login, REST installation enumeration returns one All-repositories installation, and repository enumeration confirms the canonical ADS repository is in scope. Exact parity deliberately remains `0 / 89` because `list_installations(manageable_only=true)` is still fail-closed pending native managed-account semantics and the four new names still require fresh ChatGPT host projection qualification.

Validation 137 / Checkpoint 380 preserve the final reconciliation. All 89 host-visible request contracts were captured with zero missing actions, but all 89 machine-readable output schemas and all 89 structured error schemas remain unavailable, and `create_tree` retains a genericized nested input. The result is `GITHUB_89_SCHEMA_CAPTURE=INCOMPLETE` for exact native-wrapper wire parity while practical action/request mapping is complete. G0 auth/transport work is opened because these action-specific gaps do not constrain the independent GitHub authority/API kernel; action publication remains evidence-gated.

## Design disposition

```text
EXACT_ACTION_NAMES_MAPPED=89/89
FRESH_PROJECTED_ORDER_CONFIRMED=89/89
CHECKPOINT372_EXACT_NAME_RECONSTRUCTION=CORRECTED
EXACT_REMOTE_RUNTIME_BRIDGE_PARITY_NOW=0/89
PARITY_ACTIONS_MISSING=89
LIVE_GITHUB_READONLY_TOOLS=48
FRESH_HOST_QUALIFIED_GITHUB_TOOLS=22
NEW_G1_LOCAL_LIVE_TOOLS=7
LIVE_RUNTIME_VERSION=0.1.1-preview.33-github-all-readonly-resource-links
LIVE_MCP_TOOL_COUNT=112
LOCAL_REUSE_AVAILABLE=YES
AUTH_ARCHITECTURE=GITHUB_APP_USER_TOKEN_DEVICE_FLOW
GITHUB_USER_AUTHORIZED=true
STORED_AUTHORIZATION=true
REPOSITORY_SCOPE=GITHUB_APP_INSTALLATION
PERSONAL_INSTALLATION_SCOPE=ALL_REPOSITORIES
PRODUCTION_TRANSPORT=INTERNAL_REST_GRAPHQL_CLIENT
CALLER_SUPPLIED_CREDENTIALS=FORBIDDEN
CALLER_SUPPLIED_ARBITRARY_HTTP=FORBIDDEN
TARGET_PUBLIC_SHAPE=EXPLICIT_GITHUB_ACTIONS
TOOL_COUNT_SCALING=EMPIRICAL_QUALIFICATION_REQUIRED
NATIVE_HOST_VISIBLE_SCHEMA_CAPTURE=89_OF_89_COMPLETE
EXACT_NATIVE_WIRE_CONTRACT=INCOMPLETE
G0_AUTH_TRANSPORT_KERNEL=LIVE
GRAPHQL_VIEWER_QUERY=PASS
KNOWN_PARTIAL_PARITY_GAP=github.list_installations.manageable_only_true
KNOWN_PARTIAL_PARITY_GAP_2=github.list_repositories.include_search_index_status_true
ENTERPRISE_REPOSITORY_URL=NOT_QUALIFIED
FRESH_HOST_FOUNDATION_PROJECTION=PASS_4_OF_4
FRESH_HOST_FOUNDATION_LIVE_READS=PASS_4_OF_4
G1_LOCAL_MCP_PROJECTION=PASS_7_OF_7
G1_LOCAL_LIVE_READS=PASS_7_OF_7
G1_FRESH_HOST_PROJECTION=PASS_7_OF_7
G1_FRESH_HOST_LIVE_READS=PASS_6_OF_7
G1_FRESH_HOST_INITIAL=FAIL_6_OF_7
G1_FAILED_HOST_ACTION=github.list_installed_accounts
G1_FAILED_HOST_ERROR=mcp_network_error_network_error_connection_failed
G1_POST_FAILURE_LOCAL_ACTION=PASS
G1_TARGETED_HOST_RECHECK=PASS
G1_FRESH_HOST_COMBINED_LIVE_COVERAGE=PASS_7_OF_7
G1_TOTAL_FRESH_HOST_QUALIFIED_TOOLS=11
G2_RUNTIME_TOOLS=11
G2_FRESH_HOST_PROJECTION=PASS_11_OF_11
G2_FRESH_HOST_LIVE_READS=PASS_11_OF_11
SAME_CHAT_G2_PROJECTION=STALE
NATIVE_READ_ACTIONS_TOTAL=48
NATIVE_READ_ACTIONS_IMPLEMENTED=48
NATIVE_READ_ACTIONS_REMAINING=0
FRESH_HOST_QUALIFIED_GITHUB_TOOLS=22
FRESH_HOST_PENDING_READS=26
FINAL_READ_BATCH_LOCAL_LIVE_SUCCESS=25_OF_26
DOWNLOAD_USER_CONTENT_POSITIVE_LIVE=FIXTURE_GATED
DOWNLOAD_WORKFLOW_ARTIFACT_RESOURCE_LINK=PASS
SAME_CHAT_FINAL_READ_PROJECTION=STALE
NATIVE_WRITE_ACTIONS_REMAINING=41
HOST_MACHINE_OUTPUT_SCHEMA=NOT_PROJECTED_IN_BATCH1
HOST_STRUCTURED_ERROR_SCHEMA=NOT_PROJECTED_IN_BATCH1
NEXT=FRESH_CHAT_ALL_REMAINING_READONLY_SCHEMA_AND_LIVE_QUALIFICATION
```
