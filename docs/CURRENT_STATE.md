# Current State

**Checkpoint:** 339
**Date:** 2026-09-07
**Active development branch:** `v1-source-vault-bootstrap-resume`
**Active PR:** none
**Promoted V1 integration branch:** `v1-frontend-spike` at `2480109fadeee1e480ef03b82e335aacdf9adf91`
**Latest specification:** Specification 027
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no GENERIC / ADS_HORIZON / ORACLE_HORIZON comparison may be inferred.

## Active interaction context

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-19
Conversation title       19 - Hybrid PDF Intent Matrix and Isolation Qualification
Primary collaborator     ChatGPT
```

Repository artifacts remain authoritative across chats and models.

---

## Current active stage: direct ChatGPT local-machine file access through Codexless

Checkpoint 339 is the current boundary. Research 120 is complete for the accepted automatic PDF direct-source architecture and Research 121 is now complete for the accepted DOCX/PPTX/XLSX whole-file route. The refreshed fresh-chat matrix exposed `codex.file_link` and all three deterministic Office sources materialized into the ChatGPT file layer with exact byte size and SHA-256. Native inspection established DOCX text/table/image structure, PPTX two-slide ordering/picture placement/embedded-image access, and XLSX sheets/values/formulas/style metadata. No Office-specific parser or renderer fallback is required for the accepted direct-source objective. Pixel-identical Microsoft Office rendering is explicitly not claimed and becomes separate trigger-based work only if a future task requires final rendered fidelity. Codexless remains live as `0.1.1-preview.17-office-file-link` with 61 tools and tunnel HTTP 200/200. The direct PDF + Office local-file-access phase is therefore closed for its accepted scope, and the next project stage is intentionally awaiting the project owner rather than being inferred from stale continuation text.

The manual-upload baseline remains decisive. The user can already attach supported files, including large PDFs, directly to ChatGPT. Therefore the active work is about automatic direct source access from authorized local roots, not about having another model interpret local files for ChatGPT.

Existing direct-access results remain accepted: bounded local text through `codex.read_many`, local PNG/JPEG/WebP through `codex.image_read`, deterministic PDF text through `codex.document_read`, rendered PDF pages through `codex.document_render`, and whole-PDF host materialization through `codex.document_file_link` within the clean observed 7,417,428-byte PASS to 7,993,210-byte FAIL interval.

Checkpoint 309 added one narrowly scoped direct-host experiment before PDF splitting. The fresh disposable qualification exposed the new probe tools, mounted the MCP App, and visibly completed `ui/initialize`. The host snapshot reported `updateModelContext: {}` with no `resourceLink` property. Under the MCP Apps capability schema, `resourceLink?: {}` is the explicit modality advertisement, so the current bounded result is `UPDATE_MODEL_CONTEXT=ADVERTISED` and `UPDATE_MODEL_CONTEXT_RESOURCE_LINK=NOT_ADVERTISED`. The planned tiny-PDF `resourceLink -> ui/update-model-context` test is therefore skipped for this host. Validation 068 is the detailed evidence.

The user refreshed `ADS Codexless Local Bridge` in this existing persistent conversation after the controlled restart. ChatGPT-side tool rediscovery nevertheless retained the older callable projection and did not expose the three newly added probe tools. A separate fresh disposable conversation then exposed the new probe tools successfully. The combined result now localizes the behavior: the live 59-tool publication was valid, same-chat refresh retained a stale callable projection, and a fresh chat acquired the new projection.

The temporary exact-root `codexless-live` ordinary workspace admission used most recently for the Checkpoint 317 192 MiB source publication was removed after verification. The durable registry is now revision 14 / content hash `7fb25c275497228e537a5bca518d75eb8d1ef61ab111676d9ff696c40a276129` with only `ads-public`, `ads-local-runtime`, `big-data-statistics`, and `machine-learning`.

The private local-runtime repository is synchronized exactly to `origin/main` at `386813d1a31afd6748ad829c2f1dab3ea1bb89f4` with `RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS` and `postflightOk=true`. It durably preserves the complete Office file-link candidate, the live AB-020 bounded private-integrity correction, the qualified Research 120 hybrid PDF implementation, and earlier Astra/Browser/runtime evidence. AB-020 is closed for the reproduced tracked-path scaling defect: a restarted live private semantic push passed at 32,813 tracked-path bytes and the later complete Office-candidate push passed at 40,013 bytes without widening the generic command-output envelope. The later Windows regression-cleanup hardening is also preserved at the current private head.

The deterministic multi-native-PDF `document_file_link` qualification remains a real fallback, and both first-class large-source fallback channels remain fully qualified. Research 120 now defines and implements their automatic route selection and derived-artifact lifecycle. The complete private hybrid-PDF suite passes 51/51 tests, including cache restart reuse, deterministic regeneration after eviction, atomic failed-generation cleanup, source-drift invalidation, native split render equivalence, cached embedded text, cached page vision, cached PDF resources, >192 MiB page-isolation text/render, MCP facade projection, native-result bounding, managed-cache pruning, and the two new direct-render serialization/fail-closed cases. Real read-only planning on `51.Deep Learning2.annotated.pdf` still produces bounded native parts with oversized pages 16 and 49 routed to text/render fallback. The public 192 MiB `document_read` and `document_render` envelope and the preview.16 `codex.pdf_access` facade are already live-qualified for the earlier routes. The renderer-serialization correction is installed, restarted and live-qualified. The formerly failing low-level two-page render, the fresh-host five-call intent matrix, and the >192 MiB public isolation routes all pass. Research 120 therefore has no remaining PDF route-class qualification in its accepted scope.

Two earlier cross-cutting Codexless corrections remain live-qualified. Formal Codex turns preserve the initial `Call Codex?` consent and bounded permission profile while using App Server `approvalPolicy=on-request` with `approvalsReviewer=auto_review`; the PowerShell wrapper classifier also allows documentation/search/here-string data containing `Codex` while genuine wrapped Codex CLI execution remains blocked.
Checkpoint 279 remains fully accepted beneath this research boundary: `workspace-standard` supports explicit ordinary non-Git exact-root admission and Codexless `0.1.1-preview.9` / `codexless-public-preview-v2` exposes 52 MCP tools including first-class `codex.document_read`. At that qualification boundary `big-data-statistics` had only `read`; Research 117 later added `agent` explicitly for the bounded reuse experiment while retaining no write/browser/Git capability. A fresh disposable ChatGPT conversation had already invoked `codex.document_read` against a real PDF and returned bounded embedded text plus source/parser/page provenance with no OCR and no file mutation. Validation 039 remains the decisive baseline qualification evidence.

The PDF parser is hardened out of the main Codexless event loop into a dedicated bounded Node child process with a 384 MiB V8 old-space ceiling, 30-second default hard deadline, bounded protocol output, Node permission restrictions, disabled PDF JavaScript evaluation/system-font lookup/worker fetch, and deterministic termination/recovery on timeout. The installed source admits a bounded 192 MiB PDF snapshot and revalidates identity/size after reading; the parser child uses an exact declared-size input buffer and zero-copy `Uint8Array` view to avoid unnecessary whole-source duplication. The 192 MiB source change is now live-qualified after restart. The private cached-artifact text adapter reuses the same pinned `pdfjs-dist@5.4.624` contract through a server-resolved owned dependency root rather than an ad-hoc junction or copied dependency tree.

The workspace registry is now revision `14`, content hash `7fb25c275497228e537a5bca518d75eb8d1ef61ab111676d9ff696c40a276129`, with `ads-public`, `ads-local-runtime`, `big-data-statistics`, and `machine-learning`. Temporary exact-root `codexless-live` read/write admissions have been used only for bounded one-time live publication work, most recently the Checkpoint 317 192 MiB source publication, and removed immediately after publication/test verification. `big-data-statistics` has only `read` and `agent`; `machine-learning` remains strictly `read` only. Neither personal workspace has write, browser, or Git capability. Exact personal roots remain machine-local rather than public project authority.

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

The final guided handoff used exact persisted thread `01a063b1-0d21-7011-b17c-514eb0359a15`. After source marker `PROCEED_IN_CHAT_UI_SOURCE_COMPLETE`, the user opened the exact thread in Desktop, selected `Proceed in Chat`, archived it while Desktop remained running, and selected `I've archived it Ã¢â‚¬â€ Continue`. The card reached `Ready in Chat` through model-free verification, unarchive, and rebound without starting a model turn.

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

