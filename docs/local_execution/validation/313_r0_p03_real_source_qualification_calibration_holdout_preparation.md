# Validation 313: Real prospective source-family qualification pilot and heldout falsification

**Date:** 2026-11-10
**Status:** REAL_LOCAL_CALIBRATION_AND_FALSIFICATION_PACKETS_CREATED / EXACT_BYTE_RECOMPUTATION_PASS / 43_OF_43_INTEGRATED_TESTS_PASS / EXTERNAL_SEMANTIC_QUALIFICATION_PENDING
**Research:** 627, 626, 625; **Protocol:** Research 513 and 559. **Prior validation:** 311–312.
**Scope:** Task-independent historical source-family risk calibration, with an independent heldout falsification packet. Strictly no source admission, private Wave0 access, scored author disclosure or B0–B4 scoring.
**Source pin:** `c57556a8bf993a1d327e9197acb7b7c745071cd8`.
**Checkpoint:** 898 unchanged. **Specification:** 028 unchanged.

## 1. Pinned historical source rule-pilot creation

`experiments/r0_p03_navigation_probe/prospective_source_qualification_pilot.py` reuses the exact verified 2,539-record source ledger and Research 626 citation graph, partitions all 2,003 critical historical-status/validation records into eight *non-overlapping* prospective risk/evidence strata, and samples two original source cases per stratum for **calibration** and another two for **independent falsification**.

Sample selection uses fixed source pin, exact Git blob identity and SHA-256 ordering, not future task text, model-arm success, source authority claims or prior private Wave0 conclusions. Both local-only ZIPs contain complete original pinned textual evidence and up to four explicitly referenced contextual sources per sample, with per-seed context omissions and unverified references recorded. Two historical unsupported-media cases in each packet remain uninspected/HOLD rather than fabricated as text.

Original real outputs:

```text
CALIBRATION_SEED_CASES=16
CALIBRATION_READABLE_EVIDENCE_FILES=53
CALIBRATION_UNSUPPORTED_CASES=2
CALIBRATION_ZIP_BYTES=800193
CALIBRATION_ZIP_SHA256=4b4e8a60eabdb7cb033c165bad5ae40b2f0ae8fc009ba6ab3d4c3b7b840dcc27

FALSIFICATION_SEED_CASES=16
FALSIFICATION_READABLE_EVIDENCE_FILES=58
FALSIFICATION_UNSUPPORTED_CASES=2
FALSIFICATION_ZIP_BYTES=1384419
FALSIFICATION_ZIP_SHA256=3d7236f3b69d496fd99d597f452ac5dec108716655b0724f80bbc2971c66c4b3

ALL_CRITICAL_SOURCE_RECORDS_ACCOUNTED=2003
CALIBRATION_VS_HOLDOUT_SEED_OVERLAP=0
FALSIFICATION_SEED_SOURCE_BODIES_IN_CALIBRATION=0
SOURCE_ADMISSIONS=0
SCORING=NOT_STARTED
```

The **first** `-m experiments.r0_p03_navigation_probe.prospective_source_qualification_pilot .` real run wrote the two files using exclusive creation. A **separately executed `--verify-only`** call recomputed both ZIPs and the aggregate receipt from exact original Git bytes and returned:

```text
SOURCE_QUALIFICATION_PILOT_REPRODUCIBILITY=PASS
```

The checked local path is `.venv/.r0_p03_source_qualification_pilot_v01/`. Both ZIPs are plain ZIP archives, **not encrypted**, and the `.gitignore` rule excludes them from Git. Ignored local files are not equivalent to private ACL protection or a guarantee against other local tools reading them. They were not attached to ChatGPT or sent to another reviewer. The full per-source manifests, content and restricted rule-relevant historical evidence remain local.

## 2. Independent verification

