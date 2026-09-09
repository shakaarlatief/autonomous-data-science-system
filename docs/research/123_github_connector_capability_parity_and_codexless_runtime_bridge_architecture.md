# Research 123: GitHub Connector Capability Parity and Codexless Runtime Bridge Architecture

**Date:** 2026-09-08
**Status:** ACTIVE / OWNER-DIRECTED INSERTION BEFORE PLANNED NEXT STAGE
**Scope:** Establish the exact currently observed GitHub-connected development capability surface available to ChatGPT, define practical parity requirements for the custom local connector, and formalize the connector terminology needed to keep the overall Autonomous Data Science System distinct from its transport/runtime bridge.
**Authority:** Active Level-2 architecture research. It may define implementation and qualification work for GitHub capability parity, but it does not by itself widen GitHub, local-runtime, workspace, credential, or repository authority.
**Declared references:** `research:113`, `research:116`, `checkpoint:370`, `path:docs/local_execution/validation/034_chatgpt_tool_projection_refresh_and_connector_coexistence_observations.md`, `path:docs/local_execution/validation/128_github_connector_capability_parity_baseline_and_coexistence_recheck.md`, `path:docs/local_execution/OPERATIONS.md`, `path:docs/OPEN_ARCHITECTURE_BACKLOG.md`

## 1. Owner-directed stage insertion

Research 113 was the formal active stage after Research 122 closed. During `chatgpt-19`, the project owner revisited a previously reproduced ChatGPT host limitation: the developer MCP and native GitHub connector do not reliably execute in the same conversation.

That side investigation produced a material architecture opportunity. The owner explicitly chose to complete GitHub capability parity before the separately planned next stage. Research 113 is therefore paused, not completed or rejected, while Research 123 is active.

Source Vault remains paused. The owner's separately planned stage remains intentionally deferred until this GitHub-parity stage closes.

## 2. Terminology correction

`ADS` and `Autonomous Data Science System` refer to the complete project/system. They should no longer be used as shorthand for the custom ChatGPT connector itself.

The canonical forward-looking connector name is:

```text
Codexless Runtime Bridge
```

The intended terminology is:

```text
Autonomous Data Science System (ADS)
    overall project/system

Codexless Runtime Bridge
    ChatGPT-facing custom developer-MCP connector surface

Codexless
    local service/runtime implementing the connector-side capabilities

managed tunnel
    secure transport between ChatGPT and the local runtime bridge

local runtime
    machine execution environment behind the bridge
```

Historical records that contain the exact earlier display name `ADS Codexless Local Bridge` remain valid historical evidence and are not rewritten merely for terminology cleanup. Validation 147 / Checkpoint 390 now qualify the current live ChatGPT Plugin display name as `Codexless Runtime Bridge` from direct owner-supplied UI evidence. This closes the Plugin display-name rename only; historical internal compatibility identifiers or tunnel/runtime identifiers are not rewritten merely to match the UI label.

## 3. Current coexistence problem remains reproduced

Validation 034 already preserved repeated fresh-chat failures when combining the developer MCP with the native GitHub connector. In `chatgpt-19`, the project owner rechecked the boundary from mobile web:

```text
Codexless developer MCP surface   projected and callable
codex.account_preflight           PASS / status=ok
native GitHub connector           not projected in the same conversation
```

This does not prove a permanent platform-wide impossibility. It does confirm that ADS must not currently require simultaneous native GitHub-connector execution and developer-MCP execution in one conversation.

## 4. Fresh GitHub capability qualification

Two fresh GitHub-only conversations were used to qualify the live connector surface without Browser, ADS, shell, Codex Agent, or another connector.

The first qualification discovered 89 GitHub actions and live-qualified a broad remote development workflow. Material observed capability includes:

```text
identity / installation / repository discovery
public and installation-authorized repository reads
branch listing/search and creation
commit search/history/exact lookup/compare
repository file and blob reads
file create/update/delete with remote commits
raw Git blob -> tree -> commit -> branch-ref advancement
pull-request creation and update
PR files / patches / full diff
PR comments, reviews and review threads
inline review replies / edits / resolve / unresolve
PR/review-comment reactions
reviewer request/remove actions
ready-for-review and draft transitions
PR label assignment
merge_pull_request exposed with merge/squash/rebase and expected_head_sha
issue create/read/search/update/comment/assignee/label/lock/unlock/close
workflow run/job/step/log inspection
workflow-run artifact listing and artifact-download action exposure
combined commit status
failed-run / individual-job rerun actions
```

A safe temporary qualification branch, draft PR #81, and issue #82 were used. The PR was closed unmerged, the issue was closed, and `main` was not modified. The temporary branch remained only because no branch-delete action was observed in that projection.

Merge authority was exposed but intentionally not re-executed because the qualification prohibited merging. Existing project experience already establishes that the GitHub-connected workflow can merge branches/PRs; the qualification result must therefore not be misread as a merge failure.

## 5. Negative-capability challenge

A second fresh intent-specific conversation challenged every material negative from the first inventory. It again projected the same 89 actions and no additional actions.

No equivalent route was observed for the following capability families:

```text
branch / ref deletion
tag mutation
release mutation
workflow_dispatch
repository_dispatch
workflow-run cancellation
whole-run rerun
workflow enable / disable / delete
Check Runs / Check Suites objects
GitHub Discussions
collaborator listing or administration beyond single-user permission lookup
repository label-definition CRUD
milestone CRUD
repository settings mutation
branch-protection or ruleset mutation
Actions secrets / variables / environments
webhooks
security-alert administration
repository lifecycle / administration
organization / team administration
deploy keys
GitHub Pages administration
Packages / container registry administration
Codespaces administration
```

The generic `fetch` primitive is an allowlisted GET-only GitHub facade. It can read additional approved repository resources, but it is not arbitrary REST/GraphQL mutation authority and cannot substitute for missing POST/PATCH/PUT/DELETE operations.

Negative results are deliberately classified as:

```text
NOT_OBSERVED_IN_THIS_PROJECTION
```

not as permanent connector-wide impossibilities. Tool projection, permissions, installation type, host behavior, and future connector versions can change.

## 6. Parity objective

The target is not merely an approximate GitHub reader and not merely a list of similarly named tools.

Practical parity requires Codexless Runtime Bridge to preserve the capability and information quality of the currently observed GitHub connector for equivalent tasks, including:

```text
complete observed action coverage
exact object identity and repository/ref/commit targeting
information fidelity without lossy summaries
public vs installation-authorized repository scope
repository permission enforcement
pagination / cursor / continuation semantics
all-page aggregation where the connector performs it
first-page-only behavior where that limitation is part of the observed contract
structured GitHub HTTP/state/validation failures
valid-empty vs not-found distinction
stale-SHA concurrency failures
direct file commits
raw Git object and ref primitives
deep PR/review/thread/comment/reaction workflows
issue lifecycle workflows
Actions run/job/step/log/artifact inspection
currently exposed rerun capabilities
merge authority and expected-head safeguards
```

Capabilities not observed in the current native connector are optional future supersets. They are not required to claim parity with the present observed surface.

## 7. Why parity inside the Runtime Bridge can be stronger overall

For an equivalent GitHub-only task, the goal is that work through Codexless Runtime Bridge is not lower quality than work through the native GitHub connector.

For the ADS project as a whole, the Runtime Bridge route can be more useful because one conversation can combine GitHub state with local evidence:

```text
GitHub repository / PR / issue / Actions state
    + local authorized repositories
    + local files and documents
    + Codex execution
    + real Windows/runtime behavior
    + tests
    + Browser where authorized
    + semantic Git
    + runtime maintenance
```

The architecture should therefore reproduce GitHub capability without sacrificing the local capabilities that motivated Codexless in the first place.

## 8. Design principles for the implementation

Parity does not require exposing a raw GitHub token, arbitrary HTTP client, arbitrary shell, or caller-selected credentials.

The preferred architecture remains semantic and capability-complete:

```text
ChatGPT
    -> Codexless Runtime Bridge GitHub capability layer
        -> server-owned GitHub authentication
        -> GitHub REST / GraphQL operations as required
```

