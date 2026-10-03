# Research 491: D-1 owner acceptance and J1 replay binding

**Date:** 2026-10-03
**Status:** OWNER ACCEPTED / J1 REPLAY INPUT BOUND / J2-J3 SPECIFICATION NEXT
**Parent:** Research 490
**Probe ID:** HYBRID_D1_REAL_EVENT_REPLAY_V01
**Owner packet SHA-256:** 2ac7ec839138189b5657da4c8f78f8c938ac3227da1c7af7f3c6f3fda7ae4fb4
**Owner decision:** ACCEPT
**Scope:** Bind the owner's exact decision to the frozen D-1 J1 package before any post-acceptance replay specification, source-fact fixture, evaluator key, or evaluator implementation is frozen.
**Authority:** Development replay acceptance only. This does not select production architecture, amend Specification 028, authorize migration, resume dependent DRPs, or expose hidden R2 item material.

## 1. Exact owner decision

The owner responded:

    ACCEPT

No amendment, qualification, or correction was supplied.

Therefore the exact frozen Research 490 owner package is accepted unchanged for this development replay.

## 2. Acceptance binding

The accepted replay boundary binds:

    probe
        HYBRID_D1_REAL_EVENT_REPLAY_V01

    source governing correction
        Research 485

    source event meaning
        Claude uses its own bounded GitHub collaboration write path;
        the ChatGPT-only Runtime Bridge is not a Claude execution surface;
        the incorrect Research 484 Section 5 rule is superseded;
        Research 477's transport-nonconformance classification is withdrawn.

    owner package
        experiments/ao10_hybrid_d1_replay_v01/owner_review_packet.json

    owner package SHA-256
        2ac7ec839138189b5657da4c8f78f8c938ac3227da1c7af7f3c6f3fda7ae4fb4

    owner decision payload
        ACCEPT

    accepted J1 effect count
        4

    effective replay boundary
        post-Research-485 D-2 Claude Evaluator B collaboration action.

## 3. Accepted J1 effects

The accepted package contains:

    D1-E01
        REQUIRE
        realization-tracked
        ALL_REQUIRED completion contract over:
            TRANSPORT_ATTESTED_GITHUB_CONNECTOR
            AUTHORIZED_PATH_ONLY
            COMMIT_RECEIPT_BOUND_TO_CORRECTION_HEAD

    D1-E02
        PROHIBIT
        no Claude Runtime-Bridge dependency
        standing control = DETECTIVE_ONLY

    D1-E03
        AUTHORIZE
        exactly Message 018 through Claude-side GitHub connector
        governed execution receipt required when exercised

    D1-E04
        LIFECYCLE
        replace incorrect Research 484 Section 5 transport rule with the corrected rule
        withdraw Research 477 transport-nonconformance finding
        realization succession = OPEN_RESET.

## 4. Governing consequence

The replay may now proceed to J2/J3 specification.

The owner decision does not imply that downstream implementation facts are true.

Those must be supplied independently from the actual Claude/Git event and evaluated mechanically.

## 5. Next boundary

Before evaluator implementation:

    freeze the actual J2 source-fact fixture;
    freeze shared predicates;
    freeze J3/orientation/standing-control/authorization/lineage rules;
    freeze a public output and diagnostic vocabulary;
    freeze the evaluator key;
    then independently author ChatGPT and Claude evaluators.

## 6. Current disposition

    OWNER_DECISION=ACCEPT
    J1_PACKAGE_ACCEPTED=true
    J1_PACKAGE_AMENDED=false
    J1_EFFECTS=4

    D1_RESULT_EXISTS=false
    OWNER_ARCHITECTURE_DECISION_READY=false
    PRODUCTION_TARGET_SELECTED=false
    HIDDEN_R2_DETAILS=SEALED

    NEXT=FREEZE_D1_POST_ACCEPTANCE_REPLAY_SPECIFICATION
