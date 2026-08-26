# Deferred Review and Catch-Up Protocol

**Date:** 2026-08-26  
**Status:** Candidate operational protocol under Research 036  
**Authority:** Collaboration working protocol only. It does not override frozen specifications, accepted decisions, project-current routing, or Development Method v0.4.  
**Governing research:** `docs/research/036_deferred_asynchronous_review_and_catchup_architecture.md`

## Purpose

This protocol covers the case where one collaborator remains productive while another collaborator is temporarily unavailable, but some of the continuing work is still intended to receive later review.

The governing rule is:

> **Collaborator unavailability does not globally block ADS unless a specific accepted gate requires that collaborator before the next relevant boundary.**

This pattern is distinct from simply switching to SOLO mode. Intended review remains an explicit obligation until satisfied, superseded, waived where legitimately optional, or resolved through the normal project method.

---

## This is a cross-thread scheduling pattern

Deferred catch-up is **not** currently a new `review_mode` enum under Specification 024.

Existing thread modes continue to describe the kind of collaboration:

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

Candidate requirement values:

```text
REQUIRED
OPTIONAL
```

Candidate gate boundaries:

```text
BEFORE_TARGET_MUTATION
BEFORE_THREAD_RESOLUTION
BEFORE_PROMOTION
NONE
```

These values are not yet part of the frozen Specification 024 schema. Until a later mechanical contract is accepted, they may be recorded explicitly in `THREAD.md`, review requests, and the convenience review inbox.

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

A later implementation should derive this view mechanically from per-thread state rather than depend on manual synchronization.

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

A batch must not blur three reviews into one vague endorsement.

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

## Current pressure test

The repository currently exercises this pattern with at least two Claude obligations:

```text
MC-0002
    Specification 024 direct implementation review
    higher priority because Specification 024 classification depends on it

MC-0003
    deferred-review/catch-up architecture review
    deliberately deferrable while other legitimate work continues
```

This is intentional evidence that multiple pending review threads can coexist without a global model lock.

---

## Mechanical follow-up

Specification 024 remains frozen and should not be retroactively expanded.

After Specification 024 is classified and this protocol is reviewed, a later bounded contract may add:

```text
explicit review-obligation metadata
explicit gate-boundary metadata
review-target snapshot semantics
backlog discovery command
generated review-inbox view
stale/superseded obligation checks
```

The mechanism should be justified by real use rather than added merely for completeness.