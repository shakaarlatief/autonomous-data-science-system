# Checkpoint 323: Hybrid PDF Direct-Render Serialization Candidate Qualified

**Date:** 2026-09-06
**Status:** PRIVATE CANDIDATE PASS / GUARDED RENDERER PUBLICATION NEXT
**Checkpoint class:** LOCAL EXECUTION / DIRECT CHATGPT FILE ACCESS
**Project stage:** Research 120 automatic hybrid PDF direct-source routing
**Scope:** Preserves the qualified smallest correction for the Checkpoint 322 rendering-dependent intent failure: direct multi-page source rendering now serializes selected pages through separate bounded read-only sandbox executions while preserving the public four-page request contract, source fidelity, aggregate limits and source-drift checks. The complete private hybrid-PDF suite passes 51/51. Live preview.16 has not yet been changed.
**Authority:** Research 120 defines the architecture. Validation 081 contains the implementation, regression and private-preservation evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

Checkpoint 322 localized the fresh-host intent-matrix failure to the Windows buffered direct-render transport rather than to intent routing or page fidelity.

The private renderer candidate now preserves the existing public request contract but executes one read-only sandbox renderer child per selected page. It validates every child protocol, requires consistent page counts, preserves requested order, combines validated records and diagnostics, reapplies the existing per-page and aggregate image limits, and retains final source-identity revalidation.

Candidate regression:

```text
focused serialization tests  2/2 PASS
full hybrid PDF suite         51/51 PASS
```

The exact private preserved boundary is:

```text
ad61a5619165ec5675e75daecdb4fdb29ea6f19a
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflightOk=true
```

The first private push attempt also exposed the already-anticipated AB-020 tracked-path enumeration scaling edge at 32,841 bytes. No integrity rule was weakened or bypassed. The new tests were consolidated into an existing tracked test path, returning the enumeration to 32,753 bytes while preserving 51/51 coverage, after which the normal semantic push passed.

Nothing in this checkpoint establishes that the installed runtime is repaired. The live renderer remains the old preview.16 implementation until guarded publication and controlled restart complete.

The exact next sequence is:

```text
renderer-only guarded publication preflight
-> exact live/candidate hash binding
-> staged regression
-> guarded live file replacement with backup/rollback
-> independent live hash verification
-> full controlled restart from docs/local_execution/OPERATIONS.md
-> verify preview.16 / 60 tools and tunnel health/readiness
-> fresh disposable codex.pdf_access intent-matrix retest
-> >192 MiB facade isolation only after the rendering matrix passes
```

```text
CHECKPOINT_323 = HYBRID_PDF_DIRECT_RENDER_SERIALIZATION_CANDIDATE_QUALIFIED
```
