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
227
```

Current browser route:

```text
http://localhost:5173/design-lab/connector-directionality.html
```

Exact browser implementation target:

```text
07d573b6569b9f09a3b7e00936f3eadecee721b3
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

Current connector model:

```text
connector treatment
    Clean
    Micro dots
    Frame sockets
    Direction arrows

hover / focus
    separate reveal / emphasis mechanism

semantic direction
    system-owned
```

Only one terminal treatment should normally be active at a time. Hover may reveal or intensify that selected treatment rather than adding a second terminal symbol.

## Latest retained connector refinements

```text
42ec63d17095753dc4ab97628cd859473cbdf5e8
    Micro-dot / hover-port circles mostly outside the work-unit perimeter

183264bdd07783eaa2354894592f2cf4a076b6ec
    Frame-socket outline / glow follows active relation color
```

## Active simplified directionality review

The first D0-D3 browser mixed arrows with attachment-style compatibility controls. Human review simplified the experiment.

Current comparison:

```text
D0  Undirected      A - B
    no arrow

D1  Forward         A -> B
    K3-style arrow docked directly to B

D2  Reverse         A <- B
    exact same arrow docked directly to A

D3  Bidirectional   A <-> B
    same arrow at both endpoints
```

No dots or sockets are mixed into this directionality comparison.

Current human gate:

```text
verify simple edge-connected arrow grammar
-> if accepted, treat directionality as sufficiently converged
-> then open semantic relation-class exploration
```

C5 Internal Layout Grammar remains deferred to semantic zoom / information-density work.
