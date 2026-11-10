# Validation 320: Real 80-source corpus selection, original-byte checks, and bounded release-review handoff

**Date:** 2026-11-10
**Status:** REAL_PINNED_GIT_80_SOURCE_CANDIDATE_REPRODUCIBLE / SOURCE_ORIGINAL_IDENTITIES_PASS / AUTHOR_RELEASE_NOT_ESTABLISHED
**Research:** 631; preceding 625-630 and Validation 319.
**Scope:** Actual source-world engineering, not another general method experiment, independent source admission, fresh task authorship or B0-B4 scoring.
**Authority:** Verified byte fidelity and task-independent deterministic selection only. No source automatically accepted; Checkpoint 898 and Specification 028 unchanged.

## Executed real pinned Git candidate

Ran the new module against the real trusted ADS repository at the exact historical Git commit c57556a8bf993a1d327e9197acb7b7c745071cd8:

    .venv\Scripts\python.exe -B -m experiments.r0_p03_navigation_probe.minimum_experiment_corpus_candidate .

The resulting locally ignored exact source ZIP and safe receipt are in:

    .venv\.r0_p03_eighty_source_candidate_v01\

The ZIP was created exclusively with no-overwrite semantics. The real run returned:

    CANDIDATE_SOURCE_COUNT=80
    COMPLETE_AUDITED_REVIEW_UNIVERSE=2539
    ARCHIVE_BYTES=1314310
    ARCHIVE_SHA256=8d07e100dc9aef0934e49c089a9cbe20af3ef546eaa92f05c9e66a1ef3045e13
    SOURCE_MANIFEST_SHA256=1dbcbf733d52af3b68e13d0990d9aeac3b432b2918fda4e83bf3e6fdcd4b452b
    SOURCE_ORIGINAL_BYTES=1212135
    SELECTED_HISTORY_TO_VALIDATION_LITERAL_LINKS=5
    DISTINCT_SELECTED_STATUS_DOCUMENTS_IN_LINKS=4
    DISTINCT_SELECTED_VALIDATION_DOCUMENTS_IN_LINKS=5
    SOURCE_ADMISSIONS=0
    AUTHOR_WORLD=WORLD_UNFROZEN
    SPLIT=NOT_DRAWN
    SCORED_TASKS=NONE
    B0_B4_SCORES=NONE

The 80 files are path-family balanced (3 orientation, 12 governing, 14 Product implementation, 12 Project implementation, 10 verification, 4 tooling, 10 historical status, 9 execution evidence, 3 schemas, 3 other). This distribution is not a certified representative semantic world.

A subsequent independent execution of:

    .venv\Scripts\python.exe -B -m experiments.r0_p03_navigation_probe.minimum_experiment_corpus_candidate . --verify-only

returned:

    ACTUAL_EIGHTY_SOURCE_CANDIDATE_REPRODUCIBILITY=PASS

It reconstructed the ZIP and safe receipt from exact pinned historical Git originals and compared their entire bytes to the saved files.

## Independent ZIP and omission assessment

A separate read-only Python archive checker (not the candidate builder) confirmed:

    ALL_ORIGINAL_GIT_BLOB_SHA1_SIZE_SHA256_IDENTITIES=PASS
    ARCHIVE_MEMBER_SET=80_ORIGINALS_PLUS_2_METADATA
    SOURCE_PATH_DUPLICATES=NONE
    ARCHIVE_BYTES=1314310
    ARCHIVE_SHA256=MATCH
    KNOWN_EXPLICIT_R0_P03_OLD_ANSWER_MARKERS=NONE_DETECTED
    SELECTED_FILES_WITH_LITERAL_REFERENCES_OUTSIDE_80=33
    DISTINCT_REFERENCED_OMITTED_SOURCE_FILES=199
    DISTINCT_LITERALLY_REFERENCED_INCLUDED_FILES=22

These 199 are just **literal citation targets outside the selected 80**, not automatically material dependencies or demands for 199 extra files. They demonstrate why authority/answerability completeness has **not** been established and why the reviewer must inspect concrete missing evidence rather than merely trusting filenames and graph edges. No source-specific path list or original source text was published into this validation record.

All 80 original source bodies and source-specific omitted reference metadata stay inside one locally ignored, unencrypted restricted ZIP. The current conversation has not transferred it to any external reviewer, future scored task author, arm implementer or evaluator.

## Tests and corrective evidence

Created tests/unit/test_r0_p03_minimum_experiment_corpus_candidate.py with invented-only original Git source/text graph fixtures. The tests cover:

- exact eighty source/path-family quotas and required orientation/governance/routing anchors;
- identity-fixed deterministic selection independent of enumerated input ordering;
- original source provenance in the manifest, unresolved refs and no automatic release;
- explicit previous-answer contamination and path risk-flags;
- missing mandatory anchors and wrong Git pin;
- tampered original source-body rejection before manifest;
- shortage of usable historical evidence yielding fail-closed, not fake 12-task capacity;
- absence of tasks, hidden gold or 60/20 split in the release candidate.

During development the first fictional fixture had no validation-to-history citation direction and could not satisfy its **fictional** quota; this was corrected in the fixture rather than weakening the original real source selection. A second invented test reordered the identity-bound roster without recomputing its own synthetic commitment, which correctly failed the integrity check; the test now recomputes the synthetic commitment before verifying selection-order invariance.

The corrected focused execution returned:

    8 passed in 0.09s

The real original ZIP and its deterministic content did not change during either synthetic fixture repair. Final integrated/regression and repository integrity results are recorded after execution, not inferred from code alone.

## Next bounded scientific decision

The next action is one independent **actual source-world release review** of these precise 80 originals, not another general calibration of the already tested source-eligibility rule. The reviewer applies the owner-frozen rule and interpretation to each original source and the cumulative author-visible world. Review material omitted citation/context and actual evidence capacity for three independently supportable needs in each of four preregistered categories, without writing task questions or reference answers.

The owner has **not yet authorized external disclosure of this new 80-original ZIP**. The earlier permissions for different 16-case calibration/falsification packets cannot be treated as blanket authorization. A complete handoff is saved at experiments/r0_p03_navigation_probe/R0_P03_EIGHTY_SOURCE_RELEASE_REVIEW_HANDOFF_V01.md.

A favorable reviewer result is a source-level *recommendation*, not automatic admission. One independent, exact author-world release/whole-exposure freeze is still needed before scored task authoring. If material evidence prevents sufficient verified capacity, make one prospective bounded correction or record an explicit capacity HOLD, not an endless procedural review loop.

    VALIDATION_320=REAL_80_SOURCE_CORPUS_AND_INDEPENDENT_BYTE_VERIFICATION
    SOURCE_ADMISSIONS=0
    AUTHOR_WORLD=WORLD_UNFROZEN
    REVIEW_EXTERNAL_TRANSFER=NOT_AUTHORIZED_OR_STARTED
    PRIMARY_TASKS=NOT_AUTHORED
    EQUAL_ARM_SOURCE_SPLIT=NOT_DRAWN
    B0_B4_SCORES=NONE
    CHECKPOINT=898_UNCHANGED
    SPECIFICATION_028=UNCHANGED
