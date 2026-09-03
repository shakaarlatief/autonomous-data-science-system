# Research 114: Current Codex App Server Architecture and ADS Implications

**Date:** 2026-09-03  
**Status:** ACTIVE BASELINE / OFFICIAL UPSTREAM CAPABILITY MAP STARTED  
**Scope:** Establishes a current official App Server capability baseline and compares the most consequential protocol/lifecycle features against ADS's existing Codexless architecture. This is the first topic-specific study under Research 113.  
**Authority:** Research evidence only. Current upstream `main` documentation is not automatically identical to the locally installed Codex `0.152.1` runtime. Any proposed adoption must be version-probed locally before implementation.  
**Declared references:** `research:113`, `checkpoint:276`, `research:109`, `research:110`, `research:111`, `research:112`, `path:docs/local_execution/OPERATIONS.md`, `path:docs/research/CODEX_UPSTREAM_ADS_COMPARISON_MATRIX.md`

## 1. Primary source and version caution

Primary source for this first pass:

```text
https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md
```

The current upstream README states that generated TypeScript/JSON schemas are version-specific and can be emitted by the exact Codex binary. That is an important methodological constraint for ADS: findings from `main` identify current upstream direction, while exact local implementation decisions must be checked against the installed Codex runtime and generated schemas/tests for that runtime.

Current ADS project context reports Codex CLI `0.152.1`. This study does not claim every `main` experimental method is available or behaviorally identical in that local binary.

Evidence class for sections derived from the current official README: `A / OFFICIAL_DOCUMENTATION`.

## 2. Core semantic model: Thread -> Turn -> Item

The official App Server now documents three first-class top-level interaction primitives:

```text
Thread
    conversation/session identity

Turn
    one user-to-agent interaction within a thread

Item
    persisted user input or agent output within a turn
```

Items include user messages, reasoning, agent messages, shell/command execution, file edits and tool activity. The normal streaming lifecycle is:

```text
item/started
-> zero or more item-specific deltas
-> item/completed
```

A turn itself emits `turn/started` and ends with `turn/completed`.

### ADS implication

This is the strongest current evidence that the next live-viewer renderer should be **item-centric rather than display-event-centric**.

The v16 ADS viewer proved event acquisition and live card refresh, but flattened events into independent rows. The native Desktop recording showed that commands, file reads/edits and Codex narration behave as evolving semantic units. App Server already provides the conceptual unit needed to implement that cleanly.

Preliminary classification:

```text
v16 flattened display-event projection    POTENTIAL_REPLACEMENT
item-centric transcript projection         POTENTIAL_SIMPLIFICATION / POTENTIAL_IMPROVEMENT
```

No renderer rewrite is authorized yet. First verify the item IDs, item fields and delta behavior available in local `0.152.1`.

## 3. Item-specific UI semantics

### 3.1 Agent messages

`item/agentMessage/delta` streams text for one `itemId`; clients concatenate deltas belonging to that item.

ADS implication: normal Codex narration can remain a coherent message item rather than multiple telemetry rows.

### 3.2 Plans

Experimental `item/plan/delta` streams proposed plan content for a plan item. Separate turn-plan updates also exist in the protocol.

ADS implication: a plan can be presented as an evolving plan/checklist rather than generic `CODEX` activity.

### 3.3 Reasoning summaries

The official protocol distinguishes:

```text
item/reasoning/summaryTextDelta
    readable reasoning summaries

item/reasoning/summaryPartAdded
    summary-section boundary

item/reasoning/textDelta
    raw reasoning text, applicable for e.g. open-source models
```

ADS must preserve its existing safety boundary: user-visible readable reasoning summaries can be rendered; private hidden chain-of-thought must not be exposed merely because a transport contains a reasoning-text field.

Preliminary classification:

```text
readable summary projection    KEEP / IMPROVE PRESENTATION
raw hidden reasoning exposure  REJECT
```

### 3.4 Command execution

`commandExecution` items include structured fields such as:

```text
id
command
cwd
status
commandActions
aggregatedOutput
exitCode
durationMs
```

`item/commandExecution/outputDelta` streams live stdout/stderr for the same item. The final item is authoritative for status/output metadata.

ADS implication: one command card can evolve:

```text
started
-> live output deltas
-> completed / failed / declined
```

This directly addresses the v16 duplicate start/output/completion-row problem. Parsed `commandActions` may also provide a better human display than the raw full executable invocation.

### 3.5 File changes

A `fileChange` item carries structured changes and status. File-change approvals use the same `itemId`; completion returns the same item with terminal state. App Server additionally emits `turn/diff/updated`, an up-to-date aggregated unified diff across the turn so a UI does not need to stitch separate patches itself.

