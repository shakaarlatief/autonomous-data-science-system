# Research 036: Deferred Asynchronous Review and Catch-Up Architecture

**Date:** 2026-08-26  
**Status:** Candidate Level-2 collaboration-architecture extension for later cross-model review  
**Maturity:** Strong design proposal derived from an observed operational constraint; not yet canonical development method  
**Scope:** How one collaborator may continue bounded project work while another collaborator is temporarily unavailable, while preserving required later review, exact review targets, downstream dependency risk, and efficient catch-up  
**Authority:** Research proposal only. Development Method v0.4, Specification 024, accepted project decisions, and normal repository authority remain controlling until this extension is reviewed and explicitly promoted.  
**Origin:** User identified the practical case where Claude may exhaust subscription usage while ChatGPT remains available, or vice versa, and asked that continued work remain possible without silently losing intended cross-model review.

## 1. Problem statement

The first multi-model architecture correctly established that collaboration is asynchronous, selective, and repository-mediated. It also established that SOLO work is first-class and that a collaboration thread may wait for a future actor.

A more specific operational case now needs explicit treatment:

```text
collaborator B becomes temporarily unavailable
        ↓
collaborator A can still work
        ↓
A may complete several bounded tasks
        ↓
some tasks were intended to receive later B review
        ↓
B returns later
        ↓
B catches up on one or several preserved obligations
```

The system must support this without either extreme:

```text
EXTREME 1
one unavailable reviewer blocks the entire project

EXTREME 2
availability pressure silently converts intended collaboration into SOLO work
```

The required principle is:

> **Collaborator unavailability does not globally block the project unless a specific accepted gate makes that collaborator's contribution blocking before the next relevant boundary.**

This is provider-neutral. Claude usage limits are the first observed trigger, but the same problem applies if ChatGPT is unavailable, a human reviewer is delayed, a future specialist model is offline, or an external verification dependency cannot run immediately.

---

## 2. Why ordinary asynchronous messaging is not enough

The current collaboration exchange already provides durable messages and `WAITING` / `DEFERRED` lifecycle states. Specification 024 also separates `next_expected_actor` from target-state write ownership.

Those primitives are necessary, but they do not yet answer four load-bearing questions:

1. **May the owner continue other work before the review happens?**
2. **What exact boundary is the review required before?**
3. **What exact repository state should the later reviewer review?**
4. **What happens to downstream work if a late review invalidates an earlier assumption?**

Without explicit answers, a repository may contain a pending review but still leave the practical process ambiguous.

---

## 3. Core concepts

### 3.1 Review obligation

A review obligation is an explicit statement that a specific bounded artifact or decision is expected to receive another collaborator's review.

It is not inferred merely because another collaborator exists.

A SOLO task therefore creates no hidden review debt.

Conceptually, a review obligation should eventually preserve at least:

```text
thread / task identity
reviewer or reviewer role
whether review is REQUIRED or OPTIONAL
exact review target ref
review type
review gate boundary
priority
minimal governing read set
status
known downstream reliance
```

### 3.2 Review target snapshot

A delayed review must not operate against a moving target while later being treated as if it reviewed the current state.

Every required deferred review should therefore point to an exact immutable repository target, normally a Git commit SHA plus a bounded artifact/read set.

If the target changes materially before review:

```text
old obligation
    -> SATISFIED only for the old target
    or SUPERSEDED before review

new target
    -> new/rebased obligation if review is still required
```

A later review of commit `X` must never be represented as review of commit `Y` merely because `Y` descended from `X`.

### 3.3 Gate boundary

"Blocking" is too coarse unless the blocked boundary is named.

A future mechanical extension should distinguish at least:

```text
BEFORE_TARGET_MUTATION
    reviewer must act before implementation/mutation begins

BEFORE_THREAD_RESOLUTION
    owner may work, but the bounded thread cannot be resolved as accepted
    until review is complete

BEFORE_PROMOTION
    implementation / follow-on exploration may continue,
    but the candidate cannot be promoted into accepted/canonical authority
    until review is complete

NONE
    review is advisory / optional and creates no acceptance gate
```

This is better than one boolean `blocking=true/false` because it preserves exactly what may continue.

### 3.4 Catch-up backlog

When several threads await the same collaborator, the collection is a **catch-up backlog**.

The backlog should ideally be **derived from per-thread authoritative state**, not maintained as a second independent source of truth.

A human-readable `REVIEW_INBOX.md` may exist as a routing convenience, but thread state and frozen review requests remain authoritative.

