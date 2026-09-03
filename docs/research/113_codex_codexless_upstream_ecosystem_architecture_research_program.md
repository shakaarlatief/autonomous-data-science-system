# Research 113: Codex and Codexless Upstream Ecosystem Architecture Research Program

**Date:** 2026-09-03  
**Status:** ACTIVE / COMPREHENSIVE UPSTREAM RESEARCH OPENED  
**Scope:** Establishes a broad evidence-driven research program over the current OpenAI Codex/App Server ecosystem, the public Codexless project, relevant issues, pull requests, discussions, and ADS's own experimentally verified local-execution architecture before further live-viewer or Codexless architecture work.  
**Authority:** Active bounded research program. It may identify candidates, risks, replacements, and monitoring targets, but it does not by itself supersede accepted ADS contracts or authorize implementation changes.  
**Declared references:** `research:105`, `research:109`, `research:110`, `research:111`, `research:112`, `checkpoint:275`, `path:docs/local_execution/OPERATIONS.md`, `path:docs/model_collaboration/README.md`

## 1. Why this research phase exists

ADS has spent substantial development effort on Codexless because local execution, explicit Codex escalation, task supervision, Desktop handoff, durable thread identity, bounded Git synchronization, approvals, and live task observability materially improve the development workflow for the larger ADS project.

The work is no longer a small transport experiment. It has become a substantial Level-2 engineering subsystem with durable operational procedures, permission/authority boundaries, failure-recovery knowledge, Desktop integration, Rich Task Cards, model-call governance, and experimentally verified cross-client behavior.

At the same time, the upstream ecosystem is moving rapidly. The official `openai/codex` repository has a large and active issue/PR/discussion surface, and the public Codexless repository is receiving proposals that overlap directly with problems ADS encountered independently. Continuing to extend the local implementation without first reassessing current upstream capabilities risks duplicating solved mechanisms, preserving obsolete assumptions, or missing stronger designs.

The project owner therefore explicitly pauses immediate v17 viewer implementation and reviewed Source Vault ingestion while this research program is active.

## 2. Current ADS baseline to compare against

The research must compare upstream findings against actual ADS evidence, not an imagined baseline.

Current verified ADS/Codexless capabilities include:

```text
model-free local project reads / controlled writes / commands
bounded permission-profile resolution and read-only downscope
bounded semantic Git fetch
bounded strict-fast-forward Git pull
Codex Call Profile with explicit metered-call consent
Rich Task Card lifecycle
early Open in Codex Desktop
durable persisted threadId as cross-client identity
model-free bind after restart
cooperative Desktop archive -> unarchive -> rebind -> resume
guided Proceed in Chat
repeatable same-thread Desktop/Chat round trips
v16 live Rich Task Card event transport and auto-refresh
```

Important verified limitations or open design questions include:

```text
native Codex Desktop does not live-refresh another App Server client's running turn
Desktop can retain stale archive/presentation state after backend changes
v16 live viewer is functionally live but visually behaves too much like an event log
raw event flattening loses the narrative/item hierarchy seen in Codex Desktop
Checkpoint 275 remains uncommitted because its originating cleanup/finalization turn was interrupted
```

The `.tmp/pytest-checkpoint-275/` residue remains known interruption residue and is not part of this research program's mutation scope.

## 3. v16 is frozen as the working experimental viewer baseline

The v16 viewer was successfully published to the live Codexless installation and validated after the correct restart, tunnel reconnect, ChatGPT plug-in refresh, and fresh disposable-chat sequence.

Verified publication identity:

```text
Rich Card resource
    ui://toolwire/codex-task-card-v16.html

public version
    0.1.1-preview.7

tool count
    48

agent-card-ui.mjs
    26F8654BE93D6AFDAAA94C1FEB206ACD59C05948974DACA5E50495F11C4327DB

surface-contracts.mjs
    73FCD65D5207B95617865AE0DB972ACA5F0888D64F03D2FC14A9CE09D29FBBA8

agent-tools.mjs
    C515873F58D76AE29661FF88AC353BCBF95A7D6BB0BE10946DD0DBAEC71211D2

codex-agent-executor.mjs
    255BAD09DBCFD11AA5CB66305073EF0ADD22B5D543103F77AD87B5351F568C9E
```