The caller may receive broad GitHub development capability while the implementation still preserves explicit object semantics, repository scope, permission checks, mutation intent, structured errors, and credential non-disclosure.

Do not deliberately remove useful native-connector capability merely to make the surface narrower. `bounded` describes authority shape and safety, not an artificial reduction in practical power.

## 9. Research and implementation sequence

The stage should proceed in this order:

```text
1. preserve the 89-action qualification as the parity baseline;
2. map every observed action to existing Codexless capability, missing capability, or reusable Git primitive;
3. define authentication and repository-scope architecture;
4. define read/search/pagination/error contracts;
5. define mutation contracts for files, raw Git, PRs, reviews, issues and Actions;
6. implement behind the stable Runtime Bridge surface;
7. qualify read parity against the native GitHub evidence;
8. qualify safe remote mutation parity on disposable branches/issues/PRs;
9. qualify CI/log/artifact/rerun behavior;
10. verify that the native-connector coexistence problem no longer blocks the ADS development workflow;
11. close Research 123 only when practical parity is evidence-backed;
12. resume Research 113 or the owner's separately planned next stage according to the explicit owner decision at closure.
```

## 10. ChatGPT-20 parity mapping and architecture result

The first substantive Research 123 design pass is now preserved in:

```text
docs/research/GITHUB_CONNECTOR_PARITY_MATRIX.md
docs/research/github_connector_89_action_inventory.json
docs/research/GITHUB_CONNECTOR_SCHEMA_CAPTURE.md
scripts/check_github_connector_parity_inventory.py
```

The exact 89 action names are mapped one-for-one to target `github.*` Runtime Bridge actions. Inspection of the current Runtime Bridge implementation finds no exact remote GitHub REST/GraphQL action, so exact parity is presently `0 / 89`; the existing local semantic Git layer is reusable architecture, not remote GitHub parity.

The preferred authentication design is a dedicated GitHub App using a user access token obtained through GitHub device flow. This is required to preserve installation-aware semantics without exposing caller-supplied credentials. Repository scope follows the app installation; API transport is an internal server-owned REST/GraphQL client; access and refresh tokens remain outside ordinary Git and MCP arguments/results.

The design also freezes action-specific pagination/error/mutation rules, explicit `github.*` public naming, artifact resource handoff, non-force/stale-head safeguards, and incremental projection qualification toward the full 89-action surface.

One evidence gap remains before implementation contracts can be frozen: Validation 128 preserved the exact count and capability families but not the complete native action schemas. The next gate is therefore one fresh GitHub-only discovery conversation using the preserved batched schema-capture procedure. It performs no GitHub mutation.

## 11. Fresh exact-name projection correction

The required fresh GitHub-only schema-capture conversation independently projected exactly 89 actions and invoked none. Its exact ordered action inventory exposed one defect in the Checkpoint 372 reconstructed names:

```text
fresh projection only        GitHub.download_user_content
Checkpoint 372 inventory only GitHub.add_issue_comment
```

`GitHub.add_comment_to_issue` is projected; `GitHub.add_issue_comment` is not. Because Validation 128 never publicly preserved all exact names, Validation 130 / Checkpoint 373 classify this as a Checkpoint 372 reconstruction defect rather than connector drift. The schema-version-2 machine inventory now preserves the exact fresh projected order.

The architecture selected at Checkpoint 372 remains accepted. The correction changes one action identity/family assignment but does not change the 89-action count, GitHub App/device-flow direction, installation-derived scope, internal REST/GraphQL design, or exact remote parity state.

## 12. Native schema Batch 1 result

Validation 131 / Checkpoint 374 preserve projected action contracts 1-15 from the same fixed GitHub-only conversation with zero GitHub action invocations. The specialized machine evidence now lives in `docs/research/github_connector_native_schema_capture.json` and is guarded by `scripts/check_github_connector_schema_capture.py`.

Batch 1 demonstrates that input projection fidelity is substantially stronger than output/error projection fidelity:

```text
input object contracts                       15 / 15 exposed
separate action title metadata                0 / 15 exposed
projected return type                         any for 15 / 15
machine-readable output schemas               0 / 15 exposed
structured error schemas                      0 / 15 exposed
pagination-bearing inputs                     0 / 15 exposed
```

Two projected enums are exact evidence: `add_review_to_pr.action = COMMENT | APPROVE | REQUEST_CHANGES` and `create_blob.encoding = utf-8 | base64` with default `utf-8`. Several cross-field rules are descriptive rather than structurally encoded, including review-body requirements, the `create_branch` sha/base_ref XOR, and parts of `create_pull_request` validation.

Some descriptions state normalized issue/PR snapshots or SHA/compare results while the machine return schema remains `any`. This is preserved as an evidence gap rather than filled by inference. Final parity reconciliation must determine whether additional live-result capture is required before claiming exact output-shape parity.

## 13. Native schema Batch 2 result

Validation 132 / Checkpoint 375 preserve projected actions 16-30 and advance cumulative native schema capture to `30 / 89`, again with zero GitHub action invocations. Batch 2 confirms the expected Batch 1 output/error projection limitations and adds several architecture-relevant contracts.

`GitHub.create_tree.tree_elements` is genericized to `{ [key: string]: any }[]`, so exact inner tree-entry schema remains unproven by host discovery. `GitHub.download_user_content` is now resolved as a read-only semantic downloader restricted to `https://private-user-images.githubusercontent.com`, while `GitHub.download_workflow_artifact` explicitly follows GitHub's redirect and returns a reusable ZIP file reference. These are bounded URL/file semantics, not arbitrary caller HTTP authority.

Pagination is demonstrably action-specific: `fetch_commit_workflow_runs` returns only the first page and exposes no continuation; `fetch_issue_comments` fetches all pages internally; `fetch_pr_comments` does not state an all-pages guarantee. `fetch_issue.repository_url` also explicitly names GitHub Enterprise Server custom hostnames and GHE.com API hosts as accepted selectors. That endpoint-specific evidence is now a host-scope follow-up for the final GitHub App/API architecture rather than a reason to assume either universal Enterprise support or github.com-only parity.

## 14. Native schema Batch 3 result

Validation 133 / Checkpoint 376 preserve projected actions 31-45 and advance cumulative native schema capture to `45 / 89`, again with zero GitHub action invocations. Batch 3 adds concrete error/valid-empty semantics rather than only absent structured error-schema evidence.

`GitHub.fetch_pr_file_patch` requires a path first validated by `list_pr_changed_filenames`; an accessible PR that does not contain the path returns `patch=null`, while a documented 404 means GitHub could not resolve the repository or pull request and the connector says not to retry alternative paths. This is direct evidence for preserving valid-empty versus not-found distinctions and no-blind-retry behavior.

Pagination/selection behavior expands again: `fetch_pr_patch` spans all changed-file pages; workflow-run artifacts are first-page-only; workflow-run jobs are both latest-attempt-only and first-page-only; reaction readers expose explicit 1-based `page` plus `per_page`. `get_pr_diff` exposes `diff | patch` with default `diff`, while `get_pr_info` deliberately excludes code changes. `get_profile` is zero-argument. `get_repo` repeats the descriptive repository selector XOR and Enterprise/GHE.com URL evidence. `get_repo_collaborator_permission` exposes no permission-result enum, so result values remain an output-shape gap.

## 15. Native schema Batch 4 result

Validation 134 / Checkpoint 377 preserve projected actions 46-60 and advance cumulative native schema capture to `60 / 89`, again with zero GitHub action invocations.

Batch 4 strengthens the installation-aware discovery evidence through `list_installations`, `list_installed_accounts`, and `list_repositories_by_installation`. It also confirms that listing semantics remain action-specific: recent PRs internally paginate to a final `limit`; changed PR filenames span all file-list pages; recent issues continue until `top_k` or source exhaustion; repository list families expose zero-based `page_offset`; review-thread/review and organization-list pagination remain unspecified.

