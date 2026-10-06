# R0-P01 V0.2 Prospective Implementation-Contract Clarification

**Date:** 2026-10-06
**Status:** PROSPECTIVE REFREEZE / BEFORE IMPLEMENTATION AND OWNER-SENSITIVE SETUP
**Protocol:** R0-P01-V01
**Contract revision:** R0-P01-CONTRACT-V02
**Scope:** Resolve the preimplementation audit through probe-only constructions and AC-1 through AC-6, without changing the architecture, arms, controls, thresholds or selection rules.
**Authority:** Research 521 / Checkpoint 857 / MC-0030 Message 014. Local prospective contract artifact; no owner execution or production authority.

## 1. Precedence and preserved boundary

Read this addendum together with fixture.json, implementation_contract.md, security_control_contract.md, result_contract.json, clarification_vectors_v02.json and the prospectively corrected legacy_volume_inventory_rule.json.

This addendum supersedes incomplete or conflicting V0.1 implementation details only where it explicitly defines them. The original fixture, implementation contract, security contract, result contract, Research 518 and Checkpoint 854 remain historical evidence and are not edited. Research 513 section 2.1 permits this correction before result observation.

GOVERNED_LEDGER_KERNEL_V02 is retained. AC-1 through AC-6 are architecture clarifications, not amendments. Claude Message 013 is accepted as PROBE_CLARIFICATION_ONLY. Its historical routing-lag disclosure remains unchanged. The compromise-declaration authority matrix remains an open, non-P01-blocking R1 issue; this probe does not choose that matrix.

No harness exists at this freeze. No owner credential setup/use, WebAuthn registration/assertion, owner attestation or owner result has occurred. Implementation next remains confined to harness.py, webauthn_server.mjs and score.py with Python standard library, Node built-ins and browser WebAuthn APIs. Owner operations remain outside implementation.

## 2. AC-1 through AC-6: architectural clarifications

### AC-1: Envelope, statement and record

AcceptanceEnvelope is the canonical semantic proposal fixed before the owner decision. Only that proposal is hashed as envelope_digest. It excludes decision, shown_digest, proof, semantic_base_digest, signer_set_version, issued_at and decision provenance.

SignedAcceptanceStatement records the owner's decision and contains exactly context, project_id, acceptance_id, envelope_digest, shown_digest, decision, semantic_base_digest, signer_set_version and issued_at.

AcceptanceRecord is durable evidence containing envelope, statement, proof and renderer/provenance information. Research 511's broader logical-envelope wording describes this eventual record. Research 512's separate statement implicitly narrows the hashed envelope. No proof hashes itself.

### AC-2: Signer authorization

signer_set_version is always a statement field. At the candidate synthetic ledger position, admission requires equality with the current signer-set version. A signature valid under an older historical set does not authorize new admission after rotation.

Signer-set state additionally participates in semantic_base_digest only when the acceptance changes the trust root. Ordinary P01 trials and P0 do not include it in the semantic base.

### AC-3: Semantic-base hygiene

The semantic base binds governing state, never repository state. fixture.semantic_base.source_revision remains historical fixture metadata and is excluded from both the digested base projection and dependency selector.

Each ordinary dependency carries effect_id, status, lineage_head and contract_revision. Identity/version evidence is retained to prevent ABA/value-reversion staleness. Unrelated repository metadata is excluded.

### AC-4: Verify versus admit

VERIFY is stateless: proof + exact statement + public credential -> VALID or INVALID. It performs the arm's independent cryptographic verification; it does not consume IDs or consult current ledger state.

ADMIT is stateful. It requires VERIFY=VALID, an unconsumed acceptance_id, equality of statement.signer_set_version with the current version, equality of semantic_base_digest with the recomputed current base, and the appropriate current credential role. Record/envelope/statement identity and digest consistency must also be checked.

The first admitted decision consumes its ID for ACCEPT, AMEND or REJECT. ACCEPT applies the proposed effects; AMEND/REJECT append the decision without applying effects. A validly signed but unadmitted statement, including a stale statement, consumes nothing. A revised proposal is a new acceptance, not a second admitted decision for a consumed ID.

