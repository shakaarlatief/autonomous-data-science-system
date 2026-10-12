# Validation 238: independent synthetic receipt and source-flag reference

**Date:** 2026-10-12
**Research:** Research 550
**Scope:** Synthetic P0/S01/S02/S03 terminal receipt correlation and selected source-flag derivation, including two synthetic receipt-to-B01 G1 examples.
**Parent:** Checkpoint 886 / Validation 237
**Status:** 63_NEW_RECEIPT_CASES_PASS / FULL_F1_NOT_QUALIFIED
**Authority:** Non-owner synthetic expected-case reference only. No live owner execution.

Added independent_receipt_reference.py and test_r0_p01_f1_independent_receipt_reference.py. Source-shaped receipts are checked for completeness and internal binding, **not** independently attested browser, RP or host origin. A claimed capability-unavailable receipt is rejected until a genuine independent capability-probe producer is qualified. Witness absence remains disclosure-only; invalid signature and verifier malfunction remain separate. Old original scientific outcomes and approved policy files remain unchanged.

Post-final-code reference run:

    python -B -m pytest -q -p no:cacheprovider --basetemp=.venv/.p01-886-ref-final tests/unit/test_r0_p01_f1_independent_receipt_reference.py tests/unit/test_r0_p01_f1_independent_b01_outcomes.py
    131 passed in 0.17s

Earlier executable security and admission tests, rerun unchanged in three groups:

    --basetemp=.venv/885-886-old-a: 46 passed
    --basetemp=.venv/885-886-old-b: 70 passed
    --basetemp=.venv/885-886-old-c: 63 passed

Structural/provenance regressions:

    --basetemp=.venv/.p01-886-struct: 84 passed in 17.21s

**394 focused PASS**: 63 new synthetic receipt cases + 68 earlier B01 reference tests + 179 older executable security/integration tests + 84 structural/audit guards. This does not demonstrate raw producer authenticity, full F1 scoring or a live owner-sensitive experiment. Repository integrity checks are separate.

    VALIDATION_238=SYNTHETIC_RECEIPT_FLAG_EXPECTATIONS_PASS
    NEW_CASES=63
    FOCUSED_TESTS=394
    F1_F2=UNFROZEN
    ATTEMPT_002=NOT_AUTHORIZED
