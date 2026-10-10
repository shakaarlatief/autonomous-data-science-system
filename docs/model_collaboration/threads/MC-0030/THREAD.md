# MC-0030 Thread: V03 Physical Realization Architecture

**Thread:** MC-0030
**Status:** OPEN / R0-P01 V03 REV03 TARGETED REVIEW NEXT
**Review mode:** INDEPENDENT_THEN_COMPARATIVE
**Coordination branch:** v1-source-vault-bootstrap-resume
**Frozen independent base:** c459e9c8ac4435b80d4ac9d2bdb215aa72c13adc
**Task owner:** ChatGPT / chatgpt-37
**Independent reviewer/designer:** Claude / claude-04
**Active Claude conversation:** 04 - Assurance and Delivery Architecture Design
**Authority:** Collaboration evidence only.

## Purpose

Independently design and then comparatively reconcile the physical/software realization of owner-selected THIN_CENTRED_HYBRID_V03.

The logical architecture is selected.

The physical architecture is not.

## Sequence

    D-036 owner logical-architecture selection      COMPLETE
    Research 503 neutral R0 charter                 COMPLETE
    ChatGPT independent R0 physical candidate       COMPLETE / Research 504 + 508
    Claude independent physical design              COMPLETE / Message 001 / 071d4b5a...
    comparative exposure                            AUTHORIZED / BOTH POSITIONS FROZEN
    ChatGPT comparative reconciliation              COMPLETE / Research 511 / Message 002
    Claude comparative critique                     COMPLETE / Message 003 / 72046958...
    ChatGPT reconciliation                          COMPLETE / Research 512 / Message 004
    probe preregistration                           COMPLETE / Research 513 / Message 005
    R0-P02 exact fixture/harness freeze             COMPLETE / Research 514 / Message 006
    R0-P02 bounded candidate implementation         COMPLETE / Attempt 002
    R0-P02 score + live-host leg                   PASS / Research 517
    R0-P01 original fixture freeze                 COMPLETE / Research 518
    R0-P01 read-only implementability audit        COMPLETE / Codex / 13 blocker groups
    Claude P01 architectural triage                COMPLETE / Message 013 / 1fe674c...
    P01 V0.2 reconciliation/refreeze               COMPLETE / Research 521 / Message 014
    R0-P01 bounded harness implementation          COMPLETE / THREE FILES
    independent pretrial review + bounded repair   PASS / Research 522 / Validation 214 / Message 015
    R0-P01 owner execution                         COMPLETE / ATTEMPT 001 AMEND, PERMANENTLY CONSUMED
    R0-P01 prospective AMEND triage                COMPLETE / Research 524 / Message 017
    R0-P01 independent triage critique             COMPLETE / Message 018 / c4de7bb5
    R0-P01 ChatGPT critique reconciliation          COMPLETE / Research 525 / Message 019
    R0-P01 exact successor protocol drafting       COMPLETE / Research 526 / Message 020
    R0-P01 successor contract draft critique       COMPLETE / Message 021 / AMEND_DRAFT_BEFORE_FREEZE
    R0-P01 revised successor draft critique        COMPLETE / Message 023 / AMEND_REVISED_DRAFT
    R0-P01 REV03 targeted evidence-state review     NEXT / Claude / claude-04
    R0-P03                                        AFTER P01
    physical-target owner decision                  ONLY WHEN READY

## Independence

Claude may know the selected V03 logical architecture and current repository history.

Claude must not inspect the later ChatGPT R0 physical candidate before its own Message 001 is committed.

Current physical implementation is evidence, not target constraint.

## Write ownership