ADS implication: the native Desktop-like presentation can show compact changed-file summaries while a detailed turn-level diff is available on demand.

Preliminary classification:

```text
manual display-event diff assembly    POTENTIAL_SIMPLIFICATION
turn/diff/updated                      POTENTIAL_UPSTREAM_REUSE
```

## 4. Persisted history without writer acquisition

Current App Server documentation provides read-oriented history APIs including:

```text
thread/read
thread/turns/list
thread/items/list
thread/searchOccurrences
```

These can inspect persisted history without resuming the thread. Paginated history supports summary/full item views and cursors.

`thread/resume` is increasingly oriented toward attaching to live state while history is loaded incrementally through list APIs. Full-history hydration is documented as deprecated for paginated threads.

### ADS implication

ADS's model-free non-owning bind intentionally uses `thread/read` before later resume. That principle remains sound and is now reinforced by a richer upstream read-only history surface.

Potential future simplification:

```text
historical transcript reconstruction
    thread/turns/list + thread/items/list

live attach / writer acquisition
    thread/resume only when actually needed
```

This separation may improve both the viewer and handoff recovery, but local version support must be verified.

## 5. Explicit paginated-thread writer ownership

Current official documentation states that only one App Server process can hold a **paginated thread** open for writing at a time. If another process owns it, `thread/resume`, `thread/archive`, and `thread/delete` can fail, while read-only requests remain available without resume.

### ADS implication

This is important official support for an architectural distinction ADS had to establish experimentally:

```text
persisted thread identity/read access
!=
live writer ownership
```

It strengthens the rationale behind model-free non-owning bind/read and fail-visible writer reacquisition rather than forced takeover.

It does **not** prove all previously tested legacy-thread ownership behavior or Desktop behavior, so ADS's experiments remain valuable evidence.

Preliminary classification:

```text
ADS durable threadId model                 KEEP_ADS
model-free read before writer acquisition  ADS_ALREADY_SOLVES / OFFICIALLY ALIGNED
forced writer stealing                     REJECT
```

## 6. Thread subscriptions, status and unload behavior

Current App Server provides:

```text
thread/status/changed
thread/unsubscribe
thread/closed
thread/loaded/list
```

`thread/unsubscribe` is connection-scoped. When the final subscriber leaves, App Server now keeps an inactive thread loaded for a configurable default 60-second delay before unloading, running `SessionEnd` hooks and emitting close/status events. New subscriber/activity resets the countdown.

### ADS implication

This gives a much clearer formal model for a distinction that mattered during the Desktop handoff investigation:

```text
subscription
thread loaded state
writer/runtime activity
persistence
```

These are not one thing.

Potential research question: whether a supported shared-App-Server spectator client can subscribe to a Codexless-owned thread without acquiring conflicting writer ownership, and whether that would materially improve viewing. Do not infer this is already supported across independent App Server processes.

A community issue requesting an explicit immediate `thread/unload` further indicates that unsubscribe and process-lifetime ownership remain active design areas, but that issue is only `F / COMMUNITY_OBSERVATION` until an upstream contract changes.

## 7. Same-turn steering

Current App Server documents experimental `turn/steer`:

```text
append user input to the currently active regular turn
require exact expectedTurnId
do not start a new turn
do not accept settings overrides
reject no-active/mismatched/non-steerable target
reject direct steering of parent-owned Multi-Agent V2 subagents
```

An optional client message ID is echoed on the corresponding persisted user-message item.

### ADS implication

Current Codexless `agent_send` is a next-turn continuation mechanism. ADS has not yet exposed a same-turn steering surface.

This is a potentially important capability because it could allow the supervising ChatGPT conversation to redirect a long Codex task while it is still running rather than interrupting or waiting for completion.

However, safe adoption requires:

```text
exact active turn identity
stable caller request identity
no replay after uncertain result
clear receipt/consumption evidence
Profile-bound supervision policy
no permission/model/cwd widening
clear UI semantics
```

The public Codexless same-turn steering PR independently emphasizes those same constraints. That convergence is worth deeper study.

Classification:

```text
turn/steer    INVESTIGATE
```

## 8. Persistent queued follow-up turns

App Server now documents experimental thread queue operations:

```text
thread/queue/add
thread/queue/list
thread/queue/update
thread/queue/delete
thread/queue/reorder
thread/queue/start
thread/queue/changed
```

Queued messages persist and are submitted FIFO when the thread becomes idle. Interrupted turns leave the queue paused. Queue entries retain stable submission and client-message IDs.

### ADS implication

This may provide a more reliable future mechanism for **planned follow-up work** than keeping all next-step intent only in the calling ChatGPT session while a long Codex turn runs.

