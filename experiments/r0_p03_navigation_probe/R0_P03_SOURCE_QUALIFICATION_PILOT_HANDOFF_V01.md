# R0-P03: bounded non-arm source-family qualification handoff

**Date:** 2026-11-10
**Status:** TWO_EXACT_LOCAL_REVIEW_PACKETS_CREATED_AND_VERIFIED / NEW_EXTERNAL_DISCLOSURE_NOT_YET_AUTHORIZED
**Purpose:** Test a source-family evidence-qualification method, not certify the whole 2,539-source world by sampling and not author new scored tasks.

## 1. Owner-controlled local inputs

All paths are relative to the repository. Two real, deterministic files exist in the **ignored, local-only** directory:

```text
.venv/.r0_p03_source_qualification_pilot_v01/
    R0_P03_SOURCE_QUALIFICATION_CALIBRATION_RESTRICTED.zip
    R0_P03_SOURCE_QUALIFICATION_FALSIFICATION_RESTRICTED.zip
    R0_P03_SOURCE_QUALIFICATION_PILOT.safe-receipt.json
```

These ZIPs contain original historical source bytes that may include old navigation conclusions, model-arm comparison design, historical task hints and sensitive experimental context. They are *not* a future author-facing source world. They must not be committed, attached to this coordination chat, exposed to future scored primary authors, or sent to an external model without a **new explicit owner authorization scoped to this additional disclosure**. The previous Wave0 authorization applied only to its ten sources and does not automatically cover these packets.

Calibration ZIP SHA-256:

```text
4b4e8a60eabdb7cb033c165bad5ae40b2f0ae8fc009ba6ab3d4c3b7b840dcc27
```

Falsification ZIP SHA-256:

```text
3d7236f3b69d496fd99d597f452ac5dec108716655b0724f80bbc2971c66c4b3
```

The first packet has 16 sampled source cases across eight frozen strata, including two unsupported representations that are explicitly HOLD until their real original bytes can be inspected. It provides 53 readable source/context files. The second independently selected 16-case packet remains **withheld** while the calibration rule is developed, with 58 readable files and two unsupported-representation HOLD cases. One case may have several linked source files. The 32 cases are not all the original records included in the packets.

Exact source pin: `c57556a8bf993a1d327e9197acb7b7c745071cd8`.

## 2. Critical experiment boundaries

This is an **unscored source qualification pilot**. The 16+16 selection is deliberate risk-stratified method calibration and falsification, not a statistically random or representative sample permitting blanket admission of 2,003 critical sources or 406 preliminary candidates. Review of the remaining sources must still be proportionate to authority, exposure risk, missing context and task-independent evidence sufficiency.

The **calibration** recipient must be one fresh, separate non-arm source-status reviewer with no exposure to future task authoring, neutralized legacy gold, reference writing, B0–B4 implementation or scoring. They receive only the calibration packet. They should:

1. Verify actual source accessibility and report tool/prior-exposure limitations before reading the packet.
2. Examine the exact original source versions and supplied context. Treat reference edges as lexical mentions only. Identify old answer contamination, current versus historical authority, required original links and observed validation versus claims of validation.
3. Write a prospective, source-independent qualification **rule** that states which observable evidence licenses a status, and what induces `HOLD` or exclusion. The rule must cover false-authority and false-disclosure exclusions and must not rely on source names, old task answers, comparator rankings, or citation proximity as decisive labels.
4. For each calibration case, produce a source-bound proposed decision, best falsifier, missing evidence or representation, and a clear rationale. Do not automatically admit any source.
5. Return **two separate outputs**: an explicitly source-free, publicly shareable proposed family-rule specification with no case IDs, source excerpts or task-answer claims; and a separate **restricted case-evidence report**, retained only by the owner. Neither file alone authorizes admission.

The owner must freeze the rule bytes and source/context privileges before revealing the second packet. Avoid reauthoring the rule after looking at heldout cases.

A **different separate non-arm falsification reviewer**, preferably isolated from the calibration case reports, should receive only the frozen rule and the heldout packet. Their objective is to challenge the rule on exactly those real cases, reporting erroneous potential author admission, unjustified exclusion, insufficient original context, unrendered media and cases where eligibility cannot be decided. The restricted case-specific findings stay outside the coordinator and all future task, arm and scoring actors; the safe aggregate reports exact cohort completion, detected material rule failures and explicit HOLDs.

**Stop, not endless loop:** a material false-admission or substantial false-exclusion case invalidates an unqualified rule, not the experiment itself. Make a bounded, source-grounded amendment only if the failure has a clear generalizable cause; otherwise narrow the admissible source world prospectively or HOLD that family. Never lower scored primary task capacity requirements to match a conveniently narrowed source world.

## 3. Fixed sampling logic

The calibration and holdout each have two cases from each prospective, disjoint evidence stratum:

```text
STATUS_CORE_CITED
STATUS_CROSS_LINKED
STATUS_FLAGGED
STATUS_OTHER_UNREACHED
STATUS_UNSUPPORTED
VALIDATION_FLAGGED
VALIDATION_LINKED
VALIDATION_UNLINKED
```

Every case is selected by a fixed SHA-256 order of the historical commit, group identifier, exact path and Git blob ID. Four direct neighboring source texts at most are included for each case, prioritizing cross-family validation/status and original orientation/governing context. Full source bytes are never truncated inside the ZIP, but **not all relevant context can fit in four neighbors**, so omission is explicit and never assumed immaterial.

All other 2,539 sources remain recorded in the source-world ledger and `NOT_ADMITTED`. Unlinked and unsupported strata are intentionally sampled as controls against false exclusions. The holdout source **content** is excluded from the calibration ZIP even when a calibration source cites a holdout case. The source filenames or textual references in the originals may still incidentally reveal related historical context; no full provider-level memory independence is claimed.

## 4. Reproducibility and use after permission

Read-only recomputation under ordinary project PowerShell:

```powershell
Set-Location 'C:\Projects_Data\autonomous-data-science-system'
& .\.venv\Scripts\python.exe -B -m experiments.r0_p03_navigation_probe.prospective_source_qualification_pilot . --verify-only
```

The output must contain `SOURCE_QUALIFICATION_PILOT_REPRODUCIBILITY=PASS` and source-free hashes/stratum totals. **Do not rerun the creation command**, which is no-overwrite and the same packets already exist.

A model reviewer must not receive all repository access, the local `.venv` directory, the Wave0 owner-private CMS/dossier, both packets simultaneously, or the downstream scored reference/candidate arms. If new authorization is granted, the owner personally transfers **only the calibration ZIP** to the new, isolated role. The challenge remains sealed from that role until the prospective rule is frozen.

## 5. Acceptance must remain substantive

This workflow prepares a **testable source eligibility rule**, not a mechanism for retroactively rationalizing arbitrary admission. Source family classification still needs independent substantiation against exact pinned evidence, accepted/current authority, genuine implementation receipts, inherited links, temporal qualifiers and combined document-exposure leakage.

A good pilot result supports scoped expansion and targeted review rather than author-world freeze by itself. The actual R0-P03 objective remains prospective 12-task authorship, nine separate neutralized legacy cases, independent protected gold and fair B0–B4 model-arm evaluation under Research 513 and 559.