### AC-5: Historical trust and compromise

Historical records verify against the signer set in force at their own ledger sequence position. issued_at is provenance, never order or a compromise boundary.

For boundary b, records at sequence <= b remain historical. Otherwise-valid records after b from the affected credential become REVIEW_REQUIRED with resolving_owner=GOVERNING_OWNER. They are not silently current and pre-boundary proofs are not retroactively invalidated.

Control 13 receives DECLARATION_TRUSTED_SYNTHETIC_INPUT. It tests classification consequences, not which credential may declare another compromised. That authority matrix remains R1 work.

### AC-6: P01 trust roles

PRIMARY authorizes ordinary acceptances and ordinary trust-root rotation. RECOVERY authorizes recovery trust-root transitions and never ordinary acceptance in P01. Synthetic V1 genesis is explicit; transitions are prospective and preserve historical verification.

## 3. P01-C01: Digests and canonical bytes

All digests are SHA-256. Canonical-object digest fields are lowercase hexadecimal strings of exactly 64 characters with no prefix. shown_digest is the same representation of SHA-256 over the exact displayed UTF-8 bytes.

Canonical JSON is UTF-8 without BOM or trailing newline; object keys are sorted, separators are compact (comma and colon without spaces), arrays retain their specified order, and NaN/Infinity are forbidden. Unicode strings are encoded as UTF-8 rather than unnecessarily ASCII-escaped; JSON-required escaping is retained. Current signed keys and fixture values are ASCII. Object-key ordering is lexicographic by Unicode code point. This remains PROBE_JSON_V01_SORTED_KEYS_COMPACT_UTF8_TEST_ONLY, not production canonicalization.

Arm B challenge is unpadded base64url of the raw 32-byte SHA-256 of canonical statement bytes, not of a hexadecimal digest string. Arm C uses the lowercase hexadecimal SHA-256 of those statement bytes.

## 4. P01-C02: Ordinary envelope and statement sources

For S01/S02/S03/L01, construct exactly:

```text
{
  "schema": "R0-P01-ENVELOPE-V01",
  "project_id": fixture.project_id,
  "acceptance_id": "R0-P01-<ARM>-<TRIAL>",
  "item_id": trial.trial_id,
  "title": trial.title,
  "summary": trial.summary,
  "effects": trial.effects,
  "dependency_selector": {
    "grammar_version": fixture.semantic_base.grammar_version,
    "predicate_semantics_version": fixture.semantic_base.predicate_semantics_version,
    "dependencies": [{"effect_id": ..., "contract_revision": ...}]
  }
}
```

effects retain every fixture field and their fixture order. The selector contains both BASE-A and BASE-B from fixture.semantic_base.effects, sorted by effect_id, and no other dependency. class, consequence and issued_at are excluded from the envelope. source_revision is excluded.

Statement sources are fixed:

| Field | Source |
|---|---|
| context | fixture.statement_context |
| project_id | envelope.project_id, equal to fixture.project_id |
| acceptance_id | envelope.acceptance_id |
| envelope_digest | C01 digest of the exact envelope |
| shown_digest | C01 digest of the exact displayed owner view |
| decision | Captured owner ACCEPT / AMEND / REJECT; never inferred from proof or transport |
| semantic_base_digest | C01 digest of the C03 projection recomputed from scenario state |
| signer_set_version | Current scenario signer-set version at decision/admission |
| issued_at | Exact trial.issued_at string; fixed security timestamps below for P0/P5/P6 |

The owner view uses the V0.1 renderer verbatim. Its Trial label is envelope.item_id, including security items. Project, Acceptance, Title, Summary and Effects come from the envelope. Semantic base is the recomputed digest. Each effect contributes exactly two leading ASCII spaces before its bracket line, Subject line and Text line. Indices are decimal and one-based. All lines end in LF; the final END line also ends in LF. The same in-memory bytes are displayed and hashed. A terminal/browser wrapper cannot replace those bytes.