The disposable live test established:

```text
live transport / polling                  PASS
automatic RUNNING-card updates            PASS
streamed command output                   PASS
terminal transition                       PASS
broad user-visible event coverage         PRESENT
Desktop-style semantic grouping           NOT YET PASS
Desktop-style narrative hierarchy         NOT YET PASS
```

A separate native Codex Desktop recording established the presentation target. Desktop presents one evolving conversational work narrative with compact semantic actions, rather than a flat event log. Commands evolve in place; file reads are compact; file edits have change summaries and reviewable diffs; running shell output is attached to the relevant command; approvals become prominent decision surfaces; ordinary user-visible reasoning/progress appears as prose.

No v17 implementation is authorized merely by this observation. The next renderer architecture should be designed only after the upstream semantic model is understood.

## 4. Evidence hierarchy for this research

Every material finding should be classified so an active issue or community anecdote is not mistaken for an official contract.

```text
A  OFFICIAL_DOCUMENTATION
   maintained OpenAI documentation / App Server protocol documentation

B  OFFICIAL_SOURCE
   released/current OpenAI Codex source, generated schemas, tests

C  MERGED_UPSTREAM_CHANGE
   merged OpenAI or Codexless PR/commit with inspectable implementation

D  MAINTAINER_STATEMENT
   maintainer explanation in issue/PR/discussion

E  OPEN_PROPOSAL
   open PR, design draft, unmerged branch

F  COMMUNITY_OBSERVATION
   issue/discussion reproduction or user report

G  ADS_EXPERIMENT
   locally reproduced and preserved ADS evidence

H  INFERENCE
   reasoned architectural conclusion not itself an upstream fact
```

Where claims conflict, stronger and version-matched evidence outranks weaker evidence. Recency and exact version matter.

## 5. Research workstreams

The investigation is intentionally broader than the live viewer.

### 5.1 Official App Server model

Study the current implementation and schemas for:

```text
Thread / Turn / Item lifecycle
thread start / resume / fork / read / list
subscriptions / unsubscribe / close / status
turn start / interrupt / steer
thread queue
turn and thread settings
reasoning summaries
plans
agent messages
command execution and parsed command actions
command output streaming
file changes and aggregated diffs
MCP tool calls and app metadata
approvals / permissions / Guardian / auto-review
subagents / parent-child lineage / multi-agent behavior
review mode
compaction
history pagination
projects / sections / goals / memory
background terminals / realtime
model catalog / service tier / quota surfaces
hooks
MCP extension negotiation
transport lifecycle / overload / reconnect behavior
```

### 5.2 Official Codex Desktop and cross-client behavior

Research source and community evidence around:

```text
same-thread multi-client ownership
cross-client live synchronization
thread resume conflicts
archive / unarchive
Desktop stale presentation/cache
restart recovery
history and pagination compatibility
Windows-specific lifecycle behavior
writer/subscriber semantics
approval servicing from another client
deep links and project/thread navigation
```

### 5.3 Public Codexless baseline

Establish the current public project as an independent moving baseline:

```text
source architecture
public/private tool contracts
Task Card resources
agent lifecycle and supervision
Call Profile
approval handling
Browser lifecycle
permission and authority model
tests
release/install behavior
commits
open and merged PRs
documentation drift relative to source
```

Then compare public upstream Codexless with the ADS-local variant. Do not assume the local implementation should remain divergent.

### 5.4 Issues, PRs, and discussions

Do not read thousands of issues sequentially. Use topic-cluster searches with high recall, then follow strong reports into linked issues, PRs, maintainer comments, releases, and source changes.

Priority clusters:

```text
app-server / protocol
desktop synchronization
threads / persistence / resume
archive / unarchive
approvals / Guardian
MCP / MCP Apps / resources / elicitation
permissions / sandbox / authority
Windows / WSL
history / pagination / compaction / long threads
browser
steering / queue / mid-turn interaction
subagents / multi-agent
progress / observability / task rendering
models / service tiers / quota
updates / version compatibility / migrations
recovery / idempotency / replay safety
security / prompt injection / credential boundaries
```

