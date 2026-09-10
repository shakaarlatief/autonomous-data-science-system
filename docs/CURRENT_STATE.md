# Current State

**Checkpoint:** 431
**Date:** 2026-09-10
**Active development branch:** `v1-source-vault-bootstrap-resume`
**Active PR:** none
**Promoted V1 integration branch:** `v1-frontend-spike` at `2480109fadeee1e480ef03b82e335aacdf9adf91`
**Latest specification:** Specification 027
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no GENERIC / ADS_HORIZON / ORACLE_HORIZON comparison may be inferred.

## Active interaction context

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-22
Conversation title       22 - GitHub CI Evidence Publication and Qualification
Primary collaborator     ChatGPT
```

Repository artifacts remain authoritative across chats and models.

---

## Current active stage: Research 123 GitHub connector capability parity and Codexless Runtime Bridge architecture

Checkpoint 370 opens Research 123 as an owner-directed stage insertion before the separately planned next stage. Two fresh GitHub-only qualifications on 2026-09-08 converged on the same 89-action connector projection and live-qualified a substantial remote development workflow, including direct file commits, raw Git object/ref construction, deep PR/review collaboration, issue lifecycle operations, and Actions/CI inspection. A second intent-specific negative challenge discovered no additional actions, so absent capability families are now classified conservatively as `NOT_OBSERVED_IN_THIS_PROJECTION` rather than permanent global impossibilities. In the same `chatgpt-19` mobile-web conversation, the Codexless developer MCP remained callable and `codex.account_preflight` passed while the native GitHub connector was not projected, preserving the coexistence problem already recorded by Validation 034. The project owner selected `Codexless Runtime Bridge` as the canonical forward-looking name for the custom connector, while `ADS` remains reserved for the complete Autonomous Data Science System. Validation 147 / Checkpoint 390 now qualify the live ChatGPT Plugin display name as `Codexless Runtime Bridge`; historical exact connector names remain evidence and are not rewritten. Research 113 is paused, not completed; Source Vault remains paused. Persistent session `chatgpt-22`, titled `22 - GitHub CI Evidence Publication and Qualification`, is now active.

Checkpoint 431 freezes the second beyond-parity GitHub extension family as **CI Evidence Publication**. The live App installation confirms `checks=write` and `statuses=write`. The six-action foundation contains three Checks reads (`github.get_check_run`, `github.list_check_runs_for_ref`, `github.list_check_run_annotations`), two Checks writes (`github.create_check_run`, `github.update_check_run`), and namespaced `github.create_commit_status`. Check writes expose only queued/in-progress/completed lifecycle states, exclude GitHub-Action-only statuses and stale conclusion, use strict output/annotation bounds, preserve server-owned timestamps, and enforce monotonic update transitions with read-before-write scope revalidation and no replay after mutation uncertainty. Commit statuses always use a server-owned `codexless/<context_suffix>` context namespace and expose no arbitrary target URL, preventing accidental overwrite/impersonation of unrelated CI providers. Manual check-suite controls and rerequest are deferred because suite creation is automatic and rerequest depends on webhook handling while the App webhook receiver remains disabled. No CI-evidence mutation occurred. The next boundary is local implementation/publication of the six-tool foundation with fake-dependency tests and no positive write.

Checkpoint 430 closes positive-live qualification of `github.create_repository` and completes the first beyond-parity Repository Administration foundation. The owner explicitly authorized exact repository `test-repo-codexless` with `visibility=public`. Runtime Bridge invoked the create action exactly once with `auto_init=false` and null optional metadata; it succeeded without retry or mutation uncertainty, returning `shakaarlatief/test-repo-codexless`, repository ID `1363584704`, node ID `R_kgDOUUamwA`, `private=false`, `visibility=public`, default branch `main`. One independent read-only `github.get_repo` postflight confirmed the same identity/visibility and full admin/maintain/push/triage/pull permissions. No additional administration mutation was performed. The administration foundation is now complete through implementation 3/3, local-live reads 2/2, fresh-host schema 3/3, fresh-host reads 2/2, create no-write guard PASS and create positive-live 1/1. The created repository remains as the explicitly authorized qualification artifact; no implicit delete occurs. The next boundary is read-only design selection of the next beyond-parity GitHub capability family.

Checkpoint 429 closes refreshed-host qualification of all three preview.40 Repository Administration tools. A fresh ChatGPT host projects `github.list_repository_collaborators`, `github.list_repository_invitations`, and `github.create_repository` with sufficiently bounded caller contracts. The two read-only calls succeed exactly once against the canonical ADS repository, returning one collaborator (the authenticated admin user) and zero open invitations. The deliberately invalid create input `name="bad name"` is rejected by host schema validation before Runtime Bridge/GitHub dispatch; its diagnostic directly exposes the create schema with `additionalProperties=false`, name regex `^[A-Za-z0-9._-]+$`, private/public visibility defaulting private, and `auto_init=false`. There are zero mutations, zero retries, zero mutation-uncertain results and zero repositories created. All 92 currently live GitHub tools now have fresh-host caller-schema qualification evidence. Positive `github.create_repository` remains 0/1 and still requires separate owner authorization for one exact repository name and visibility.

Checkpoint 428 activates the first beyond-parity Repository Administration foundation on Runtime Bridge preview.40 at 156 public tools / 92 GitHub tools. The three new actions are `github.list_repository_collaborators`, `github.list_repository_invitations`, and controlled personal-only `github.create_repository`. Focused fake-dependency tests pass 4/4. Preview.39 first exposed an outer-runtime facade delegation defect during safe live reads; no write occurred. A narrow preview.40 repair adds the missing delegates and regression coverage, publishes from local-runtime head `5846f02785c97df99c0ba8edc47f160a3710ef2b`, and postactivation verification reports zero mismatches for manifest `a638f715565ebf939cdaa37ea9e1caeb743b1b5939423b68537da0346fd5e778`. Direct local MCP now positively reads one collaborator on the canonical ADS repository and zero open invitations. A deliberately invalid create name containing a space is rejected by input schema before GitHub dispatch. No schema-valid repository creation call has occurred. The persistent `chatgpt-21` host projection remains stale and does not expose the three new tools, so the next boundary is one refreshed disposable fresh-host schema/read/no-write qualification. Positive repository creation remains separately owner-authorized after that host gate.

Checkpoint 427 freezes the first beyond-parity Repository Administration extension slice using current official GitHub contracts and the already-installed extended App permissions. The first foundation contains exactly three new actions: read-only `github.list_repository_collaborators`, read-only `github.list_repository_invitations`, and controlled `github.create_repository`. The reads use installation-derived repository authority and fixed paginated endpoints with bounded collaborator affiliation/permission filters and normalized invitation metadata. Personal repository creation uses the fixed authenticated-user endpoint, is limited to the authenticated personal account in v1, exposes only a 1..100 documented repository name, optional bounded description/homepage, semantic `visibility=private|public` defaulting **private**, and `auto_init` defaulting false. It accepts no organization owner, template/team selector, feature/merge/security settings, ruleset, rename, visibility mutation, archive/transfer/delete or arbitrary transport authority. Creation is serialized by authenticated user/name and never automatically retried after uncertain transport. GitHub documents that Apps that create repositories are automatically granted access, so no installation permission/scope change is required; the existing App already has Repository Administration(write). Collaborator/invitation writes, destructive lifecycle changes and rulesets remain deferred into later semantic families. No GitHub administration mutation occurred. The next boundary is local implementation/publication of this three-action foundation with fake-dependency tests and no positive create mutation.

Checkpoint 426 reconciles the complete native GitHub parity implementation boundary. Runtime Bridge now implements all 89 captured native action names and all 41 native write names, with fresh-host schema coverage 89/89 and positive-live action coverage 84/89: 47/48 reads plus 37/41 writes. The five action-level positive-live gaps are genuine fixture/environment gates: `download_user_content`, dismiss-review, auto-merge, reviewer request and reviewer removal. Three option/host semantics remain explicitly fail-closed or separate: `list_installations(manageable_only=true)`, repository search-index enrichment, and Enterprise repository-URL routing; live preview.38 reconfirmed the two `GITHUB_PARITY_OPTION_NOT_QUALIFIED` guards and `GITHUB_ENTERPRISE_NOT_QUALIFIED`. Exact provider-wrapper wire parity remains conservatively 0/89 because native machine-readable output schemas, structured error schemas, normalized result envelopes and several wrapper-only precedence/pagination semantics remain hidden. This is an evidence limitation, not an implementation count. The native-parity implementation phase is therefore structurally complete under current evidence/environment, with residual gates left explicit rather than forced. Research 123 remains active because it was already expanded beyond parity to selected GitHub capabilities. The next boundary returns to that extension track with read-only bounded design of Repository Administration(write), the strongest previously selected extension family and an explicit owner requirement.

Checkpoint 425 closes positive-live qualification of `github.update_pull_request` and `github.merge_pull_request` on a new disposable base/head/PR fixture completely isolated from PR #84 and `main`. Both disposable branches were created from exact preflight main SHA `3c7bcc51b10bfac787aee4b12cc3cd0f6b553400`; the head fixture commit is `4e73cdb991870dbd99c3f9d5733171a802813ba4`. PR #85 targeted disposable base `r123/update-merge-base-20260909` from disposable head `r123/update-merge-head-20260909`. `github.update_pull_request` ran exactly once and changed title/body metadata only. After read-only head/base confirmation, `github.merge_pull_request` ran exactly once with required `expected_head_sha=4e73cdb991870dbd99c3f9d5733171a802813ba4` and returned `merged=true`, merge SHA `c409925a1589da7976628f6fc2534f13481a4ba0`. Postflight shows PR #85 closed/merged, disposable base advanced to that SHA, disposable head unchanged, and `main` still exactly `3c7bcc51b10bfac787aee4b12cc3cd0f6b553400`. No retry or mutation uncertainty occurred, and PR #84 was not replayed. Native-write positive-live coverage is now 37/41, with PR/review at 15/19. The four remaining write positive-live gaps are environment-gated rather than implementation gaps: dismiss-review requires a genuine dismissible second-reviewer fixture, auto-merge requires repository-level auto-merge configuration, and reviewer request/removal require a known second reviewer or team. The next boundary is read-only Research 123 reconciliation of all remaining parity/qualification gaps.

Checkpoint 424 activates Runtime Bridge preview.38 at 153 public tools / 89 GitHub tools and removes two avoidable PR/review mutation-uncertainty paths without changing caller schemas. Dismiss-review scope now resolves review database ID/state, rejects anything other than APPROVED/CHANGES_REQUESTED before mutation, revalidates scope/state inside the serialized PR mutation boundary, and uses GitHub's fixed REST dismissal endpoint so classified HTTP validation errors remain non-uncertain. Auto-merge now rejects repository `allow_auto_merge != true` before GraphQL mutation. Focused PR/review tests pass 4/4; Runtime Release `prepare` is the authoritative complete regression gate and succeeded. Immutable release `github-pr-review-semantic-hardening-v1` is bound to local-runtime head `7eda5dbce805dd4452d4ec6a667ee39e4e45fc74` and manifest `7edebf36973d619e808773b74ddc5a37c96c79830db5dd7ebb411b219892cb0c`; publication/restart succeeded without recovery and postactivation verify reports zero mismatches. Live no-write calls on PR #84 now return deterministic `GITHUB_PR_REVIEW_NOT_DISMISSIBLE` for its COMMENTED review and `GITHUB_AUTO_MERGE_DISABLED` for repository configuration, both `retryable=false`, `mutationUncertain=false`, with no underlying mutation dispatch. No PR #84 mutation was replayed. Positive-live coverage remains 35/41; update/merge are ready for a separately authorized fresh disposable PR fixture, while dismissal/reviewer request/removal and auto-merge remain environment-gated.

Checkpoint 423 classifies the six remaining PR/review positive-live gaps through read-only environment and semantic analysis without resuming PR #84. All twelve installed repositories report `allow_auto_merge=false`, so auto-merge has no currently valid installed positive fixture without non-parity repository-setting mutation. All discovered pull requests across the installed surface are authored by `shakaarlatief`; no independent second reviewer/bot/team fixture exists, and bounded generic fetch intentionally refuses collaborator/team enumeration families. GitHub documentation confirms that dismissal applies to approved/rejected reviews, explaining the prior COMMENTED-review failure. The current Runtime Bridge should therefore harden dismissal by resolving review state/database ID, rejecting non-dismissible states before mutation, and using the fixed REST dismissal endpoint so classifiable validation errors stay non-uncertain. Auto-merge should also fail deterministically before GraphQL when repository `allow_auto_merge` is false. `update_pull_request` and `merge_pull_request` can be qualified independently on a fresh disposable base/head/PR without touching PR #84. Thus two actions are immediately isolatable and four remain environment-gated; the current environment can reach at most 37/41 successful positive-live writes without changing repository configuration/collaborator relationships outside the captured parity surface. The next boundary is preview.38 semantic guard hardening only.

Checkpoint 422 closes positive-live qualification of both GitHub Actions rerun mutations. After fresh read-only state checks, `github.rerun_failed_workflow_run_jobs` was invoked exactly once on Knowledge map integrity run `33501596538`; it returned `accepted=true`, and read-only postflight observed `run_attempt=2` with new job `102615182694`. `github.rerun_workflow_job` was then invoked exactly once on independent failed Ubuntu job `99836356121` from Current routing consistency run `33501718088`; it returned `accepted=true`, and postflight observed `run_attempt=2` with newly executed target job `102615588321`. Neither mutation returned uncertainty and neither was retried. Both selected workflows were already preflight-qualified as `permissions: contents: read` validation-only workflows, so the expected external effect was limited to Actions compute and run/job attempt state. The Actions rerun family is now 2/2 through implementation, local wire, fresh-host schema/guard and positive-live layers. Overall native write positive-live coverage is now 35/41. The remaining six actions are all PR/review actions and remain governed by the preserved uncertainty boundary: dismissal blocked after `mutationUncertain=true`, auto-merge configuration-gated, reviewer request/removal fixture-gated, and update/merge not yet invoked after the stop. No PR/review mutation was resumed or replayed. The next boundary is resolution design for those six remaining actions.

Checkpoint 421 completes read-only positive-live fixture preflight for the two Actions rerun mutations. Two distinct historical failed validation workflows were selected so one rerun cannot alter the other fixture before its call. `github.rerun_failed_workflow_run_jobs` is assigned Knowledge map integrity run `33501596538`, which is completed/failure at historical SHA `a2f215fe66c881049e0456e7ecc28df4ae54aad7` and contains exactly one failed job `99835969925`. `github.rerun_workflow_job` is assigned Current routing consistency run `33501718088`, completed/failure at SHA `8c602f79d0137ac0b0155ed67f8d74246324b07a`, targeting failed Ubuntu job `99836356121`. Exact historical workflow YAML for both fixtures declares only `permissions: contents: read` and performs checkout plus local validation commands; no repository mutation, deployment, release, package publication, issue/PR mutation or external-service write step is present. No positive rerun occurred. A later positive-live test requires explicit owner authorization, fresh read-only state checks before each call, exactly one attempt per mutation, immediate stop on `mutationUncertain=true`, and read-only postflight. The independent PR/review family remains stopped at 13/19 after the preserved dismissal uncertainty.

Checkpoint 420 closes the refreshed ChatGPT host schema/guard gate for both preview.37 GitHub Actions rerun mutation actions. In a fresh disposable host, `github.rerun_failed_workflow_run_jobs` and `github.rerun_workflow_job` both projected with strict object schemas, `additionalProperties=false`, bounded repository strings, and positive integer run/job IDs. No caller-selected credential/token, GitHub host/endpoint, arbitrary HTTP/GraphQL/transport authority, filesystem/process authority or permission selector was exposed. Exactly two invalid ID-zero calls were attempted and both failed host-side minimum validation before Runtime Bridge/GitHub dispatch, with zero retries, zero mutation-uncertain outcomes and zero workflow/job changes. Combined with Checkpoint 419, all 89 captured GitHub action names are implemented and the final two names now have local-wire plus fresh-host schema evidence. Actions rerun positive-live remains 0/2; the next step is read-only fixture preflight only. The independent PR/review boundary remains stopped at 13/19 after the preserved dismissal mutation-uncertainty result. Exact native-wrapper parity remains conservatively 0/89.

Checkpoint 419 reaches full implementation-name coverage of the captured GitHub connector inventory. Runtime Bridge preview.37 is live at 153 public tools / 89 GitHub tools and adds the final two native action names, `github.rerun_failed_workflow_run_jobs` and `github.rerun_workflow_job`. Both use installation-derived repository authority, fixed GitHub Actions REST endpoints, positive integer IDs, deterministic preflight state checks and mutation-aware single-attempt transport. Focused Actions rerun tests pass 4/4; broad reconstructed qualification passes 48 read schemas, 8 repository Git/content writes, 12 issue writes, 19 PR/review writes, the two rerun writes, and `PUBLIC_SURFACE_REGISTRATION=PASS tools=153`. Immutable release `github-actions-rerun-mutations-v1` is bound to local-runtime head `f29241ce1be4368fcd956c197e5d976eef6f15b8` and manifest `eb8393734f0d9af0ebd33ea32e7b6cbd950bbe27f8c7e540a62e10ca4f314eaf`; publication and restart succeeded without recovery and postactivation verify reports zero mismatches. Live MCP `tools/list` reports exactly 89 GitHub tools and both new rerun names. Invalid run/job ID zero probes fail during input validation before GitHub dispatch, so no workflow rerun occurred. Protected authorization remains healthy. Runtime Bridge now implements all 89 captured action names and all 41 native write names. This is not exact native-wrapper parity: hidden native output envelopes and deliberate Runtime Bridge narrowings remain explicit, so exact parity rows closed remain 0/89. The PR/review positive-live boundary remains stopped at 13/19 after the preserved mutation-uncertain dismissal result, with no replay. Actions rerun positive-live remains 0/2. The current persistent host predates preview.37, so the next gate is one refreshed disposable fresh-host schema/guard qualification of the two rerun actions before any positive workflow rerun.

Checkpoint 418 preserves the owner-authorized disposable PR/review positive-live sequence through the first explicit Runtime Bridge mutation-uncertainty stop. Thirteen of nineteen PR/review mutations are positive-live qualified on disposable PR #84 between disposable branches; `main` remains unchanged. The successful subset includes create PR, draft/ready transitions, PR labeling, PR reaction add/remove, COMMENT review creation with inline review comment, review-comment update, review-comment reaction add/remove, review-comment reply, and review-thread resolve/unresolve. The first long harness timed out externally and was reconstructed read-only without replaying ambiguous mutations; a fresh supporting review/thread was used for thread-state actions. `github.dismiss_pull_request_review` was then invoked once on a fresh COMMENTED review and returned `GITHUB_GRAPHQL_ERROR`, `retryable=false`, `mutationUncertain=true` with error `Can not dismiss a commented pull request review`. Readback still shows COMMENTED, but the uncertainty contract stopped the sequence: no dismissal retry and no later PR/review mutation. Six actions remain positive-live: dismissal blocked at uncertainty, auto-merge config-gated because `allow_auto_merge=false`, reviewer request/removal fixture-gated because no safe second reviewer was resolved, and update/merge not yet invoked after the stop. PR #84 remains open/unmerged and `main` is unchanged. The stop does not block independent implementation of the final two unimplemented Actions rerun names, so that becomes the next boundary. Runtime Bridge remains at 87/89 implemented action names and 39/41 implemented writes. Exact native-wrapper parity remains conservatively 0/89.

Checkpoint 417 closes the fresh-host schema/guard gate for all nineteen preview.36 PR/review mutation actions. In a refreshed disposable ChatGPT host, all nineteen exact names projected and all nineteen caller-visible schemas were reported sufficiently bounded, with no caller-selected secret/credential authority, arbitrary transport/host/process authority or secret value exposure. Exactly three invalid no-write calls then passed with zero retries and zero mutation-uncertain outcomes: unsupported PR reaction `party` was rejected by the eight-value reaction enum, an empty reviewer request was rejected by the non-empty reviewer/team semantic guard, and `merge_pull_request` with `expected_head_sha=not-a-sha` was rejected by the hexadecimal 7..64-character schema before any merge dispatch. The validation diagnostics directly exposed `additionalProperties=false` for the reaction and merge contracts and confirmed `expected_head_sha` is required for merge. No GitHub mutation occurred. Positive-live PR/review coverage therefore remains 0/19. The next gate is deliberate disposable PR/review fixture design rather than an indiscriminate 19-write sequence, because merge, draft/ready, auto-merge, review dismissal, reviewer request/removal and thread state transitions have distinct prerequisites and risk. Runtime Bridge implements 39/41 native write names and 87/89 captured native GitHub action names; only two Actions rerun writes remain unimplemented. Exact native-wrapper parity remains conservatively 0/89.

Checkpoint 416 preserves live Runtime Bridge preview.36 at 151 public tools / 87 GitHub tools and closes local implementation/wire qualification for all nineteen captured PR/review mutation action names. The immutable release `github-pr-review-mutations-v1` is bound to local-runtime head `70dd9d028e20d607e58aa1012b1b961125e6213e`; publication and restart succeeded without recovery, postactivation verification returned zero mismatches, and protected GitHub authorization remains stored/authorized/non-expired. Focused tests pass all nineteen fixed REST/GraphQL mutation routes, fail-closed semantic guards, exact expected-head protection for merges and single-attempt handling of mutation uncertainty. The broad reconstructed surface passes at 151 tools with 48 read schemas, eight repository Git/content writes, twelve issue writes and nineteen PR/review writes. Two live local no-write probes rejected unsupported PR reaction `party` and an empty reviewer request before GitHub dispatch. No positive PR/review mutation occurred. The persistent `chatgpt-21` projection predates preview.36, so the next gate is one refreshed disposable fresh-host schema/guard qualification of all nineteen exact PR/review tools. Runtime Bridge now implements 39/41 native write names and 87/89 captured native GitHub action names overall; only two Actions rerun writes remain unimplemented. Exact native-wrapper parity remains conservatively 0/89.

Checkpoint 415 closes the second native write family with a separately authorized positive-live disposable issue qualification. All twelve preview.35 issue mutation actions succeeded exactly once on new issue #83 in `shakaarlatief/autonomous-data-science-system`; no mutation result was uncertain and no mutation call was retried. The sequence created issue #83, added/removed assignee `shakaarlatief`, added/removed label `bug`, created comment `5605536681`, updated it, added reaction `413975888`, removed it, locked/unlocked the conversation, then updated and closed the issue as completed. Postflight confirms issue closed/completed, assignees and labels empty, conversation unlocked, updated comment present and reaction absent. The positive label mutation itself establishes that `bug` exists; an earlier unauthenticated direct label-list attempt was blocked by the local command sandbox and caused no GitHub interaction. Issue #83 remains intentionally as a closed qualification artifact because issue deletion is outside the captured native action surface. Repository Git/content plus issue families are now 20/41 native writes implemented, fresh-host schema-qualified and positive-live. The next implementation family is all nineteen PR/review mutations; two Actions rerun mutations remain after that. Exact native-wrapper parity remains conservatively 0/89.

Checkpoint 414 closes the fresh-host schema/guard gate for all twelve preview.35 issue mutation actions. In a refreshed disposable ChatGPT host, all twelve exact names projected and all twelve caller-visible contracts were sufficiently bounded; the owner supplied the detailed projection showing bounded repository/name/text/list/integer inputs, the exact reaction/lock/state/state-reason enums, and no credential, token, host, arbitrary endpoint/method/header, GraphQL, permission-profile, transport, filesystem or shell authority. The host did not separately expose `additionalProperties` for most actions and no separate titles/annotations were visible; those absences are preserved rather than inferred. Exactly two authorized invalid calls then reproduced the no-write guards with no retry: `add_reaction_to_issue_comment` rejected reaction `party` at host schema validation against the eight-value enum, and `update_issue` with `state_reason=completed` and no state returned `state_reason requires state`. No positive issue mutation occurred. The twelve issue writes are therefore implemented/live and fresh-host schema-qualified while positive-live remains 0/12. The next gate is one separately authorized disposable positive issue sequence in which all downstream issue/comment/reaction IDs are derived from actual results and any uncertain mutation stops without replay. Because the captured native surface exposes no issue-delete action, the final qualification issue should be closed and retained. Runtime Bridge implements 20/41 native writes; 21 remain: nineteen PR/review plus two Actions rerun. Exact native-wrapper parity remains conservatively 0/89.

Checkpoint 413 live-qualifies the second mutation implementation family without performing a positive issue write. Private local-runtime head `6f1651a0c5258f1d9185962798f43babdf7ba018` preserves immutable release `github-issue-mutations-v1`, live as `0.1.1-preview.35-github-issue-mutations` with 132 public tools / 68 GitHub tools: 48 reads, eight repository Git/content mutations and all twelve issue mutations. The focused issue mutation integration test passes fixed installation-scoped REST behavior, no-write guards, same-issue serialization and uncertain-mutation single-attempt semantics; reconstructed public-wire qualification reports `GITHUB_ISSUE_MUTATION_WIRE_SCHEMA=PASS tools=12` and `PUBLIC_SURFACE_REGISTRATION=PASS tools=132`. Runtime Release preparation succeeds with manifest `66802022e3e8375b0eab14b395d74462de6f8e067c4996ee14d190d642c354ea`; publication `rm_cfe9e661da3d6035b6f4f7273089a304` and restart `rm_0fc4891d51a6ec8c18932ed772000b9d` succeed without recovery; postactivation verification reports zero mismatches. Fresh local MCP tools/list confirms all twelve exact issue-mutation names. Two deliberate no-write probes are rejected at input validation before handler/transport dispatch: unsupported reaction `party` and `update_issue` with `state_reason=completed` but no state. No issue/comment/reaction/label/assignee/lock mutation occurs. Immediately after restart the protected access token was expired but refresh authorization remained valid; one safe read-only login request exercised normal refresh and subsequent metadata reports stored/authorized, access and refresh non-expired, no refresh recommendation. No reconnect or authorization reset occurred. The existing chat is stale for preview.35 projection, so the next gate is a refreshed fresh-host schema/guard qualification of the twelve issue mutations before any disposable positive issue-mutation sequence. Runtime Bridge now implements 20/41 native writes; 21 remain: nineteen PR/review plus two Actions rerun. Exact native-wrapper parity remains conservatively 0/89.

Checkpoint 412 closes the first native write family with a separately authorized positive-live disposable mutation qualification. All eight preview.34 repository Git/content mutation actions succeeded exactly once on `shakaarlatief/autonomous-data-science-system`, restricted to branch `r123/runtime-bridge-g3-qualification-20260909`; no mutation result was uncertain and no mutation call was retried. The Contents path was created, updated using the exact returned content SHA, then deleted using the next returned content SHA; the deletion commit restored the exact original main tree. The raw Git sequence then created blob `9461d695574713a653f90ffd16b2c77bf5c98ee0`, tree `de0b463f9d36c6a13ea395d293e29e4b5d90b4da`, commit `88e70054a93956b469f5533ffd9949d3a1c72e6f`, and moved only the disposable branch with `force=false`. Postflight readback confirms the temporary Contents path is absent, the raw qualification path is present with exact expected content, the branch is ahead of main by four and behind by zero, and `main` remained `3c7bcc51b10bfac787aee4b12cc3cd0f6b553400` before and after. A first Node harness attempt failed parsing MCP initialize before any `tools/call`; the successful harness reverified branch/path absence before the first mutation, so no uncertain write was retried. The branch remains intentionally as a qualification artifact because branch deletion is outside the captured native 89-action surface. Repository Git/content mutations are now 8/8 implemented, fresh-host schema-qualified and positive-live. The next implementation family is the twelve issue mutations. Exact native-wrapper parity remains conservatively 0/89.

Checkpoint 411 closes the fresh-host schema/guard gate for all eight preview.34 repository Git/content mutation actions. In a refreshed disposable ChatGPT host, all eight exact names projected; the owner reports every caller-visible contract remained bounded, with no genericization/truncation sufficient to obscure caller authority and no credential, token, host, arbitrary endpoint/method/header, GraphQL, ref-namespace, permission-profile, transport, filesystem or shell authority. The full field-by-field Part A transcript was not recopied into this persistent chat, so Validation 167 remains the exact local MCP wire-schema authority rather than reconstructing details. Two exactly-once non-writing guard calls reproduced the local behavior through the fresh host: `github.create_branch` with both SHA and base-ref returned `GITHUB_BRANCH_BASE_INVALID`, and `github.update_ref(force=true)` returned `GITHUB_FORCE_REF_UPDATE_NOT_QUALIFIED`; both were `retryable=false`, `mutationUncertain=false`, `githubRequestId=null`, and no GitHub mutation occurred. The first eight writes are therefore implemented/live and fresh-host schema-qualified, while positive-live mutation remains 0/8. The next gate is a separately authorized disposable positive-mutation qualification on a dedicated branch with exact SHA chaining, `force=false`, no `main` movement and no retry after uncertain mutation. The captured native connector exposes no branch-delete action, so test-branch cleanup/disposition must be decided explicitly rather than silently using extra authority. Exact native-wrapper parity remains conservatively 0/89.

Checkpoint 410 live-qualifies the first GitHub mutation implementation family without performing a positive GitHub write. Private local-runtime head `fc86cdc827d8c6850539e3f94052d6209f4152f4` preserves rollback-compatible immutable release `github-repository-git-mutations-v2`, live as `0.1.1-preview.34-github-repository-git-mutations` with 120 public tools: 48 GitHub reads plus eight repository Git/content mutation tools. The first immutable v1 publication is preserved as a failed `RUNTIME_RELEASE_PUBLICATION_ROLLBACK_FAILED` operation; its original forward failure cause is not exposed and remains unobserved. Post-failure target verification reported ten target mismatches, showing preview.34 was not left installed; the subsequent successful v2 publication then verified the exact expected preview.33 baseline before applying the corrected target. Inspection of the release publisher exposed a structural rollback hazard: it reruns the target regression list after restoring previous source, so target-only add-mode regression paths are not rollback-compatible. v2 keeps the focused mutation test independently preserved/qualified but uses only regression paths available on both target and restored previous source. v2 publication, restart and postactivation verification pass with zero mismatches and no recovery. Direct loopback health reports preview.34 / 120 tools; fresh stateless MCP tools/list reports 120 total / 56 GitHub tools and all eight mutation names with strict bounded schemas. Live non-writing guards also pass: conflicting create-branch SHA/base-ref returns `GITHUB_BRANCH_BASE_INVALID`, and update-ref `force=true` returns `GITHUB_FORCE_REF_UPDATE_NOT_QUALIFIED`; both are non-retryable, not mutation-uncertain semantic rejections. Protected GitHub authorization remains healthy. No branch, blob, tree, commit or repository content was created, updated or deleted. The already-open `chatgpt-21` host remains stale for the new mutation names, so the next gate is one refreshed fresh-host schema qualification of the eight mutation-sensitive actions before any disposable positive live GitHub mutation is considered. Exact native-wrapper parity remains conservatively 0/89.

Checkpoint 409 closes the complete GitHub read phase in a refreshed disposable ChatGPT host. All 26 final preview.33 read actions projected simultaneously with bounded caller contracts; the host did not separately render `additionalProperties=false`, titles or annotations, so those exact host-visible fields are not overclaimed. Calls 2-26 all succeeded exactly once against canonical Research 123 fixtures. `github.download_user_content` intentionally used a non-allowlisted hostname and returned the expected bounded rejection, so its positive-live path remains `FIXTURE_GATED` rather than failed. The canonical issue #82, PR #81, workflow run `32815726116`, job `97703468768`, and non-expired artifact `9553693015` were all readable; PR discussion/reviews/threads, changed filename, Actions logs/steps/artifacts/jobs, combined status, reactions, recent issues/PRs and searches succeeded. `github.download_workflow_artifact` returned compact metadata plus a reusable host-materialized resource rather than embedding ZIP bytes/base64. The 112-tool / 48-GitHub-read surface showed no fresh-host scaling problem. Read capability is now fresh-host qualified at 48/48 action names, with 47/48 positive-live and only `download_user_content` positive-live fixture-gated. No secret or GitHub mutation occurred. The remaining native inventory is 41 writes, grouped into repository Git/content (8), issues (12), PR/reviews (19), and Actions reruns (2). The next implementation family is the eight repository Git/content mutations behind bounded schemas and synthetic regressions; no live GitHub mutation is authorized by this checkpoint. Exact native-wrapper parity remains conservatively 0/89 because hidden native output/semantic gaps remain explicit.

Checkpoint 408 live-qualifies implementation of every captured native GitHub read action. Private local-runtime head `3be4bfb1bdabecd1833aa42844e7047f0a34f787` preserves corrected immutable release `github-all-readonly-expansion-v2`, live as `0.1.1-preview.33-github-all-readonly-resource-links` with 112 public tools, 48 `github.*` read-only tools, six changed release files, sixteen regressions, one runtime dependency and zero postactivation source mismatches. The preceding preview.32 release first activated all 26 remaining reads and produced 25/26 positive local live successes against bounded canonical public fixtures; `github.download_user_content` remains positive-live-fixture-gated because no suitable authorized private-user-images URL was found in the canonical public material. Preview.32 also exposed a quality defect before host qualification: workflow artifact bytes were embedded as base64 instead of using the native reusable-file-reference semantics. Preview.33 corrects both GitHub download actions to compact MCP `resource_link` results backed by bounded ephemeral server-owned resources; a separate `resources/read` reproduced the exact 322,868-byte canonical artifact with matching SHA-256 and no bytes/base64 in the tool result. Health/ready pass and protected GitHub authorization remains stored, authorized and non-expired. This persistent chat still has a stale projection for the 26 additions, so the next gate is one refreshed fresh disposable host qualification. Fresh-host read coverage is currently 22/48; after that gate the only unimplemented native inventory will be 41 write actions. Exact native-wrapper parity remains conservatively 0/89.

Checkpoint 407 closes the preview.31 G2 fresh-host gate. In a disposable fresh host, all eleven G2 actions projected with bounded read-only schemas and all eleven were invoked exactly once successfully against the canonical ADS repository. `github.fetch_blob` used a blob SHA derived from the preceding canonical file read; installed-repository searches kept hidden search-index enrichment disabled; zero-result `github.search` and `github.search_commits` responses were preserved as successful bounded application responses without retry. No credential secret or GitHub mutation occurred. Combined G1 plus G2 fresh-host coverage is now 22 public GitHub read-only tools. The captured native inventory contains 48 read actions total, leaving 26 read actions. Because authorization, installation-derived scope, REST/GraphQL transport, release lifecycle, MCP projection and two representative read-only families are now repeatedly qualified, Research 123 deliberately increases batch size: the next implementation phase targets all 26 remaining issue, PR/review, Actions/CI and content-download reads in one larger read-only release family, with domain-specific regression/live evidence preserved internally. Mutations remain a separate later risk boundary. Exact native-wrapper parity remains conservatively 0/89 because hidden native outputs and unresolved option semantics are still not inferred.

Checkpoint 406 live-qualifies the Research 123 G2 read-only repository fetch/search/branch/commit/file/blob/compare implementation on Runtime Bridge preview.31. Private local-runtime head `b446a3fc2ff480e66acc81ddad56f12bb871feca` preserves corrected immutable release `github-g2-readonly-expansion-v2`, targeting `0.1.1-preview.31-github-g2-readonly`, 86 public tools, 22 GitHub read-only tools, ten release files, sixteen regressions and one exact runtime dependency. The earlier v1 path remains preserved: its first 17-regression manifest exceeded the existing release bound; after correction to sixteen, publication failed a new public-wire regression because the test incorrectly expected no serialized enum for nullable commit-search sort. The product schema was correct, the test was repaired, and immutable prepared-state conflict correctly forced a new v2 release ID rather than rewriting prepared state. Corrected v2 publication `rm_59bfec18a65b6d64e35b5ad003f7463d` succeeded; restart `rm_ad739f5850d15cd2b7eb267d6ca25c0b` activated preview.31 without recovery; postactivation verification is `verified` with zero mismatches. Protected GitHub authorization remains configured, stored, authorized and non-expired. The eleven G2 additions are compare/fetch/blob/commit/file plus code, branch, commit and repository search. This persistent `chatgpt-21` host still does not project the new G2 names, reproducing AB-008 same-chat staleness, so the next gate is a fresh disposable ChatGPT host discovery/schema/live-read qualification. No GitHub mutation occurred and exact native-wrapper parity remains conservatively 0/89.

Checkpoint 405 closes the G1 fresh-host gate by composing the preserved Validation 161 evidence with a separately authorized targeted recheck of the single unresolved action. `github.list_installed_accounts` remained projected and the targeted call succeeded with `schemaVersion=codexless.github-readonly.v1`, account count 1, and personal User `shakaarlatief` present; no credential secret or GitHub mutation appeared. The original Validation 161 connector failure `mcp_network_error / network_error / Connection failed.` remains preserved and is not rewritten into an initial PASS. Combined G1 host coverage is now 7/7: six successful live reads from the original qualification plus the successful installed-accounts recheck. No Plugin rescan, Runtime Bridge restart or authorization change was required. Known `manageable_only=true`, `include_search_index_status=true`, Enterprise repository-URL and hidden native output gaps remain open, so exact native-wrapper parity stays conservatively 0/89. Research 123 now advances to G2 read-only compare/fetch/blob/commit/file plus code/branch/commit/repository/installation-scope search.

Checkpoint 404 preserves the first seven-action G1 fresh-host qualification as an explicit FAIL with a sharply localized next discriminator. All seven preview.30 actions projected with bounded host schemas, but only six of seven required live reads succeeded. The sole failure was `github.list_installed_accounts`, which returned connector transport error `mcp_network_error / network_error / Connection failed.` before any application result; the disposable qualification correctly made no retry. The other six fresh-host calls succeeded read-only: the canonical ADS repository resolved, collaborator permission is `admin`, both repository-listing routes returned 12 repositories with the canonical ADS repository present, and organization memberships/organizations both returned zero. No secret or arbitrary transport authority appeared and no GitHub mutation occurred. After this FAIL was supplied, this persistent conversation performed no host retry. Protected authorization metadata remained healthy, and a fresh stateless loopback MCP invocation of exactly `github.list_installed_accounts` succeeded with count 1 and personal User `shakaarlatief` present. This rules out treating the fresh-host error as evidence of broken preview.30 action logic or stored authorization, while not proving the exact host/tunnel root cause. The next gate is now one targeted host requalification of only `github.list_installed_accounts`; the six successful fresh-host calls do not need to be repeated, and no Plugin rescan, runtime publication or authorization change is currently justified.

Checkpoint 403 live-qualifies the remainder of the Research 123 G1 read-only identity/account/repository-discovery/permission slice on Runtime Bridge preview.30. Private local-runtime head `7af8600dd2213d2fc2e5aca3b3ef32b8fafeacc6` preserves immutable release `github-g1-readonly-expansion-v1`, targeting `0.1.1-preview.30-github-g1-readonly`, 75 public tools, nine release files and one exact runtime dependency. The first manifest draft correctly failed the Runtime Release v2 16-regression ceiling at 18 entries; the contract was not widened and the corrected 16-regression bundle prepared successfully. A conservative private secret-scan false positive on a synthetic fixture was likewise repaired in the fixture rather than by weakening secret detection. Prepublication verification reported the expected nine mismatches against preview.29; publication operation `rm_bc3ee2e4f09d12ed8f92af6686663961` succeeded without recovery; restart operation `rm_9c321da1381ec4ebd69657441d939be6` activated preview.30 without recovery; and postactivation verification returned zero mismatches. Protected GitHub authorization survived restart as configured, authorized, stored and non-expired. A fresh stateless loopback MCP `initialize -> tools/list` returned exactly 75 tools with eleven `github.*` actions. The seven additions are `github.get_repo`, `github.get_repo_collaborator_permission`, `github.list_installed_accounts`, `github.list_repositories`, `github.list_repositories_by_affiliation`, `github.list_user_org_memberships`, and `github.list_user_orgs`. All seven were then invoked exactly once read-only against live GitHub: the canonical public ADS repository resolved successfully; collaborator permission for `shakaarlatief` is `admin`; one personal installed User account is present; owner-filtered and owner-affiliation repository listings each returned 12 repositories with the canonical ADS repository present and no continuation; and both organization-list calls returned count zero. Unrelated private repository names were not printed or preserved. No GitHub mutation or credential exposure occurred. `manageable_only=true`, `include_search_index_status=true`, Enterprise-host repository URL routing, and hidden native result envelopes remain explicitly unqualified, so exact native-wrapper parity stays conservatively 0/89. The active MCP contains all eleven GitHub actions, but this persistent `chatgpt-21` projection still exposes only the earlier four, reproducing AB-008 same-chat staleness. The next gate is a refreshed fresh disposable ChatGPT qualification of the seven new G1 actions before G2 begins.

Checkpoint 402 closes the fresh-host qualification gate for the first four public GitHub read-only foundation actions. The project owner supplied the completed disposable-chat qualification, whose final marker is `GITHUB_READONLY_FOUNDATION_FRESH_HOST=PASS`. All four exact actions projected through the refreshed ChatGPT host and all four bounded read-only invocations succeeded in the required order. `github.get_profile` and `github.get_user_login` both resolved authenticated login `shakaarlatief`; `github.list_installations(manageable_only=false)` returned one personal User installation with `repositorySelection=all`; and `github.list_repositories_by_installation(page_size=20,page_offset=0)` returned all 12 installation-authorized repositories with `hasMore=false` and confirmed `shakaarlatief/autonomous-data-science-system` is in scope. The fresh-host result reports bounded schemas and no caller-selected token, credential, GitHub host, URL, REST endpoint, GraphQL document, HTTP method/header, permission profile or equivalent arbitrary transport authority. No access/refresh token, device code, client secret, Authorization header or credential-store payload appeared, and no GitHub mutation occurred. The owner did not reproduce the installation ID or unrelated private repository names. The exact Part A schema transcript was not copied into this persistent chat, so Validation 157 remains the exact local MCP schema evidence while Validation 159 preserves fresh-host projection/boundedness and live-read success. The known `manageable_only=true` native-wrapper semantic gap remains open, so exact native parity remains conservatively 0/89. Research 123 now advances to the remaining G1 identity, account, repository-discovery and permission read-only actions before G2 read/search expansion.

Checkpoint 401 closes the recurring owner-manual semantic Git unstage gap without displacing active Research 123. Private local-runtime head `ffb0356acb0dc69024146869c5bebe0ee76de5a3` preserves immutable release `semantic-git-transactional-commit-v1`; publication passed the bounded regression matrix, restart activated `0.1.1-preview.29-semantic-git-transactional-commit` without recovery, and postactivation verification reports 68 tools, one runtime dependency and zero mismatches. `codex.git_commit_paths` still requires an initially empty index, but if its own exact staging is followed by a definite guarded failure and HEAD remains unchanged, it now restores only the declared staged scope, verifies an empty index, and preserves working-tree edits. Cleanup uncertainty fails visibly as `GIT_COMMIT_PATHS_ROLLBACK_FAILED`; an uncertain commit result with a changed HEAD is never auto-rolled back. A focused trailing-whitespace regression passed, then the live public tool reproduced the same failure and returned `indexRestored=true`, `rollbackAttempted=true`, with HEAD unchanged and the working-tree validation file preserved. The corrected preservation commit proceeded without an owner-side `git restore --staged -- .`. No general reset/unstage authority was added. The Research 123 next boundary therefore returns to the pre-existing fresh-host qualification of the four live GitHub read-only foundation tools.

Checkpoint 400 live-qualifies the first public `github.*` read-only foundation. Private local-runtime head `a18983d2b2199f350d07664cfe91dbf013e2df3c` preserves immutable release `github-readonly-foundation-v3`; publication succeeded after migrating the historical G0 zero-public-action regression, bounded restart activation succeeded without recovery, and postactivation verification reports `0.1.1-preview.28-github-readonly-foundation`, 68 tools, one runtime dependency and zero mismatches. Direct local MCP `tools/list` exposes `github.get_profile`, `github.get_user_login`, `github.list_installations`, and `github.list_repositories_by_installation`; all four were live-invoked read-only against the stored GitHub App user authorization. The viewer GraphQL query resolved authenticated login `shakaarlatief`; installation enumeration returned one personal installation with `repositorySelection=all`; repository enumeration returned 12 in-scope repositories and confirmed the canonical public ADS repository is present. No token or private repository-name list was preserved. Exact native parity remains 0/89 because `list_installations(manageable_only=true)` deliberately fails closed as `GITHUB_PARITY_OPTION_NOT_QUALIFIED` until the native managed-account filter semantics are evidenced. The current `chatgpt-21` connector projection still omits all four new names despite the live 68-tool MCP surface, so the next boundary is Plugin refresh plus fresh-chat host schema and live-read qualification.

Checkpoint 399 closes the live GitHub user-authorization bootstrap. Owner evidence confirms Device Flow remained enabled on the registered App, and the earlier HTTP 404 was localized instead to a transcription error in the non-secret Client ID. GitHub's public App record supplied the corrected Client ID, direct device-code discrimination changed from 404 with the superseded value to 200 with the live value, and immutable release `github-client-config-v4` activated `0.1.1-preview.27-github-client-id-correction` with 64 tools, one runtime dependency and zero mismatches. Exactly one corrected Runtime Bridge device authorization then completed successfully. Follow-up `codex.github_authorization metadata` now reports `authorized=true`, `storedAuthorization=true`, non-expired access/refresh lifetimes and no exposed credential values. The downloaded PEM had already been deleted as confirmed by the owner; no Client secret exists. Public `github.*` parity actions remain 0, so the next boundary is authenticated identity, installation-scope and first read-only GitHub action qualification.

Checkpoint 398 records successful installation of the live `Codexless Runtime Bridge` GitHub App on personal account `shakaarlatief` with **All repositories** selected. Owner-supplied GitHub evidence shows the App as `Installed now` and the repository-access selector at All repositories, matching the clarified broad personal-repository target. The installation ID has not yet been captured. Because GitHub required an App private key before installation, a private key was generated solely to cross that gate; Runtime Bridge still does not use App-JWT/private-key authority. The immediate security boundary is therefore local deletion of the downloaded `.pem` private key before authorization proceeds. No Client secret has been generated, no user/refresh token exists, and live GitHub device authorization remains unstarted. After PEM deletion is confirmed, the next technical step is fixed server-owned configuration of non-secret Client ID `Iv23lirgmw82wV0SGTWn`, followed by a metadata-only qualification requiring `configured=true` and `storedAuthorization=false`.

Checkpoint 397 records the first live GitHub App registration. GitHub created `Codexless Runtime Bridge` under owner `shakaarlatief` with App ID `4881901`, Client ID `Iv23lirgmw82wV0SGTWn`, and slug `codexless-runtime-bridge`. The App is registered but not yet installed and no client secret, private key, access token, refresh token or device code exists. GitHub's post-registration UI now exposes an empirical installation gate requiring a private key before the App can be installed. This corrects the earlier no-private-key bootstrap assumption without changing Runtime Bridge's selected user-token/device-flow architecture: official GitHub device flow uses Client ID and device code, and refresh of device-flow-derived user tokens does not require a client secret. The corrected bootstrap is to generate exactly one App private key solely to satisfy GitHub's install gate, never expose/commit/use it in Runtime Bridge, install on `shakaarlatief` with All repositories, then securely destroy the downloaded local PEM while leaving the GitHub-side public key registration intact.

Checkpoint 396 closes the final owner-UI pre-creation gate. Owner-supplied screenshots show the manually completed GitHub registration form now matches the frozen 74-row extended profile exactly: Repository permissions 33 selected + 1 mandatory = 34 total, Organization 30, Account 10, Enterprise 0; Device Flow ON; expiring user authorization tokens ON; install-time OAuth OFF; Setup/Redirect blank/off; Webhook inactive with blank URL/secret; and Any account selected. The App has not yet been created, so no client ID, installation or GitHub authorization exists. The owner may now click Create GitHub App, then install it on `shakaarlatief` with All repositories and return only non-secret identifiers/evidence.

Checkpoint 395 freezes the first actual extended GitHub App creation target after the complete 118-row live permission capture. Validation 152 selects 74 live permission rows: 34 repository, 30 organization, 10 account and zero enterprise. The old seven-permission parity set remains a subset, with Commit statuses upgraded to write; Repository Administration(write) is now explicitly included so Codexless can later expose bounded repository creation/settings/collaborator capabilities beyond the provider-owned native GitHub connector. Only six repository rows remain No access: Agent secrets, Codespaces secrets, Dependabot secrets, Actions Secrets, redundant Single file and Webhooks. The registration prefill embeds 56 independently documented permission parameter names and leaves 18 newer/live-only rows as explicit manual selections rather than guessing query keys. Device Flow ON, expiring user tokens ON, install-time OAuth OFF, webhooks OFF, Any-account/public visibility and personal installation `All repositories` are frozen. No App/client ID/token exists yet. The next step is the owner-performed App creation/install using the extended prefill and manual checklist.

Checkpoint 394 completes the live GitHub App permission-surface capture. The owner supplied scrolling screenshots covering all current permission groups, yielding 118 exact visible options: 40 repository, 42 organization, 19 account and 17 enterprise permissions. Validation 151 and `github_app_live_permission_inventory_20260909.json` reconcile that live UI against current GitHub API documentation and freeze a broad developer-superset candidate: enable/read 34 repository, 30 organization and 10 account families, with all enterprise permissions off. The only repository exclusions are Agent secrets, Codespaces secrets, Dependabot secrets, Actions Secrets, redundant Single file and Webhooks. Repository Administration is explicitly included so Codexless can later create/manage repositories beyond native connector parity; secret-value and arbitrary-webhook authority remain deferred pending dedicated safety contracts. Personal installation scope remains All repositories. No App has been created and no authorization has started. The next step is to turn this candidate into the final extended permission manifest and rebuild the registration prefill/checklist before creation.

Checkpoint 393 reopens the GitHub App authority design before creation because the product goal is now explicitly broader than native connector parity. The owner wants Codexless Runtime Bridge to exceed the provider-owned GitHub integration where useful, including repository creation/administration and other professional GitHub operations. Validation 150 records current official permission-family inventory and establishes Repository Administration(write) as a strong extension candidate; other high-value candidates include Checks(write), Commit statuses(write), Deployments(write), Environments(write), Variables(write), code/security families, Attestations, Agent tasks/variables and optional Codespaces/Pages/custom-property capabilities. Secret-bearing permissions and repository Webhooks are not auto-selected because they require dedicated secure secret/external-destination contracts. The intended personal installation scope is corrected to All repositories rather than one ADS repository. Checkpoints 391/392 remain historical parity/preflight evidence, but their seven-permission immediate creation instruction is superseded and App creation is paused pending complete live-permission reconciliation and a broad developer-superset manifest.

Checkpoint 392 freezes the exact non-secret GitHub App registration and first-installation configuration around that seven-permission manifest. The App is to be registered under personal account `shakaarlatief` as `Codexless Runtime Bridge`, with homepage at the public ADS repository, Any account/public installability, device flow enabled, expiring user authorization tokens enabled, install-time OAuth authorization disabled, no callback/setup URL, webhooks disabled, no private-key bootstrap, and no extra organization/account/enterprise permissions. Public visibility is required to preserve later personal+organization installation parity; it does not itself grant repository authority. The first live installation is deliberately staged to `Only select repositories` with only `shakaarlatief/autonomous-data-science-system`, so authorization/installation-scope/GraphQL sufficiency can be qualified with minimal blast radius before any broader installation is approved. A GitHub-supported prefill URL and exact owner checklist are machine-preserved and validated. No App/client ID/token exists yet; the next step is the owner-performed account UI creation/install using that frozen configuration.

Checkpoint 391 freezes the first dedicated GitHub App authority manifest for the exact 89-action parity target. Validation 148 maps every native action in exact inventory order and the new machine validator passes 89/89. The REST-derived initial App requests exactly seven repository permission families: Actions(write), Contents(write), Issues(write), Metadata(read), Pull requests(write), Commit statuses(read), and Workflows(write); organization/account/enterprise permissions and webhooks remain empty, and Administration/Checks/Members are explicitly excluded. Workflows(write) is retained because the observed arbitrary file/ref mutations must remain able to affect `.github/workflows`. Current GitHub documentation does not publish an exact GitHub App permission table for GraphQL and instead instructs developers to test intended queries/mutations; eight observed PR/review actions therefore remain a live sufficiency probe under the already-required Pull requests(write), with no speculative extra permission. No GitHub App has yet been registered, no client ID is configured, and live GitHub auth remains unstarted. The next boundary is to freeze the exact non-secret App registration configuration before the owner performs the account-bound GitHub UI creation/install step.

Checkpoint 390 closes the preview.25 fresh-host authorization support gate and the live ChatGPT Plugin display-name rename. In a refreshed fresh disposable conversation, `codex.github_authorization` projected as a structured flat bounded object with visible six-value `action`, bounded optional `requestId`, bounded optional `authorizationRef`, and literal `confirmClear=true`; the preview.24 generic map did not recur. The exactly one permitted `metadata` invocation reached Runtime Bridge and returned `configured=false`, `initialized=false`, `authorized=false`, `storedAuthorization=false`, `authMode=github-app-user-token-device-flow`, `host=github.com`, REST `2026-03-10`, with no device-flow/token/credential mutation. A current ChatGPT UI screenshot supplied by the project owner also shows the Plugin display name `Codexless Runtime Bridge`, closing the display-name qualification explicitly left open at Checkpoint 370. Historical `ADS Codexless Local Bridge` references remain historical evidence. Actual GitHub authorization remains unstarted because no server-owned GitHub App client ID is configured. The next Research 123 gate is to derive and freeze the exact minimal GitHub App permission manifest from official endpoint requirements before App registration/device flow.

Checkpoint 389 preserves the failed preview.24 fresh-host authorization qualification and the live preview.25 flat-schema correction. In the fresh disposable ChatGPT conversation, `codex.github_authorization` was projected but its host input schema collapsed to `{ [key: string]: any }`; the single permitted `metadata` call was then blocked by OpenAI safety controls before any Runtime Bridge payload returned. Direct local MCP inspection proved preview.24 still had a strict six-branch `oneOf`, reproducing the AB-008 top-level-union genericization class without proving that genericization alone caused the safety block. Private local-runtime head `ad10aa30342503d303b6a22629fe56dc914f0fa2` replaces that union with one strict flat object exposing required six-value `action`, bounded optional `requestId`, bounded optional `authorizationRef`, optional literal `confirmClear=true`, and `additionalProperties=false`; exact cross-field rules remain server-enforced. The full 16-regression staged release matrix passed, release `github-auth-control-flat-v2` published under operation `rm_6215ff67fd5ca530af3ca953b0cad03a`, restart operation `rm_accbd4edacc46458cae81dd493173feb` activated version `0.1.1-preview.25-github-auth-flat`, and postactivation verification reports 64 tools, one runtime dependency and zero mismatches. Direct local MCP now serializes the flat schema exactly and metadata still reports configured/authorized/storedAuthorization false. No GitHub authorization has started. The next gate is refreshed fresh-chat host projection plus exactly one metadata-only requalification.

Checkpoint 388 live-qualifies the explicit GitHub authorization-control support surface. Private local-runtime head `d63bb48112985fd05e4a32925b83e75214dd2a4a` preserves corrected release `github-auth-control-v2-fix2`; Runtime Release v2 preparation froze manifest SHA-256 `92554d6da7418885fcb491f1c16a2527517ca09d6c230d0d8a5dc54e1421a7be`, publication operation `rm_137444f8dda39d01c282b2c1d47a9356` succeeded after all sixteen regressions, restart operation `rm_91321739c5b2287e638719a37c2de0b3` succeeded without recovery, and fresh postactivation verification reports version `0.1.1-preview.24-github-auth-control`, 64 public tools, one runtime dependency and zero mismatches. Direct active local MCP `tools/list` contains `codex.github_authorization`, and a metadata-only live call returned `configured=false`, `authorized=false`, `storedAuthorization=false`, `github.com`, REST `2026-03-10`. No device flow, token creation or GitHub OAuth/API request occurred. This same persistent ChatGPT conversation still does not project the new support tool as callable, reproducing AB-008 stale same-chat projection; the next gate is refreshed fresh-chat discovery/schema capture plus exactly one metadata-only call before any GitHub App configuration/device authorization. Public `github.*` parity actions remain 0/89.

Checkpoint 387 live-qualifies the first Runtime Release v2 dependency activation. Private local-runtime head `19a4d1852f99f0d10d1a5b4bca23c0f39d825bb1` preserves release `github-g0-keyring-activation-v2` (manifest SHA-256 `33d8b19ae09c10f602857828e1257c8e5db1d050646d9769eeb9c09ee6ff81f1`), which declares only fixed dependency id `github-keyring-win32-x64`, advances the runtime to `0.1.1-preview.23-github-g0-keyring`, keeps the public tool count at 63, and adds no `github.*` action. A fresh real-binding smoke loaded `@napi-rs/keyring` from immutable tree `abe67a212121747d57d1bb78cd7880e7e7bb29e1f44e2ba8ec5010e5f1e50858`; live v2 prepare returned `runtimeDependencyCount=1`; publication operation `rm_080792c073690364c32fa90c7c1da128` succeeded with all 15 regressions; postpublication verification reached zero mismatches; restart operation `rm_41cf35130455181ec38697d2aa1ae435` succeeded without recovery; and fresh postactivation verification reports `runtimeDependencyCount=1`, `mismatchCount=0`. The exact keyring generation is therefore active for the live worker, while live GitHub authorization, protected GitHub-token creation, GitHub API requests, and public parity actions remain unstarted. The next boundary is an explicit bounded GitHub authorization-control support surface before the first read-only parity action bundle.

Checkpoint 386 live-qualifies the source-only G0 dependency bootstrap. Private local-runtime head `21b8597abde893a2b6e6b9b91d3488de0fe8aa16` preserves release `github-g0-dependency-bootstrap-v1` (26 files, 14 regressions, manifest SHA-256 `77dde3e241d422ba2d7e8e66edb3d9dbe89383fb57f1bd48209294f158a30fe2`). The still-live v1 engine prepared it successfully, the expected prepublication verification reported 26 mismatches, publication operation `rm_92d5a1cdf16ee979cabda34918b5c686` succeeded, postpublication verification reached zero mismatches, and restart operation `rm_1dcf2e517515a89eee1c5c651bc440ef` activated target version `0.1.1-preview.22-github-g0-bootstrap` with no recovery. Fresh postactivation verification comes from the new dependency-aware release service and returns `runtimeDependencyCount=0`, `mismatchCount=0`, target tool count 63. The v2-capable release engine and G0 source are therefore live with an intentionally empty dependency binding, zero public `github.*` actions, and no live GitHub authorization. The next boundary is a Runtime Release v2 activation of only the fixed `github-keyring-win32-x64` generation.

Checkpoint 385 closes the runtime dependency-provisioning architecture blocker with immutable native-package generations. Private local-runtime head `5b63371536fa2f09bb122ed09470ec5204f18d9b` now integrates exact server-owned dependency preparation, canonical `{dependencyId, treeSha256}` worker bindings, Runtime Release v2 dependency state, activation/rollback/restart/recovery selection, startup revalidation, and G0 keyring loading through the exact generation only. A real Windows x64 `@napi-rs/keyring@2.0.0` generation prepared and loaded successfully at tree digest `abe67a212121747d57d1bb78cd7880e7e7bb29e1f44e2ba8ec5010e5f1e50858` (10 files, 1,971,364 bytes), and real Runtime Release v2 preparation produced the same binding. Same-process deletion after native loading failed with Windows `EPERM` while post-process cleanup succeeded, so release/rollback now switches immutable worker bindings rather than mutating loaded live `node_modules`. Combined focused regressions pass 22/22, candidate syntax passes 21/21 and 15/15, the secret scanner reports zero matches, and private publication passes `RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS`. The current live runtime still has Release v1, so the next step is a source-only v1 bootstrap release that installs the dependency-aware engine/G0 source with an empty dependency binding before v2 activates the keyring generation.

Checkpoint 384 qualifies the first main-runtime G0 source-integration candidate at private local-runtime head `6ce0da8818a455731acc10ba231ef9f52c0c8206`. The candidate composes a lazy internal GitHub runtime kernel into public-preview construction while preserving the existing 63-tool public surface and zero `github.*` actions. Syntax checks pass 9/9, integration regressions pass 4/4, the secret scanner reports zero matches, and the private push passes `RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS`. The only newly localized live-release blocker is deployment dependency provisioning: Runtime Release v1 may target only `src`, `test`, `scripts`, and `config`, and cannot provision root package manifests or `node_modules`; the Windows-qualified `@napi-rs/keyring@2.0.0` staging tree was intentionally removed. The next work is therefore a bounded deterministic dependency-provisioning/rollback extension, not live GitHub auth or public action registration.

Checkpoint 383 closes the concrete Windows protected-store discriminator. The exact `@napi-rs/keyring@2.0.0` package loaded successfully on Windows x64 and one bounded normal-user-session synthetic Credential Manager lifecycle returned `set=true`, `readMatch=true`, `delete=true`, `absentAfterDelete=true`, and `cleanupAttempted=true`. No GitHub token was used, the synthetic secret stayed in memory and was not printed, and staging-only `node_modules`/npm-cache artifacts were removed afterward. The earlier sandbox `ERROR_NO_SUCH_LOGON_SESSION` is therefore localized to sandbox execution context rather than keyring incompatibility. Main Codexless G0 integration is now the next step; live GitHub authorization and public `github.*` actions remain unstarted.

Checkpoint 382 qualifies the first private G0 implementation candidate at local-runtime head `3c5f3688ec578c0817953890dc69ecb7ce679153`. The candidate implements OS-keyring-backed token-store abstraction, device-flow state, single-flight refresh, fixed github.com REST `2026-03-10` transport, server-registered GraphQL operations, semantic transport/error classification and installation-derived repository authority. `npm run check` passes and the focused suite is 12/12 PASS with zero real GitHub calls and zero real OS credential writes. The first private push failed closed because conservative secret detection matched ordinary source assignment syntax; the validator was not weakened. Source/fixtures were rewritten to produce zero scanner hits and the normal push then returned `RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS`. Live Codexless and public `github.*` actions remain unchanged. The next bounded gate is exact `@napi-rs/keyring` Windows import plus one synthetic OS Credential Manager set/get/delete round trip with verified cleanup.

Checkpoint 381 freezes the current official GitHub platform baseline needed for G0. Current GitHub documentation confirms the selected GitHub App user-access-token/device-flow model, user+app intersection authority, installation-derived repository scope, device-flow issuance and refresh without a client secret, eight-hour access tokens plus six-month refresh tokens, and explicit github.com REST version `2026-03-10` with required User-Agent. The same pass closes platform-level `create_tree` nested entry semantics, create-PR normalized head/base requirements, and same-path Contents write serialization. The G0 implementation contract is therefore ready without any live GitHub credential or mutation; the protected Windows token-store implementation is the main local design choice next.

Checkpoint 380 preserves the final 89-action GitHub schema reconciliation. The six-batch host-visible capture is exact at `89 / 89` with zero missing/extra actions and zero GitHub action invocations, but the final native marker is `GITHUB_89_SCHEMA_CAPTURE=INCOMPLETE` because every output schema and structured error schema is hidden by the host projection and `create_tree.tree_elements` remains genericized. This is now explicitly treated as an exact native-wrapper wire-contract gap, not a failure of practical capability mapping. Action/request mapping is ready. Broad replay of all 89 native actions is not justified. The independent G0 GitHub App/device-flow/auth/REST-GraphQL transport kernel is ready to begin while action-specific publication remains evidence-gated. Authoritative GitHub API contract mapping and targeted wrapper qualification only for surviving material gaps are the next Research 123 route.

Checkpoint 379 preserves native GitHub schema-capture Batch 6 and completes the six-batch discovery capture at `89 / 89` with zero GitHub action invocations. The final batch adds commit-search qualifier rejection plus a narrow recent-commit empty-query exception, opaque next-token and 1-based-page installed-repository search models, issue-search repository-selector exclusivity, sequential same-path `update_file` mutation guidance with named `content_sha`, issue replacement-set semantics with no explicit milestone-clear operation, and branch-oriented `update_ref(force=false)` without a tag/ref-namespace selector. The machine artifact is intentionally marked `CAPTURED_89_OF_89_PENDING_FINAL_RECONCILIATION`: final same-conversation reconciliation must classify every remaining genericized/hidden/ambiguous contract before implementation begins.

Checkpoint 378 preserves native GitHub schema-capture Batch 5 and advances cumulative discovery evidence to `75 / 89` with zero GitHub action invocations. The batch captures the exact PR merge-method enum and `expected_head_sha` optimistic-concurrency guard, preserves reviewer request/removal optional-array ambiguity, confirms top-level-only inline review replies, and records GitHub Actions write permission for both exposed rerun mutations. It also distinguishes final-`topn` code search with valid-empty empty-query behavior from opaque-cursor branch search. Thirteen of the fifteen Batch 5 actions are mutations. Implementation remains unstarted, only fourteen native action contracts remain, and projected actions 76-89 are the final discovery-only Batch 6 before final 89-action reconciliation.

Checkpoint 377 preserves native GitHub schema-capture Batch 4 and advances cumulative discovery evidence to `60 / 89` with zero GitHub action invocations. The batch directly captures installation/account discovery and installation-scoped repository listing, further supporting the selected GitHub App/user-token architecture. It confirms internal-final-limit recent-PR pagination, all-pages changed-filename listing, recent-issue pagination until `top_k` or exhaustion, zero-based repository offsets, and unspecified pagination for PR review threads/reviews and organization lists. Four actions are zero-argument calls. `lock_issue_conversation.lock_reason` is a genuine four-value enum, while recent-PR state and repository-affiliation examples remain plain strings. Implementation remains unstarted and projected actions 61-75 are the next discovery-only Batch 5.

Checkpoint 376 preserves native GitHub schema-capture Batch 3 and advances cumulative discovery evidence to `45 / 89` with zero GitHub action invocations. The batch supplies the first concrete valid-empty/not-found contract: `fetch_pr_file_patch` returns `patch=null` for a valid PR lacking the validated changed path, but documents 404 for an unresolved repository/PR and explicitly says not to retry alternative paths. It further differentiates all-pages PR patch retrieval, first-page workflow artifacts, latest-attempt plus first-page workflow jobs, and explicit page/per_page reaction pagination. `get_pr_diff` exposes `diff | patch` with default `diff`; `get_profile` is zero-argument; `get_repo` repeats the Enterprise-aware selector XOR; collaborator-permission output values remain unprojected. Implementation remains unstarted and projected actions 46-60 are the next discovery-only Batch 4.

Checkpoint 375 preserves native GitHub schema-capture Batch 2 and advances the fixed-projection machine evidence to `30 / 89` with zero GitHub action invocations. The batch resolves `GitHub.download_user_content` as a narrowly allowlisted private-user-image URL downloader, confirms workflow-artifact redirect plus reusable file-reference semantics, and demonstrates action-specific pagination: commit workflow runs are first-page-only, issue comments are internally all-pages, and PR-comments pagination is unspecified. `GitHub.create_tree.tree_elements` is genericized to `{ [key: string]: any }[]`, so exact inner tree-entry schema remains a preimplementation evidence gap. `fetch_issue.repository_url` explicitly mentions GitHub Enterprise Server custom hostnames and GHE.com API hosts; this is now a Research 123 host-scope follow-up rather than an assumed global capability. Implementation remains unstarted, and projected actions 31-45 are the next discovery-only Batch 3.

Checkpoint 374 preserves native GitHub schema-capture Batch 1 from the same fixed fresh GitHub-only conversation. Exact host-visible contracts for projected actions 1-15 are now machine-preserved in `docs/research/github_connector_native_schema_capture.json` and mechanically validated at `15 / 89`; no GitHub action was invoked. The first batch establishes an important parity constraint: all fifteen actions expose object input contracts, but all fifteen project return type `any`, no separate action-title metadata, and no machine-readable structured error schema. Several cross-field rules are descriptive rather than structurally encoded, including review-body conditions, the `create_branch` sha/base_ref XOR, and parts of `create_pull_request` validation. Exact projected enums include `add_review_to_pr.action = COMMENT | APPROVE | REQUEST_CHANGES` and `create_blob.encoding = utf-8 | base64` with default `utf-8`. Implementation remains unstarted; projected actions 16-30 are now the exact next discovery-only Batch 2, including the corrected `GitHub.download_user_content` action.

Checkpoint 373 corrects the one exact-name defect exposed when the required fresh GitHub-only schema-capture conversation returned its actual projected inventory. The host again projected exactly 89 actions and no GitHub action was invoked. Compared with the Checkpoint 372 reconstructed inventory, the fresh projection contains `GitHub.download_user_content`, not `GitHub.add_issue_comment`; `GitHub.add_comment_to_issue` remains the projected issue-comment creation action. Because Validation 128 never publicly preserved all exact names, Validation 130 classifies this as `RECONSTRUCTION_DEFECT_NOT_CONNECTOR_DRIFT`. The schema-version-2 machine inventory now preserves the exact fresh projected order and the validator asserts that order. The Checkpoint 372 GitHub App/device-flow, installation-scope, REST/GraphQL and mutation-safety architecture remains accepted. Native schema capture is now active in the same fixed GitHub-only conversation, with projected actions 1-15 as Batch 1 and implementation still not started.

Checkpoint 372 freezes the first complete Research 123 preimplementation design boundary. The public repository created its first 89-entry native GitHub action reconstruction plus a mechanical count/uniqueness/order validator and mapped every action one-for-one into the preferred `github.*` Runtime Bridge namespace. Exact remote parity is correctly recorded as `0 / 89`: the existing semantic Git layer provides reusable local safety/transport patterns but is not remote GitHub API parity. The selected authentication design is a dedicated GitHub App with device-flow user authorization, installation-derived repository scope, server-owned protected token/refresh lifecycle, and internal REST/GraphQL transport. The design also freezes action-specific pagination/error/mutation rules, artifact resource handoff, stale-SHA/expected-head/non-force safeguards, and incremental host-projection qualification toward the full 89-tool surface. Validation 128 did not preserve complete native schemas, so Checkpoint 372 opened the discovery-only fresh GitHub schema-capture gate. Its one exact-name reconstruction defect is explicitly superseded by Validation 130 / Checkpoint 373 rather than silently rewritten.

Checkpoint 371 qualifies the private knowledge companion as a first-class Runtime Bridge workspace without changing the public/private authority hierarchy. The dedicated `private-companion` Git integrity policy was preserved in the private local-runtime repository at `7297e7740f5973ed11d434c24b3e0c43b7a05205`, prepared, published, activated and post-verified through the semantic runtime-release path with zero final mismatches. Registry revision 17 now admits `ads-private` with `read`, `write`, `agent`, `browser`, `git_fetch`, `git_pull_ff_only`, `git_commit_paths`, and `git_push_ff_only`, semantic Git bound to `origin`, and protected `.git` metadata. Live fetch, strict FF-only pull, semantic commit and semantic push all passed; pushes returned `PRIVATE_COMPANION_REPOSITORY_SAFETY=PASS`. The private companion remains a knowledge-preservation complement only. Its public continuity anchor was reconciled to exact public Checkpoint 371 / `97189ba4b53adedbdb50fea47542e550a3f05fca` and `PRIVATE_CONTINUITY_INTEGRITY=PASS` before the current Checkpoint 372 transition. Checkpoint 372 private continuity is evaluated separately after the exact public commit exists.

Checkpoint 369 preserves a post-closure operational hardening without reopening Research 122. Validation 127 localizes a Windows Codex installation-generation failure in which the running process lost its sandbox-helper resolution while the ADS tunnel remained healthy. The already-qualified bounded `codex.runtime_maintenance` restart recovered command execution by launching against a complete installed generation. A separate semantic-Git hardening then moved bounded `git add`/`git commit` metadata mutations from the ordinary Codex command sandbox to the existing host Git substrate while preserving exact-path, expected-HEAD, branch/upstream, protected-path, diff, parent and clean-index gates. Release `semantic-git-host-metadata-v2` was prepared, published, activated and post-verified with zero mismatches while the public runtime contract remained preview.20 / 63 tools. The operations runbook now owns the recovery sequence. AB-002 and Research 122 remain closed; Research 113 remains active.

Checkpoint 368 closes Research 122 and returns the active boundary to Research 113. Validation 126 refreshes current OpenAI product evidence and live-qualifies the paired Windows/iPhone Codex Remote path: a manually started Windows Codex thread appeared in the native iPhone Remote surface, a phone follow-up ran successfully against the Windows-hosted repository while the visible desktop UI was closed, and reopening the desktop app showed the same thread with both turns. Combined with Validation 125's successful normal-mobile-web ADS tunnel path, the accepted phone architecture is now intentionally split: native ChatGPT Remote for Codex and ordinary mobile web for ADS developer-MCP/local tools. The project owner accepts manual Codex prompt/result copy-paste, so direct ADS-to-Codex dispatch and custom cross-device Codex card/handoff/wakeup machinery are optional conveniences rather than core blockers. AB-003, AB-004, AB-006 and AB-007 are demoted accordingly; AB-001 is resolved, AB-002 remains closed, and AB-017 remains broader open research. Research 113 resumes its reuse-first upstream comparison survey; Source Vault ingestion remains paused until that broader Level-2 program produces a resume decision.
Checkpoint 367 is the current boundary. Validation 125 resolves AB-001 connector reachability through the normal ChatGPT mobile web client. A fresh native mobile-app chat could discover the ADS connector and `codex.account_preflight` but its single invocation returned HTTP 401 `tunnel_active_organization_required`, localizing that surface to organization-context authorization failure rather than a dead tunnel. A separate fresh normal mobile-browser chat exposed the same connector/tool and completed `codex.account_preflight` successfully with all account/auth/quota/rate-limit checks `ok`; the local tunnel independently logged dispatcher forwarding and the laptop conversation continued reaching ADS afterward. Desktop-site mode is skipped because normal mobile web passed. The accepted phone path is therefore ordinary `chatgpt.com` mobile web with the existing secure tunnel. AB-002 remains closed, AB-001 is resolved for connector reachability, and AB-006 cross-device task/card/approval recovery is now the active Research 122 discriminator.
Checkpoint 366 is the current boundary. Validation 124 closes AB-002 for the accepted narrow runtime self-maintenance scope. Fresh-host rollback `status` returns durable `rollback_release / succeeded`; post-rollback `verify` returns the expected `verification_failed` with exactly two mismatches because preview.20 is installed while the prepared target remains preview.21. Independent inspection confirms healthy preview.20 / 63 at PID 10280 / `ri_3901...`, exact restored preview.20 hashes, no pending activation, no active managed release, no shared mutation lock, a clean synchronized private release source at `7aa303f...`, and tunnel `live/ready`. Forward semantic update and explicit semantic rollback are therefore both production-qualified without a user-run `%LOCALAPPDATA%` publication helper or manual Codexless/tunnel restart. Research 122 remains active for AB-001 device-independent connector reachability and then AB-006 interruption/cross-device task recovery. The next discriminator is the native-mobile versus mobile-browser ChatGPT access matrix.

Checkpoint 365 is the current boundary. Validation 123 live-qualifies semantic rollback activation: one bounded restart replaced preview.21 PID 56332 / `ri_3ae3...` with healthy preview.20 / 63 PID 10280 / `ri_3901...`, while exact restored preview.20 hashes remained installed and the same tunnel PID 67468 stayed `live/ready`. Durable restart status is `succeeded`, pending activation and the shared lock are cleared, and the active managed-release pointer is absent as expected when rolling the first managed release back to its unmanaged preview.20 predecessor. Forward update and rollback execution are now both production-qualified without ordinary-host publication or manual restart. The final AB-002 gate is read-only fresh-host rollback status plus expected preview.21 verification mismatch after rollback.

Checkpoint 364 is the current boundary. Validation 122 qualifies semantic rollback source restoration separately from runtime activation. Fresh-host `codex.runtime_release rollback` returned `armed`; the detached rollback reached durable `succeeded`, restored both preview.20 source hashes exactly, released the shared mutation lock, and created a rollback-direction pending activation. The executing process is deliberately still preview.21 PID 56332 / `ri_3ae3...`, the active-release record still points to preview.21, and the tunnel remains `live/ready`. The next isolated mutation is one semantic restart expected to activate preview.20 / 63 from the restored bytes, clear pending state, remove the active managed-release pointer, and preserve the tunnel.

Checkpoint 363 is the current boundary. Validation 121 qualifies fresh-host public readback after the first end-to-end semantic forward update. `codex.runtime_release status` for the original publish requestId returns the durable `publish_release / succeeded` operation, and post-activation `verify` returns `verified` with `mismatchCount=0` for preview.21 / 63. Independent live inspection confirms the same preview.21 process remains active, exact target hashes are installed, pending activation and the shared mutation lock are absent, the active managed release is preview.21, and the tunnel remains `live/ready`. The next isolated mutation is semantic rollback publication only; rollback activation must remain separate so restored preview.20 source and rollback pending state can be verified before restart.

Checkpoint 362 is the current boundary. Validation 120 qualifies the first end-to-end normal future update through semantic release + semantic restart. Preview.21 source was already published semantically; one bounded maintenance restart then replaced preview.20 PID 41548 / `ri_c862...` with healthy `0.1.1-preview.21-semantic-release-e2e` PID 56332 / `ri_3ae3...`, while the exact same tunnel PID 67468 stayed `live/ready`. Durable restart status is `succeeded`, pending activation and the shared lock are cleared, preview.21 is recorded as the active managed release with immutable history, and installed target hashes remain exact. No user-run `%LOCALAPPDATA%` publication helper or manual Codexless/tunnel restart was used for preview.21. Remaining AB-002 work is host-visible post-activation verify/status plus explicit semantic rollback and rollback activation qualification.

Checkpoint 361 is the current boundary. Validation 119 qualifies the first real semantic publication into the installed Codexless tree. Fresh-host `codex.runtime_release publish` returned `armed`; the detached operation then reached durable `succeeded`, both installed targets exactly match preview.21 hashes, the shared mutation lock is released, and a forward pending-activation contract binds preview.20 / 63 to preview.21 / 63. The still-running process remains preview.20 PID 41548 / `ri_c862...` and the tunnel remains `live/ready`, proving publication itself did not restart either layer. This is the first production proof that ordinary installed-source publication can occur without a user-run `%LOCALAPPDATA%` helper. The next isolated mutation is semantic restart activation.

Checkpoint 360 is the current boundary. Validation 118 live-qualifies `codex.runtime_release prepare` plus pre-publication `verify` for the genuine preview.21 bundle. Prepare returned `prepared`; verify returned the exactly expected `verification_failed` with `mismatchCount=2`, proving live verification still sees the two preview.20 baseline files. Independent inspection confirms preview.20 / 63 remains the same running instance, both live file hashes are unchanged, tunnel is `live/ready`, and private release source remains clean/synchronized at `7aa303f...`. The next isolated mutation is one semantic `publish` call only. Do not combine publish and restart: preserve the source-published/activation-pending boundary first, then activate through the already-qualified semantic self-restart.

Checkpoint 359 is the current boundary. Validation 117 qualifies the first genuine next-version bundle for the live semantic release path: `preview21-semantic-release-e2e` at clean synchronized private head `7aa303f4f362f7d4a3ae9b4d492679751c5e892b`, targeting `0.1.1-preview.21-semantic-release-e2e` / 63 tools. The canonical manifest has two exact replace entries whose expected-current hashes match live preview.20 and whose payload hashes match the preserved private bytes. A staged exact-live overlay passes all nine declared public/release regressions. No live install/runtime mutation or prepared release state has occurred yet. The next gate is fresh-host `prepare` plus pre-publication `verify`, with publish explicitly forbidden until those live receipts are qualified.

Checkpoint 358 is the current boundary. Validation 116 qualifies the refreshed fresh-chat host projection of live preview.20 `codex.runtime_release`: one structured object with exactly four required fields (`action`, `releaseId`, `requestId`, `expectedSourceHead`), the exact five-action enum, bounded release/request identifiers and exact lowercase 40-hex source HEAD. No generic-map projection or caller-selected host/process/filesystem authority is exposed. No ADS tool was invoked in the disposable qualification chat. Direct local health remains preview.20 / 63 tools with tunnel `live/ready`. The next objective is now the decisive AB-002 proof: construct a genuine next-version release bundle in the fixed private namespace, qualify it completely against preview.20, then execute the update through semantic release + semantic restart without another ordinary-host `%LOCALAPPDATA%` publication helper.

Checkpoint 357 is the current boundary. Validation 115 live-qualifies the one-time preview.19 -> preview.20 semantic bootstrap activation. The already-live preview.19 `codex.runtime_maintenance` surface returned `armed` before destructive work, and the newly installed bootstrap-compatible supervisor replaced PID 69280 / instance `ri_780a...` with PID 41548 / `ri_c862...`, healthy as `0.1.1-preview.20-runtime-release` / 63 tools. The managed tunnel remained the exact same PID 67468 and stayed `live/ready`. Durable status for the exact requestId returned `succeeded` with no recovery. Manual Codexless/tunnel restart was not needed. The current conversation predates the new tool projection, so the next gate is developer-plugin refresh and fresh-chat schema discovery of `codex.runtime_release` without invoking it.

Checkpoint 356 is the current boundary. Validation 114 preserves successful source-only publication of preview.20 from private head `77e13dc69aec8e2fdc7ffa8379cccf039046785e`. The protected helper returned PASS with all nine live-disk public regressions green and no restart. Independent verification compared all 22 candidate `src`/`test` files against the installed Codexless tree with zero mismatches. The executing process is still preview.19 / 62 tools at PID 69280 / instance `ri_780a...`, while the managed tunnel remains `live/ready`. This is the deliberate source-published / activation-pending boundary. The next step is one semantic `codex.runtime_maintenance restart_codexless` call from the already-live preview.19 surface to activate the newly installed preview.20 / 63-tool runtime.

Checkpoint 355 is the current boundary. Validation 113 qualifies the corrected final preview.20 runtime-release candidate at private head `77e13dc69aec8e2fdc7ffa8379cccf039046785e` and the exact guarded one-time source-publication helper. The bootstrap correction is essential: when still-running preview.19 dispatches the newly installed maintenance supervisor, the supervisor now detects the old launcher environment, derives the fixed install root from its own installed module location, and derives the preview.20 / 63 replacement contract from newly installed server-owned surface constants. A dedicated isolated preview.19 -> preview.20 restart probe passes. Two complete no-publish helper runs pass all nine staged public regressions, 12/7/6 lifecycle suites, six lifecycle/release functional probes and Windows atomic replace/add rollback smoke. The helper performs no restart and live production remains preview.19 / 62 tools with tunnel live/ready. Ordinary-host source-only publication through that exact helper is next; after independent hash verification, activation should use the already-live semantic self-restart.

Checkpoint 354 is the current boundary and Research 122 remains active. Validation 112 now qualifies the complete preview.20 semantic runtime-release candidate at private head `00355fa8354147a8c62dfd40521c122dede5530b`: a strict 63-tool `codex.runtime_release` surface with fixed private release-source authority, exact source-HEAD and payload hashes, prepared server-owned state, staged/live regression gates, installed-baseline hashes, durable rollback snapshots, pending activation, immutable chained activation history, and release-aware reuse of the already-qualified `codex.runtime_maintenance` restart path. Real isolated worker probes pass forward activation, forward startup-failure recovery, rollback activation and rollback startup-failure recovery. Production remains preview.19 / 62 tools and was not mutated. The next gate is an exact guarded one-time preview.20 bootstrap publication preflight; successful source publication should then be activated through the already-live self-restart rather than another manual Codexless stop/start.

Checkpoint 353 is the current boundary and Research 122 is active. Validation 111 now live-qualifies ordinary Codexless-only self-restart through the bounded `codex.runtime_maintenance` surface: fresh-host dispatch returned an `armed` receipt before destructive work, the exact preview.19 instance changed from PID 8564 / `ri_e052...` to PID 69280 / `ri_780a...`, the replacement remained preview.19 / 62 tools, the same managed tunnel process stayed running and `live/ready`, durable status for the exact requestId returned terminal `succeeded`, and an explicit duplicate restart replay returned the same operation with no second restart after the destructive-delay window. Manual tunnel/Codexless stop-start is therefore no longer required for ordinary Codexless-only restart. AB-002 remains open for narrow semantic publication/verify/rollback into the installed runtime tree, and AB-001 remains open for the phone/mobile-web matrix. Validation 110 now qualifies the refreshed fresh-chat ChatGPT host projection of preview.19: `codex.runtime_maintenance` is a structured callable object containing only required `action` and `requestId`, the action enum is exactly `restart_codexless | status`, requestId bounds/pattern are visible, no generic map/index signature remains, and no arbitrary host-process authority field is exposed. No ADS tool was invoked in that fresh chat. Combined with Validation 109 process-live local MCP evidence, the host-schema safety gate is now closed. The first production `restart_codexless` qualification using one stable requestId is next. Preview.19 is now process-live at 62 tools. Independent verification binds listener PID, private runtime identity and public health to the same exact instance, confirms the private shutdown token is not exposed, and confirms the tunnel is live/ready. A direct active MCP initialize/tools-list returns `codex.runtime_maintenance` as the corrected flat object with exactly required `action` and `requestId`, action enum `restart_codexless | status`, `additionalProperties: false`, and no top-level union. No production self-restart has been invoked. Refresh the existing developer MCP app and use a fresh disposable chat for the decisive host-schema projection test next. Preview.19 source publication has succeeded and independent read-only verification proves all three installed candidate hashes exactly match while AB-020 semantic-Git is unchanged. The active process intentionally remains preview.18 / 62 tools and the tunnel remains live/ready, so this is a clean source-published/restart-pending boundary. Because preview.18 failed the ChatGPT host schema-fidelity gate, it will not self-restart into preview.19. One manual runbook-controlled activation restart is next. After activation, refresh the app and require a fresh-chat structured flat-schema discovery PASS before any live `restart_codexless` invocation. Validation 107 now qualifies the exact guarded preview.19 three-file publication package. Two complete no-publish runs pass the actual flat MCP wire-schema assertion, all eight public compatibility regressions, all 12/7/6 lifecycle suites plus three probes, and the Windows atomic replacement/rollback primitive. Production remains preview.18 / 62 tools with the tunnel live/ready and no live self-restart invoked. Ordinary-host source publication is next; the helper performs no restart. After publication and independent hash verification, preview.19 still requires a manual activation restart because preview.18's generic host-projected mutation schema is deliberately not accepted for bootstrap. The refreshed fresh-chat host discovered `codex.runtime_maintenance` but genericized its preview.18 top-level discriminated-union schema to `{ [key: string]: any }`; no ADS tool or production restart was invoked, and direct local MCP remained strictly bounded. Validation 105 localizes this as a host schema-projection fidelity failure. Validation 106 now qualifies a minimal preview.19 correction at private head `ac3e05de0ebd9553eafb322ce19ec17539f1c09d`: one strict top-level object with required `action`/`requestId`, action enum `restart_codexless | status`, `additionalProperties: false`, and an actual MCP initialize/tools-list wire regression. All staged public and lifecycle compatibility tests pass. Production remains preview.18 / 62 tools with the tunnel live/ready. Guarded preview.19 publication is next. Validation 104 now qualifies the one final bootstrap activation: active Codexless is preview.18 / 62 tools, the listener/private identity/public health all bind to one exact instance, the private shutdown token is not exposed, the tunnel is live/ready, and direct local MCP initialize/tools-list returns all 62 tools including `codex.runtime_maintenance` with the intended closed schema. No production self-restart has been invoked yet. Refresh the existing ChatGPT developer MCP app and use a fresh disposable chat for host discovery next. Validation 103 now preserves successful preview.18 source publication and independent installed-hash verification. All eleven preview.18 source files and three replaced regression files exactly match the qualified candidate, AB-020 semantic-Git is unchanged, and preserved Office/PDF/image regressions remain unchanged. The active process is intentionally still preview.17 / 61 tools while the tunnel remains live/ready. One final full runbook-controlled bootstrap restart is next; only afterward can the 62-tool `codex.runtime_maintenance` surface be refreshed/discovered and live-qualified. Validation 102 now qualifies the exact guarded preview.18 publication package: exact preview.17 live-baseline hashes, exact preview.18 candidate hashes, eight staged 62-tool regressions, the full lifecycle suites/probes, Windows atomic forward/rollback smoke coverage, and two complete no-publish passes. Production remains preview.17 / 61 tools and the tunnel remains live/ready; ordinary-host source publication is next and will deliberately perform no restart. Validation 101 now qualifies the production-shaped direct runtime-maintenance path in isolation: exact private runtime-instance binding, authenticated fixed-loopback graceful shutdown, fixed replacement launch, durable active-operation exclusion/status, and direct Codexless-owned helper dispatch that returns an armed receipt before destructive work. The private preview.18 integration candidate proposes `0.1.1-preview.18-runtime-maintenance` / 62 tools with the narrow `codex.runtime_maintenance` action, while production remains unchanged on preview.17 / 61 tools. Guarded publication preflight is next. The detached one-shot helper architecture now has a durable file-backed operation ledger and a narrowly bounded detached launcher preserved in the private runtime candidate. The original 12-test semantic coordinator suite and the new 6-test durable-ledger/launcher suite both pass. A real isolated dummy-service probe further proved that the delayed detached helper can continue after the invoking generic command wrapper times out, replace the dummy service, verify the replacement healthy, and leave a durable succeeded receipt for later inspection. This qualifies helper survival and recoverable terminal state, while explicitly rejecting generic command_exec as the permanent lifecycle launcher. The next implementation boundary is direct Codexless-owned helper dispatch plus exact process identity checks on an isolated Codexless-style worker.  The exact installed tunnel-client managed runtime is now functionally qualified across a local MCP target outage: real initialize/tools-list traffic passed before the outage, a queued request failed visibly with 502 while the target was absent, and a new initialize/tools-list passed through the same still-running managed tunnel after the target returned without reconnecting it. This supports keeping the managed tunnel alive for ordinary Codexless-only restarts and moves the next architecture work to a separately owned detached one-shot restart helper with durable operation receipts. Tunnel readiness alone is not treated as backend-recovery proof because the isolated runtime could remain nominally ready while the target path was absent.  The project owner selected the previously preserved runtime-maintenance and phone/device-access gaps as the next stage after Research 120/121 closed. The repository already owned these under AB-001, AB-002, AB-006 and AB-017. Initial evidence now sharpens the architecture: the installed tunnel-client v0.0.13 already provides native managed-runtime commands (`runtimes connect/list/status/stop/rm/cleanup`), while ordinary ADS workspace authority correctly cannot initialize its default user-profile state directory. The same native command works when its state root is redirected into a bounded admitted directory, confirming that the remaining problem is a separate host-runtime state/credential/lifecycle authority class rather than missing tunnel lifecycle functionality. A Codexless-served action also cannot safely synchronously kill Codexless or the tunnel carrying its own request and still guarantee a response, so the permanent design must use a separately owned bounded supervisor/deferred lifecycle mechanism rather than generic process authority. Current OpenAI documentation also states that MCP apps are web-only and unavailable on mobile, so the earlier phone `401 tunnel_active_organization_required` is no longer treated as merely a local tunnel failure. The next empirical phone work separates native mobile app from mobile-browser ChatGPT web before any custom phone surface is considered. Codexless remains live as `0.1.1-preview.17-office-file-link` with 61 tools and tunnel HTTP 200/200.

The manual-upload baseline remains decisive. The user can already attach supported files, including large PDFs, directly to ChatGPT. Therefore the active work is about automatic direct source access from authorized local roots, not about having another model interpret local files for ChatGPT.

Existing direct-access results remain accepted: bounded local text through `codex.read_many`, local PNG/JPEG/WebP through `codex.image_read`, deterministic PDF text through `codex.document_read`, rendered PDF pages through `codex.document_render`, and whole-PDF host materialization through `codex.document_file_link` within the clean observed 7,417,428-byte PASS to 7,993,210-byte FAIL interval.

Checkpoint 309 added one narrowly scoped direct-host experiment before PDF splitting. The fresh disposable qualification exposed the new probe tools, mounted the MCP App, and visibly completed `ui/initialize`. The host snapshot reported `updateModelContext: {}` with no `resourceLink` property. Under the MCP Apps capability schema, `resourceLink?: {}` is the explicit modality advertisement, so the current bounded result is `UPDATE_MODEL_CONTEXT=ADVERTISED` and `UPDATE_MODEL_CONTEXT_RESOURCE_LINK=NOT_ADVERTISED`. The planned tiny-PDF `resourceLink -> ui/update-model-context` test is therefore skipped for this host. Validation 068 is the detailed evidence.

The user refreshed `ADS Codexless Local Bridge` in this existing persistent conversation after the controlled restart. ChatGPT-side tool rediscovery nevertheless retained the older callable projection and did not expose the three newly added probe tools. A separate fresh disposable conversation then exposed the new probe tools successfully. The combined result now localizes the behavior: the live 59-tool publication was valid, same-chat refresh retained a stale callable projection, and a fresh chat acquired the new projection.

The temporary exact-root `codexless-live` ordinary workspace admission used most recently for the Checkpoint 317 192 MiB source publication was removed after verification. The durable registry is now revision 17 / content hash `49f4c56a32b75f5d40ec07333394650bb2e71a69214c6ce3ca88241e70163557` with `ads-public`, `ads-local-runtime`, `ads-private`, `big-data-statistics`, and `machine-learning`.

The private local-runtime repository is synchronized exactly to `origin/main` at `ac3e05de0ebd9553eafb322ce19ec17539f1c09d` with `RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS` and `postflightOk=true`. It durably preserves the complete Office file-link candidate, the live AB-020 bounded private-integrity correction, the qualified Research 120 hybrid PDF implementation, and earlier Astra/Browser/runtime evidence. AB-020 is closed for the reproduced tracked-path scaling defect: a restarted live private semantic push passed at 32,813 tracked-path bytes and the later complete Office-candidate push passed at 40,013 bytes without widening the generic command-output envelope. The later Windows regression-cleanup hardening is also preserved at the current private head.

The deterministic multi-native-PDF `document_file_link` qualification remains a real fallback, and both first-class large-source fallback channels remain fully qualified. Research 120 now defines and implements their automatic route selection and derived-artifact lifecycle. The complete private hybrid-PDF suite passes 51/51 tests, including cache restart reuse, deterministic regeneration after eviction, atomic failed-generation cleanup, source-drift invalidation, native split render equivalence, cached embedded text, cached page vision, cached PDF resources, >192 MiB page-isolation text/render, MCP facade projection, native-result bounding, managed-cache pruning, and the two new direct-render serialization/fail-closed cases. Real read-only planning on `51.Deep Learning2.annotated.pdf` still produces bounded native parts with oversized pages 16 and 49 routed to text/render fallback. The public 192 MiB `document_read` and `document_render` envelope and the preview.16 `codex.pdf_access` facade are already live-qualified for the earlier routes. The renderer-serialization correction is installed, restarted and live-qualified. The formerly failing low-level two-page render, the fresh-host five-call intent matrix, and the >192 MiB public isolation routes all pass. Research 120 therefore has no remaining PDF route-class qualification in its accepted scope.

Two earlier cross-cutting Codexless corrections remain live-qualified. Formal Codex turns preserve the initial `Call Codex?` consent and bounded permission profile while using App Server `approvalPolicy=on-request` with `approvalsReviewer=auto_review`; the PowerShell wrapper classifier also allows documentation/search/here-string data containing `Codex` while genuine wrapped Codex CLI execution remains blocked.
Checkpoint 279 remains fully accepted beneath this research boundary: `workspace-standard` supports explicit ordinary non-Git exact-root admission and Codexless `0.1.1-preview.9` / `codexless-public-preview-v2` exposes 52 MCP tools including first-class `codex.document_read`. At that qualification boundary `big-data-statistics` had only `read`; Research 117 later added `agent` explicitly for the bounded reuse experiment while retaining no write/browser/Git capability. A fresh disposable ChatGPT conversation had already invoked `codex.document_read` against a real PDF and returned bounded embedded text plus source/parser/page provenance with no OCR and no file mutation. Validation 039 remains the decisive baseline qualification evidence.

The PDF parser is hardened out of the main Codexless event loop into a dedicated bounded Node child process with a 384 MiB V8 old-space ceiling, 30-second default hard deadline, bounded protocol output, Node permission restrictions, disabled PDF JavaScript evaluation/system-font lookup/worker fetch, and deterministic termination/recovery on timeout. The installed source admits a bounded 192 MiB PDF snapshot and revalidates identity/size after reading; the parser child uses an exact declared-size input buffer and zero-copy `Uint8Array` view to avoid unnecessary whole-source duplication. The 192 MiB source change is now live-qualified after restart. The private cached-artifact text adapter reuses the same pinned `pdfjs-dist@5.4.624` contract through a server-resolved owned dependency root rather than an ad-hoc junction or copied dependency tree.

The workspace registry is now revision `17`, content hash `49f4c56a32b75f5d40ec07333394650bb2e71a69214c6ce3ca88241e70163557`, with `ads-public`, `ads-local-runtime`, `ads-private`, `big-data-statistics`, and `machine-learning`. `ads-private` has the full supported project-workspace capability set under the dedicated `private-companion` Git integrity policy and server-owned `origin` remote while remaining a private knowledge complement only. Temporary exact-root `codexless-live` read/write admissions have been used only for bounded one-time live publication work, most recently the Checkpoint 317 192 MiB source publication, and removed immediately after publication/test verification. `big-data-statistics` has only `read` and `agent`; `machine-learning` remains strictly `read` only. Neither personal source workspace has write, browser, or Git capability. Exact personal roots remain machine-local rather than public project authority.

`docs/OPEN_ARCHITECTURE_BACKLOG.md` is now the durable index for explicit future architecture ideas and deferred side tracks. It preserves, among other items, mobile/device-independent connector access, narrow `%LOCALAPPDATA%` runtime-maintenance authority, autonomous Codex supervision/wakeup, active-turn writer transfer, Rich Card actionability, shared spectator synchronization, v17 semantic viewer work, broader host-capability taxonomy, the reproduced reconstruction-to-operational-authority routing gap, a backlog/open-question discoverability audit, high-recall new-session reconstruction, an explicit nested-workstream/resume graph, Knowledge Map topic-saturation risk, and an audit of scattered known weaknesses/deferred architecture triggers so anticipated limitations can be surfaced before they are rediscovered through failure. It is an index, not a replacement for `CURRENT_STATE.md`, `OPEN_QUESTIONS.md`, research, validation evidence, or accepted specifications.

Checkpoint 278 remains the accepted Research 116 core boundary: live flexible multi-repository authority, explicit two-layer admission of the private `autonomous-data-science-system-local-runtime` workspace, reviewed non-secret runtime-repository bootstrap, the private authenticated Git transport correction, and end-to-end generalized fetch/push qualification against `ads-local-runtime`.

The stable architecture now supports explicit register/update/remove of ordinary filesystem/project roots without another MCP schema publication. Per-workspace capability checks remain server-owned; semantic Git selects only `workspaceId`, derives branch/upstream dynamically, preserves the registered remote and integrity policy, and exposes no caller-selected cwd/URL/refspec/credentials/config/profile/sandbox/force inputs. Authenticated private Git is proven through the bounded host-network substrate. The latest preserved local-runtime boundary is `386813d1a31afd6748ad829c2f1dab3ea1bb89f4`. It preserves the live AB-020 integrity correction, the complete preview.17 Office file-link candidate, the qualified Research 120 hybrid-PDF core/facade, and earlier host-capability, Astra Phase 2 and GPT-5.6 Sol Browser evidence in private history. The latest private push passed `RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS`, exact local/remote equality, clean tracked postflight, and `postflightOk=true`.

The public baseline immediately before Checkpoint 305 preservation was `30437ff9df9a9bfcedcba8841c65e68fc309549a`, which already included the AB-028 Astra follow-up obligation. The known protected `.tmp/pytest-*` warning residue remains untouched.

The live Codexless server is now `0.1.1-preview.17-office-file-link` with 61 source tools and `codexless-public-preview-v2`; tunnel `/healthz` and `/readyz` both return HTTP 200. Fresh disposable ChatGPT conversations have qualified the complete accepted PDF route family and now the DOCX/PPTX/XLSX `codex.file_link` whole-file matrix end to end. The current persistent conversation still demonstrates the historical AB-008 same-chat projection behavior for newly added tools, while the refreshed fresh chat successfully acquired and executed `codex.file_link`. The existing PDF source ceilings, native `auto_review`, direct-Codex guard and AB-020 bounded integrity scanner remain otherwise unchanged.

Validation 035 now preserves a separate supervision-liveness gap discovered during the active Research 116 Codex candidate task. After ChatGPT approved one in-turn command and ended its response, Codex resumed, reached a second approval shortly afterward, and remained blocked until the user sent another message. The Rich Task Card could reflect `Action required`, but ChatGPT itself did not autonomously wake to inspect/resolve the new state. The same reproduction also reinforces the open question of whether writer ownership can be cooperatively transferred/reacquired during an active turn rather than only through the already-verified idle archive/unarchive/rebind handoff. This is now a first-class Codexless research/architecture issue, not an incidental UI observation.

The private runtime repository now preserves reviewed non-secret `.ads-private/codexless` implementation evidence without becoming a competing ADS project-development authority. Its trust/bootstrap sequence is closed: supported App Server `config/batchWrite` trust qualification passed against Codex `0.152.1`, the explicit Codexless workspace registry admission created `ads-local-runtime`, the first reviewed import produced root commit `0ce61ba794929ee71c555d480a936fdced28ef2e`, and the one-time host bootstrap created `origin/main`. Validation 038 then closed the authenticated-private Git boundary after the published host-network correction: generalized fetch succeeded and generalized push returned up to date with `RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS`, `retried=false`, exact local/remote equality, clean tracked postflight, and `postflightOk=true`.

Checkpoint 276 opened Research 113, a comprehensive evidence-driven study of the current OpenAI Codex/App Server ecosystem, the public Codexless project, and relevant issues, pull requests, discussions, source, schemas, tests, and community design ideas before further local Codexless architecture changes. That broader research remains active. The project owner continues to pause both v17 live-viewer implementation and reviewed Source Vault ingestion while this Level-2 research phase and its current authority subproblem are active.

The v16 viewer is preserved as the current working experimental baseline. It was published successfully as `ui://toolwire/codex-task-card-v16.html` on public Codexless `0.1.1-preview.7` with `toolCount 48`. After the controlled Codexless restart, tunnel reconnect, ChatGPT plug-in refresh, and a fresh disposable test chat, live transport, automatic card updates, streamed command output, and terminal transition all worked. A separate native Codex Desktop recording showed that v16 still lacks Desktop-style semantic grouping and narrative hierarchy, so implementation is paused rather than prematurely polishing the event-log renderer.