## 5. P01-C03: Semantic base and expected-value validation

The ordinary base is exactly:

```text
{
  "grammar_version": ...,
  "predicate_semantics_version": ...,
  "dependencies": [
    {"effect_id": ..., "status": ..., "lineage_head": ..., "contract_revision": ...}
  ]
}
```

Dependencies are BASE-A and BASE-B, sorted by effect_id and selected by the envelope's selector. Resolve them in the current isolated scenario state; do not substitute a repository revision. All selector identities, pinned contract revisions and grammar/predicate versions must match before signing/admission. Missing, duplicate or mismatched dependencies fail closed.

The expected ordinary V1 digest is 76a7391fafd9683566f011be522dd4c3bfbe6bcfb0f1963500d1776b77b4d7a6. Independently recompute the object/digest from the hash-bound fixture and compare to clarification_vectors_v02.json before owner display. The stored vector does not replace recomputation. A mismatch blocks execution; it is not normalized or silently repaired.

For TRUST_ROOT_ROTATE and TRUST_ROOT_RECOVERY_ROTATE only, additionally include:

```text
"signer_set": {"version": current_version, "members_digest": C05_members_digest}
```

These grammars identify the trust-root subject in the probe. Their dependency selector uses the ordinary selector plus "trust_root_subject":"SYNTHETIC-SIGNER-SET"; no live signer version or semantic-base digest is placed in the selector. Resolve that subject against current scenario trust state. No owner-signed compromise declaration is constructed in control 13.

## 6. P01-C04: Isolated scenarios and ledger order

Use deterministic in-memory synthetic ledgers, separately for each arm and attempt. The scenarios are BASE_SECURITY (controls 1-10), BURDEN, ROTATION, RECOVERY and COMPROMISE. Each has its own consumed-ID registry and immutable trust-state history. State never leaks between scenarios or attempts. No persistent production ledger is created.

Each fresh scenario begins at seq1 GENESIS with V1, recording its public members and explicit synthetic/TOFU provenance. The owner confirms initial public identifiers in setup; no model supplies a secret. All ordinary semantic dependencies start at the fixture V1 projection.

BASE_SECURITY admits P0 at seq2; failed mutations/replay append nothing. BURDEN processes S01 -> S02 -> S03 -> L01 under unchanged V1. Each admitted decision advances sequence; an unadmitted decision does not. ROTATION and RECOVERY independently copy and historically admit the already-created P0 at seq2, then test their transition at seq3. They do not request another P0 proof. COMPROMISE uses the exact C09 positions.

A transition record verifies under the pre-transition trust state at its own position. Only an admitted ACCEPT applies the new version, effective for subsequent positions. AMEND/REJECT consume the decision ID but do not change trust state. A required security transition that is not ACCEPT is a failed control, not permission to request a replacement proof.

## 7. P01-C05: Trust members and public setup receipts

A member is exactly:

```text
{"role":"PRIMARY|RECOVERY", "kind":"SSH_ED25519|WEBAUTHN_ES256", "public_id":"<probe public identifier>"}
```

Sort members lexicographically by role, kind, public_id. members_digest is the lowercase hexadecimal SHA-256 of the canonical sorted members array.

SSH public_id is "SSH-ED25519-SHA256-HEX:" followed by lowercase SHA-256 of the decoded OpenSSH public-key blob. Ignore the public comment for identity; validate Ed25519 type. WebAuthn public_id is "WEBAUTHN-ES256-SPKI-SHA256-HEX:" followed by lowercase SHA-256 of SPKI DER. Import and validate the actual ES256/P-256 key, not merely a client algorithm claim. Store the registered WebAuthn credential ID separately for byte equality.

