# Checkpoint 319: Hybrid PDF Access Live Source Published, Restart Pending

**Date:** 2026-09-06
**Status:** LIVE SOURCE PUBLICATION VERIFIED / CONTROLLED RESTART PENDING
**Checkpoint class:** LOCAL EXECUTION / DIRECT CHATGPT FILE ACCESS
**Project stage:** Research 120 automatic hybrid PDF direct-source routing
**Scope:** Preserves qualification and guarded installed-source publication of the bounded `codex.pdf_access` public facade over the Research 120 hybrid PDF core. The installed source/test bytes match the qualified candidate, while the currently running MCP process intentionally remains on preview.15 / 59 tools until the controlled restart.
**Authority:** Research 120 defines the architecture. Validation 077 contains the detailed publication evidence. `docs/local_execution/OPERATIONS.md` owns the exact restart/reconnect/app-refresh procedure.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-18`
**Conversation title:** `18 - Astra Architecture Review and Multimodal Handoff Continuation`
**Primary collaborator:** ChatGPT

Checkpoint 318's remaining implementation seam is now closed at the source-publication level. The candidate public facade is `codex.pdf_access`, with deterministic intents:

```text
native
text
visual
mixed
auto
```

The facade routes over the already-qualified direct-source primitives and managed derivatives:

```text
small native PDF
    -> unchanged whole-source resource_link

large native PDF
    -> deterministic managed native PDF parts

individually oversized native page
    -> embedded text + rendered-page fallback

text / visual / mixed <= 192 MiB
    -> direct source processing

text / visual / mixed > 192 MiB
    -> bounded page/range isolation
    -> cached text / render over the isolated artifact
```

The candidate also fixes the first managed-cache product defaults at 2 GiB total artifact bytes and a 30-day idle horizon, keeps active artifact/resource leases eviction-safe, caps one native result at 48 PDF resource links, and shares one total embedded-text budget across oversized-page fallbacks.

Pre-publication qualification passed:

```text
private core regression       49 / 49 PASS
bounded Git fetch regression  PASS tools=60
bounded Git pull regression   PASS tools=60
document file-read regression PASS tests=7
document render regression    PASS tests=10
document resource-link        PASS tests=9
image-read regression         PASS tests=7
public surface registration   PASS tools=60
```

The user then executed the exact guarded host PowerShell publication helper from an ordinary host shell. Independent read-only post-publication verification through the still-running Codexless bridge established:

```text
published source files matching qualified candidate   17 / 17
adapted installed regression files matching staging    4 / 4
source workspace writes                                 NONE
runtime authority widening                              NONE
manual source-PDF upload                                NONE
```

All ten expected-new hybrid-routing source modules are now present in the installed Codexless source tree, and every changed/new source SHA-256 matches the private qualified candidate.

The active process was deliberately not restarted by publication. Direct health evidence immediately after publication remains:

```text
version       0.1.1-preview.15-host-capability-probe
toolCount     59
tunnel health 200
tunnel ready  200
```

This is the expected restart-pending state. It proves disk publication without claiming that `codex.pdf_access` is already callable in the active process.

Private implementation/publication evidence is synchronized at:

```text
85b1de4bad00e71a723a6c7e3a89b959b2582241  Qualify hybrid PDF public facade candidate
8e2b98cfe5cd7eecafb9764dfd9e29b5602638d4  Record hybrid PDF live source publication
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflightOk=true
```

The next action is not more PDF implementation. It is the repository-authoritative controlled activation sequence:

```text
follow docs/local_execution/OPERATIONS.md
    -> stop tunnel first while keeping its Git Bash shell open
    -> stop and restart Codexless
    -> verify local health reports preview.16 and toolCount 60
    -> restart tunnel
    -> verify tunnel healthz 200 and readyz 200
    -> refresh the existing ChatGPT developer MCP app
    -> use a fresh disposable chat for discovery
    -> qualify codex.pdf_access end to end on representative PDFs
```

Do not infer live 60-tool activation, host materialization, managed-part delivery, or mixed text/image behavior until that post-restart host qualification is performed.

```text
CHECKPOINT_319 = HYBRID_PDF_ACCESS_LIVE_SOURCE_PUBLISHED_RESTART_PENDING
```