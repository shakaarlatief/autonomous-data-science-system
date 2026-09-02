# Codex Desktop catalog and writer-ownership follow-up

**Date:** 2026-09-02
**Status:** `CATALOG_RECONCILIATION_CHARACTERIZED / WRITER_RELEASE_LADDER_VERIFIED`
**Scope:** Preserve the post-H6 evidence separating transient Desktop visibility, persistent local catalog adoption, and writer-ownership release behavior.
**Authority:** Bounded UI/catalog and lifecycle evidence. It does not authorize private Codex database mutation or forceful writer takeover.

## Catalog follow-up

A fresh externally created ADS thread opened successfully by `codex://threads/<threadId>` and could appear transiently in Desktop `Recent` while still having no durable row in Desktop `local_thread_catalog` and no synchronization-watermark advance.

Manual Desktop `Vastzetten` / pinning then caused a broader Desktop-owned reconciliation that imported the target external thread and other missing genuine threads into the local catalog. Manual unpinning left the target durable in ordinary `Recent`.

Observed pattern:

```text
hidden genuine ADS thread
-> exact deeplink opens it
-> transient Recent visibility may occur without durable catalog row
-> manual pin triggers broad Desktop catalog reconciliation
-> manual unpin leaves target durable in normal Recent
```

The investigation also identified the official protocol concept `thread/section/move`, but no bounded ADS public tool for programmatic pin/unpin was accepted or live-verified. Private database writes and arbitrary App Server RPC wrappers remain rejected.

## Writer-ownership release ladder

The same persisted thread was used to test what releases Codex Desktop's writer ownership.

```text
Desktop owns thread -> switch to home/new chat       DOES NOT RELEASE
Desktop owns thread -> close Desktop window          DOES NOT RELEASE
Desktop owns thread -> fully quit Desktop with Ctrl+Q RELEASES
```

After full Desktop quit, ChatGPT/Codexless successfully resumed the exact persisted thread and completed a new turn. This establishes that Desktop window/navigation state and Desktop writer ownership are distinct on the tested build.

## Classification

```text
exact deeplink openability                           PASS
transient Recent != durable catalog                  VERIFIED
manual pin can trigger broad catalog reconciliation  VERIFIED
manual unpin retains reconciled target in Recent     VERIFIED
programmatic section move through ADS                NOT VERIFIED
switch-away release                                  FALSIFIED
window-close release                                 FALSIFIED
full Desktop quit release                            PASS
force takeover                                        REJECTED
```

Detailed synthesis: `docs/research/110_durable_bidirectional_codex_thread_handoff_and_cooperative_release.md`.
