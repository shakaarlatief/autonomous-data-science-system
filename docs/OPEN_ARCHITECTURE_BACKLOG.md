# Open Architecture Backlog

**Status:** Current durable architecture and integration backlog
**Opened:** 2026-09-03
**Authority:** Planning and retrieval index only. This file preserves future ideas, intended investigations, explicitly deferred engineering directions, and continuation obligations so they are not lost across chats. It does not replace `docs/CURRENT_STATE.md`, `docs/OPEN_QUESTIONS.md`, accepted specifications/decisions, or the evidence artifacts linked from each item.

## Purpose

This backlog is for project knowledge of the form:

```text
we should investigate this later
this architecture is promising but not yet accepted
this is a known gap we do not want to forget
this should happen after the current phase
this workaround deserves a cleaner permanent design
```

The repository remains the memory. If an idea becomes important enough that the project owner explicitly wants to revisit it, record it here even when detailed evidence already exists elsewhere.

This is not a second current-state file. Volatile branch heads, active tool counts, and exact next actions belong in `docs/CURRENT_STATE.md` unless needed to explain an open item.

## Status and priority

```text
OPEN         worth investigating/designing
RESEARCHING  active evidence gathering or architecture comparison
IN_PROGRESS  implementation or qualification has started
PAUSED       deliberately deferred behind another boundary
BLOCKED      cannot proceed until an external prerequisite is met
MONITOR      watch upstream/product behavior; no immediate implementation
READY        sufficiently defined to execute when its turn arrives

P0  reliability/safety/continuity gap that can block normal ADS operation
P1  high-value near-term architecture or integration improvement
P2  useful future generalization or upstream simplification
P3  exploratory idea without current implementation commitment
```

Closed/accepted work should normally move into the stronger evidence layer and be removed or marked closed during reconciliation rather than accumulating indefinitely here.

---

## AB-001: Device-independent ChatGPT access to the local ADS connector

**Status:** RESOLVED FOR CONNECTOR REACHABILITY / MOBILE WEB PASS / NATIVE APP AUTH-CONTEXT FAIL
**Priority:** P0

If the user's laptop is running Codexless and the tunnel, the same authorized ADS connector should work from ChatGPT on laptop, phone, tablet, or another signed-in client.

Observed in `chatgpt-16`: the connector worked from the laptop, while the same conversation on the phone returned `401 tunnel_active_organization_required` even though the laptop remained on.

Research 122 / Validation 098 add an important current product constraint. Current OpenAI Developer Mode/MCP-app documentation states that MCP apps are not available on mobile and are web-only. The historical native-phone failure therefore must not be diagnosed merely as a dead laptop/tunnel. The next discriminator is device-surface specific: reproduce the native mobile-app behavior, then test `chatgpt.com` from the phone browser and, only if materially useful, desktop-site mode. If mobile web works, prefer that supported ChatGPT web path. If it does not, compare explicit remote/operator alternatives rather than weakening tunnel organization/principal validation.
Validation 125 / Checkpoint 367 complete that matrix. A fresh native-app chat discovered the ADS connector/tool but the invocation returned HTTP 401 `tunnel_active_organization_required`. A fresh ordinary phone-browser `chatgpt.com` conversation then invoked the same `codex.account_preflight` successfully with no connector/MCP/transport/auth/client error, while the local tunnel logged dispatcher forwarding and the laptop conversation remained usable afterward. Normal mobile web is therefore the accepted phone solution; desktop-site mode is unnecessary. AB-001 is resolved for connector reachability. Task/card/approval continuity across devices is deliberately not inferred and remains AB-006.

Research/acceptance targets:

```text
identify which layer requires active organization context
separate ChatGPT client/session identity from Codexless host identity
avoid relying on client-specific context that another client omits
verify laptop -> phone -> laptop continuity on one running tunnel
verify task/card inspection and approvals across devices
preserve least authority; do not weaken tunnel authentication to fix this
```

---

## AB-002: Narrow Codexless runtime self-maintenance authority

**Status:** CLOSED / LIVE SEMANTIC PUBLICATION + RESTART + ROLLBACK QUALIFIED
**Priority:** P1

Allow tightly bounded publication/recovery of the installed Codexless runtime without granting general filesystem authority over `%LOCALAPPDATA%` or another broad user-profile root.

Candidate semantic direction:

```text
codex.runtime_maintenance
    show
    publish
    verify
    rollback
```

Potentially add a separately bounded restart/lifecycle action only if it is safer than general host-process authority.

Required rule:

```text
ordinary workspace authority != host runtime-maintenance authority
```

Publication should use server-owned known install locations, exact candidate hashes, guarded atomic replacement, backup, verification, and rollback. Do not solve this by registering `%LOCALAPPDATA%` as an ordinary workspace.

Primary context: Research 116 and existing guarded host publication helpers. Validation 042 now provides a concrete reproduced case: the `codex.image_read` publication helper passed all candidate gates, but ordinary inherited `command_exec` was denied before writing `%LOCALAPPDATA%\\Codexless`; live hashes remained unchanged. This is exactly the separation this backlog item should solve without broadening workspace authority.

Validations 062-063 add two later examples. The native Auto-review executor and the direct-Codex guard correction were both safely qualified inside the authorized local-runtime workspace, but live installation still required one-time guarded host PowerShell publication with exact old/new hashes, backup, atomic replacement, verification, and rollback. Those bootstraps are accepted operational evidence, not a solution to AB-002.

Validation 067 provides a third concrete case. Publication of the temporary ChatGPT host-capability probe failed closed from the normal `ads-local-runtime` authority because the live `%LOCALAPPDATA%\\Codexless` install remained outside ordinary workspace write authority. A temporary exact-root `codexless-live` `workspace-standard` admission was used only to publish the already-qualified bytes, then removed immediately after verification. This was a bounded operational workaround, not the desired permanent architecture. AB-002 remains open specifically so future runtime maintenance does not require temporarily treating the install root as an ordinary workspace.

Validation 077 adds a fourth case and a cleaner workaround pattern. The normal `ads-local-runtime` authority again refused a direct write to `%LOCALAPPDATA%\\Codexless`, and this time no temporary live-install workspace was registered. A guarded ordinary-host PowerShell helper bound exact live/candidate hashes, staged and regressed the 60-tool candidate, performed atomic replacement with backups/rollback, and independent post-publication reads verified exact installed hashes. This confirms that the desired future semantic runtime-maintenance capability should reproduce those narrow publication/verification/rollback semantics without turning the install tree into an ordinary workspace.

Research 122 / Validation 098 add a new reuse-first discriminator. The exact installed tunnel-client v0.0.13 already exposes native managed-runtime lifecycle commands including `runtimes connect`, `status`, `stop`, `list`, `rm` and `cleanup`; its help explicitly positions `runtimes connect` as the long-lived runtime path managed by Codex. A direct `runtimes list --json` probe failed under ordinary ADS workspace authority only because the tunnel client attempted to initialize its default user-profile state directory. The same command succeeded with `TUNNEL_CLIENT_STATE_DIR` redirected into a bounded admitted temporary root. The current design target is therefore a dedicated runtime-maintenance state/credential/lifecycle authority that reuses the native tunnel manager, not broad `%LOCALAPPDATA%`/process authority and not a custom tunnel daemon by default. A separately owned supervisor/deferred helper is still required for Codexless/tunnel restart because a process cannot synchronously guarantee the response to the request that stops its own transport.


Validation 099 / Checkpoint 341 strengthen that discriminator with a functional failure/recovery test. An isolated managed tunnel forwarded real MCP initialize/tools-list traffic to Codexless, returned a visible 502 for a queued command while the local MCP path was intentionally absent, stayed running, and then forwarded a new initialize plus tools/list after the path returned without any tunnel reconnect. The preferred ordinary maintenance path is therefore now tunnel-preserving: a separately owned deferred helper should restart Codexless only, while full managed-tunnel stop/connect is reserved for tunnel-specific changes or failure. Tunnel `/readyz` alone is not sufficient proof of local-backend recovery because the isolated runtime could remain nominally ready while the backend path was absent.

Validation 100 / Checkpoint 342 qualify the next layer. A private file-backed ledger now preserves request-to-operation identity across independent instances using a server-owned state root, hashed request-index filenames and atomic JSON replacement; a narrow detached launcher accepts only the already-bound opaque operation ID while executable/script/cwd/state/environment remain server-owned. The focused suites pass 12/12 plus 6/6. A real isolated dummy-service probe then demonstrated that the detached helper continued after the invoking generic `command_exec` wrapper timed out, replaced generation A with healthy generation B on the same endpoint, and wrote a durable `succeeded` receipt read by a later invocation. The timeout is explicitly not treated as a clean launch result: generic `command_exec` is rejected as the permanent launcher. The intended semantic `codex.runtime_maintenance` implementation must dispatch the helper directly from Codexless, return/record the accepted operation before the destructive delay, and use later requestId/operationId status as authoritative if delivery is uncertain. The next gate is exact Codexless process/listener identity plus an isolated production-shaped worker restart.

Validation 101 / Checkpoint 343 qualify that next gate. The candidate now has a private random runtime instance identity and shutdown token, exact health-to-identity matching, a fixed authenticated loopback graceful-shutdown endpoint, a production-shaped one-shot supervisor that never kills an arbitrary PID, a fixed replacement-worker launcher, durable active-operation exclusion, and direct Codexless-owned semantic dispatch that returns an armed receipt before the fixed destructive delay. Functional probes prove exact-instance replacement, acceptance before restart, idempotent replay, wrong-token rejection and private identity cleanup. The staged preview.18 integration exposes only `restart_codexless`/`status` plus `requestId` at 62 tools and preserves existing Git/PDF/Office regressions. Production is still preview.17 / 61 tools; the next gate is guarded preview.18 source publication and one final runbook-controlled bootstrap restart before the new tool can live-qualify itself.

Validation 102 / Checkpoint 344 qualify the guarded publication package itself. The helper is exact-head/hash bound, requires the running preview.17 / 61-tool and live/ready tunnel baseline, stages and tests the full 62-tool integration, exercises the same Windows atomic forward/rollback primitive before mutation, and has passed two complete no-publish runs. Publication will remain source-only with exact backups/rollback and `RESTART_PERFORMED=false`; ordinary-host publication is now the next gate.

Validation 103 / Checkpoint 345 preserve successful ordinary-host source publication. Independent rehashing proves every installed preview.18 publication target exactly matches the qualified candidate while AB-020 semantic-Git and preserved document regressions remain unchanged. The currently running process is still preview.17 / 61 tools and the tunnel remains live/ready, so the next gate is the one final full runbook-controlled bootstrap restart before the 62nd tool can be discovered and live-qualified.

Validation 104 / Checkpoint 346 qualify that activation gate. The active process now reports preview.18 / 62 tools; listener PID, private runtime identity and public health all bind to the same instance; the private shutdown token is not exposed; the tunnel is live/ready; and a direct local MCP initialize/tools-list returns exactly 62 tools including `codex.runtime_maintenance` with the intended closed schema. ChatGPT app refresh plus fresh-chat host discovery is now the next gate before any live restart mutation.

Validation 105 / Checkpoint 347 localize a new host-schema fidelity gate. Fresh-chat discovery exposed `codex.runtime_maintenance`, but ChatGPT genericized the top-level discriminated-union schema to `{ [key: string]: any }`, so the action enum, required `requestId` and `additionalProperties: false` were not host-certifiable. No tool was invoked. Local MCP remained strictly validated, so this is projection fidelity rather than server authority widening. Validation 106 / Checkpoint 348 qualify a minimal preview.19 correction: one strict top-level object with an action enum plus required `requestId`, with an actual MCP initialize/tools-list wire regression proving the serialized schema. Core public and lifecycle suites remain green; production stays preview.18 / 62 tools pending guarded publication.

Validation 107 / Checkpoint 349 qualify the exact three-file guarded publication package for preview.19. Two no-publish preflights passed the wire-schema assertion, eight public regressions, lifecycle suites/probes and atomic replacement/rollback smoke. The helper performs no restart; ordinary-host source publication is next, followed by independent installed-hash verification and a manual activation restart because the preview.18 host projection is not accepted for self-restart bootstrap.