The long-term mechanism should be capable of answering:

```text
What does Claude currently owe?
What does ChatGPT currently owe?
Which review blocks implementation?
Which review blocks only promotion?
Which reviews are optional?
What exact heads should be reviewed?
In what order should catch-up normally happen?
```

---

## 4. Progression rule while another collaborator is unavailable

The project should not ask a binary question such as:

> "Is Claude available?"

It should ask:

> "Does the current next action depend on a Claude obligation whose gate boundary has been reached?"

This yields the following rule:

```text
IF required review gate has not been reached
    owner may proceed with legitimate bounded work

IF required review gate is reached
    affected task/boundary waits

UNRELATED bounded tasks
    may still proceed unless a broader accepted dependency blocks them
```

Therefore one blocked thread does not imply global project paralysis.

---

## 5. Multiple tasks while a reviewer is unavailable

The intended pattern is explicitly supported:

```text
Claude unavailable

ChatGPT completes Task A
    -> Claude review required before promotion
    -> freeze A review target
    -> queue A

ChatGPT completes Task B
    -> Claude verification useful but non-blocking
    -> freeze B review target
    -> queue B

ChatGPT performs Task C
    -> SOLO by design
    -> no Claude obligation

ChatGPT begins Task D
    -> independent of A/B
    -> continue normally

Claude returns
    -> discover A and B
    -> review according to gate/priority
    -> no need to review C merely because it happened while Claude was absent
```

This prevents the collaboration architecture from degenerating into either mandatory dual-model bureaucracy or accidental review loss.

---

## 6. Downstream reliance is the critical safety problem

Delayed review introduces a risk not present in immediate review: later work may depend on something that has not yet been reviewed.

For example:

```text
Task A architecture candidate
    ↓
Claude review deferred
    ↓
Task B implementation depends on A
    ↓
Task C migration depends on B
    ↓
Claude later finds A is wrong
```

The architecture must not hide this propagation risk.

### 6.1 Safe continuation

Continuation is safest when later work is:

```text
independent of the unreviewed result
or
explicitly provisional and cheap to revise
```

### 6.2 When deferral should become blocking

A deferred review should be escalated to an earlier blocking boundary when subsequent work would create:

```text
large irreversible cost
large migration/rework cost
external side effects
scientific contamination
loss of independence
security/privacy exposure
promotion of an unreviewed claim into authority
```

The collaboration system should not continue merely because it technically can.

### 6.3 Downstream impact sweep

If a late review produces a required correction, the task owner should inspect not only the reviewed artifact but also downstream work created after the review target.

The impact sweep should ask:

```text
Which later tasks relied on the corrected claim/design?
Which artifacts remain valid?
Which tests/results must be rerun?
Which decisions or checkpoints need qualification?
Which pending reviews are now stale or superseded?
```

This should be a normal catch-up responsibility, not an exceptional recovery tactic.

---

## 7. Catch-up ordering

When a collaborator returns with several pending items, the default ordering should be based on consequence, not simply creation time.

Candidate order:

```text
1. reviews blocking target mutation / irreversible next steps
2. reviews blocking acceptance or promotion
3. reviews whose outcome has broad downstream dependency fan-out
4. ordinary required direct reviews
5. optional/advisory reviews
```

Within the same class, older obligations normally come first unless a newer item is more consequential.

No pseudo-precise numerical priority score is needed initially.

---

## 8. One-by-one review versus batching

The reviewer may process several queued items in one session, but they should remain separate obligations.

### Default: one-by-one

Use one-by-one review when:

```text
tasks have different governing specifications
tasks have different target heads
findings may affect later queued tasks
independence requirements differ
one review may supersede another
```

### Batching may be efficient when

```text
items share the same governing context
items are tightly related
review mode is direct/comparative rather than blind-independent
the reviewer can preserve a separate disposition for every item
batching does not obscure exact reviewed heads
```

A batch is a scheduling optimization, not a merge of thread identity.

The reviewer must still be able to say:

```text
MC-0010 -> accepted
MC-0011 -> required correction
MC-0012 -> obsolete because MC-0011 changed the premise
```

---

## 9. Efficient reviewer reconstruction

Catch-up must not require replaying every message the owner exchanged with the human while the reviewer was unavailable.

Each queued obligation should provide a minimal packet:

```text
thread / task
exact target head
frozen governing requirement/specification
artifacts to inspect
why review is requested
what boundary the review gates
known downstream reliance
requested output location
```

