# Research 035: Multi-Model Development Collaboration Architecture

**Date:** 2026-08-25  
**Status:** Candidate Level-2 development-method research for independent cross-model review  
**Maturity:** Strong design proposal; not yet canonical development method  
**Scope:** How ChatGPT, Claude, the human project owner, Git/GitHub, and future optional API orchestration should collaborate while developing ADS itself  
**Authority:** Research proposal only. `docs/DEVELOPMENT_METHOD.md`, `docs/CONTINUITY.md`, current repository governance, and accepted project decisions remain authoritative until this proposal is reviewed and explicitly promoted.  
**Origin:** User request to make multi-model collaboration a deliberate professional development architecture rather than informal model switching.

## 1. Why this is a Level-2 architecture problem

The Autonomous Data Science System is being built through a development method that is itself intentionally evolving.

Adding a second strong model is not merely adding another tool. It changes:

```text
who may reason about the project
who may write project state
how independent review is obtained
how disagreement is represented
how continuation provenance is recorded
how branches are owned
how reviews are transferred
how humans arbitrate
how duplicated work is avoided
how consensus pressure is controlled
how future automated orchestration might be justified
```

The existing repository already solves a large part of the information-continuity problem. A new model can reconstruct project state from durable repository artifacts instead of requiring another model's conversation transcript.

However:

```text
shared repository state
    !=
safe multi-model collaboration protocol
```

A repository alone does not prevent concurrent conceptual ownership, contradictory canonical updates, review anchoring, sycophantic agreement, duplicated work, or ambiguous responsibility.

Therefore multi-model development should be designed as an explicit Level-2 subsystem before it becomes routine.

---

## 2. Current facts and constraints

### 2.1 Repository authority already scales across models

The existing continuity principle is strong:

> Repository artifacts, not prior chat memory, are the durable source of truth.

This naturally generalizes from ChatGPT-session continuity to model-to-model continuity.

A collaborator should reconstruct from:

```text
README.md
CURRENT_STATE.md
KNOWLEDGE_MAP.md
current_routing.json
accepted foundations
current research/specifications
checkpoints
DECISIONS.md
DEVELOPMENT_METHOD.md
CONTINUITY.md
Git history
active PR state
relevant tests/results
```

A full raw conversation transfer should normally be unnecessary.

### 2.2 Current checkpoint provenance is ChatGPT-specific

The current checkpoint contract requires:

```text
Design session
ChatGPT project
Session title
```

The contract already says it should be deliberately revised if development moves outside ChatGPT.

A genuine multi-model process therefore creates a real pressure point: future provenance should represent the interaction environment and collaborator without erasing historical ChatGPT-specific metadata.

This should be changed only after the collaboration architecture itself survives review.

### 2.3 Product subscriptions and APIs are economically different modes

The initial collaboration mode should exploit the user's existing interactive ChatGPT and Claude subscriptions.

Programmatic API orchestration is technically possible later, but it introduces separately metered usage, repeated context transmission, orchestration code, provider integration, operational failure modes, and potentially substantial token cost.

Exact provider prices are intentionally not frozen into this architecture.

### 2.4 The human project owner remains a real participant

The goal is not to hide the human behind an artificial agent hierarchy.

The human owns project intent and remains the ultimate authority for unresolved normative choices, scope, risk tolerance, resource commitments, and whether a major project direction is actually desired.

---

## 3. Design goals

The collaboration architecture should optimize for the following jointly rather than maximizing model activity.

### G1. Repository coherence

At any moment there should be an unambiguous current project state and an auditable path from proposal to acceptance.

### G2. Genuine epistemic diversity

A second model should create independent pressure, not merely restate or endorse the first model.

### G3. Explicit responsibility

For a bounded task, it should be clear who owns implementation/writes, who reviews, who decides, and who is merely observing or researching.

### G4. Low coordination burden

The user should not become a permanent copy-paste transport layer.

### G5. Efficient context transfer

Models should reference durable artifacts by path, commit, section, issue, PR, or thread rather than repeatedly transmitting large conversation histories.

### G6. Safe disagreement

