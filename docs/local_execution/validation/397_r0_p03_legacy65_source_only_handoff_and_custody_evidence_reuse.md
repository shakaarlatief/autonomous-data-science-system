# Validation 397: Legacy-65 source-only handoff and scoped reuse of synthetic custody evidence

**Date:** 2026-11-16
**Status:** EXACT_SOURCE_ONLY_CAPSULE_PASS / NO_NEW_BACKUP_FOLDER / OWNER_FAKE_PACKET_INTEGRITY_REPORTED_PASS / FULL_LEVEL_B_REFERENCE_SEPARATION_OPEN
**Research:** 701. **Checkpoint:** 962. **MC-0030:** Message 116.
**Scope:** Exact original source-horizon/capsule verifier, no reference labels or scores.

The owner declined an assistant-suggested extra backup folder/USB requirement, after an owner-reported correct exact 2,163-byte private fake packet hash and UTF-8/JSON readback, source-safe receipt SHA-256 `7afeb5abaa31e73a7819eea79d8bae3c87cc5da62401e02180d2850e3f40eb58`. Research 585 already separately preserves completed owner-reported fictional 21-case generation and recovery. No new owner storage path, real reference output, hidden gold, answerer exclusion test or blanket Level B admission was created.

Executed:

    .venv\Scripts\python.exe -m experiments.r0_p03_navigation_probe.legacy_65_source_only_handoff_v01
    .venv\Scripts\python.exe -m pytest -q --maxfail=1 --tb=short -p no:cacheprovider tests/unit/test_r0_p03_legacy65_source_only_handoff_v01.py

Result: **7 PASS**, original ZIP exact raw bytes **622,066**, SHA-256 `db2eb5fc66105918166db54de225b0625ce6d7faf9cb9270bfd98ba3842ffc7b`, 68 exact ZIP entries (65 original Git blobs plus source manifest, nine-topic hints, independent author brief). All 65 source paths have exact historical Git tree membership at `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`; Git blob and SHA-256 identities and ZIP CRC verified. No W5 B1 annotations, scenario-answer or score metadata packaged. The initial individual-Git-process test timed out; batch-verified Git reading preserves byte-identical ZIP output.

Output is locally staged in the ignored `.ads-private/p03_legacy_independent_source_only_handoff/` directory and is **not** public Git or a gold packet. No individual fresh reviewer yet received or adjudicated the ZIP. Final repository integrity/CI publication to be checked independently.

    VALIDATION=397
    LEGACY_PACK=65_SOURCE_ONLY
    ZIP_EXACT_SHA256=db2eb5fc66105918166db54de225b0625ce6d7faf9cb9270bfd98ba3842ffc7b
    NEW_TESTS=7_PASS
    NEW_PRIVATE_GOLD=NONE
    FORMAL_P03=INCOMPLETE