Initial primary-source inspection already shows important upstream evolution, including explicit `Thread -> Turn -> Item` lifecycle semantics, history pagination without resume, thread status notifications, connection-scoped unsubscribe/unload behavior, experimental same-turn steering, persistent thread queues, structured command/file-change items, richer approval-reviewer paths, and expanded subagent/project/thread APIs. These are research candidates, not adopted ADS changes. Research 113 governs evidence classes, comparison methodology, and stop rules.

Research 114 now preserves the first deep official App Server capability baseline and ADS implications. Research 115 separately maps the active public Codexless architecture/PR landscape, including lifecycle-state consolidation, fail-closed same-turn steering, Browser elicitation policy, and the need to distinguish current public source from lagging README/tool-count documentation. `docs/research/CODEX_UPSTREAM_ADS_COMPARISON_MATRIX.md` is the living cross-source disposition index.

The completed integration architecture separates four layers:

```text
Codex thread persistence
Codex writer/process ownership
Codex Desktop sidebar/catalog reconciliation
durable cross-client thread identity and runtime-agent rehydration
```

H6 remains live: completed ADS Codex tasks expose the exact persisted `threadId` plus `codex://threads/<threadId>`, and the Rich Task Card's `Open in Codex Desktop` handoff was verified against a real same-thread Desktop continuation.

