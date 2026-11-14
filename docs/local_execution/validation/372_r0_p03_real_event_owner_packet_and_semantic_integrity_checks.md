# Validation 372: Original D1 Git event and proposed P03 experimental owner-packet integrity

**Date:** 2026-11-14
**Status:** ORIGINAL_D1_GIT_PROVENANCE_AND_DEVELOPMENT_OWNER_RECORD_VERIFIED / PROPOSED_NEW_P03_PACKET_IMMUTABLE / TWENTY_ONE_TESTS_PASS / P03_EXPERIMENTAL_ADMISSION_HOLD
**Scope:** Check one authentic owner-reviewed real-event replay against exact old Git object bytes, validate the original D1 acceptance scope and corrected byte-hash basis, build a prospectively new owner-visible experiment-only packet, and mechanically reject false new P03 J1/J2 authority.
**Research:** 675. **Checkpoint:** 936. **Collaboration:** MC-0030 Message 088.
**Authority:** Development/research integrity only, not new owner acceptance or scored experiment.

## 1. Original evidence base

Starting branch v1-source-vault-bootstrap-resume, clean HEAD 486e6351be898e4e06088529b31c823ad45b6f53.

Pin for original D1 and owner records: 5463b2ad2e6799339746637f38340fa2a9dc00f6.

Original correction event commit: 73f54c6a96b7a9172376b4c88deb9a5a400506d0.
Original Claude Message 018 event commit: cd0cf087a4d0ddb30920a8c753e478da8f92295c.

Git cat-file and rev-list confirm both original commits are present. Git show of the Claude action commit identifies one parent equal to the correction commit, and git diff-tree identifies one added file, the exact MC-0029 Message 018 path. This Git evidence verifies the action receipt and one-path scope, not independently the original Claude connector transport API.

Original D1 owner_review_packet Git blob length=5,107 bytes, SHA-256 af7037517174dda8e80a34f4c3cc3608afacf498ed798a3fb91242dfe4765e79. Original recorded owner-packet CRLF worktree length=5,193 bytes, SHA-256 2ac7ec839138189b5657da4c8f78f8c938ac3227da1c7af7f3c6f3fda7ae4fb4. These content-equivalent, byte-different bases are classified separately; the original Research 491 decision is not retroactively restamped.

The original accepted_j1 effect array equals the original owner_review_packet proposed effect array, exactly four independent IDs. Research 491 provides the original scoped owner ACCEPT and Research 499 preserves the independent D1 V01 AMEND result. No further owner act is inferred.

## 2. New executable candidate contract

Files:

    experiments/r0_p03_navigation_probe/v03_d1_real_event_admission_contract_v01.py
    experiments/r0_p03_navigation_probe/v03_d1_real_event_owner_proposal_v01.json
    experiments/r0_p03_navigation_probe/v03_d1_real_event_admission_preflight_result_v01.json
    tests/unit/test_r0_p03_v03_d1_real_event_admission_contract_v01.py

The new program read 12 original Git-pinned source artifacts, checked the D1 ownership/effect, source-action and lineage consistency, used the actual original D1 evaluator to derive a labelled non-governing preview and retained Research 499's corrected ordered initialization shape without changing the historical D1 outcome.

New proposal ID: R0_P03_V2_D1_REAL_EVENT_REUSE_CANDIDATE_001.
New canonical owner packet SHA-256 (sorted compact UTF-8 JSON):
186c70ff487104f8ee5baee8d21b50ffd466e812c6b97debb20296c8bbf9451f.

Actual program execution returned status REAL_D1_EVENT_VERIFIED_EXPERIMENT_REUSE_NOT_YET_ACCEPTED, twelve Git source documents, four historically reviewed original D1 effects, ZERO newly accepted P03 effects. First-run output files are immutable to a later changed replay.

