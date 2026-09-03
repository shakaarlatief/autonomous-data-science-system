# Research 115: Public Codexless Current Architecture, PR Landscape, and ADS Delta

**Date:** 2026-09-03  
**Status:** ACTIVE BASELINE / PUBLIC CODEXLESS LANDSCAPE MAPPED  
**Scope:** Maps the current public Codexless project, its active design direction, and the most relevant open pull requests against the ADS-local Codexless architecture. This is not an upstream merge recommendation.  
**Authority:** Research evidence only. Open pull requests remain proposals until merged/published; maintainer comments indicate direction but are not a released contract.  
**Declared references:** `research:113`, `research:114`, `checkpoint:276`, `path:docs/research/CODEX_UPSTREAM_ADS_COMPARISON_MATRIX.md`, `path:docs/local_execution/OPERATIONS.md`

## 1. Why public Codexless must be studied separately

ADS did not invent the underlying Codexless concept from scratch. The public Codexless project is the origin/reference architecture for the two-lane idea:

```text
ChatGPT conversation as orchestrator
    |
    +-- model-free local Codex-backed tools for bounded work
    |
    +-- explicit formal Codex Agent escalation when model work is warranted
```

The public project is actively changing while ADS has also evolved a significant local variant. Treating the public repository as static would be incorrect. Current open PRs and maintainer comments show ongoing work in exactly the areas ADS has encountered: Agent lifecycle, task state, Browser lifecycle, same-turn steering, progress observability, approval semantics, and no-replay recovery.

Primary public surfaces:

```text
https://github.com/liyana31811/Codexless
https://github.com/liyana31811/Codexless/pulls
https://github.com/openai/codex/discussions/38868
```

## 2. Original public product philosophy remains aligned with ADS

The OpenAI Codex Discussion introducing Codexless describes two lanes in one ChatGPT conversation:

```text
1. model-free local tool work
2. explicit Codex escalation
```

It emphasizes:

```text
narrow local capabilities
no second Codex runtime
no quota-bypass claim
read-first Browser posture
human-visible Codex escalation/consent
```

This high-level philosophy remains strongly aligned with ADS. ADS has extended it with more rigorous project authority, Call Profile policy, direct-Git semantic tools, durable thread handoff, Rich Task Cards, restart/recovery evidence, and the v16 live-viewer work.

Classification: `KEEP_ADS / UPSTREAM-ALIGNED`.

## 3. Public repository surface is moving faster than README counts

The public repository currently shows 0 Issues and 4 open pull requests. The public README/discussion material can lag the active code baseline. In particular, PR #6 states that its base already exposes 42 tools while README/SECURITY still describe 39; the proposed steering tool would make 43 total / 40 model-visible.

This is not merely a documentation nuisance. It means ADS research must identify:

```text
published release contract
current main source contract
open-PR base contract
ADS-local contract
```

as distinct states.

A raw tool count cannot be used as a proxy for architectural equivalence.

Classification: `MORE_EVIDENCE_REQUIRED` whenever documentation and code-base claims diverge.

## 4. PR #2: lifecycle-state consolidation behind fixed kernels

Open PR:

```text
https://github.com/liyana31811/Codexless/pull/2
```

Evidence class:

```text
E  OPEN_PROPOSAL
D  MAINTAINER_STATEMENT for maintainer comments
```

### 4.1 Proposed Browser architecture

The PR proposes a fixed Browser operation kernel with a closed set of named actions, centralizing:

```text
prepared-reference claiming
action-kind validation
Workbench generation/provider/tab/URL validation
dispatch
receipt
finalization
```

It preserves claim-before-await and no-blind-replay semantics. Callers still cannot provide arbitrary selectors, coordinates, JavaScript, provider IDs, arbitrary keys or new operation types.

### 4.2 Proposed Agent architecture

The PR proposes one canonical Agent task ledger owning:

```text
task identity
consent state
request indexes
cards
persistence
terminal snapshots
```

Important stated invariants include:

```text
consentRef is task identity, not permission evidence
Rich Card commit token is a separate server-bound approval capability
replaying consentRef/requestId cannot authorize a metered turn
non-terminal persisted task recovers as lost after restart, never replayed
first terminal snapshot wins
stale prior-turn notifications/approvals cannot affect later turn
acceptance-unknown work is not blindly replayed
```