Validation 108 / Checkpoint 350 preserve successful preview.19 source publication. Independent read-only rehashing proves the exact three qualified installed hashes and unchanged AB-020 semantic-Git while the active process remains preview.18 / 62 and the tunnel remains live/ready. One manual runbook-controlled activation restart is next; only after preview.19 is active and a fresh chat projects the flat schema structurally may the first production self-restart be invoked.

Validation 109 / Checkpoint 351 qualify preview.19 process-live activation. Exact runtime-instance binding and tunnel recovery pass, and direct MCP initialize/tools-list now returns the corrected flat schema with required `action`/`requestId`, action enum, `additionalProperties: false`, and no top-level union. The next gate is refreshed fresh-chat host projection; no live self-restart has yet been invoked.

Validation 110 / Checkpoint 352 close the fresh-host schema gate. After app refresh, a disposable fresh chat projects `codex.runtime_maintenance` as a structured object containing only required `action` and `requestId`, with the exact two-action enum and requestId bounds/pattern; the preview.18 generic-map projection is gone. No ADS tool was invoked. The first production self-restart qualification is now the next gate.

Validation 111 / Checkpoint 353 qualify the first production self-restart end to end. The fresh-host restart returned `armed` before destructive work, the exact old Codexless instance was replaced by a new preview.19 / 62-tool instance, the same tunnel process stayed running and healthy, durable status returned `succeeded`, and explicit same-request replay produced no second restart. Ordinary Codexless-only lifecycle restart is therefore live-qualified. AB-002 remains open for the other half of its original objective: narrow semantic publication/verify/rollback of qualified installed-runtime bytes without ordinary `%LOCALAPPDATA%` workspace authority or host PowerShell helpers.

Validation 112 / Checkpoint 354 qualify that remaining authority class in an isolated preview.20 candidate. The proposed 63rd tool accepts only a semantic action, bounded release/request identifiers and an exact private source HEAD; release bytes are fixed to a clean synchronized private-runtime release namespace and exact hashes. Publication is baseline-hash bound, regression-gated, snapshot-backed and source-only until pending activation. The existing exact-instance restart helper now verifies the pending target contract and automatically recovers previous source/runtime on failed forward activation; rollback has symmetric target-reapply recovery. Immutable activation history fixes chained release rollback semantics. No live install mutation occurred. AB-002 remains open only for the guarded preview.20 bootstrap publication, live host-schema/operation qualification and confirmation that subsequent qualified releases no longer require ordinary-host publication helpers.

Validation 113 / Checkpoint 355 harden the one-time preview.19 -> preview.20 activation seam before publication. The newly installed supervisor can now distinguish the legacy preview.19 launcher environment, derive its fixed install root from its own module location and derive the preview.20 replacement contract from newly installed surface constants, while normal preview.20+ restarts retain explicit process-bound configuration. The dedicated bootstrap probe passes. The exact helper, bound to private head `77e13dc...` and SHA-256 `c88c3085...`, passed two complete no-publish runs with the full public/lifecycle/release matrix and Windows atomic forward/rollback smoke. Production remains unchanged. AB-002 now advances to source-only publication, semantic activation, fresh-host `codex.runtime_release` qualification and proof that a later qualified release can use the semantic release path end to end without another ordinary-host publication helper.

Validation 114 / Checkpoint 356 preserve the successful source-only publication boundary. The qualified helper published preview.20, all nine live-disk public regressions passed, and independent post-publication comparison found zero mismatches across all 22 candidate `src`/`test` files. The executing process remains preview.19 / 62 and the tunnel remains `live/ready`, so no hidden restart occurred. AB-002 now advances to semantic bootstrap activation through `codex.runtime_maintenance`, followed by refreshed-host `codex.runtime_release` schema/live-operation qualification.

Validation 115 / Checkpoint 357 qualify that semantic bootstrap activation in production. The old preview.19 process returned `armed`, the newly installed supervisor launched preview.20 / 63 successfully, both PID and instance changed, durable status returned `succeeded`, and the same tunnel PID remained live/ready throughout. No manual process/tunnel restart was needed. AB-002 now advances to refreshed-host `codex.runtime_release` schema discovery and then one later qualified release updated end to end through the semantic release + semantic restart path, which is the proof required to retire ordinary-host publication helpers for normal future updates.

Validation 116 / Checkpoint 358 close the refreshed-host schema gate. A fresh disposable chat projects `codex.runtime_release` as one strict four-field object with required semantic action/release/request/source-head inputs and no generic host-authority surface. No tool was invoked in that chat. AB-002 now advances to the decisive normal-update proof: build a genuine next-version release bundle under the fixed private namespace, then qualify prepare -> publish -> activation -> verify/status and rollback/recovery through the semantic surfaces without another ordinary-host install helper.

Validation 117 / Checkpoint 359 qualify that genuine next-version bundle. `preview21-semantic-release-e2e` is committed at clean synchronized private head `7aa303f...`, changes only the public version constant plus matching exact-version regression, binds exact live preview.20 baseline hashes and target payload hashes, and passes the full nine-script staged release regression set. No live mutation has occurred. AB-002 now advances to live semantic prepare/pre-publication verification before the first semantic publish.

Validation 118 / Checkpoint 360 qualify live preparation and the pre-publication verifier. `prepare` returned `prepared`; `verify` returned the expected two-file mismatch while independent checks prove the live preview.20 install/process/tunnel remain unchanged. This establishes server-owned prepared state plus real installed-byte verification before mutation. AB-002 now advances to one isolated semantic `publish` call, followed by independent source/status verification before any activation restart.

Validation 119 / Checkpoint 361 qualify the first semantic installed-source publication. The public publish call returned `armed`, the detached operation reached durable `succeeded`, exact preview.21 bytes are installed, a forward pending activation is present, the shared lock is released, and preview.20 plus the same tunnel remain running. This is the first real proof that `%LOCALAPPDATA%` publication no longer needs an ordinary-host helper. AB-002 now advances to semantic activation, post-activation verify/status, and live rollback/recovery qualification.

Validation 120 / Checkpoint 362 complete the forward update proof. Semantic restart replaced preview.20 with healthy preview.21 / 63, preserved the exact tunnel process, returned durable `succeeded`, cleared pending/lock state, and finalized preview.21 as the active managed release with immutable activation history. No ordinary-host publication or manual restart was used. AB-002 now requires only post-activation public verify/status plus explicit semantic rollback and rollback activation qualification before closure can be considered.

Validation 121 / Checkpoint 363 close the post-activation public readback portion. Fresh-host status returns the original publish operation as durable `succeeded`, fresh-host verify reports `verified` with zero mismatches, and independent inspection confirms the active preview.21 install/process/tunnel remain unchanged. AB-002 now advances to semantic rollback publication followed by separate rollback activation and final-state qualification.

Validation 122 / Checkpoint 364 qualify semantic rollback publication. The public rollback call returned `armed`, the detached operation reached durable `succeeded`, exact preview.20 source hashes were restored, a rollback pending activation was created, and preview.21 plus the tunnel intentionally remain running. AB-002 now advances to rollback restart activation and final readback/state qualification.

Validation 123 / Checkpoint 365 qualify rollback activation itself. Semantic restart replaces preview.21 with healthy preview.20 / 63, preserves the exact tunnel process and restored hashes, returns durable `succeeded`, clears pending/lock state and removes the active managed-release pointer because preview.20 is the unmanaged predecessor. AB-002 now has both forward and rollback execution paths production-qualified; only final public rollback status/verify readback remains before closure can be considered.

Validation 124 / Checkpoint 366 close AB-002. Fresh-host rollback status returns durable `rollback_release / succeeded`; post-rollback verify returns the exact expected two mismatches; independent final inspection confirms healthy preview.20 / 63, exact restored hashes, no pending/active managed release or mutation lock, clean synchronized private source and tunnel `live/ready`. The accepted architecture now performs ordinary future release publication, activation, verification, rollback and Codexless-only restart through narrow semantic surfaces without ordinary `%LOCALAPPDATA%` workspace authority, caller-selected process/path/command authority, a user-run installation helper or manual Codexless/tunnel restart. Reopen AB-002 only if a materially different runtime topology/authority contract or new reproduced maintenance failure makes this accepted class insufficient.

Validation 127 / Checkpoint 369 exercise that accepted architecture during a real post-closure recovery. A Windows Codex installation-generation transition orphaned sandbox-helper resolution; bounded semantic restart recovered command execution while preserving the managed tunnel. The same incident also exposed that semantic `git_commit_paths` should treat `git add` and `git commit` as bounded host-owned repository-metadata mutations rather than ordinary Codex command-sandbox writes. The corrected host-metadata route was published and activated through `codex.runtime_release` plus `codex.runtime_maintenance` without broadening `.git` ACLs or public authority. This strengthens rather than reopens AB-002.

---

## AB-003: Autonomous supervision and wakeup for long-running Codex tasks

**Status:** DEFERRED / OPTIONAL DIRECT-CODEX ORCHESTRATION CONVENIENCE
**Priority:** P2

Validation 035 reproduced the liveness failure:

```text
ChatGPT starts/supervises Codex
-> assistant response ends
-> Codex continues
-> Codex later reaches approval/error/completion
-> Rich Card may update
-> ChatGPT does not autonomously wake to inspect it
-> task can remain blocked until the user sends another message
```

Candidate directions:

```text
App Server notification/subscription mechanism that can drive a real wakeup
MCP App mechanism that can cause genuine assistant follow-up execution
external task supervisor/daemon with durable state monitoring
user notification when attention is needed
server-side handling of only profile-approved low-risk approvals
prominent actionable card state for approval/error/completion
```

The Call Profile is policy guidance, not a scheduler. The permanent design must close the liveness gap rather than merely instruct the assistant to supervise harder.

Validation 062 live-qualified one important mitigation: formal turns now use App Server `approvalPolicy=on-request` with `approvalsReviewer=auto_review` while preserving the separate initial `Call Codex?` gate and existing bounded permission profile. Routine in-turn command approvals no longer reproduced the `awaitingApproval` stall in the tested case. AB-003 remains open because ChatGPT still has no demonstrated autonomous wakeup for task completion, errors, escalations, or any future action that native Auto-review cannot safely resolve.

Primary evidence: `docs/local_execution/validation/035_running_codex_supervision_liveness_gap_reproduced.md`.

Checkpoint 368 / Validation 126 change the priority rather than disputing the reproduced gap. The project owner accepts manual ChatGPT-to-Codex prompt transfer, and current OpenAI Codex Remote already provides supported phone supervision for Windows-hosted Codex work. Autonomous ChatGPT wakeup is therefore no longer a core ADS blocker. Reopen this item only if direct ADS-to-Codex orchestration is deliberately re-prioritized and a concrete workflow needs unattended assistant-side supervision beyond native Remote.

---

## AB-004: Active-turn writer ownership transfer and reacquisition

**Status:** DEFERRED / OPTIONAL DIRECT-CODEX DESKTOP-HANDOFF RESEARCH
**Priority:** P2

Support a professional handoff between ChatGPT/Codexless and Codex Desktop while a turn is active, not only after the thread becomes idle.

Questions:

```text
can writer ownership transfer cooperatively during an active turn?
can Desktop service an approval for a Codexless-owned active turn?
can Chat reacquire writer ownership without replaying work?
if transfer is unsupported, can interrupt/release/resume preserve exact continuity?
how are pending approvals routed when ownership changes?
```

The verified idle archive -> unarchive -> rebind -> resume path remains accepted.

Primary evidence: Validation 035, Research 109-112, Validations 027-032.

Checkpoint 368 / Validation 126 demote active-turn writer transfer from a core requirement. The accepted workflow is manual prompt copy/paste plus native Codex Remote, so ChatGPT/Codexless does not need to own and transfer every active Codex thread. Preserve the verified idle handoff and this research question for future optional direct-orchestration work only.

---

## AB-005: Reuse-first multimodal document architecture