Four actions are true zero-argument calls: `get_user_login`, `list_installed_accounts`, `list_user_org_memberships`, and `list_user_orgs`. Recent-PR `state` examples and repository `affiliation` examples remain plain strings rather than enums, while `lock_issue_conversation.lock_reason` is a genuine projected enum of `off-topic | too heated | resolved | spam` with null default.

The host still projects return type `any` and no structured error schema across the batch, so installation/account/review/repository output models remain a later result-shape evidence question rather than an inferred contract.

## 16. Native schema Batch 5 result

Validation 135 / Checkpoint 378 preserve projected actions 61-75 and advance cumulative native schema capture to `75 / 89`, again with zero GitHub action invocations.

Batch 5 captures the strongest PR merge safety contract so far. `merge_pull_request.merge_method` is exactly `merge | squash | rebase`, and optional `expected_head_sha` is an explicit optimistic-concurrency guard: GitHub rejects the merge when the pull-request head moved. The description also exposes semantic merge result fields `sha`, `merged`, and `message`, although their machine types remain hidden behind `any`.

Reviewer request/removal actions expose optional individual/team arrays but no projected at-least-one rule. `reply_to_review_comment` requires the thread's top-level inline review comment ID and explicitly does not support replies-to-replies. Both exposed Actions rerun mutations require GitHub Actions write permission.

Search semantics diverge again: `search` exposes a final `topn` limit, treats empty query as valid no-results, and exposes no continuation interface; `search_branches` exposes an opaque cursor plus `page_size`, while the `any` output hides the response field carrying the next cursor. Batch 5 contains thirteen mutations and two reads, so later parity qualification will require correspondingly bounded disposable mutation fixtures.

## 17. Native schema Batch 6 result

Validation 136 / Checkpoint 379 preserve projected actions 76-89 and complete cumulative native schema capture at `89 / 89`, again with zero GitHub action invocations.

The final batch adds several high-value search and mutation constraints. Commit search exposes `best-match | author-date | committer-date` and `desc | asc`, rejects qualifier-only queries, and documents a narrow empty-query plus `repository_full_name` path for listing recent commits. Installed-repository search exposes both opaque `next_token` continuation and a separate 1-based page model, while repository search exposes 1-based paging plus a `topn` alias for `per_page`. Issue search allows at most one repository-selector family; PR search does not project an equivalent mutual-exclusion rule.

`update_file` requires the current blob SHA, exposes semantic result values for commit SHA and `content_sha`, and explicitly says same-path update/delete writes must not run in parallel. `update_issue` uses full replacement semantics for assignees and labels and exposes no explicit way to clear an existing milestone. `update_ref` remains branch-oriented with `force=false` default and no tag/ref-namespace selector. `update_review_comment` can edit both inline review comments and replies, unlike the top-level-only creation rule of `reply_to_review_comment`.

All 89 host-visible contracts are now captured in the machine artifact, but the status deliberately remains `CAPTURED_89_OF_89_PENDING_FINAL_RECONCILIATION`. The known host-projection gaps around `any` outputs, hidden normalized models, genericized inner schemas, descriptive-only validation and unspecified pagination must be reconciled before implementation contracts are frozen.

## 18. Final 89-action schema reconciliation

Validation 137 / Checkpoint 380 preserve the final same-conversation reconciliation after all six native schema batches. The inventory is exact and complete at 89/89, with zero missing or extra projected actions and zero GitHub action invocations during discovery.

The reconciliation marker is deliberately `GITHUB_89_SCHEMA_CAPTURE=INCOMPLETE`. This means exact native-wrapper wire parity cannot be reconstructed from the host projection: every action returns machine type `any`, every structured error schema is absent, separate title metadata is absent, and `create_tree.tree_elements` is structurally genericized. Several cross-field rules, alias semantics, pagination guarantees and continuation result fields are also descriptive or hidden.

This result does **not** invalidate practical action mapping. Action names, host-visible request fields, required/optional status, defaults, visible enums, visible constraints, read/mutation classification and visible pagination semantics are captured for all 89. The dedicated gap plan now distinguishes native host-visible contracts, authoritative GitHub platform contracts and wrapper-only hidden behavior.

G0 is opened because the remaining gaps are action-specific and do not constrain the independent GitHub authority/API substrate. G0 may implement GitHub App/device-flow authorization, protected server-owned token lifecycle, installation-derived scope, bounded REST/GraphQL transport and transport-level semantic errors without declaring any `github.*` action parity-qualified. Action-specific publication remains gated by its relevant platform/result/error evidence. Broad live replay of all 89 native actions is not justified merely to sample hidden `any` results.

## 19. Official GitHub API/auth baseline

Validation 138 / Checkpoint 381 apply current official GitHub platform documentation to the reconciled connector surface. The selected GitHub App user-access-token/device-flow architecture is confirmed: user tokens are bounded by both app and user access, installation scope is directly enumerable, device-flow token issuance does not require a client secret, and refresh likewise may omit the client secret when the token originated through device flow. The current expiring user-token lifecycle is eight hours plus a six-month refresh token.

For the first github.com target, the REST transport is pinned to API version `2026-03-10`, `application/vnd.github+json`, a fixed valid User-Agent and Bearer user authorization. Enterprise Server is intentionally separate because supported REST API versions differ.

The same platform pass closes the most important host-projection request gaps: Git Tree entries now have authoritative path/mode/type/sha/content semantics; create-PR requires normalized head/base and title/issue conditional behavior; Contents create/update/delete operations on the same path must be serialized. Native alias precedence remains hidden, so Codexless adopts an explicit fail-closed conflict rule rather than guessing.

## 20. G0 private implementation result

Validation 139 / Checkpoint 382 preserve the first actual G0 code at private local-runtime head `3c5f3688ec578c0817953890dc69ecb7ce679153`. The candidate implements the protected token-store abstraction and OS-keyring adapter boundary, device authorization with private in-memory `device_code`, interval/`slow_down` handling, single-flight refresh, fixed github.com REST transport, server-registered GraphQL operations, installation-derived repository authority and stable semantic error/uncertainty classification.

The focused candidate suite passes 12/12 with fake HTTP/keyring implementations only. No GitHub credential, real GitHub request, real OS credential write, installed Codexless byte or public `github.*` tool was touched.

The private runtime integrity gate also provided useful negative evidence. Its first push rejected ordinary token-handling source syntax as secret-like material. The gate was kept intact; code/fixtures were changed until the exact scanner patterns produced zero matches, after which normal semantic push passed `RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS`.

## 21. Windows protected-store host qualification

Validation 140 / Checkpoint 383 close the concrete Windows keyring discriminator. The exact `@napi-rs/keyring@2.0.0` package had already passed import/API checks under Windows x64. A sandboxed Credential Manager write failed with `ERROR_NO_SUCH_LOGON_SESSION`, but the same package then completed one bounded normal-user-session synthetic lifecycle with set/read-match/delete/verified-absence all true. No GitHub token was involved and the synthetic secret was neither printed nor persisted.

This separates package/runtime viability from sandbox logon-session limitations. The temporary package tree and npm cache used for qualification were removed afterward.

## 22. Main-runtime G0 source integration

Validation 141 / Checkpoint 384 preserve the first main-runtime source integration at private head `6ce0da8818a455731acc10ba231ef9f52c0c8206`. Public-preview construction now has a lazy internal GitHub kernel that reads only whether `CODEXLESS_GITHUB_APP_CLIENT_ID` is configured at startup, performs no keyring import/credential read/network request until future internal services are requested, and exposes only non-secret runtime metadata. The MCP server factory and public allowlist are intentionally unchanged, so the public surface remains 63 tools with zero `github.*` actions.

The candidate passes 9/9 source syntax checks and 4/4 integration regressions with zero secret-scanner matches and no live GitHub or OS credential activity. The private push passes `RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS`.

The release-path inspection exposes one deployment blocker: Runtime Release v1 owns only `src`, `test`, `scripts`, and `config` targets and has no package dependency transaction. It cannot provision `@napi-rs/keyring@2.0.0` into the installed runtime. Because temporary host-qualification staging was removed, a source-only G0 release would be incomplete when configured.

