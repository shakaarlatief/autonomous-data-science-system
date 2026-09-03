# Codex Upstream vs ADS Comparison Matrix

**Status:** ACTIVE LIVING RESEARCH INDEX  
**Opened:** 2026-09-03  
**Authority:** Comparative research index under Research 113. Individual research records and cited primary sources govern the detailed evidence. This matrix does not itself authorize implementation changes.

## Classification vocabulary

```text
KEEP_ADS
UPSTREAM_NOW_PROVIDES
POTENTIAL_REPLACEMENT
POTENTIAL_SIMPLIFICATION
POTENTIAL_IMPROVEMENT
KNOWN_UPSTREAM_LIMITATION
ADS_ALREADY_SOLVES
DEFER
MONITOR
MORE_EVIDENCE_REQUIRED
```

## Evidence classes

```text
A OFFICIAL_DOCUMENTATION
B OFFICIAL_SOURCE
C MERGED_UPSTREAM_CHANGE
D MAINTAINER_STATEMENT
E OPEN_PROPOSAL
F COMMUNITY_OBSERVATION
G ADS_EXPERIMENT
H INFERENCE
```

## Current matrix

| Area | Current upstream evidence | Current ADS behavior | Difference / implication | Classification | Confidence / next proof |
|---|---|---|---|---|---|
| Thread/Turn/Item semantic model | App Server `main` officially models Thread -> Turn -> Item with item lifecycle events. `A` | v16 stores/derives a display-safe activity projection but renders many events as flat rows. | Strong candidate to make viewer item-centric instead of event-centric. | `POTENTIAL_REPLACEMENT` / `POTENTIAL_SIMPLIFICATION` | High for upstream main; verify exact local 0.152.1 item schema/events. |
| Agent narration | `item/agentMessage/delta` reconstructs one message by item ID. `A` | v16 shows Codex message activity but with weak narrative hierarchy. | Can render one evolving/prose message item. | `POTENTIAL_IMPROVEMENT` | Verify local deltas/item IDs. |
| Reasoning summaries | `summaryTextDelta` + `summaryPartAdded` are explicitly readable summaries; separate raw reasoning text exists. `A` | ADS intentionally exposes only user-visible summaries, not hidden raw chain-of-thought. | Upstream supports the safety/presentation split ADS wants. | `KEEP_ADS` / `UPSTREAM_NOW_PROVIDES` | High; verify local event set and keep hidden-reasoning guard. |
| Command lifecycle | One `commandExecution` item streams output and completes with parsed actions/status/exit/duration. `A` | v16 displays separate command/output/completion rows and raw invocation detail. | One evolving command card is directly supported semantically. | `POTENTIAL_SIMPLIFICATION` | High; inspect local final fields and parsed actions. |
| File-change presentation | Structured `fileChange` items plus `turn/diff/updated` aggregated turn diff. `A` | v16 can show file changes/diffs but presentation is event-oriented. | Use compact changed-file summaries + on-demand aggregate diff. | `POTENTIAL_SIMPLIFICATION` | Verify local diff notification and behavior. |
| Persisted history read | `thread/read`, `thread/turns/list`, `thread/items/list` read without resume. `A` | ADS uses `thread/read` for non-owning bind and persisted inspection. | Upstream now has richer read-only history that may simplify transcript reconstruction. | `ADS_ALREADY_SOLVES` / `POTENTIAL_IMPROVEMENT` | Verify local paginated APIs. |
| Writer ownership | Current docs state one App Server process can own a paginated thread for writing while read-only requests remain available. `A` | ADS experimentally separates durable identity/read from actual writer reacquisition. | Strong alignment with ADS design. | `KEEP_ADS` | High for paginated main; retain local experimental evidence for exact runtime/legacy cases. |
| Subscription vs persistence | Connection-scoped `thread/unsubscribe`, status changes, delayed unload. `A` | ADS previously inferred several process/subscription boundaries experimentally. | Gives a clearer supported lifecycle model; may help viewer/handoff design. | `POTENTIAL_IMPROVEMENT` | Verify local 0.152.1 behavior in disposable thread. |
| Native cross-client live sync | Community reports still describe independent clients/processes not live-syncing automatically. `F`; ADS observed same. `G` | Desktop deeplink can read persisted state but did not live-update a Codexless-owned active turn. | Current companion viewer remains justified unless shared-runtime spectator path is proven. | `KNOWN_UPSTREAM_LIMITATION` / `KEEP_ADS` | Need source/maintainer-level confirmation of intended multi-client model. |
| Archive/unarchive Desktop UI | Multiple issue reports show backend success with stale Desktop path/UI/resume behavior. `F`; ADS saw stale post-reacquisition presentation. `G` | ADS classifies its observed stale state as Desktop presentation/cache quirk, not backend failure. | External corroboration, not proof of identical root cause. | `KNOWN_UPSTREAM_LIMITATION` | Continue monitoring fixes/linked PRs. |
| Same-turn steering | Experimental `turn/steer` with exact expectedTurnId. `A`; public Codexless PR #6 proposes a fail-closed surface. `E` | ADS currently has next-turn `agent_send`, stop, and supervision, but no same-turn steering. | Could materially improve supervision of long tasks. | `POTENTIAL_IMPROVEMENT` / `INVESTIGATE` | Verify local method and develop no-replay/idempotency contract before adoption. |
| Persistent follow-up queue | Experimental thread queue persists FIFO follow-up turns. `A` | Next-step intent currently remains mostly in calling Chat session until another send. | Potential reliability improvement for planned follow-ups, but metered consent/user intent semantics are unresolved. | `INVESTIGATE` | Need persistence/restart/approval experiments. |
| Live settings updates | Experimental exact-turn reviewer/model setting patch; no silent retarget. `A` | ADS Call Profile is ChatGPT-side policy and model choice is explicit per turn. | Lower-level complement, not Call Profile replacement. | `MONITOR` / `INVESTIGATE` | Determine exact local support and correctness constraints. |
| Call Profile | No direct upstream equivalent to ADS's full ChatGPT-side call/supervision policy found in this first pass. | Durable local profile controls call approval, sizing, supervision, model/effort strategy, pending-action handling, verification. | Remains useful even if App Server reviewer routing expands. | `KEEP_ADS` | Revisit after deeper public Codexless/Guardian study. |
| approvalsReviewer / auto_review | App Server can route in-turn approvals to user or automatic risk-review subagent; managed/app-specific rules exist. `A` | ADS normally applies Call Profile + user/ChatGPT supervision around Codex pending approvals. | Potential complement or future reviewer option, but different policy layer. | `INVESTIGATE` | Deep Guardian/approval-source study required. |
| Approval UI identity | Requests include thread/turn/item identity and available decisions. `A` | Rich Card can surface pending approval state; earlier cleanup approval exposed outer OpenAI dispatch mismatch. | More semantic item-driven approval UI is possible; outer ChatGPT safety remains separate. | `POTENTIAL_IMPROVEMENT` | Map exact local approval request types/available decisions. |
| Multi-agent lineage | Parent/ancestor thread IDs, agent nickname/role, parent-owned child restrictions. Ultra drives proactive multi-agent behavior. `A` | ADS currently supervises root Codex agent tasks; viewer has some subagent event coverage but no full tree model. | Future supervision/viewer may need thread-tree semantics. | `INVESTIGATE` / `MONITOR` | Map local subagent lifecycle before custom design. |
| MCP extension profile | Fixed when session is start/resume/forked; inherited by subagents. `A` | ADS must restart/reconnect/refresh infrastructure after MCP/Rich Card changes to avoid stale host resources. | May explain some capability/resource lifetime behavior; needs ChatGPT-host-specific study. | `INVESTIGATE` | Dedicated MCP App/resource lifecycle research. |
| Broad App Server process APIs | Current main exposes unsandboxed process APIs and absolute-path filesystem utilities. `A` | ADS deliberately withholds broad public process authority and uses bounded Codex authority/semantic tools. | Upstream availability is not a reason to broaden public ChatGPT authority. | `KEEP_ADS` | High; continue least-authority design. |
| App Server daemon/local control path | Current main documents daemon and local control transports including protected Windows socket DACL. `A` | Codexless currently owns its own App Server lifecycle. | Possible future simplification if stable and compatible. | `MONITOR` / `POTENTIAL_SIMPLIFICATION` | Track stability/support status; do not adopt experimental transports prematurely. |
| Long-thread pagination | Current main supports paginated history, but community reports protocol drift and large recent-turn bootstrap slowness. `A/F` | ADS relies on durable long threads for handoff and continuity. | Compatibility/version probes and lazy transcript detail are important. | `POTENTIAL_IMPROVEMENT` / `MONITOR` | Study issues #41512, #38653 and linked fixes/source. |
| Public Codexless same-turn steering | Open PR #6 proposes exact-turn, idempotent, no-replay steering and notes current Agent lane gap. `E` | ADS local fork has no same-turn steering yet. | Independent convergence on same opportunity and safety constraints. | `MONITOR` / `INVESTIGATE` | Track maintainer disposition and compare implementation to local architecture. |
| Public Codexless native progress | Open PR #5 exists for bounded native agent progress. `E` | ADS built a richer app-only live activity projection for v16. | Could overlap or simplify public progress plumbing; needs source-level comparison. | `MORE_EVIDENCE_REQUIRED` | Deep-read PR #5 and base/current code. |
| Public Codexless lifecycle kernels | Open PR #2 proposes Browser/Agent lifecycle consolidation. `E` | ADS local fork has accumulated handoff/live-viewer lifecycle state and guards. | Potential upstream simplification or conflict with local divergence. | `MORE_EVIDENCE_REQUIRED` | Deep-read PR #2 and tests. |
| Public Codexless Browser elicitation | Open PR #4 treats semantic recognition separately from approval policy. `E/D` | ADS Browser path uses dynamic confirmation policy and prepared exact actions. | Principle strongly aligns with ADS: known request shape is not approval evidence. | `KEEP_ADS` / `MONITOR` | Verify final upstream merge/disposition. |

## Research notes

This file intentionally stays concise. When a row requires more than a bounded summary, open a numbered research record and link it here rather than turning the matrix into an unreviewable wall of text.

Current deep records:

```text
docs/research/113_codex_codexless_upstream_ecosystem_architecture_research_program.md
docs/research/114_current_codex_app_server_architecture_and_ads_implications.md
```

Planned next records:

```text
public Codexless upstream baseline and ADS-local delta
OpenAI Codex issue/PR/discussion topic clusters
exact local Codex 0.152.1 schema/capability verification
MCP Apps/resource lifecycle and ChatGPT host integration
approval/Guardian comparison
steering/queue supervision design
multi-agent/subagent lifecycle
```