The durable identity is `threadId`; Codexless `agentRef` values are ephemeral runtime handles. Model-free `codex.agent_bind` remains verified, including re-binding after a complete Codexless restart.

The final guided handoff used exact persisted thread `01a063b1-0d21-7011-b17c-514eb0359a15`. After source marker `PROCEED_IN_CHAT_UI_SOURCE_COMPLETE`, the user opened the exact thread in Desktop, selected `Proceed in Chat`, archived it while Desktop remained running, and selected `I've archived it ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â Continue`. The card reached `Ready in Chat` through model-free verification, unarchive, and rebound without starting a model turn.

A separate stateless MCP request resolved exact task reference `task_e89b4b3c-0e43-40a2-b3d3-aa32a9fe31e7` to fresh `agentRef` `agent_645095a6-efa5-4224-a8c1-029da74abea7`, the same `threadId`, `boundThread=true`, `status=idle`, `canSend=true`, `turnId=null`, `pendingApproval=null`, `modelTurnStarted=false`, and `handoffStatus=ready`. This proves Ready survives across distinct requests through runtime-lifetime shared `agentPreviewState`; it remains intentionally non-persistent across process restart.

Ordinary metered `codex.agent_send` then resumed the same thread. Turn `01a063b5-c8d9-7692-b8b1-d23a0a55a7ea` completed exact result `PROCEED_IN_CHAT_END_TO_END_COMPLETE`, with `thread/reacquired`, `turn/accepted`, `turn/started`, `turn/completed`, `thread/released`, and `app-server/released` observed. A second same-thread cycle then visibly completed markers `SECOND_DESKTOP_CYCLE_SOURCE` and `SECOND_CHAT_CYCLE_COMPLETE` after the two first-cycle markers. This proves repeatable cooperative handoff on one durable thread.

