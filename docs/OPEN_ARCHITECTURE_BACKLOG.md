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

**Status:** OPEN / REPRODUCTION OBSERVED
**Priority:** P0

If the user's laptop is running Codexless and the tunnel, the same authorized ADS connector should work from ChatGPT on laptop, phone, tablet, or another signed-in client.

Observed in `chatgpt-16`: the connector worked from the laptop, while the same conversation on the phone returned `401 tunnel_active_organization_required` even though the laptop remained on.

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

**Status:** OPEN
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

Primary context: Research 116 and existing guarded host publication helpers.

---

## AB-003: Autonomous supervision and wakeup for long-running Codex tasks

**Status:** OPEN / REPRODUCED ARCHITECTURE GAP
**Priority:** P0

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

Primary evidence: `docs/local_execution/validation/035_running_codex_supervision_liveness_gap_reproduced.md`.

---

## AB-004: Active-turn writer ownership transfer and reacquisition

**Status:** OPEN / RESEARCH QUESTION
**Priority:** P0

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

---

## AB-005: Reuse-first multimodal document architecture

**Status:** RESEARCHING / CUSTOM IMPLEMENTATION PAUSED
**Priority:** P1

The first-class `codex.document_read` PDF baseline is no longer open work. It is live-qualified on Codexless `0.1.1-preview.9` / 52 tools through Validation 039 and Checkpoint 279, including the isolated bounded `pdfjs-dist@5.4.624` parser child and a real read-only personal-PDF test.

Research 117 has now changed the default direction: before ADS builds any of the capabilities below, first test/reuse native OpenAI PDF multimodality, installed Codex PDF/Documents/Presentations/Spreadsheets Skills, App Server image/local-image semantics, and only then mature converters such as MarkItDown, Docling, or PyMuPDF4LLM if concrete gaps remain. The likely missing problem is a safe local-file/media handoff seam, not document understanding itself.

Remaining document-system directions are deliberately separate capabilities and are paused pending those reuse experiments:

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

Primary accepted baseline evidence: `docs/local_execution/validation/039_workspace_standard_and_document_read_live_qualified.md`.

---

## AB-006: Robust Codex task recovery after caller/tunnel/device interruption

**Status:** OPEN
**Priority:** P0

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

---

## AB-007: Actionable Rich Card supervision surface

**Status:** OPEN
**Priority:** P1

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

---

## AB-008: Stable MCP schema and ChatGPT tool-projection lifecycle

**Status:** OPEN / MONITOR
**Priority:** P1

Validation 034 showed an existing conversation can retain an older callable action projection after the live MCP server publishes new actions. Research 116 therefore moved ordinary workspace/project variability into server-owned policy behind stable schemas.

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

**Status:** RESEARCHING
**Priority:** P1

Study whether App Server `approvalsReviewer` / `auto_review` can complement the ChatGPT-side Codex Call Profile.

Do not collapse the layers without evidence:

```text
Call Profile        user-authored policy for calling/supervising Codex
App Server reviewer lower-level in-turn action review/routing
```

A future design may allow routine low-risk approvals under explicit user policy while preserving user review for high-risk or ambiguous actions.

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

**Status:** OPEN / FUTURE ARCHITECTURE
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

**Status:** OPEN / MONITOR
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