Closed issues are evidence too: they can reveal fixes and changed assumptions.

### 5.5 Community design discovery

Actively search for ideas ADS has not yet considered. The research should not merely confirm the current architecture.

Potential examples include:

```text
same-turn steering
queued follow-ups
shared or spectator clients
different task supervision models
native progress projection
lifecycle-state kernels
alternative approval routing
automatic review
thread goals / durable projects
multi-agent supervision
better recovery and no-replay semantics
alternative Rich Card/MCP App architectures
```

## 6. Initial primary-source findings

These findings are preliminary and establish why the research is worthwhile. They are not yet architecture decisions.

### F1. App Server explicitly models semantic Item lifecycles

Current official App Server documentation defines `Thread -> Turn -> Item` as the core interaction model. A turn streams `item/started`, item-specific deltas, and `item/completed`.

This strongly supports replacing v16's flattened event-log rendering with a semantic-item projection if later implementation evidence confirms the relevant IDs/statuses are stable for the ADS runtime.

Source:
`https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md`

Evidence class: `A / OFFICIAL_DOCUMENTATION`.

### F2. App Server exposes richer history without resuming

Current documentation includes `thread/read`, `thread/turns/list`, and `thread/items/list` for persisted history without resuming the thread. `thread/start`, `thread/resume`, and `thread/fork` automatically subscribe the connection to turn/item events.

This must be compared against ADS's existing read/bind/resume assumptions and could simplify future transcript reconstruction.

Evidence class: `A / OFFICIAL_DOCUMENTATION`.

### F3. App Server now exposes thread status and explicit unsubscribe/unload behavior

`thread/status/changed` exists. `thread/unsubscribe` is connection-scoped; when the last subscriber leaves, the thread remains loaded until an idle unload delay before closing.

This is directly relevant to writer/subscriber lifecycle, spectator behavior, and the distinction ADS previously had to infer experimentally.

Evidence class: `A / OFFICIAL_DOCUMENTATION`.

### F4. Same-turn steering and persistent queued turns now exist experimentally

The current App Server documents experimental `turn/steer` and `thread/queue/*` APIs. `turn/steer` can add user input to an already-running regular turn when the expected active turn matches; queue APIs persist follow-up turns for later FIFO submission.

These capabilities may materially affect the current Codexless supervision architecture and should be compared with `agent_send`, waiting-time supervision, and future interactive controls rather than added blindly.

Evidence class: `A / OFFICIAL_DOCUMENTATION`.

### F5. Command and file-change rendering can be item-driven

Current App Server documentation gives structured command/file lifecycle events, including command output deltas, final command state, file-change items, and turn-level diff updates.

This aligns with the native Desktop recording and suggests that v17 should not manually reconstruct semantics from unrelated display rows if the authoritative item structure is available.

Evidence class: `A / OFFICIAL_DOCUMENTATION` plus `G / ADS_EXPERIMENT` for the Desktop/v16 comparison.

### F6. Approval routing has evolved beyond a single user-review path

The current App Server surface supports an approvals reviewer and includes an `auto_review` path associated with risk review. This does not automatically replace ADS's Call Profile or human approval policy, because those govern a different ChatGPT-side supervision layer, but it creates a serious comparison question.

Evidence class: `A / OFFICIAL_DOCUMENTATION`.

### F7. Public Codexless development is independently converging on ADS problem areas

The public Codexless repository currently has active PRs around:

```text
same-turn steering
bounded native agent progress
Browser origin elicitation
Browser/Agent lifecycle-state consolidation
```

The same-turn steering PR explicitly frames lack of in-turn steering as a current Agent-lane gap and emphasizes exact current-turn identity, request idempotency, no replay after uncertainty, and authority preservation.

Sources:
`https://github.com/liyana31811/Codexless/pulls`
`https://github.com/liyana31811/Codexless/pull/6`
`https://github.com/liyana31811/Codexless/pull/4`
`https://github.com/liyana31811/Codexless/pull/2`