These principles are very close to the reliability discipline ADS has independently reinforced through guided handoff, fresh agent bindings, task refs, no-replay behavior, and exact-turn checks.

### 4.3 Maintainer disposition is more important than the module shape

The maintainer later stated that the PR had already influenced current Browser lifecycle work and Agent safety invariants, but did not want to wholesale-port the old module shape because current Task Card/Profile/Agent lifecycle code had moved substantially.

This is a significant research signal:

```text
semantic lessons           actively valuable
exact old implementation   probably stale relative to newer main
```

ADS should therefore compare invariants and current-base behavior, not copy PR #2's module structure.

### ADS implications

Potential opportunities:

```text
canonicalize local task state ownership
reduce duplicate lifecycle state
make first-terminal-wins explicit everywhere
strengthen stale-event rejection
make uncertain dispatch/receipt states first-class
retain release-byte/version identity discipline
```

But the ADS local variant already includes newer Task Card/Profile/handoff/live-viewer work. A broad refactor before the upstream/current-local delta is mapped would be premature.

Classification: `POTENTIAL_SIMPLIFICATION / INVESTIGATE`.

## 5. PR #6: fail-closed same-turn steering

Open PR:

```text
https://github.com/liyana31811/Codexless/pull/6
```

The proposed `codex.agent_steer` wraps official App Server `turn/steer` with explicit safety/reliability constraints:

```text
exact active expectedTurnId
caller-stable requestId
confirmed duplicates do not dispatch twice
same requestId + different payload is rejected
explicit RPC rejection != transport uncertainty
uncertain acceptance is never replayed automatically
pending approval / terminal / stale turns reject steer
steer cannot change model, effort, cwd, sandbox, permission profile or output schema
correlated userMessage clientId acts as a consumption receipt
```

The author reports a live Codex 0.147.0 qualification with the same turn/request ID correlated through dispatch, acceptance and consumption.

The maintainer explicitly states that same-turn steering is a real gap in current Codexless: existing Agent supervision can observe a running turn, but an ordinary follow-up waits until idle and starts another turn. The direction is accepted, but the patch must be reconciled against the newer Agent architecture first.

### ADS implications

This is one of the most promising new capabilities for ADS because our Call Profile explicitly says ChatGPT should remain responsible for running Codex work. Today that supervision can inspect, approve, interrupt, stop or later continue, but it cannot naturally say:

```text
keep this same turn running, but change focus now
```

A safe steering surface could materially improve long-running Codex work.

However, OpenAI Codex issue #32254 reports a current idempotency gap for retries of `turn/steer` by `clientUserMessageId`. This reinforces the PR's no-replay/consumption-receipt concerns rather than eliminating them.

Therefore:

```text
same-turn steering concept      HIGH-VALUE INVESTIGATE
blind raw turn/steer exposure   REJECT
fail-closed wrapper             PROMISING DESIGN
```

No local implementation yet.

## 6. PR #4: Browser elicitation and the distinction between recognition and approval

Open PR:

```text
https://github.com/liyana31811/Codexless/pull/4
```

The PR correctly identified several seams:

```text
Streamable HTTP session continuity for elicitation continuation
current/legacy App Server request-shape normalization
exact recognition of browser-use/access_browser_origin
Browser-lane-specific runtime wiring
```

The original PR proposed automatic website-origin acceptance for the recognized request shape.

The maintainer explicitly rejected that product-policy part while accepting the core diagnosis/plumbing. The maintained direction is:

```text
recognize exact semantic request
    !=
automatically approve it

recognition
    -> dynamic Browser confirmation policy
    -> decision
```

### ADS implication

This is a strong validation of ADS's current Browser policy philosophy. Prepared references and exact action recognition bind an action, but do not themselves constitute user approval. The actual decision is derived from the current task context and Browser confirmation policy.

This should remain a system-wide architectural principle:

```text
IDENTITY / CLASSIFICATION != AUTHORIZATION
```

That same principle applies beyond Browser to:

```text
Codex task refs
consent refs
approval request IDs
thread IDs
prepared Git semantics
future steering receipts
```

Classification: `KEEP_ADS / MAINTAINER-ALIGNED`.

## 7. PR #5: bounded native Agent progress

