# Research 492: D-1 post-acceptance replay specification freeze

**Date:** 2026-10-03
**Status:** POST-ACCEPTANCE SPEC + SOURCE FACTS + KEY FROZEN / CHATGPT EVALUATOR A NEXT
**Parent:** Research 490-491
**Fixed evidence base:** 499df4ccf687b4aa18697cb3915dcfba92596d3f
**Probe ID:** HYBRID_D1_REAL_EVENT_REPLAY_V01
**Scope:** Freeze the accepted J1 payload, actual J2 source facts, deterministic replay rules, output contract, and hidden semantic key before either D-1 evaluator implementation exists.
**Authority:** Development replay specification only. No D-1 result is observed or inferred here.

## 1. Frozen artifacts

    accepted_j1.json
        SHA-256 a1faa89f9183e521831a84d6248158420a8aec1b62aace873e4453fd9f377c17

    source_facts.json
        SHA-256 011e894d3b7ac0d664ec85a59d13359f859f37394dd430837ee5fdc4d20fb4d2

    definitions.json
        SHA-256 411e843c1d14e705b49702f60bc6202301ce2a5d7340115bd77da4ed8b4155f6

    evaluator_contract.json
        SHA-256 228b1cc283b91a0e42a1c0d08233668b44d59d477b73e90e768b3be440da5e43

    evaluator_key.json
        SHA-256 666ce81691e7c2cfde005433b865f9d28641c2a55a850050adb33f1db8e6106f

No evaluator source exists at this freeze.

## 2. Accepted J1 binding

accepted_j1.json binds:

    owner decision
        ACCEPT

    owner packet SHA-256
        2ac7ec839138189b5657da4c8f78f8c938ac3227da1c7af7f3c6f3fda7ae4fb4

    accepted effects
        D1-E01 REQUIRE
        D1-E02 PROHIBIT
        D1-E03 AUTHORIZE
        D1-E04 LIFECYCLE.

The evaluator may inspect accepted J1 but may not alter it.

## 3. Actual J2 source facts

source_facts.json binds the real action:

    correction commit
        73f54c6a96b7a9172376b4c88deb9a5a400506d0

    Claude Message 018 commit
        cd0cf087a4d0ddb30920a8c753e478da8f92295c

    Message 018 parent
        correction commit exactly

    changed path
        exactly docs/model_collaboration/threads/MC-0029/messages/018_claude_d2_lineage_evaluator_b.md

    Message 018 transport attestation
        CLAUDE_SIDE_GITHUB_CONNECTOR

    Claude Runtime Bridge availability
        false under the accepted Research 485 correction.

These are source facts, not governing semantic authority.

## 4. Shared deterministic predicates

The frozen definitions require both evaluators to derive:

    transport_attested_github_connector
    authorized_path_only
    commit_receipt_bound_to_correction_head
    runtime_bridge_prohibition_not_violated
    evidence_valid
    qualification_complete
    authorization_exercise_valid
    lineage_transition_valid.

The predicate definitions are public to both evaluator authors.

No evaluator may reinterpret the source prose.

## 5. J3 and orientation

The realization-tracked D1-E01 is satisfied only when:

    its ALL_REQUIRED completion components are true;
    evidence_valid is true;
    qualification_complete is true.

The accepted REPLACE relation initializes the successor realization path as:

    OPEN_RESET.

The later actual J2 facts may then satisfy the requirement through ordinary J3 derivation.

Thus:

    lineage initialization
        is not
    final realization orientation.

This directly exercises realization succession followed by actual realization.

## 6. Currentness

After the real Message 018 action:

    D1-E01 REQUIRE
        remains current as a satisfied standing accepted requirement.

    D1-E02 PROHIBIT
        remains current as a standing constraint.

    D1-E03 AUTHORIZE
        is consumed by the one bounded Message 018 exercise.

    D1-E04 LIFECYCLE
        has executed the replacement and becomes historical.

Therefore the expected current-effect set contains:

    D1-E01-D2-CLAUDE-WRITE-REQUIREMENT
    D1-E02-NO-CLAUDE-RUNTIME-BRIDGE.

## 7. Standing and authorization views

The standing prohibition view is one of:

    DETECTIVE_ONLY_COMPLIANT
    DETECTIVE_ONLY_VIOLATION
    UNBOUND_REVIEW_REQUIRED.

The bounded authorization view is one of:

    EXERCISED_VALID
    EXERCISED_INVALID
    NOT_EXERCISED.

These views are derived.

They do not become new accepted authority.

## 8. Review routing

If material inconsistency is found, review_owner must be one of:

    GOVERNING_OWNER
    INTEGRATION_OWNER
    ASSURANCE_OWNER.

A fully coherent replay returns:

    review_required = false
    review_owner = null.

## 9. Hidden key

The semantic key is frozen before either evaluator implementation.

Unlike D-2, D-1 has no diagnostic reason-code field.

Every required output field is material and scored exactly.

Claude Evaluator B must not inspect:

    evaluator_key.json
    future ChatGPT Evaluator A
    Evaluator A output
    D-1 result/comparison.

## 10. Independent evaluator route

Evaluator A:

    author = ChatGPT
    next.

Evaluator B:

    author = Claude / claude-04
    after Evaluator A is frozen and unexecuted.

The two implementations must be authored from:

    accepted_j1.json
    source_facts.json
    definitions.json
    evaluator_contract.json.

They may not derive expectations from the hidden key.

## 11. Current boundary

    J1_ACCEPTED=true
    J2_SOURCE_FACTS=FROZEN
    RULES=FROZEN
    OUTPUT_CONTRACT=FROZEN
    HIDDEN_KEY=FROZEN
    EVALUATOR_A_EXISTS=false
    EVALUATOR_B_EXISTS=false
    D1_RESULT_EXISTS=false

    NEXT=AUTHOR_AND_FREEZE_D1_CHATGPT_EVALUATOR_A