Initial version is SIGNERS-P01-V1. Arm A has PRIMARY=owner_primary_ed25519 and RECOVERY=owner_recovery_ed25519. Arm B has PRIMARY=the registered WebAuthn credential and RECOVERY=owner_recovery_ed25519. Public setup receipts bind those members, public verification material, credential ID where applicable, explicit owner confirmation/TOFU and setup status. Only public material is preserved; private-key paths are not public evidence. Non-empty passphrase and no-agent requirements remain unchanged.

## 8. P01-C06: Controls 1-10 and P0

Exactly one owner-authenticated baseline proof P0 is created per cryptographic arm. Its envelope uses the C02 schema/selector with these substitutions:

```text
acceptance_id: R0-P01-<ARM>-SEC-VALID_ACCEPTANCE
item_id: SECURITY_BASELINE
title: Security control baseline
summary: One-effect synthetic baseline for R0-P01 exact-binding controls.
effects: [{
  "effect_id":"SEC-BASE-001",
  "grammar":"REQUIRE",
  "subject":"SYNTHETIC-SECURITY-BASELINE",
  "text":"Synthetic low-consequence security baseline effect for R0-P01 exact-binding qualification.",
  "independently_acceptable":true
}]
decision: ACCEPT
issued_at: 2026-10-04T01:00:00Z
```

The text is a single string without the line wrapping used in the handoff. Capture the owner's actual decision; do not manufacture ACCEPT. If the baseline is not the required valid ACCEPT, record failure and do not request another baseline to rescue this attempt.

Control result keys are the exact 13 frozen keys. Controls 2-10 reuse P0; their result key does not create another signed security acceptance ID. Evaluate each mutation independently from an unmodified copy of P0 and its statement; no mutations accumulate.

| Control | Exact action and PASS predicate |
|---|---|
| 1 VALID_ACCEPTANCE | VERIFY=VALID and first ADMIT succeeds |
| 2 FORGED_OR_AGENT_PREPARED_PROOF_REJECTS | XOR the first raw proof byte with 0x01; VERIFY rejects. For SSH this is decoded SSHSIG payload before re-armoring; for WebAuthn it is signature DER. Never replace it with a valid forged proof. |
| 3 CHANGED_ENVELOPE_REJECTS | Append " [MUTATED]" to SEC-BASE-001.text; recompute envelope_digest in the presented statement, reuse P0; VERIFY rejects |
| 4 CHANGED_SHOWN_VIEW_REJECTS | Change the first displayed byte R to X; recompute shown_digest, reuse P0; VERIFY rejects |
| 5 DECISION_SUBSTITUTION_REJECTS | ACCEPT -> REJECT in the presented statement; VERIFY rejects |
| 6 CROSS_PROJECT_REPLAY_REJECTS | statement.project_id -> fixture.wrong_project_id; VERIFY rejects |
| 7 ACCEPTANCE_ID_REPLAY_REJECTS | A: statement.acceptance_id -> R0-P01-<ARM>-SEC-ACCEPTANCE_ID_REPLAY_REJECTS; VERIFY rejects. B: exact second ADMIT of P0 rejects its consumed ID even though VERIFY may remain VALID. Both must pass. |
| 8 SEMANTIC_BASE_MISMATCH_REJECTS | Change BASE-A.lineage_head to BASE-A-1 in a copied base; recompute statement.semantic_base_digest, reuse P0; VERIFY rejects |
| 9 UNRELATED_REPOSITORY_LANDING_DOES_NOT_INVALIDATE | Add only separate in-memory metadata {"repository_note":"UNRELATED-P01-SYNTHETIC-LANDING"}; leave envelope, statement, displayed bytes and proof unchanged; exact P0 VERIFY remains VALID |
| 10 SIGNER_SET_MISMATCH_REJECTS | statement.signer_set_version -> SIGNERS-P01-V999-SYNTHETIC; reuse P0; VERIFY rejects |

Negative crypto controls must actually check the proof against the changed statement, not report PASS solely from a caller-supplied rejection flag. They do not ADMIT changed proposals. Missing baseline proof makes dependent controls FAIL, never NOT_APPLICABLE for A/B.

## 9. P01-C07: Ordinary rotation and P5