Canonical numbered Checkpoint 339 is now the current meaningful project boundary. Checkpoint 339 preserves the successful fresh-chat DOCX/PPTX/XLSX `codex.file_link` matrix, exact host materialization/source identity, native structure/embedded-asset fidelity evidence, fallback disposition, Research 121 closure and qualification-scratch cleanup. Validation 097 is the exact evidence. Checkpoint 338 remains the preview.17 live/fresh-chat-discovery boundary. Checkpoint 338 preserves live preview.17 / 61-tool activation, tunnel 200/200, exact new-source hash verification, and the persistent-chat stale `codex.file_link` projection. Validation 096 is the exact evidence. Checkpoint 337 remains the live-source-published/restart-pending boundary. Checkpoint 337 preserves successful preview.17 host publication, independent exact installed-hash verification for all nine publication targets plus semantic-Git preservation, and the explicit pre-restart process boundary. Validation 095 is the exact evidence. Checkpoint 336 remains the atomic replacement harness requalification boundary. Checkpoint 336 preserves the second preview.17 host publication failure, exact rollback verification, the corrected Windows atomic forward/rollback replacement primitives, new publication-primitive smoke coverage, and two successful complete requalification preflights. Validation 094 is the exact evidence. Checkpoint 335 remains the Windows temporary-cleanup harness requalification boundary. Checkpoint 335 preserves the safely contained first preview.17 host publication attempt, zero-live-mutation proof, Windows cleanup harness hardening, private preservation at `386813d1a31afd6748ad829c2f1dab3ea1bb89f4`, and two successful publication requalification preflights. Validation 093 is the exact evidence. Checkpoint 334 remains the original preview.17 guarded publication-preflight qualification. Checkpoint 334 preserves the exact guarded preview.17 Office file-link publication preflight. Validation 092 contains the nine-file package, hash bindings and regression evidence. Checkpoint 333 closes the concrete AB-020 scaling defect and preserves the Office candidate durably at private head `fa5cc2a6c3e6d47f45961ab475c2ac66c24aff0b`. Checkpoint 332 remains the AB-020 source-published/restart-pending boundary. Checkpoint 332 preserves successful AB-020 host publication, independent installed-hash verification, healthy pre-restart preview.16/tunnel state, and the explicit restart-pending boundary. Validation 090 is the exact evidence. Checkpoint 331 preserves the qualified Office file-link scratch candidate and deterministic host fixtures. Checkpoint 330 remains the bounded private-integrity candidate/publication-preflight boundary. Checkpoint 330 preserves the bounded AB-020 private-integrity enumeration candidate, its 8/8 regression suite, private preservation at `7e70bd05e4da76ff1ad260b2b1cbdc5c1d65a3fb`, source-control temporary-artifact cleanup, and guarded live-publication preflight. Validation 088 is the exact evidence. Checkpoint 329 remains the Research 121 reuse-first Office handoff baseline. Checkpoint 329 opens Research 121's reuse-first non-PDF Office handoff work after the PDF route family closed: current OpenAI product evidence supports DOCX/PPTX/XLSX uploads, MCP resource links are MIME-generic, and local implementation inspection identifies the existing PDF whole-file resource lifecycle as the preferred transport substrate for a narrow allowlisted `codex.file_link` candidate. Validation 087 preserves the evidence baseline and Research 121 governs the architecture. Checkpoint 328 preserves the successful >192 MiB public facade isolation qualification across text, visual and mixed routes, including managed-artifact reuse, original source-page provenance, direct ChatGPT image consumption, unchanged source identity and no source-adjacent derived files. Validation 086 contains the exact route, artifact, hash, warning and source-cleanliness evidence. Checkpoint 327 preserves the successful fresh disposable five-call `codex.pdf_access` intent matrix after the renderer repair, and Checkpoint 326 preserves the successful controlled restart and low-level live qualification of the formerly failing two-page `codex.document_render` path. Checkpoint 325 remains the source-published / restart-pending boundary. Checkpoint 325 preserves the successful live-source publication and independent installed-hash verification while explicitly keeping the running process restart-pending. Validation 083 is the detailed evidence, and `docs/local_execution/OPERATIONS.md` governs the next full controlled restart. Checkpoint 324 preserves the guarded publication preflight: the private 51/51 renderer candidate and a matching adapted installed render regression pass the complete seven-script staged public regression set, exact old/new hashes are bound, and no live file has yet been modified. Validation 082 is the detailed evidence; the next action is ordinary-host PowerShell publication with the exact qualified helper, followed by independent installed-hash verification before restart. Checkpoint 323 preserves the qualified direct-render serialization candidate: the public four-page request contract is unchanged, but each selected source page is rendered through a separate bounded read-only sandbox execution before ordered recombination and existing aggregate/source-drift checks. The focused serialization cases pass 2/2 and the full hybrid-PDF private suite passes 51/51 at private boundary `ad61a5619165ec5675e75daecdb4fdb29ea6f19a`. Validation 081 is the detailed evidence. The installed preview.16 renderer has not yet been changed, so guarded renderer-only publication and controlled restart remain next. Checkpoint 322 preserves the failed fresh-chat five-call `codex.pdf_access` intent matrix and the localized multi-page direct-render transport gap: text and auto-text routes passed; visual, mixed and auto-visual routes failed at the renderer; the same two pages fail when rendered together but pass individually with the already-qualified Checkpoint 321 image hashes. Checkpoint 321 preserves the fresh-chat end-to-end `codex.pdf_access` native hybrid qualification on the live preview.16 / 60-tool runtime: automatic `native-parts-plus-page-fallback` routing over the 78,874,939-byte Deep Learning 2 source, fourteen bounded native PDF resource links, direct embedded text and rendered images for individually oversized pages 16 and 49, direct ChatGPT inspection of both images, 14/14 host materialization of the native resources, and ordinary ChatGPT-side inspection of one materialized PDF part. Checkpoint 320 remains the simpler fresh-host native split qualification, and Checkpoint 319 remains the guarded facade source-publication and restart-pending boundary now superseded operationally by the successful preview.16 activation. The complete private hybrid-PDF suite now remains 51/51 PASS and the complete staged public regression remains accepted at the 60-tool surface. Checkpoint 318 remains the core-qualification boundary that closed the Checkpoint 317 restart-pending state by live-qualifying the 192 MiB direct text/render envelope and preserving deterministic routing, source profiling, native splitting, >192 MiB page/range isolation, managed content-addressed cache reuse/regeneration, cached text/render/resource adapters, native split render equivalence and the high-level `PdfAccessOrchestrator`. Checkpoint 317 remains the accepted architecture and 192 MiB source-publication boundary. Checkpoint 316 remains the successful same-chat end-to-end large-source text qualification, and Checkpoint 314 remains the successful same-chat end-to-end large-source visual qualification. Checkpoint 315 and Checkpoint 313 preserve the respective source-publication boundaries. Checkpoint 312 remains the Machine Learning generalization result that native PDF page-range splitting is not sufficient for all oversized PDFs because several individual pages exceed the host-qualified envelope by themselves. Checkpoint 311 remains the successful multi-native-PDF direct-access qualification for the 11,825,407-byte source. Checkpoint 310 remains the resolved fresh-host result that `updateModelContext` is advertised without the `resourceLink` modality. Checkpoint 309 remains the live 59-tool host-capability diagnostic publication and same-conversation stale-projection boundary. Checkpoint 308 remains the governing objective correction that restores direct ChatGPT local-machine file access through Codexless and separates it from delegated document analysis and future ADS product architecture. Checkpoint 307 remains the historical first held-out Astra semantic-worker `AMBIGUOUS` result and environment diagnosis. Checkpoint 306 remains the completed GPT-6 Astra Phase 2 reconciliation and preserved non-live source-bound semantic-evidence candidate. Checkpoint 305 remains the completed GPT-5.6 Sol Browser compatibility baseline. Checkpoint 304 preserves the live-qualified direct-Codex guard correction, while Checkpoint 303 preserves the localized resource-link host materialization interval, direct-HTTPS rejection, native `auto_review` live qualification, and Browser fallback opening. Checkpoints 302-293 remain the detailed progression from intermediate/large resource-link host tests through the original resource-link publication-preflight boundary. Checkpoint 292 preserves the live embedded-PDF host result, Checkpoints 291-280 preserve the preceding document-handoff/reuse-first/render/image experiments, and Checkpoint 279 remains the accepted `workspace-standard` + `codex.document_read` baseline.

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