Codexless remained public version `0.1.1-preview.7`, `toolCount 48`, with tunnel ready HTTP 200. Desktop briefly showed stale archived presentation state after backend reacquisition; `Dearchiveren en openen` failed, but a Desktop restart plus the exact thread deep link restored the correct conversation. This is a Desktop UI synchronization/cache quirk, not a backend failure.

No forced writer stealing, private Codex DB/session/catalog write, Desktop forced termination for handoff, permission widening, or manual raw lifecycle workaround was used. Desktop voluntarily released by archive; Chat verified, unarchived, rebound and resolved Ready model-free. Only ordinary metered `agent_send` began the continuation turn. The guided handoff UX/integration is closed for current scope.

Checkpoint 274 was originally local-only because the direct sandboxed push could not access the configured Git credential-manager / VS Code askpass path. Checkpoint 275 was then deliberately left uncommitted at the time because its originating reconciliation turn did not reach a clean finalization boundary. Validation created repository-local `.tmp/pytest-checkpoint-275/` residue and then proposed an exact-path-guarded cleanup containing `Remove-Item -Recurse -Force`. The user approved that pending Codex action, but the outer OpenAI tool-dispatch safety layer blocked the programmatic approval before it reached Codexless; the request type also did not support decline. That historical interruption remains valid evidence, and the `.tmp` warning remains known residue. The preservation was later committed as `1b9bbd2`, Checkpoint 274 plus the later Checkpoint 275/276 research boundary were included in the exact public HEAD `94e7bf7a011c202d2c9def718e3f2eefd066f1b8`, and the new bounded semantic push subsequently synchronized that exact HEAD to origin. Nothing was deleted through the blocked cleanup action.