The reviewer reconstructs from the repository and exact target, not from a conversation transcript.

This preserves the original repository-authority principle and controls context cost.

---

## 10. Interaction with independence-preserving review

Deferred review is not always compatible with proceeding first.

If the intended review is **prospective** or **blind independent** by design, performing the dependent work before review may contaminate the question.

Examples:

```text
experiment design that must be challenged before execution
architecture counter-design that must be independent of implementation evidence
held-out interpretation gate
security approval required before deployment
```

For such tasks the gate should normally be `BEFORE_TARGET_MUTATION` or another early boundary.

The project must not use reviewer unavailability as a reason to retroactively reclassify a prospective gate as a later review.

---

## 11. Current Specification 024 relationship

Specification 024 already provides valuable primitives:

```text
per-thread state
WAITING / DEFERRED lifecycle
next_expected_actor
target_write_owner
exact base refs / transitions
allowed secondary write surfaces
```

It deliberately does **not** yet encode the richer review-obligation semantics above.

Specification 024 is already prospectively frozen and awaiting MC-0002 review. It should not be rewritten post hoc to absorb this new requirement.

Candidate mechanical follow-up after Specification 024 classification and cross-model review of this design:

```text
Specification 025 or later
    explicit review-obligation / gate metadata
    backlog discovery command
    stale-target / supersession semantics
    optional human-readable generated review inbox
```

This separation preserves the integrity of Specification 024 while allowing the architecture to evolve from real use.

---

## 12. No global reviewer lock

The catch-up design strengthens the argument against a global model lock.

At one moment the repository may legitimately contain:

```text
MC-0002  waiting for Claude review
MC-0003  waiting for Claude review
MC-0004  ChatGPT actively owns implementation
MC-0005  SOLO human documentation task
```

These states are not contradictory because ownership is bounded by task/thread and write scope.

The unavailable collaborator has a backlog, not ownership of the whole repository.

---

## 13. Human role

The human should not need to manually remember all deferred obligations.

The system should make them discoverable.

The human may still decide to:

```text
raise/lower priority
waive an optional review
convert a deferrable review into a blocking gate
stop work that is accumulating too much provisional downstream dependence
request a batch catch-up session
```

A required review should never be silently waived merely because the reviewer was unavailable for a long time.

---

## 14. Operational evidence from the current project

The trigger is already real rather than hypothetical.

During MC-0001, Claude reached its product usage limit after a substantial high-effort review. ChatGPT remained available and the user explicitly asked whether project work could continue while preserving work for Claude to inspect later.

The current repository already has one pending Claude obligation:

```text
MC-0002
Specification 024 implementation review
```

MC-0003 is intentionally being opened as the first explicit **deferred catch-up** architecture review. ChatGPT may complete and preserve the candidate design now. Claude can review it later without blocking unrelated work.

This creates the first real backlog with multiple Claude obligations and allows the process to be pressure-tested rather than merely described.

---

## 15. Candidate acceptance criteria

A future promoted deferred-review mechanism should demonstrate:

```text
DR-C01  reviewer unavailability does not silently erase intended review
DR-C02  unrelated work can continue without global collaborator locking
DR-C03  every deferred required review names an exact immutable target
DR-C04  the boundary gated by review is explicit
DR-C05  SOLO tasks do not create automatic review obligations
DR-C06  pending obligations are discoverable without chat memory
DR-C07  stale/superseded review targets cannot be misrepresented as current review
DR-C08  downstream reliance is visible enough to trigger impact review
DR-C09  late required corrections trigger downstream impact analysis
DR-C10  batching preserves per-thread identity and disposition
DR-C11  prospective/blind gates cannot be retroactively converted to post-hoc review
DR-C12  process overhead remains lower than blocking all work or replaying entire conversations
```

---

## 16. Current candidate recommendation

```text
collaborator unavailability != global project block

review obligation is explicit, never inferred from mere model availability

required review records an exact review target

review requirement and gate boundary are distinct

owner may continue other bounded work until the relevant gate is reached

later dependent work must be independent or explicitly provisional

late required corrections trigger downstream impact analysis

catch-up backlog is derived from per-thread authoritative state

human-readable inbox is routing convenience, not a second authority

one-by-one review is default; batching is allowed only when it preserves item-level dispositions

Specification 024 remains frozen; richer gate/backlog mechanics belong in a later contract after review
```

The next legitimate step is to freeze this candidate in MC-0003, queue Claude's direct review as deferrable, and use the resulting multiple-pending-review situation as an actual pressure test of the architecture.