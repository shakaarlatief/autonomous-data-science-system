# Research 680: Typed J2 source-owner and evidence-assurance port over two real events

**Date:** 2026-11-14
**Status:** SOURCE_BOUND_TYPED_J2_PORT_EXECUTED / TWO_E01_GIT_OBSERVABLES_VERIFIED / SOURCE_OWNER_AND_PROVIDER_PROOF_UNAVAILABLE / NO_NEW_J2_OR_J3_PROMOTION
**Scope:** Implement an experimental typed interface that distinguishes OBSERVABLE, RELATIONAL and EPHEMERAL source evidence, binds it to the correct real event and accepted effect, and mechanically rejects authority laundering. Contrast original D1 and the actual forward action-time source event.
**Authority:** Exposed and unscored. Research 512 section 9, Research 673, the four accepted experiment-only J1 effects in Research 676, and Research 678/679 remain in force. No production J1, governing J2, J3 satisfaction, formal B0-B4 score, physical target or migration is authorized.
**Implementation:** experiments/r0_p03_navigation_probe/v03_typed_j2_assurance_port_v01.py
**Derived receipt:** experiments/r0_p03_navigation_probe/v03_typed_j2_assurance_port_result_v01.json
**Tests:** tests/unit/test_r0_p03_v03_typed_j2_assurance_port_v01.py
**Original Git events:** D1 cd0cf087a4d0ddb30920a8c753e478da8f92295c; forward 131c54a4aec9f8733af35b1c90e8b16a7c9919a5.

## 1. What this port must prevent

The owner-accepted experiment-only E01 requires ALL_REQUIRED across TRANSPORT_ATTESTED_GITHUB_CONNECTOR, AUTHORIZED_PATH_ONLY and COMMIT_RECEIPT_BOUND_TO_CORRECTION_HEAD. The original Git changeset and parent are exact source facts, but Git does not independently establish which connector API executed the action. The original message and commit message both assert connector use, without a separate independent provider receipt, and later Claude Message 091 says CANNOT_ATTEST.

Research 679 created a genuinely new source event with a contemporaneously co-committed COVERS claim. That claim targets only UNACCEPTED_PROBE_ONLY_ACTION_RECORDING_CRITERION, not a newly accepted J1 effect. The new event proves the claim is in the same Git tree, not that its author is independently authenticated or the claim is governing J2.

An invalid port could accept a forged provider-verification flag, treat source-reported transport as a platform receipt, relabel an actual forward-event Git fact as satisfying historical D1 E01, turn a model-authored COVERS claim into owner-approved coverage, count repeated transport text as two proofs, or mark new J3 complete without a governing evaluator. All those routes must fail closed.

## 2. Actual bounded interface

The implementation defines a FactKind enum for OBSERVABLE, RELATIONAL and EPHEMERAL; immutable source-observation and claim records; a source-verification context; a closed claim schema; and explicit qualification dispositions.

The context is constructed by re-reading the original frozen D1 accepted packet and real Git objects, verifying the original source-author Message 018 and its exact action/parent, parsing the genuine Message 091 CANNOT_ATTEST status, and reopening the forward event commit and single-file record. The verifier constructs source-owned observations only from those actual Git checks, not from caller-supplied independent-proof flags.

The two actual source event and component bindings are frozen in this deliberately bounded development specimen. A fact observed in one event cannot be moved onto another accepted effect, even if the observed Git commit really exists. The claimed-assurance field is not an authorization channel. Caller-supplied natural-owner-authenticator or provider-verifier capability flags fail closed because no qualifying backend was actually implemented or invoked.

This hardcoded exact-source specimen is not the proposed general production registry. An eventual source adapter must derive current accepted effect bindings from governed semantic contracts and qualified natural-owner source metadata, without duplicating governing authority. The present constants make an adversarial source-specific test auditable rather than pretending the full production admission system already exists.

## 3. Verified source results

For original D1 E01:

| Component | Verified type | Qualification |
| --- | --- | --- |
| AUTHORIZED_PATH_ONLY | OBSERVABLE direct Git changeset | VERIFIED_GIT_OBSERVABLE |
| COMMIT_RECEIPT_BOUND_TO_CORRECTION_HEAD | OBSERVABLE direct Git parent | VERIFIED_GIT_OBSERVABLE |
| TRANSPORT_ATTESTED_GITHUB_CONNECTOR | EPHEMERAL source-attested statement | HOLD_PROVIDER_RECEIPT_UNAVAILABLE |

