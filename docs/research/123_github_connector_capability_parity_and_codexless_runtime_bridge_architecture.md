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

Historical records that contain the exact earlier display name `ADS Codexless Local Bridge` remain valid historical evidence and are not rewritten merely for terminology cleanup. Actual live connector/display-name/tunnel renaming is implementation work that must be mapped and qualified before being claimed complete.

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

## 15. Current boundary

Research 123 remains active. The exact fresh 89-action inventory is frozen and native schema capture has reached `45 / 89` in the same fixed GitHub-only conversation. Implementation has not started. No credential mutation, GitHub App registration, live GitHub action publication, live connector rename, runtime release, repository-administration mutation, or Source Vault ingestion is implied by this research record.

```text
RESEARCH123=ACTIVE
GITHUB_CONNECTOR_BASELINE=89_ACTIONS_OBSERVED
GITHUB_NEGATIVE_CHALLENGE=SAME_89_ACTIONS
FRESH_GITHUB_ACTION_COUNT=89
FRESH_GITHUB_ACTIONS_INVOKED=0
CHECKPOINT372_EXACT_NAME_RECONSTRUCTION=CORRECTED_BY_CHECKPOINT373
FRESH_ONLY_ACTION=GitHub.download_user_content
RECONSTRUCTION_ONLY_ACTION=GitHub.add_issue_comment
GITHUB_ACTION_NAMES_MAPPED=89_OF_89
RUNTIME_BRIDGE_EXACT_REMOTE_PARITY=0_OF_89
AUTH_DIRECTION=GITHUB_APP_USER_TOKEN_DEVICE_FLOW
TARGET_PUBLIC_ACTIONS=EXPLICIT_GITHUB_NAMESPACE
NATIVE_SCHEMA_CAPTURE=45_OF_89
CREATE_TREE_INNER_SCHEMA=GENERICIZED
PAGINATION_POLICY=ACTION_SPECIFIC_CONFIRMED
VALID_EMPTY_VS_NOT_FOUND=EXPLICITLY_OBSERVED
NO_BLIND_RETRY_SEMANTIC=OBSERVED
ENTERPRISE_SELECTOR_SCOPE=FOLLOWUP_REQUIRED
PERMISSION_RESULT_ENUM=NOT_PROJECTED
HOST_MACHINE_OUTPUT_SCHEMA=NOT_PROJECTED
HOST_STRUCTURED_ERROR_SCHEMA=NOT_PROJECTED
CONNECTOR_CANONICAL_NAME=CODEXLESS_RUNTIME_BRIDGE
RESEARCH113=PAUSED_NOT_CLOSED
SOURCE_VAULT=PAUSED
NEXT=GITHUB_SCHEMA_CAPTURE_BATCH_4
```
