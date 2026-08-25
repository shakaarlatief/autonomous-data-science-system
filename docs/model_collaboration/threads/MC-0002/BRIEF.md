# MC-0002 Brief: Collaboration-State Guard Implementation Review

**Thread:** MC-0002  
**Review mode:** REVIEWED  
**Target contract:** Specification 024  
**Purpose:** Implement and directly review the first machine-readable per-thread collaboration-state coherence guard.

## Problem

MC-0001 established that prose-only ownership rules are too weak for routine multi-model canonical development, while a single global `active_writer` is too coarse.

The bounded task is to implement Specification 024 exactly enough to test whether a scoped per-thread state record plus deterministic validator provides useful mechanical protection without creating disproportionate ceremony.

## Roles

```text
ChatGPT
    TASK_OWNER
    IMPLEMENTER
    target-state write owner during implementation

Claude
    REVIEWER
    may write only new numbered review messages under MC-0002/messages/

Human project owner
    HUMAN_DECIDER only if a genuine project-intent question emerges
```

## Review design

This is deliberately not an independent-then-comparative architecture exercise.

Claude should review the concrete frozen-contract implementation after ChatGPT has preserved the exact pre-review head.

Review should focus on:

```text
Specification 024 gate compliance
state-schema correctness
validator failure modes
whether target vs secondary write surfaces are modeled safely
whether the mechanism stays a coherence guard rather than pretending to authenticate model identity
unnecessary ceremony or under-specification
cross-platform behavior
```

## Success boundary

Classification is one of:

```text
COLLABORATION_STATE_GUARD_ACCEPTED
NEEDS_REVISION
FAILED
```

No canonical Development Method promotion occurs until the review and classification are complete.
