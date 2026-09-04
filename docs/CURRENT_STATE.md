# Current State

**Checkpoint:** 292
**Date:** 2026-09-04
**Active development branch:** `v1-source-vault-bootstrap-resume`
**Active PR:** none
**Promoted V1 integration branch:** `v1-frontend-spike` at `2480109fadeee1e480ef03b82e335aacdf9adf91`
**Latest specification:** Specification 027
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no GENERIC / ADS_HORIZON / ORACLE_HORIZON comparison may be inferred.

## Active interaction context

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-17
Conversation title       17 - MCP Image Bridge Publication Recovery and Multimodal Document Continuation
Primary collaborator     ChatGPT
```

Repository artifacts remain authoritative across chats and models.

---

## Current active stage: reuse-first multimodal document architecture research inside the broader upstream research phase

Checkpoint 292 records the live host discrimination after preview.12 publication and ChatGPT app refresh. `codex.document_file_read` succeeds and the ChatGPT host visibly materializes a returned `application/pdf` MCP resource as a PDF attachment/file card, but the same assistant turn does not automatically receive parsed PDF content, rendered pages, or native visual PDF input. The tiny two-page `probe.pdf` therefore classified `MCP_PDF_RESOURCE_TO_CHATGPT_NATIVE_PDF=FAIL` for same-turn promotion while still proving host attachment materialization. A representative 1.68 MiB PDF repeatedly triggered the misleading `maximum chat length is reached` UI error in otherwise fresh/usable chats; its inline base64 payload is about 2.24 million characters, so representative inline embedded-resource transport is not viable as tested. The active machine-readable boundary is now `mcp-pdf-attachment-materialized-same-turn-native-pdf-failed`.

The reuse-first branch is not closed yet because the host-created PDF attachment may be consumable by the first-party PDF Skill in the next turn of the same conversation. That zero-code-change experiment now takes priority over resuming the paused Checkpoint 289 loopback transport. If next-turn `@PDF` can inspect the already-materialized `probe.pdf`, the remaining problem is how to materialize representative PDFs without multi-megabyte inline base64, with MCP `resource_link`/resource-read semantics the next candidate. If `@PDF` cannot consume the materialized attachment, the file card is only host/UI materialization and does not solve Research 117.

Checkpoint 279 remains fully accepted beneath this research boundary: `workspace-standard` supports explicit ordinary non-Git exact-root admission and Codexless `0.1.1-preview.9` / `codexless-public-preview-v2` exposes 52 MCP tools including first-class `codex.document_read`. At that qualification boundary `big-data-statistics` had only `read`; Research 117 later added `agent` explicitly for the bounded reuse experiment while retaining no write/browser/Git capability. A fresh disposable ChatGPT conversation had already invoked `codex.document_read` against a real PDF and returned bounded embedded text plus source/parser/page provenance with no OCR and no file mutation. Validation 039 remains the decisive baseline qualification evidence.

The PDF parser is hardened out of the main Codexless event loop into a dedicated bounded Node child process with a 256 MiB V8 old-space ceiling, 30-second default hard deadline, bounded protocol output, Node permission restrictions, disabled PDF JavaScript evaluation/system-font lookup/worker fetch, and deterministic termination/recovery on timeout. The main process performs a bounded file-handle read capped at 32 MiB plus one byte and revalidates identity/size after reading. Focused qualification is `DOCUMENT_READ_REGRESSION=PASS tests=11`, while flexible authority, bounded Git, dependency, and 52-tool public-surface regressions also pass.

The workspace registry is now revision `4`, content hash `2960f0b113550301a692470b0f2ff527317812550b6d3ae7cd2e519c94ad9e80`, with `ads-public`, `ads-local-runtime`, and `big-data-statistics`. The last workspace now has only `read` and `agent` for Research 117 qualification and still has no write, browser, or Git capability. The exact personal root remains machine-local rather than public project authority.

`docs/OPEN_ARCHITECTURE_BACKLOG.md` is now the durable index for explicit future architecture ideas and deferred side tracks. It preserves, among other items, mobile/device-independent connector access, narrow `%LOCALAPPDATA%` runtime-maintenance authority, autonomous Codex supervision/wakeup, active-turn writer transfer, Rich Card actionability, shared spectator synchronization, v17 semantic viewer work, broader host-capability taxonomy, the reproduced reconstruction-to-operational-authority routing gap, a backlog/open-question discoverability audit, high-recall new-session reconstruction, an explicit nested-workstream/resume graph, Knowledge Map topic-saturation risk, and an audit of scattered known weaknesses/deferred architecture triggers so anticipated limitations can be surfaced before they are rediscovered through failure. It is an index, not a replacement for `CURRENT_STATE.md`, `OPEN_QUESTIONS.md`, research, validation evidence, or accepted specifications.

Checkpoint 278 remains the accepted Research 116 core boundary: live flexible multi-repository authority, explicit two-layer admission of the private `autonomous-data-science-system-local-runtime` workspace, reviewed non-secret runtime-repository bootstrap, the private authenticated Git transport correction, and end-to-end generalized fetch/push qualification against `ads-local-runtime`.

The stable architecture now supports explicit register/update/remove of ordinary filesystem/project roots without another MCP schema publication. Per-workspace capability checks remain server-owned; semantic Git selects only `workspaceId`, derives branch/upstream dynamically, preserves the registered remote and integrity policy, and exposes no caller-selected cwd/URL/refspec/credentials/config/profile/sandbox/force inputs. Authenticated private Git is now proven through the bounded host-network substrate with `RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS`, `retried=false`, exact local/remote equality, clean tracked postflight, and `postflightOk=true` at private runtime commit `0ce61ba794929ee71c555d480a936fdced28ef2e`.

The current synchronized public boundary is commit `de56c4976bd298e3094f48f65e931e667cddf9f8`, where local `HEAD` and `origin/v1-source-vault-bootstrap-resume` were equal after `codex.git_push_ff_only` completed with `PUBLIC_REPOSITORY_INTEGRITY=PASS`, `retried=false`, clean tracked postflight, and `postflightOk=true`. This exact public HEAD includes Checkpoint 291 and Validation 050. The known protected `.tmp/pytest-*` warning remains interruption residue and was not modified.

The live Codexless server now exposes 54 public MCP tools on `0.1.1-preview.11`. The refreshed surface preserves `codex.document_read` and `codex.image_read` and adds live-qualified `codex.document_render`. Fresh disposable ChatGPT testing proves both the earlier direct image bridge (`MCP_IMAGE_TO_CHATGPT_VISION=PASS`) and the new direct PDF-page render bridge (`MCP_DOCUMENT_RENDER_TO_CHATGPT_VISION=PASS`). Tunnel health and readiness are both verified at HTTP 200. The earlier 51-tool/47-recipient projection mismatch remains historical host evidence in Validation 034 rather than current live state. Ordinary future workspace registrations continue to change server-owned policy without another MCP schema publication.

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

The final guided handoff used exact persisted thread `01a063b1-0d21-7011-b17c-514eb0359a15`. After source marker `PROCEED_IN_CHAT_UI_SOURCE_COMPLETE`, the user opened the exact thread in Desktop, selected `Proceed in Chat`, archived it while Desktop remained running, and selected `I've archived it — Continue`. The card reached `Ready in Chat` through model-free verification, unarchive, and rebound without starting a model turn.

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
automatic ACL repair
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