Disagreement must remain visible until resolved by evidence, clarified objectives, or human judgment. It must not be averaged away for social smoothness.

### G7. Safe agreement

Agreement should carry evidence that the reviewer actually challenged the proposal. Consensus without challenge is weak evidence.

### G8. Serialized canonical mutation

Two capable models must not independently mutate the same canonical development state without explicit ownership transfer.

### G9. Auditability

A future reader should be able to determine what each collaborator proposed, what another collaborator challenged, and why the project eventually chose its course.

### G10. Incremental automation

API orchestration should be introduced only when observed workflow friction or measured benefit justifies it.

### G11. Provider neutrality

The collaboration model should not depend semantically on a permanent ChatGPT-vs-Claude pairing. Additional or replacement collaborators should fit the same role/provenance model later.

---

## 4. Non-goals

This stage does not attempt to:

```text
build an automated multi-agent orchestrator
make models autonomously merge one another's work
create majority-vote truth
assign one model permanently as architect and another permanently as coder
replace the human project owner
mirror every chat message into Git
force every small task through two-model review
turn GitHub into a real-time chat application
freeze one provider's current API/pricing model
```

The architecture should first prove that structured asynchronous collaboration creates enough benefit to justify its overhead.

---

# 5. Proposed layered collaboration architecture

The candidate architecture has four distinct layers.

```text
LAYER A  PROJECT AUTHORITY
         canonical repository state

LAYER B  MODEL COLLABORATION EXCHANGE
         dedicated asynchronous model-to-model working channel

LAYER C  TASK / PR REVIEW SURFACES
         branch, diff, tests, PR review, issue comments

LAYER D  OPTIONAL AUTOMATION
         future API orchestration only after evidence
```

The layers have different authority.

## 5.1 Layer A: project authority

This remains the existing repository hierarchy.

Examples:

```text
accepted specifications
DECISIONS.md
PRINCIPLES.md
foundations
CURRENT_STATE.md
current routing
promoted implementation
accepted experiment/result evidence
```

Neither ChatGPT nor Claude may make a statement authoritative merely by writing it in a conversation or collaboration thread.

## 5.2 Layer B: Model Collaboration Exchange

Create a dedicated repository area:

```text
docs/model_collaboration/
```

Its purpose is not to become another canonical knowledge layer.

It is a durable asynchronous exchange for:

```text
review requests
independent proposals
critiques
responses
counterarguments
open disagreements
requests for evidence
handoff messages
resolution records
```

This gives models a place to communicate directly through project infrastructure without cluttering `CURRENT_STATE`, research memos, or ordinary checkpoints with conversational traffic.

The exchange is collaboration provenance.

### Candidate structure

```text
docs/model_collaboration/
    README.md
    threads/
        MC-0001/
            BRIEF.md
            THREAD.md
            messages/
                001_...
                002_...
                003_...
            RESOLUTION.md       # only when closed
```

The stable thread identifier is semantic. It should not depend on the GitHub issue or PR number because those are transport-specific.

## 5.3 Layer C: task/PR review surfaces

Code and artifact-specific review should continue to use the surface best suited to it:

```text
PR diffs
inline review comments
CI checks
GitHub issue comments
experiment result artifacts
```

The collaboration exchange should point to these rather than duplicate large diffs or logs.

For general architecture dialogue, an optional GitHub issue can act as a low-friction live transport surface for a collaboration thread. The repository thread remains the durable protocol/summary location.

This separation is deliberate:

```text
transport
    !=
authority
    !=
durable resolution
```

## 5.4 Layer D: optional API orchestration

Future orchestration may invoke multiple provider APIs automatically.

It should be considered only if repository-mediated collaboration shows recurring evidence such as:

```text
high manual handoff cost
repetitive review prompts
repeated missed review opportunities
too-slow cross-model iteration
measurable benefit from automatic adversarial review
need for large repeated benchmark panels
need for machine-triggered conditional reviewers
```

Automation should then be evaluated against:

```text
quality gain
latency
API/token cost
context duplication
engineering complexity
failure modes
observability
privacy/security
human control
```

No API orchestrator is justified merely because two APIs exist.

---

# 6. Task ownership and write authority