Use fresh ROTATION V1 state, independent of burden/recovery. The envelope uses the C02 schema, C03 trust selector, and a single independently_acceptable=true effect:

```text
acceptance_id: R0-P01-<ARM>-SEC-TRUST_ROOT_ROTATION_DRY_RUN
item_id: TRUST_ROOT_ROTATION
title: Synthetic trust-root rotation
summary: Synthetic prospective ordinary trust-root rotation for R0-P01.
effect_id: TRUST-ROTATE-001
grammar: TRUST_ROOT_ROTATE
subject: SYNTHETIC-SIGNER-SET
text: Rotate SIGNERS-P01-V1 -> SIGNERS-P01-V2; PRIMARY: <target public_id>; RECOVERY: <target recovery public_id>.
issued_at: 2026-10-04T01:01:00Z
required decision: ACCEPT
```

Substitute the exact C05 public identifiers without angle brackets. V2 (SIGNERS-P01-V2) has, for A, PRIMARY=Arm-A recovery and RECOVERY=Arm-A original primary. For B it has PRIMARY=Arm-A primary and RECOVERY=Arm-A recovery. Both complete member bindings are visible in the rendered effect. V1 PRIMARY signs P5. VERIFY and role-correct ADMIT must succeed before the version changes.

Independently evaluate the ordinary-rotation authorization predicate for the proposed target alone against V1: A's target is RECOVERY, not PRIMARY; B's target is not a V1 PRIMARY member. It must deny and leave state unchanged. This role-admission negative test does not request another owner signature or fabricate one; P01 tests that even possession of the candidate credential cannot grant the missing current PRIMARY authority. Merely observing a bad signature is not this authority test. Preserve this predicate result alongside the valid P5 proof and transition receipt.

## 10. P01-C08: Recovery and P6

Use fresh RECOVERY V1 state. The envelope has the C02 schema, C03 trust selector and one independently_acceptable=true effect:

```text
acceptance_id: R0-P01-<ARM>-SEC-RECOVERY_CREDENTIAL_DRY_RUN
item_id: RECOVERY_ROTATION
title: Synthetic recovery rotation
summary: Synthetic prospective recovery trust-root rotation for R0-P01.
effect_id: TRUST-RECOVERY-001
grammar: TRUST_ROOT_RECOVERY_ROTATE
subject: SYNTHETIC-SIGNER-SET
text: Recover SIGNERS-P01-V1 -> SIGNERS-P01-V2R; PRIMARY: <Arm-A recovery public_id>; RECOVERY: <Arm-A original primary public_id>.
issued_at: 2026-10-04T01:02:00Z
required decision: ACCEPT
```

V2R is SIGNERS-P01-V2R for both arms, with PRIMARY=Arm-A recovery and RECOVERY=Arm-A original primary. V1 RECOVERY signs P6 using the dedicated passphrase-protected Arm-A recovery Ed25519 key. Verify under V1 and admit under RECOVERY authority; only then apply V2R prospectively.

The negative control uses a probe-only synthetic non-owner Ed25519 test key absent from V1. Its mathematically valid proof over the exact recovery statement must VERIFY=VALID under that test public key but fail recovery-authority ADMIT; no ID or version changes. This test material is explicitly a test double, not owner evidence. It is generated only when the reviewed harness executes that control, not by this refreeze.

Reverify P0 historically at its V1 sequence position after recovery. Current V2R membership must not replace its historical trust state. Preserve the public evidence and authority/transition outcomes, never a recovery secret.

## 11. P01-C09: Compromise classification

Fresh COMPROMISE ledger: seq1 GENESIS V1; seq2 the already-created valid P0; boundary=2; seq3 the already-created successful S01 proof from the same PRIMARY. The declaration is DECLARATION_TRUSTED_SYNTHETIC_INPUT and names that PRIMARY public_id. There is no new signed declaration or owner invocation.

