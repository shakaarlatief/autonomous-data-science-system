# Deferred Review and Catch-Up Protocol

**Date:** 2026-08-26  
**Status:** Accepted operational collaboration protocol  
**Authority:** Canonical collaboration-method supplement under Development Method v0.5. Frozen specifications and accepted project decisions remain stronger within their declared scopes.  
**Governing research:** `docs/research/036_deferred_asynchronous_review_and_catchup_architecture.md`  
**Review evidence:** MC-0003, including exact-target Claude review at `74fbf8f5dbf7b57bb5f3038b41122f20e09a4b53`

## Purpose

This protocol covers the case where one collaborator remains productive while another collaborator is temporarily unavailable, but some of the continuing work is still intended to receive later review.

The governing rule is:

> **Collaborator unavailability does not globally block ADS unless a specific accepted gate requires that collaborator before the next relevant boundary.**

This pattern is distinct from simply switching to SOLO mode. Intended review remains an explicit obligation until satisfied, superseded, waived where legitimately optional, or resolved through the normal project method.

---

## This is a cross-thread scheduling pattern

Deferred catch-up is **not** a `review_mode` enum under Specification 024.

Existing thread modes describe the kind of collaboration:

```text
SOLO
REVIEWED
INDEPENDENT_THEN_COMPARATIVE
COORDINATED_HANDOFF
ADVERSARIAL_REVIEW
```

Deferred catch-up describes when a required or optional reviewer acts relative to other bounded tasks.

Several threads may therefore legitimately be waiting for the same reviewer while another thread is active.

---

## Required distinction: review requirement versus gate boundary

Two questions must be kept separate:

```text
Is review required?

Before what boundary must it happen?
```

Current requirement values:

```text
REQUIRED
OPTIONAL
```

Current gate-boundary vocabulary:

```text
BEFORE_TARGET_MUTATION
BEFORE_THREAD_RESOLUTION
BEFORE_PROMOTION
NONE
```

Semantic constraint established by MC-0003 review:

```text
REQUIRED -> must use a real gate boundary
OPTIONAL -> may use NONE
```

`REQUIRED + NONE` is not a valid current combination. If review is truly required, the process must name what project boundary waits for it.

These values are not part of the frozen Specification 024 schema. Until a later prospective mechanical contract is justified, they may be recorded explicitly in `THREAD.md`, review requests, and the convenience review inbox.

---

## Rules for continuing work

### Rule 1: do not silently erase review

If a task was intended to receive later review, temporary reviewer unavailability must not silently convert it to SOLO.

### Rule 2: freeze the review target

Before moving on, preserve the exact target the reviewer is expected to assess, normally:

```text
exact Git SHA
bounded artifacts
frozen governing requirement/specification
requested review output
```

### Rule 3: obey the gate, not reviewer availability in the abstract

If the gate is `BEFORE_TARGET_MUTATION`, the affected work waits.

If the gate is later, the owner may continue legitimate work until that boundary is reached.

Other independent bounded tasks may proceed even while one thread waits.

### Rule 4: do not over-accumulate provisional dependence

Later work that depends materially on an unreviewed result must be either:

```text
cheaply reversible / explicitly provisional
```

or the pending review should be escalated to an earlier blocking boundary.

### Rule 5: preserve downstream impact

If a late review causes a required correction, inspect downstream tasks that relied on the corrected result. Do not patch only the reviewed file and ignore later consequences.

MC-0003 established that this is currently a procedural safety property, not yet a machine-readable dependency graph. If real cross-thread dependency chains become non-trivial, explicit thread-dependency metadata is the highest-priority candidate mechanical extension.

### Rule 6: no automatic review of SOLO work

Work intentionally completed as SOLO creates no hidden obligation merely because another model exists.

---

## Review inbox

`docs/model_collaboration/REVIEW_INBOX.md` is the current human-readable catch-up routing view.

It is **not** a second source of truth.

Authoritative evidence remains in each thread's:

```text
STATE.json
THREAD.md
frozen review request
exact repository target
```

The inbox exists so a returning collaborator can quickly discover what awaits them without relying on chat memory.

MC-0003 confirmed that manual inbox/state consistency is a real future drift risk. The current project still defers a generated inbox or CI consistency guard until repeated backlog use or observed drift justifies the extra mechanism.

---

## Catch-up sequence

When a collaborator returns:

```text
1. open REVIEW_INBOX.md
2. inspect the highest-consequence pending item
3. reconstruct from the item's minimal read set
4. verify the exact review target SHA
5. perform the requested review without assuming later descendants were reviewed
6. write the durable numbered message
7. route REQUIRED_CORRECTION / OPTIONAL_IMPROVEMENT / NO_CHANGE or the thread-specific disposition
8. perform downstream impact analysis when required
9. mark/supersede the obligation through the thread process
10. continue to the next pending item
```

---

## Default ordering

Normal priority is:

```text
1. blocks target mutation / irreversible action
2. blocks resolution or promotion
3. broad downstream dependency fan-out
4. ordinary required review
5. optional/advisory review
```

This is a qualitative ordering, not a fake-precision score.

---

## One-by-one versus batch catch-up

One-by-one is the default.

Batching is allowed when items are tightly related and share enough governing context that one session reduces redundant context cost.

Batching must still preserve:

```text
separate thread identity
exact reviewed head per item
separate disposition per item
separate required corrections
```

A batch must not blur several reviews into one vague endorsement.

MC-0002 and MC-0003 provided the first positive operational example: both were processed in one Claude session while retaining separate targets, review artifacts, findings, and dispositions.

---

## Stale review targets

If a review target changes materially before the reviewer acts:

```text
old target -> remains the only target covered by the old request
new target -> requires an explicit rebased/new obligation if review is still needed
```

A review of an ancestor commit is not automatically review of the current descendant.

---

## Independence-sensitive work

Some reviews cannot safely be deferred until after implementation.

Examples include:

```text
prospective experiment challenge
blind independent counter-design
held-out interpretation gate
security/privacy approval before an external side effect
```

For those cases, the gate should occur before the contaminating action. Reviewer unavailability does not justify turning prospective review into retrospective review.

---

## Scheduled or unattended execution

The current method does not use unattended scheduled Claude/ChatGPT review execution.

This was explicitly considered after the first real usage-limit pressure. It is deferred because:

```text
scheduled execution does not create extra weekly subscription capacity
unattended repository writes add concurrency risk
an unattended review cannot easily pause for clarification
usage may be consumed before the human can intervene
current manual triggering is already lightweight because the repository holds the backlog
```

This is not a permanent rejection. Revisit if product capabilities, isolated write surfaces, usage economics, or backlog scale materially change.

---

## Current evidence

The first pressure test used two Claude obligations:

```text
MC-0002
    Specification 024 direct implementation review
    higher priority because Specification 024 classification depended on it

MC-0003
    deferred-review/catch-up architecture review
    lower immediate priority because it blocked method promotion, not unrelated work
```

Both were simultaneously `WAITING` without a global model lock. Claude later processed MC-0002 first and MC-0003 second, exactly as the inbox specified.

This is direct evidence that multiple pending reviewer obligations can coexist while unrelated legitimate work continues.

---

## Mechanical follow-up

Specification 024 remains accepted as frozen and is not retroactively expanded.

No Specification 025 is opened merely because future improvements are imaginable.

Evidence-backed future candidates are:

```text
1. explicit cross-thread dependency metadata for downstream impact discovery
2. deterministic review-inbox generation / consistency validation if drift appears
3. secondary-vs-secondary write-surface overlap if simultaneous secondary writers appear
4. explicit review-obligation / gate-boundary fields when backlog scale justifies schema support
5. stale/superseded obligation checks when repeated use shows manual handling is unreliable
```

The mechanism should continue to earn complexity through actual use.