ACL repair is never automatic merely to make a Git operation pass.

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

Canonical numbered Checkpoint 291 is now the current meaningful project boundary. It preserves publication-preflight qualification of the bounded `codex.document_file_read` candidate targeting preview.12 / 55 tools while live Codexless remains preview.11 / 54. Checkpoint 290 remains the reuse-first reprioritization toward authorized local PDF -> standard MCP PDF resource -> native ChatGPT file-input/first-party PDF Skill handoff, Checkpoint 289 remains the representative Windows buffered `command/exec` transport-ceiling boundary, Checkpoint 288 remains `MCP_DOCUMENT_RENDER_TO_CHATGPT_VISION=PASS` for its tested smaller pages, Checkpoint 287 remains the host-publication/restart-pending boundary, Checkpoint 286 remains publication-preflight qualification of the sandboxed maintained PDF.js + canvas candidate, Checkpoint 285 remains independent managed-Poppler reuse evidence, Checkpoint 284 remains the live-qualified model-free MCP image bridge with `MCP_IMAGE_TO_CHATGPT_VISION=PASS`, Checkpoint 283 remains its publication-preflight boundary, Checkpoint 282 remains native Codex local-image vision, Checkpoint 281 remains the earlier PDF-Skill renderer-discovery failure, Checkpoint 280 remains the reuse-first stop rule, and Checkpoint 279 remains the accepted `workspace-standard` + `codex.document_read` baseline.

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

