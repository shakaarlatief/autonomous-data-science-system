# Model Collaboration Review Inbox

**Date:** 2026-08-28  
**Status:** Current human-readable routing view  
**Authority:** Convenience index only. Per-thread `STATE.json`, `THREAD.md`, frozen requests, exact Git refs and resolution records remain authoritative.  
**Repository:** `shakaarlatief/autonomous-data-science-system`  
**Coordination branch:** `v1-cockpit-design-exploration`

## Routing discipline

The repository and coordination branch above must also be named explicitly in any human-to-Claude trigger prompt.

Claude should not infer or switch the coordination branch. If a trigger names a different branch than this authoritative routing state, Claude should stop and report the mismatch rather than choose a branch heuristically.

## Pending model obligation

```text
none
```

Claude Message 010 remains complete at:

```text
8c2c95aec8bf9d53e17500f4a38f9311d19a1e8b
```

## Next actor

```text
human project owner
```

Current checkpoint:

```text
250
```

## Critical current state

The first holistic integrated Cockpit at:

```text
8e554d847bb3b6318db432abcb5dff742f0fa523
```

failed fidelity review and is not an accepted baseline.

Source-level audit found that major accepted decisions and executable artifacts remain preserved, but the holistic browser was manually reimplemented from textual summaries rather than faithfully reused/ported from exact accepted targets.

Primary recovery evidence:

```text
docs/checkpoints/250_integrated_cockpit_fidelity_failure_recovery_audit_opened.md
docs/research/088_integrated_cockpit_fidelity_failure_and_source_of_truth_recovery_audit.md
```

## Current gate

Do not perform further visual design or another holistic rebuild yet.

```text
construct accepted-implementation manifest
    -> exact target SHA
    -> exact source files
    -> invariant properties
    -> allowed integration adaptations
    -> known fixture caveats
    -> fidelity verification

then rebuild by reuse/porting
then validate against exact accepted targets
then resume holistic human review
```

The failed browser remains diagnostic evidence only. Earlier Phase-C decisions remain held at their established level.

Production `/cockpit` remains untouched.