It is not automatically a replacement for `agent_send` or the ChatGPT-side Call Profile. Questions include:

```text
Does queue persistence survive the exact failure/restart modes ADS cares about?
How are metered-call consent and user intent preserved?
Can ChatGPT safely enqueue without accidentally starting unwanted later work?
How does queued work interact with approvals and changed project state?
What happens across Desktop/Chat handoff?
```

Classification: `INVESTIGATE / POTENTIAL_IMPROVEMENT`.

## 9. Live settings updates

Experimental APIs distinguish future-thread settings from exact-live-turn settings:

```text
thread/settings/update
turn/settings/update
```

Exact-turn updates can change reviewer/model-related settings for subsequent captured steps under restrictions. Existing captured steps and pending approvals keep their prior reviewer. Failed/vanished targets are not silently retargeted.

### ADS implication

The fail-closed exact-target semantics align well with ADS's current lifecycle discipline. But the API is explicitly experimental and documentation warns that complete model-instruction correctness/resume behavior for live model switching is not guaranteed.

This is not a basis for replacing the Call Profile. It is a possible lower-level mechanism for future exact-turn controls after more evidence.

Classification: `MONITOR / INVESTIGATE`.

## 10. Approval reviewer and automatic review

Turn start can select:

```text
approvalsReviewer = user
auto_review
```

`auto_review` routes approval requests to a risk-review subagent. Managed requirements can require automatic review on selected models, and app-specific configuration can override reviewer settings.

Command approval requests include the same thread/turn/item identity and can expose the set of available decisions. File-change approvals similarly tie the pending request to the active item.

### ADS implication

This must be compared carefully with the ADS Call Profile, because they solve different layers:

```text
ADS Call Profile
    ChatGPT-side policy for when to call Codex, task sizing, supervision,
    model/reasoning choice, pending-action handling and result integration

App Server approvalsReviewer
    Codex/App-Server-side reviewer routing for in-turn approval requests
```

Possible future integration exists, but collapsing these layers would lose useful policy separation.

Preliminary classification:

```text
Call Profile                         KEEP_ADS
approvalsReviewer / auto_review      INVESTIGATE AS COMPLEMENT
silent replacement of Call Profile  REJECT
```

## 11. Multi-agent/subagent expansion

Current App Server exposes persisted thread lineage:

```text
parentThreadId
ancestorThreadId
agentNickname
agentRole
```

Thread list can query descendants. Parent-owned Multi-Agent V2 child sessions have special ownership semantics and reject several direct operations. Deprecated `multiAgentMode` is ignored; current documentation points to Ultra reasoning effort for proactive multi-agent behavior.

### ADS implication

Future Codexless supervision may need to understand a **tree of threads**, not only one root `threadId`.

This matters for:

```text
live viewer hierarchy
approval routing
stop/interrupt semantics
handoff
history reconstruction
resource accounting
failure recovery
```

ADS should not add custom multi-agent lifecycle rules until the official lineage/ownership semantics are mapped more fully.

Classification: `INVESTIGATE / MONITOR`.

## 12. MCP extension profile and Apps

Clients advertise supported MCP extensions during App Server initialization. The extension profile used by a Codex session is fixed when the session is created by `thread/start`, `thread/resume`, or `thread/fork`; it is not dynamically rewritten by a later turn from a different connection. Subagents inherit that profile.

App Server also exposes app listing/tool listing and update notifications.

### ADS implication

This has direct relevance to Rich Task Card/MCP App compatibility and to why resource/capability changes often require a runtime/tunnel/ChatGPT plug-in refresh rather than assuming an already-running thread will inherit new client capabilities.

The exact relationship to the ChatGPT MCP host and our v16 resource caching needs dedicated follow-up research.

Classification: `INVESTIGATE`.

## 13. Transport and control-plane evolution

Current App Server supports:

```text
stdio
experimental websocket listener
local unix-socket/websocket control path, including Windows
daemon lifecycle
```

On Windows, the documented local socket directory uses a protected current-user-only DACL and rejects pre-existing broad permissions rather than silently repairing them.

The server also documents bounded transport queues and an overload error (`-32001`) that clients should treat as retryable with backoff/jitter.

### ADS implication

Codexless currently supervises its own App Server process/transport. Upstream daemon/control-plane evolution may eventually reduce custom process-lifecycle code, but experimental/unsupported transports must not be adopted prematurely.

The fail-closed Windows ACL behavior is philosophically aligned with ADS's authority model.

Classification: `MONITOR / POTENTIAL_SIMPLIFICATION`.

## 14. Unsandboxed process/filesystem surfaces are not an ADS shortcut