**Status:** RESOLVED FOR ACCEPTED PDF + OFFICE DIRECT-SOURCE SCOPE / REOPEN ON NEW FORMAT OR RENDERED-FIDELITY TRIGGER
**Priority:** P1

Research 119 / Checkpoint 308 restore the actual objective: ordinary ChatGPT chat should gain direct bounded access to files in already-authorized local-machine workspaces through Codexless, without requiring the user to manually upload each file and without inserting a Codex reasoning model merely because the source is local. Whole-file/native handoff is preferred when supported; faithful model-free text, structure, cells or rendered media delivered directly to ChatGPT are valid fallbacks. Research 118's semantic-worker/receipt branch remains preserved only as optional future delegated-analysis or ADS-product research. The prepared second Astra semantic-worker task was declined before any model turn.

Checkpoint 309 / Validation 067 introduced the narrow direct-host discriminator before PDF splitting, and Checkpoint 310 / Validation 068 resolved it: the current ChatGPT host advertises `updateModelContext` but not its `resourceLink` modality. Checkpoint 311 / Validation 069 qualified deterministic multi-native-PDF handoff. Checkpoint 312 / Validation 070 showed that individual native pages can still exceed the host envelope. Checkpoint 313 / Validation 071 and Checkpoint 314 / Validation 072 qualified direct model-free page rendering from the 78,874,939-byte Deep Learning 2 source into ChatGPT vision. Checkpoint 315 / Validation 073 and Checkpoint 316 / Validation 074 qualified the corresponding large-source embedded-text route. Research 120 / Checkpoint 317 accepted the automatic hybrid architecture: conservative 7,000,000-byte native whole/part targets, a 192 MiB direct text/render processing envelope, isolation above that envelope, and a Codexless-owned content-addressed cache for generated split/page artifacts with source-authority revalidation. Checkpoint 318 / Validation 076 qualified that core end to end. Checkpoint 319 / Validation 077 qualified the bounded `codex.pdf_access` public facade and preserved guarded live-source publication. Checkpoint 320 / Validation 078 qualified the first fresh-host automatic native split route. Checkpoint 321 / Validation 079 now qualify the difficult large-PDF native hybrid route end to end: one facade call on `51.Deep Learning2.annotated.pdf` returned fourteen bounded native PDF resource links plus embedded text and rendered PNG fallback for individually oversized source pages 16 and 49; ChatGPT directly inspected both images, the host materialized all fourteen native PDF resources, and ordinary ChatGPT-side PDF inspection succeeded on one materialized part. The current persistent chat still lacks the new callable projection, reinforcing AB-008 while leaving the fresh-host result intact. The `intent=native` architecture is therefore closed at the host boundary. Checkpoint 322 / Validation 080 then attempted the remaining five-call intent matrix. Explicit `text` and `auto` with `visualRequired=false` passed as `direct-text`; `visual`, `mixed`, and `auto` with `visualRequired=true` failed at the lower renderer with `DOCUMENT_RENDER_PROTOCOL_ERROR`. Call 2 also carried a preserved extra `visualPages` input, while Calls 3 and 5 matched their frozen inputs and independently reproduced the same failure. Low-level discrimination showed pages 16 and 49 fail only when rendered together and pass individually with the same hashes as Checkpoint 321. The active seam was therefore the previously known Windows buffered `command/exec` transport pressure in multi-page direct rendering. Checkpoint 323 / Validation 081 now qualify the bounded correction in the private candidate: each selected source page is rendered in one separate read-only sandbox execution, child protocols/page counts are validated independently, requested order is preserved, and the existing per-page/aggregate/source-drift safeguards remain. Focused serialization regression passes 2/2 and the complete private hybrid-PDF suite passes 51/51 at `ad61a5619165ec5675e75daecdb4fdb29ea6f19a`. Checkpoint 324 / Validation 082 qualified the exact guarded publication package. Checkpoint 325 / Validation 083 now preserve successful host publication and independent installed-hash verification: the live-disk renderer and matching render regression exactly match the qualified target hashes, all seven live-disk public regressions passed, backups were created, and the helper explicitly reported `RESTART_PERFORMED=false`. The running preview.16 process and tunnel remain healthy at 60 tools and HTTP 200/200 before restart, but the newly published renderer behavior is not yet active evidence. Checkpoint 326 / Validation 084 qualify the restarted low-level renderer live: the formerly failing two-page `[16,49]` request succeeds with both prior hashes preserved and direct image delivery. Checkpoint 327 / Validation 085 close the corresponding fresh-host high-level matrix. All five scheduled `codex.pdf_access` routes succeeded: explicit text -> `direct-text`, explicit visual -> `direct-render`, explicit mixed -> `direct-text-plus-selective-render`, auto without required vision -> text/direct-text, and auto with required vision -> mixed/direct-text-plus-selective-render. Every rendering-dependent call returned pages 16 and 49 with identical PNG hashes across Calls 2, 3 and 5, while every text-bearing call returned the same untruncated 19,344 characters. No PDF resource links or host PDF materialization were involved. Checkpoint 328 / Validation 086 now qualify the remaining >192 MiB public facade routes on a valid 211,813,221-byte source: `isolate-then-text`, `isolate-then-render`, and `isolate-then-text-plus-render` all pass; the first request generates one 862-byte managed page artifact; later routes reuse the same generation; original source-page provenance remains 1; the image is directly inspectable; the source hash remains unchanged; and no derived artifact appears beside the source. Research 120's accepted PDF route family is therefore complete. Research 121 / Checkpoint 329 / Validation 087 now open the next reuse-first file-type boundary. Current OpenAI product evidence explicitly supports DOCX, PPTX and XLSX uploads, maintained MCP resource links are MIME-generic, and local source inspection shows that the current PDF whole-file resource path already contains the reusable authority/binding/TTL/read-revalidation substrate while its PDF restriction is concentrated in media validation. The accepted next implementation is therefore one narrow allowlisted `codex.file_link` private candidate, not three new parsers. Tiny deterministic DOCX/PPTX/XLSX fixtures should then qualify host materialization, text/data/structure access and visual/layout fidelity separately; format-specific parser/render fallbacks are justified only where that matrix exposes a real gap.

The first-class `codex.document_read` PDF baseline is no longer open work. It is live-qualified on Codexless `0.1.1-preview.9` / 52 tools through Validation 039 and Checkpoint 279, including the isolated bounded `pdfjs-dist@5.4.624` parser child and a real read-only personal-PDF test.

Research 117/119 now applies a direct-access-first rule: first reuse supported ChatGPT/OpenAI/MCP file transport and model-free source/media delivery so ChatGPT itself receives the authorized local source. Installed Codex Skills and Codex workers can still inform implementation or serve optional delegation workflows, but they are not the default data path for this objective. Mature converters such as MarkItDown, Docling, or PyMuPDF4LLM remain candidates only when a concrete format gap cannot be solved through supported direct/native or deterministic source representations.

Checkpoint 339 / Validation 097 close the Research 121 Office capability matrix. A refreshed fresh ChatGPT conversation exposed `codex.file_link`; exactly one DOCX, PPTX and XLSX call each succeeded; all three original files materialized with exact byte size/SHA-256; and ordinary ChatGPT-side inspection established native content/structure beyond flattened text. DOCX preserved table structure plus the embedded image, PPTX preserved two-slide ordering plus picture-object placement and embedded image content, and XLSX preserved sheets, formulas, cached values and style metadata. No format-specific parser/render fallback is required for the accepted whole-file direct-source objective. Pixel-identical Microsoft Office rendering was not claimed and is now a trigger-based separate capability only if a future task explicitly needs final rendered fidelity.

The accepted current direct-source family is therefore:

```text
local images        -> codex.image_read
PDF                  -> codex.pdf_access + qualified semantic fallback routes
DOCX / PPTX / XLSX  -> codex.file_link native whole-file handoff
```

Remaining document-system directions are separate capabilities rather than unfinished AB-005 work:

```text
codex.document_render
    visual page/slide rendering for equations, tables, diagrams, plots, and layout

explicit OCR path
    only for scanned/no-text material
    separate from ordinary embedded-text extraction

future adapters
    DOCX / text / Markdown / PPTX / other formats when justified

stronger parser isolation
    evaluate an OS-level no-network parser sandbox if its operational benefit justifies the added complexity
```

Do not weaken the accepted `codex.document_read` authority contract merely to add these companions. Rendering/OCR/adapters should continue to inherit explicit workspace authority and remain semantic rather than arbitrary host-file execution paths.

Primary accepted baseline evidence: `docs/local_execution/validation/039_workspace_standard_and_document_read_live_qualified.md`. Validation 040 proves that the maintained Codex PDF Skill routes in the authorized workspace, although that turn found an unusable MiKTeX `pdftoppm` stub and did not locate an alternative renderer. Validation 041 proves that an already-authorized local PNG can be visually understood through Codex's native `view_image` path. Validation 043 proves the model-free direct-host path: `codex.image_read` returns standard MCP image content visible to ChatGPT model vision, with no extra Codex model turn, Browser or OCR. Validation 044 proves the maintained OpenAI/Codex primary runtime already contains viable Poppler rendering. Validation 045 then qualifies the preferred thin semantic seam: `codex.document_render` keeps untrusted PDF rendering inside the existing Codex `command/exec` read-only sandbox and reuses maintained primary-runtime `pdfjs-dist` + `@napi-rs/canvas` to produce in-memory PNG pages returned as standard MCP image content. Its publication preflight passes at preview.11 / 54 tools with no caller write authority, no extra Codex model turn, no new external dependency, and no live publication yet. Representative PDF fidelity remains the next document-specific qualification after live publication.

---

## AB-006: Robust Codex task recovery after caller/tunnel/device interruption

**Status:** DEFERRED / OPTIONAL CODEXLESS-DIRECT TASK RECOVERY / NATIVE REMOTE ACCEPTED
**Priority:** P2

A task already accepted under Codexless should remain recoverable when the ChatGPT client changes device, the tunnel temporarily rejects the caller, or the supervising chat cannot poll.

Desired guarantees:

```text
durable taskRef/threadId identity where runtime state permits
no replacement task before surviving state is inspected
model-free reattach/recovery where possible
pending approval state remains explicit
uncertain sends are never replayed
terminal completion/failure is reconstructable after reconnection
caller-device changes do not silently orphan supervision
```

This is distinct from AB-001 (connector access) and AB-003 (automatic wakeup).
Checkpoint 367 / Validation 125 now remove the AB-001 prerequisite: normal phone-browser ChatGPT reaches the same ADS connector successfully. AB-006 can therefore test recovery on a real supported second client rather than conflating task continuity with connector availability. The first discriminator should use a bounded non-destructive task whose durable identity is known on laptop, switch to the phone browser without creating replacement work, inspect surviving task/card/thread state, then return to laptop and verify the same identity/state before any continuation.

Checkpoint 368 / Validation 126 supersede that next discriminator as a project blocker. Current OpenAI Codex Remote is now live-qualified on the paired Windows/iPhone setup, including phone-started continuation of the same desktop Codex thread while the visible desktop UI is closed. Because the project owner accepts manual prompt/result transfer, direct Codexless-owned task recovery across devices is optional convenience work. Preserve the original guarantees if direct orchestration returns to scope, but do not block the broader ADS roadmap on them.

---

## AB-007: Actionable Rich Card supervision surface

**Status:** DEFERRED / OPTIONAL CUSTOM RICH-CARD SUPERVISION
**Priority:** P2

Make the Rich Task Card a professional supervisory surface rather than only a passive status display.

Candidate improvements:

```text
prominent approval-required state
safe approve/reject controls when host policy permits
clear writer/owner/client identity
one evolving semantic command/file/message item rather than raw event rows
clear completion/error/recovery actions
cross-device card continuity
```

Design this with AB-003, AB-004 and the v17 viewer rather than as an isolated UI patch.

Checkpoint 368 / Validation 126 also demote this item. Native Codex Remote already supplies the user-facing mobile supervision surface, and the project owner does not require ChatGPT to launch every Codex turn directly. Rich Card improvements remain useful only for optional direct Codexless orchestration or future viewer work; they are no longer a core mobile requirement.

