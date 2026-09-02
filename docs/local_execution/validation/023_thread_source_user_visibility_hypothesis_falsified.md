# Explicit threadSource user visibility hypothesis falsified

**Date:** 2026-09-02  
**Status:** `THREAD_SOURCE_USER_PERSISTS / DESKTOP_VISIBILITY_HYPOTHESIS_FALSIFIED`  
**Scope:** Preserve the bounded H1 experiment that added `threadSource = "user"` to formal Codex thread creation and tested whether that alone made ADS-created threads appear in Codex Desktop `Recent`.  
**Authority:** Negative local-execution evidence. The result rejects one explanation only and does not imply a broader Codex persistence failure.

## Hypothesis

```text
thread/start with threadSource = "user"
    -> Desktop-visible user thread
```

## Result

The one-field candidate was syntax-checked, regression-tested, activated with exact hash/backup guards, and used for a fresh formal Codex task.

Observed:

```text
threadSource persisted as user    PASS
thread persisted normally         PASS
Desktop Recent visibility         FAIL
```

Therefore `threadSource = "user"` is not sufficient to produce Desktop sidebar discovery on the tested build.

The later H6 candidate removes this experimental override because the investigation found no evidence that it contributes to the accepted handoff behavior.

No Codex session, SQLite, history or Desktop catalog data was manually rewritten.

Detailed synthesis: `docs/research/109_codex_desktop_thread_handoff_and_catalog_reconciliation.md`.