The open pull-request list identifies PR #5 as work on bounded native Agent progress through `agent_show`. The GitHub page was not reliably retrievable in this research pass, so its detailed claims are intentionally **not** treated as established.

This is important because ADS v16 independently built a richer app-only live activity projection. PR #5 may overlap with:

```text
progress visibility
event-tail bounding
public vs app-only projection
Agent supervision
```

Classification: `MORE_EVIDENCE_REQUIRED`.

Next action: retrieve PR #5 through a reliable source path or inspect its branch/source diff before drawing conclusions.

## 8. Public Codexless and ADS-local architecture are no longer equivalent

The ADS-local system currently includes work beyond the original public preview concept, including:

```text
Codex Call Profile with recurring natural-language supervision policy
48-tool local/public surface state at v16 publication
semantic bounded direct Git fetch/pull
agent bind / thread unarchive / guided Proceed in Chat
server-owned Ready taskRef resolution
repeatable same-thread Desktop <-> Chat continuation
Open in Codex Desktop while running
v16 app-only live Rich Task Card event projection
specific restart/tunnel/plugin-refresh operational discipline
ADS repository authority/continuity integration
```

Therefore the correct research question is not:

> Should ADS return to upstream Codexless?

It is:

> Which newer public/upstream Codexless mechanisms or invariants should ADS adopt, which local additions should remain, and where can divergence be reduced without losing verified behavior?

## 9. Architectural principles already converging across public Codexless and ADS

The strongest common principles so far are:

```text
least-authority public surfaces
semantic wrappers instead of arbitrary raw capability
exact target identity
claim/consume before uncertain dispatch where appropriate
no automatic replay after uncertain side effect
idempotent request identity where possible
server-bound approval capability separate from task identity
stale observation rejection
first terminal state wins
explicit release/version identity
current policy determines authorization
Browser and Agent lifecycle state need a small number of canonical owners
```

This convergence suggests ADS's safety/reliability direction is not an isolated local preference.

## 10. Important difference: ADS has experimentally gone further on cross-client thread handoff

The current public PR landscape studied here does not yet show an equivalent of ADS's full tested sequence:

```text
Desktop persisted thread
-> cooperative archive/release
-> model-free unarchive
-> model-free non-owning bind / Ready resolution
-> normal metered same-thread continuation in Chat
-> repeat cycle on same durable thread
```

Nor does it yet eliminate the native Desktop live-sync limitation that motivated the companion viewer.

Therefore these ADS mechanisms should remain preserved while upstream thread ownership/synchronization is studied.

Classification: `KEEP_ADS / MONITOR UPSTREAM`.

## 11. Public maintenance style itself contains useful engineering lessons

The maintainer comments reveal a disciplined approach worth preserving in ADS:

```text
do not rebase a large old-base PR blindly against a moving architecture
separate semantic lessons from stale module shape
absorb small current-shape slices after review
preserve attribution
never publish different bytes under the same release version
require platform/live-host qualification where host behavior matters
be explicit about baseline failures rather than claiming full green
```

These are directly compatible with the ADS Development Method and should influence future Codexless upgrades.

## 12. Immediate ADS disposition

At this stage:

```text
KEEP
    two-lane Codexless philosophy
    Call Profile
    bounded semantic tool surfaces
    current Browser confirmation-policy separation
    durable thread/handoff evidence
    v16 as frozen working baseline

INVESTIGATE
    same-turn steering
    canonical Agent lifecycle ledger/state ownership
    public native progress work
    current public Browser lifecycle composition

DO NOT DO YET
    broad merge from public main
    PR #2 wholesale port
    raw turn/steer exposure
    unconditional origin auto-approval
    v17 renderer implementation before exact local/upstream semantic comparison
```

## 13. Next public-Codexless research

The next pass should establish the exact current public `main` source baseline and diff it conceptually against ADS-local v16, including:

```text
agent-card-ui.mjs
agent-tools.mjs
codex-agent-executor.mjs
codex-app-server-client.mjs
call-profile/task state modules
Browser lifecycle modules
surface-contracts.mjs
public registration/tests
release manifest/versioning
```

Then inspect PR #5 and any newly merged PRs against that baseline.

The goal is not a line-by-line merge plan yet. The goal is to identify where ADS is carrying unique value versus unnecessary divergence.