---

## AB-008: Stable MCP schema and ChatGPT tool-projection lifecycle

**Status:** OPEN / MONITOR / TOP-LEVEL UNION SCHEMA GENERICIZATION REPRODUCED
**Priority:** P1

Validation 034 showed an existing conversation can retain an older callable action projection after the live MCP server publishes new actions. Research 116 therefore moved ordinary workspace/project variability into server-owned policy behind stable schemas.

Validation 067 reproduces the behavior more strongly. The live server was directly verified at `0.1.1-preview.15-host-capability-probe` / 59 tools and the tunnel was ready; the user then refreshed the existing `ADS Codexless Local Bridge` Plugin in the same persistent conversation. ChatGPT-side rediscovery still did not expose the three newly added host-capability tools. Validation 068 then confirms that a separate fresh disposable conversation did expose those new tools and successfully mounted the probe MCP App. Validation 078 reproduces the same lifecycle pattern on the preview.16 / 60-tool publication: the persistent conversation lacked callable `codex.pdf_access`, while a fresh disposable chat immediately discovered and executed the facade successfully. Validation 096 / Checkpoint 338 reproduce the pattern again for preview.17 / 61 tools: the live runtime and tunnel were healthy but the persistent chat did not expose newly added `codex.file_link`. Validation 097 then closes the fresh-chat discriminator: after app refresh, a fresh disposable conversation exposed `codex.file_link` and successfully executed the complete DOCX/PPTX/XLSX matrix. The observed rule therefore remains: same-chat Plugin refresh can retain a stale callable projection, while a fresh chat acquires the updated projection. The broader cause/lifecycle contract remains open. Validation 105 adds a distinct schema-shape projection failure. A fresh chat did acquire the new runtime-maintenance tool, but its top-level discriminated union was projected as a generic map. The current host likewise genericizes the older workspace-authority discriminated union, while ordinary top-level object schemas remain structured. Preview.19 therefore uses a flat strict object for the mutation-sensitive runtime-maintenance surface and adds wire-schema regression coverage. This does not resolve the host behavior generally; AB-008 remains open. Validation 110 confirms the flat preview.19 schema projects correctly in a refreshed fresh chat, resolving the concrete runtime-maintenance projection blocker while leaving AB-008 open for the broader stale-projection and union-genericization behavior.
Validation 116 adds the same positive host result for preview.20 `codex.runtime_release`: the fresh chat exposes the strict four-field flat object correctly. This further supports flat top-level object schemas for mutation-sensitive developer-MCP actions while the broader same-conversation stale-projection behavior remains open.
Validation 145 / Checkpoint 388 reproduce the separate stale-projection branch at preview.24 / 64 tools. Runtime Release publication and activation pass, direct active local MCP `tools/list` contains the new `codex.github_authorization` support tool with its strict schema, and a direct local metadata-only call succeeds. The existing persistent ChatGPT conversation nevertheless does not expose that new tool as a callable projected action. This is direct evidence that a healthy live 64-tool server can still coexist with a stale same-chat host projection; fresh-chat qualification remains the accepted route for newly added tools.
Validation 146 / Checkpoint 389 add a second preview.24 host result after fresh-chat discovery: `codex.github_authorization` itself projects, but its top-level discriminated union is genericized to a string-keyed `any` map and the single metadata attempt is safety-blocked before dispatch is established. Preview.25 now reuses the qualified flat-object correction from runtime maintenance/release. Direct local wire inspection proves the corrected schema has no union. Fresh-chat requalification remains required to determine whether metadata safety blocking disappears once the host sees bounded fields.
Validation 147 / Checkpoint 390 close the concrete AB-008 authorization discriminator: preview.25 projects the flat bounded schema structurally in a fresh host and the metadata action succeeds. The same checkpoint also qualifies the live ChatGPT Plugin display name as `Codexless Runtime Bridge`. No broader claim is made that all top-level unions will always fail, but mutation-sensitive developer-MCP actions continue to prefer host-visible flat schemas where equivalent bounded authority can be preserved server-side.

Remaining questions:

```text
what causes ChatGPT to refresh/retain MCP action projections?
which changes truly require app refresh or a fresh chat?
why can live MCP tool count differ from projected callable count?
can compatibility probes detect stale projections automatically?
```

---

## AB-009: Developer MCP and native ChatGPT connector coexistence

**Status:** MONITOR / OPEN HOST LIMITATION
**Priority:** P2

Repeated fresh-chat attempts to combine the ADS developer MCP with native connectors such as GitHub produced `FORBIDDEN: This conversation is restricted to developer MCPs` while the native connector could still appear discoverable.

Direction:

```text
monitor OpenAI product/documentation changes
reproduce after relevant updates
prefer Codexless + authorized local clones for critical development continuity
keep native GitHub useful for remote-only metadata/review when available
do not make same-conversation coexistence a hard dependency until proven
```

Primary evidence: Validation 034 and Research 116.

---

## AB-010: v17 semantic Codex task viewer

**Status:** PAUSED / RESEARCHING
**Priority:** P1

Replace the v16 event-log-like presentation with a semantic, Desktop-quality task narrative while preserving the companion-card advantages.

Candidate architecture uses App Server `Thread -> Turn -> Item` semantics where the exact runtime proves them:

```text
one evolving agent-message item
one evolving command item with streamed output
compact file-change summaries + reviewable diffs
prominent approval items
safe visible reasoning-summary presentation without hidden chain-of-thought
semantic status/lifecycle grouping
subagent/tree presentation when justified
```

The target is to expose the useful user-visible information normally available in Codex Desktop, including normal visible reasoning/progress summaries where the product exposes them. If a truly native-equivalent live Desktop view cannot be achieved, keep the previously discussed professional fallback of a strong companion surface plus exact Desktop handoff/opening rather than faking unsupported synchronization.

Do not implement v17 until Research 113 provides enough evidence to avoid duplicating upstream mechanisms.

---

## AB-011: Same-turn steering and persistent follow-up queues

**Status:** RESEARCHING
**Priority:** P1

Evaluate official/experimental App Server `turn/steer` and `thread/queue/*` for supervision and planned follow-ups.

Required safeguards:

```text
exact expected active-turn identity
caller-stable idempotency
no replay after uncertainty
no authority widening
clear steer-vs-next-turn distinction
metered consent remains explicit
queued work has predictable persistence/recovery
```

---

## AB-012: App Server reviewer / auto-review integration with Call Profile

**Status:** LIVE-QUALIFIED COMPLEMENT / BROADER ESCALATION BEHAVIOR OPEN
**Priority:** P1

Validation 062 established the supported complement for the tested routine-command case. Codexless formal turns now explicitly request App Server `approvalPolicy=on-request` plus `approvalsReviewer=auto_review`, while the separate ChatGPT-side `Call Codex?` gate and the resolved bounded permission profile remain unchanged.

The layers stay distinct:

```text
Call Profile        user-authored policy for whether/how ChatGPT calls and supervises Codex
App Server reviewer lower-level in-turn action risk review/routing
```

A fresh formal task under `ads-direct-git` completed routine PowerShell and Git status work without surfacing an in-turn approval or entering `awaitingApproval`. Full access was not used.

This does not prove every action can or should be auto-reviewed. High-risk/ambiguous escalation behavior, user-facing explanation for native reviewer decisions, and interaction with the still-open autonomous wakeup/writer-ownership questions remain research work.

---

## AB-013: Shared spectator / cross-client live synchronization

**Status:** RESEARCHING
**Priority:** P1

Determine whether ChatGPT, Rich Card and Codex Desktop can observe one running thread through a supported shared/spectator model without competing for writer ownership.

Research:

```text
connection-scoped subscriptions
read-only history/item APIs during active writer ownership
Desktop live-refresh limits
shared-runtime vs separate-App-Server behavior
approval visibility for spectators
whether one writer + many spectators is the correct permanent model
```

---

## AB-014: Long-thread pagination, history and restart compatibility

**Status:** MONITOR / RESEARCHING
**Priority:** P2

Keep durable ADS Codex threads reliable as history/pagination APIs evolve.

```text
verify exact local thread/read, turns/list, items/list support
avoid expensive full-history bootstrap when lazy detail is enough
capability-probe version-sensitive APIs
preserve durable thread identity across restarts
reconstruct terminal/pending state without resuming when possible
monitor upstream protocol-drift and pagination issues
```

---

## AB-015: Multi-agent / subagent supervision and lineage

**Status:** MONITOR / RESEARCHING
**Priority:** P2

Prepare for subagents only when real use justifies it:

```text
parent/child thread lineage
agent nickname/role
root-vs-child authority constraints
child progress aggregation
approval routing
hierarchical viewer presentation
handoff/recovery of a task tree
```

Do not prematurely design a complex multi-agent UI without exact local lifecycle evidence.

---

## AB-016: App Server daemon / local-control transport as a future simplification

**Status:** MONITOR
**Priority:** P3

Track official daemon/local-control transports as possible simplifications of Codexless-owned App Server lifecycle management. Adopt only if stability, Windows security semantics, authority preservation, recovery and compatibility are stronger than the current accepted path.

---

## AB-017: Broader host-capability taxonomy beyond workspaces

**Status:** RESEARCHING / FIRST RUNTIME-MAINTENANCE AUTHORITY CLASS RESOLVED / BROADER TAXONOMY OPEN
**Priority:** P2

Define explicit authority classes for host operations that are not naturally ordinary project workspaces:

```text
Codexless runtime maintenance
process lifecycle
Windows services
Windows registry
credential-store mediated operations
machine-level configuration
other non-workspace host resources
```

Each class should be semantic, narrow, server-owned and independently permissioned. Research 116 deliberately closed workspace/project authority without claiming universal host authority. AB-002 is the first concrete instance.

Checkpoint 366 / Validation 124 close that first concrete instance: installed Codexless publication/restart/verify/rollback is now a live-qualified semantic authority class. This does not close AB-017. The broader taxonomy for Windows services, registry, credential-mediated operations, machine configuration and other non-workspace host resources remains research work and must continue to require independent semantic authority rather than inheriting runtime-maintenance privileges.

Validations 062-063 reinforce this separation. Two exact runtime publications were safe to perform only through guarded host PowerShell because ordinary workspace authority intentionally does not grant `%LOCALAPPDATA%` installation authority. The successful one-time bootstraps should inform the eventual semantic runtime-maintenance capability, not justify broad ordinary host access.

---

## AB-018: Public Codexless and OpenAI Codex upstream reconciliation

**Status:** RESEARCHING
**Priority:** P1

Complete Research 113 before major new local divergence.

Continually classify:

```text
what upstream now provides
what ADS already solves
what custom ADS mechanism remains necessary
what can be simplified/replaced
what should remain deliberately narrower than upstream
what version-sensitive assumptions need probes
what should merely be monitored
```

Active clusters include lifecycle kernels, native progress, steering, Browser elicitation, approvals/Guardian, history, multi-agent behavior, daemon transports and MCP Apps/resource lifecycle.

Primary index: `docs/research/CODEX_UPSTREAM_ADS_COMPARISON_MATRIX.md`.

---

## AB-019: Exact local Codex capability/version probes

**Status:** RESEARCHING
**Priority:** P1

Do not adopt an upstream-main feature merely because it exists in current source/documentation.

For every version-sensitive mechanism considered for live use:

```text
verify the exact installed Codex version
probe the concrete method/schema on that version
preserve positive and negative evidence
fail closed on runtime drift
prefer capability/contract probes over version-name inference
```

Especially relevant to item/history APIs, steer/queue, reviewer settings, subscription semantics and daemon/local-control features.

---

## AB-020: Private local-runtime preservation and publication workflow refinement

**Status:** RESOLVED / LIVE ABOVE-32-KIB PUSH QUALIFIED
**Priority:** P2

Keep `autonomous-data-science-system-local-runtime` useful as reviewed non-secret implementation evidence without creating a second ADS development authority.

Potential refinements:

```text
deterministic candidate -> private-runtime synchronization
manifest/coherence validation before publication
secret/sensitivity gates as runtime evidence evolves
clear mapping of live installed bytes to preserved candidate bytes
bounded semantic publication of runtime evidence
recovery on another machine without copying secrets
```

Checkpoint 319 work exposed one concrete scaling edge in the current private semantic-Git integrity gate. The integrity policy enumerates tracked paths through the normal 32 KiB command-output envelope. Committing several redundant candidate copies of already-installed regression scripts would have pushed that enumeration beyond the envelope and made the private push fail closed. The publication work therefore kept those supplemental staging copies under protected `.tmp/` while committing only durable candidate source/tests and documentation; the resulting private push passed.

Checkpoint 323 converted that anticipated edge into a direct live reproduction. After adding one focused renderer test file, the NUL-delimited `git ls-files --cached -z` output measured 32,841 bytes for 412 paths. The first normal private semantic push failed closed with `RUNTIME_BOOTSTRAP_INTEGRITY_UNCERTAIN: tracked-file enumeration was truncated`. No integrity policy was weakened or bypassed. The two focused tests were consolidated into an existing tracked candidate test file, preserving 51/51 coverage while reducing enumeration to 32,753 bytes / 411 paths, after which the normal semantic push passed with `RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS` and `postflightOk=true`.

Checkpoint 330 / Validation 088 now qualify the permanent bounded-enumeration correction. Instead of transporting the complete tracked-file list through the generic 32 KiB response envelope, the candidate launches one fixed server-owned read-only Node scanner inside the already-authorized sandbox. The scanner internally permits a separately bounded 4 MiB tracked-path enumeration and at most 20,000 tracked files, preserves the existing containment/regular-file/2 MiB-per-file/50 MiB-total/binary/secret gates, and returns only compact JSON. Malformed/truncated scanner receipts or scanner failure remain fail-closed. A regression deliberately creates a tracked-path set above 32 KiB and passes.

The candidate is privately preserved at `7e70bd05e4da76ff1ad260b2b1cbdc5c1d65a3fb`. Checkpoint 332 / Validation 090 now preserve successful host publication and independent installed-hash verification at `3b2ddbbe00339045b81044bb3e1e39c314a461a7e0f8e4e608b79b4b0f37de02`. Checkpoint 333 / Validation 091 close this concrete defect. After restart, one real private semantic push succeeded with 412 tracked files / 32,813 tracked-path bytes, above the old generic ceiling, and the complete Office candidate was then pushed successfully at 503 tracked files / 40,013 tracked-path bytes. Both pushes reported `RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS` and `postflightOk=true`. Reopen only if the bounded 4 MiB / 20,000-file internal scanner limits themselves become material or a new integrity-transport failure appears.

Primary contract: `docs/local_execution/LOCAL_RUNTIME_REPOSITORY.md`.

---

## AB-021: Privacy/consent behavior for developer-MCP arguments

**Status:** OPEN / OBSERVATION TO CHARACTERIZE
**Priority:** P2

During `chatgpt-16`, ChatGPT displayed a consent card before sending values classified as contact information to the ADS developer MCP. The card was generated from proposed tool arguments, not evidence that Codexless had independently discovered those values.

Future work:

```text
understand which argument classes trigger ChatGPT privacy consent
avoid unnecessarily including unrelated personal data in diagnostic searches
prefer narrow searches using only the minimum literal needed
record whether consent behavior differs across desktop/mobile clients
ensure Codexless design never depends on bypassing platform privacy interlocks
```

This is a host/privacy integration observation, not a reason to weaken the consent layer.

---

## AB-022: Reconstruction-to-operational-authority routing and required-read enforcement

**Status:** OPEN / REPRODUCED ARCHITECTURE GAP
**Priority:** P0

A concrete failure was reproduced at the start of `chatgpt-17` after an unexpected context-limit termination. The new session correctly performed the canonical public bootstrap reads and reconstructed Checkpoint 283 / Research 117, but it did not read `docs/local_execution/OPERATIONS.md` before giving the next operational restart instructions. This happened even though:

```text
CURRENT_STATE.md
    listed docs/local_execution/OPERATIONS.md in Minimum reading for continuation

Checkpoint 283
    said to restart Codexless using the controlled runbook

Validation 042
    required controlled restart/reconnect/schema refresh after publication

OPERATIONS.md
    was the authoritative owner of the exact full restart order
```

The result was a wrong instruction from the collaborator: stop Codexless first and then stop the tunnel. The repository-authoritative full controlled restart order is the reverse at the beginning: stop the tunnel first, keep its Git Bash shell open, then stop/restart Codexless, verify the new local surface, restart/verify the tunnel, and only then refresh ChatGPT. The project owner noticed the mismatch and forced a direct runbook check before acting on the incorrect order.

This must be treated as more than an isolated collaborator mistake. The repository contained the correct knowledge and even linked it from the live state, but the reconstruction architecture did not make consumption of the task-relevant operational authority sufficiently reliable before action guidance was produced.

Research targets:

```text
make active next-action routing resolve the governing operational/specification authority, not only the current checkpoint/research narrative

separate "minimum reading exists" from "required authority was actually consumed before an action is recommended"

consider typed/machine-readable next-action prerequisites or governing-procedure references where an exact procedure owns execution order

consider a lightweight reconstruction/action preflight that can prove task-relevant required reads were resolved before operational mutation guidance

avoid solving the problem by making every new chat read the entire repository or an ever-growing static list

preserve the distinction between information-architecture failure, routing failure, and collaborator non-compliance, while designing the system so high-consequence omissions are harder to make

add a regression/validation scenario based on this exact restart-order miss once a stronger routing mechanism is designed
```

Acceptance direction:

```text
new session reconstructs current boundary
    -> active next action is identified
    -> governing execution authority is resolved automatically or fail-visibly
    -> collaborator reads that authority before giving exact operational steps
    -> action order is reproduced from the authority rather than chat memory/inference
```

This issue is directly relevant to continuity, knowledge routing, operational safety and the wider ADS goal that the repository should make correct continuation behavior recoverable across chats rather than merely store the answer somewhere discoverable.

---

## AB-023: Open Architecture Backlog vs Open Questions discoverability and usage audit

**Status:** OPEN / SELF-AUDIT REQUESTED
**Priority:** P1

The project owner explicitly requested a follow-up audit of whether `docs/OPEN_ARCHITECTURE_BACKLOG.md` itself is sufficiently clear, easy to discover and reliably used, including whether its role is clearly distinguished from `docs/OPEN_QUESTIONS.md` and other current-state/research surfaces.

Current repository inspection already shows that the distinction is documented in several places:

```text
docs/README.md
    fast-routes explicit deferred architecture ideas and side tracks to OPEN_ARCHITECTURE_BACKLOG
    separately routes important unresolved questions to OPEN_QUESTIONS

OPEN_ARCHITECTURE_BACKLOG.md
    defines itself as planning/retrieval for future architecture ideas, known gaps,
    deferred side tracks and continuation obligations
    explicitly says it is not a second CURRENT_STATE or replacement for OPEN_QUESTIONS/research/evidence

OPEN_QUESTIONS.md
    defines itself as the canonical register of important unresolved project questions

CURRENT_STATE.md and KNOWLEDGE_MAP.md
    already link the architecture backlog in the active development-governance route
```

So the current concern is not simply that the backlog has no documentation. The `chatgpt-17` restart-order miss exposed a more general risk: knowledge can be clearly documented and linked yet still fail to influence the collaborator at the moment it matters. The backlog/open-question audit should therefore examine both **human clarity** and **operational routing behavior**.

Audit targets:

```text
is the backlog purpose obvious from the mandatory bootstrap path without prior memory?

is the difference between OPEN_ARCHITECTURE_BACKLOG and OPEN_QUESTIONS sufficiently crisp for future collaborators deciding where to preserve a new issue?

are "remember this / investigate later / architecture gap / deferred side track" triggers reliably routed to the backlog during normal work and chat rotation?

are important backlog items surfaced when they become relevant to an active stage, or can they remain technically discoverable but practically invisible?

should CURRENT_STATE, KNOWLEDGE_MAP, CONTINUITY or DEVELOPMENT_METHOD carry a stronger typed/backlog-routing obligation without duplicating the backlog contents?

can lightweight validation or reconstruction checks detect when an explicitly relevant backlog obligation was skipped?
```

This backlog item deliberately preserves the recursive concern itself: even the mechanism used to remember future architecture work must be evaluated for whether future sessions are reliably led to it, rather than assuming that a well-written Markdown file is sufficient.

The concrete `chatgpt-17` wording that triggered this audit also exposed a smaller manifestation of the same problem: after publication, the collaborator suggested to "refresh the connector/app if that surface supports it" instead of immediately following the already-preserved exact ChatGPT developer-MCP refresh procedure in `docs/local_execution/OPERATIONS.md`. The repository already records the observed path (`Settings -> Plug-ins -> ADS Codexless Local Bridge -> Vernieuwen`) and the invariant that refresh occurs only after Codexless and tunnel readiness are healthy. This should be included in the eventual routing regression together with the incorrect restart order: task-relevant operational knowledge existed, but generic fallback wording was produced because the governing runbook had not been consumed.

---

## AB-024: High-recall new-session reconstruction and hierarchical knowledge traversal

**Status:** OPEN / ARCHITECTURE AUDIT REQUESTED
**Priority:** P0

The project owner challenged the current continuation framing around "minimum reading." The objective of a fresh persistent ADS conversation should not be to consume the smallest possible amount of repository knowledge that permits the next action. It should be to reconstruct the **best practically achievable understanding of the whole project**, including current state, governing authority, important historical context, parent workstreams, unresolved obligations, and task-relevant deep evidence.

The existing architecture already contains strong ingredients: `README.md` as the stable entry point, `docs/README.md` as the structural guide, `CURRENT_STATE.md` / `current_routing.json` as live-state owners, `KNOWLEDGE_MAP.md` as the exhaustive semantic routing layer, `CONTINUITY.md` as the reconstruction procedure, and specialized foundations/research/specifications/checkpoints/ledgers. Research 103 and 104 explicitly strengthened repository-wide discoverability and exhaustive routing. Foundation 014 also anticipated stronger indexes, semantic retrieval, dependency graphs and machine-checkable metadata if observed retrieval failures eventually justified them.

The `chatgpt-17` restart-order miss now provides new evidence that **having comprehensive knowledge stored and routed is not equivalent to having it activated in the new collaborator's working context**. The current long "Minimum reading for continuation" list also risks becoming a static enumeration whose existence does not prove that the listed knowledge was actually traversed or understood.

The architecture audit should therefore distinguish two goals that must not be conflated:

```text
maximum repository bytes read
    !=
maximum useful project understanding
```

Literal exhaustive reading of every repository file on every new chat may waste context on implementation detail, duplicate historical states, stale evidence, generated artifacts and low-relevance material. It can also make authority distinctions harder rather than easier. The desired target is instead **high-recall, authority-aware, hierarchical reconstruction** that seeks the maximum useful understanding while preserving context quality.

Candidate reconstruction shape to research:

```text
stable project entry / authority
    -> structural repository map
    -> current live state + machine route
    -> active workstream and its complete parent/resume chain
    -> governing canonical procedures/specifications for the next boundary
    -> semantic Knowledge Map neighborhood around the active work
    -> current open questions / architecture backlog / continuation obligations
    -> relevant foundations and accepted decisions
    -> relevant research, validations and historical checkpoints
    -> specialized ledgers/manifests/private complement where applicable
    -> coverage/reconstruction receipt showing what was actually traversed
```

Research targets:

```text
replace "bare minimum" as the implicit optimization target with maximum useful/high-recall understanding

determine whether a cold-start orientation pass should inspect repository-wide metadata/index coverage before selective deep reads

define which knowledge classes should always be activated in a new persistent conversation and which should remain retrievable on demand

make authority, chronology, supersession and current-vs-historical status explicit during reconstruction

investigate a machine-readable traversal plan or generated reconstruction manifest rather than relying on one manually growing list

consider whether the observed retrieval failure now justifies stronger dependency/graph/index machinery previously deferred by Foundation 014 and Research 104

measure reconstruction completeness and missed-governing-artifact failures rather than only whether the current checkpoint was found

preserve context-window efficiency without using efficiency as a reason to omit important project knowledge
```

