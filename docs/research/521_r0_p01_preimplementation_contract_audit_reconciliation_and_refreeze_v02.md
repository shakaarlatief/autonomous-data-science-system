# Research 521: R0-P01 preimplementation contract-audit reconciliation and refreeze V0.2

**Date:** 2026-10-06
**Status:** PROBE_CLARIFICATION_ONLY / PROSPECTIVE V0.2 REFREEZE / HARNESS IMPLEMENTATION NEXT
**Parent:** Research 511-513, Research 518, Research 520, MC-0030 Message 013
**Candidate:** GOVERNED_LEDGER_KERNEL_V02
**Probe:** R0-P01
**Scope:** Reconcile the read-only implementability audit and Claude's bounded architectural triage, freeze complete probe constructions before owner-sensitive setup, correct the legacy inventory byte basis, and repair stale collaboration/current routing.
**Authority:** Prospective probe-contract clarification only. No owner execution, P01 result, physical target, production credential, migration, Specification 028 amendment, Runtime Bridge extraction or authority switch.
**Companion collaboration thread:** MC-0030
**Interaction environment:** ChatGPT
**Interaction session:** chatgpt-37
**Conversation title:** 37 - Project System Realization Architecture and Qualification
**Primary collaborator:** ChatGPT

## 1. Preserved preimplementation history

Codex's initial bounded implementation stopped before creating or modifying any source file because the exact envelope hashed by envelope_digest was underdetermined. No Git mutation or owner credential operation occurred.

The subsequent bounded read-only audit read the complete R0-P01 frozen surface and Research 511-513/518. It found thirteen blocker groups: digest representation; envelope projection; semantic-base construction/validation; security baseline/proof reuse; rotation/recovery templates; trust/history/admission state; compromise scenario; WebAuthn state/policy; Arm C selection/provenance; preview/timing order; trial/result normalization; infrastructure exemption evidence; and inventory byte basis. These were prospective implementability findings, not owner-trial failures or architecture results.

Claude independently triaged the architecture-sensitive subset in MC-0030 Message 013, committed at 1fe674c3836b7c36fc62e62e85b8a8e765beda30. Message 013 disclosed that THREAD/STATE still routed to R0-P02 candidate implementation despite P02 already being PASS. That disclosure remains historical evidence; Claude's message is not rewritten.

Claude's disposition is PROBE_CLARIFICATION_ONLY. ChatGPT independently reconciled the review and accepts that disposition. No blocking architectural defect has been established. GOVERNED_LEDGER_KERNEL_V02 remains retained; THIN_CENTRED_HYBRID_V03 is not reopened. R0-P02 remains PASS.

## 2. Prospective authority and object separation

Research 513 section 2.1 permits an explicit prospective superseding freeze for a protocol defect found before result observation. The V0.1 fixture.json, implementation_contract.md, security_control_contract.md, result_contract.json, Research 518 and Checkpoint 854 remain unchanged historical evidence.

implementation_contract_addendum_v02.md prospectively supersedes their incomplete or conflicting implementation-detail semantics only where explicitly stated. clarification_vectors_v02.json freezes public construction vectors; the corrected inventory rule replaces only its byte/provenance binding and preserves the former basis explicitly. The refreeze was first materialized in the local working tree for independent review. It does not by itself authorize owner execution; repository freeze/publication follows only after independent ChatGPT postflight through the governed Runtime Bridge Git path.

AC-1 through AC-6 are recorded as clarifications of V02, not architectural amendments:

1. **AC-1:** The predecision AcceptanceEnvelope is distinct from SignedAcceptanceStatement and durable AcceptanceRecord. The envelope excludes decision, shown_digest, proof, semantic_base_digest, signer_set_version, issued_at and decision provenance. Research 511's broader logical envelope describes the eventual record; Research 512 already separates the statement.
2. **AC-2:** Statement signer_set_version always participates in admission-time authority equality. Signer state enters the semantic base additionally only for an acceptance changing the trust root.
3. **AC-3:** Semantic-base dependencies preserve monotonic identity/version evidence. fixture.semantic_base.source_revision remains historical metadata and is excluded from the digested projection and selector; no repository-global binding is introduced.
4. **AC-4:** Stateless VERIFY is distinct from stateful ADMIT. First admitted ACCEPT/AMEND/REJECT consumes its ID; valid but unadmitted/stale statements consume nothing.
5. **AC-5:** Historical verification uses trust state at the record's ledger position. Compromise boundary is a sequence position; records at/before it remain historical and affected later records become REVIEW_REQUIRED / GOVERNING_OWNER. Control 13's declaration is DECLARATION_TRUSTED_SYNTHETIC_INPUT.
6. **AC-6:** PRIMARY authorizes ordinary acceptance/rotation; RECOVERY authorizes recovery trust-root transition and never ordinary acceptance in P01. Genesis is explicit synthetic V1; transitions are prospective and history remains verifiable.