The two historical transport statements belong to one source-claim family with two textual carriers and zero independent provider receipts. The current evidence does not decide whether the owner-accepted TRANSPORT_ATTESTED component's assurance threshold is met merely because a source attestation exists. Its wording and qualification requirement are not silently amended. The historical E01 new J3 status remains HOLD, with no new governing J3 evaluator executed by this port.

For the real forward at-action event, Git independently verifies both its source path and parent. A co-committed RELATIONAL COVERS claim exists but points to an unaccepted diagnostic criterion, so the claim and both forward OBSERVABLE inquiries are HOLD_NO_ACCEPTED_TARGET for governing J2 purposes. A forwarded source-reported execution claim also lacks a qualified accepted target and provider-native evidence. The event establishes traceable source context, not a new accepted governing effect.

The exact inquiry matrix has seven entries, with two verified original D1 Git facts and five other claims blocked by assurance or accepted-target boundaries.

## 4. Adversarial and architectural qualification

The evaluator binds each inquiry to an exact source event, fact kind, component, accepted target and claim family. A genuine original Git observation relabeled as another effect is rejected, as is a forward action's probe-only COVERS statement transplanted to E01. An external caller cannot extend the accepted effect list, add an observation anchor, change its factual value, change its Git source digest, or claim the missing authentication backends have been installed.

Crucially, VERIFIED_GIT_OBSERVABLE means a Git fact was independently verified from its natural source. It is not identical to a qualified RELATIONAL J2 realization or a complete J3 predicate. A source-reported EPHEMERAL action without independently sufficient evidence remains on hold.

The resultant immutable JSON retains:

    original_P03_experiment_only_accepted_J1 = 4
    new_accepted_J1 = 0
    source_verified_D1_E01_git_observables = 2
    qualified_new_RELATIONAL_J2 = 0
    verified_native_provider_receipts = 0
    historical_E01_J3 = HOLD
    original_D1_raw_outcome = D1_AMEND_UNCHANGED
    formal_R0_P03_scores = null
    physical_architecture_selected = false

## 5. Executed tests and prototype limitations

The first full program invocation timed out at the Runtime Bridge's 30-second limit because multiple nested source-validation builders redundantly recomputed the same original packet and event records. The implementation was optimized to preserve exact original source verification and avoid repeating expensive aggregate checks; the next direct invocation completed successfully.

An additional possible evidence-to-effect transplantation loophole was detected during implementation. The port was hardened with exact source-to-effect bindings and a constrained verified-context boundary. The direct invocation still succeeded after the fix.

The focused test suite passed **44 tests**, including invalid source effects, false actor or provider identity, forged backend availability, unsupported assurance claims, changed source digests, substituted Git fact values, schema injection, source claim family substitution, duplicate observation anchors, and protected current J1/J3 boundaries. These tests are engineering controls, not independent primary P03 tasks or formal architecture comparison scores.

Only exact Git-object verification is implemented. The prototype lacks a real independent natural-owner authentication backend, a qualified native provider receipt verifier, a generic accepted-semantic contract resolver, and the governing V03 J3 evaluator. A caller supplying a source claim or model-generated text cannot supply these missing capabilities.

## 6. Implications and next discriminating work

The evidence supports continued evaluation of a typed J2 interface that separates verified source observations, natural-owner declarations and non-reproducible provider events, with explicit assurance and correct accepted-effect binding. It does not by itself select GOVERNED_LEDGER_KERNEL_V02 or another physical architecture.

The next finite test should inventory which existing provider-native receipt and source-owner authentication mechanisms are genuinely available, test whether they can be bound to an accepted experiment-only source effect without unapproved authority substitution, and return bounded UNKNOWN where proof is unavailable. If a new consequential accepted effect is needed, prepare its exact owner-visible proposal rather than inferring approval from this general development continuation.

The whole physical design remains reconsiderable: source carriers, tooling, event protocols, storage, branch/CI workflow, provider adapters and migration plan. Research 673's independently authored formal task/gold controls, Research 513/559/576 gates, Specification 028 and the current unselected physical target remain unchanged.

    RESEARCH=680
    NEW_TYPED_PORT=DEVELOPMENT_SPECIMEN_EXECUTED
    ORIGINAL_EXPERIMENT_ONLY_J1=4
    NEW_J1=0
    VERIFIED_E01_OBSERVABLES=2
    NEW_RELATIONAL_J2=0
    VERIFIED_PROVIDER_RECEIPTS=0
    HISTORICAL_E01_J3=HOLD
    FORMAL_P03=INCOMPLETE
    PHYSICAL_TARGET_SELECTED=false
    NEXT=REAL_SOURCE_OWNER_AUTHENTICATION_AND_PROVIDER_RECEIPT_FEASIBILITY
