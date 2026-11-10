# Research 627: Prospective source-family qualification rule, calibration and falsification

**Date:** 2026-11-10
**Status:** REAL_EVIDENCE_CALIBRATION_AND_HELDOUT_PACKETS_REPRODUCIBLE / NO_SEMANTIC_RULE_OR_ADMISSION_YET
**Scope:** Bridge task-independent pinned historical evidence tracing (Research 626) to a *finite, independently falsifiable* prospective source-status method. Do not release sources to the scored author, generate questions or treat sampled cases as population authority.
**Basis:** Research 513, 559, 576, 590–593, 620–626; Validations 299–312.
**Authority:** Coordinator engineering creates candidate review fixtures, not substantive source-status judgments; separate independent non-arm semantic role still required. Previous Wave0 authorization does not cover another recipient.
**Source pin:** `c57556a8bf993a1d327e9197acb7b7c745071cd8`.
**Operational state:** Checkpoint 898, Specification 028 unchanged.

## 1. Why source review must avoid both extremes

The previous 2,539-record exact-Git corpus audit found 406 preliminary candidates and 2,133 historical supplemental review records, including 1,756 historical research/checkpoint records and 247 validation records (Research 625). Research 626 found many explicit historical status/validation citation mentions but no semantic authority guarantees. A new real, source-free check of the full critical-family textual citation graph revealed:

```text
CRITICAL_HISTORICAL_AND_VALIDATION_RECORDS=2003
UNDIRECTED_CITATION_CONNECTED_COMPONENTS=192
LARGEST_CONNECTED_COMPONENT=1769
LARGEST_COMPONENT_HISTORICAL_STATUS=1522
LARGEST_COMPONENT_EXECUTION_EVIDENCE=247
OTHER_COMPONENT_SIZES_TOP=18,7,4,4,4,2,2,2,2
SINGLETON_HISTORICAL_RECORDS=175
SINGLETON_VALIDATION_RECORDS=0
```

This immediately rules out a naive plan to use weakly connected components as independent review batches: almost all validation evidence belongs to one enormous *citation-connected* component, and many historical records have no such detected connection. Neither all-at-once manual review nor isolating the small near-core frontier constitutes a scientifically defensible path.

The next step is not to infer a semantic source world from path labels. It is to test whether prospective, evidence-grounded **family-level eligibility rules** can be formulated with explicit HOLDs, source-level escalation triggers and falsification of both false admission and false exclusion. A successful pilot can guide proportionate scaling. It does not automatically approve unreviewed sources.

## 2. Actually implemented and pinned pilot

Added `experiments/r0_p03_navigation_probe/prospective_source_qualification_pilot.py` and fabricated-only negative-control tests. From the real pinned source ledger and exact citation graph, it partitions all **2,003** critical historical/validation records into exactly eight nonoverlapping, task-independent evidence/risk strata. Stratum precedence prevents double-counting flagged/core-linked records:

| Prospective stratum | Real pinned records |
| --- | ---: |
| Historical status, cited from preliminary core | 214 |
| Historical status, other cross-family linked | 231 |
| Historical status, lexical/path risk flagged | 106 |
| Historical status, other not reached | 1,195 |
| Historical status, unsupported representation | 10 |
| Execution validation, risk flagged | 8 |
| Execution validation, linked to historical status | 231 |
| Execution validation, otherwise unlinked | 8 |
| **Total** | **2,003** |

The sample then takes **exactly two cases per stratum per role** by fixed SHA-256 order of original Git pin, stratum, path and blob identity, creating disjoint `CALIBRATION` and `FALSIFICATION` seed sets. It is a deliberately **targeted rule-calibration/falsification pilot**, not a random survey, statistically representative sample or authority certificate.

For each sampled seed, the locally sealed review packet contains original full bytes when text-supported, plus at most four actual pinned adjacent source texts selected by a predetermined preference for cross-family context then governing/orientation context. Literal reference evidence, source identity, omission counts, unsupported-media and unverified context remain visible to reviewer. Future holdout seed **contents** are excluded from the first packet, even where the calibration evidence references them. Original text could incidentally mention a heldout source's name, so complete conceptual independence is not claimed.

Real local-only, no-overwrite artifacts, explicitly under ignored `.venv`:

```text
R0_P03_SOURCE_QUALIFICATION_CALIBRATION_RESTRICTED.zip
    16 cases, 53 readable source/context files, 2 unsupported cases
    SHA256=4b4e8a60eabdb7cb033c165bad5ae40b2f0ae8fc009ba6ab3d4c3b7b840dcc27
    bytes=800193

R0_P03_SOURCE_QUALIFICATION_FALSIFICATION_RESTRICTED.zip
    16 disjoint cases, 58 readable source/context files, 2 unsupported cases
    SHA256=3d7236f3b69d496fd99d597f452ac5dec108716655b0724f80bbc2971c66c4b3
    bytes=1384419
```

The packets are not owner-private Wave0 artifacts, but **still contain unqualified historical evidence that may include old gold or comparator design**. Do not send them to public ChatGPT project context, future scored authors, arm builders or evaluators. The coordinator has not used the earlier private Wave0 decision plaintext, authorized a new recipient, sent the packets to a reviewer or applied any source admission.

## 3. Prospective finite scientific procedure

The detailed safe handoff and exact integrity hashes are in `experiments/r0_p03_navigation_probe/R0_P03_SOURCE_QUALIFICATION_PILOT_HANDOFF_V01.md`.

1. **New scoped owner authorization before any external transfer.** Select one distinct non-arm calibration reviewer with only the calibration packet, and no access to the heldout packet, private Wave0 reports, old gold or scored experimental tasks.
2. **Evidence-based rule proposal.** Require a source-independent family eligibility rule grounded in actual original/pinned authority, temporal state, implementation and validation receipts, linked context, old-answer leakage and combined exposure hazards. Each sampled case must have a reasoned proposal or material HOLD, with evidence and strongest falsifier. Separate publicly shareable source-free rule text from owner-held restricted case-specific reasoning.
3. **Freeze rule and future exposure contract before holdout.** Preserve rule bytes/digest and prohibited context. The second packet remains withheld during development.
4. **Independent heldout attack.** A separate non-arm reviewer tests the frozen rule on the actual falsification cases, recording false-authority admission, missed essential evidence, representation/context insufficiency and other material failures. Neither stage permits immediate scored-author disclosure.
5. **Scale only a supported, falsifiable rule.** Avoid extrapolating a small diagnostic sample to every record. Where case evidence is insufficient, HOLD or independently inspect targeted linked evidence. Disallow easy tasks chosen to fit a prematurely narrowed source world. The 406 preliminary candidates must also be qualified.

This creates a **finite, falsifiable gate** rather than four-actor reviews of every source. A material failure requires bounded cause analysis or a narrower admitted scope with accountable coverage HOLD; it must not be retroactively absorbed into post-hoc score selection.

## 4. Engineering evidence and limits

The real artifact creation succeeded; a distinct `--verify-only` process independently recomputed the two saved ZIPs and receipt byte-for-byte:

```text
SOURCE_QUALIFICATION_PILOT_REPRODUCIBILITY=PASS
CALIBRATION_EXPOSES_FALSIFICATION_SEED_CONTENTS=false
PILOT_SAMPLED_DECISIONS=NONE
POPULATION_SOURCE_ADMISSIONS=0
WORLD=WORLD_UNFROZEN
SCORED_TASKS=NOT_STARTED
```

A further independent ZIP-level read checked exact expected member sets, no duplicates, original blob Git SHA-1, SHA-256 and byte lengths, two cases in every stratum per role, zero seed overlap, and no challenge seed source bytes inside the calibration packet:

```text
INDEPENDENT_ARCHIVE_CHECK=PASS
CALIBRATION_HOLDOUT_SEED_OVERLAP=0
FALSIFICATION_SOURCE_BODIES_IN_CALIBRATION=0
SOURCE_ADMISSIONS=0
```

The local tool validates pinned source identity and refuses cross-cohort content leakage and overwrite. Nine invented-only tests exercise deterministic cohorts, content integrity, missing evidence, tampered source IDs, failed role switching, no overwrite, and unsupported media HOLD. The final integrated tests and repository integrity are independently reported in Validation 313.

The pilot is **not a valid final source-world freeze** and cannot be represented as scientific acceptance. The scored source list, fresh twelve primary tasks, nine separately neutralized legacy cases, independent protected references, and B0–B4 evaluation remain outstanding.

```text
RESEARCH_627=TASK_INDEPENDENT_REAL_SOURCE_QUALIFICATION_CALIBRATION_AND_HOLDOUT_PREPARED
NEW_REVIEWER_OR_POLICY_ACCEPTANCE=NOT_STARTED
SOURCE_WORLD_ADMISSIONS=ZERO
SOURCE_WORLD=WORLD_UNFROZEN
SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