Program file SHA-256: 89600ccaa04dd4ff0b1e50c68122f2927c7abbfab6ccd208c56104525ffca9db.
Proposal JSON file SHA-256: d9220667ddb60d89d12259ee553c0c3666e0d37329723360e00be311299baddd.
Preflight JSON file SHA-256: 06f5d287818c9d444d1ec8069358a2c9bc71d5a04285ac84cad22e38211e095f.
New test file SHA-256: 86caa7426cec6ebf16939460c542c88bab35818a9fc4a86cbdabb0a970dde79f.

## 3. Tests and negative controls

Exact newly added test command:

    .venv/Scripts/python.exe -m pytest -q -p no:cacheprovider
        tests/unit/test_r0_p03_v03_d1_real_event_admission_contract_v01.py

Initial observation: 21 passed in 23.34s. After adding exact pinned-evaluator-source verification and a deliberately forged local evaluator negative control: final **22 passed in 25.68s**, exit 0. The frozen owner packet and its canonical SHA-256 were unchanged.

Checks cover exact original source Git OIDs, original owner packet CRLF-vs-blob SHA, four effect equality and accounting, true Git parent/path, source attestation versus independently verified transport, REPLACE/OPEN_RESET relation, D1 AMEND output-shape boundary, new-world ZERO accepted J1/J2, and rejection of fabricated owner decision, changed effect, changed lineage, wrong source-fact parent/path, missing owner record, invalid packet hash, unknown Git path and nonexistent object.

The admission method intentionally rejects even an agent-authored dictionary claiming owner ACCEPT. A new, scope-limited owner act with a separately designed binding must be received before accepting any of these effects in P03-V2.

## 4. Expected postflight and unresolved source obligations

Actual postflight checks after Checkpoint 936 and Research 675 were routed:

- scripts/check_current_routing.py: PASS, checkpoint 936, latest formal experiment outcome INCOMPLETE, current boundary p-three-exact-experiment-owner-decision.
- scripts/check_knowledge_map.py: PASS, 19 topics, 24 foundations, 28 specifications, 675 Research records and 937 numbered checkpoints.
- scripts/check_checkpoint_metadata.py: 937/937 numbered checkpoints compliant, zero errors.
- scripts/check_model_collaboration_state.py: PASS, 28 state records.
- scripts/check_repository_integrity.py: PUBLIC_REPOSITORY_INTEGRITY=PASS, including Project Knowledge, source-map, checkpoint, collaboration and routing guards.
- git diff --check: PASS (Windows LF/CRLF advisory messages only).
- Previously established R0-P03 real-source, X1 and Project Knowledge authority suite rerun after documentation/routing updates: 180 PASS in 13.56s.
- New D1 source-owner-packet targeted suite: 22 PASS in 25.68s, including exact historical evaluator Git source pin. Total **202 PASS across two independently invoked test commands**. These are not 202 independent scored P03 tasks and the scientific outcome remains INCOMPLETE.

This is repository and experimental source-contract verification, not independent owner identity, new P03 J1 admission, source-owner J2 certification, formal navigation scoring or physical architecture selection.

Open: the source message's GitHub connector attestation is not independently provider-verified; the original D1 independent replay ended AMEND (shape cardinality), although semantic details were reconciled; new P03 natural-owner RELATIONAL declaration and owner-specific effect acceptance are not qualified; one actual event does not establish four-class task coverage or 60/20 eligibility. No model may convert these unresolved items to positive authority or score.

    ORIGINAL_D1_OWNER_REPLAY_SCOPE=VERIFIED
    REAL_GIT_PARENT_AND_PATH=VERIFIED
    NEW_P03_REUSE_PACKET=PREPARED_NOT_ACCEPTED
    PROPOSED_P03_J1_EFFECTS=4
    ACCEPTED_P03_J1=0
    QUALIFIED_P03_J2=0
    NEW_TESTS=22_PASS
    FORMAL_P03_SCORE=NONE
    PHYSICAL_TARGET_SELECTED=false
