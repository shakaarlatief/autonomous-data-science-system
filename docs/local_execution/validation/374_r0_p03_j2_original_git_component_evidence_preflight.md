# Validation 374: J2 original Git facts, Claude source attestation and natural-owner COVERS preflight

**Date:** 2026-11-14
**Status:** COMPONENT_EVIDENCE_PREFLIGHT_EXECUTED / 33_NEW_TESTS_PASS / NATURAL_OWNER_J2_RELATIONAL_UNQUALIFIED / J3_HOLD
**Scope:** Verify exact original source owner and Git event evidence for the three already accepted P03 E01 completion components; enforce Research 512 OBSERVABLE, RELATIONAL and EPHEMERAL separation, validate adversarial hypothetical COVERS payloads, preserve source-owner identity and formal scoring boundary.
**Research:** 677. **Checkpoint:** 938. **Collaboration:** MC-0030 Message 090, prepared but not delivered.
**Authority:** Experimental source evidence and implementation checks only. No newly received Claude source owner COVERS declaration, new J2 qualified relation, new J3 completion, physical target or production authority.

## 1. Original source and actual execution

Starting Git branch v1-source-vault-bootstrap-resume, HEAD 922ce48434488c863ac2b989536acee31ec11e60, clean and equal to upstream.

Input source pin: 5463b2ad2e6799339746637f38340fa2a9dc00f6.

Actual original action commit: cd0cf087a4d0ddb30920a8c753e478da8f92295c, whose sole parent is 73f54c6a96b7a9172376b4c88deb9a5a400506d0; sole changed path is MC-0029 Message 018. The original message Git blob 2d8fdf1a50dba34427f72d4c01949504003d7037 has SHA-256 890ea35d0e6ea99143e0918cb41ee93a8c28add9981d57add9f20dcc707cadaa. The original source and action-commit versions matched byte-for-byte.

New files:

    experiments/r0_p03_navigation_probe/v03_j2_natural_owner_evidence_contract_v01.py
    experiments/r0_p03_navigation_probe/v03_j2_natural_owner_evidence_result_v01.json
    tests/unit/test_r0_p03_v03_j2_natural_owner_evidence_contract_v01.py

Original source line 6 reports Claude as collaborator author; line 13 reports Claude-side GitHub connector as transport. This proves a source statement exists, not the provider API act or independent identity.

Direct module invocation returned exit 0:

    git_verified = 2
    transport_attested = 1
    qualified_relational = 0
    status = J2_SOURCE_FACTS_VERIFIED_RELATIONAL_OWNER_DECLARATION_PENDING

Original E01 completion components and source classes are matched against the accepted immutable Checkpoint 937 J1 source.

## 2. First-run result provenance

- JSON result: 3,776 exact bytes, SHA-256 f45cd1b709c87d54bc99f5808e52b7685aa63646e8204c9827bab1d1b81f6c0b.
- Python implementation at first stable post-test read: 12,965 bytes, SHA-256 63686bd5a9e35b7ef4d039763937f23a9b6d2069515c9d53b69d3b3f1a1387b6.
- Focused test source at first stable post-test read: 10,608 bytes, SHA-256 71bc80f5910ccd273700e1fa92d1e86867628ff09a22ffab631da88b3e5fa74b.

The JSON is immutable under regeneration, refusing overwrite after a source mutation. No old J1 owner packet or historical fixture is rewritten.

## 3. Test and negative evidence

The new focused test command was:

    .venv/Scripts/python.exe -m pytest -q -p no:cacheprovider tests/unit/test_r0_p03_v03_j2_natural_owner_evidence_contract_v01.py

Observed result: 33 passed in 19.85 seconds, exit code 0.

The tests validate exact original Git parent, path, source blob, author and transport attestation line, accepted E01 three-component completion, two independently Git-verifiable facts, one original Claude-attributed attestation, and zero J2 relations. Negative witnesses include forged Git parent/path, changed original transport text, false new source owner or original source revision, attempted source-owner coverage of an unaccepted effect, duplicate facts, invented component or evidence class, overstated FULL coverage, false provider-proof claim, and injected governing status.

A structurally valid hypothetical declaration remains a source-owner CLAIM pending authentication and independent qualification. Its existence in a test suite is not actual Claude testimony or J3 certification.

## 4. Missing natural-owner J2 action

MC-0030 Message 090 is prepared but not yet delivered. It requests a separate original Claude source-owner declaration of actual FULL/PARTIAL coverage, CANNOT_ATTEST or contradiction for the exact P03 E01 effect, with source role/evidence limitations and no false provider proof. It instructs a shared GitHub connector publication only if available/authorized and otherwise a transparent full-text return for owner relay. It does not ask Claude to modify J1 acceptance or mark J3 satisfied.

The external natural owner has not provided a new attested relationship in this run. New P03 J2 RELATIONAL count remains zero and J3 is HOLD.

## 5. Postflight repository and regression checks

Actual final postflight after Checkpoint 938 routing, Research 677, Message 090 and J2 program/result updates:

- scripts/check_current_routing.py: PASS, checkpoint 938, current boundary p-three-j-two-natural-owner-response-next, latest formal experiment outcome INCOMPLETE.
- scripts/check_knowledge_map.py: PASS, 19 subjects, 24 foundations, 28 specifications, 677 numbered Research records and 939 numbered checkpoints.
- scripts/check_checkpoint_metadata.py: 939/939 numbered checkpoints compliant, zero errors.
- scripts/check_model_collaboration_state.py: PASS, 28 thread state records.
- scripts/check_repository_integrity.py: PUBLIC_REPOSITORY_INTEGRITY=PASS, including Project Knowledge, source map, checkpoint, model-collaboration and routing guards.
- git diff --check: exit 0, only advisory Windows LF/CRLF messages.
- New J2 natural-owner evidence preflight suite: **33 PASS in 19.39s**.
- Prior real-content source, X1, historical evidence chain and Project Knowledge authority suites: **180 PASS in 14.55s**.
- Accepted P03 D1 experimental J1 projection suite: **16 PASS in 6.62s**.
- Original D1 owner event/source admission suite: **22 PASS in 26.94s**.
- Total **251 passing test cases across four separately executed commands**. These are regression and source-proof tests, not 251 independent formal P03 information-needs or a navigation accuracy score.

The new first-run J2 receipt is immutable and new source-owner COVERS claims remain absent; no independent provider transport proof was established. Message 090 remains PREPARED, NOT DELIVERED. New P03 qualified J2 RELATIONAL count remains zero, J3 HOLD, formal P03 INCOMPLETE and physical target not selected.

    SOURCE_FACTS_EXACT_GIT_VERIFIED=true
    J2_GIT_OBSERVABLE_COMPONENTS=2
    J2_TRANSPORT_SOURCE_ATTESTED=1
    J2_PROVIDER_TRANSPORT_PROOF=NOT_VERIFIED
    J2_RELATIONAL_QUALIFIED=0
    NEW_J3_COMPLETION=HOLD
    NEW_J2_TESTS=33_PASS
    ORIGINAL_D1_RAW=D1_AMEND_UNCHANGED
    FORMAL_R0_P03=INCOMPLETE
