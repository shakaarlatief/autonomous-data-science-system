# Checkpoint 33: P0 Open Feature-Concern Repair-Priority Correction

**Date:** 2026-08-09  
**Status:** Historical mixed checkpoint  
**Checkpoint class:** MIXED  
**Project stage:** Prototype V0 held-out protocol and implementation preparation  
**Scope:** Records the historical milestone described by this checkpoint: P0 Open Feature-Concern Repair-Priority Correction.  
**Authority:** Historical provenance; current canonical documents and promoted sources govern current interpretation.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Record a second P0 controller edge case identified by inspection before the first deterministic test run and before any real-model P0 trajectory.

## Edge case

K-INFO-003 can legitimately remain OPEN during Phase 1 because feature timing may still be only provisionally known. If later authoritative evidence invalidates a feature-eligibility assumption, the existing scoped K-INFO-003 question must become a repair priority even if its status was already OPEN.

The initial `reopen` helper only added repair priority when a knowledge instance transitioned from RESOLVED/BLOCKED to REOPENED. An already-OPEN question therefore could have remained non-repair-priority after material invalidation.

## Correction

The operational controller now treats invalidation of a state object tagged `feature_eligibility` or `validation_regime` as a repair event for the corresponding existing knowledge instance.

It:

```text
keeps the existing scoped knowledge instance;
reopens it when a status transition is needed;
and adds priority:repair to any still-open/reopened question or open obligation.
```

This means final model lock can be prospectively blocked until the material repair concern is resolved, without creating duplicate questions.

## Regression test

A third controller test now verifies that an already-OPEN K-INFO-003 question receives `priority:repair` after authoritative invalidation.

P0-related tests awaiting local execution are now:

```text
9 tests in test_p0.py
3 tests in test_p0_controller.py
12 new tests total
```

The pre-P0 suite contained 34 passing tests, so the expected total is now:

```text
46 passed
```

No real P0 model call has occurred and no held-out artifact, evaluator rule, knowledge component, or continuation threshold changed.