The guided handoff boundary is preserved through Checkpoint 275. `chatgpt-17` then continued Research 113/117 through the document-resource and Browser-baseline work and closed at Checkpoint 305 after its own context-limit termination. `chatgpt-18` completed the independent Astra architecture challenge, corrected the workstream objective, qualified the host-capability, native split, large-source text/render and complete native-hybrid PDF routes, and closed at Checkpoint 321 when the conversation reached its length limit. The current `chatgpt-19` interaction preserved the failed fresh-chat PDF intent matrix as Checkpoint 322, qualified the renderer correction through Checkpoints 323-327, completed >192 MiB PDF isolation as Checkpoint 328, opened Research 121 at Checkpoint 329, closed AB-020 through Checkpoint 333, qualified/published/restarted the 61-tool Office file-link surface through Checkpoints 334-338, and now closes the fresh DOCX/PPTX/XLSX host matrix as Checkpoint 339. The direct ChatGPT local-machine PDF + Office access phase is complete for its accepted scope. The next stage is intentionally awaiting project-owner direction.

The repository now preserves the guided/repeated handoff, the Checkpoint 275 interruption residue, the v16 publication/test and Desktop comparison, the comprehensive upstream-research route, the successful semantic Git publication/push, the flexible multi-repository authority architecture, the `workspace-standard` generic non-Git extension, and live first-class PDF document reading. `chatgpt-17` also reproduced a continuity/routing weakness: the correct operational restart and ChatGPT app-refresh procedure already existed in `docs/local_execution/OPERATIONS.md`, but the collaborator initially gave generic/incorrect operational guidance before reading that governing runbook. The instance and the requested follow-up architecture audit are preserved in `docs/OPEN_ARCHITECTURE_BACKLOG.md` as AB-022 and AB-023; no routing fix has yet been accepted. The frozen public Checkpoint 279 content baseline is `bd7a2fcf802d99e6b9dd2b94745f248f347a12a9`. The private runtime repository is synchronized to that public baseline at `d86a96e2a26fbc946a31e28ef1ca14c8a129628a`, where `RUNTIME_STATE.json` explicitly records public Checkpoint 279 / `bd7a2fcf...`; this avoids recursive public/private anchoring while allowing a later public routing-envelope commit to point MC-0010 at both frozen evidence boundaries. Before Claude Message 001, verify that a fresh Claude environment can actually access both repositories; if private-repository access is unavailable, preserve that limitation rather than substituting public summaries. The earlier planned Chat 17 rotation preflight referred to the then-stable 52-tool surface; the current live surface is now 54 tools after the qualified `codex.image_read` and `codex.document_render` publications.