Claude may write only:

    docs/model_collaboration/threads/MC-0030/messages/**

## ChatGPT candidate freeze

Research 504 freezes R0-CANDIDATE-A.

Claude independent design is now next.

Claude must remain blind to:

    Research 504
    Checkpoint 841
    any summary of ChatGPT Candidate A
    any comparative artifact

until MC-0030 Message 001 is durably committed.

    PHASE=R0_CLAUDE_INDEPENDENT_DESIGN
    NEXT_ACTOR=claude

## Claude blind handoff freeze

Research 505 / Checkpoint 842 freezes the exact Message 001 handoff.

Claude must use the selected V03 logical architecture plus Research 503 and remain blind to Research 504 / Checkpoint 841 and any derivative Candidate-A material until Message 001 is durably committed.

    NEXT=CLAUDE_MESSAGE_001


## Owner scope clarification before Claude

The owner confirmed the Runtime Bridge separation direction and asked that the architecture overview and R0 basis be made clear before proceeding.

Research 506 now records:

    generic Codexless Runtime Bridge
        future standalone reusable product boundary

    ADS
        consumer / integration / policy / qualification owner

    immediate extraction
        not authorized

The prior semantic-organization/navigation omission also remains to be corrected explicitly.

Claude remains blind to Research 504 / Checkpoint 841.

    PHASE=R0_CHARTER_AMENDMENT
    NEXT_ACTOR=chatgpt
    NEXT=FREEZE_NEUTRAL_R0_AMENDMENT


## Neutral R0 amendment and ChatGPT addendum

Research 507 now explicitly adds semantic organization/navigation and external execution infrastructure to the neutral charter.

Research 508 extends ChatGPT Candidate A against those requirements and remains hidden from Claude.

The previously frozen Research 505 handoff is now stale and must be superseded before Claude is prompted.

    PHASE=R0_CLAUDE_HANDOFF_REFRESH
    NEXT_ACTOR=chatgpt
    NEXT=FREEZE_REFRESHED_CLAUDE_HANDOFF


## Refreshed Claude handoff

Research 509 supersedes Research 505 for launch.

Neutral Claude basis:

    Research 503
    Research 506
    Research 507

Hidden ChatGPT independent position:

    Research 504
    Research 508
    Checkpoint 841
    Checkpoint 844

Claude must also avoid CURRENT_STATE and the temporary ARCHITECTURE_PROGRAM_OVERVIEW until Message 001 is committed because those current orientation surfaces may summarize hidden Candidate-A work.

    PHASE=R0_CLAUDE_INDEPENDENT_DESIGN_AMENDED
    NEXT_ACTOR=claude
    NEXT=CLAUDE_MESSAGE_001

## Claude Message 001 intake and comparative transition

Claude Message 001 is durably committed at:

    071d4b5a232c07aaa3e96a2b91ba3ae1fd1a9c2d

Exact path:

    docs/model_collaboration/threads/MC-0030/messages/001_claude_independent_r0_physical_architecture.md

The commit changes exactly that one collaboration-message file. Claude attests that the blind boundary remained intact and reports no accidental exposure. The message identifies LEDGER-KERNEL as Claude's preferred independent architecture and keeps physical-target selection, implementation, migration and Specification 028 authority unchanged.

The pre-handoff coordination metadata incorrectly preallocated claude-05. No new Claude conversation was opened. The work was performed in the already-existing persistent Claude conversation 04 - Assurance and Delivery Architecture Design, whose provider-local interaction identity remains claude-04. PROVENANCE_CORRECTION.md records the bounded factual repair. The Claude-authored Message 001 is not rewritten; its disclosure accurately records the mismatch that existed when it was authored.

Both independent positions are now durably frozen. Comparative exposure is authorized. ChatGPT / chatgpt-36 is the next actor for comparative reconciliation.

    PHASE=R0_COMPARATIVE_RECONCILIATION
    NEXT_ACTOR=chatgpt
    CHATGPT_CANDIDATE=RESEARCH_504_PLUS_508
    CLAUDE_MESSAGE_001=071d4b5a232c07aaa3e96a2b91ba3ae1fd1a9c2d
    COMPARATIVE_EXPOSURE=AUTHORIZED
    PHYSICAL_ARCHITECTURE_SELECTED=false
    IMPLEMENTATION_STARTED=false
    MIGRATION_AUTHORIZED=false
    SPECIFICATION_028_AUTHORITY=UNCHANGED
    NEXT=CHATGPT_COMPARATIVE_RECONCILIATION

## ChatGPT comparative reconciliation

Research 511 and MC-0030 Message 002 compare both independently frozen R0 designs and reconcile them into:

    GOVERNED_LEDGER_KERNEL_V01

The comparison finds strong independent convergence on a repository-native immutable governing ledger, natural-owner J2, deterministic kernel/J3, disposable derived indexes, provider-neutral executor boundary, external Runtime Bridge ownership, guarded serialized authority admission, and shadow-before-migration discipline.

Material refinements include:

    owner-exclusive cryptographic proof binds the semantic Acceptance Envelope rather than requiring Git commit identity to be the canonical proof
    generated-first J2 with source-owned realization manifests only where needed
    relation-first deterministic navigation core with Research 217 / concerns / semantic retrieval still subject to a fair probe
    optional derived publication channel rather than a correctness-critical derived ref
    whole-repository Product / Project boundary with project/system and project/engineering separation

Three probes remain decision-critical before physical-target selection:

    R0-P01 owner authenticity and acceptance burden
    R0-P02 authority admission / ordering / concurrency
    R0-P03 semantic navigation / fresh-agent reconstruction

Comparative blindness has ended. Claude / claude-04 may now inspect Research 504 + 508 and Research 511 and must author one adversarial comparative critique as Message 003.

    PHASE=R0_CLAUDE_COMPARATIVE_CRITIQUE
    NEXT_ACTOR=claude
    RECONCILED_CANDIDATE=GOVERNED_LEDGER_KERNEL_V01
    PHYSICAL_ARCHITECTURE_SELECTED=false
    OWNER_DECISION=NOT_READY
    NEXT=CLAUDE_MESSAGE_003

## Claude critique reconciliation

Claude Message 003 is frozen at:

    72046958ce4f5c1f79375bb71dfa2291607e1ba9

Research 512 / MC-0030 Message 004 reconcile it as ACCEPT_WITH_REFINEMENTS and freeze:

    GOVERNED_LEDGER_KERNEL_V02

Material changes from V0.1 include:

    semantic-base rather than whole-repository stale binding
    canonical anti-replay signed acceptance statement
    sign-what-you-see owner flow
    governed trust-root / rotation / recovery / compromise semantics
    in-ledger hash-chained admission order rather than Git topology as authority
    explicit anti-rollback witness question inside R0-P02
    OBSERVABLE / RELATIONAL / EPHEMERAL J2 fact classes
    relation substrate selected while navigation architecture remains a probe question
    mandatory connector-readable derived orientation service level
    explicit project/system versus project/engineering direction rules
    provider-native executor contracts translated by ADS adapters
    capability-scoped idempotency and recovery
    private-J1 public consequence skeleton
    explicit owner/developer workflow
    Git / Python / R8-A assumptions made explicit and falsifiable

The three decision-critical probes remain:

    R0-P01 owner authenticity and acceptance burden
    R0-P02 authority admission / ordering / concurrency / tamper evidence
    R0-P03 semantic navigation / fresh-agent reconstruction

No probe has run.

    PHASE=R0_PROBE_PROTOCOL_PREREGISTRATION
    NEXT_ACTOR=chatgpt
    RECONCILED_CANDIDATE=GOVERNED_LEDGER_KERNEL_V02
    PHYSICAL_ARCHITECTURE_SELECTED=false
    PROBE_PROTOCOLS=NOT_YET_FROZEN
    NEXT=R0_P01_TO_P03_PROTOCOL_PREREGISTRATION

## Probe preregistration

Research 513 / MC-0030 Message 005 freeze the protocol family for:

    R0-P01 owner authenticity and acceptance burden
    R0-P02 authority admission / ordering / concurrency / tamper evidence
    R0-P03 semantic navigation / fresh-agent reconstruction

No result has been observed.

Preferred execution order:

    R0-P02 -> R0-P01 -> R0-P03

The next task is to freeze the exact P02 fixture, synthetic key handling, case list, harness boundary, witness variants, output schema and deterministic evaluator before any P02 implementation result is observed.

    PHASE=R0_P02_FIXTURE_HARNESS_FREEZE
    NEXT_ACTOR=chatgpt
    PROBE_PROTOCOL=RESEARCH_513_V01
    R0_P01=NOT_RUN
    R0_P02=NOT_RUN
    R0_P03=NOT_RUN
    NEXT=R0_P02_EXACT_FIXTURE_HARNESS_FREEZE

## R0-P02 exact fixture/harness freeze

Research 514 / MC-0030 Message 006 freeze the exact P02 deterministic surface:

    20 fixture cases
    frozen oracle
    candidate implementation contract
    deterministic scorer
    two metamorphic checks
    candidate blindness boundary
    single-attempt repair rule
    real-host squash-transport leg

Frozen hashes:

    fixture   dda68b1f4368dc982edffa2718330032f69842e7ac490dd84cbaaadcd4740d23
    oracle    ea059f0482298b21e290aa2b87823122d2ff1c583728bacbaa0c0568a17fdba4
    contract  bad3e5f0adb74c9887d0cb68d290e1a2534af5b836ad4a036bb0f4838106fa52
    scorer    616bbce9571b69cbefd7419fb0ab64de4919309122fc5719fcec68fab4fa07d8

No candidate.py exists at the freeze and no score has been observed.

    PHASE=R0_P02_CANDIDATE_IMPLEMENTATION
    NEXT_ACTOR=chatgpt
    R0_P02_RESULT=NOT_OBSERVED
    NEXT=BOUNDED_CODEX_R0_P02_CANDIDATE_IMPLEMENTATION

## Historical R0-P01 prospective refreeze (Checkpoint 857)

The preceding transition sections preserve historical boundaries. R0-P02 is now PASS through Research 517 / Checkpoint 853. Research 518 / Checkpoint 854 froze the original P01 surface, and Research 520 / Checkpoint 856 closed the Runtime Bridge interruption.

Codex stopped initial implementation before mutation because the contract was underdetermined. Its bounded read-only audit identified thirteen blocker groups. Claude Message 013 at 1fe674c3836b7c36fc62e62e85b8a8e765beda30 triaged the architecture-sensitive findings as PROBE_CLARIFICATION_ONLY. ChatGPT accepts that disposition. AC-1..AC-6 clarify GOVERNED_LEDGER_KERNEL_V02 rather than amend it; the compromise-declaration authority matrix remains non-P01-blocking R1 work.

Research 521 / Checkpoint 857 / Message 014 prospectively refreeze P01 V0.2 through implementation_contract_addendum_v02.md, clarification_vectors_v02.json and the corrected Git-blob inventory rule. Historical V0.1 contracts and Claude's routing-lag disclosure remain unchanged. The explicit ChatGPT refinement starts Attempt 001 before the first real owner-sensitive setup/credential action; no real setup observation can guide an out-of-attempt repair.

Research 521, Checkpoint 857 and Message 014 define the prospectively refrozen V0.2 contract after independent ChatGPT postflight. No P01 harness exists, no owner credential operation or attestation has occurred and no P01 result has been observed. The next action is bounded Codex implementation of harness.py, webauthn_server.mjs and score.py only, followed by independent implementation review/freeze before owner use. Specification 028 remains operational authority; production, migration, Runtime Bridge extraction and authority switch remain unauthorized.

    PHASE=R0_P01_HARNESS_IMPLEMENTATION
    NEXT_ACTOR=chatgpt
    INTERACTION_SESSION=chatgpt-37
    R0_P02=PASS
    R0_P01_CONTRACT=V02
    R0_P01_HARNESS=NOT_IMPLEMENTED
    R0_P01_RESULT=NOT_OBSERVED
    NEXT=BOUNDED_CODEX_R0_P01_HARNESS_IMPLEMENTATION

## R0-P01 harness implementation qualified; owner execution next

Research 522 / Validation 214 / Checkpoint 858 / Message 015 close the three-file harness implementation, independent ChatGPT adversarial pretrial review and bounded harness.py-only durability repair. ChatGPT / chatgpt-37 independently inspected the actual implementation and requalified the repair as ACCEPT_AFTER_BOUNDED_REPAIR. Exact qualified/frozen implementation hashes and byte lengths are recorded in those artifacts. Research 521 / Checkpoint 857 remain the prospective V0.2 contract freeze; historical collaboration evidence is preserved.

The original cross-process Attempt-001 restart bug was an implementation defect against already-frozen P01-C16, not an architecture or contract defect. The production non-secret %LOCALAPPDATA%\ADS-R0-P01\attempt-001.started.json claim is create-only, flushed/fsynced, never automatically removed/overwritten and has no reset/retry flag. Existing/partial markers fail closed; temporary synthetic tests confirm SECOND_ATTEMPT_001_START_ALLOWED=false. No production marker or owner probe keys exist.

Attempt 001 remains NOT STARTED. No real owner setup, WebAuthn registration/assertion, recovery signing, Arm C attestation or owner result occurred. Next is ChatGPT-orchestrated owner execution under the committed reviewed implementation. The durable claim and first raw snapshot must precede the first real owner-sensitive action; no result-guided implementation repair follows attempt start. This documentation task begins no owner execution and creates no commit.

R0-P02 remains PASS; R0-P03 remains pending; no physical target is selected. Specification 028 remains authoritative. Production implementation, migration, Runtime Bridge extraction and authority switch remain unauthorized.

    PHASE=R0_P01_OWNER_EXECUTION_READY
    NEXT_ACTOR=chatgpt
    INTERACTION_SESSION=chatgpt-37
    R0_P02=PASS
    R0_P01_CONTRACT=V02
    R0_P01_HARNESS=QUALIFIED
    R0_P01_ATTEMPT_001=NOT_STARTED
    R0_P01_RESULT=NOT_OBSERVED
    NEXT=ORCHESTRATE_R0_P01_OWNER_EXECUTION


## R0-P01 Attempt 001 scored AMEND; prospective triage next

Research 523 / Validation 215 / Checkpoint 859 / Message 016 close the real, permanently claimed Attempt 001 as AMEND / VIABLE_PROOF_WITHOUT_FULL_ELIGIBILITY. The durable marker and 25 append-only snapshots were preserved and hash-matched with an independent owner backup. Arm A exact-statement cryptography is proof-viable, but RECOVERY_CREDENTIAL_DRY_RUN failed (12/13 security controls PASS) and S02 recorded 130.849 seconds against the 120-second individual mechanical gate. Arm B WebAuthn registration and Arm C comparator were interrupted and remain unqualified. The original frozen evidence and control rules have not changed.

The owner reports using the primary passphrase when the recovery credential was required and considers it a small mistake. A brief role-specific prompt is a candidate prospective UX clarification only; broader real-decision contextual presentation is a separate owner-experience requirement. An initial independent scorer INVALID stemmed from unsuitable readOnly temporary-file permissions; a proper unchanged scorer run reported AMEND. The exact diagnostic is in Validation 215.

No reset/retry-to-green, new owner attempt, production credential, physical target, migration, or authority switch is authorized. R0-P02 remains PASS, R0-P03 pending, Specification 028 unchanged. ChatGPT / chatgpt-37 owns bounded prospective AMEND triage and may request architecture-sensitive Claude critique before any new refreeze.

    PHASE=R0_P01_ATTEMPT_001_AMEND_PROSPECTIVE_TRIAGE
    NEXT_ACTOR=chatgpt
    R0_P01_ATTEMPT_001=CONSUMED_AND_PRESERVED
    R0_P01_RESULT=AMEND
    PHYSICAL_ARCHITECTURE_SELECTED=false
    NEXT=PROSPECTIVE_R0_P01_AMEND_TRIAGE


## R0-P01 prospective AMEND triage completed; independent critique next

Research 524 / Checkpoint 860 / Message 017 compare five prospectively legitimate ways forward after the preserved Attempt 001 AMEND. The preferred *candidate* is a full independently claimed successor qualification, not selective retries, while preserving every original security and timing gate. Owner feedback on minor recovery-key passphrase confusion supports a simple role cue rather than crypto architecture redesign. S02 timing miss and the interrupted B/C arms remain unqualified observations. Future real-decision context/provenance is a separate UX requirement.

This stage does not freeze, implement, execute or authorize a successor probe. Claude / claude-04 is the preferred next independent reviewer under the established comparative collaboration boundary; it may write only a new MC-0030 message, not mutate contracts or observed owner evidence. ChatGPT remains task owner for comparative reconciliation after the review. R0-P02 PASS; R0-P03 pending; no physical target selected; Specification 028 unchanged.

    PHASE=R0_P01_PROSPECTIVE_TRIAGE_PEER_REVIEW_PENDING
    NEXT_ACTOR=claude
    R0_P01_RESULT=AMEND
    FOLLOWUP_ATTEMPT=NOT_AUTHORIZED
    NEXT=CLAUDE_INDEPENDENT_TRIAGE_CRITIQUE


## Claude Message 018 and independent ChatGPT reconciliation

Claude Message 018 was committed at c4de7bb52c7f85d7ecf230a622e7ba69329a6121, changing only that allowed message path. Its AMEND_PROSPECTIVE_DIRECTION critique was reconciled in Research 525 / Checkpoint 861 / Message 019 as ACCEPT_WITH_QUALIFICATIONS. The original Attempt 001 AMEND and all failed security/timing observations remain unchanged.

A complete separately identified successor is a candidate, not authorized. It requires a prospectively fixed stopping rule (no automatic Attempt 003), fresh keys and signed IDs, bounded SSH unlock opportunities with honest WebAuthn-opacity disclosure, safe ceremony guidance and independent scorer known answers. Cross-process resumability is not already supported by the old numbered snapshots; it requires a new independent recovery model or should be omitted. Validation 216 corrects Research 523 and Checkpoint 859 raw-file SHA-256 transcriptions by appended erratum, leaving historical documents intact. Research 525 tracks real owner-view contextual provenance and rare-key durability for future R1.

ChatGPT / chatgpt-37 owns the next **non-executing contract draft**. Claude / claude-04 may be asked for a further bounded critique after drafting. No credential use, owner trial, refreeze, physical target, production implementation, migration or authority switch is authorized.

    PHASE=R0_P01_SUCCESSOR_PROTOCOL_DESIGN_PENDING
    NEXT_ACTOR=chatgpt
    R0_P01_ATTEMPT_001=IMMUTABLE_AMEND
    SUCCESSOR_PROTOCOL=UNFROZEN
    NEXT=CHATGPT_EXACT_SUCCESSOR_CONTRACT_DRAFT


## R0-P01 V03 successor unfrozen draft completed; critique next

Research 526 / Checkpoint 862 / Message 020 record a detailed draft contract at docs/research/r0_p01_successor_design/R0_P01_CONTRACT_V03_UNFROZEN_DRAFT.md and a candidate machine-readable outcome-policy JSON. No real credential, claim, fixture freeze or scored trial occurred. Original P01 Attempt 001 remains AMEND, with recovery FAIL and S02 >120 seconds unchanged.

The draft keeps Research 513 security, threshold, selection and volume gates. Its candidate improvements include a separate fresh-key/signature namespace, bounded same-event SSH unlock attempts, explicit no-WebAuthn-parity disclosure, three-tier owner-view boundaries, verifier known answers, safe localhost opening, diagnostic timers, **no cross-process resumption**, and a finite no-automatic-Attempt-003 stop rule. Native OpenSSH error classification and interrupted no-result taxonomy are explicit blockers, not presumed solved.

Claude / claude-04 is the preferred next critical reviewer under MC-0030 messages-only write scope. ChatGPT retains task-owner authority to reconcile critique later. No successor execution or physical target selection authorized.

    PHASE=R0_P01_V03_UNFROZEN_DRAFT_INDEPENDENT_REVIEW_PENDING
    NEXT_ACTOR=claude
    R0_P01_ATTEMPT_001=IMMUTABLE_AMEND
    R0_P01_ATTEMPT_002=NOT_AUTHORIZED
    NEXT=CLAUDE_SUCCESSOR_V03_DRAFT_CRITIQUE


## Claude Message 021 reconciled, successor draft REV02 independent review pending

Claude Message 021, e431b4de38949a6e9014b02a1212bcc6039815f7, added exactly that review message and returned AMEND_DRAFT_BEFORE_FREEZE. Research 527 / Checkpoint 863 / ChatGPT Message 022 reconcile all five blocking findings and revise the two unfrozen V03 candidate artifacts. Native SSH stderr classifier removed; owner R/S invocations and preconditions proposed. Every claimed attempt scored under prospective G1/G2, tri-state verification with preclaim KAT, structural signed context+ID, synthetic P5/P6 member templates, and genuinely finite two-new-claim policy proposed. G1/G2 family interpretation and owner stopping-policy approval remain outstanding. Original Attempt 001, V02 frozen code and evidence untouched.

Claude / claude-04 may perform only a new bounded critique in Message 023. No other authoring permission, key operation, new claim, owner proof, freeze or physical target authorization.

    PHASE=R0_P01_V03_REV02_UNFROZEN_PEER_REVIEW_PENDING
    NEXT_ACTOR=claude
    ATTEMPT_001=AMEND_IMMUTABLE
    ATTEMPT_002=NOT_AUTHORIZED
    NEXT=CLAUDE_V03_REV02_REVIEW


## Claude Message 023 reconciled; R0-P01 V03 REV03 targeted recheck pending

Claude Message 023 was committed as the sole changed file at 8783994f267718be6a24a86fb6c4151d0ca93249, yielding AMEND_REVISED_DRAFT. Research 528, Validation 217, Checkpoint 864 and Message 024 reconcile R1-R4 and bounded R5-R9 into the UNFROZEN candidate contract and policy. Per-arm proof evidence_state fixes false REOPEN; INVALID reasons now derive from fixed raw flags; VERIFIER_ERROR sets instrument not attempt-integrity; JSON blockers exactly match contract and policy is genuinely capped. The owner hash witness, snapshot atomicity and RP interrupt are future implementation obligations, not proved behavior.

Next Claude / claude-04 may commit only a narrowly targeted Message 025 check. Neither G1/G2 Research 513 interpretation nor owner stopping-policy assent is granted. No contract/fixture freeze, Attempt 002, owner key, credential, production target or semantic authority switch has occurred. R0-P02 PASS; R0-P03 pending, Specification 028 unchanged.

    PHASE=R0_P01_V03_REV03_TARGETED_RECHECK_PENDING
    NEXT_ACTOR=claude
    ATTEMPT_001=IMMUTABLE_AMEND
    ATTEMPT_002=NOT_AUTHORIZED
    NEXT=CLAUDE_MESSAGE025_TARGETED_RECHECK