The central coordination rule should be stronger than "do not edit at the same time."

## 6.1 One bounded task owner

Every substantive collaboration task has one `TASK_OWNER`.

The task owner is responsible for:

```text
bounded task scope
active implementation/design branch
canonical mutations within that task
checkpoint detection during the task
integrating accepted review changes
keeping the task's repository state coherent
```

The owner may be ChatGPT, Claude, or another future collaborator.

## 6.2 Reviewer does not silently become co-owner

A `REVIEWER` may inspect all relevant repository state and may write review artifacts in the collaboration exchange or review surfaces allowed by the task.

The reviewer should not independently rewrite the owner's branch outside the allowed review surface unless ownership is explicitly transferred or the owner requests a concrete patch.

This prevents asynchronous conceptual races even when Git would technically permit both edits.

## 6.3 Path-scoped review exception

The reviewer may be allowed to add new immutable review messages under the active collaboration thread without obtaining task ownership.

For example:

```text
docs/model_collaboration/threads/MC-0001/messages/
```

This is not authority over the target implementation. It is append-only review provenance.

## 6.4 Ownership transfer

Ownership transfer should be explicit and preserved in the thread or checkpoint:

```text
old owner
new owner
scope transferred
repository head / branch
reason
open obligations
```

The new owner should reconstruct the task from repository state, not from a private summary alone.

---

# 7. Role model

Roles are per task, not permanent identities.

Candidate roles:

```text
TASK_OWNER
    owns bounded task state and integration

INDEPENDENT_REVIEWER
    evaluates the work without write authority over target state

CRITIC
    deliberately searches for failure modes, hidden assumptions, and falsifiers

COUNTER_DESIGNER
    independently proposes an alternative architecture before seeing the proposed solution where useful

RESEARCHER
    gathers external or repository evidence without owning the decision

IMPLEMENTER
    executes a bounded implementation under an accepted contract

VERIFIER
    independently checks claims, tests, provenance, or result interpretation

HUMAN_DECIDER
    resolves project-intent/normative conflicts and authorizes consequential direction where required
```

The same model may occupy different roles on different tasks.

Permanent specialization such as "Claude is reviewer forever" or "ChatGPT is architect forever" should be avoided unless evidence later shows a persistent comparative advantage worth institutionalizing.

---

# 8. Genuine independence and anti-anchoring protocol

The collaboration should not confuse two sequentially conditioned model outputs with independent evidence.

For high-value design questions, use a two-stage review when practical.

## Stage A: independent construction

The reviewer receives:

```text
the problem statement
relevant accepted repository state
constraints
success criteria
```

but not the proposer's detailed solution.

The reviewer records its own preferred architecture, risks, and open questions first.

## Stage B: comparative review

Only after Stage A is durably recorded does the reviewer inspect the proposer's full architecture.

It then compares:

```text
where the designs converge
where they differ
what the proposer noticed that the reviewer missed
what the reviewer noticed that the proposer missed
which disagreements are substantive
which differences are only terminology
what evidence could discriminate alternatives
```

This creates much stronger cross-model evidence than asking:

> "Do you agree with this proposal?"

For lower-risk tasks, a normal direct review may be sufficient.

---

# 9. Anti-sycophancy and anti-contrarianism rules

The goal is neither agreement nor disagreement.

The goal is calibrated judgment.

A reviewer should not receive credit for being supportive, and should not receive credit merely for finding objections.

## 9.1 Requirements when agreeing

If a reviewer substantially agrees, it should still identify:

```text
the strongest plausible failure mode
the strongest alternative considered
what evidence would make it withdraw support
which parts remain weakly supported or provisional
```

## 9.2 Requirements when disagreeing

If a reviewer disagrees, it should identify:

```text
the exact disputed claim or design choice
why the disagreement matters
its alternative
what evidence would make it accept the original proposal
whether disagreement is factual, architectural, normative, or evidence-sufficiency based
```

## 9.3 No forced synthesis

If two high-quality positions remain incompatible, preserve them as an explicit unresolved disagreement.

Do not automatically split the difference.

A hybrid is justified only if it independently satisfies the requirements.

---

# 10. Disagreement taxonomy

