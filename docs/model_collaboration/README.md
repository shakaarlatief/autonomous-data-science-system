# Model Collaboration Exchange

**Status:** Current canonical model-collaboration protocol  
**Date promoted:** 2026-08-26  
**Authority:** Canonical operational supplement to Development Method v0.5 for collaborative ADS development. It does not override accepted project specifications or decisions outside its scope.  
**Evidence base:** Research 035, MC-0001, Specification 024, MC-0002, Research 036, and MC-0003

## Purpose

This directory is the provider-neutral asynchronous collaboration surface for AI collaborators working on ADS itself.

It exists because:

```text
repository as project authority
    !=
model-to-model collaboration transport/provenance
```

The exchange preserves review requests, independent proposals, critiques, responses, handoffs, deferred review obligations, and resolution records without turning raw model dialogue into project authority.

Multi-model collaboration is selective. SOLO ChatGPT work and SOLO Claude work remain first-class development modes.

---

## Operating modes

### SOLO

One collaborator owns a bounded task with the human and repository. No second-model obligation exists unless one is explicitly created.

Use when additional review is unlikely to justify coordination cost.

### REVIEWED

One collaborator owns the task and another performs a bounded review, critique, verification, or research role.

### INDEPENDENT_THEN_COMPARATIVE

For high-impact questions where anchoring matters, the reviewer first reasons from an accepted pre-proposal repository ref plus a neutral brief, freezes its own position, and only then sees the proposer solution for comparative review.

Known contamination must be disclosed. Apparent convergence after leaked candidate content is not treated as fully independent evidence.

### COORDINATED_HANDOFF

A bounded task/subtask is explicitly transferred with repository state, write scope, and outstanding obligations preserved. Handoff does not create simultaneous co-ownership.

### ADVERSARIAL_REVIEW

A reviewer is specifically tasked with searching for falsifiers, unsupported assumptions, leakage, failure modes, or weak gates without being rewarded merely for disagreement.

---

## Core rules

1. Repository authority remains unchanged by model participation.
2. Collaboration is selective, not mandatory.
3. Every substantive collaborative bounded task has one task owner unless ownership is explicitly transferred.
4. `ROLE != WRITE_SCOPE`.
5. One collaborator owns target-state mutation at a time.
6. Secondary collaborators may write only explicitly declared secondary surfaces while another collaborator retains target-state ownership.
7. `next_expected_actor` does not imply target-state write ownership.
8. GitHub issues and PR comments are transport, not canonical authority.
9. Numbered repository message files are durable collaboration provenance.
10. Agreement and disagreement are not goals. Calibrated judgment is the goal.
11. Material disagreement stays explicit until resolved, deferred, or routed elsewhere.
12. Human arbitration is reserved for genuine project intent, desired requirement changes, consequential risk acceptance, resource commitments, and technically underdetermined normative choices.
13. API orchestration and unattended scheduled model review are not part of the current method.
14. Collaboration machinery must remain proportionate to task importance and observed need.

---

## Machine-readable state

Collaborative threads may use:

```text
docs/model_collaboration/threads/MC-NNNN/STATE.json
```

under accepted Specification 024.

The V1 state guard records:

```text
thread identity
review mode
lifecycle / phase
target and write paths
task owner
target-state write owner
participants / roles
allowed secondary write surfaces
next expected actor
independence status / exposures
latest transition
```

The validator is a **coherence guard, not an authenticated distributed lock**. Current provider integrations act through the project owner's GitHub authority, so repository state cannot cryptographically prove which model made a mutation.

Known V1 limitation: target-vs-secondary path overlap is guarded, but simultaneous secondary-vs-secondary overlap is not yet checked. Revisit only if a real thread needs multiple concurrent secondary writers.

---

## Thread structure

Stable collaboration identity uses:

```text
MC-NNNN
```

Typical structure:

```text
threads/
    MC-NNNN/
        BRIEF.md
        THREAD.md
        STATE.json          # when guarded
        messages/
            001_...
            002_...
            ...
        RESOLUTION.md       # when resolved/terminal
```

`BRIEF.md` defines the bounded problem. `THREAD.md` is the human-readable collaboration contract. `STATE.json` is machine-checkable execution/coherence state. Numbered messages preserve substantive collaboration provenance. `RESOLUTION.md` records terminal disposition.

A thread does not itself promote project knowledge. Normal checkpoint/promotion governance still controls canonization.

---

## Interaction provenance and naming

Both provider workspaces use the human-facing project/workspace name:

```text
Autonomous Data Science System
```

Visible conversations use:

```text
NN - Main Topic / Stage
```

Each interaction environment maintains its own sequence. Repository provenance uses self-describing provider-local IDs such as:

```text
chatgpt-06
claude-01
```

A substantive collaboration message should normally preserve:

```text
Thread
Message
Author / collaborator
Role
In reply to
Interaction environment
Project / workspace
Interaction session
Conversation title
Repository head reviewed
Purpose
```

Model/configuration, effort/reasoning mode, interaction surface, timestamp, and artifacts read are optional when they materially improve interpretation or reproducibility. Values that a model cannot reliably introspect should preserve their source when known rather than be guessed.