The earlier direct synchronization result remains accepted for the exact frozen contracts:

```text
codex.git_fetch_origin
    VERIFIED
    fixed git fetch origin

codex.git_pull_ff_only
    VERIFIED
    fixed trusted ADS branch/upstream
    strict fast-forward only
    clean-tree fail-closed preconditions
    no caller-controlled Git arguments
```

The successful strict-fast-forward pull was also followed by another successful routine bounded synchronization using the same accepted contract.

Research 105 remains:

```text
ACCEPTED_FOR_ADS_LOCAL_EXECUTION
```

Codexless remains a replaceable bounded local-execution transport. It is not project authority, a mandatory core dependency, a permission source, or an unrestricted host-control path.

The direct synchronization feasibility question that paused Source Vault work is closed for its exact accepted scope.

---

## What the investigation established

The investigation distinguished multiple execution layers rather than treating every failed attempt as the same failure:

```text
ChatGPT / OpenAI outer safety and dispatch
MCP action contract
Codexless routing and public surface
Codex authority/profile resolution
network authority
Codex command/exec sandbox
Windows filesystem ACLs / capability identities
Git semantics
repository branch/upstream/cleanliness state
postcondition verification
```

Key evidence sequence:

```text
generic codex.command_exec carrying Git
    BLOCKED BEFORE LOCAL EXECUTION

bounded codex.git_fetch_origin
    DISCOVERED
    DISPATCHED
    EXECUTED THROUGH MODEL-FREE CODEX command/exec
    EXIT 0

bounded codex.git_pull_ff_only first dispatch
    DISCOVERED
    DISPATCHED
    REACHED LOCAL EXECUTION
    FAILED AT .git/FETCH_HEAD WITH PERMISSION DENIED
    REPOSITORY UNCHANGED

read-only host diagnosis
    RECURRENT WINDOWS WORKSPACE-CAPABILITY DENY CONFIRMED ON .git
    INHERITED DENY CONFIRMED ON .git/FETCH_HEAD
    DEDICATED .git WRITABLE CAPABILITY STILL HAD MODIFY

guarded host ACL repair
    BACKUP CREATED
    EXACT TWO MATCHING EXPLICIT DENY RULES REQUIRED
    TWO -> ZERO IN-MEMORY GUARD PASSED
    ACL WRITTEN ONLY AFTER GUARDS PASSED
    POST-REPAIR DENY ABSENT
    EXPECTED MODIFY ALLOWANCES PRESENT

second separately authorized semantic pull dispatch
    DISPATCHED EXACTLY ONCE
    EXIT 0
    STRICT FAST-FORWARD VERIFIED
    CLEAN POSTFLIGHT VERIFIED
    OLD-HEAD ANCESTRY VERIFIED

later routine bounded synchronization
    EXIT 0
    STRICT FAST-FORWARD VERIFIED AGAIN
```

