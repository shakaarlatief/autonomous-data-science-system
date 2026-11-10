# R0-P03: bounded non-arm source-family qualification handoff

**Date:** 2026-11-10
**Status:** FIRST_SEPARATE_CALIBRATION_REVIEWER_REPORTED_16_CASES_COMPLETE / TWO_MARKDOWN_ARTIFACT_IDENTITIES_REPORTED / PUBLIC_RULE_CONTENT_INSPECTION_AND_FREEZE_PENDING / HOLDOUT_WITHHELD
**Purpose:** Test a source-family evidence-qualification method, not certify the whole 2,539-source world by sampling and not author new scored tasks.

## 1. Owner-controlled local inputs

All paths are relative to the repository. Two real, deterministic files exist in the **ignored, local-only** directory:

```text
.venv/.r0_p03_source_qualification_pilot_v01/
    R0_P03_SOURCE_QUALIFICATION_CALIBRATION_RESTRICTED.zip
    R0_P03_SOURCE_QUALIFICATION_FALSIFICATION_RESTRICTED.zip
    R0_P03_SOURCE_QUALIFICATION_PILOT.safe-receipt.json
```

These ZIPs contain original historical source bytes that may include old navigation conclusions, model-arm comparison design, historical task hints and sensitive experimental context. They are *not* a future author-facing source world. They must not be committed, attached to this coordination chat, or exposed to future scored primary authors. The owner **explicitly authorized on 2026-11-10 only the calibration ZIP's disclosure to one new separate non-arm reviewer for rule development and confidential source-case assessment**. The previous Wave0 authorization did not cover these packets; this new authorization does **not** include the heldout falsification ZIP, owner-private Wave0 reports, scored authors, arm builders or reference/scoring roles.

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

A model reviewer must not receive all repository access, the local `.venv` directory, the Wave0 owner-private CMS/dossier, both packets simultaneously, or the downstream scored reference/candidate arms. The required calibration-only authorization was granted on 2026-11-10. The owner now personally transfers **only the calibration ZIP** to the new, isolated reviewer role. The challenge remains withheld from that role until the prospective rule is frozen; holdout disclosure is **not** authorized at this stage.

## 5. Acceptance must remain substantive

This workflow prepares a **testable source eligibility rule**, not a mechanism for retroactively rationalizing arbitrary admission. Source family classification still needs independent substantiation against exact pinned evidence, accepted/current authority, genuine implementation receipts, inherited links, temporal qualifiers and combined document-exposure leakage.

A good pilot result supports scoped expansion and targeted review rather than author-world freeze by itself. The actual R0-P03 objective remains prospective 12-task authorship, nine separate neutralized legacy cases, independent protected gold and fair B0–B4 model-arm evaluation under Research 513 and 559.
## 6. Owner-authorized first calibration transfer and separate-role instructions

On 2026-11-10, the owner replied "Yes, I authorize" to the exact request to share **only the 16-case calibration ZIP** with **one new separate non-arm source-family rule developer and confidential case reviewer**. This scope includes the original 53 readable source/context files and two unsupported-representation HOLD cases. This authorization excludes the later falsification ZIP, the owner-private Wave0 reports, future primary task authors, gold annotators, arm builders, and evaluators.

The calibration archive was rechecked with a metadata/hash-only operation in the original local repository and returned CALIBRATION_PACKET_LOCAL_IDENTITY=PASS, with exact original size 800193 bytes and SHA-256 4b4e8a60eabdb7cb033c165bad5ae40b2f0ae8fc009ba6ab3d4c3b7b840dcc27.

**External transfer has not occurred.** The exposed coordinating chat cannot create a separate ChatGPT Temporary Chat or serve as this independent reviewer. The owner personally attaches only R0_P03_SOURCE_QUALIFICATION_CALIBRATION_RESTRICTED.zip to a new Temporary Chat outside this Project, with no connected apps or earlier restricted/scored context. The falsification packet must remain local and undisclosed.

### Exact new independent reviewer request

You are a separately authorized, **NON-ARM R0-P03 source-family qualification rule calibration reviewer**. You may receive only the attached 16-case historical calibration ZIP and its contained original pinned Git source/context bytes, MANIFEST.json, and REVIEW_BRIEF.txt.

This is a **real non-scored source qualification exercise**, not a scored architecture experiment, hidden-gold annotation, future task authorship, author-world admission or source-world freeze. You must not later become a B0-B4 arm author, primary-task author, independent gold annotator or scored evaluator.

