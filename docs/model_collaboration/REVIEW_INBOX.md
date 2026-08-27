# Model Collaboration Review Inbox

**Date:** 2026-08-27  
**Status:** Current human-readable routing view  
**Authority:** Convenience index only. Per-thread `STATE.json`, `THREAD.md`, frozen requests, exact Git refs, and resolution records remain authoritative.  
**Purpose:** Let a returning collaborator discover pending review/catch-up obligations without relying on private chat memory.

## Current pending model obligation

```text
none
```

Claude completed the MC-0004 divergent work-unit grammar contribution at:

```text
faf18ed9932d60a24dd80589b0ec0ba71c5940fd
```

No Claude action is currently pending.

## Current next actor

```text
human project owner
```

Current checkpoint:

```text
230
```

Current browser route:

```text
http://localhost:5173/design-lab/work-unit-disposition-grammar.html
```

Exact browser implementation target:

```text
565fdeabc1ebaa29f993699a4c0673b29e972be3
```

## Promoted configurable-appearance foundations

Work-unit appearance:

```text
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
```

Connector treatment / hover behavior / semantic directionality:

```text
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
```

## Directionality result

Human review accepted the simplified arrow grammar:

```text
D0  Undirected      no arrow
D1  Forward         arrow at B
D2  Reverse         same arrow at A
D3  Bidirectional   same arrow at both endpoints
```

Exact accepted directionality target:

```text
07d573b6569b9f09a3b7e00936f3eadecee721b3
```

Directionality is sufficiently settled for the current Phase-C design work.

## Relation-class encoding result

Human review selected and accepted:

```text
E5  Hue + Tag
    SELECTED / sufficiently settled for current Phase C
```

Latest accepted relation-class browser target:

```text
497e81f06ba1f9901511449237d1bb9f96b2d108
```

Stroke rhythm from E2/E4/E6 remains preserved:

```text
visually promising
not rejected
not currently assigned to relation class
candidate for another future line-level semantic dimension
```

Representative relation classes remain provisional fixtures and are not a frozen ADS relation taxonomy.

## Active project-disposition review

The current bounded question separates:

```text
category               what the work unit is
project disposition    current slice
runtime state          held out
importance / priority  held out
```

Representative visual-test states:

```text
S0  Active / Current
S1  Recommended / Next
S2  Deferred
S3  Completed
S4  Blocked
S5  Future / Not yet active
```

Encoding families:

```text
P0  Neutral Control
P1  Disposition Hue
P2  Explicit Tag
P3  Tonal Hierarchy
P4  State Rhythm
P5  Hue + Tag
P6  Restrained Hybrid
```

Current human gate:

```text
compare P0-P6 across S0-S5
-> prefer / reject / combine / refine
-> preserve project-disposition visual evidence
-> do not freeze the state ontology
-> keep runtime and importance separate
```

C5 Internal Layout Grammar remains deferred to semantic zoom / information-density work.