A collaboration thread should classify material disagreement where useful.

Candidate classes:

```text
FACT
    disagreement about what is true or what repository/external evidence says

INTERPRETATION
    same evidence, different conclusion

REQUIREMENT
    disagreement about what the system must optimize for

ARCHITECTURE
    different mechanisms for accepted requirements

RISK
    different assessment of failure likelihood/consequence

EVIDENCE_SUFFICIENCY
    disagreement about whether current evidence is enough to advance

NORMATIVE / PROJECT_INTENT
    depends on the human owner's goals/preferences rather than technical truth

SCOPE
    disagreement caused by different assumed task boundaries
```

Classification helps select the resolution mechanism.

For example:

```text
FACT -> inspect source / test
ARCHITECTURE -> compare against requirements / prototype
EVIDENCE_SUFFICIENCY -> predefine stronger gate
PROJECT_INTENT -> human decision
```

---

# 11. Collaboration thread lifecycle

Candidate lifecycle:

```text
OPEN
  -> INDEPENDENT_PASS_REQUESTED
  -> INDEPENDENT_PASS_RECORDED
  -> COMPARATIVE_REVIEW_REQUESTED
  -> COMPARATIVE_REVIEW_RECORDED
  -> RESPONSE / CHALLENGE ROUNDS
  -> RESOLVED | UNRESOLVED | DEFERRED
  -> CLOSED
```

Not every thread needs every state.

A normal direct reviewer task might use:

```text
OPEN -> REVIEW_REQUESTED -> REVIEWED -> RESOLVED -> CLOSED
```

A thread should not remain indefinitely open merely because further discussion is theoretically possible.

Close when:

```text
accepted resolution is promoted
explicit unresolved disagreement is routed elsewhere
the question is deferred with reopen criteria
the task is abandoned/superseded
```

---

# 12. Message design

Collaboration messages should be concise enough to be useful but structured enough to avoid vague endorsement.

A substantive message should normally contain some subset of:

```text
Thread ID
Message ID
Author / collaborator
Role
In reply to
Repository head reviewed
Artifacts actually read
Purpose
Position / findings
Evidence or repository references
Strongest objection / risk
Uncertainty
Requested next action
```

The message should reference existing files rather than quoting them wholesale.

Large code diffs or research should live in their natural artifacts and be linked by commit/path.

Messages are append-only provenance after another participant has relied on them. Corrections should normally be a new message rather than rewriting history.

---

# 13. Human role

The human should not become a transport clerk, but should remain a decision participant.

The human normally performs four functions.

## 13.1 Task initiation / priority

The user decides what major project question is worth spending effort on.

## 13.2 Normative arbitration

When the disagreement depends on desired product behavior, risk appetite, effort, cost, user experience, or project ambition, the human decides.

## 13.3 Escalation arbitration

If models reach a durable unresolved disagreement that cannot efficiently be resolved by available evidence, the user decides whether to:

```text
choose one position
request more evidence
run an experiment
defer the question
ask a third reviewer
```

## 13.4 Consequential approval

Existing project governance continues to determine where explicit human approval is needed.

Multi-model consensus should not automatically bypass a human gate.

---

# 14. Collaboration patterns

The architecture should support several patterns rather than one rigid pipeline.

## Pattern A: owner + reviewer

```text
ChatGPT TASK_OWNER
Claude INDEPENDENT_REVIEWER
```

or the reverse.

Good for normal implementation/design work.

## Pattern B: independent parallel design

Both models independently design from the same requirements before seeing each other's answer.

Good for high-impact architecture.

## Pattern C: proposer + critic

One creates a solution; the other is explicitly tasked with falsification and hidden-assumption search.

Good before freezing a specification or expensive experiment.

## Pattern D: researcher + integrator

One gathers literature/current external evidence; the owner integrates it into ADS without treating the researcher's prose as authority.

## Pattern E: implementer + verifier

One writes code; another verifies tests, invariants, migration behavior, privacy boundaries, and claims.

## Pattern F: experiment designer + adversarial reviewer

One proposes the experiment; the other tries to identify confounding, leakage, weak gates, post-hoc flexibility, or interpretations the experiment cannot support before execution.