## 23. Immutable runtime dependency generations

Validation 142 / Checkpoint 385 close the package-provisioning architecture blocker at private local-runtime head `5b63371536fa2f09bb122ed09470ec5204f18d9b`. The exact Windows keyring package is prepared as a server-owned immutable generation and selected by canonical `{dependencyId, treeSha256}` worker binding. The Runtime Release v2 candidate stores those refs in prepared/pending/active state and selects target/previous generations correctly for forward activation, rollback, ordinary restart and recovery. Runtime startup revalidates every bound generation before exposing the resolver.

A real package preparation and load succeeded for 10 files / 1,971,364 bytes at tree digest `abe67a212121747d57d1bb78cd7880e7e7bb29e1f44e2ba8ec5010e5f1e50858`. Real Release v2 preparation produced the same exact generation binding. A Windows discriminator also established why the generation must remain immutable: deleting the loaded native generation in the same Node process failed with `EPERM`, while cleanup succeeded after process exit. Rollback therefore switches worker bindings instead of replacing/deleting loaded native package directories.

The G0 keyring importer now resolves only through that exact dependency resolver and has no ambient live-`node_modules` fallback. The combined focused suite passes 22/22; source syntax passes 21/21 for the combined G0 candidate and 15/15 for the release dependency candidate; the focused secret scanner reports zero matches. No GitHub credential or public `github.*` action was introduced.

## 24. Live source-only G0 bootstrap

Validation 143 / Checkpoint 386 live-qualify the source-only bootstrap release at private head `21b8597abde893a2b6e6b9b91d3488de0fe8aa16`. Release `github-g0-dependency-bootstrap-v1` deliberately remains manifest v1 so the old live engine can consume it. It carries 26 source/test files and 14 regressions while preserving target surface `codexless-public-preview-v2` and 63 tools.

The old engine prepared the bundle, publication succeeded under operation `rm_92d5a1cdf16ee979cabda34918b5c686`, exact installed-source verification reached zero mismatches, and restart operation `rm_1dcf2e517515a89eee1c5c651bc440ef` activated version `0.1.1-preview.22-github-g0-bootstrap` without recovery. A fresh postactivation verification returned the new dependency-aware field `runtimeDependencyCount=0`, proving that the upgraded Release v2-capable source is live while the keyring generation remains deliberately unbound.

The public surface is unchanged at 63 tools with no `github.*` action, and no live GitHub authorization or GitHub API call was started. This closes the self-bootstrap problem identified at Checkpoint 385.

## 25. Live exact keyring-generation activation

Validation 144 / Checkpoint 387 live-qualify the first Runtime Release v2 dependency activation at private head `19a4d1852f99f0d10d1a5b4bca23c0f39d825bb1`. Release `github-g0-keyring-activation-v2` declares only server-owned dependency id `github-keyring-win32-x64`, advances the runtime to `0.1.1-preview.23-github-g0-keyring`, retains surface `codexless-public-preview-v2` and 63 tools, and introduces no public GitHub action.

A fresh real-binding smoke resolved the exact immutable tree `abe67a212121747d57d1bb78cd7880e7e7bb29e1f44e2ba8ec5010e5f1e50858` and loaded the native keyring `Entry` constructor without reading or writing credentials. The live v2 engine then prepared one runtime dependency, publication operation `rm_080792c073690364c32fa90c7c1da128` succeeded with fifteen regressions including that smoke, and restart operation `rm_41cf35130455181ec38697d2aa1ae435` succeeded without recovery. Fresh postactivation verification returns `runtimeDependencyCount=1` and zero source mismatches.

The package-deployment path is therefore closed for G0. The internal GitHub kernel still has no configured live authorization lifecycle on the public MCP surface, and no GitHub token or API request was created by this activation.

## 26. Live authorization-control support surface

Validation 145 / Checkpoint 388 live-qualify the explicit GitHub App authorization-control support surface at private local-runtime head `d63bb48112985fd05e4a32925b83e75214dd2a4a`. The final immutable release is `github-auth-control-v2-fix2`, target version `0.1.1-preview.24-github-auth-control`, 64 public tools, one exact keyring runtime dependency and manifest SHA-256 `92554d6da7418885fcb491f1c16a2527517ca09d6c230d0d8a5dc54e1421a7be`. Publication and restart both succeeded without recovery, and postactivation verification reports zero source mismatches.

The one new public support tool is `codex.github_authorization`, separate from the 89-action parity namespace. Its closed operations are `metadata`, `begin(requestId)`, `status(authorizationRef)`, `poll(authorizationRef)`, `cancel(authorizationRef)` and `clear(confirmClear=true)`. It exposes no client secret, token, private device code, arbitrary OAuth scope, URL/header/method, keyring payload or package authority. Direct live local MCP `tools/list` contains the tool and its full schema. A live metadata-only invocation returned `configured=false`, `initialized=false`, `authorized=false` and `storedAuthorization=false` for github.com REST `2026-03-10`; it started no device flow and made no GitHub OAuth/API request.

Two failed immutable release attempts remain preserved rather than rewritten. The original release failed a public-surface regression; changed bytes under that prepared ID then correctly produced a prepared-release conflict. The first new immutable retry exposed two older semantic-Git tests that still froze 63 tools. The final fix updated those exact expectations and passed. This strengthens the release/regression contract rather than weakening it.

The live server is now 64 tools, but the current persistent ChatGPT conversation still does not project `codex.github_authorization` as a callable action. This is another AB-008 same-conversation stale-projection observation.

## 27. Fresh-host union genericization and flat authorization correction

Validation 146 / Checkpoint 389 preserve the first fresh-host qualification of `codex.github_authorization`. The tool name and description projected, but the host collapsed the strict local six-branch authorization union to `{ [key: string]: any }`. The one allowed `metadata` invocation was blocked by host safety controls before a Runtime Bridge payload returned. No title/annotations or machine-readable action fields were visible in that projection. Local preview.24 MCP discovery still showed the intended closed `oneOf`, so this is another direct AB-008 local-union/host-generic-map reproduction. The safety-block cause is not asserted beyond that evidence.

The correction reuses the already qualified preview.19/preview.20 pattern rather than adding a new workaround. Private head `ad10aa30342503d303b6a22629fe56dc914f0fa2` flattens the authorization support schema to one strict object containing required six-value `action` plus optional bounded `requestId`, `authorizationRef` and literal `confirmClear=true`; exact per-action field combinations are server-validated with `GITHUB_AUTHORIZATION_INPUT_INVALID`. A dedicated MCP wire regression proves no top-level union and full field visibility.

Release `github-auth-control-flat-v2` passed all sixteen staged regressions, published successfully under `rm_6215ff67fd5ca530af3ca953b0cad03a`, and activated successfully under restart `rm_accbd4edacc46458cae81dd493173feb`. The active runtime is now `0.1.1-preview.25-github-auth-flat`, 64 tools, one exact keyring dependency and zero source mismatches. Direct local MCP `tools/list` exposes the flat schema and a local metadata-only call remains non-secret with `configured=false`, `authorized=false`, `storedAuthorization=false`.

## 28. Fresh-host flat authorization and live Plugin-name qualification

Validation 147 / Checkpoint 390 close the preview.25 fresh-host discriminator. A refreshed fresh disposable ChatGPT conversation projects `codex.github_authorization` as a structured flat bounded schema rather than a generic map. The machine-visible host contract includes required six-value `action`, optional `requestId` with 1..128 bounds and regex, optional exact-format `authorizationRef`, and optional literal `confirmClear=true`. The host rendering does not separately print `additionalProperties=false`, so that keyword remains a local MCP wire fact from Validation 146 rather than an overclaimed host-visible field. No top-level `oneOf`/`anyOf` or arbitrary index signature is projected.

Exactly one `metadata` invocation succeeds through the host and returns `configured=false`, `initialized=false`, `authorized=false`, `storedAuthorization=false`, `github-app-user-token-device-flow`, `github.com`, and REST `2026-03-10`. No user code, verification URI, authorizationRef, token, credential write/delete or GitHub API/OAuth operation occurs. This resolves the concrete preview.24 qualification failure and validates the flat schema shape for this support tool.