Current App Server exposes broad process and filesystem utilities. The process API documentation explicitly states that spawned processes are unsandboxed and connection-scoped, and filesystem utilities operate on absolute host paths.

### ADS implication

Their existence does not mean ADS should expose them publicly. ADS's existing deliberate choice to keep broad process authority off the public ChatGPT surface remains justified by least authority and interpretability.

Classification:

```text
broad unsandboxed process as public shortcut  REJECT / KEEP CURRENT BOUNDARY
bounded semantic actions                      KEEP_ADS
```

## 15. Current community evidence relevant to ADS experiments

Issue reports are `F / COMMUNITY_OBSERVATION`, not contracts. Nevertheless, several current reports strongly resemble ADS-observed failure classes:

### 15.1 Archive/unarchive stale Desktop state

Current reports include successful backend archive/unarchive followed by stale Desktop resume/path/UI behavior, sometimes recovering after restart.

Examples:

```text
https://github.com/openai/codex/issues/26174
https://github.com/openai/codex/issues/33860
https://github.com/openai/codex/issues/26159
https://github.com/openai/codex/issues/25713
```

This gives external corroboration for ADS's bounded classification that its observed stale post-handoff Desktop state can be a UI/client synchronization problem rather than durable thread corruption.

It does not prove the exact ADS event had the same root cause.

### 15.2 Cross-client live synchronization remains a real ecosystem problem

Community reports describe history being shared while live in-memory state is not automatically synchronized across independent clients/processes.

Examples include:

```text
https://github.com/openai/codex/issues/11958
https://github.com/openai/codex/issues/29094
```

This is consistent with ADS's experiment where Desktop could open the persisted Codexless-owned thread but remained static until reload.

### 15.3 Protocol/version drift can strand otherwise intact threads

A very recent Windows report describes a Desktop/App-Server mismatch around paginated resume parameters after an update, while persisted data remained intact:

```text
https://github.com/openai/codex/issues/41512
```

This is especially important for ADS because durable thread identity is only useful if client/server protocol compatibility is also guarded.

Potential ADS action: add a version/capability compatibility probe before claiming same-thread Desktop handoff support after significant Codex/Desktop updates.

Classification: `POTENTIAL_IMPROVEMENT`.

### 15.4 Pagination solves only part of long-thread UX

A recent issue reports that a large recent turn can still make paginated task bootstrap slow because item-count limits do not bound serialized byte size:

```text
https://github.com/openai/codex/issues/38653
```

This matters for a future Rich Task Card viewer: do not assume loading hundreds of full command/output items is an acceptable transcript bootstrap strategy. Summary views and lazy details should be preferred.

Classification: `MONITOR / DESIGN_INPUT`.

## 16. First architecture disposition

The official current App Server baseline does **not** imply that ADS's custom architecture should be thrown away. It already validates several of ADS's important principles:

```text
stable durable thread identity
read without writer acquisition
exact turn identity
semantic item lifecycle
inline approval identity
fail-visible target mismatch
separation of live subscription from persistence
```

But upstream has advanced enough that several custom mechanisms should be re-evaluated before further extension:

```text
v16 display-event renderer
next-turn-only supervision
history reconstruction
approval reviewer integration
multi-agent visibility
runtime/process lifecycle
MCP resource/capability refresh assumptions
```

## 17. Highest-priority local verification experiments after research

Do not run these yet. They are candidates for a later controlled validation phase.

```text
1. Generate/inspect the exact 0.152.1 App Server schema and compare it with main.
2. Verify local thread/items/list and thread/turns/list availability/semantics.
3. Verify exact local commandExecution item IDs/deltas/final fields for renderer use.
4. Verify exact local reasoning-summary events while preserving hidden-reasoning policy.
5. Verify turn/diff/updated behavior against fileChange items.
6. Determine whether turn/steer exists locally and how uncertainty/idempotency can be proven.
7. Determine whether thread queues exist locally and what persists across App Server restart.
8. Probe thread status/unsubscribe behavior only in disposable threads.
9. Characterize local multi-agent lineage if Ultra/subagents are used.
10. Add a Desktop/App-Server compatibility preflight concept before durable handoff claims.
```

## 18. Research continuation

The next parallel research tracks are:

```text
public Codexless current source/tests/PR baseline and ADS-local delta
systematic openai/codex issue/PR/discussion cluster mining
exact local 0.152.1 schema/capability comparison
MCP Apps/resource lifecycle and ChatGPT host refresh behavior
approval/Guardian architecture comparison
steering/queue supervision design
multi-agent/subagent lifecycle
```

All findings should feed `docs/research/CODEX_UPSTREAM_ADS_COMPARISON_MATRIX.md` and Research 113's final architecture reconciliation.
