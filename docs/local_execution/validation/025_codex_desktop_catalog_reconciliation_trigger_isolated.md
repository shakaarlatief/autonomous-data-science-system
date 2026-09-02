# Codex Desktop catalog reconciliation trigger isolated

**Date:** 2026-09-02  
**Status:** `DESKTOP_CATALOG_RECONCILIATION_TRIGGER_REPRODUCED / COMPOSER_ONLY_NEGATIVE`  
**Scope:** Preserve the H5 experiments separating exact thread openability from Codex Desktop `Recent`/sidebar catalog adoption and identify the smallest repeatedly observed Desktop-side reconciliation trigger.  
**Authority:** Bounded UI/catalog integration evidence. This record does not authorize direct modification of Codex Desktop private databases.

## Core architecture finding

Read-only inspection established that valid ADS-created Codex threads can exist in core Codex state while being absent from Desktop's separate local thread catalog.

Therefore:

```text
core Codex thread persistence
    !=
Desktop local_thread_catalog / Recent
```

## Reproduced reconciliation

Creating and completing a genuine Desktop-native new thread caused Desktop's local catalog synchronization watermark and observation sequence to advance and imported previously missing ADS-created threads.

This effect reproduced more than once.

## Negative discriminators

The following did not independently trigger catalog adoption in bounded tests:

```text
open exact external thread by codex://threads/<id>        NO
continue already-open external thread                     NO
bring/reopen Desktop                                      not a reliable trigger
open New Chat composer without sending                    NO
```

For the composer-only test, a fresh ADS thread remained absent and both the catalog watermark and observation sequence remained unchanged.

## Classification

```text
external ADS thread directly openable                     PASS
Desktop can later catalog external ADS threads            PASS
Desktop-native new-thread completion triggers reconcile   REPRODUCED
composer-only reconcile                                   FALSIFIED
supported explicit sidebar reindex API                    NOT IDENTIFIED
private DB editing as workaround                          REJECTED
```

The deterministic integration seam is therefore the canonical thread deeplink, not an assumption of immediate sidebar registration.

Detailed synthesis: `docs/research/109_codex_desktop_thread_handoff_and_catalog_reconciliation.md`.
