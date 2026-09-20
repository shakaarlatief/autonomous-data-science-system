# Source Evidence 001: Chat 26 Interaction-Orchestration Discussion

**Source date:** 2026-09-19
**Conversation:** `26 - Full Rebuild and Incremental Refresh Equivalence`
**Evidence supplied again by owner:** 2026-09-20 in Chat 27
**Durable prior extraction:** `AB-031: Intent-driven interaction orchestration, collaboration routing, and recoverable conversation continuity`
**Prior preservation commit:** `d08102459120988ed636db853bf620f6f6e9f806`
**Authority:** OWNER-PROVIDED INTERACTION EVIDENCE / NON-AUTHORITATIVE

## 1. Why this evidence is preserved again

AB-031 correctly distilled the 2026-09-19 discussion, but the owner supplied the richer conversation again on 2026-09-20 because the detailed reasoning matters for the next architecture stage.

This file does not replace AB-031. It preserves nuances that a short backlog item can compress away and makes the source reasoning recoverable without requiring the owner to paste the prior chat again.

## 2. Fundamental owner question

The owner was not merely asking how a new ChatGPT conversation should read a continuation file.

The deeper question was:

> What is my role, and should the architecture make it so that I can express normal project intent while the system itself knows which process, knowledge, model, tool, preservation path, recovery path, and continuation path apply?

The owner explicitly questioned whether the project should rely on the assistant simply recognizing what to do, or whether the architecture should create durable paths that make the correct behavior reconstructable.

Examples included:

```text
new chat / continuation
    human should not need a large manual continuation prompt

new idea / observation
    system should know whether to investigate, preserve, change,
    capture, research, or route elsewhere

architecture change
    system should know the appropriate review / decision path

model collaboration
    human should not need to remember to ask:
        "do you want to ask Claude?"

runtime failure
    Codexless-down should activate a professional recovery workflow

context-window exhaustion
    should behave like governed interruption / rollover recovery

unsaved discussion
    project should be able to know that unresolved non-authoritative
    interaction material exists without making the conversation canonical
```

## 3. Desired human role

```text
HUMAN
    project owner
    source of intent
    source of observations
    decision authority where human judgment is genuinely required
    explicit override authority

NOT primarily
    workflow operator
    file-path memory
    model scheduler
    recovery-runbook operator
    architecture-backlog librarian
    continuation-prompt transport mechanism
```

Explicit owner instructions should always remain possible, for example:

```text
"Ask Claude."
"Do not modify anything."
"Save this for later."
"Just investigate."
```

But these should be overrides or conveniences rather than prerequisites for correct project operation.

## 4. Natural language and commands should share semantics

The discussion proposed that natural language and optional command-like shortcuts should resolve to the same underlying project intent.

```text
"I want to continue where we left off."
"continue"
/continue

    -> same semantic continuation intent
```

The owner should not need to memorize special commands merely to access project capabilities.

## 5. Actor entry is more fundamental than a new chat

A key abstraction was:

> The problem is not specifically how a new ChatGPT chat knows what to do. It is how an actor entering an arbitrary project situation determines the correct process.

Potential actors include:

```text
fresh ChatGPT conversation
returning ChatGPT conversation
Claude
Codex
Claude Code / local agent
GitHub Action
future ADS agent
human at terminal
recovery process
```

Therefore the desired mechanism is project reconstruction + routing, with a new chat only one case.

## 6. Intent-driven project operation

The conceptual flow developed in the discussion was:

```text
owner intent
    ->
model-assisted intent understanding
    ->
typed project intent
    ->
project-controlled routing
    ->
reconstruction plan
    ->
applicable workstream / governing procedure
    ->
authority / freshness / private-state checks
    ->
tool and/or collaborator selection
    ->
execution or investigation
    ->
result / evidence
    ->
preservation decision
    ->
continuation receipt
```

The LLM may help interpret what the owner means, but governing-source closure, authority, safety, and mutation rules should not depend solely on model memory.

## 7. Idea / observation / change lifecycle

Examples discussed:

```text
"I noticed X."
    -> observation / possible capture

"Can you investigate X?"
    -> research / exploratory investigation

"I think X should work differently."
    -> candidate architecture/change question

"Change X."
    -> governed implementation after authority/procedure resolution

"Save this for later."
    -> capture / backlog / obligation

"Resume what we were doing."
    -> continuation / reconstruction
```

A mature system should avoid both extremes:

```text
user said an idea -> silently edit canonical architecture
user said an important idea -> forget it when chat ends
```

## 8. Collaboration routing

The owner specifically questioned why they should have to remember to suggest Claude.

The desired behavior was policy-based collaboration routing using factors such as:

```text
task class
consequence
uncertainty
architecture novelty
implementation boundedness
need for independence
need for adversarial review
machine-local evidence need
provider/tool availability
quota/capacity
```

Possible outcomes:

```text
ChatGPT only
Codex bounded implementation
Claude architecture / independent review
Claude Code for machine-local evidence/work
independent-first multi-model review
no extra collaborator when unnecessary
```

## 9. Operational break-glass recovery

The owner gave Codexless failure as a concrete example.

A professional flow could be:

```text
local runtime unavailable
    ->
recognize incident class
    ->
preserve/pause primary workstream context
    ->
activate recovery procedure
    ->
use an access path independent of the broken component
    ->
diagnose / restore
    ->
verify
    ->
record cause + recovery evidence
    ->
resume original workstream
```

Recovery instructions must not depend exclusively on the failed component.

## 10. Interaction continuity without making chat authoritative

The owner proposed a non-authoritative interaction/session envelope capable of preserving facts such as:

```text
interaction/session identity
interaction role
mode
durable project anchor at entry
current workstream
bounded purpose/topic
unpromoted material present?
external collaborators involved
pending review/capture?
content recoverability status
return/resume condition
last durable receipt
```

This would allow a future actor to know that unresolved interaction-local reasoning exists without claiming the conversation itself is canonical project truth.

The discussion distinguished:

```text
EPHEMERAL
    ordinary transient conversation

INTERACTION-DURABLE / NON-AUTHORITATIVE
    continuity metadata / unresolved material exists

PROMOTED PROJECT KNOWLEDGE
    accepted meaning moved through capture/research/decision/etc.
```

## 11. Context-window rollover as interruption recovery

Instead of manually asking for a giant summary and transporting it into a new chat, the desired architecture could make context rollover a governed interruption:

```text
interaction reaches boundary
    -> durable interaction receipt
    -> canonical state + unresolved interaction state known
    -> new interaction reconstructs canonical state
    -> optionally recovers/requests unresolved interaction context
    -> continues
```

## 12. Core principle

> **The human should not need to remember the architecture in order to use the architecture.**

AB-031 was created because this discussion was important but not yet ready to become selected architecture.

The 2026-09-20 discussion in Source Evidence 002 demonstrates that this concern is no longer merely prospective: the project experienced a fresh activation miss where the owner had to remind ChatGPT of AB-031/AB-027 before they became active in reasoning.