The compromise-declaration authority matrix is a genuine but non-P01-blocking R1 issue. No default matrix suggested by Claude is adopted by this probe.

## 3. P01-C01 through P01-C16

The addendum freezes all sixteen prescribed clarifications: exact SHA-256/canonical representations; ordinary envelope and semantic-base projections; isolated scenarios; public trust-member representation; P0 and exact control mutations; rotation P5 and recovery P6; compromise reuse of S01; proof/run plan; WebAuthn challenge/state/expiry and recorded-not-gated signCount; C=S01/L01 and platform provenance; one decision timestamp; successful L01 and normalized unavailable/failed records; infrastructure receipts; Git-blob inventory; and the conservative attempt boundary.

The detailed addendum also supplies literal security envelope summaries/texts, public-value substitution sources, renderer item labels, version identifiers, historical transition positions, authorization observations, public evidence/result normalization and fail-closed consistency rules. These are probe instantiations of the prescribed choices, not production semantics.

Ordinary rotation's proposed target is denied by the current-role authorization predicate without adding another owner signing event. Recovery's unregistered-key negative control requires a mathematically valid synthetic non-owner proof that fails authority admission; no such key or proof is created by this refreeze.

P0/P5/P6 are the three additional owner security proof events per arm. Burden remains S01/S02/S03/L01; compromise reuses already-created S01. All ledgers are isolated in-memory probe scenarios. No owner signature, setup or attestation is performed now.

### ChatGPT's explicit refinement of Message 013

P01-C16 interprets Research 518 conservatively: Attempt 001 begins immediately before the first real owner-sensitive P01 action, including interactive SSH probe-key creation, WebAuthn registration, signing/assertion/recovery, or C owner attestation. Real setup observations cannot be used to repair code before recognizing attempt start.

The one predeclared unchanged WebAuthn registration repeat after SETUP_INTERRUPTED remains allowed inside that already-started attempt. It is not harness repair and grants no other retries. Raw setup/trial/control outcomes are preserved; no code/fixture/threshold/control repair or retry-to-green follows attempt start.

## 4. Exact artifact identities

Hash basis for these newly written local artifacts is exact UTF-8 LF file bytes, without BOM. The canonical strings inside the vectors have no terminal newline; the owner-view string is LF-terminated. These identities do not claim an uncreated commit.

| Artifact under experiments/r0_p01_owner_acceptance_v01/ | Bytes | SHA-256 |
|---|---:|---|
| implementation_contract_addendum_v02.md | 32641 | 1d5344ad16498517c4178959d34d2c4966baa054d3ef1e1f5c75f4396dab0dd6 |
| clarification_vectors_v02.json | 4573 | 326962f8de0a26d9cf0e7d21fd1f1137ee2c341c3a8dbe0bd250fcbf0011559e |
| legacy_volume_inventory_rule.json | 1841 | 4b7c261fdcc1b6343f91ad3f76ce505fbbafffcc4a5bc81e377e8d1df0e26ac2 |

## 5. Golden construction validation only

Independent Python-standard-library and Node-built-in reconstructions from fixture.json reproduced all four supplied hashes. Node additionally compared every reconstructed object, canonical JSON string and rendered string against the stored vectors. No credential or owner result was involved.

Golden case is Arm A / S01 / ACCEPT, acceptance_id R0-P01-A-S01:

```text
ordinary semantic base 76a7391fafd9683566f011be522dd4c3bfbe6bcfb0f1963500d1776b77b4d7a6
envelope              b4a274d82c6bc22b8c6168c2fdd7ee8b0b5dea8f6140907960022eb0fd6dc71c
shown                 e55af5a611651ca0efaae4aba2a013df9b9c87cbe8e61f147a612cd94f7e6d1d
statement             66b397b12d23d83b475e15e143272f68be7bd655d8432ff170de6985e87ade46
```

