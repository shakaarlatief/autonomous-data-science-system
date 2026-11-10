# Validation 316: Actual source-free calibration rule verified and evaluated for holdout readiness

**Date:** 2026-11-10
**Status:** EXACT_REAL_RULE_RECEIVED_AND_PRESERVED / BOUNDED_NO_DIRECT_CASE_LEAK_REVIEW / RECOMMEND_ACCEPT_FOR_FALSIFICATION_ONLY / OWNER_RULE_FREEZE_AND_HOLDOUT_DISCLOSURE_NOT_AUTHORIZED
**Research:** 628, 627; **Previous validation:** 315.
**Scope:** Independently verify the actual uploaded source-free qualification method, separately from the original reviewer's self-report, and prepare a prospective fixed application contract without reading confidential calibration cases or challenge evidence.
**Specification:** 028 unchanged. **Checkpoint:** 898 unchanged.

## 1. Actually received and measured artifact

The owner uploaded the actual `R0_P03_CALIBRATION_FAMILY_RULE_SOURCE_FREE.md` attachment to the coordinator. Independent binary read returned:

```text
CALIBRATION_RULE_BYTES=18580
CALIBRATION_RULE_SHA256=9e402bbaa5f190d72b55e76f38979ea032f90c724e2385e99c20da3e0a4b1268
CALIBRATION_RULE_LINES=121
CALIBRATION_RULE_UTF8=PASS
REVIEWER_REPORTED_HASH_MATCH=PASS
```

The coordinating role inspected all eight sections of the actual proposed source-free rule. It did **not** receive, open or query the separate 64,186-byte restricted 16-case calibration assessment file or the withheld 16-case falsification ZIP.

The proposed original rule was transferred unchanged into `experiments/r0_p03_navigation_probe/R0_P03_CALIBRATION_FAMILY_RULE_SOURCE_FREE.md`, which independently matched its exact **18,580 bytes** and original SHA-256 in the Windows repository. A specific `.gitattributes` `-text` entry suppresses automatic Windows newline conversion for the exact independently authored artifact; there was no content modification, reformatting, source-specific edit or synthetic replacement.

## 2. Independent content and direct-leak review

Section-by-section method review found adequate explicit controls for: exact source revision and claim/audience/time tuple; governing authority versus implementation and validation; prior results and old task-answer contamination; source provenance versus independent authenticity; eight source-function families; ten minimum evidence fields; six proposal/restriction outcomes; named material HOLD; false admission **and** false exclusion; no circular task or comparator selection; separate independent falsifier; and distinct rule freeze versus per-source author release.

The bounded source-free screen found **zero** direct matches for 40-character Git blob IDs, 64-character source hashes, concrete repository relative file paths, explicit numbered case identifiers, URLs and direct case-outcome assignments. No source excerpts, sample-specific actual case verdicts or task answer claims were observed in the reviewed text. This inspection does not prove a semantic absence of all possible leakage because the separately restricted 16-case evidence was correctly **not** used for cross-correlation. This is a plausible source-free method, not proof of safe model-provider isolation.

**Judgment:** The rule is scientifically suitable to **test under a fixed independent 16-case falsification**, without another calibration-review loop. It has **not** been proven accurate and must not automatically admit any source.

## 3. Source-free pre-holdout application interpretation

Two legitimate ambiguities need fixed interpretation *before* the challenger sees the unseen original sources:

- Define the proposed recipient as a **fresh blind primary information-need author**, not interchangeable with a privileged private reviewer, future scorer or arm engineer. Review each possible truthful historical/current claim and whether the original whole file or a separately approved bounded derivative could be safe for precisely that audience.
- Define material missing evidence by a concrete plausible discriminator capable of changing the claim, temporal applicability, authority, disposition or aggregate author exposure, rather than vague global incompleteness. A reasoned narrow historical claim remains eligible for review, while a verifiable contamination hazard forces no release.

The full source-independent, prospective interpretation is preserved at `experiments/r0_p03_navigation_probe/R0_P03_SOURCE_FAMILY_FALSIFICATION_INTERPRETATION_V01.md`, without changing the calibration reviewer's original 121-line file.

```text
PRE_HOLDOUT_INTERPRETATION_BYTES=8178
PRE_HOLDOUT_INTERPRETATION_SHA256=7594b420f215c311c4075a98c2775857c0e359e712efbec397d3ac969d8862ff
PRE_HOLDOUT_INTERPRETATION_STATE=PROPOSED_NOT_FROZEN
SOURCE_ADMISSIONS=ZERO
```

These definitions address operational consistency, not new reviewer evidence. The separate challenger should explicitly seek verified wrongful admission, wrongful exclusion, legitimate HOLD, indeterminate unreadable case and no demonstrated counterexample, preserving complete private case justifications. Any material false admission is a substantive failure even if other cases pass; no numerical score or 16-case sample accuracy can license a general family-wide admission.

## 4. Tests and release boundary

A source-free artifact identity guard at `tests/unit/test_r0_p03_source_free_calibration_rule_identity.py` returns **4/4 PASS** for exact source hash/bytes and line endings, original proposed/non-admission labels, required scientific dispositions, bounded regex case leak signals, companion digest binding, and no-challenge/no-owner-freeze state. This is a protective regression, **not** independent semantic proof.

**Owner permission still required:** The earlier user authorization was specifically for the calibration ZIP only, not for a freeze of this rule or disclosure of the distinct falsification ZIP. The coordinator therefore recommends that the owner **ACCEPT the unchanged original rule + exact source-free interpretation solely as a frozen method for independent falsification** and authorize one new, different non-arm reviewer to receive the heldout 16-case evidence, **only after** the combined exact rule/interpretation SHA-256 freeze and evidence-isolation contract are recorded.

Until explicit owner acceptance and authorization:

```text
VALIDATION_316=ACTUAL_CALIBRATION_RULE_CONTENT_REVIEWED
RULE_PRESERVED_EXACT_BYTES=PASS
RULE_DIRECT_CASE_LEAK_PATTERN_SCAN=PASS_LIMITED
FALSIFICATION_METHOD_SUITABILITY=RECOMMEND_ACCEPT_FOR_TEST_ONLY
OWNER_METHOD_FREEZE=NOT_AUTHORIZED
FALSIFICATION_HOLDOUT_DISCLOSURE=NOT_AUTHORIZED
INDEPENDENT_CHALLENGE=NOT_STARTED
SOURCE_ADMISSIONS=ZERO
AUTHOR_WORLD=WORLD_UNFROZEN
B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