A likely professional target is a layered process where the system first obtains broad repository awareness, then expands deterministically into the active and semantically adjacent knowledge, and finally reads exact governing evidence before giving operational or architectural guidance. This is a research direction, not yet an accepted replacement for the current continuation procedure.

Primary context: Foundation 014, Research 103, Research 104, `docs/CONTINUITY.md`, `docs/KNOWLEDGE_MAP.md`, and AB-022.

---

## AB-025: Nested workstream graph, active route stack, and deterministic resume semantics

**Status:** OPEN / ARCHITECTURE AUDIT REQUESTED
**Priority:** P1

ADS frequently leaves the main development route for a bounded investigation or implementation branch, and that side route can itself open another nested route. The current repository preserves many of these relationships in prose, checkpoints and continuation obligations, but the active machine route remains largely flat. `docs/current_routing.json`, for example, identifies one `current_boundary` but does not encode the parent workstream, nested child route, return condition or exact resume target.

The current project state demonstrates the need clearly. A simplified conceptual route is:

```text
Source Vault / Source Universe continuation
    PAUSED while broader Level-2 research is active
    |
    -> Research 113: Codex / Codexless upstream ecosystem research
         |
         -> Research 117: reuse-first multimodal document architecture
              |
              -> E117-1: direct ChatGPT MCP image visibility
                   -> current codex.image_read publication / host test

separate paused sibling/related route:
    v17 semantic Codex task viewer
```

When the innermost work closes, ADS needs to know which parent boundary becomes active again. When Research 117 closes, the wider Research 113 route may still have unfinished obligations. When that Level-2 research closes, the preserved Source Vault ingestion route should resume at its exact stored action rather than requiring a future collaborator to reconstruct the return path from scattered prose.

A pure chronological timeline is insufficient because chronology answers "what happened when," while continuation requires "what is active, what interrupted what, what depends on what, and where do we return?" A pure tree may also be insufficient because some workstreams can depend on multiple other branches. The audit should therefore compare a simple tree against a more general **workstream DAG plus one explicit active stack/breadcrumb**.

Candidate node semantics to research:

```text
workstream / route id
human title
status: ACTIVE / PAUSED / BLOCKED / READY / CLOSED
parent route(s)
child route(s)
why opened
opened-from boundary
blocking/dependency relation
current boundary
completion / return condition
exact resume target after closure
governing evidence
related backlog/open-question ids
historical checkpoints / commits
```

Candidate live representation:

```text
MAIN ROUTE
    -> parent workstream
        -> child workstream
            -> current leaf

ACTIVE STACK
    [main, parent, child, leaf]

ON LEAF CLOSE
    resolve declared return condition
    -> activate parent or next dependency
    -> never guess the resume point from chat memory
```

Research targets:

```text
make nested side missions first-class rather than prose-only continuation knowledge

separate chronological history from dependency/resumption structure

ensure every PAUSED route has a reason, blocker/return condition and exact resume target

ensure opening a nested route records the parent edge automatically or through a required development-method step

consider extending current_routing.json versus introducing a separate machine-readable workstream-routing artifact with a generated human view

validate that no active/paused branch becomes orphaned and that completed child routes lead deterministically to the next eligible parent/peer route

integrate backlog/open-question obligations without turning either file into the live routing graph

preserve Git/checkpoints as historical provenance while giving current continuation a separate explicit control-flow representation
```

This should also improve new-session reconstruction: instead of only learning the current leaf, a collaborator can reconstruct the entire active breadcrumb and understand why the project is temporarily doing the current work, what broader objective it serves, and what comes next when it closes.

Primary context: `docs/current_routing.json`, `docs/CURRENT_STATE.md`, `docs/CONTINUITY.md`, Foundation 014, Research 104, AB-022, AB-024, and CO-003.

---

## AB-026: Knowledge Map topic saturation, hierarchical decomposition, and retrieval usability

**Status:** OPEN / ARCHITECTURE AUDIT REQUESTED
**Priority:** P1

The project owner suspects that the current `docs/KNOWLEDGE_MAP.md` subject taxonomy may itself be approaching a retrieval-scaling failure even though its mechanical coverage contract is healthy. The concern is that too many artifacts can accumulate under one broad subject. If one topic eventually routes dozens or hundreds of files, a future collaborator may technically discover the correct section while still failing to inspect enough of the material inside that section to recover the important knowledge.

Current repository evidence supports treating this as a real audit target rather than only a hypothetical concern. Research 103 already identified discoverability and routing quality as the main scaling pressure. Research 104 deliberately introduced exhaustive subject routing and warned against giant tables, hundreds of visible checkpoint links, and absorption of specialized indexes into the global map. The current Knowledge Map now contains visibly uneven fan-out: some subjects remain compact, while broad subjects such as `development-governance` route a large set of foundations, specifications, research records, validations, ledgers, local-execution documents, backlog material and checkpoints. The map can therefore satisfy exhaustive coverage while still becoming too coarse at the point of use.

The key distinction to preserve is:

```text
coverage completeness
    !=
retrieval usability

"artifact is assigned to a topic"
    !=
"a collaborator can efficiently identify and consume the important artifacts inside that topic"
```

The audit should investigate whether the global topic layer needs another level of semantic structure rather than continuing to append direct file paths to broad subjects indefinitely.

Candidate directions to compare include:

```text
hierarchical topics / subtopics
    broad domain -> narrower semantic clusters -> artifacts

topic-local indexes
    one global subject points to a specialized sub-index when fan-out becomes large

core vs extended evidence
    small governing/entry set first, deeper supporting evidence separately reachable

artifact-role grouping inside a subject
    canonical / foundation / specification / research / validation / historical evidence

priority or authority-aware routing
    distinguish "read first" from "supporting / historical / optional deep evidence"

machine-generated or validated fan-out metrics
    warn when one topic becomes semantically overloaded

cross-topic graph edges
    preserve multiple genuine memberships without forcing every relationship into one flat list
```

Research targets:

```text
audit every current Knowledge Map subject for semantic coherence, direct-artifact count, overlap, authority mix and likely retrieval burden

identify sections that are broad because the domain is genuinely broad versus sections that have become catch-all buckets

preserve exhaustive coverage while reducing the number of direct artifacts a collaborator must scan before finding the governing subset

consider stable subtopic IDs and validator support rather than informal headings that can drift

consider whether specialized indexes should be introduced earlier, not only after a whole domain becomes very large

ensure decomposition does not create a second failure where knowledge becomes fragmented across too many tiny categories

define practical saturation signals or thresholds from observed use rather than choosing arbitrary limits

test reconstruction scenarios against the redesigned map: can a fresh collaborator reach the right governing evidence without already knowing filenames or document numbers?
```

This concern is closely connected to AB-024. High-recall reconstruction cannot rely on a Knowledge Map that is exhaustive only in the set-theoretic sense; its semantic neighborhoods must remain traversable enough that broad project understanding can actually be activated. It is also connected to Foundation 014's distinction between durability and discoverability: a file may be perfectly preserved and formally routed while still being practically hidden inside an overloaded category.

Primary context: `docs/KNOWLEDGE_MAP.md`, Foundation 014, Research 064, Research 103, Research 104, AB-022, and AB-024.

---

## AB-027: Deferred architecture risks, known weaknesses, and evolution-trigger register

**Status:** OPEN / ARCHITECTURE AUDIT REQUESTED
**Priority:** P1

The project owner identified a recurring pattern across ADS development: a new problem is observed in live use, the collaborator investigates it, and repository research then reveals that the same weakness, possible future failure mode, or escalation condition had already been anticipated earlier. The prior work often explicitly said some version of:

```text
this may become a problem later
this is a known limitation
we deliberately accept this simpler architecture for now
revisit this if X happens
stronger machinery is not justified yet
this future mechanism should be introduced only when measured pressure appears
```

The knowledge is therefore durable, but these **latent architecture warnings and reopen conditions are scattered across foundations, decisions, research records, specifications and checkpoints**. They are often rediscovered only after the project owner independently notices the concrete symptom. That is weaker than the intended repository-memory architecture.

This pattern is already visible in current evidence. Foundation 014 explicitly deferred stronger preservation infrastructure while naming future triggers such as unreliable Knowledge Map maintenance, frequent failure to discover existing knowledge, dependency networks too large for prose, expensive reconciliation, and multi-contributor coordination pressure. Research 064 said stronger knowledge machinery should wait for a real discoverability or synchronization failure. Research 103 later recorded that such discoverability pressure had arrived. Research 104 again deferred a heavier semantic/vector/dependency system until concrete retrieval failures remained after the lighter architecture was used. D-024 similarly preserved future upgrades and trigger conditions. Other decisions preserve their own escalation conditions, for example D-032 for stronger workflow durability/runtime machinery and D-034 for collaboration mechanization.

The architectural issue is therefore not lack of foresight. It is that foresight does not yet have a sufficiently reliable **promotion and monitoring surface**.

The audit should determine whether `docs/OPEN_ARCHITECTURE_BACKLOG.md` should become the canonical retrieval index for this class of knowledge, or whether a distinct but tightly integrated architecture-evolution register is justified. Do not create another competing repository-memory layer merely for naming convenience. The selected design should have one clear owner and link back to the detailed evidence rather than copying it.

Candidate entry semantics to research:

```text
stable issue / trigger id
short weakness or deferred-capability title
current accepted architecture / workaround
known limitation or risk
why the stronger alternative was deferred
observable trigger(s) that should cause reconsideration
current trigger state: NOT_OBSERVED / PARTIAL / OBSERVED / SUPERSEDED
source decisions / foundations / research / validations
related active backlog / open-question / workstream ids
last reconciliation date
result when revisited: KEEP / RESEARCH / IMPLEMENT / CLOSE
```

Research targets:

```text
perform a retrospective repository-wide extraction of explicitly known limitations, deferred upgrades, reopen conditions and future escalation triggers

identify items that are currently buried only inside long-form research or decision rationale and are not represented in the architecture backlog

separate ordinary speculative ideas from explicit known weaknesses and evidence-backed future triggers

make trigger conditions discoverable before a failure is rediscovered conversationally

at meaningful reconciliation boundaries, evaluate whether any stored trigger has become true or materially closer to true

when a live problem is reported, check the trigger/weakness register early as part of diagnosis rather than only after broad ad hoc searching

link each concise register item to authoritative detailed evidence so the index does not become another source of substantive truth

preserve historical cases where the project correctly anticipated a limitation and later observed its trigger, because these are valuable evidence about architecture evolution

integrate with AB-023/024/026 so backlog discoverability, new-session reconstruction and Knowledge Map routing all surface relevant known weaknesses at the right time
```

A useful end state would let a future collaborator answer immediately:

```text
What weaknesses of the current architecture do we already know about?
What did we deliberately postpone?
Why did we postpone it?
What event would justify reopening it?
Have any of those trigger conditions now occurred?
Where is the detailed reasoning/evidence?
```

This is directly aligned with Foundation 014's principle that the preservation architecture itself must remain empirical. ADS should not merely preserve past architectural decisions; it should preserve the **conditions under which those decisions were intentionally provisional** and make those conditions easy to monitor.

Checkpoint 328 / Validation 086 add one concrete hardening trigger to this register. The isolated cached-artifact renderer passes functionally, but Node emits its standard warning that `--allow-addons` can invalidate the permission model because the maintained `@napi-rs/canvas` native addon is enabled. The current accepted design treats that pinned addon as trusted functionality, not as evidence that Node's permission model provides an OS-grade security boundary. Reopen stronger renderer isolation if addon/runtime trust changes, untrusted native code enters the path, the warning becomes operationally material, or a supported OS-level sandbox can replace this caveat without disproportionate complexity.

Primary context: Foundation 014, D-024, D-032, D-034, Research 064, Research 103, Research 104, AB-023, AB-024, AB-026, Research 120, and Validation 086.

