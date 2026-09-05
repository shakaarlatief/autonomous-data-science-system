# Validation 062: Resource-Link Host Boundary Localized and Native Auto-Review Live-Qualified

**Date:** 2026-09-05
**Status:** PASS / HOST BOUNDARY LOCALIZED / NATIVE AUTO-REVIEW LIVE-QUALIFIED / BROWSER FALLBACK OPEN
**Research:** Research 117, with cross-reference to Research 113/114 and Validation 035

This validation preserves the post-Validation-061 evidence for the MCP `resource_link` whole-PDF path and the reuse-first correction for repeated routine Codex in-turn approvals.

## 1. Clean near-threshold resource-link host tests

Fresh no-folder single-file tests produced the following direct evidence:

```text
7,305,623 B  Lecture-BDS-4-24-25-print.pdf  PASS
7,417,428 B  Lecture_4_Week_2.pdf            PASS
7,993,210 B  CheatSheet_A4_FullWidth.pdf    FAIL
8,715,014 B  32.LinearModels2.annotated.pdf FAIL, independently repeated
```

Confirmed PASS cases:

```text
Lecture-BDS-4-24-25-print.pdf
    size       7,305,623 bytes
    SHA-256    2cfb45e47b32b41a00435530250a6aa696bbdffb1779c140824b29d41479dc06
    host ID    file_000000003e248210853078fd61005fdc
    host path  /mnt/data/Lecture-BDS-4-24-25-print.pdf

Lecture_4_Week_2.pdf
    size       7,417,428 bytes
    SHA-256    0b38655c0412c4be1e1bb12306f1a4c996ac2727fd12a733292b01bddcfe725c
    host ID    file_00000000b42081f48ba7089a487679ad
    host path  /mnt/data/Lecture_4_Week_2.pdf
```

Confirmed FAIL cases:

```text
CheatSheet_A4_FullWidth.pdf
    size       7,993,210 bytes
    SHA-256    dfc4f94ac917207139f2a05b6ea03bb9fdaef4b6dd15b4efb919303aae0db61a
    ADS resource-link preparation  PASS
    next-turn host materialization FAIL
    next-turn full-PDF access      FAIL

32.LinearModels2.annotated.pdf
    size       8,715,014 bytes
    SHA-256    9b4bb8efa6f1adfc27f1cacbfc7b77e1c4335d1629962235f64121ad2768f3e9
    ADS resource-link preparation  PASS
    clean next-turn materialization/full-PDF access FAIL
    independent clean repetition   FAIL again
```

The currently observed clean host materialization interval is:

```text
highest confirmed PASS  7,417,428 bytes
lowest confirmed FAIL    7,993,210 bytes
interval width              575,782 bytes, approximately 0.55 MiB
```

This is not an exact or universal ChatGPT host maximum. Codexless resource-link preparation continues to succeed beyond this interval, including the repeated 8,715,014-byte case. The first limiting hidden host materialization/resolution layer remains unobserved because no explicit host-side `resources/read`, transport, or materialization error is surfaced.

## 2. Direct HTTPS/raw-PDF route rejected for the current tunnel

A bounded investigation classified:

```text
DIRECT_HTTPS_RAW_PDF_CANDIDATE = NOT_FEASIBLE
```

HTTPS `resource_link` values are MCP-valid, but the current Secure MCP Tunnel is an MCP JSON-RPC transport and does not expose an arbitrary public raw-GET origin for local PDF bytes. No direct-HTTPS candidate code was published. A future route would require a separately supported public HTTPS download gateway or an explicit raw-GET tunnel mode.

## 3. Repeated in-turn approval weakness and reuse-first mitigation

Validation 035 had already reproduced the supervision-liveness gap: ChatGPT can finish its assistant turn while Codex continues, Codex can later reach an approval, and ChatGPT does not autonomously wake to resolve it. Codex Desktop also could not service the approval while Codexless owned the active writer.

Research into the current Codex App Server showed that Desktop's `Approve for me` behavior maps to the App Server reviewer `auto_review`. The accepted Codexless formal-agent route therefore keeps the existing bounded permission profile while explicitly requesting:

```text
approvalPolicy     = on-request
approvalsReviewer  = auto_review
permissions        = existing resolved profile such as ads-direct-git
```

The separate ChatGPT-side `Call Codex?` consent gate remains enabled. Full access / `danger-full-access` was not introduced.

Pre-publication qualification:

```text
old live executor SHA-256
255BAD09DBCFD11AA5CB66305073EF0ADD22B5D543103F77AD87B5351F568C9E

qualified candidate SHA-256
CF13405B4E65EFCDBDFE13FFB7C1A63A1A37A3467BA590B2B342262D80769BE7

CODEXLESS_NATIVE_AUTO_REVIEW_REGRESSION=PASS
```

One formal Codex publication attempt was deliberately interrupted after it reproduced the old reviewer behavior while attempting the `%LOCALAPPDATA%` replacement. No live replacement occurred in that blocked turn. This is consistent with the separate runtime-maintenance authority and active-writer architecture questions tracked by AB-002, AB-004 and AB-017.

The user then executed the exact guarded host publication manually. Accepted output included:

```text
NATIVE_AUTO_REVIEW_PUBLICATION_PREFLIGHT=PASS
NATIVE_AUTO_REVIEW_PUBLICATION_RESULT=PASS
backup SHA-256 = 255BAD09DBCFD11AA5CB66305073EF0ADD22B5D543103F77AD87B5351F568C9E
live SHA-256 after = CF13405B4E65EFCDBDFE13FFB7C1A63A1A37A3467BA590B2B342262D80769BE7
RESTART_PERFORMED=false
```

After the repository-authoritative restart/reconnect sequence, Codexless reported `0.1.1-preview.14`, `codexless-public-preview-v2`, 56 tools, and the tunnel returned HTTP 200 for both `/healthz` and `/readyz`.

A fresh formal Codex qualification retained the initial `Call Codex?` approval and existing `ads-direct-git` authority, then ran routine read-only PowerShell and `git status` commands. No in-turn approval surfaced, Codexless never entered `awaitingApproval`, and the terminal result reported:

```text
approvalPolicy = on-request
approvalsReviewer = auto_review
NATIVE_AUTO_REVIEW_LIVE_QUALIFICATION=PASS
```

The qualification completed in 18 seconds and modified no files.

This proves the routine-command case only. Native Auto-review may still reject or escalate risky actions, and the separate autonomous wakeup, completion/error notification, and active-writer transfer questions remain open.

## 4. Browser fallback status

After the Auto-review restart, the model-free Browser status remained:

```text
status      unavailable
reason      chrome_skill_unavailable
chromeSkill missing
nodeRepl    unknown
```

Therefore Browser upload compatibility remains unresolved and is the next Research 117 fallback investigation. Machine Learning remains read-only, and no Chrome/native-host/plugin installation state was modified by this validation.

Accepted result:

```text
RESOURCE_LINK_HOST_BOUNDARY_LOCALIZED=PASS
DIRECT_HTTPS_RAW_PDF_CANDIDATE=NOT_FEASIBLE
NATIVE_AUTO_REVIEW_LIVE_QUALIFICATION=PASS
BROWSER_UPLOAD_COMPATIBILITY=UNRESOLVED
```
