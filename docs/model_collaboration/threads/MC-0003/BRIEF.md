# MC-0003 Brief: Deferred Review and Catch-Up

**Thread:** MC-0003  
**Date opened:** 2026-08-26  
**Topic:** Preserve intended cross-model review while one collaborator temporarily remains unavailable and another collaborator continues through multiple bounded tasks  
**Authority:** Neutral task brief. It defines the problem and constraints but does not make Research 036 authoritative.

## Problem

ADS must support a real operational condition:

```text
one collaborator temporarily unavailable
another collaborator remains available
project still has legitimate work to do
some completed work is intended for later cross-model review
```

The process must not force the whole project to wait, but it also must not silently convert intended collaboration into SOLO work.

The reviewer may return after several bounded tasks have accumulated.

## Required capabilities

A satisfactory design should explain:

1. when unavailable-reviewer work blocks the affected task;
2. when unrelated bounded work may continue;
3. how intended review remains visible and cannot be forgotten;
4. how the exact review target is frozen;
5. how multiple pending review items are discovered later;
6. how a reviewer catches up one-by-one or in a justified batch;
7. how stale review targets are handled;
8. how downstream work that relied on an unreviewed result is handled;
9. how SOLO tasks avoid acquiring accidental review obligations;
10. how prospective/blind review gates are protected from post-hoc substitution;
11. how the design avoids introducing a global collaborator lock;
12. how the mechanism remains provider-neutral.

## Constraints

```text
repository remains project authority
Specification 024 is already frozen and must not be rewritten post hoc
current collaboration-state guard is a coherence mechanism, not authenticated locking
reviewer usage/availability is an operational constraint, not an authority signal
human should not become a manual memory/transport layer
review obligations should be discoverable from durable project infrastructure
explicit machinery should remain proportionate
```

## Current operational evidence

The project already has a pending Claude obligation in MC-0002.

Claude previously reached its product usage limit during substantial review work while ChatGPT remained available.

MC-0003 is intentionally designed so ChatGPT may preserve the candidate architecture now and Claude may review it later. This should create a real multi-item catch-up situation rather than only a hypothetical design.

## Review expectation

Claude should later challenge the candidate design directly rather than being asked for immediate participation.

The review should focus on whether the proposed blocking/deferral semantics are safe, whether the review-inbox concept creates duplicate authority, whether downstream dependency handling is sufficient, and whether the proposed future mechanical extension is overbuilt or under-specified.