The first failed semantic pull was useful evidence because it localized the first failing layer after proving earlier layers had succeeded.

---

## Accepted Git boundary remains deliberately narrow

Accepted:

```text
fixed semantic fetch from origin
fixed trusted-branch strict-fast-forward pull
bounded network + Git-metadata authority
clean-tree and repository-state fail-closed checks
readOnly downscope to :read-only
postflight equality / cleanliness / ancestry verification
```

Not accepted merely because pull succeeded:

```text
arbitrary Git commands
commit
push
force push
reset
checkout
rebase
merge commits
arbitrary branch / remote / refspec selection
public codex.process
unrestricted host access
arbitrary or unguarded ACL repair
permission widening to bypass a guard
```

Exact accepted capability is governed by:

```text
docs/local_execution/SEMANTIC_PULL_ACCEPTANCE.md
```

---

## Durable operational and investigation knowledge

Repository-owned operational procedures:

```text
docs/local_execution/OPERATIONS.md
docs/local_execution/AUTHORITY_BOOTSTRAP.md
docs/local_execution/ACL_INTEGRITY_GATE.md
docs/local_execution/SEMANTIC_PULL_ACCEPTANCE.md
```

The authority bootstrap is part of reproducible ADS operation. A healthy Codexless process or ready tunnel is not sufficient evidence that the ADS-specific `ads-direct-git` authority is active.

The Windows Git-metadata ACL condition is lifecycle-sensitive. The problematic workspace-capability DENY was observed to recur after later lifecycle activity even while the logical profile still reported `.git` as writable. The exact recreating lifecycle event was not isolated, so no stronger causal claim is made.

After relevant Codex/Codexless/sandbox lifecycle changes:

```text
restore and verify the ADS authority bootstrap
-> run the read-only ACL integrity gate before direct Git mutation
-> stop if a DENY is detected
```

ACL repair is never automatic merely to make a Git operation pass. A project-owner standing authorization now exists only for the exact recurring registered-repository workspace-capability DENY defect after fresh read-only diagnosis matches the guarded contract in `ACL_INTEGRITY_GATE.md`; any drift remains a stop condition.

Broader reusable lessons are preserved in:

```text
docs/local_execution/DIRECT_GIT_INVESTIGATION_LESSONS.md
```

The central methodological rule is disciplined claim scope:

```text
a failed route is not automatically an impossible capability
```

when multiple contracts or layers can still explain the result.

Future cross-layer investigations should localize the failure, research relevant contracts when ambiguity remains, design the smallest safe discriminating experiment, keep it fail-closed, preserve negative evidence by layer, change only the implicated layer, and keep successful claims bounded to the exact verified contract.

---

## Current Source Vault state

The Source Universe remained untouched throughout the direct Git investigation.

Current permanent Source Vault boundary:

```text
permanent Source Registry           MIGRATED / VERIFIED
Alembic head                        0003_source_universe
SQLite tables                       33
first permanent corpus compare      20 / 20 MATCH
DIFFERENT_ARTIFACT                  0
MISSING_LOCAL_SOURCE                0
ADDITIONAL_LOCAL_SOURCE             0
source ingestion                    NOT STARTED
working-store integrity audit       PENDING
independent encrypted backup proof  PENDING
clean restore + restored audit      PENDING
Course 2                            BLOCKED
```

The original source root and other machine/storage coordinates remain `RESOLVED_PRIVATE`. Their exact values must be retrieved from the accepted private/local continuity layer only when concrete execution requires them.

No Source Universe, Source Vault, original corpus, credential, backup payload, or recovery state was changed by the Codexless/direct-Git work.

---

## Preserved next Source Vault action (currently paused)

When the current Research 113 Level-2 route closes, the preserved next Source Vault action is:

```text
reviewed ingestion of the frozen 20-entry first corpus
```

Then:

```text
working-store integrity audit
-> deterministic backup staging
-> client-side encryption
-> independent remote replication
-> remote retrieval
-> encrypted-object digest reproduction
-> decryption
-> clean restore
-> restored integrity audit
-> Course 2 unblock only after the accepted recovery proof succeeds
```

The governing Source Vault procedure is:

```text
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
```

---

## Repository integrity and development method

Research 103-108 and Specifications 024-027 continue to govern repository integrity and continuity.

Development Method v0.9 remains current.

Canonical numbered Checkpoint 353 is now the current meaningful project boundary. Checkpoint 353 / Validation 111 live-qualify first production self-restart, durable status, tunnel preservation and duplicate suppression. Checkpoint 352 remains the fresh-host schema qualification. Checkpoint 352 / Validation 110 qualify the refreshed fresh-chat structured host schema for preview.19 without mutation. Checkpoint 351 remains the process-live local flat-schema activation qualification. Checkpoint 351 / Validation 109 qualify active preview.19, exact runtime identity and process-live local flat MCP schema without yet invoking self-restart. Checkpoint 350 remains the source-published/restart-pending boundary. Checkpoint 350 / Validation 108 preserve successful preview.19 source publication and independent installed-hash verification with the active process deliberately still preview.18. Checkpoint 349 remains the qualified publication preflight. Checkpoint 349 / Validation 107 qualify the exact guarded preview.19 schema-correction publication package with two no-publish passes and no live mutation. Checkpoints 347-348 remain the fresh-host failure localization and flat-schema candidate qualification. Checkpoint 347 / Validation 105 preserve the fresh-host schema projection failure and deliberate no-mutation decision. Checkpoint 348 / Validation 106 qualify the flat preview.19 host-schema correction and actual MCP wire-schema regression without live mutation. Checkpoint 346 remains the preview.18 bootstrap activation/local-discovery qualification. Checkpoint 346 / Validation 104 qualify active preview.18 / 62 tools, exact runtime identity and local MCP discovery without yet invoking production self-restart. Checkpoint 345 remains the source-published/restart-pending boundary. Checkpoint 345 / Validation 103 preserve successful preview.18 source publication and exact installed-hash verification while the active process remains preview.17 / 61 tools. Checkpoint 344 remains the guarded publication-preflight qualification. Checkpoint 344 / Validation 102 qualify the guarded preview.18 publication helper and exact source/test replacement package with no live mutation. Checkpoint 343 remains the production-shaped exact-instance/direct-dispatch integration qualification. Checkpoint 343 / Validation 101 qualify the production-shaped exact-instance Codexless-only restart and 62-tool preview.18 integration candidate without live mutation. Checkpoint 342 remains the detached-helper survival qualification. Checkpoint 342 / Validation 100 qualify durable runtime-maintenance state and detached helper survival across a failed/timed-out caller wrapper. Checkpoint 341 remains the managed-tunnel backend recovery qualification. Checkpoint 341 / Validation 099 qualify functional same-process managed-tunnel recovery across a real local MCP target outage and establish tunnel-preserving Codexless-only restart as the preferred normal lifecycle architecture. Checkpoint 340 remains the Research 122 opening baseline. Checkpoint 340 opens Research 122 for runtime self-maintenance, lifecycle supervision and device-independent access; Validation 098 preserves the initial repository/upstream/local managed-runtime evidence and the current mobile product constraint. Checkpoint 339 remains the completed Office file-link matrix boundary. Checkpoint 339 preserves the successful fresh-chat DOCX/PPTX/XLSX `codex.file_link` matrix, exact host materialization/source identity, native structure/embedded-asset fidelity evidence, fallback disposition, Research 121 closure and qualification-scratch cleanup. Validation 097 is the exact evidence. Checkpoint 338 remains the preview.17 live/fresh-chat-discovery boundary. Checkpoint 338 preserves live preview.17 / 61-tool activation, tunnel 200/200, exact new-source hash verification, and the persistent-chat stale `codex.file_link` projection. Validation 096 is the exact evidence. Checkpoint 337 remains the live-source-published/restart-pending boundary. Checkpoint 337 preserves successful preview.17 host publication, independent exact installed-hash verification for all nine publication targets plus semantic-Git preservation, and the explicit pre-restart process boundary. Validation 095 is the exact evidence. Checkpoint 336 remains the atomic replacement harness requalification boundary. Checkpoint 336 preserves the second preview.17 host publication failure, exact rollback verification, the corrected Windows atomic forward/rollback replacement primitives, new publication-primitive smoke coverage, and two successful complete requalification preflights. Validation 094 is the exact evidence. Checkpoint 335 remains the Windows temporary-cleanup harness requalification boundary. Checkpoint 335 preserves the safely contained first preview.17 host publication attempt, zero-live-mutation proof, Windows cleanup harness hardening, private preservation at `386813d1a31afd6748ad829c2f1dab3ea1bb89f4`, and two successful publication requalification preflights. Validation 093 is the exact evidence. Checkpoint 334 remains the original preview.17 guarded publication-preflight qualification. Checkpoint 334 preserves the exact guarded preview.17 Office file-link publication preflight. Validation 092 contains the nine-file package, hash bindings and regression evidence. Checkpoint 333 closes the concrete AB-020 scaling defect and preserves the Office candidate durably at private head `fa5cc2a6c3e6d47f45961ab475c2ac66c24aff0b`. Checkpoint 332 remains the AB-020 source-published/restart-pending boundary. Checkpoint 332 preserves successful AB-020 host publication, independent installed-hash verification, healthy pre-restart preview.16/tunnel state, and the explicit restart-pending boundary. Validation 090 is the exact evidence. Checkpoint 331 preserves the qualified Office file-link scratch candidate and deterministic host fixtures. Checkpoint 330 remains the bounded private-integrity candidate/publication-preflight boundary. Checkpoint 330 preserves the bounded AB-020 private-integrity enumeration candidate, its 8/8 regression suite, private preservation at `7e70bd05e4da76ff1ad260b2b1cbdc5c1d65a3fb`, source-control temporary-artifact cleanup, and guarded live-publication preflight. Validation 088 is the exact evidence. Checkpoint 329 remains the Research 121 reuse-first Office handoff baseline. Checkpoint 329 opens Research 121's reuse-first non-PDF Office handoff work after the PDF route family closed: current OpenAI product evidence supports DOCX/PPTX/XLSX uploads, MCP resource links are MIME-generic, and local implementation inspection identifies the existing PDF whole-file resource lifecycle as the preferred transport substrate for a narrow allowlisted `codex.file_link` candidate. Validation 087 preserves the evidence baseline and Research 121 governs the architecture. Checkpoint 328 preserves the successful >192 MiB public facade isolation qualification across text, visual and mixed routes, including managed-artifact reuse, original source-page provenance, direct ChatGPT image consumption, unchanged source identity and no source-adjacent derived files. Validation 086 contains the exact route, artifact, hash, warning and source-cleanliness evidence. Checkpoint 327 preserves the successful fresh disposable five-call `codex.pdf_access` intent matrix after the renderer repair, and Checkpoint 326 preserves the successful controlled restart and low-level live qualification of the formerly failing two-page `codex.document_render` path. Checkpoint 325 remains the source-published / restart-pending boundary. Checkpoint 325 preserves the successful live-source publication and independent installed-hash verification while explicitly keeping the running process restart-pending. Validation 083 is the detailed evidence, and `docs/local_execution/OPERATIONS.md` governs the next full controlled restart. Checkpoint 324 preserves the guarded publication preflight: the private 51/51 renderer candidate and a matching adapted installed render regression pass the complete seven-script staged public regression set, exact old/new hashes are bound, and no live file has yet been modified. Validation 082 is the detailed evidence; the next action is ordinary-host PowerShell publication with the exact qualified helper, followed by independent installed-hash verification before restart. Checkpoint 323 preserves the qualified direct-render serialization candidate: the public four-page request contract is unchanged, but each selected source page is rendered through a separate bounded read-only sandbox execution before ordered recombination and existing aggregate/source-drift checks. The focused serialization cases pass 2/2 and the full hybrid-PDF private suite passes 51/51 at private boundary `ad61a5619165ec5675e75daecdb4fdb29ea6f19a`. Validation 081 is the detailed evidence. The installed preview.16 renderer has not yet been changed, so guarded renderer-only publication and controlled restart remain next. Checkpoint 322 preserves the failed fresh-chat five-call `codex.pdf_access` intent matrix and the localized multi-page direct-render transport gap: text and auto-text routes passed; visual, mixed and auto-visual routes failed at the renderer; the same two pages fail when rendered together but pass individually with the already-qualified Checkpoint 321 image hashes. Checkpoint 321 preserves the fresh-chat end-to-end `codex.pdf_access` native hybrid qualification on the live preview.16 / 60-tool runtime: automatic `native-parts-plus-page-fallback` routing over the 78,874,939-byte Deep Learning 2 source, fourteen bounded native PDF resource links, direct embedded text and rendered images for individually oversized pages 16 and 49, direct ChatGPT inspection of both images, 14/14 host materialization of the native resources, and ordinary ChatGPT-side inspection of one materialized PDF part. Checkpoint 320 remains the simpler fresh-host native split qualification, and Checkpoint 319 remains the guarded facade source-publication and restart-pending boundary now superseded operationally by the successful preview.16 activation. The complete private hybrid-PDF suite now remains 51/51 PASS and the complete staged public regression remains accepted at the 60-tool surface. Checkpoint 318 remains the core-qualification boundary that closed the Checkpoint 317 restart-pending state by live-qualifying the 192 MiB direct text/render envelope and preserving deterministic routing, source profiling, native splitting, >192 MiB page/range isolation, managed content-addressed cache reuse/regeneration, cached text/render/resource adapters, native split render equivalence and the high-level `PdfAccessOrchestrator`. Checkpoint 317 remains the accepted architecture and 192 MiB source-publication boundary. Checkpoint 316 remains the successful same-chat end-to-end large-source text qualification, and Checkpoint 314 remains the successful same-chat end-to-end large-source visual qualification. Checkpoint 315 and Checkpoint 313 preserve the respective source-publication boundaries. Checkpoint 312 remains the Machine Learning generalization result that native PDF page-range splitting is not sufficient for all oversized PDFs because several individual pages exceed the host-qualified envelope by themselves. Checkpoint 311 remains the successful multi-native-PDF direct-access qualification for the 11,825,407-byte source. Checkpoint 310 remains the resolved fresh-host result that `updateModelContext` is advertised without the `resourceLink` modality. Checkpoint 309 remains the live 59-tool host-capability diagnostic publication and same-conversation stale-projection boundary. Checkpoint 308 remains the governing objective correction that restores direct ChatGPT local-machine file access through Codexless and separates it from delegated document analysis and future ADS product architecture. Checkpoint 307 remains the historical first held-out Astra semantic-worker `AMBIGUOUS` result and environment diagnosis. Checkpoint 306 remains the completed GPT-6 Astra Phase 2 reconciliation and preserved non-live source-bound semantic-evidence candidate. Checkpoint 305 remains the completed GPT-5.6 Sol Browser compatibility baseline. Checkpoint 304 preserves the live-qualified direct-Codex guard correction, while Checkpoint 303 preserves the localized resource-link host materialization interval, direct-HTTPS rejection, native `auto_review` live qualification, and Browser fallback opening. Checkpoints 302-293 remain the detailed progression from intermediate/large resource-link host tests through the original resource-link publication-preflight boundary. Checkpoint 292 preserves the live embedded-PDF host result, Checkpoints 291-280 preserve the preceding document-handoff/reuse-first/render/image experiments, and Checkpoint 279 remains the accepted `workspace-standard` + `codex.document_read` baseline.

The public repository remains the sole project-development authority.

Any public branch mutation must pass Repository Integrity on its exact resulting HEAD before an exact-target `PUBLIC_REPOSITORY_INTEGRITY=PASS` claim is made.

Private continuity remains an orthogonal claim and must be reconciled to the exact public boundary when required for planned conversation rotation.

---

## Model collaboration state

The obsolete MC-0009 direct-Git feasibility collaboration has been retired by explicit project-owner decision. It never received a Claude Message 001; its bounded Git question was later resolved experimentally, its thread directory has been removed, and it is no longer a live routing obligation. Historical validation prose may retain provenance that MC-0009 existed at the time.

MC-0010 is now `OPEN / PARALLEL UPSTREAM RESEARCH`. It is a current-context `REVIEWED` collaboration, not a blind-to-candidate pass. Claude is intentionally allowed to inspect the current ADS Codexless architecture, v16/Desktop comparison, Research 113, and relevant validation history, then independently research and challenge the upstream ecosystem. ChatGPT research may continue while the Claude contribution is unavailable, but the separate report should be considered before final architecture reconciliation when practically available.

---

## Current canonical route