---

## AB-028: Post-Browser Astra independent architecture review after the GPT-5.6 Sol baseline

**Status:** CLOSED / PHASE 2 COMPLETE / RESEARCH 118
**Priority:** P1

Closure 2026-09-05: Astra completed the independent Phase 1 review before private Sol exposure, then completed Phase 2 against the frozen Sol baseline. Research 118 / Validation 065 / Checkpoint 306 preserve that reconciliation. The reviewed private source-bound PDF evidence candidate is preserved at `a5025c2071077f719dcc59c7dfd729ee59ec34eb`. Direct existing-tab Browser mutation remains blocked and direct new-tab mutation remains deferred as lifecycle-unproven. Research 119 / Checkpoint 308 subsequently corrected the governing local-file objective: the Phase 2 semantic-worker recommendation is optional delegated-analysis research, not the direct ChatGPT file-access solution. AB-028 stays closed; the active direct-access work remains under AB-005 / Research 117/119.

The project owner explicitly wants the newly available Astra model treated as a material architecture-review opportunity rather than a routine model substitution. The existing GPT-5.6 Sol Research 117 Browser thread has now completed its bounded baseline: maintained Browser/Chrome discovery was qualified, but live Browser publication correctly stopped because direct `mcpServer/tool/call` has no proven supported claimed-tab cleanup equivalent to a genuine Codex turn. That blocked result is preserved as Validation 064 / Checkpoint 305 and private local-runtime commit `e45a5de7ddae7f8158445b4b71d9c5f70cab8a2c`.

The next action is to open a **new Codex thread with Astra**. The Astra task should not begin as a narrow request to "improve the Browser fix" and should not be over-anchored on the existing implementation. Its first pass should independently review the broader current integration architecture, actively search for supported solutions to the Browser lifecycle blocker, and ask what it would design or simplify from the present requirements and evidence.

Primary review scope:

```text
ChatGPT <-> Codexless <-> Codex App Server <-> Codex Desktop

active-turn writer ownership and cooperative handoff
approval supervision and native auto_review
Call Codex consent vs lower-layer reviewer policy
Rich Task Cards and task/thread lifecycle
thread persistence, rebind, archive/unarchive and cross-client continuity
runtime publication / maintenance authority
Browser / Chrome compatibility and file-upload fallback
model-free execution and semantic tool boundaries
local document / image / PDF handoff architecture
host materialization limits and fallback design
upstream mechanisms that may replace custom Codexless machinery
security, authority, fail-closed behavior and unnecessary complexity
```

Desired comparison sequence:

```text
1. GPT-5.6 Sol finished the existing Browser thread and qualified current-plugin discovery.
2. ChatGPT independently reviewed the code/tests and confirmed the maintained genuine-turn cleanup contract.
3. The baseline stopped safely before publication because direct-call claimed-tab cleanup is unsupported/unproven.
4. Commit/push/checkpoint/validate that blocked baseline as evidence rather than forcing a workaround.
5. Start a fresh Astra Codex thread.
6. Give Astra repository authority/evidence and requirements, but ask for an independent architecture and solution search before treating the GPT-5.6 Sol implementation as the assumed answer.
7. Then let Astra inspect and challenge the preserved GPT-5.6 Sol baseline and its blocker.
8. Compare supported alternatives, simplifications and upstream mechanisms against that evidence-backed baseline.
9. Change ADS only where evidence supports an improvement; newer-model suggestions are not accepted merely because the model is newer.
```

Questions Astra should explicitly answer include:

```text
Is the Browser fallback architecture itself the right solution?
Did the preserved baseline introduce avoidable complexity?
Are there newer/native Codex or OpenAI mechanisms ADS missed?
Are any Skills/Browser/App Server assumptions obsolete?
Can custom compatibility layers now be deleted or narrowed?
Is there a supported Browser execution primitive with a genuine cleanup lifecycle?
Can existing-tab claiming be avoided entirely?
Is there a more direct solution to local-file/PDF handoff?
Are approval, writer-ownership, task-card or runtime-publication boundaries incomplete?
What would Astra design if starting from current ADS requirements rather than implementation history?
```

Astra should actively search for solutions rather than merely review the blocker. Candidate outcomes include a supported genuine App Server turn/lifecycle, another maintained Browser API path, an explicit release/unclaim contract, a new-tab/deliverable architecture, a different whole-PDF handoff, or a well-evidenced conclusion that no supported route currently exists.

This item is also an architecture-evolution trigger under AB-027: a materially stronger/new model can justify a deliberate independent re-evaluation of previously accepted custom architecture, especially in a rapidly changing upstream ecosystem. The trigger does **not** mean rewriting working systems by default. The professional comparison is an evidence-backed challenger review against a fully tested baseline.

Related work: Research 113, Research 117, AB-003, AB-004, AB-005, AB-007, AB-012, AB-013, AB-017, AB-018, AB-019, AB-020, and AB-027.
---

## AB-029: Native GitHub connector capability parity inside Codexless Runtime Bridge

**Status:** ACTIVE / RESEARCH 123
**Priority:** P1

The current ChatGPT host does not reliably allow the custom developer MCP and the native GitHub connector to execute in the same conversation. Validation 034 preserved the repeated coexistence failure, and Validation 128 rechecked the boundary from normal mobile web: the Codexless developer-MCP surface remained callable and `codex.account_preflight` passed while the GitHub connector was not projected in that conversation.

Two fresh GitHub-only qualifications now provide a concrete parity target. Both projected the same 89 GitHub actions. The first live-qualified a broad remote development workflow including direct file commits, raw Git blob/tree/commit/ref operations, PR/review/thread collaboration, issue lifecycle operations, and Actions/CI inspection. The second explicitly challenged negative conclusions and discovered no additional action or equivalent route for the previously absent capability families.

The target is practical capability parity, not a weaker read-only approximation. Codexless Runtime Bridge should preserve the currently observed GitHub connector's information fidelity, authorization/scope semantics, pagination and continuation behavior, structured failure distinctions, file and raw Git mutations, PR/review collaboration, issue lifecycle operations, Actions inspection/reruns, and exposed merge authority. `Bounded` should describe the authority shape and credential safety, not intentionally reduce useful GitHub power.

Negative connector findings remain conservative `NOT_OBSERVED_IN_THIS_PROJECTION` results rather than permanent global impossibilities. Features not observed in the current native connector may later be added as ADS supersets, but they are not required for first parity closure.

Research 123 owns the implementation and qualification route. Research 113 is paused, not completed. Source Vault remains paused. The project owner's separately planned next stage comes after this parity work unless explicitly redirected.

Checkpoint 372 design work maps the 89-action baseline into the planned `github.*` Runtime Bridge namespace and selects a dedicated GitHub App user-token/device-flow architecture with installation-derived repository scope, internal REST/GraphQL transport, server-owned secret storage, structured pagination/errors and mutation guards. Exact remote parity remains 0/89 because implementation has not started. The public qualification had not preserved complete native schemas, so it opened the discovery-only batched schema-capture gate.

Validation 130 / Checkpoint 373 preserve the first exact fresh inventory from that gate. The host again projected 89 actions and invoked none, but comparison exposed one Checkpoint 372 exact-name reconstruction error: the fresh projection contains `GitHub.download_user_content`, while the reconstructed inventory had `GitHub.add_issue_comment`; the actual projected issue-comment creation name is `GitHub.add_comment_to_issue`. This is classified as a reconstruction defect rather than connector drift because Validation 128 never publicly froze all exact names. The schema-version-2 inventory now preserves the exact fresh projected order.

Validation 131 / Checkpoint 374 preserve discovery-only schema Batch 1 for projected actions 1-15. All fifteen expose input object contracts, but all fifteen project return type `any`; separate action-title metadata and structured error schemas are absent. Several conditional rules appear only descriptively rather than structurally. The specialized schema-capture artifact is mechanically validated at `15 / 89`. Continue Batch 2 in the same fixed GitHub-only conversation before implementation; final Research 123 reconciliation must explicitly decide whether exact normalized output shapes require additional live-result evidence beyond host schema discovery.

Validation 132 / Checkpoint 375 advance the same fixed discovery projection to `30 / 89`. Batch 2 confirms action-specific pagination, a genericized `create_tree.tree_elements` inner schema, a host-restricted `download_user_content` URL contract, workflow-artifact reusable file-reference semantics, and a bounded GET-only generic `fetch` rather than arbitrary HTTP. `fetch_issue.repository_url` explicitly names GitHub Enterprise Server custom hostnames and GHE.com API hosts, so final Research 123 architecture must reconcile endpoint-specific Enterprise selector support rather than assuming github.com-only scope globally. Batch 3 is next; implementation remains unstarted.

Validation 133 / Checkpoint 376 advance the same discovery projection to `45 / 89`. Batch 3 adds explicit valid-empty (`patch=null`) versus unresolved-resource (404) semantics for `fetch_pr_file_patch` plus a documented no-retry-other-paths rule, further differentiates all-pages, first-page-only, latest-attempt-only, and page/per_page pagination contracts, and confirms a zero-argument profile lookup plus repository-selector XOR. Collaborator-permission output values remain hidden behind `any`, so exact result enums remain a later parity-evidence gap. Batch 4 is next; implementation remains unstarted.

Validation 134 / Checkpoint 377 advance the same fixed discovery projection to `60 / 89`. Batch 4 captures installation/account discovery and installation-scoped repository listing, further differentiates final-limit/internal, all-pages, until-limit-or-exhaustion, zero-based-offset, and unspecified pagination contracts, and records four zero-argument identity/account/org actions. `lock_issue_conversation.lock_reason` is a real four-value enum while recent-PR state and repository affiliation examples remain untyped strings. Batch 5 is next; implementation remains unstarted.

Validation 135 / Checkpoint 378 advance the same fixed discovery projection to `75 / 89`. Batch 5 captures exact merge-method and expected-head concurrency behavior, reviewer-array ambiguity, top-level-only inline review replies, GitHub Actions write permission for rerun mutations, final-limit code search with valid-empty empty query, and opaque-cursor branch search. Thirteen of fifteen Batch 5 actions are mutating. Fourteen native action contracts remain in the final discovery batch; implementation remains unstarted.

Validation 136 / Checkpoint 379 complete the six-batch native schema discovery at `89 / 89` with zero GitHub action invocations. Batch 6 adds qualifier-only commit-search rejection plus the recent-commit empty-query exception, opaque next-token and 1-based-page installed-repository search, issue-search selector-family exclusivity, sequential same-path file-write constraints with named `content_sha`, issue replacement-set semantics with no milestone-clear path, and branch-only `update_ref(force=false)` semantics. The machine capture remains explicitly pending final same-conversation reconciliation; implementation is still unstarted.

Validation 137 / Checkpoint 380 close that reconciliation. All 89 host-visible request contracts are captured, but exact native-wrapper wire parity remains incomplete because every result/error schema is hidden and `create_tree` retains nested input genericization. The project therefore rejects an indiscriminate 89-action live replay: practical action mapping is ready, authoritative GitHub platform contract mapping becomes the primary evidence source, and targeted native wrapper qualifications are reserved for material behaviors that survive that mapping. The independent G0 GitHub App/device-flow/auth/REST-GraphQL kernel is ready to begin; no action-specific parity publication is implied.