## Pattern G: selective panel

Only for unusually consequential decisions, two or more independent reviewers may be used.

This should remain exceptional until its additional value is demonstrated.

---

# 15. Branch and PR coordination

## 15.1 One owner per bounded branch

The active branch should have one owner unless explicitly transferred.

## 15.2 Reviewer surfaces

A reviewer may use:

```text
collaboration-thread message
GitHub issue comment
PR top-level review
inline PR review
separate review artifact
```

without taking branch ownership.

## 15.3 Reviewer patch requests

If the owner wants the reviewer to implement a specific change, either:

```text
transfer ownership for that bounded patch
```

or:

```text
use a separate reviewer-owned branch/commit and have the owner integrate it
```

The choice should be explicit.

## 15.4 No hidden canonical changes

A reviewer must not silently change:

```text
CURRENT_STATE
current_routing.json
DECISIONS.md
accepted specifications
promoted integration branches
```

while still acting as reviewer.

---

# 16. Dedicated communication transport

The project should distinguish the durable collaboration record from the convenience transport used to exchange messages.

## Candidate primary transport: repository thread messages

Advantages:

```text
provider-neutral
cloneable
versioned
available to any collaborator with repository access
not dependent on one chat surviving
append-only review artifacts are easy to audit
```

Disadvantage:

```text
less conversational than a comment thread
requires a commit for each durable message
```

## Candidate interactive transport: GitHub issue comments

A GitHub issue associated with `MC-XXXX` can provide a dedicated asynchronous conversation board.

Advantages:

```text
chronological comments
no branch-file edit conflicts
natural discussion surface
models with GitHub write access can communicate without user copy-paste
```

Disadvantages:

```text
not part of a normal repository clone
capability depends on each model's GitHub integration
comments may become verbose/noisy
```

Recommended initial policy:

```text
repository thread = durable collaboration identity + structured review artifacts
GitHub issue/PR comments = optional low-friction transport
canonical resolution = promoted normal project artifact
```

This gives redundancy without making raw discussion authoritative.

---

# 17. Efficiency and context economy

Cross-model collaboration becomes harmful if every round requires rereading the entire repository or copying huge outputs.

The protocol should favor references such as:

```text
commit SHA
PR number
thread/message ID
file path
section heading
checkpoint
specification/result ID
```

A handoff should identify a **minimal governing read set**, not dump a transcript.

For example:

```text
Read:
- THREAD.md
- BRIEF.md
- Foundation X sections 3-6
- Specification Y
- PR #N diff

Do not initially read:
- proposer's Research Z
```

This supports both efficiency and independent review.

---

# 18. Provenance evolution required if accepted

If this architecture is promoted, the current ChatGPT-specific checkpoint/session provenance should evolve deliberately.

A likely direction is a provider-neutral interaction provenance block such as:

```text
Development session
Interaction environment
Workspace / project
Session title
Primary collaborator
Collaboration role
Collaboration thread        # when applicable
```

Historical checkpoints should remain untouched except for any separately governed metadata migration.

The validator should accept the new contract prospectively rather than allowing silent metadata drift.

Exact field names and backward-compatibility rules should be designed after the collaboration trial exposes what information is actually useful.

---

# 19. What should become canonical if the trial succeeds

Potential promotions include:

```text
DEVELOPMENT_METHOD.md v0.5
    multi-model task ownership, review, disagreement, and promotion rules

CONTINUITY.md
    model-neutral reconstruction and handoff procedure

checkpoints/README.md
    provider-neutral interaction provenance

checkpoint metadata validator
    prospective support for new provenance contract

docs/model_collaboration/README.md
    operational collaboration-exchange protocol

MAJOR_CHANGES.md
    record shift from single-model ChatGPT development to governed multi-model collaboration
```

No promotion should occur merely because this research memo exists.

---

# 20. Failure modes to pressure-test

The first collaboration trial should actively look for:

```text
both models converging because the reviewer was anchored
reviewer disagreeing performatively rather than substantively
unclear branch ownership
models editing each other's target state
user becoming a copy-paste relay
review messages becoming another stale knowledge silo
excessive process overhead for small tasks
conflicting canonical updates
unclear human decision boundary
reviewer failing to reconstruct from repository state
thread messages duplicating full research artifacts
GitHub issue discussion becoming authority by accident
provider-specific assumptions leaking into the protocol
checkpoint provenance failing outside ChatGPT
costly temptation to automate before need is demonstrated
```

The architecture should be revised from observed failures rather than defended for aesthetic consistency.

---

# 21. First empirical trial: MC-0001

Use this architecture itself as the first multi-model collaboration test.

Participants:

```text
ChatGPT
    initial proposer / task owner

Claude
    independent counter-designer + comparative reviewer

Human project owner
    arbiter and project-intent authority
```

Recommended review design:

```text
Phase A
    Claude reads neutral BRIEF + governing project method only.
    Claude does NOT read Research 035 yet.
    Claude records its own preferred collaboration architecture.

Phase B
    Claude then reads Research 035.
    Claude records a comparative review:
        convergence
        disagreements
        missing concerns
        overengineering
        underengineering
        must-change items
        what evidence would change its view

Phase C
    ChatGPT reads Claude's preserved independent proposal + comparative review.
    ChatGPT responds to each material disagreement without optimizing for consensus.

Phase D
    unresolved disagreements are classified and routed to:
        evidence/test
        human decision
        deferred open question

Phase E
    only then decide whether to promote a Development Method v0.5.
```

This trial intentionally evaluates both the proposed architecture and the collaboration process used to review it.

---

# 22. Candidate acceptance criteria for the collaboration method

Before declaring the method ready for routine use, the first trial should show at least:

```text
C1  both models reconstruct the relevant repository state correctly
C2  review can happen without large conversation copy-paste
C3  task ownership remains unambiguous
C4  independent first-pass output is preserved before cross-conditioning
C5  material disagreement remains explicit rather than socially normalized
C6  reviewer can agree without becoming uncritical
C7  reviewer can disagree without performative contrarianism
C8  user arbitration is limited to genuine decision points rather than transport work
C9  collaboration messages remain clearly non-canonical provenance
C10 resolution can be promoted through the existing project method
C11 process overhead remains proportionate to task importance
C12 no provider-specific mechanism becomes an unnecessary hard dependency
```

These criteria are methodological evidence, not an automated benchmark yet.

---

# 23. Open questions for cross-model review

Claude should specifically challenge the following.

1. Is one-task-owner strong enough, or should ownership be modeled at path/worktree scope?
2. Are immutable repository message files useful, or would GitHub issues/PR reviews provide a cleaner primary exchange?
3. Is the two-stage independent-then-comparative review worth its overhead, and for what task classes?
4. What prevents a reviewer from being anchored by the repository's own framing even when it has not read the proposal?
5. Should the human always arbitrate unresolved model disagreement, or should some classes default to experiment/evidence generation first?
6. How should reviewer confidence and uncertainty be represented without fake precision?
7. How much raw collaboration history should be preserved versus summarized?
8. Should review messages be append-only at the file level or only logically immutable after reliance?
9. How should checkpoint provenance evolve to represent ChatGPT, Claude, Codex, and future collaborators without bloating every checkpoint?
10. At what point does the collaboration exchange become enough infrastructure that an API/event-based orchestrator actually becomes simpler?
11. What risks arise from both models sharing the same repository and therefore the same conceptual framing?
12. How should the project measure whether a second model actually improves decisions instead of merely increasing confidence and latency?

---

# 24. Current recommendation

The candidate direction is:

```text
subscription-mediated human-supervised collaboration now
    +
repository as project authority
    +
dedicated Model Collaboration Exchange
    +
one task owner / serialized canonical writes
    +
role-based review
    +
independent-first review for high-impact questions
    +
explicit disagreement preservation
    +
optional GitHub issue/PR transport
    +
human arbitration for genuine project-intent conflicts
    +
API orchestration deferred until observed need
```

The next legitimate step is not to canonize this proposal.

The next legitimate step is to make Claude review the same problem under a deliberately independence-preserving protocol, then compare the two architectures honestly and revise from the disagreement.