```text
docs/checkpoints/398_github_app_installed_all_repositories_private_key_cleanup_next.md
docs/local_execution/validation/155_github_app_installed_all_personal_repositories.md
docs/research/github_app_live_registration_20260909.json
docs/checkpoints/397_github_app_registered_private_key_install_gate_next.md
docs/local_execution/validation/154_github_app_registered_private_key_install_gate_discovered.md
docs/research/github_app_live_registration_20260909.json
docs/checkpoints/396_github_extended_app_precreation_verified_owner_create_now.md
docs/local_execution/validation/153_github_extended_app_precreation_ui_verified.md
docs/checkpoints/395_github_extended_permission_manifest_frozen_owner_creation_next.md
docs/local_execution/validation/152_github_extended_permission_manifest_and_registration_prefill_frozen.md
docs/research/GITHUB_APP_EXTENDED_PERMISSION_MANIFEST.md
docs/research/github_app_extended_permission_manifest.json
docs/research/GITHUB_APP_EXTENDED_REGISTRATION_CONFIGURATION.md
docs/research/github_app_extended_registration_configuration.json
docs/checkpoints/394_github_live_permission_inventory_complete_extended_manifest_next.md
docs/local_execution/validation/151_github_live_permission_ui_118_option_reconciliation.md
docs/research/GITHUB_APP_LIVE_PERMISSION_RECONCILIATION_20260909.md
docs/research/github_app_live_permission_inventory_20260909.json
docs/checkpoints/393_github_extended_permission_review_open_live_inventory_next.md
docs/local_execution/validation/150_github_extended_permission_review_opened.md
docs/research/GITHUB_APP_EXTENDED_PERMISSION_REVIEW.md
docs/checkpoints/392_github_app_registration_configuration_frozen_owner_creation_next.md
docs/local_execution/validation/149_github_app_registration_configuration_frozen_owner_creation_next.md
docs/research/GITHUB_APP_REGISTRATION_CONFIGURATION.md
docs/research/github_app_registration_configuration.json
docs/checkpoints/391_github_app_permission_manifest_frozen_registration_config_next.md
docs/local_execution/validation/148_github_app_rest_permission_manifest_frozen_graphql_probe_required.md
docs/research/GITHUB_APP_PERMISSION_MANIFEST.md
docs/research/github_app_permission_manifest.json
docs/checkpoints/390_github_authorization_fresh_host_pass_live_name_qualified_permission_manifest_next.md
docs/local_execution/validation/147_github_authorization_flat_fresh_host_and_live_plugin_name_qualified.md
docs/checkpoints/389_github_authorization_flat_schema_live_fresh_chat_requalification_next.md
docs/local_execution/validation/146_github_authorization_host_union_genericization_flat_schema_correction_live.md
docs/checkpoints/388_github_authorization_control_surface_live_fresh_chat_projection_next.md
docs/local_execution/validation/145_github_authorization_control_surface_live_local_mcp_qualified.md
docs/checkpoints/387_github_g0_keyring_generation_live_auth_control_surface_next.md
docs/local_execution/validation/144_github_g0_keyring_generation_live_activation_qualified.md
docs/checkpoints/386_github_g0_source_bootstrap_live_keyring_activation_next.md
docs/local_execution/validation/143_github_g0_source_bootstrap_release_live_qualified.md
docs/checkpoints/385_github_g0_immutable_dependency_generations_qualified_bootstrap_release_next.md
docs/local_execution/validation/142_github_g0_immutable_dependency_generation_release_architecture_qualified.md
docs/checkpoints/384_github_g0_runtime_integration_candidate_qualified_dependency_provisioning_next.md
docs/local_execution/validation/141_github_g0_main_runtime_integration_candidate_qualified.md
docs/checkpoints/383_github_g0_windows_keyring_qualified_runtime_integration_next.md
docs/local_execution/validation/140_github_g0_windows_keyring_host_roundtrip_qualified.md
docs/checkpoints/382_github_g0_private_candidate_qualified_keyring_runtime_next.md
docs/local_execution/validation/139_github_g0_auth_transport_private_candidate_qualified.md
docs/checkpoints/381_github_official_api_baseline_g0_contract_ready.md
docs/local_execution/validation/138_github_official_api_auth_and_first_contract_gaps_resolved.md
docs/research/GITHUB_API_AUTH_AND_CONTRACT_BASELINE.md
docs/checkpoints/380_github_schema_reconciled_g0_and_targeted_evidence_ready.md
docs/local_execution/validation/137_github_89_schema_final_reconciliation_contract_gaps_localized.md
docs/research/GITHUB_CONNECTOR_PREIMPLEMENTATION_EVIDENCE_GAPS.md
docs/checkpoints/379_github_native_schema_capture_complete_final_reconciliation_pending.md
docs/local_execution/validation/136_github_native_schema_capture_batch6_preserved.md
docs/checkpoints/378_github_native_schema_capture_batch5_preserved.md
docs/local_execution/validation/135_github_native_schema_capture_batch5_preserved.md
docs/checkpoints/377_github_native_schema_capture_batch4_preserved.md
docs/local_execution/validation/134_github_native_schema_capture_batch4_preserved.md
docs/checkpoints/376_github_native_schema_capture_batch3_preserved.md
docs/local_execution/validation/133_github_native_schema_capture_batch3_preserved.md
docs/checkpoints/375_github_native_schema_capture_batch2_preserved.md
docs/local_execution/validation/132_github_native_schema_capture_batch2_preserved.md
docs/checkpoints/374_github_native_schema_capture_batch1_preserved.md
docs/local_execution/validation/131_github_native_schema_capture_batch1_preserved.md
docs/research/github_connector_native_schema_capture.json
docs/research/GITHUB_CONNECTOR_SCHEMA_CAPTURE.md
docs/checkpoints/373_github_fresh_projection_exact_inventory_corrected_schema_capture_opened.md
docs/local_execution/validation/130_github_fresh_projection_exact_inventory_correction_and_schema_capture_opened.md
docs/research/github_connector_89_action_inventory.json
docs/research/GITHUB_CONNECTOR_PARITY_MATRIX.md
docs/research/123_github_connector_capability_parity_and_codexless_runtime_bridge_architecture.md
docs/checkpoints/347_runtime_maintenance_fresh_chat_schema_projection_failed_localized.md
docs/local_execution/validation/105_runtime_maintenance_fresh_chat_schema_projection_failed_localized.md
docs/checkpoints/353_runtime_maintenance_first_live_self_restart_qualified.md
docs/local_execution/validation/111_runtime_maintenance_first_live_self_restart_qualified.md
docs/checkpoints/352_runtime_maintenance_preview19_fresh_chat_schema_qualified.md
docs/local_execution/validation/110_runtime_maintenance_preview19_fresh_chat_schema_qualified.md
docs/checkpoints/351_runtime_maintenance_preview19_bootstrap_activation_qualified.md
docs/local_execution/validation/109_runtime_maintenance_preview19_bootstrap_activation_qualified.md
docs/checkpoints/350_runtime_maintenance_preview19_live_source_published_restart_pending.md
docs/local_execution/validation/108_runtime_maintenance_preview19_live_source_published_restart_pending.md
docs/checkpoints/349_runtime_maintenance_preview19_publication_preflight_qualified.md
docs/local_execution/validation/107_runtime_maintenance_preview19_publication_preflight_qualified.md
docs/checkpoints/348_runtime_maintenance_preview19_flat_schema_candidate_qualified.md
docs/local_execution/validation/106_runtime_maintenance_preview19_flat_schema_candidate_qualified.md
docs/checkpoints/346_runtime_maintenance_preview18_bootstrap_activation_qualified.md
docs/local_execution/validation/104_runtime_maintenance_preview18_bootstrap_activation_qualified.md
docs/checkpoints/345_runtime_maintenance_preview18_live_source_published_restart_pending.md
docs/local_execution/validation/103_runtime_maintenance_preview18_live_source_published_restart_pending.md
docs/checkpoints/344_runtime_maintenance_preview18_publication_preflight_qualified.md
docs/local_execution/validation/102_runtime_maintenance_preview18_publication_preflight_qualified.md
docs/checkpoints/343_runtime_maintenance_preview18_integration_qualified.md
docs/local_execution/validation/101_runtime_maintenance_preview18_integration_qualified.md
docs/checkpoints/339_office_file_link_fresh_chat_matrix_qualified_research121_complete.md
docs/local_execution/validation/097_office_file_link_fresh_chat_matrix_qualified.md
docs/checkpoints/338_office_preview17_live_fresh_chat_discovery_next.md
docs/local_execution/validation/096_office_preview17_restarted_live_fresh_chat_discovery_required.md
docs/checkpoints/337_office_preview17_live_source_published_restart_pending.md
docs/local_execution/validation/095_office_preview17_live_source_published_restart_pending.md
docs/checkpoints/336_office_preview17_atomic_replacement_harness_requalified.md
docs/local_execution/validation/094_office_preview17_atomic_replacement_harness_requalified.md
docs/checkpoints/335_office_preview17_publication_retry_harness_requalified.md
docs/local_execution/validation/093_office_preview17_publication_retry_harness_requalified.md
docs/checkpoints/334_office_file_link_preview17_publication_preflight_qualified.md
docs/local_execution/validation/092_office_file_link_preview17_publication_preflight_qualified.md
docs/checkpoints/333_ab020_live_qualified_office_candidate_preserved.md
docs/local_execution/validation/091_ab020_live_qualified_office_candidate_preserved.md
docs/checkpoints/332_ab020_live_source_published_restart_pending.md
docs/local_execution/validation/090_ab020_live_source_published_restart_pending.md
docs/checkpoints/331_office_file_link_scratch_candidate_qualified.md
docs/local_execution/validation/089_office_file_link_scratch_candidate_qualified.md
docs/checkpoints/330_private_integrity_enumeration_candidate_publication_preflight_qualified.md
docs/local_execution/validation/088_private_integrity_enumeration_candidate_publication_preflight_qualified.md
docs/checkpoints/329_non_pdf_office_handoff_reuse_first_research_opened.md
docs/local_execution/validation/087_non_pdf_office_handoff_reuse_first_research_baseline.md
docs/research/121_non_pdf_file_capability_matrix_and_native_handoff_reuse.md
docs/checkpoints/328_hybrid_pdf_over_192mib_public_facade_isolation_qualified.md
docs/local_execution/validation/086_hybrid_pdf_over_192mib_public_facade_isolation_qualified.md
docs/checkpoints/327_hybrid_pdf_access_fresh_chat_intent_matrix_qualified.md
docs/local_execution/validation/085_hybrid_pdf_access_fresh_chat_intent_matrix_qualified.md
docs/checkpoints/326_hybrid_pdf_render_serialization_live_activation_qualified.md
docs/local_execution/validation/084_hybrid_pdf_render_serialization_live_activation_qualified.md
docs/checkpoints/325_hybrid_pdf_render_serialization_live_source_published_restart_pending.md
docs/local_execution/validation/083_hybrid_pdf_render_serialization_live_source_published_restart_pending.md
docs/checkpoints/324_hybrid_pdf_render_serialization_publication_preflight_qualified.md
docs/local_execution/validation/082_hybrid_pdf_render_serialization_publication_preflight_qualified.md
docs/checkpoints/323_hybrid_pdf_direct_render_serialization_candidate_qualified.md
docs/local_execution/validation/081_hybrid_pdf_direct_render_serialization_candidate_qualified.md
docs/checkpoints/322_hybrid_pdf_intent_matrix_render_transport_gap_localized.md
docs/local_execution/validation/080_hybrid_pdf_access_fresh_chat_intent_matrix_renderer_transport_failed.md
docs/checkpoints/321_hybrid_pdf_access_fresh_chat_native_hybrid_qualified.md
docs/local_execution/validation/079_hybrid_pdf_access_fresh_chat_native_hybrid_qualified.md
docs/checkpoints/320_hybrid_pdf_access_fresh_chat_native_split_qualified.md
docs/local_execution/validation/078_hybrid_pdf_access_fresh_chat_native_split_qualified.md
docs/checkpoints/319_hybrid_pdf_access_live_source_published_restart_pending.md
docs/local_execution/validation/077_hybrid_pdf_access_live_source_published_restart_pending.md
docs/checkpoints/318_hybrid_pdf_routing_core_qualified_public_facade_next.md
docs/local_execution/validation/076_hybrid_pdf_routing_core_qualified.md
docs/research/120_automatic_hybrid_pdf_direct_source_routing_and_managed_artifact_cache.md
docs/checkpoints/316_large_pdf_text_read_qualified.md
docs/local_execution/validation/074_large_pdf_text_read_qualified.md
docs/checkpoints/315_large_pdf_text_read_source_published_restart_pending.md
docs/local_execution/validation/073_large_pdf_text_read_source_published_restart_pending.md
docs/checkpoints/314_large_pdf_page16_direct_render_qualified.md
docs/local_execution/validation/072_large_pdf_page16_direct_render_qualified.md
docs/checkpoints/313_large_pdf_page_render_source_published_restart_pending.md
docs/local_execution/validation/071_large_pdf_page_render_source_published_restart_pending.md
docs/checkpoints/312_machine_learning_large_pdf_hybrid_fallback_required.md
docs/local_execution/validation/070_machine_learning_large_pdf_splitter_generalization.md
docs/checkpoints/311_multi_native_pdf_direct_access_qualified.md
docs/local_execution/validation/069_multi_native_pdf_direct_access_qualified.md
docs/checkpoints/310_fresh_chat_host_resource_link_not_advertised_multi_pdf_next.md
docs/local_execution/validation/068_fresh_chat_host_capability_resource_link_not_advertised.md
docs/checkpoints/309_chatgpt_host_capability_probe_live_fresh_chat_required.md
docs/local_execution/validation/067_chatgpt_host_capability_probe_live_same_chat_projection_stale.md
docs/checkpoints/308_chatgpt_local_file_access_objective_restored.md
docs/research/119_chatgpt_local_machine_file_access_objective_restoration.md
docs/checkpoints/307_astra_pdf_worker_ambiguous_nested_cwd_runtime_reconciled.md
docs/local_execution/validation/066_astra_large_pdf_semantic_worker_ambiguous_runtime_cwd_reconciled.md
docs/checkpoints/306_astra_phase2_browser_free_pdf_evidence_review_complete.md
docs/local_execution/validation/065_astra_phase2_pdf_evidence_candidate_reviewed.md
docs/research/118_astra_phase2_browser_free_pdf_evidence_architecture_reconciliation.md
docs/checkpoints/305_gpt56_browser_compatibility_baseline_blocked_direct_call_cleanup.md
docs/local_execution/validation/064_gpt56_browser_compatibility_baseline_blocked_direct_call_cleanup.md
docs/checkpoints/304_direct_codex_guard_false_positive_live_qualified.md
docs/local_execution/validation/063_direct_codex_guard_false_positive_live_qualified.md
docs/checkpoints/303_resource_link_boundary_native_auto_review_live_qualified.md
docs/local_execution/validation/062_resource_link_boundary_native_auto_review_live_qualified.md
docs/checkpoints/302_clean_6_63mib_resource_link_host_materialization_passed.md
docs/local_execution/validation/061_clean_6_63mib_resource_link_host_materialization_passed.md
docs/checkpoints/301_clean_8mib_resource_link_host_materialization_failed.md
docs/local_execution/validation/060_clean_8mib_resource_link_host_materialization_failed.md
docs/checkpoints/300_clean_large_pdf_4mib_host_pass_8mib_retest_required.md
docs/local_execution/validation/059_large_pdf_host_ladder_folder_contamination_and_clean_4mib_pass.md
docs/checkpoints/299_large_pdf_resource_link_preview14_live_smokes_passed.md
docs/local_execution/validation/058_large_pdf_resource_link_preview14_live_smokes_passed.md
docs/checkpoints/298_large_pdf_resource_link_publication_passed_restart_pending.md
docs/local_execution/validation/057_large_pdf_resource_link_publication_passed_restart_pending.md
docs/checkpoints/297_large_pdf_resource_link_scaling_publication_preflight_qualified.md
docs/local_execution/validation/056_large_pdf_resource_link_scaling_publication_preflight_qualified.md
docs/checkpoints/296_scanned_mcp_pdf_resource_link_full_pdf_access_passed.md
docs/local_execution/validation/055_scanned_mcp_pdf_resource_link_full_pdf_access_passed.md
docs/checkpoints/295_representative_mcp_pdf_resource_link_full_pdf_access_passed.md
docs/local_execution/validation/054_representative_mcp_pdf_resource_link_full_pdf_access_passed.md
docs/checkpoints/294_tiny_mcp_pdf_resource_link_host_materialization_passed.md
docs/local_execution/validation/053_tiny_mcp_pdf_resource_link_host_materialization_passed.md
docs/checkpoints/293_mcp_pdf_resource_link_publication_preflight_qualified.md
docs/local_execution/validation/052_mcp_pdf_resource_link_publication_preflight_qualified.md
docs/checkpoints/292_mcp_pdf_resource_attachment_materialized_same_turn_native_pdf_failed.md
docs/local_execution/validation/051_mcp_pdf_resource_materializes_attachment_but_not_same_turn_native_pdf.md
docs/checkpoints/291_document_file_handoff_publication_preflight_qualified.md
docs/local_execution/validation/050_document_file_handoff_publication_preflight_qualified.md
docs/checkpoints/290_official_pdf_skill_local_ads_handoff_research_prioritized.md
docs/local_execution/validation/049_official_pdf_skill_local_ads_handoff_research_prioritized.md
docs/checkpoints/289_representative_pdf_fidelity_exposes_windows_command_exec_capture_ceiling.md
docs/local_execution/validation/048_representative_pdf_fidelity_exposes_windows_command_exec_capture_ceiling.md
docs/checkpoints/288_document_render_live_chatgpt_vision_qualified.md
docs/local_execution/validation/047_document_render_live_chatgpt_vision_qualified.md
docs/checkpoints/287_document_render_live_source_published_restart_pending.md
docs/local_execution/validation/046_document_render_live_source_published_restart_pending.md
docs/checkpoints/286_sandboxed_managed_pdf_render_publication_preflight_qualified.md
docs/local_execution/validation/045_sandboxed_managed_pdf_render_publication_preflight_qualified.md
docs/checkpoints/285_managed_primary_runtime_poppler_page_rendering_probe_qualified.md
docs/local_execution/validation/044_managed_primary_runtime_poppler_page_rendering_probe_qualified.md
docs/checkpoints/284_model_free_mcp_image_bridge_live_chatgpt_vision_qualified.md
docs/local_execution/validation/043_model_free_mcp_image_bridge_live_chatgpt_vision_qualified.md
docs/checkpoints/283_model_free_mcp_image_bridge_publication_preflight_qualified.md
docs/checkpoints/282_codex_native_local_image_view_qualified.md
docs/checkpoints/281_codex_pdf_skill_reuse_experiment_rendering_dependency_blocked.md
docs/checkpoints/280_reuse_first_document_architecture_and_local_media_bridge_research.md
docs/checkpoints/279_generic_workspace_document_read_and_architecture_backlog_qualified.md
docs/checkpoints/278_flexible_multi_repository_authority_and_private_git_qualified.md
docs/checkpoints/277_semantic_git_publication_runtime_repository_and_flexible_authority_opened.md
docs/research/116_flexible_multi_repository_codexless_authority_and_runtime_repository_architecture.md
docs/research/117_reuse_first_multimodal_document_architecture_and_local_media_handoff.md
docs/local_execution/LOCAL_RUNTIME_REPOSITORY.md
docs/local_execution/validation/033_semantic_git_commit_push_surface_publication_and_public_ads_push_verified.md
docs/local_execution/validation/034_chatgpt_tool_projection_refresh_and_connector_coexistence_observations.md
docs/local_execution/validation/035_running_codex_supervision_liveness_gap_reproduced.md
docs/local_execution/validation/036_live_config_batchwrite_qualification_host_boundary.md
docs/local_execution/validation/037_flexible_authority_live_source_published_restart_pending.md
docs/local_execution/validation/038_runtime_repository_bootstrap_private_git_credentials_boundary.md
docs/local_execution/validation/039_workspace_standard_and_document_read_live_qualified.md
docs/local_execution/validation/040_codex_pdf_skill_visual_read_reuse_experiment.md
docs/local_execution/validation/041_codex_native_local_image_view_qualified.md
docs/local_execution/validation/042_model_free_mcp_image_bridge_publication_preflight_qualified.md
docs/OPEN_ARCHITECTURE_BACKLOG.md
docs/checkpoints/276_codex_codexless_upstream_ecosystem_research_opened_source_vault_paused.md
docs/research/113_codex_codexless_upstream_ecosystem_architecture_research_program.md
docs/research/114_current_codex_app_server_architecture_and_ads_implications.md
docs/research/115_public_codexless_current_architecture_pr_landscape_and_ads_delta.md
docs/research/CODEX_UPSTREAM_ADS_COMPARISON_MATRIX.md
docs/model_collaboration/threads/MC-0010/BRIEF.md
docs/model_collaboration/threads/MC-0010/THREAD.md
docs/model_collaboration/threads/MC-0010/STATE.json
docs/checkpoints/275_guided_proceed_in_chat_roundtrip_verified_source_vault_active.md
docs/research/112_guided_proceed_in_chat_shared_ready_and_repeatable_roundtrip.md
docs/local_execution/validation/032_guided_proceed_in_chat_repeatable_same_thread_verified.md
docs/checkpoints/274_archive_unarchive_reacquire_verified_source_vault_ingestion_resumed.md
docs/research/111_archive_unarchive_reacquire_closes_codex_desktop_handoff.md
docs/local_execution/validation/031_desktop_archive_unarchive_rebind_resume_verified.md
docs/checkpoints/273_durable_bidirectional_codex_thread_handoff_verified_cooperative_release_next.md
docs/research/110_durable_bidirectional_codex_thread_handoff_and_cooperative_release.md
docs/local_execution/validation/027_codex_desktop_deeplink_handoff_live_verified.md
docs/local_execution/validation/028_codex_desktop_catalog_writer_ownership_followup.md
docs/local_execution/validation/029_durable_thread_bind_restart_reacquisition_verified.md
docs/local_execution/validation/030_bound_active_writer_combined_live_test_blocked_by_platform_safety.md
docs/checkpoints/272_codex_desktop_thread_handoff_verified_deeplink_candidate_preflighted.md
docs/research/109_codex_desktop_thread_handoff_and_catalog_reconciliation.md
docs/checkpoints/271_bounded_direct_git_synchronization_verified_source_vault_resume_ready.md
docs/local_execution/OPERATIONS.md
docs/local_execution/AUTHORITY_BOOTSTRAP.md
docs/local_execution/ACL_INTEGRITY_GATE.md
docs/local_execution/DIRECT_GIT_INVESTIGATION_LESSONS.md
docs/local_execution/SEMANTIC_PULL_ACCEPTANCE.md
docs/current_routing.json
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
```