Validation 138 / Checkpoint 381 freeze the first authoritative GitHub platform pass. GitHub App user-access-token/device-flow auth, installation/user intersection scope, eight-hour/six-month token rotation, github.com REST `2026-03-10`, required User-Agent, create-tree nested entry semantics, create-PR head/base requirements and same-path Contents serialization are now source-backed. G0 implementation may begin without live credentials; the protected Windows token-store mechanism is the next local design choice.
Validation 139 / Checkpoint 382 implement and privately preserve the first G0 auth/transport candidate at `3c5f3688ec578c0817953890dc69ecb7ce679153`. The focused 12/12 suite uses fake HTTP/keyring only; the candidate has not touched live GitHub or the OS credential store. The conservative private secret scanner initially rejected source syntax, was not weakened, and passed after scanner-safe code/fixture correction. Concrete Windows keyring import + synthetic credential round-trip is next before runtime integration.
Validation 140 / Checkpoint 383 then qualify the exact keyring package on Windows x64 and complete one synthetic normal-user-session Credential Manager set/read-match/delete/absence lifecycle. The sandbox-only `ERROR_NO_SUCH_LOGON_SESSION` is localized to execution context. Main-runtime G0 integration is now the next Research 123 implementation boundary.
Validation 141 / Checkpoint 384 qualify main-runtime G0 source composition with 9/9 syntax and 4/4 focused integration regressions while retaining the 63-tool public surface. Runtime Release v1 cannot provision the required `@napi-rs/keyring@2.0.0` package because its target contract excludes package manifests and `node_modules`; bounded deterministic dependency provisioning/rollback is now the active implementation blocker.
Validation 142 / Checkpoint 385 close the dependency-provisioning design blocker with immutable exact native-package generations, v2 release refs, restart/rollback/recovery selection and G0 exact-generation loading. Same-process Windows deletion after native load failed with `EPERM`, so old generations are intentionally retained and garbage collection remains a separate future lifecycle. The live runtime still has Release v1; one source-only v1 bootstrap release is now required before dependency-aware v2 activation.
Validation 143 / Checkpoint 386 live-qualify the source-only bootstrap through the old v1 engine: prepare, publication, zero-mismatch source verification and restart all pass, and the replacement runtime now exposes dependency-aware verification with `runtimeDependencyCount=0`. The public surface stays at 63 tools and zero `github.*` actions. The active implementation boundary is now exact v2 keyring-generation activation before any live GitHub authorization.
Validation 144 / Checkpoint 387 then live-qualify one exact Runtime Release v2 keyring dependency. The worker is now bound to one immutable `github-keyring-win32-x64` generation, publication/restart/postactivation verification all pass, and the public surface remains 63 tools with zero `github.*` actions. Package deployment is no longer the G0 blocker; the next architecture item is an explicit bounded authorization-control support surface before read-only parity actions.
Validation 145 / Checkpoint 388 live-qualify that bounded authorization-control support surface as `codex.github_authorization`. The final immutable fix2 release activates preview.24 / 64 tools with the exact keyring generation retained; local MCP discovery and metadata-only invocation pass while `configured=false`, `storedAuthorization=false`, and all 89 parity actions remain unpublished. The current persistent ChatGPT projection remains stale, so a refreshed fresh-chat schema plus metadata-only qualification is the immediate Research 123 gate. No device flow or GitHub API request has started.
Validation 146 / Checkpoint 389 then apply the known host-projection correction after the first fresh-chat qualification exposes the preview.24 union only as a generic map. Preview.25 keeps 64 tools and zero parity actions while flattening the authorization input schema and retaining exact server-side action-field validation. The full 16-regression release matrix, publication, activation and local metadata all pass; fresh-host flat-schema/metadata requalification is next.
Validation 147 / Checkpoint 390 then host-qualify the corrected support surface: fresh-chat schema projection is structured, metadata succeeds without mutation, and the live Plugin rename is directly evidenced. AB-029 now advances to the exact GitHub App permission manifest required before registration/device flow.
Validation 148 / Checkpoint 391 freeze the 89-action GitHub App authority manifest at seven repository permissions with no organization/account/enterprise/webhook authority. Administration/Checks/Members remain excluded. Exact REST permission evidence is complete; GitHub documents GraphQL permission sufficiency as something Apps must test, so eight PR/review GraphQL operations remain a live probe under existing Pull requests(write). Registration configuration is the next boundary.
Validation 149 / Checkpoint 392 freeze the GitHub App registration and initial installation configuration around that authority: Any account/public App, device flow + expiring tokens, no install-time OAuth/webhooks/callback/setup/private-key path, and first live installation limited to the canonical ADS repository. AB-029 now requires an owner-performed GitHub UI creation/install before Runtime Bridge Client ID configuration can proceed.
Validation 150 / Checkpoint 393 reopen the authority manifest before App creation after the owner explicitly expands the goal beyond native 89-action parity. Repository Administration(write) and a broader set of CI/CD, checks, security, agent and optional Codespaces capabilities are now under review. Secret-value and arbitrary-webhook authority remain deferred pending dedicated safety contracts. Personal installation scope is corrected to All repositories. The seven-permission Checkpoint 392 creation instruction is paused until the complete live permission surface is reconciled and a developer-superset manifest is frozen.
Validation 151 / Checkpoint 394 complete the current GitHub App live permission inventory at 118 rows (40 repository, 42 organization, 19 account, 17 enterprise) and qualify a broad developer-superset candidate. Validation 152 / Checkpoint 395 freeze the actual initial extended profile at 74 selected/read rows, including Repository Administration(write), with 56 documented prefill parameters plus 18 manual live-only selections. Secret-value and webhook authority remain off; personal install scope is All repositories. AB-029 is now back at owner-performed App creation/install, using the extended configuration rather than the superseded seven-permission prefill.
Validation 154 / Checkpoint 397 then record successful App registration and an unexpected live GitHub install gate requiring at least one App private key before installation. This does not alter the Runtime Bridge user-token/device-flow design, which still uses Client ID without Client secret/private-key authority. The bounded correction is generate one key only for the install gate, never expose/use it, install with All repositories, then destroy the downloaded local PEM.
Validation 155 / Checkpoint 398 then close the personal-installation gate: the App is live on `shakaarlatief` with All repositories selected. The generated bootstrap private key is not part of Runtime Bridge authority and its downloaded PEM is now pending local deletion before Client ID configuration and device-flow qualification continue.

Current continuation through Validation 201 / Checkpoint 444 supersedes that old execution pointer. Protected device-flow authorization remains live and healthy; Runtime Bridge implements all 89 captured native action names, and four beyond-parity families are complete. The final Repository Governance value decision selects one fifth and intended-final important extension family: Repository Branch-Safety Governance. Current GitHub state has no rulesets and no protection on `main` or promoted integration branch `v1-frontend-spike`, while the App has `Administration=write`. Because ADS still has maintained automation that performs ordinary fast-forward pushes to `v1-frontend-spike`, the selected baseline deliberately does not require PRs or status checks. It only blocks force pushes and branch deletion and enforces those restrictions for administrators while preserving ordinary fast-forward updates. The foundation contains three bounded actions: read exact branch protection, create the fixed `codexless.branch-safety-baseline.v1` only when no protection exists, and remove only that exact baseline when branch head and policy still match. Capability qualification uses a disposable branch; permanent protection of `main` and `v1-frontend-spike` remains a separate explicit owner-authorization gate. The immediate AB-029 route is implementation/publication and non-writing qualification of this three-action foundation. Other GitHub surfaces remain recorded for future need rather than scheduled now. Secret-value and webhook-management APIs remain deferred. Historical branch cleanup remains optional and separate. AB-030 remains parked unchanged and is not part of this work.

---

## AB-030: Governed ADS validation to GitHub CI-evidence workflow

**Status:** OPEN / CI-EVIDENCE FOUNDATION QUALIFIED / DESIGN CANDIDATE
**Priority:** P1

The CI Evidence Publication foundation introduced under Research 123 is a publication capability, not a new validator or an automatic pre-push gate. A valuable next architecture step is to connect existing ADS validation and repository-integrity evidence to that GitHub publication surface so that the exact result of governed local validation can become first-class visible evidence on the corresponding GitHub commit or pull request.

Candidate workflow:

```text
ADS prepares a repository change
    -> resolve the required V0-V4 verification level and governing validators
    -> run the required local deterministic / integrated validation
    -> fail closed locally if the required validation is incomplete or fails
    -> create/push the exact commit through the existing guarded Git path when authorized
    -> bind the resulting exact GitHub commit SHA
    -> publish a Codexless-owned GitHub Check and/or namespaced commit status
    -> attach bounded summaries and useful file/line annotations where available
    -> update the Check monotonically to its final completed conclusion
    -> use the GitHub-visible evidence for review, PR decisions, and later audit
```

The key architectural distinction must remain explicit:

```text
ADS validation / repository-integrity mechanisms
    decide what was actually checked and whether the change is acceptable

GitHub CI Evidence Publication
    records and exposes that already-earned evidence on the exact commit
```

GitHub publication must therefore never turn a missing, partial, stale, or failed local validation into a green status merely because a status can be written. The published result should carry enough provenance to identify the exact commit and the validation family/tier that produced it. Existing local push/integrity guards remain authoritative for whether a push is permitted unless a later accepted architecture deliberately changes that responsibility.

Useful future decisions include:

```text
which ADS validators deserve persistent GitHub Checks versus lightweight commit statuses
whether publication occurs only after push, during PR preparation, or at several lifecycle points
how V0-V4 verification tiers map to stable Check names and conclusions
how exact test/validator provenance is summarized without duplicating large logs
when line-level annotations are useful and trustworthy
how repeated validation of the same SHA is versioned or updated without hiding earlier failures
how local ADS evidence should coexist with GitHub Actions results rather than impersonate them
whether selected Codexless Checks should eventually participate in merge or branch-protection policy
how publication failure is handled so GitHub visibility failure does not falsify the underlying local validation result
```

The first concrete example worth evaluating after the six-action CI-evidence foundation is live-qualified is publication of an exact `PUBLIC_REPOSITORY_INTEGRITY` result for one explicitly selected commit under a Codexless-owned Check/status identity. Positive publication must remain separately authorized until Research 123 deliberately opens that workflow.

Primary current foundation:

```text
docs/local_execution/validation/188_github_extended_ci_evidence_foundation_design.md
docs/checkpoints/431_github_extended_ci_evidence_foundation_designed_implementation_next.md
```

---

# Continuation obligations that must not be forgotten

## CO-001: MC-0010 Claude dual-repository research

**Status:** READY / PENDING EXECUTION
**Priority:** P1

Before Claude Message 001, verify a fresh Claude environment can access both the public ADS authority repository and the private local-runtime implementation repository. If the private repository is unavailable, preserve that limitation rather than substituting public summaries as equivalent evidence.

---

## CO-002: Deliberate Chat 17 rotation after continuity preflight

**Status:** READY AFTER CURRENT PRESERVATION
**Priority:** P1

The Research 116 blocker is closed and the 52-tool `codex.document_read` surface is live-qualified. Rotation must still use the actual `CHAT_ROTATION_PREFLIGHT` procedure and must not occur while Checkpoint 279 public/private preservation or another meaningful current-session side track remains unpreserved. A fresh chat should begin with the final stable 52-tool MCP surface intended for the next phase.

---

## CO-003: Resume Source Vault only after the selected Level-2 research pause closes

**Status:** PAUSED
**Priority:** P1

Preserved sequence:

```text
reviewed ingestion of frozen 20-entry first corpus
-> working-store integrity audit
-> deterministic backup staging
-> client-side encryption
-> independent remote replication
-> remote retrieval
-> encrypted-object digest reproduction
-> decryption
-> clean restore
-> restored integrity audit
-> Course 2 unblock only after recovery proof succeeds
```

Primary procedure: `docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md`.

---

# Maintenance rule

Whenever the project owner or collaborator says something equivalent to:

```text
remember this
we should investigate this later
this needs a better architecture
we should add this eventually
do not forget this when we rotate chats
```

perform a backlog check before the session boundary.

Use this routing rule:

```text
1. Already represented here?
   -> update the existing item when material new evidence emerges.

2. Important unresolved scientific/product question?
   -> `docs/OPEN_QUESTIONS.md` may be the stronger owner; link instead of duplicating.

3. Live current action/boundary?
   -> `docs/CURRENT_STATE.md` remains the owner.

4. Substantial evidence-producing investigation?
   -> open/update research or validation evidence and link it here.

5. Accepted/implemented?
   -> move durable truth into the stronger accepted layer and close/remove the backlog item during reconciliation.
```

At planned chat rotation, scan this backlog together with `CURRENT_STATE.md`, `OPEN_QUESTIONS.md`, and the active research/checkpoint so side ideas do not disappear merely because they were not the main route.
