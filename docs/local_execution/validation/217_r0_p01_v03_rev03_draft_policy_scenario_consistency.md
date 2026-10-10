# Validation 217: R0-P01 V03 REV03 static policy consistency

**Date:** 2026-10-10
**Status:** TARGETED UNFROZEN DRAFT CHECKS PASS / NO IMPLEMENTATION QUALIFICATION
**Scope:** Validate agreement of the proposed REV03 contract and JSON policy and simulate nine classification scenarios using only synthetic data.
**Research:** Research 528
**Parent:** MC-0030 Message 023 / Research 513
**Authority:** Read-only static draft evidence, not live harness/scorer results, protocol freeze or owner authorization.

An ephemeral Python checker read `docs/research/r0_p01_successor_design/R0_P01_CONTRACT_V03_UNFROZEN_DRAFT.md` and `R0_P01_OUTCOME_POLICY_V03_UNFROZEN_DRAFT.json`. It verified ten unique §11 blocker IDs equal the JSON's sole list; seven unique outcome rows (NOT_RUN, PASS_WITH_SELECTION, AMEND, REOPEN, three INVALID reasons); two-new-claim absolute cap, ALL_REQUIRED conditions, no claim after PASS, no exception after integrity failure and all authorization booleans false.

It verified evidence-state values NOT_REALIZABLE, COMPLETED and INCOMPLETE, the enumerated event terminal outcomes, the fact that integrity and instrument source flag sets are disjoint, and that `attempt_integrity_failure` is not an instrument source.

Nine simulated design scenarios returned expected outcomes:

| Synthetic inputs | Draft-class outcome |
|---|---|
| A/B setups completed, abort before P0 | INVALID_INCOMPLETE |
| Both arms completed, no viable owner proof | REOPEN |
| A completed nonviable, B incomplete | INVALID_INCOMPLETE |
| A eligible, B registered but interrupted | PASS_WITH_SELECTION plus OTHER_ARM_INCOMPLETE |
| A viable but ineligible, B incomplete | AMEND |
| Instrument flag only | INVALID_INSTRUMENT |
| Instrument and integrity flags | INVALID_INTEGRITY |
| A NOT_REALIZABLE, B completed nonviable | REOPEN |
| A eligible but original volume gate fails | AMEND |

Output `DRAFT_STATIC_CONTRACT_JSON_CONSISTENCY=PASS`, `B_COUNT=10`, `POLICY_ROWS=7`, `SCENARIOS=9`. This demonstrates **consistency of a proposed rule set**, not tested runtime code. It does not qualify Windows SSH prompting, WebAuthn RP/UV, tri-state verifier, snapshot crash atomicity, final-head witnessing or actual scorer behavior. All original Attempt 001 evidence remained untouched and no new owner credential was used.

```text
VALIDATION_217=STATIC_REV03_CONSISTENCY_PASS
RUNTIME_QUALIFICATION=NOT_PERFORMED
OWNER_ATTEMPT_002=NOT_AUTHORIZED
```
