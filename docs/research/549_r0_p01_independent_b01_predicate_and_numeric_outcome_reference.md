# Research 549: bounded independent B01 predicate and numeric expected-outcome reference

**Date:** 2026-10-12
**Status:** BOUNDED_B01_ORACLE_REFERENCE_TESTS_PASS / F1_UNFROZEN
**Scope:** Author a separate, test-only prospective B01 result evaluator and explicit expected cases, compare the older unreviewed 288-row draft without treating the draft as truth, and distinguish scoring decisions from the subsequently owner-approved accidental replacement policy.
**Parent:** Checkpoint 884, Research 548, Validation 236; October 10 approved B01/B02 decisions; October 11 owner-approved prospective accidental/technical replacement supersession.
**Authority:** Non-owner, non-cryptographic derived-predicate tests. No independent raw receipt verification, F1 freeze, production scorer, F2 freeze, real owner execution or Attempt 002.

## Why this task matters

Research 548 completed a narrowly bounded synthetic atomic signed-acceptance and measurement path. A cryptographically verified ACCEPT, however, is not a complete scientific trial result. The eventual research interpretation must be determined by prospectively accepted evidence and decision rules, not a self-reported harness outcome or a model's retrospective preference.

This checkpoint implements experiments/r0_p01_successor_synthetic/independent_b01_oracle.py. The test-only module imports **none** of the owner harness, synthetic claim controller, WebAuthn/SSHSIG verification implementation, legacy decision generator, or 288-row draft. It accepts explicitly derived, prevalidated per-arm evidence_state/proof_viable/selection_eligible fields and integrity/instrument/selected-arm volume flags. It deliberately does not claim to derive those fields from raw evidence. It applies accepted B01 precedence:

1. INVALID_INTEGRITY dominates all other flags/evidence.
2. Without integrity violation, INVALID_INSTRUMENT dominates arm assessment.
3. If neither A nor B is proof-viable, any INCOMPLETE evidence produces INVALID_INCOMPLETE; both resolved arm states yield REOPEN, not a false impossibility claim after a mere interruption.
4. With a viable arm but no eligible arm, outcome AMEND.
5. With exactly one eligible arm and complete selected-arm projected-volume gates, PASS_WITH_SELECTION; when the other arm is incomplete, the mandatory G2 OTHER_ARM_INCOMPLETE disclosure accompanies the pass.
6. With two eligible arms, **the numeric selected arm is required** before final PASS/AMEND; an unqualified placeholder is returned as PENDING_NUMERIC_SELECTION, explicitly a processing status and **not** a fifth primary result class.
7. The frozen selection thresholds are evaluated with exact Fraction arithmetic on decimal strings: a difference of 10 seconds or more in median small operation chooses faster A/B, else a 15-second difference or more in large operation chooses faster A/B, else B tie-break. Selected-arm projected volume is 97 times its median small technical seconds / 60, with 90-minute ceiling and 100-acceptance count gate. This is derived aggregate logic, **not** a real human time measurement.

## Executed, source-separated reference evidence

tests/unit/test_r0_p01_f1_independent_b01_outcomes.py contains **68 independently stated test cases/parameterizations** comprising:

- 23 literal, author-stated expected B01 outcomes for precedence, missing/no viable arm, AMEND, G1, G2, one/two eligible arm cases, erroneous volume and two-arm numeric-selection pending.
- 10 exact-decimal arm-selection examples, including equal-to and just-below 10s and 15s thresholds, large-vs-small precedence and B tie-break.
- Seven literal complete selection-plus-volume expected outcomes.
- Six exact projected-time/count threshold cases and invalid-input negatives.
- Fail-closed contradictions and invalid types for arm states, selected arm and decimal timing.
- A separate **diagnostic comparison**, never a golden oracle source, against the existing frozen-status=UNREVIEWED 288-row B01 candidate table.

**The diagnostic result:** 286 of the 288 candidate rows have sufficient predicate-only information and match the separately implemented decisions. **CASE-281 and CASE-282** have two eligible arms without numerical selection inputs, so cannot yet be considered fully scored outcomes. Their historical candidate classes (AMEND and PASS_WITH_SELECTION, respectively) are not declared wrong; they are **underdetermined with the supplied fields**. Both cases need real specified numeric winner and its selected-arm volume result before qualification. The original table remains unchanged and UNFROZEN.

Observed new focused tests: **68/68 PASS**. Prior existing executable suites were rerun in three bounded groups: 46/46 measured/atomic, 70/70 governed claim, 63/63 signed/crypto, total 179/179. Existing structural suite: 84/84 PASS. **331 focused tests pass**. A larger initial combined run returned a bridge timeout with no result and was not counted.

## Important independence and authority limits

"Independent" here means the bounded reference is implemented without importing the currently tested successor scorer/harness, without computing its expected cases from the 288-row table, and with directly authored expected outputs. The same engineering collaborator authored the reference and tests: **this is not a separately authored second-language cryptographic scorer, independent domain reviewer acceptance, or an F1 freeze**.

The B01 evaluator trusts its derived flags and evidence states as inputs. It has not demonstrated genuine capability evidence, terminal WebAuthn/SSH receipt status, 13 security controls, owner views, underlying elapsed human times, role-dependent trust transitions, source-flag provenance, witness handling or complete end-to-end independent result scoring. Those are remaining F1/F2 qualification boundaries, and the 55 historical audit notes must be selectively triaged for real correctness risk rather than requiring a ceremonial review of every note.

The exact SHA-bound 2026-10-10 B02 finite claim rule is **historical evidence**, and the later 2026-10-11 human owner decision explicitly supersedes its rigid retry cap and exceptional-retry preconditions **for new separately authorized accidental or technical replacements**. No old STOP seed from that superseded procedural branch may gate such an approved replacement. This reference assesses scored outcomes only and does not create permission to run, repair, erase or reinterpret any attempt.

## Next engineering boundary

Independently specify and exercise the **raw-receipt to derived-flag/evidence-state interface**, emphasizing G1 credible capability proof, B01 terminal no-proof evidence versus interrupted/incomplete, source-validated integrity/instrument flags, selected-arm numeric inputs, and disclosure-only witness absence. Qualify a separate independent scorer implementation only after clear F1 expectations. No speculative exceptional-retry bureaucracy or human credential operation is needed for this stage.

```text
RESEARCH_549=B01_DERIVED_PREDICATE_REFERENCE_PASS
NEW_TESTS=68
PREDICATE_COMPLETE_SEED_ROWS=286
NUMERICALLY_UNDETERMINED_SEED_ROWS=2
EXECUTABLE_TESTS=247
STRUCTURAL_TESTS=84
FOCUSED_TOTAL=331
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
