# Validation 226: F1 scoring-boundary candidate matrix source and scope verification

**Date:** 2026-10-11
**Status:** STATIC_SOURCE_AND_SCENARIO_GUARD_PASS / INDEPENDENT SEMANTIC PEER REVIEW PENDING
**Parent:** Research 537 / Checkpoint 873 / MC-0030 Message 054
**Scope:** Verify the newly authored non-executable four-gate, 17-case F1 prospective scoring-boundary matrix against the original source-unit audit and owner-approved contract/policy hashes.
**Authority:** Public synthetic source review only; no owner run or F1 freeze.

`R0_P01_F1_SCORING_BOUNDARY_CANDIDATES_REV01_UNFROZEN.json` has 17 unique scenario records with exact normatively indexed source-line or JSON-leaf references, including 12 `SOURCE_DETERMINED` narrow cases and 5 `CANDIDATE_BLOCKED` semantic choices. Neither category is an executable scorer oracle: `SOURCE_DETERMINED` states only a local implication of approved rule text under an explicit trusted-evidence precondition.

The source guard checks the actual SHA-256 of the B01/B02 accepted contract (`9160a30c...`) and policy (`9b5bbc4d...`) before accepting any scenario; verifies each source ID exists in the committed 1,022-unit inventory; disallows ambiguous case IDs, missing gate families, incomplete provenance, unexpected determination categories, silently converted F1 statuses and count mismatch from all 18 independent reviewer receipts. Tests use mutated *synthetic review objects*, not any owner credential, proof, real evidence or source edit.

`scripts/check_r0_p01_scoring_boundary_candidates.py` **does not** prove the conceptual expected behavior in these 17 cases or resolve the 55 pending source-unit findings. That work requires independently challenging the formal table and eventually separate qualified expected-output vectors.

The nine new synthetic regression checks are in tests/unit/test_r0_p01_scoring_boundary_candidates.py. They cover original-source hash drift, exact source-unit references, four family presence, controlled status vocabulary, duplicate IDs, omitted gates, global-scoring restraint, and immutable audit provenance. They do not implement the 117 planned F1 qualification tests.

Observed combined regression: 56 passed in 2.86s (nine new scenario-guard tests plus forty-seven previous audit/trace/registration tests). The static scenario guard reports 17 scenarios, 4 gates, 12 source-determined, 5 candidate-blocked. Full repository integrity must separately PASS before publishing this checkpoint.

```text
VALIDATION_226=STATIC_SCORING_BOUNDARY_MATRIX_GUARD_ONLY
SEMANTIC_APPROVAL=INDEPENDENT_CHALLENGE_PENDING
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