Expected comparison: seq2 remains unchanged historical; otherwise-valid seq3 is REVIEW_REQUIRED / GOVERNING_OWNER. Both rows are required evidence. If no valid S01 proof exists, control 13 is FAIL; do not request another owner proof. Sequence, not issued_at, determines the boundary.

## 12. P01-C10: Owner-proof plan and run order

Per cryptographic arm: setup -> P0 and controls 1-10 -> S01, S02, S03, L01 -> rotation P5 -> recovery P6 -> compromise classification. Additional security proof events are exactly P0, P5 and P6; control 13 reuses S01. No security event is included in the 3+1 burden timings. Scenario copies and offline mutations do not initiate owner ceremonies.

Burden success permits the owner's chosen ACCEPT, AMEND or REJECT. Security transitions require the prescribed ACCEPT to demonstrate the transition; a different owner decision is preserved, not coerced or retried. The synthetic non-owner recovery negative proof is distinct from owner-proof events.

## 13. P01-C11: WebAuthn ceremony state

The RP remains http://localhost:8765, rpId localhost, ES256/COSE -7 only, UV required, attestation none, residentKey preferred and authenticatorAttachment omitted. Registration uses the three frozen browser response methods and SPKI DER with Node built-in crypto.

Node generates 32 cryptographically random registration challenge bytes. Keep one pending registration record containing the challenge, attempt/arm identity, issuance/expiry and unused status. It expires 120 seconds after issuance and is single use, consumed on the first submitted response or terminal cancellation/timeout. Registration verification independently checks webauthn.create type, the exact pending challenge and origin, rpIdHash and UP/UV, and actual ES256 public material. Store the resulting confirmed credential ID/public key only after verification; do not replace a registered root through an unsolicited registration.

An assertion record contains exact statement SHA-256, acceptance ID, attempt/arm identity, issuance/expiry and unused status. Keep one pending assertion, expire it after 120 seconds, and consume it on the first submitted response or terminal cancellation/timeout. allowCredentials contains only the registered credential ID. The submitted response cannot choose a different statement, public key or trust root. The qualified local client owns the view, decision and canonical preview.

Assertion verification independently performs every V0.1 check: webauthn.get type, exact unpadded base64url statement digest, exact origin, rpIdHash, UP, UV, registered credential ID equality and ES256 verification over authenticatorData || SHA256(clientDataJSON). Reject malformed structures and inconsistent ES256 keys. signCount is recorded if available and never used as a monotonicity gate. No additional counter, backup-state, attachment or transport policy may silently make a conforming ES256/UV arm ineligible. Offline proof verification does not require a live pending ceremony; stored bytes support deterministic mutation controls without another owner ceremony.

Capability inability to meet ES256/UV or the required response methods is NOT_REALIZABLE. Owner cancellation/timeout is SETUP_INTERRUPTED, not capability failure. One predeclared repeat of the exact unchanged registration step is permitted after the first such interruption; its challenge is a fresh nonce with identical policy. Record both setup events. No third registration attempt, code repair or retry-to-green is allowed. A second interruption leaves B incomplete and ineligible. This narrow setup repeat does not authorize repeating failed burden/security proofs.

## 14. P01-C12: Arm C comparator

Use exactly S01 and L01. Construct their C envelopes/statements with the same field-source rules and C-specific acceptance IDs. Present exactly R0-P01 PLATFORM ATTEST <acceptance_id> <lowercase statement SHA256>.

Completion requires that exact line in a user-authored ChatGPT message. Preserve expected/observed lines, equality, user-role observation, platform/chat provenance reference, available interaction count and non-secret friction information. A task-owner observation receipt identifies that message; a terminal paste alone is not user-role provenance. State explicitly that provenance is not independently repository-verifiable. End comparator observation at deterministic line/provenance checking; report available timings but impose no C mechanical timing gate. C controls are NOT_APPLICABLE and selection_eligible is always false. It never receives cryptographic VERIFY/ADMIT authority.

## 15. P01-C13: Timing

