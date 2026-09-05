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

Primary context: Research 116 and existing guarded host publication helpers. Validation 042 now provides a concrete reproduced case: the `codex.image_read` publication helper passed all candidate gates, but ordinary inherited `command_exec` was denied before writing `%LOCALAPPDATA%\\Codexless`; live hashes remained unchanged. This is exactly the separation this backlog item should solve without broadening workspace authority.

Validations 062-063 add two later examples. The native Auto-review executor and the direct-Codex guard correction were both safely qualified inside the authorized local-runtime workspace, but live installation still required one-time guarded host PowerShell publication with exact old/new hashes, backup, atomic replacement, verification, and rollback. Those bootstraps are accepted operational evidence, not a solution to AB-002.

---

## AB-003: Autonomous supervision and wakeup for long-running Codex tasks

**Status:** OPEN / WAKEUP GAP REMAINS / ROUTINE APPROVAL MITIGATION LIVE
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

Validation 062 live-qualified one important mitigation: formal turns now use App Server `approvalPolicy=on-request` with `approvalsReviewer=auto_review` while preserving the separate initial `Call Codex?` gate and existing bounded permission profile. Routine in-turn command approvals no longer reproduced the `awaitingApproval` stall in the tested case. AB-003 remains open because ChatGPT still has no demonstrated autonomous wakeup for task completion, errors, escalations, or any future action that native Auto-review cannot safely resolve.

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

**Status:** RESEARCHING / ATTEMPT 01 AMBIGUOUS / CONTROLLED SECOND RUN READY
**Priority:** P1

Research 118 / Validation 066 / Checkpoint 307 now preserve the first held-out 11,825,407-byte semantic worker as `AMBIGUOUS`, not a semantic failure. The worker stopped fail-closed when it could not establish the maintained execution runtime from the selected nested scratch cwd. Model-free reconciliation then proved the exact maintained primary-runtime parser/extractor/Poppler stack is available, reproduced the nested-cwd write setup failure, rendered all eight pages successfully from the registered ADS repository root, and verified the local-image-to-native-vision path. The next action is the controlled changed-condition second worker from the repository-root execution context, not new rendering/OCR implementation, Browser upload, or a blind retry.

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

Primary accepted baseline evidence: `docs/local_execution/validation/039_workspace_standard_and_document_read_live_qualified.md`. Validation 040 proves that the maintained Codex PDF Skill routes in the authorized workspace, although that turn found an unusable MiKTeX `pdftoppm` stub and did not locate an alternative renderer. Validation 041 proves that an already-authorized local PNG can be visually understood through Codex's native `view_image` path. Validation 043 proves the model-free direct-host path: `codex.image_read` returns standard MCP image content visible to ChatGPT model vision, with no extra Codex model turn, Browser or OCR. Validation 044 proves the maintained OpenAI/Codex primary runtime already contains viable Poppler rendering. Validation 045 then qualifies the preferred thin semantic seam: `codex.document_render` keeps untrusted PDF rendering inside the existing Codex `command/exec` read-only sandbox and reuses maintained primary-runtime `pdfjs-dist` + `@napi-rs/canvas` to produce in-memory PNG pages returned as standard MCP image content. Its publication preflight passes at preview.11 / 54 tools with no caller write authority, no extra Codex model turn, no new external dependency, and no live publication yet. Representative PDF fidelity remains the next document-specific qualification after live publication.

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

Primary context: Foundation 014, D-024, D-032, D-034, Research 064, Research 103, Research 104, AB-023, AB-024, and AB-026.

---

## AB-028: Post-Browser Astra independent architecture review after the GPT-5.6 Sol baseline

**Status:** CLOSED / PHASE 2 COMPLETE / RESEARCH 118
**Priority:** P1

Closure 2026-09-05: Astra completed the independent Phase 1 review before private Sol exposure, then completed Phase 2 against the frozen Sol baseline. Research 118 / Validation 065 / Checkpoint 306 preserve the reconciliation. The reviewed private source-bound PDF evidence candidate is preserved at `a5025c2071077f719dcc59c7dfd729ee59ec34eb`. Direct existing-tab Browser mutation remains blocked, direct new-tab mutation is deferred as lifecycle-unproven, and the Browser-free held-out semantic PDF experiment is now the exact next Research 117 action. This backlog item is closed; live semantic qualification remains under AB-005 / Research 117-118 rather than reopening AB-028.

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