The project owner also supplied a current ChatGPT UI screenshot showing the connected Plugin as `Codexless Runtime Bridge`. That direct UI evidence closes the live Plugin display-name rename left open at Checkpoint 370. `ADS` remains the overall project/system name; historical exact `ADS Codexless Local Bridge` evidence remains untouched.

## 29. GitHub App permission manifest

Validation 148 / Checkpoint 391 derive the first registration-ready permission manifest from the exact 89-action inventory and current official GitHub REST permission requirements. The machine artifact `github_app_permission_manifest.json` preserves one exact mapping row per native action and `check_github_app_permission_manifest.py` protects inventory order, manifest minimality and the GraphQL evidence boundary.

The frozen initial repository permissions are exactly: Actions(write), Contents(write), Issues(write), Metadata(read), Pull requests(write), Commit statuses(read), and Workflows(write). No organization/account/enterprise permission or webhook event is requested. Administration, Checks and Members remain explicitly absent. `Workflows(write)` is required for practical parity because GitHub conditionally requires it for file/ref mutations that affect `.github/workflows`, while the observed native actions accept arbitrary repository paths/refs.

The remaining permission uncertainty is intentionally narrow. GitHub publishes exact REST permission requirements but tells GitHub App developers to test GraphQL queries/mutations for sufficient permissions rather than publishing an exact GraphQL permission matrix. Eight observed actions use GraphQL or GraphQL-node handling, all in the pull-request/review family. The App already needs Pull requests(write) for ordinary REST parity mutations, so that is the frozen least-privilege candidate and no speculative permission is added. A post-registration live GraphQL sufficiency probe is mandatory.

## 30. Frozen GitHub App registration configuration

Validation 149 / Checkpoint 392 freeze the non-secret registration and first-installation settings around the seven-permission manifest. The dedicated App is owned by the personal account that owns the canonical public ADS repository and requests the canonical name `Codexless Runtime Bridge`; GitHub itself must confirm global name availability at creation. The App is configured as Any account/public so the same registration can later be installed on explicitly approved personal and organization accounts. A private personal-account App would be owner-account-only and would structurally prevent the multi-installation parity target.

The authorization configuration is deliberately separate from installation: device flow ON, expiring user access tokens ON, Request user authorization during installation OFF, no callback URL, no setup URL, webhooks OFF, and no private key/JWT bootstrap. The seven repository permissions are reused exactly. A GitHub-supported registration prefill URL captures the identity, visibility, webhook and permission fields; device flow and token-expiration toggles remain manual confirmations because GitHub does not expose them in the documented URL-parameter table.

The first installation is intentionally limited to the owner account and `Only select repositories` with only `shakaarlatief/autonomous-data-science-system`. This minimizes the first live authorization blast radius while allowing installation-intersection and read-only GraphQL sufficiency qualification. It does not weaken the final parity target; broader installations remain explicit future approvals.

## 31. Extended GitHub capability scope reopened

Validation 150 / Checkpoint 393 preserve a deliberate product-scope expansion before the dedicated GitHub App is created. Research 123 is no longer only an 89-action parity implementation. The target becomes native connector parity plus selected GitHub capabilities that a project-owned App can expose but the provider-owned ChatGPT GitHub integration does not currently project. Repository creation/administration is explicitly desired.

Current official GitHub permission documentation plus the owner's live registration UI show a much broader permission surface than the seven parity-derived repository families. `GITHUB_APP_EXTENDED_PERMISSION_REVIEW.md` records the established repository/organization/user/enterprise headings and newer preview categories such as Agent tasks. Repository Administration(write) is the strongest immediate extension candidate because it covers repository creation/deletion/settings/teams/collaborators and related administrative APIs. Other strong candidates include Checks(write), Commit statuses(write), Deployments(write), Environments(write), Variables(write), code/security alert families, Attestations, Agent tasks/variables and selected Codespaces/Pages/custom-property capabilities.

The review distinguishes maximum useful developer capability from indiscriminate authority. Secret-value permission families are deferred until a secure secret transport exists. Repository Webhooks(write) is deferred until external destinations are bounded. Organization/account/enterprise permissions will be selected only where they add concrete development workflows because they broaden approval requirements.

The owner also clarified that the personal App installation should cover **All repositories**, not remain limited to the ADS repository. Organization repositories continue to require explicit installation/approval and remain bounded by the user + installation intersection.

## 32. Complete live GitHub permission inventory

Validation 151 / Checkpoint 394 close the live-permission discovery gap. Owner-supplied screenshots cover all four current GitHub App permission groups and expose 118 selectable/mandatory permission rows: 40 repository, 42 organization, 19 account and 17 enterprise. This live surface is broader than the consolidated public permission index and includes current/preview capabilities such as Agent tasks, Discussions, License compliance alerts, Merge queues, Packages, Projects, security-request families, Models, newer organization administration/security/Copilot controls and expanded enterprise-preview permissions.

The machine artifact `github_app_live_permission_inventory_20260909.json` preserves the exact live labels and a broad developer-superset candidate. The candidate enables or reads 34 repository, 30 organization and 10 account permission families, with all 17 enterprise permissions off. The only repository permissions kept off are Agent secrets, Codespaces secrets, Dependabot secrets, Actions Secrets, redundant Single file and Webhooks. Repository Administration is retained as a core extension because GitHub confirms Administration(write) can create repositories for the authenticated user and organizations plus manage broad repository settings.

The selection policy remains maximum useful professional development capability rather than maximum checkbox count. Secret-value families remain deferred until secure value transport exists; Webhooks remain deferred until external destinations are explicitly bounded. Organization credential/PAT/billing-sensitive families remain excluded from the current broad profile, while organization developer/admin/security capabilities are generally included. Enterprise permissions remain out of scope until a real enterprise target exists.

## 33. Extended permission manifest and registration frozen

Validation 152 / Checkpoint 395 convert the 118-row live UI inventory into the first actual broader-than-native App creation profile. The frozen profile selects 74 rows: 34 repository, 30 organization, 10 account and no enterprise permission. Native 89-action connector parity remains a subset rather than the ceiling. Repository Administration(write) is explicitly included so future bounded Codexless actions can create repositories and manage repository settings/collaborators; Checks/status publication, deployments/environments, Codespaces, discussions, packages/projects, security management, Agent/Copilot surfaces and selected organization/account administration are also included.

The profile deliberately stops short of indiscriminate authority. Repository Agent secrets, Codespaces secrets, Dependabot secrets, Actions Secrets, Single file and Webhooks remain No access. Organization secret/credential/PAT/webhook families and unrelated account-control permissions remain excluded; all enterprise permissions remain off. High-consequence selected permissions still require semantic Runtime Bridge actions and confirmation controls before public exposure.

The registration prefill embeds 56 independently documented permission parameter names. Eighteen current live/newer permission rows are manual UI selections because their registration parameter names were not independently verified. The project explicitly prefers a manual row over inventing an undocumented query key. Device Flow ON, user-token expiration ON, install-time OAuth OFF, webhook Active OFF, Any-account/public visibility and personal installation All repositories are frozen.

## 34. Owner UI pre-creation qualification

Validation 153 / Checkpoint 396 close the final manual registration-form gate. Owner-supplied screenshots show the completed form now matches the frozen extended profile exactly: repository 33 selected + 1 mandatory = 34 total, organization 30, account 10, enterprise 0. Device Flow is ON, expiring user authorization tokens are ON, install-time OAuth authorization is OFF, wildcard matching is OFF, Setup URL and Redirect URI are blank, Redirect on update is OFF, Webhook Active is OFF with blank URL/secret, and `Any account` is selected.

The App has not yet been created in this evidence, so no App ID, Client ID, installation or GitHub authorization exists. The owner may now click `Create GitHub App`, then install it on personal account `shakaarlatief` with **All repositories**.

## 35. Live GitHub App registered; installation private-key gate discovered