Historical ChatGPT-specific checkpoint provenance remains historical. Checkpoint 204 introduces the prospective provider-neutral checkpoint contract.

See `INTERACTION_PROVENANCE_AND_NAMING.md`.

---

## Genuine review requirements

When substantially agreeing, a reviewer should still identify:

```text
strongest plausible failure mode
strongest alternative considered
what would make support change
remaining provisional parts
```

When materially disagreeing, a reviewer should identify:

```text
exact disputed choice
why it matters
preferred alternative
what would make the reviewer accept the original
disagreement type
```

Useful disagreement classes include:

```text
FACT
INTERPRETATION
REQUIREMENT
ARCHITECTURE
RISK
EVIDENCE_SUFFICIENCY
NORMATIVE_PROJECT_INTENT
SCOPE
```

There is no blanket conservative-wins or narrow-scope-wins rule. Use evidence, accepted authority, reversibility, consequence, and project intent appropriate to the disagreement.

---

## Independent review integrity

When a review is intended to be genuinely independent, the normal starting package is:

```text
accepted pre-proposal repository ref
+
neutral problem brief
+
constraints / success criteria
+
explicit candidate-content exclusion/exposure audit
```

The reviewer should not reconstruct from candidate-branch routing documents that already summarize the proposal if the purpose is blind counter-design.

MC-0001 demonstrated why this matters: Claude avoided the full proposal but still saw candidate concepts leaked through routing documents, so the first pass was correctly classified as only partially independent.

---

## Deferred review and catch-up

The accepted cross-thread rule is:

> **Collaborator unavailability does not globally block ADS unless a specific accepted gate requires that collaborator before the next relevant boundary.**

An intended review must not silently become SOLO merely because the reviewer is temporarily unavailable.

For deferred work, preserve:

```text
review requirement
review gate
exact immutable review target
minimal governing read set
expected output
priority / downstream consequence
```

A required review must name a real gate. `NONE` is reserved for optional review.

Exact target discipline is strict: review of ancestor commit X is not automatically review of descendant Y.

When several obligations wait for the same collaborator, `REVIEW_INBOX.md` is the current convenience routing view. It is not authoritative; thread state and exact repository evidence control.

One-by-one catch-up is the default. Related items may be batched in one model session only if each keeps a separate exact target, findings, corrections, and disposition.

If a late review changes an upstream result, downstream reliance must be inspected. Cross-thread dependency discovery is currently procedural rather than machine-readable and is the highest-priority future mechanization trigger once real dependency chains justify it.

See `DEFERRED_REVIEW_AND_CATCHUP.md`.

---

## Review inbox and standardized catch-up prompt

Current pending work is routed in:

```text
docs/model_collaboration/REVIEW_INBOX.md
```

For Claude, when pending obligations exist, the standard user trigger is intentionally short:

```text
Check the repository and docs/model_collaboration/REVIEW_INBOX.md, then proceed with the pending Claude reviews in order.
```

The repository, not the relay prompt, should carry the detailed review contract.

---

## Transport

Optional GitHub issue/PR discussion can provide low-friction asynchronous transport:

```text
GitHub issue / PR comment
    -> notice / pointer / lightweight discussion

numbered repository message
    -> durable substantive collaboration provenance

accepted project docs / code
    -> authority after normal promotion
```

A complete issue comment may be used as a disclosed fallback if direct durable writing is temporarily unavailable, but no future continuation should depend on issue text as the only preserved material conclusion.

---

## Resource proportionality

A second model should create marginal epistemic value, not merely more activity.

Use expensive independent/comparative review selectively. Routine implementation under a frozen contract normally deserves a cheaper bounded direct review. Mechanical checks may remain SOLO or deterministic.

Model, effort level, and product surface are operational choices rather than fixed architecture. The project may collect lightweight evidence about review value versus usage cost before institutionalizing model-specific defaults.

Claude product usage was observed to be materially scarce during the first collaboration trial, which strengthened the case for deferred catch-up and bounded reading sets. Exact percentage usage is historical operational evidence, not a permanent architecture constant.

---

## Scheduled execution and API orchestration

Unattended scheduled review execution is currently deferred. It does not create extra weekly subscription capacity and introduces unattended write/concurrency, clarification, and budget-consumption risks that are not justified at current backlog scale.

API orchestration is also deferred. It would introduce separately metered provider usage, repeated context transmission, credentials, retry/failure handling, and orchestration infrastructure.

Revisit either mechanism only when observed manual coordination cost or backlog scale outweighs those costs and risks.

---

## Evidence from the first three threads

```text
MC-0001
    architecture design and independent/comparative challenge
    exposed candidate-content leakage and global-writer over-coarseness

MC-0002
    direct implementation review of Specification 024
    accepted all frozen gates
    proved lower-overhead REVIEWED mode

MC-0003
    deferred catch-up architecture review
    proved two waiting Claude obligations can coexist and later be processed
    in priority order without a global collaborator lock
```

The collaboration method should continue to evolve from observed failure rather than aesthetic completeness.