These are representation vectors, not an authenticated trial. They do not qualify a harness or classify R0-P01.

## 6. Legacy inventory correction

The authoritative source is docs/model_collaboration/threads/MC-0029/messages/006_claude_drp03_obligation_units_a.json. Its last-changing commit is b9fba658e422279d8f8b8193b8c1bda88302dcda and blob OID is 56ecc1da7677a6be450b3b38beaa9266d6ffb8a8, independently verified against the current authoritative HEAD.

The corrected GIT_BLOB_LF binding is 119155 bytes and SHA-256 2a3be898be6d7ac61d045a41492374d9fedb2ed3bf91734e4e07f0f20053355c. The old 119279-byte SHA-256 71fd3b691afb245e294e6012d29bc0780fe4d671fe7a4d09ef6a44845d3e0630 is retained as SUPERSEDED_WORKTREE_CRLF_BASIS. No source content is edited or silently normalized.

Direct recount from the Git blob confirms 97 acceptance units, 157 effect proxies and distribution 1->62, 2->17, 3->11, 4->7. Counts, formula and >100 / >90-minute gates remain unchanged.

## 7. Preserved experiment and authority boundary

Arms remain A OPENSSH_ED25519_PASSPHRASE_V01, B LOCALHOST_WEBAUTHN_ES256_UV_V01 and C CHATGPT_OWNER_USER_ROLE_DIGEST_ATTESTATION_V01. C remains a weaker non-selection comparator. All 13 security controls, zero-miss eligibility, 1/2/4/30-effect burden packet, small median <=60 seconds, individual small <=120 seconds with only the frozen receipt exception, successful L01 <=120 seconds, zero metadata edits, secret boundary, proof viability, classification and A/B 10-second/15-second/B tie-break rules are preserved.

No P01 result is observed. No credential is created or used. No WebAuthn registration/assertion or owner attestation occurs. No physical target, production implementation, migration, Runtime Bridge extraction, Specification 028 amendment or authority switch is authorized. Specification 028 remains current; latest scientific experiment outcome remains INCOMPLETE.

## 8. Next boundary

Checkpoint 857, Message 014 and the corrected current/MC-0030 routing name the next step: bounded Codex implementation of harness.py, webauthn_server.mjs and score.py only, under the V0.2 addendum and original preserved gates. Implementation review/freeze precedes every real owner-sensitive action. This documentation task neither implements nor runs those files.

```text
R0_P01_AUDIT=COMPLETE_13_BLOCKER_GROUPS
CLAUDE_MESSAGE_013=1fe674c3836b7c36fc62e62e85b8a8e765beda30
DISPOSITION=PROBE_CLARIFICATION_ONLY
ARCHITECTURE_AMENDMENT=false
R0_P01_CONTRACT=PROSPECTIVELY_REFROZEN_V02
R0_P01_HARNESS=NOT_IMPLEMENTED
R0_P01_OWNER_SENSITIVE_SETUP=NOT_STARTED
R0_P01_RESULT=NOT_OBSERVED
R0_P02=PASS
NEXT=BOUNDED_CODEX_R0_P01_HARNESS_IMPLEMENTATION
```

## 9. Repository validation

The existing managed interpreter executes the aggregate gate with bytecode writes disabled in the parent and child processes:

```text
PYTHONDONTWRITEBYTECODE=1
.venv/Scripts/python.exe -B scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume
```

Family-aware repository contracts, project-knowledge validation, checkpoint metadata, Knowledge Map, model-collaboration state and current routing all return PASS; PUBLIC_REPOSITORY_INTEGRITY=PASS. Current-routing validation includes the CURRENT_STATE fragments and latest-checkpoint freshness. No durable-evidence/materialization option is enabled and no extra report file is created.

An initial run using the host-global Python failed to import jsonschema for project-knowledge and model-collaboration validation. This was an interpreter/dependency binding defect, resolved by selecting the already-existing repository .venv; no package, dependency file or validator was installed or changed. The successful run does not bypass either validator.

The golden vectors are independently reconstructed by Python standard library and Node built-ins, not by a future harness. Direct Git-blob recount and public construction checks invoke no owner credential path. These checks validate the local documentation/refreeze transition only, not R0-P01 acceptance or harness qualification.