Validation 154 / Checkpoint 397 preserve the successful live App creation. GitHub registered `Codexless Runtime Bridge` under `shakaarlatief` with App ID `4881901`, Client ID `Iv23lirgmw82wV0SGTWn`, and slug `codexless-runtime-bridge`. The App is not yet installed and no Client secret, private key, access token, refresh token or device code has been generated.

GitHub's current post-registration UI now exposes an empirical gate not represented in the earlier design assumptions: `Registration successful. You must generate a private key in order to install your GitHub App.` This requires a bounded bootstrap correction. Official GitHub documentation still confirms that user access-token device flow itself uses the App Client ID and device code without a client secret, and refresh of a user token originally produced by device flow likewise does not require a client secret. GitHub App private keys are for authenticating as the App itself, including JWT/installation-token flows, which the selected Runtime Bridge authorization path does not use.

The corrected installation sequence is therefore to generate exactly one App private key only to satisfy GitHub's current install gate, never expose or commit the PEM, never use it for Runtime Bridge API authority, install the App on `shakaarlatief` with All repositories, then securely destroy the downloaded local private-key file. GitHub stores only the public portion of the registered key, so destroying the local private half does not alter the installation relation; if an App-authenticated flow is intentionally added later, a new private key can be generated under a dedicated secure-key architecture.

## 36. Live App installed on all personal repositories

Validation 155 / Checkpoint 398 preserve successful installation of `Codexless Runtime Bridge` on the owner's personal account. The live GitHub installation page shows the App as `Installed now` and `All repositories` selected. This closes the personal-repository installation-scope gate and matches the clarified target that Codexless should cover all repositories under the personal installation rather than only ADS. The installation ID is not yet captured.

The GitHub-required private key was generated only to satisfy the installation gate discovered at Checkpoint 397. No Runtime Bridge flow uses the private key. The downloaded local PEM is now a temporary bootstrap credential and must be deleted before live authorization proceeds. No Client secret has been generated.

## 37. Interrupted authorization recovery and Client-ID correction

Validation 156 / Checkpoint 399 close the interrupted device-flow bootstrap. The owner supplied current GitHub App settings evidence showing `Enable Device Flow` ON, so the earlier HTTP 404 was not caused by a disabled App setting. A public GitHub App lookup for slug `codexless-runtime-bridge` instead exposed a transcription defect in the Client ID previously copied from manual UI evidence. The live App record binds App ID `4881901` to corrected Client ID `Iv23lirgmw82wV0SGTWn`.

Direct non-secret transport discrimination reproduced HTTP 404 `Not Found` with the superseded value and HTTP 200 with the live value. Earlier public occurrences were repaired as a factual identifier correction; Git history preserves the superseded transcription. No access token, refresh token or private device code was printed by these diagnostics.

Private local-runtime head `6d641881423ea50e0fdf1329782dd2489735d551` preserves the corrected immutable release path. Release `github-client-config-v3` corrected the configuration but its first restart failed safely because the target version contract was not updated in `surface-contracts.mjs`; automatic runtime recovery restored the previous healthy worker. New immutable release `github-client-config-v4` corrected both configuration and runtime identity, published successfully, restarted without recovery, and postactivation verification reports `0.1.1-preview.27-github-client-id-correction`, 64 tools, one runtime dependency and zero mismatches.

## 38. Live GitHub user authorization qualified

Exactly one corrected Runtime Bridge device authorization was begun after metadata confirmed `configured=true`, `storedAuthorization=false`. The Runtime Bridge returned only the bounded authorization reference, user code and verification URI while retaining GitHub's private `device_code` internally.

After the owner completed GitHub authorization, exactly one poll of that same authorization reference returned `status=authorized`. Follow-up metadata now reports `authorized=true`, `storedAuthorization=true`, non-expired access and refresh lifetimes, `github-app-user-token-device-flow`, `github.com` and REST `2026-03-10`. A later status read of the consumed authorization reference returned `GITHUB_DEVICE_FLOW_REF_UNKNOWN`, confirming the pending in-memory device-flow session was removed after successful protected token storage. No token value was exposed through MCP or committed to Git.

The owner had already confirmed deletion of the locally downloaded PEM. Runtime Bridge still does not use App private-key/JWT authority, and no Client secret was generated.

## 39. First public GitHub read-only foundation live-qualified locally

Validation 157 / Checkpoint 400 advance the live Runtime Bridge from authorization-only G0 to its first public `github.*` action bundle. Private local-runtime head `a18983d2b2199f350d07664cfe91dbf013e2df3c` preserves final immutable release `github-readonly-foundation-v3`. The release migrates the historical G0 invariant that public GitHub action count must remain zero to the intentional four-action foundation, while retaining lazy construction, protected-store isolation and no-network-at-construction guarantees.

Publication operation `rm_d607e555f858e60d7ae5c253fcc71215` succeeded after the full bounded regression matrix. Restart operation `rm_86a5699c3cf0160932348716698b4230` then activated `0.1.1-preview.28-github-readonly-foundation` without recovery. Fresh postactivation verification reports 68 public tools, one exact runtime dependency and zero source mismatches. Direct Codexless health is live, and the already-running tunnel remains `live` and `ready` without restart.

The four public tools are:

```text
github.get_profile
github.get_user_login
github.list_installations
github.list_repositories_by_installation
```

`github.get_profile` and `github.get_user_login` use a fixed server-owned GraphQL viewer query. The installation/repository actions use the fixed github.com REST transport with the protected GitHub App user access token and installation-derived authority. Callers cannot supply tokens, hosts, endpoints, GraphQL documents, HTTP methods/headers or permission overrides.

A fresh stateless local MCP session against the active server discovered all 68 tools and invoked all four new actions read-only. The GraphQL viewer query returned authenticated login `shakaarlatief`. Installation enumeration returned one installation with `repositorySelection=all`. Repository enumeration returned twelve repositories through that installation and confirmed `shakaarlatief/autonomous-data-science-system` is in scope. Other repository names and all credential values were intentionally omitted from preservation.

The current bundle is deliberately a read-only **foundation**, not yet four fully closed native parity rows. The known discriminator is `github.list_installations(manageable_only=true)`: the native connector says this filters to managed setup account types but does not project the exact account-type/filter semantics. Runtime Bridge therefore fails closed with `GITHUB_PARITY_OPTION_NOT_QUALIFIED` rather than inventing wrapper behavior. The successful viewer GraphQL query also does not close the separate permission-sufficiency probes required for the eight PR/review GraphQL operations.

The same persistent `chatgpt-21` conversation still exposes its earlier connector tool projection and does not expose any of the four new `github.*` names even though direct active MCP `tools/list` contains them. This is the already-established AB-008 same-conversation stale-projection class. The decisive evidence is exact-name presence in live MCP and exact-name absence from this conversation, not a raw count comparison alone.

## 40. Current boundary

Research 123 remains active. The live Runtime Bridge now has four public read-only GitHub foundation tools, while exact native parity remains `0 / 89` until fresh-host qualification and the remaining native-contract gap are closed. The next bounded gate is to refresh/rescan the existing `Codexless Runtime Bridge` Plugin and use a fresh disposable ChatGPT conversation to capture the four host-visible schemas and invoke each new action once read-only. No remote GitHub mutation is authorized by this checkpoint.

```text
RESEARCH123=ACTIVE
TARGET=GITHUB_PARITY_PLUS_EXTENSIONS
GITHUB_APP_REGISTERED=true
GITHUB_APP_ID=4881901
GITHUB_APP_CLIENT_ID=Iv23lirgmw82wV0SGTWn
GITHUB_APP_SLUG=codexless-runtime-bridge
GITHUB_APP_INSTALLED=true
PERSONAL_INSTALL_SCOPE=ALL_REPOSITORIES
INSTALLATION_ID=RESOLVED_LIVE_NOT_PUBLICLY_REPRODUCED
PRIVATE_KEY_GENERATED=true
LOCAL_PRIVATE_KEY_DELETION=CONFIRMED_BY_OWNER
CLIENT_SECRET_GENERATED=false
GITHUB_APP_CLIENT_ID_CONFIGURED=true
GITHUB_USER_AUTHORIZED=true
STORED_AUTHORIZATION=true
LIVE_RUNTIME_VERSION=0.1.1-preview.28-github-readonly-foundation
LIVE_PUBLIC_TOOL_COUNT=68
LIVE_GITHUB_FOUNDATION_TOOLS=4
EXACT_PARITY_ROWS_CLOSED=0
KNOWN_PARTIAL_PARITY_GAP=github.list_installations.manageable_only_true
GRAPHQL_VIEWER_QUERY=PASS
SAME_CHAT_NEW_TOOL_PROJECTION=STALE
SOURCE_VAULT=PAUSED
NEXT=FRESH_CHAT_GITHUB_READONLY_FOUNDATION_SCHEMA_AND_LIVE_READ_QUALIFICATION
```

