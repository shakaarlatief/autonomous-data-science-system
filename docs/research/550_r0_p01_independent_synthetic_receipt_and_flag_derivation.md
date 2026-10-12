# Research 550: bounded synthetic evidence and source-flag reference

**Date:** 2026-10-12
**Status:** SYNTHETIC_RECEIPT_REFERENCE_PASS / F1_UNFROZEN
**Scope:** Independently test B01 terminal-event completeness and narrow mechanically checkable source flags, without accepting fabricated platform capability, browser assertions or source labels as independent proof.
**Parent:** Research 549 / Validation 237 / Checkpoint 885; accepted B01 and owner-approved simplified accident replacement.
**Authority:** Non-owner synthetic reference only, not a production scorer, F1/F2 freeze, actual credential ceremony, or execution consent.

## Implementation

Added experiments/r0_p01_successor_synthetic/independent_receipt_reference.py. Its test-only typed receipt schema is independent from the owner V02 harness and the existing synthetic credential/admission implementation.

The reference checks the claimed synthetic attempt, A/B arm, P0/S01/S02/S03 event, unique event-bound acceptance ID, terminal status, enumerated terminal outcome and separate verification result. COMPLETED requires four qualified terminal events and REALIZABLE setup, not successful authentication at every event. Owner S, exhausted native SSH budget and terminal failed signature verification are terminal evidence without successful owner proof. An interrupted, crashed, missing or nonterminal event remains INCOMPLETE, and native SSH S/budget terminal outcomes cannot complete a WebAuthn event.

For WebAuthn NotAllowedError/cancel/timeout to count as a synthetic terminal no-proof event, the record must include correlated RP-issued, delivered, browser-get-invoked, RP-consumed and matching acceptance identities. A mere NotAllowedError report or absent consumed receipt remains INCOMPLETE. These fields can still be forged by a caller: their correlation is not independently authenticated platform evidence.

Setup refusal, not visited, or a self-declared unavailable capability never becomes NOT_REALIZABLE. This stage has **no qualified independent capability receipt producer**, so providing purported capability proof fails closed instead of awarding NOT_REALIZABLE.

The narrow flag evaluator distinguishes verifier ERROR from a completed INVALID proof, RP exit before a recorded owner abort from an exit after it, computes SHA-256 from actual previous snapshot bytes to catch a link mismatch, and treats an absent optional owner final-head witness as disclosure only. It does not claim to compute every frozen integrity or instrument source flag, or authenticate the complete snapshot history.

## Evidence and limitations

New test module tests/unit/test_r0_p01_f1_independent_receipt_reference.py has **63 new test cases**, including synthetic receipt completeness, forged/mismatched fields, correct native SSH vs WebAuthn terminal classes, incomplete/unsupported platform proof, exact byte-hash mismatches, source timing/order, witness disclosure, and two integrated reference G1 outcomes. These tests prove that an uncorroborated cancellation cannot falsely qualify REOPEN, while fully observed terminal no-proof cases can support G1 when independently assessed proof viability is false.

The final B01-reference group passed 131/131, comprising 63 new receipt tests and 68 previous expected-predicate/numeric tests. Earlier executable synthetic security/measurement tests passed 179/179 across three groups; historical structural/guard tests passed 84/84. **394 focused PASS** = 310 executable tests plus 84 structural checks.

This remains a test-only syntactic and arithmetic reference. It cannot guarantee genuine SSH/WebAuthn/browser/RP source provenance, actual user presence, true platform incapability, 13 security controls, independent host attestations, full arm eligibility, independently frozen F1 or full run-level scoring. A source-shaped JSON receipt is not itself a trusted source receipt. No owner keys were used.

The 2026-10-11 owner-authorized simple accidental/technical replacement rule remains effective, distinct from cryptographic proof and unchanged original attempt scores. Historical B01/B02 bytes, Attempt 001 AMEND and 55 pending audit entries remain preserved.

## Next bounded engineering work

Connect real, authoritative, claim-bound event producers and verification to these derived-state rules: local SSH verification, genuinely invoked browser/RP and consumed assertion receipts, independently qualified capability probe if NOT_REALIZABLE is needed, full source-flag checks and scorer known-answer qualification. Design and test this as part of F1 rather than adding another top-level milestone or resurrecting strict B02 retry paperwork.

    RESEARCH_550=SYNTHETIC_RECEIPT_AND_FLAG_REFERENCE_PASS
    NEW_CASES=63
    EXECUTABLE_TOTAL=310
    STRUCTURAL_TOTAL=84
    FOCUSED_TOTAL=394
    F1_F2=UNFROZEN
    ATTEMPT_002=NOT_AUTHORIZED