**Before source inspection**, report your actual file tools and original source-access limitations, nested ZIP support, and any material prior exposure relevant to independence. Use only the attached ZIP. Do not access websites, repositories, connected apps, user accounts, project memory, other chats or external sources. Where the original evidence is not inspectable, explicitly mark it inaccessible rather than inventing a finding.

Verify the attached ZIP's exact SHA-256 4b4e8a60eabdb7cb033c165bad5ae40b2f0ae8fc009ba6ab3d4c3b7b840dcc27 and size 800193 bytes if your tools support it. Read the brief and manifest and actually inspect all 16 calibration cases, including their available source/context members and version identities. Do not assume a lexical citation proves semantic dependency, authority or validation success.

Propose a **source-independent, prospective, falsifiable family-level qualification rule** for whole-file candidate, auxiliary-only, exposure prohibition or evidence-dependent HOLD. Evaluate original source identity, historical versus governing currentness, proposed versus realized effects, actual execution/validation receipts, source ownership, old question/answer leakage, comparator/design exposure, combined-source exposure, missing source links and unsupported representations. Include falsification tests for both wrongful admission and wrongful exclusion. Source names, sample order, old task answers, preferred arm and citation proximity must never directly decide statuses.

For each of the 16 calibration source cases, write a **restricted full case assessment**, providing exact source identity and version, actual support and contrary evidence, strongest alternate interpretation, claim and author-disclosure materiality, unresolved evidence, proposed decision or material HOLD, specific falsifier and necessary next action. Absence of material context must not be silently filled in. A status remains PROPOSED and does not admit a source.

**Return two distinct downloadable artifacts:**

1. R0_P03_CALIBRATION_FAMILY_RULE_SOURCE_FREE.md: a complete reusable source-free proposed rule with definitions, decision procedure, materiality and threshold distinctions, authority/currentness requirements, exclusion and HOLD logic, false-exclusion controls, coverage limitations and scope of application. It must contain **no real case paths, source IDs, quotations, case outcomes, prior gold or task-answer hints**.
2. R0_P03_CALIBRATION_CASE_ASSESSMENTS_RESTRICTED.md, or equivalent restricted ZIP: full source-specific assessments for all 16 cases. Keep this separate and confidential. This artifact is for **owner-private custody**, not public Git or this coordinating Project chat.

Respond in chat only with a **safe receipt** listing both artifact filenames, byte lengths, SHA-256 values, how many real original cases and context files were actually inspected, known technical/evidence limitations, and these exact states: RULE=PROPOSED_NOT_FROZEN; SOURCE_ADMISSIONS=ZERO; AUTHOR_WORLD=WORLD_UNFROZEN; FALSIFICATION_HOLDOUT=NOT_ACCESSED. Do not disclose source-specific findings or status counts in the chat response.

If you cannot inspect the evidence or produce actual downloadable files, report the precise limitation and do not claim completion. **Do not request or examine the falsification packet.** A different isolated non-arm reviewer will later test the exact rule frozen from this calibration stage.

### Result custody and next gate

**Actual calibration completion receipt returned on 2026-11-10 (Validation 315):** The separate reviewer reports both Markdown artifacts created and all 16 calibration cases assessed, including two cases whose original representations were unavailable. The self-reported source-free rule is `R0_P03_CALIBRATION_FAMILY_RULE_SOURCE_FREE.md`, 18,580 bytes, SHA-256 `9e402bbaa5f190d72b55e76f38979ea032f90c724e2385e99c20da3e0a4b1268`. The private case evidence is `R0_P03_CALIBRATION_CASE_ASSESSMENTS_RESTRICTED.md`, 64,186 bytes, SHA-256 `2052d5662055f3efbc2eb4d6f98d42a9caf2239ea32bf192f905f983107289cf`. These are reviewer-reported identities, not yet locally independently read back. No real file contents have been accessed by this coordinating session.

**Next action:** Owner downloads and checks both files, keeps confidential case assessments private, and provides **only the actual source-free rule** to this coordinating session for an independent substantive and leakage review. Neither the safe receipt nor the reviewer's self-certification allows freezing or promoting the rule. A qualified rule must be explicitly accepted by evidence, canonical bytes/digest fixed, and access isolation confirmed before the second falsification packet is disclosed to a *different* independent non-arm reviewer under a separately qualified scope. The original calibration authorization does not include holdout disclosure. No source can be admitted solely because its family rule was proposed.