## 41. Fresh-host four-action read-only foundation qualified

Validation 159 / Checkpoint 402 close the fresh-ChatGPT-host projection gate left by Checkpoint 400 and resumed after the Checkpoint 401 semantic-Git reliability correction. The project owner supplied the completed refreshed disposable-chat qualification with final marker `GITHUB_READONLY_FOUNDATION_FRESH_HOST=PASS`.

All four expected actions projected and all four authorized live reads succeeded in the required order:

```text
github.get_profile
github.get_user_login
github.list_installations(manageable_only=false)
github.list_repositories_by_installation(page_size=20,page_offset=0)
```

The two identity calls agree on authenticated login `shakaarlatief`. Installation enumeration returns one personal User installation with `repositorySelection=all`. Installation-scoped repository enumeration returns 12 of 12 repositories, `hasMore=false`, and confirms `shakaarlatief/autonomous-data-science-system` is inside installation-derived scope. Installation ID and unrelated private repository names are deliberately not preserved.

The fresh-host result reports bounded schemas and no caller-selected token, credential, GitHub host, URL, REST endpoint, GraphQL document, HTTP method/header, permission profile or equivalent arbitrary transport authority. No access token, refresh token, device code, client secret, Authorization header or credential-store payload appeared, and no GitHub mutation occurred.

The owner did not reproduce the field-by-field Part A host-schema transcript in the persistent project conversation. This is an evidence-boundary detail, not a failed qualification: Validation 157 already preserves the exact local MCP serialized schemas, while Validation 159 preserves the fresh-host presence/boundedness judgment and four-call live-read result. No missing Part A fields are reconstructed from memory or inference.

The known `github.list_installations(manageable_only=true)` native-wrapper semantic gap remains open because the fresh qualification intentionally exercised only `false`. The broader 89-action host projection also still hides machine-readable output schemas behind `any`. Exact native-wrapper wire parity therefore remains conservatively `0 / 89`; Research 123 does not silently redefine that metric merely because the four Runtime Bridge foundation capabilities are now live and host-qualified.

The next implementation boundary is the remainder of G1 read-only identity/account/repository-discovery/permission coverage. Strong direct candidates from the already captured native contracts are:

```text
github.get_repo
github.get_repo_collaborator_permission
github.list_installed_accounts
github.list_repositories
github.list_repositories_by_affiliation
github.list_user_org_memberships
github.list_user_orgs
```

Search-installed-repository actions remain better grouped with G2 search. The unresolved `manageable_only=true` option can be targeted separately and must not block unrelated read-only G1 expansion.

```text
RESEARCH123=ACTIVE
GITHUB_READONLY_FOUNDATION_FRESH_HOST=PASS
FRESH_HOST_FOUNDATION_ACTIONS=4_OF_4
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
KNOWN_PARTIAL_PARITY_GAP=github.list_installations.manageable_only_true
NEXT=G1_IDENTITY_ACCOUNT_REPOSITORY_PERMISSION_READONLY_EXPANSION
```

## 42. G1 seven-action read-only expansion live-qualified locally

Validation 160 / Checkpoint 403 publish and activate the remainder of the G1 identity/account/repository-discovery/permission read-only slice. Private local-runtime head `7af8600dd2213d2fc2e5aca3b3ef32b8fafeacc6` preserves immutable release `github-g1-readonly-expansion-v1`, targeting `0.1.1-preview.30-github-g1-readonly`, 75 public tools, nine release files and one exact runtime dependency.

The first release-manifest draft declared 18 regressions and was correctly rejected by the existing Runtime Release v2 maximum of 16. The project kept that release bound unchanged and reduced the bundle to a still-representative 16-regression matrix. Separately, the private-runtime integrity scanner rejected a synthetic test token whose value resembled secret material; the fixture was changed rather than weakening the scanner. Neither event involved a real credential.

Prepublication verification reported the expected nine target mismatches against preview.29. Publication operation `rm_bc3ee2e4f09d12ed8f92af6686663961` then succeeded without recovery. Restart operation `rm_9c321da1381ec4ebd69657441d939be6` activated preview.30 without recovery, and postactivation verification returned `mismatchCount=0`. Protected GitHub App user authorization survived activation and remained configured, stored, authorized and non-expired.

A fresh stateless loopback MCP initialize/tools-list returned exactly 75 public tools and eleven `github.*` actions. The seven additions are:

```text
github.get_repo
github.get_repo_collaborator_permission
github.list_installed_accounts
github.list_repositories
github.list_repositories_by_affiliation
github.list_user_org_memberships
github.list_user_orgs
```

All seven new actions were then invoked exactly once read-only against live GitHub. The canonical public ADS repository resolved successfully and reported public visibility. Collaborator permission for `shakaarlatief` on that repository returned `admin`. Installed-account enumeration returned one personal User account. Owner-filtered repository listing and owner-affiliation listing each returned twelve repositories, no continuation, and the canonical ADS repository present. Organization memberships and organization listings both returned zero. Unrelated private repository names were deliberately not printed or preserved. No GitHub mutation or credential exposure occurred.

The new repository operations remain installation-scoped rather than caller-authority-scoped. `github.get_repo` accepts only one repository selector at a time and requires the selected repository to be available through the authorized App installation before repository data is returned. `github.list_repositories_by_affiliation` intersects GitHub's authenticated-user affiliation result with installation-derived repository scope.

Three known gaps remain explicitly fail-closed or separately scoped:

```text
github.list_installations(manageable_only=true)
    -> native managed-account filter semantics still hidden

github.list_repositories(include_search_index_status=true)
    -> native search-index enrichment contract still hidden

github.get_repo(repository_url=<Enterprise host>)
    -> Enterprise routing not yet qualified; initial URL selector is github.com-only
```

The native host still exposes machine output as `any`, so exact native-wrapper wire parity remains conservatively `0 / 89`. The eleven actions are real live Runtime Bridge capabilities, but Research 123 does not convert implementation/live-use evidence into exact native-wrapper parity where output or option semantics remain undocumented.

After preview.30 activation, the active MCP contains all eleven names while this persistent `chatgpt-21` connector projection still exposes only the prior four GitHub actions. This is the established AB-008 same-conversation stale-projection class. The next bounded gate is therefore a refreshed fresh disposable ChatGPT qualification of the seven new actions. G2 fetch/search/branch/commit/file reads begin only after that host gate is preserved.

```text
RESEARCH123=ACTIVE
LIVE_RUNTIME_VERSION=0.1.1-preview.30-github-g1-readonly
LIVE_MCP_TOOL_COUNT=75
LIVE_GITHUB_READONLY_TOOLS=11
G1_NEW_TOOLS=7
G1_LOCAL_MCP_PROJECTION=PASS_7_OF_7
G1_LOCAL_LIVE_READS=PASS_7_OF_7
G1_FRESH_HOST_PROJECTION=PENDING_7_ACTIONS
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
NEXT=FRESH_CHAT_GITHUB_G1_READONLY_SCHEMA_AND_LIVE_READ_QUALIFICATION
```

## 43. Seven-action G1 fresh-host qualification failed on one connector transport read