After the complete exact owner view is displayed, start semantic review. One decision-capture timestamp simultaneously ends review and starts mechanical time. Final canonical statement construction/preview occurs inside the mechanical interval. End mechanical time only at deterministic local proof verification result, successful or failed. Collect friction after that endpoint. Use elapsed monotonic time; preserve unrounded measured seconds for gates and selection. Capture safe wall-clock provenance separately. No preview, network or interruption time is silently removed.

## 16. P01-C14: Result normalization and interruption

The V0.1 required arm/trial fields and result vocabulary remain. A/B burden success means exact proof VERIFY=VALID over the owner's actual ACCEPT/AMEND/REJECT statement. L01 has the same predicate and must succeed for full eligibility. Record admission separately; cryptographic success must not be inferred from decision=ACCEPT or a client flag.

Executed failure has success=false and preserves measured times when available. NOT_REALIZABLE/unexecuted trials have success=false and times=null. Interrupted/incomplete trials have success=false, safe available measurements and null missing values. Required null or unsuccessful trials cannot qualify the arm. Missing measurements are never zero.

Normalize the raw result as an object with schema_version=2, protocol=R0-P01-V01, contract_revision=R0-P01-CONTRACT-V02, attempt_id, provenance, integrity, and arms keyed A/B/C. provenance binds the exact repository head, fixture/contract/harness artifact hashes and byte bases, and material runtime versions. integrity records secret exposure, result-affecting post-observation tuning and attempt-integrity failure. Any of these integrity failures requires primary classification INVALID; redaction cannot erase the fact of exposure.

Each arm contains all V0.1 required fields. arm_id is the exact fixture.arm_ids value. setup_receipt contains status, chronological setup events, public trust confirmation/material and safe capability/interruption observations. A resolved realizability uses only REALIZABLE or NOT_REALIZABLE; unresolved setup has realizability=null and setup status SETUP_INTERRUPTED or INCOMPLETE, never a fabricated NOT_REALIZABLE. Security controls map exactly the 13 keys to PASS/FAIL (A/B) or NOT_APPLICABLE (C), with separate per-control observations/evidence. Unexecuted A/B controls are FAIL with an unexecuted reason, not successful negative tests.

small_trials for A/B is exactly S01/S02/S03 in order; large_trial is L01. C has S01 and L01 only. Trial rows contain every V0.1 trial field; missing decision, rating or unavailable count is null, success is boolean, elapsed seconds are finite nonnegative numbers or null, counts are nonnegative integers or null, and notes are short non-secret strings. Include manual_metadata_edits, infrastructure receipts and safe failure/recovery observations. Arm manual_metadata_edits is the total of recorded owner metadata edits, with setup/control edits included; zero remains mandatory. security/burden records preserve envelope, exact statement/canonical bytes, displayed view, proof/public verification material and verifier result needed for independent checking. These are public proof records, not private-key material. Evidence encoding may vary only if exact bytes round-trip.

selection_eligible is derived, never accepted as an unverified input claim. A/B requires REALIZABLE, all 13 PASS, all 3 small successes, L01 success, every required V0.1 burden-trial field and measurement present and non-null (a supplied empty friction_note is permitted), friction ratings that are integers 1 through 5, small median <=60, each small <=120 unless its permitted receipt exempts that max check, L01 <=120, zero metadata edits and no secret exposure. C is always false. Proof viability remains REALIZABLE + controls 1-10 PASS + at least one authenticated small success + no secret exposure.

Preserve raw outcomes before scoring. The scorer adds classification/selection in a separate derived output rather than overwriting raw evidence. With intact attempt integrity, apply the unchanged rules: no viable A/B -> REOPEN; viable but none fully eligible -> AMEND; select eligible A/B by the existing 10-second small / 15-second large / B tie-break rule; volume breach -> AMEND, otherwise PASS_WITH_SELECTION. Incomplete/unavailable arms cannot claim viability or eligibility; keep their reasons visible. Inventory/source mismatch blocks classification pending prospective refreeze, never a silent substitute count or PASS. Malformed/conflicting result identity or provenance is an integrity defect, not an architectural failure measurement.

