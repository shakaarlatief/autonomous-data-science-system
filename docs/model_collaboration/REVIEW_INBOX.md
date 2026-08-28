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
ChatGPT
```

Current checkpoint:

```text
251
```

## Critical current state

The first holistic integrated Cockpit at:

```text
8e554d847bb3b6318db432abcb5dff742f0fa523
```

failed fidelity review and remains an excluded implementation source.

The Checkpoint 250 implementation-provenance recovery is now complete. The repository contains an exhaustive Phase-C decision ledger, a 23-entry implementation manifest, a deterministic validator and a full-history GitHub Actions gate.

Exact-history verification has passed:

```text
workflow run 33156357834
Cockpit implementation manifest: PASS
entries=23 required=19 non_promotable=4
exact historical source verification: PASS
```

Primary current evidence:

```text
docs/checkpoints/251_cockpit_implementation_provenance_recovered_and_reintegration_opened.md
docs/research/089_cockpit_implementation_provenance_recovery_completion_and_exact_history_gate.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
```

## Current gate

The provenance gate is closed. The integrated fidelity gate is open.

```text
replacement holistic integration
    -> source-faithful reuse/porting
    -> preserve all MUST_PORT / MUST_PRESERVE items
    -> retain provisional items as provisional
    -> do not select deferred/rejected/evidence-only candidates
    -> minimum unresolved shell glue only, explicitly provisional

then

integrated fidelity validation against exact accepted targets

then

human holistic product review
```

No Claude review is currently required. ChatGPT is the current actor for controlled reintegration.

Production `/cockpit` remains untouched.