Validation 161 / Checkpoint 404 preserve the refreshed fresh-ChatGPT-host qualification of the seven preview.30 G1 actions. All seven exact action names projected and the supplied host qualification judged all seven schemas bounded, with no caller-selected token, credential, GitHub host, arbitrary URL, REST endpoint, GraphQL document, HTTP method/header, permission profile or equivalent arbitrary transport authority.

The qualification attempted all seven live reads exactly once and in the required order. Six succeeded. `github.get_repo` resolved `shakaarlatief/autonomous-data-science-system`; `github.get_repo_collaborator_permission` returned `admin`; both repository listing routes returned twelve repositories with the canonical ADS repository present and no continuation; and both organization reads returned count zero. No unrelated private repository names, secrets or GitHub mutations were preserved.

The only failed live call was `github.list_installed_accounts`, which returned before any application result with:

```text
type     mcp_network_error
code     network_error
message  Connection failed.
```

The disposable qualification did not retry the read and therefore correctly ended `GITHUB_G1_READONLY_FRESH_HOST=FAIL`. This result does not invalidate the 7/7 host projection or the six successful live reads.

After the failure was supplied to the persistent project conversation, protected authorization metadata remained healthy and a fresh stateless active-loopback MCP invocation of exactly `github.list_installed_accounts` succeeded with one installed account containing personal User `shakaarlatief`. This is a discriminator, not a retroactive repair of the failed host qualification. It establishes that preview.30 action logic and stored authorization remained operational after the fresh-host error, while leaving the exact connector/tunnel root cause unresolved.

The remaining G1 host gate is therefore reduced to one read-only action. The six successful fresh-host calls should not be repeated merely for symmetry. A separately authorized follow-up call to `github.list_installed_accounts` in the same disposable conversation is sufficient if that conversation still projects the action; otherwise one new disposable chat may be used. No Plugin rescan, Runtime Bridge publication or GitHub authorization mutation is required before that discriminator.

```text
RESEARCH123=ACTIVE
G1_FRESH_HOST_PROJECTION=PASS_7_OF_7
G1_FRESH_HOST_LIVE_READS=PASS_6_OF_7
G1_FRESH_HOST_OVERALL=FAIL
FAILED_ACTION=github.list_installed_accounts
FAILED_ACTION_CLASS=connector_network_before_application_result
POST_FAILURE_LOCAL_ACTION=PASS
PROTECTED_AUTHORIZATION_HEALTHY=true
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
NEXT=TARGETED_HOST_LIST_INSTALLED_ACCOUNTS_REQUALIFICATION
```

## 44. Targeted installed-accounts host recheck closed G1

Validation 162 / Checkpoint 405 close the single unresolved fresh-host G1 action left by Validation 161. `github.list_installed_accounts` remained projected in the disposable ChatGPT host and a new separately authorized invocation succeeded exactly once with no input. It returned `schemaVersion=codexless.github-readonly.v1`, one installed account, and confirmed personal account `shakaarlatief` with type `User`. No credential secret appeared and no GitHub mutation occurred.

The original Validation 161 failure remains first-class evidence:

```text
mcp_network_error / network_error / Connection failed.
```

It is not retroactively converted into an initial PASS. Instead, the preserved evidence composes cleanly:

```text
Validation 161  -> 7 / 7 projected, 6 / 7 live reads, one connector transport failure
Validation 162  -> targeted unresolved host read PASS
Combined G1    -> 7 / 7 host live coverage PASS
```

No Plugin rescan, Runtime Bridge restart or GitHub authorization change was needed between the failure and successful targeted host call, supporting the transient connector-transport classification without claiming an exact transport root cause.

Research 123 now advances to G2. The intended repository-git read-only action set is:

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

These eleven actions cover the G2 design label `fetch/search + branches/commits/files/blobs/compare` while leaving issue, PR/review and Actions-specific reads in their later slices. Exact native input contracts are already preserved by the 89-action schema capture; native output envelopes remain hidden behind `any` and must not be invented.

```text
RESEARCH123=ACTIVE
G1_FRESH_HOST_PROJECTION=PASS_7_OF_7
G1_FRESH_HOST_LIVE_COVERAGE=PASS_7_OF_7
ORIGINAL_G1_TRANSPORT_FAILURE_PRESERVED=true
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
NEXT=G2_FETCH_SEARCH_BRANCH_COMMIT_FILE_BLOB_COMPARE_READONLY_IMPLEMENTATION
```

## 45. G2 preview.31 live; fresh-host qualification next

Validation 163 / Checkpoint 406 preserve live activation of the eleven-action G2 read-only repository fetch/search/branch/commit/file/blob/compare slice. Private local-runtime head `b446a3fc2ff480e66acc81ddad56f12bb871feca` preserves corrected immutable release `github-g2-readonly-expansion-v2`, targeting `0.1.1-preview.31-github-g2-readonly`, 86 public tools, 22 GitHub read-only tools, ten release files, sixteen regressions and one exact runtime dependency.

The new public actions are:

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

The implementation remains installation-scoped and read-only. The generic fetch action is GET-only and limited to approved GitHub repository URL families; caller-supplied credentials, arbitrary methods, arbitrary headers, arbitrary GraphQL documents and non-GitHub host authority remain absent. Hidden native search-index enrichment behavior is not invented, Enterprise repository URL routing remains separately unqualified, and conflicting repository-search `per_page`/`topn` aliases fail closed instead of guessing precedence.

The first immutable v1 release path produced two useful fail-closed results. Its initial 17-regression manifest exceeded the existing Runtime Release v2 ceiling of sixteen and was rejected without widening that contract. After reducing the matrix to sixteen, the release prepared successfully but publication failed with `RUNTIME_RELEASE_REGRESSION_FAILED`. A reconstructed current-source stage localized the failing regression to an incorrect test expectation: nullable commit-search `sort` correctly serializes the visible enum `best-match | author-date | committer-date` plus null, while the test had expected no enum. The product schema was correct and the test was repaired. Because the v1 release ID was already immutably bound, the changed manifest/bytes correctly returned `RUNTIME_RELEASE_PREPARED_CONFLICT`; the corrected release therefore moved to a new immutable v2 ID.

Corrected v2 publication operation `rm_59bfec18a65b6d64e35b5ad003f7463d` succeeded after the full bounded release regression matrix. Restart operation `rm_ad739f5850d15cd2b7eb267d6ca25c0b` then activated preview.31 without recovery. One immediate read-only restart-status request crossed the deliberate worker-replacement window and returned host HTTP 502; the restart mutation was not replayed, and the same durable operation later returned `succeeded`. Fresh postactivation release verification reports `targetToolCount=86`, `fileCount=10`, `runtimeDependencyCount=1`, and `mismatchCount=0`.

Protected GitHub authorization survived activation and remains configured, stored, authorized and non-expired. No credential value or GitHub mutation appeared.

Targeted tool rediscovery inside this already-open `chatgpt-21` conversation still projects only the earlier G1 GitHub names. The eleven G2 actions are absent from this same-chat host surface despite the verified live preview.31 source contract. This is another AB-008 same-chat projection-staleness observation. The project therefore does not force live G2 calls through a stale host. The next bounded gate is one fresh disposable ChatGPT conversation that discovers the eleven exact actions, captures their bounded host-visible schemas and executes a bounded read-only live qualification against installation-authorized GitHub state.

Exact native-wrapper parity remains conservatively `0 / 89`. The live Runtime Bridge capabilities are real, but hidden native output envelopes and unresolved option semantics are not silently promoted into exact wire parity.

```text
RESEARCH123=ACTIVE
LIVE_RUNTIME_VERSION=0.1.1-preview.31-github-g2-readonly
LIVE_PUBLIC_TOOL_COUNT=86
LIVE_GITHUB_READONLY_TOOL_COUNT=22
G2_NEW_TOOL_COUNT=11
G2_RELEASE_V2=PASS
G2_POSTACTIVATION_VERIFY=PASS_ZERO_MISMATCH
PROTECTED_AUTHORIZATION_HEALTHY=true
SAME_CHAT_G2_PROJECTION=STALE
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
NEXT=FRESH_CHAT_G2_SCHEMA_AND_LIVE_READ_QUALIFICATION
```