Do not subtract interruption time. The single-small-max exemption requires a task-owner receipt with exactly these mandatory fields:

```text
trial_id
start_utc
end_utc
affected_component
observable_event_or_error
classification = EXTERNAL_INFRASTRUCTURE_ONLY
task_owner_receipt = true
```

The receipt identifies the affected trial, observable infrastructure-only cause and interval; non-infrastructure causes cannot receive that classification. Missing/conflicting receipts do not exempt. Raw duration remains in the small median. The exemption never applies to L01 and never creates a retry. Measurement/report fields do not broaden Research 513's resumption permissions.

## 17. P01-C15: Legacy inventory byte basis

The corrected rule binds the Git blob at source_last_changing_commit=b9fba658e422279d8f8b8193b8c1bda88302dcda and source_git_blob_oid=56ecc1da7677a6be450b3b38beaa9266d6ffb8a8. source_byte_basis is GIT_BLOB_LF, source_bytes=119155 and source_sha256=2a3be898be6d7ac61d045a41492374d9fedb2ed3bf91734e4e07f0f20053355c.

The prior CRLF-worktree basis is preserved as SUPERSEDED_WORKTREE_CRLF_BASIS, 119279 bytes, SHA-256 71fd3b691afb245e294e6012d29bc0780fe4d671fe7a4d09ef6a44845d3e0630. Read the exact committed blob and independently recount; do not merely normalize a worktree file to evade mismatch. Source drift still requires prospective refreeze.

Counts remain 97 acceptances, 157 effects and distribution 1:62, 2:17, 3:11, 4:7. Baseline burden is 97 * selected median small seconds / 60 minutes. The >100 acceptance / >90 minute gates remain unchanged.

## 18. P01-C16: Conservative attempt boundary

This is ChatGPT's explicit refinement of Claude Message 013's setup wording. Attempt 001 starts immediately BEFORE the first real owner-sensitive P01 setup/credential action, whichever comes first: interactive Arm-A probe-key creation, WebAuthn registration, owner SSH signing, WebAuthn assertion, recovery signing or Arm C owner attestation.

No real setup observation may inform a repair before recognizing that the attempt has started. After start, no code, harness, fixture, threshold or control repair is permitted. Preserve raw setup/trial/control outcomes. The one predeclared unchanged WebAuthn setup repeat is not code repair; it grants no further retries. No retry-to-green. Harness defects require preservation, explicit INVALID classification and prospective refreeze.

## 19. Golden vector and unchanged gates

clarification_vectors_v02.json contains exact objects, canonical strings and the LF-terminated view for A/S01/ACCEPT. Expected digests:

```text
ordinary semantic base 76a7391fafd9683566f011be522dd4c3bfbe6bcfb0f1963500d1776b77b4d7a6
envelope              b4a274d82c6bc22b8c6168c2fdd7ee8b0b5dea8f6140907960022eb0fd6dc71c
shown                 e55af5a611651ca0efaae4aba2a013df9b9c87cbe8e61f147a612cd94f7e6d1d
statement             66b397b12d23d83b475e15e143272f68be7bd655d8432ff170de6985e87ade46
```

A mismatch stops execution; expected values are not changed to fit output. These vectors contain no credential or trial evidence.

Retain A OPENSSH_ED25519_PASSPHRASE_V01, B LOCALHOST_WEBAUTHN_ES256_UV_V01 and C CHATGPT_OWNER_USER_ROLE_DIGEST_ATTESTATION_V01; all 13 controls and the zero-miss gate; 1/2/4/30 effects; small median <=60 seconds, individual small <=120 with only the stated infrastructure exception, successful L01 <=120; zero manual metadata edits; no secret exposure; the proof-viability distinction; the A/B selection rule; and both volume gates. R0-P02 remains PASS. No physical target, production credential, migration, Runtime Bridge extraction, Specification 028 amendment or authority switch is selected or authorized.
