# Validation 385: Experiment-only J2 policy proposal source binding and negative admission

**Date:** 2026-11-15
**Status:** FROZEN_PROPOSAL_SOURCE_BOUND / CURRENT_J1_AND_REAL_GIT_J2_HOLD_REPLAY_PASS / 53_ADVERSARIAL_CHECKS_PASS / OWNER_DECISION_NOT_RECEIVED
**Research:** 688. **Checkpoint:** 949. **MC-0030:** Message 102.
**Scope:** Mechanically verify the proposed one-event experimental source-owner policy against the exact currently accepted J1 and prospective Checkpoint 948 Git event; test that the proposal cannot itself activate policy, owner identity, J2 or J3.
**Authority:** Unscored development-only proposal consistency test. No policy acceptance, independently authenticated model principal, source-owner J2 qualification, new source revision, S1 activation, formal R0-P03 scoring or physical architecture selection.

## Exact reproducible inputs

    Proposal:
      experiments/r0_p03_navigation_probe/v03_real_pk_j2_experiment_assurance_owner_proposal_rev01.json
      SHA-256 f0217d8c24aba8aa5a5d493d6c816f9e439de4e32f32c00d56665b075ead798f

    Prior genuinely prospective source event:
      Git faf8ff2686c6b09f53d3569470cf2057c11e5971
      immutable assay SHA-256 b64569b802f5d9d6de2e6d975ba8a3e462698ba696752afe0392c4abd0f565ac

    Preflight:
      experiments/r0_p03_navigation_probe/v03_real_pk_j2_experiment_assurance_preflight_rev01.py
      experiments/r0_p03_navigation_probe/v03_real_pk_j2_experiment_assurance_preflight_result_rev01.json
      receipt SHA-256 6d59f973af051df42423ad7bb1f58ff39992ab87d9e3ba1750990a534deec369

    Tests:
      tests/unit/test_r0_p03_v03_real_pk_j2_experiment_assurance_preflight_rev01.py

Reproduction:

```powershell
.venv\Scripts\python.exe -m experiments.r0_p03_navigation_probe.v03_real_pk_j2_experiment_assurance_preflight_rev01
.venv\Scripts\python.exe -m pytest -q --tb=short -p no:cacheprovider tests/unit/test_r0_p03_v03_real_pk_j2_experiment_assurance_preflight_rev01.py
```

The final focused adversarial run produced **53 passed**. The later combined new-policy/prior-at-action assay suite passed **78 tests**, and the adjacent accepted-J1 projection suite passed **16 tests**. Thus 94 tests passed in two additional completed bounded commands, overlapping the initial 53-test run; these numbers are not additive unique-test counts. The proposal tests' attempted forgeries included fake owner ACCEPT, production effect promotion, changed accepted S1 target/components, retroactive Checkpoint 948 J2/S1/J3 promotion, fake independent owner/model authentication, non-forward temporal applicability, omitted actual realizer ownership and execution, asserted FULL coverage, altered standing/independence controls, self-qualified source metadata, and an invented J3 PASS.

The proposal and its derived output are protected as exact LF bytes through `.gitattributes`; the prior prospective carrier and authorial claim are likewise explicitly protected from checkout line-ending conversion.

## Actual result

    proposal_state=PROPOSED_NOT_OWNER_ACCEPTED
    owner_decision=NOT_RECEIVED
    prior_event_git_structural=PASS
    prior_event_j2=HOLD
    prior_event_s1=NOT_ACTIVATED
    prior_event_j3=HOLD
    strong_actor_authentication_satisfied=false
    prospective_policy_admitted=false
    future_source_revision_required=true
    future_execution_and_separate_j3_required=true
    formal_r0_p03=INCOMPLETE

The preflight is deliberately not a simulation of an accepted human decision. A matching hash tests the stored proposal's consistency, not signer identity, authorization or scientific adequacy. No actual future event has yet been authored under this unaccepted policy.

The final public-repository integrity, local/remote publication and GitHub CI conclusions must be verified on the exact preserved revision rather than inferred from this bounded pytest result.