The guided handoff boundary is preserved through Checkpoint 275. The previous `chatgpt-16` interaction then published and tested v16, compared it against native Codex Desktop presentation, and opened Checkpoint 276 / Research 113 for comprehensive upstream ecosystem research. The current `chatgpt-17` interaction is the recovery/continuation session after the unexpected Chat 16 context-limit termination.

The repository now preserves the guided/repeated handoff, the Checkpoint 275 interruption residue, the v16 publication/test and Desktop comparison, the comprehensive upstream-research route, the successful semantic Git publication/push, the flexible multi-repository authority architecture, the `workspace-standard` generic non-Git extension, and live first-class PDF document reading. `chatgpt-17` also reproduced a continuity/routing weakness: the correct operational restart and ChatGPT app-refresh procedure already existed in `docs/local_execution/OPERATIONS.md`, but the collaborator initially gave generic/incorrect operational guidance before reading that governing runbook. The instance and the requested follow-up architecture audit are preserved in `docs/OPEN_ARCHITECTURE_BACKLOG.md` as AB-022 and AB-023; no routing fix has yet been accepted. The frozen public Checkpoint 279 content baseline is `bd7a2fcf802d99e6b9dd2b94745f248f347a12a9`. The private runtime repository is synchronized to that public baseline at `d86a96e2a26fbc946a31e28ef1ca14c8a129628a`, where `RUNTIME_STATE.json` explicitly records public Checkpoint 279 / `bd7a2fcf...`; this avoids recursive public/private anchoring while allowing a later public routing-envelope commit to point MC-0010 at both frozen evidence boundaries. Before Claude Message 001, verify that a fresh Claude environment can actually access both repositories; if private-repository access is unavailable, preserve that limitation rather than substituting public summaries. The earlier planned Chat 17 rotation preflight referred to the then-stable 52-tool surface; the current live surface is now 54 tools after the qualified `codex.image_read` and `codex.document_render` publications.

When rotation is chosen, follow `docs/CONTINUITY.md` and evaluate the actual transition evidence:

```text
exact-head public Repository Integrity PASS
required private continuity anchor reconciled and verified when applicable
local checkout synchronized with the public authority when required
no unrecorded guided or repeated handoff state
CHAT_ROTATION_PREFLIGHT evaluated as PASS / HOLD / FAIL from actual evidence
```

A new persistent conversation must allocate a fresh provider-local session/title, reconstruct public authority first, recover any relevant private complement, and continue from the `document-file-handoff-publication-preflight-qualified` boundary unless the repository has advanced further. For operational continuation steps, the collaborator must also resolve and read the governing procedure referenced by the active boundary before giving exact execution instructions; AB-022 preserves the currently observed gap while a stronger mechanism remains unaccepted. The broader `codexless-upstream-ecosystem-research` program remains active above that sub-boundary, and the preserved Source Vault ingestion route remains paused beneath the Level-2 research phase.

---

## Minimum reading for continuation

```text
README.md
docs/README.md
docs/CONTINUITY.md
docs/current_routing.json
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
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