When rotation is chosen, follow `docs/CONTINUITY.md` and evaluate the actual transition evidence:

```text
exact-head public Repository Integrity PASS
required private continuity anchor reconciled and verified when applicable
local checkout synchronized with the public authority when required
no unrecorded guided or repeated handoff state
CHAT_ROTATION_PREFLIGHT evaluated as PASS / HOLD / FAIL from actual evidence
```

A new persistent conversation must allocate a fresh provider-local session/title, reconstruct public authority first, recover the relevant private local-runtime complement when accessible, and continue from the `office-file-link-matrix-qualified-awaiting-next-stage` boundary unless the repository has advanced further. Research 120 and Research 121 are both complete for their accepted PDF and DOCX/PPTX/XLSX direct-source scopes. No further Office parser/render fallback should be invented without a new concrete fidelity requirement. The current leaf is deliberately awaiting project-owner direction for the next stage. Preserve the 61-tool preview.17 live baseline, the closed AB-020 bounded integrity result, and the AB-008 fresh-chat projection caveat. For any future operational continuation, resolve and read the governing procedure referenced by the active boundary before giving exact mutation/restart instructions; AB-022 remains open. The broader `codexless-upstream-ecosystem-research` program remains active above this completed leaf, and the preserved Source Vault ingestion route remains paused beneath that Level-2 research phase until the project owner selects the next stage.

---

## Minimum reading for continuation

```text
README.md
docs/README.md
docs/CONTINUITY.md
docs/current_routing.json
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
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
