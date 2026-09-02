# Formal Codex thread persistence and Desktop visibility baseline

**Date:** 2026-09-02  
**Status:** `FORMAL_CODEX_THREAD_PERSISTENCE_VERIFIED / DESKTOP_VISIBILITY_NOT_OBSERVED`  
**Scope:** Preserve the first real Codex model call through ADS/Codexless, prove that it created normal persistent Codex state, and separate persistence from Codex Desktop sidebar discovery.  
**Authority:** Bounded local-execution evidence only. This record does not define final Desktop integration behavior.

## Result

A minimal read-only Codex Agent task was started through the formal ADS Codex interface and completed successfully.

Observed properties:

```text
real Codex model turn                 PASS
result returned through ADS           PASS
standard Codex session JSONL exists   PASS
core Codex thread row exists          PASS
completed turn exists                 PASS
normal user input item exists         PASS
agent response exists                 PASS
repository mutation                   none
Codex Desktop Recent visibility       NOT OBSERVED
```

The session lived under the normal `%USERPROFILE%\.codex` persistence substrate. Therefore an ADS formal-agent result is a genuine Codex thread, not merely transient bridge output.

## Classification

```text
THREAD EXISTENCE / PERSISTENCE     VERIFIED
DESKTOP SIDEBAR DISCOVERY         SEPARATE UNRESOLVED LAYER
```

This baseline invalidates the inference that failure to appear in Desktop `Recent` means the thread was not created correctly.

Detailed synthesis: `docs/research/109_codex_desktop_thread_handoff_and_catalog_reconciliation.md`.