A separate read-only archive-inspection command opened both real ZIPs, checked the exact manifest-derived member names with no duplicates, each included source's SHA-256, Git blob SHA-1 and byte count, canonical manifest bytes, two seed cases per frozen stratum, a disjoint calibration/holdout source-ID roster, the absence of future challenge seed original content from the calibration ZIP, and all zero-admission flags. It returned:

```text
INDEPENDENT_ARCHIVE_CHECK=PASS
CALIBRATION_HOLDOUT_SEED_OVERLAP=0
FALSIFICATION_SOURCE_BODIES_IN_CALIBRATION=0
SOURCE_ADMISSIONS=0
```

The first synthetic test run found a guard-schema difference: the source citation frontier records exact source SHA-256 and Git blob IDs but does not duplicate the byte-length metadata held authoritatively in the original 2,539-record ledger. The extra byte-length comparison produced a protective failure on actual Git data. We removed only that redundant comparison, retained cross-checks for Git ID, SHA-256, role, visibility, risk flags and admission status, and verified **the original already-created real ZIP bytes remained unchanged**, with independent `--verify-only=PASS`. This was not a post-score scientific rule change.

Nine synthetic tests in `tests/unit/test_r0_p03_prospective_source_qualification_pilot.py` cover stable selection, all eight stratum quotas, no overlap and reserved content leakage, actual ZIP original-source metadata integrity, wrong role/status, forged identity, altered source context, no-overwrite and exact-output repair refusal, unsupported representation HOLD, and no author admission.

The combined existing source-world roster, dependency-frontier, neutral retrieval and new pilot regression returned:

```text
43 passed in 9.72s
```

Git `check-ignore -v` directly confirmed `.gitignore:2:.venv/` excludes both actual ZIP files.

## 3. What this does NOT show

The actual 16 calibration cases have **not** been reviewed by a new independent non-arm actor; no family-level qualification rule has been authored, accepted, frozen or challenged. The 16 heldout cases remain separately stored and unreleased. No population-wide source classification can be inferred from sample strata. A path risk flag, lexical reference, and successful ZIP hash prove neither accepted source authority nor safe author exposure.

This coordinator still cannot read or disclose the owner-private Wave0 substantive decision map; it has not used it. The previous Wave0 disclosure authorization applies only to its specific ten-source packet and does not automatically authorize transfer of either new ZIP. A separate, explicit scoped owner permission is required before giving the calibration packet to a newly independent non-arm reviewer.

The exact owner-only/reviewer handoff and risk-of-false-exclusion requirements are described in `experiments/r0_p03_navigation_probe/R0_P03_SOURCE_QUALIFICATION_PILOT_HANDOFF_V01.md`. The source world stays WORLD_UNFROZEN, no new primary scored tasks or neutral nine-case gold were authored, and there is no real B0–B4 score.

## 4. Immediate next decision

With source-free code and tests published, the owner can authorize precisely **one external non-arm calibration reviewer to receive only the first 16-case restricted ZIP**. The second heldout ZIP must remain unavailable until the source-free family qualification rule is written, reviewed and frozen. If the user chooses not to authorize this disclosure, the work can continue only inside the owner-controlled local access boundary, with no claim of an independent external semantic decision.

The goal is to test a bounded, falsifiable source-family method that can be responsibly scaled to the larger project world, not to repeat the four-stage Wave0 review on thousands of files. Any material unexpected false admission or missing authority context must cause targeted HOLD or bounded change before author-world freeze, never retrospective task simplification.

```text
VALIDATION_313=REAL_TASK_INDEPENDENT_QUALIFICATION_CALIBRATION_AND_FALSIFICATION_PACKETS_VERIFIED
EXTERNAL_REVIEWER=NOT_AUTHORIZED_OR_STARTED
FAMILY_RULE=NOT_AUTHORED_OR_FROZEN
SOURCE_ADMISSIONS=ZERO
WORLD=WORLD_UNFROZEN
SCORED_TASKS_OR_ARMS=NONE
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