Evidence class: `E / OPEN_PROPOSAL`, with maintainer comments classified separately where used.

### F8. Public documentation can lag the implementation

The public Codexless README describes a 39-tool contract while current PR discussion refers to a newer code baseline with a larger surface. Therefore this research must inspect source/tests/current PR bases rather than treating README counts as sufficient live-version evidence.

Evidence class: `E / OPEN_PROPOSAL` plus repository documentation observation.

## 7. ADS comparison matrix

The research should maintain a living matrix with at least:

```text
area
upstream official behavior
public Codexless behavior
ADS-local behavior
evidence class + exact source/version/date
difference
risk/opportunity
candidate action
classification
confidence
revisit trigger
```

Allowed action classifications:

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

No architecture should change solely because upstream has a feature. ADS must compare authority, reliability, UX, backward compatibility, failure modes, and the project's actual needs.

## 8. Questions that can change the current architecture

The study must explicitly answer:

1. Which custom ADS mechanisms now duplicate supported upstream capabilities?
2. Which custom mechanisms remain necessary because ChatGPT, Desktop, Codexless, or App Server still expose a real gap?
3. Can the live viewer become a direct semantic Item projection instead of a custom display-event pipeline?
4. Can current thread supervision use `turn/steer` or queues safely, and where should ordinary `agent_send` remain the correct boundary?
5. Does current App Server lifecycle support a better cross-client spectator architecture than the one already tested?
6. Which parts of Proceed in Chat remain valuable if upstream thread ownership/synchronization changes?
7. Should the Call Profile remain ChatGPT-side policy, integrate with App Server reviewer settings, or stay deliberately separate?
8. Can progress and task state be simplified using upstream Agent/Codexless changes?
9. Are there public Codexless improvements we should upstream-adopt instead of maintaining local divergence?
10. What new risks appear from project APIs, memory, goals, queues, subagents, remote environments, Browser integration, or MCP Apps?
11. Which current ADS assumptions are version-sensitive and therefore need explicit compatibility probes?
12. What should become a monitored upstream dependency rather than a custom implementation?

## 9. Claude collaboration

A new collaboration thread should run in parallel with this program, with full disclosure of the current ADS state. It is not a blind-to-candidate exercise.

Claude should independently search the same public ecosystem, challenge this research taxonomy, find important sources or ideas ChatGPT misses, and produce a separate evidence-classified architecture report. ChatGPT research may proceed concurrently. Claude's result should be considered before a final architecture reconciliation or major replacement decision when practical.

The obsolete MC-0009 Git-feasibility research thread has been retired by explicit project-owner decision. Its question was already resolved experimentally and should not remain a live Claude obligation.

## 10. Preservation plan

This program should produce durable knowledge rather than a browser-history dump.

Expected durable outputs include:

```text
this research program / methodology
topic-specific research records when a cluster becomes substantial
a maintained upstream-vs-ADS comparison matrix
important issue/PR/discussion source references
a final architecture disposition
a later Codexless documentation/repository audit
a checkpoint when the research materially changes or closes the active boundary
```

Raw issue volume is not a success metric. The goal is high-quality evidence and reusable architectural knowledge.

## 11. Current stop rule

Do not implement v17, replace a lifecycle mechanism, widen permissions, or adopt an upstream experimental API merely because it is interesting.

Implementation resumes only after enough evidence exists to state:

```text
what the current upstream mechanism actually guarantees
what ADS currently does
why changing ADS is materially better
what failure modes are introduced
how the change will be tested
what remains intentionally custom
```

## 12. Exact next research action

Continue the upstream survey in parallel across:

```text
official App Server docs/source/schema/tests
openai/codex issue/PR/discussion clusters
public Codexless source/tests/history/PRs
ADS-local Codexless deltas and validation history
```

Populate the comparison matrix and open narrower research records when a topic produces enough durable findings to justify one.

Source Vault ingestion remains preserved but paused during this project-owner-selected Level-2 research phase.