---

## Conversation-rotation boundary

The guided handoff boundary is preserved through Checkpoint 275. `chatgpt-17` then continued Research 113/117 through the document-resource and Browser-baseline work and closed at Checkpoint 305 after its own context-limit termination. `chatgpt-18` completed the independent Astra architecture challenge, corrected the workstream objective, qualified the host-capability, native split, large-source text/render and complete native-hybrid PDF routes, and closed at Checkpoint 321 when the conversation reached its length limit. The current `chatgpt-19` interaction preserved the failed fresh-chat PDF intent matrix as Checkpoint 322, qualified the renderer correction through Checkpoints 323-327, completed >192 MiB PDF isolation as Checkpoint 328, opened Research 121 at Checkpoint 329, closed AB-020 through Checkpoint 333, qualified/published/restarted the 61-tool Office file-link surface through Checkpoints 334-338, closed the fresh DOCX/PPTX/XLSX host matrix as Checkpoint 339, and now opens Research 122 at Checkpoint 340 for runtime self-maintenance, lifecycle supervision and device-independent/phone access.

The repository now preserves the guided/repeated handoff, the Checkpoint 275 interruption residue, the v16 publication/test and Desktop comparison, the comprehensive upstream-research route, the successful semantic Git publication/push, the flexible multi-repository authority architecture, the `workspace-standard` generic non-Git extension, and live first-class PDF document reading. `chatgpt-17` also reproduced a continuity/routing weakness: the correct operational restart and ChatGPT app-refresh procedure already existed in `docs/local_execution/OPERATIONS.md`, but the collaborator initially gave generic/incorrect operational guidance before reading that governing runbook. The instance and the requested follow-up architecture audit are preserved in `docs/OPEN_ARCHITECTURE_BACKLOG.md` as AB-022 and AB-023; no routing fix has yet been accepted. The frozen public Checkpoint 279 content baseline is `bd7a2fcf802d99e6b9dd2b94745f248f347a12a9`. The private runtime repository is synchronized to that public baseline at `d86a96e2a26fbc946a31e28ef1ca14c8a129628a`, where `RUNTIME_STATE.json` explicitly records public Checkpoint 279 / `bd7a2fcf...`; this avoids recursive public/private anchoring while allowing a later public routing-envelope commit to point MC-0010 at both frozen evidence boundaries. Before Claude Message 001, verify that a fresh Claude environment can actually access both repositories; if private-repository access is unavailable, preserve that limitation rather than substituting public summaries. The earlier planned Chat 17 rotation preflight referred to the then-stable 52-tool surface; the current live surface is now 54 tools after the qualified `codex.image_read` and `codex.document_render` publications.

When rotation is chosen, follow `docs/CONTINUITY.md` and evaluate the actual transition evidence:

```text
exact-head public Repository Integrity PASS
required private continuity anchor reconciled and verified when applicable
local checkout synchronized with the public authority when required
no unrecorded guided or repeated handoff state
CHAT_ROTATION_PREFLIGHT evaluated as PASS / HOLD / FAIL from actual evidence
```

A new persistent conversation must allocate a fresh provider-local session/title, reconstruct public authority first, recover the relevant private local-runtime complement when accessible, and continue from the `runtime-self-restart-qualified-publication-authority-next` boundary unless the repository has advanced further. Research 122 now governs the active runtime self-maintenance, lifecycle-supervision and device-independent-access stage; Research 120 and Research 121 remain complete beneath it. The immediate work is to implement and qualify the minimum detached one-shot lifecycle owner for Codexless-only restart, give it a durable bounded operation ledger and exact process-identity contract, then define private credential/state ownership for eventual production managed-tunnel migration. The native-mobile versus mobile-browser ChatGPT access matrix remains the next user-assisted device discriminator. Do not broaden ordinary workspace authority to `%LOCALAPPDATA%`, the full user profile or general process control merely to automate restart. Preserve the live preview.17 / 61-tool baseline, closed AB-020 integrity result and AB-008 fresh-chat projection caveat. Before any exact restart/publication mutation guidance, resolve and read `docs/local_execution/OPERATIONS.md`; AB-022 remains open. The broader `codexless-upstream-ecosystem-research` program remains active above this leaf, and the preserved Source Vault ingestion route remains paused beneath that Level-2 research phase until it is deliberately resumed.

---

## Minimum reading for continuation

```text
README.md
docs/README.md
docs/CONTINUITY.md
docs/current_routing.json
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/checkpoints/385_github_g0_immutable_dependency_generations_qualified_bootstrap_release_next.md
docs/local_execution/validation/142_github_g0_immutable_dependency_generation_release_architecture_qualified.md
docs/checkpoints/384_github_g0_runtime_integration_candidate_qualified_dependency_provisioning_next.md
docs/local_execution/validation/141_github_g0_main_runtime_integration_candidate_qualified.md
docs/checkpoints/383_github_g0_windows_keyring_qualified_runtime_integration_next.md
docs/local_execution/validation/140_github_g0_windows_keyring_host_roundtrip_qualified.md
docs/checkpoints/382_github_g0_private_candidate_qualified_keyring_runtime_next.md
docs/local_execution/validation/139_github_g0_auth_transport_private_candidate_qualified.md
docs/checkpoints/381_github_official_api_baseline_g0_contract_ready.md
docs/local_execution/validation/138_github_official_api_auth_and_first_contract_gaps_resolved.md
docs/research/GITHUB_API_AUTH_AND_CONTRACT_BASELINE.md
docs/checkpoints/380_github_schema_reconciled_g0_and_targeted_evidence_ready.md
docs/local_execution/validation/137_github_89_schema_final_reconciliation_contract_gaps_localized.md
docs/research/GITHUB_CONNECTOR_PREIMPLEMENTATION_EVIDENCE_GAPS.md
docs/checkpoints/379_github_native_schema_capture_complete_final_reconciliation_pending.md
docs/local_execution/validation/136_github_native_schema_capture_batch6_preserved.md
docs/checkpoints/378_github_native_schema_capture_batch5_preserved.md
docs/local_execution/validation/135_github_native_schema_capture_batch5_preserved.md
docs/checkpoints/377_github_native_schema_capture_batch4_preserved.md
docs/local_execution/validation/134_github_native_schema_capture_batch4_preserved.md
docs/checkpoints/376_github_native_schema_capture_batch3_preserved.md
docs/local_execution/validation/133_github_native_schema_capture_batch3_preserved.md
docs/checkpoints/375_github_native_schema_capture_batch2_preserved.md
docs/local_execution/validation/132_github_native_schema_capture_batch2_preserved.md
docs/checkpoints/374_github_native_schema_capture_batch1_preserved.md
docs/local_execution/validation/131_github_native_schema_capture_batch1_preserved.md
docs/research/123_github_connector_capability_parity_and_codexless_runtime_bridge_architecture.md
docs/research/GITHUB_CONNECTOR_PARITY_MATRIX.md
docs/research/GITHUB_CONNECTOR_SCHEMA_CAPTURE.md
docs/research/github_connector_89_action_inventory.json
docs/research/github_connector_native_schema_capture.json
docs/checkpoints/342_detached_runtime_helper_survival_qualified.md
docs/local_execution/validation/100_detached_runtime_helper_survival_qualified.md
docs/checkpoints/341_managed_tunnel_backend_recovery_qualified.md
docs/local_execution/validation/099_managed_tunnel_backend_recovery_qualified.md
docs/checkpoints/340_runtime_lifecycle_and_device_access_research_opened.md
docs/local_execution/validation/098_runtime_lifecycle_and_device_access_research_baseline.md
docs/research/122_runtime_self_maintenance_lifecycle_and_device_independent_access.md
docs/local_execution/OPERATIONS.md
docs/checkpoints/339_office_file_link_fresh_chat_matrix_qualified_research121_complete.md
docs/local_execution/validation/097_office_file_link_fresh_chat_matrix_qualified.md
docs/checkpoints/329_non_pdf_office_handoff_reuse_first_research_opened.md
docs/local_execution/validation/087_non_pdf_office_handoff_reuse_first_research_baseline.md
docs/research/121_non_pdf_file_capability_matrix_and_native_handoff_reuse.md
docs/checkpoints/328_hybrid_pdf_over_192mib_public_facade_isolation_qualified.md
docs/local_execution/validation/086_hybrid_pdf_over_192mib_public_facade_isolation_qualified.md
docs/checkpoints/327_hybrid_pdf_access_fresh_chat_intent_matrix_qualified.md
docs/local_execution/validation/085_hybrid_pdf_access_fresh_chat_intent_matrix_qualified.md
docs/checkpoints/326_hybrid_pdf_render_serialization_live_activation_qualified.md
docs/local_execution/validation/084_hybrid_pdf_render_serialization_live_activation_qualified.md
docs/checkpoints/325_hybrid_pdf_render_serialization_live_source_published_restart_pending.md
docs/local_execution/validation/083_hybrid_pdf_render_serialization_live_source_published_restart_pending.md
docs/checkpoints/324_hybrid_pdf_render_serialization_publication_preflight_qualified.md
docs/local_execution/validation/082_hybrid_pdf_render_serialization_publication_preflight_qualified.md
docs/checkpoints/323_hybrid_pdf_direct_render_serialization_candidate_qualified.md
docs/local_execution/validation/081_hybrid_pdf_direct_render_serialization_candidate_qualified.md
docs/checkpoints/322_hybrid_pdf_intent_matrix_render_transport_gap_localized.md
docs/local_execution/validation/080_hybrid_pdf_access_fresh_chat_intent_matrix_renderer_transport_failed.md
docs/checkpoints/321_hybrid_pdf_access_fresh_chat_native_hybrid_qualified.md
docs/local_execution/validation/079_hybrid_pdf_access_fresh_chat_native_hybrid_qualified.md
docs/checkpoints/320_hybrid_pdf_access_fresh_chat_native_split_qualified.md
docs/local_execution/validation/078_hybrid_pdf_access_fresh_chat_native_split_qualified.md
docs/checkpoints/319_hybrid_pdf_access_live_source_published_restart_pending.md
docs/local_execution/validation/077_hybrid_pdf_access_live_source_published_restart_pending.md
docs/checkpoints/318_hybrid_pdf_routing_core_qualified_public_facade_next.md
docs/local_execution/validation/076_hybrid_pdf_routing_core_qualified.md
docs/research/120_automatic_hybrid_pdf_direct_source_routing_and_managed_artifact_cache.md
docs/checkpoints/316_large_pdf_text_read_qualified.md
docs/local_execution/validation/074_large_pdf_text_read_qualified.md
docs/checkpoints/315_large_pdf_text_read_source_published_restart_pending.md
docs/local_execution/validation/073_large_pdf_text_read_source_published_restart_pending.md
docs/checkpoints/314_large_pdf_page16_direct_render_qualified.md
docs/local_execution/validation/072_large_pdf_page16_direct_render_qualified.md
docs/checkpoints/313_large_pdf_page_render_source_published_restart_pending.md
docs/local_execution/validation/071_large_pdf_page_render_source_published_restart_pending.md
docs/checkpoints/312_machine_learning_large_pdf_hybrid_fallback_required.md
docs/local_execution/validation/070_machine_learning_large_pdf_splitter_generalization.md
docs/checkpoints/311_multi_native_pdf_direct_access_qualified.md
docs/local_execution/validation/069_multi_native_pdf_direct_access_qualified.md
docs/checkpoints/310_fresh_chat_host_resource_link_not_advertised_multi_pdf_next.md
docs/local_execution/validation/068_fresh_chat_host_capability_resource_link_not_advertised.md
docs/checkpoints/309_chatgpt_host_capability_probe_live_fresh_chat_required.md
docs/local_execution/validation/067_chatgpt_host_capability_probe_live_same_chat_projection_stale.md
docs/checkpoints/308_chatgpt_local_file_access_objective_restored.md
docs/research/119_chatgpt_local_machine_file_access_objective_restoration.md
docs/checkpoints/307_astra_pdf_worker_ambiguous_nested_cwd_runtime_reconciled.md
docs/local_execution/validation/066_astra_large_pdf_semantic_worker_ambiguous_runtime_cwd_reconciled.md
docs/checkpoints/306_astra_phase2_browser_free_pdf_evidence_review_complete.md
docs/local_execution/validation/065_astra_phase2_pdf_evidence_candidate_reviewed.md
docs/research/118_astra_phase2_browser_free_pdf_evidence_architecture_reconciliation.md
docs/checkpoints/305_gpt56_browser_compatibility_baseline_blocked_direct_call_cleanup.md
docs/local_execution/validation/064_gpt56_browser_compatibility_baseline_blocked_direct_call_cleanup.md
docs/checkpoints/304_direct_codex_guard_false_positive_live_qualified.md
docs/local_execution/validation/063_direct_codex_guard_false_positive_live_qualified.md
docs/checkpoints/302_clean_6_63mib_resource_link_host_materialization_passed.md
docs/local_execution/validation/061_clean_6_63mib_resource_link_host_materialization_passed.md
docs/checkpoints/301_clean_8mib_resource_link_host_materialization_failed.md
docs/local_execution/validation/060_clean_8mib_resource_link_host_materialization_failed.md
docs/checkpoints/300_clean_large_pdf_4mib_host_pass_8mib_retest_required.md
docs/local_execution/validation/059_large_pdf_host_ladder_folder_contamination_and_clean_4mib_pass.md
docs/checkpoints/299_large_pdf_resource_link_preview14_live_smokes_passed.md
docs/local_execution/validation/058_large_pdf_resource_link_preview14_live_smokes_passed.md
docs/checkpoints/298_large_pdf_resource_link_publication_passed_restart_pending.md
docs/local_execution/validation/057_large_pdf_resource_link_publication_passed_restart_pending.md
docs/checkpoints/297_large_pdf_resource_link_scaling_publication_preflight_qualified.md
docs/local_execution/validation/056_large_pdf_resource_link_scaling_publication_preflight_qualified.md
docs/checkpoints/296_scanned_mcp_pdf_resource_link_full_pdf_access_passed.md
docs/local_execution/validation/055_scanned_mcp_pdf_resource_link_full_pdf_access_passed.md
docs/checkpoints/295_representative_mcp_pdf_resource_link_full_pdf_access_passed.md
docs/local_execution/validation/054_representative_mcp_pdf_resource_link_full_pdf_access_passed.md
docs/checkpoints/294_tiny_mcp_pdf_resource_link_host_materialization_passed.md
docs/local_execution/validation/053_tiny_mcp_pdf_resource_link_host_materialization_passed.md
docs/checkpoints/293_mcp_pdf_resource_link_publication_preflight_qualified.md
docs/local_execution/validation/052_mcp_pdf_resource_link_publication_preflight_qualified.md
docs/checkpoints/292_mcp_pdf_resource_attachment_materialized_same_turn_native_pdf_failed.md
docs/local_execution/validation/051_mcp_pdf_resource_materializes_attachment_but_not_same_turn_native_pdf.md
docs/checkpoints/291_document_file_handoff_publication_preflight_qualified.md
docs/local_execution/validation/050_document_file_handoff_publication_preflight_qualified.md
docs/checkpoints/290_official_pdf_skill_local_ads_handoff_research_prioritized.md
docs/local_execution/validation/049_official_pdf_skill_local_ads_handoff_research_prioritized.md
docs/checkpoints/289_representative_pdf_fidelity_exposes_windows_command_exec_capture_ceiling.md
docs/local_execution/validation/048_representative_pdf_fidelity_exposes_windows_command_exec_capture_ceiling.md
docs/checkpoints/288_document_render_live_chatgpt_vision_qualified.md
docs/local_execution/validation/047_document_render_live_chatgpt_vision_qualified.md
docs/checkpoints/287_document_render_live_source_published_restart_pending.md
docs/local_execution/validation/046_document_render_live_source_published_restart_pending.md
docs/checkpoints/286_sandboxed_managed_pdf_render_publication_preflight_qualified.md
docs/local_execution/validation/045_sandboxed_managed_pdf_render_publication_preflight_qualified.md
docs/checkpoints/285_managed_primary_runtime_poppler_page_rendering_probe_qualified.md
docs/local_execution/validation/044_managed_primary_runtime_poppler_page_rendering_probe_qualified.md
docs/checkpoints/284_model_free_mcp_image_bridge_live_chatgpt_vision_qualified.md
docs/local_execution/validation/043_model_free_mcp_image_bridge_live_chatgpt_vision_qualified.md
docs/checkpoints/283_model_free_mcp_image_bridge_publication_preflight_qualified.md
docs/checkpoints/282_codex_native_local_image_view_qualified.md
docs/checkpoints/281_codex_pdf_skill_reuse_experiment_rendering_dependency_blocked.md
docs/checkpoints/280_reuse_first_document_architecture_and_local_media_bridge_research.md
docs/checkpoints/279_generic_workspace_document_read_and_architecture_backlog_qualified.md
docs/checkpoints/278_flexible_multi_repository_authority_and_private_git_qualified.md
docs/checkpoints/277_semantic_git_publication_runtime_repository_and_flexible_authority_opened.md
docs/research/116_flexible_multi_repository_codexless_authority_and_runtime_repository_architecture.md
docs/research/117_reuse_first_multimodal_document_architecture_and_local_media_handoff.md
docs/local_execution/LOCAL_RUNTIME_REPOSITORY.md
docs/local_execution/validation/033_semantic_git_commit_push_surface_publication_and_public_ads_push_verified.md
docs/local_execution/validation/034_chatgpt_tool_projection_refresh_and_connector_coexistence_observations.md
docs/local_execution/validation/035_running_codex_supervision_liveness_gap_reproduced.md
docs/local_execution/validation/036_live_config_batchwrite_qualification_host_boundary.md
docs/local_execution/validation/037_flexible_authority_live_source_published_restart_pending.md
docs/local_execution/validation/038_runtime_repository_bootstrap_private_git_credentials_boundary.md
docs/local_execution/validation/039_workspace_standard_and_document_read_live_qualified.md
docs/local_execution/validation/040_codex_pdf_skill_visual_read_reuse_experiment.md
docs/local_execution/validation/041_codex_native_local_image_view_qualified.md
docs/local_execution/validation/042_model_free_mcp_image_bridge_publication_preflight_qualified.md
docs/OPEN_ARCHITECTURE_BACKLOG.md
docs/checkpoints/276_codex_codexless_upstream_ecosystem_research_opened_source_vault_paused.md
docs/research/113_codex_codexless_upstream_ecosystem_architecture_research_program.md
docs/research/114_current_codex_app_server_architecture_and_ads_implications.md
docs/research/115_public_codexless_current_architecture_pr_landscape_and_ads_delta.md
docs/research/CODEX_UPSTREAM_ADS_COMPARISON_MATRIX.md
docs/model_collaboration/threads/MC-0010/BRIEF.md
docs/model_collaboration/threads/MC-0010/THREAD.md
docs/model_collaboration/threads/MC-0010/STATE.json
docs/checkpoints/275_guided_proceed_in_chat_roundtrip_verified_source_vault_active.md
docs/research/112_guided_proceed_in_chat_shared_ready_and_repeatable_roundtrip.md
docs/local_execution/validation/032_guided_proceed_in_chat_repeatable_same_thread_verified.md
docs/checkpoints/274_archive_unarchive_reacquire_verified_source_vault_ingestion_resumed.md
docs/research/111_archive_unarchive_reacquire_closes_codex_desktop_handoff.md
docs/local_execution/validation/031_desktop_archive_unarchive_rebind_resume_verified.md
docs/checkpoints/273_durable_bidirectional_codex_thread_handoff_verified_cooperative_release_next.md
docs/research/110_durable_bidirectional_codex_thread_handoff_and_cooperative_release.md
docs/checkpoints/272_codex_desktop_thread_handoff_verified_deeplink_candidate_preflighted.md
docs/research/109_codex_desktop_thread_handoff_and_catalog_reconciliation.md
docs/checkpoints/271_bounded_direct_git_synchronization_verified_source_vault_resume_ready.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/local_execution/OPERATIONS.md
docs/local_execution/AUTHORITY_BOOTSTRAP.md
docs/local_execution/ACL_INTEGRITY_GATE.md
docs/local_execution/DIRECT_GIT_INVESTIGATION_LESSONS.md
docs/local_execution/SEMANTIC_PULL_ACCEPTANCE.md
docs/DEVELOPMENT_METHOD.md
```
