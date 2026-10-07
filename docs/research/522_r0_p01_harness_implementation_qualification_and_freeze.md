# Research 522: R0-P01 harness implementation qualification and freeze

**Date:** 2026-10-07
**Status:** ACCEPT_AFTER_BOUNDED_REPAIR / HARNESS QUALIFIED AND FROZEN / OWNER EXECUTION NEXT
**Parent:** Research 521 / Checkpoint 857 / MC-0030 Message 014
**Candidate:** GOVERNED_LEDGER_KERNEL_V02
**Probe:** R0-P01
**Scope:** Preserve the independent implementation review, bounded Attempt-001 durability repair, exact qualified implementation identities and pretrial evidence, and route to owner-execution readiness.
**Authority:** Probe implementation qualification only. No owner execution or P01 result; no physical-target selection, production implementation, migration, Runtime Bridge extraction, Specification 028 amendment or authority switch.
**Companion collaboration thread:** MC-0030
**Interaction environment:** ChatGPT
**Interaction session:** chatgpt-37
**Conversation title:** 37 - Project System Realization Architecture and Qualification
**Primary collaborator:** ChatGPT

## 1. Prospective contract and implementation history

Research 521 / Checkpoint 857 / Message 014 froze the P01 V0.2 implementation contract before any owner use. The V0.2 addendum and normative clarification vectors prospectively resolve the earlier implementability audit; historical V0.1 evidence remains unchanged. AC-1 through AC-6 and P01-C01 through P01-C16 are not reinterpreted by this implementation freeze.

Codex implemented exactly harness.py, webauthn_server.mjs and score.py under experiments/r0_p01_owner_acceptance_v01/. ChatGPT / chatgpt-37 independently inspected the actual working-tree implementation and performed adversarial pretrial qualification. The first review found one bounded implementation defect: interruption at the first SSH key-generation prompt could leave Attempt 001 started in evidence directory A without a key file, allowing a fresh process with evidence directory B to start another Attempt 001.

This violated the already-frozen P01-C16 attempt boundary. It was an implementation defect, not an architecture or contract defect. No owner execution had begun and no P01 result had been observed, so a bounded pretrial repair was legitimate. Codex repaired only harness.py; score.py, webauthn_server.mjs and the frozen contracts were unchanged. ChatGPT independently inspected and requalified the repair with disposition ACCEPT_AFTER_BOUNDED_REPAIR.

## 2. Durable Attempt-001 boundary

The production claim is the non-secret marker:

```text
%LOCALAPPDATA%\ADS-R0-P01\attempt-001.started.json
```

Creation is atomic/create-only through exclusive file creation. The public record binds attempt_id, protocol, contract revision, reviewed repository HEAD, evidence directory and UTC claim time. The marker is flushed and fsynced before the first raw start snapshot and before any owner-sensitive operation. It is never overwritten or automatically removed; there is no reset, force or retry flag. An existing or partial marker fails closed even in a fresh process, with a different evidence directory and no SSH key files. A filesystem failure after the claim may conservatively consume the attempt.

The order is validated preflight/reviewed freeze/paths, evidence-directory establishment, durable claim, preservation of ATTEMPT_001_STARTED_BEFORE_OWNER_SENSITIVE_SETUP, then owner setup. First raw evidence still precedes the first real owner-sensitive action. After attempt start, no result-guided implementation repair or retry-to-green is permitted. The single frozen unchanged interrupted WebAuthn registration repeat remains within the already-started attempt and grants no broader retry authority. A legitimate future new attempt requires prospective governed refreeze.

Synthetic claim tests use temporary test-only locations, never the production marker. They establish first-claim persistence, second-claim rejection, different-evidence-directory rejection, fresh-process rejection without SSH files, non-secret contents, partial-marker rejection and a production-marker guard for normal --selftest.

## 3. Exact qualified implementation identities

Starting authoritative HEAD and origin/v1-source-vault-bootstrap-resume were synchronized at fb19c4f9deebf1b667d64f2e4f82c68569ab2daf on branch v1-source-vault-bootstrap-resume. These are exact working-tree file bytes, not a claim that the implementation was already committed at that HEAD.

| File under experiments/r0_p01_owner_acceptance_v01/ | Bytes | SHA-256 |
|---|---:|---|
| harness.py | 64666 | 0aede5baccaf88e176b3f6c53d69135953405c9f22416e23b017cbd1eb272846 |
| webauthn_server.mjs | 32608 | 6ca17d7da0dbf65938ea7d9f98432ca200ca6233896f3895f10649a9bdc4edd8 |
| score.py | 24078 | 9817febe60db6d68e3dd3887d0dbd2e5573fa398ef2398cd39ceccea7696509c |

The final implementation is qualified/frozen at these identities. This documentation task does not modify those files or create a repository commit. Owner execution must use the committed reviewed implementation; publication remains a separate governed step.

## 4. Independent final pretrial qualification

Validation 214 records ChatGPT's independent final qualification. The owner supplied that independent review for Codex materialization; it is not owner-trial evidence.

```text
SECOND_ATTEMPT_001_START_ALLOWED=false
PRODUCTION_ATTEMPT_001_MARKER_EXISTS=false
PRIMARY_PRIVATE_EXISTS=false
RECOVERY_PRIVATE_EXISTS=false
```

harness.py --selftest: PASS, including all four golden vectors; controls 1-13 for synthetic A/B; decision consumption; stale-base and role enforcement; historical trust; secret redaction; Arm C construction; embedded synthetic WebAuthn qualification; durable Attempt-001 claim; fresh-process second-claim rejection; partial-marker rejection; and production marker guard.

webauthn_server.mjs --selftest: PASS, including golden PASS; synthetic ES256 assertion PASS; 9 statement mutations; 14 structural negatives; counter policy; registration binding; single-use state; expiry; predeclared registration-repeat behavior; and defect retry prohibition.

score.py --selftest: PASS, including normalization; raw immutability; integrity/provenance; INVALID / REOPEN / AMEND / PASS_WITH_SELECTION; A/B selection thresholds/ties; large-trial and missing-measurement gates; infrastructure exception behavior; volume gates; C ineligibility; complete public-evidence reverification; and rejection of synthetic evidence masquerading as owner evidence.

The golden hashes remain exactly:

```text
semantic base 76a7391fafd9683566f011be522dd4c3bfbe6bcfb0f1963500d1776b77b4d7a6
envelope      b4a274d82c6bc22b8c6168c2fdd7ee8b0b5dea8f6140907960022eb0fd6dc71c
shown         e55af5a611651ca0efaae4aba2a013df9b9c87cbe8e61f147a612cd94f7e6d1d
statement     66b397b12d23d83b475e15e143272f68be7bd655d8432ff170de6985e87ade46
```

Inventory remains 119155 Git-blob bytes, 97 acceptances and 157 effects, with effects-per-acceptance distribution 1->62 / 2->17 / 3->11 / 4->7. Its source blob is 56ecc1da7677a6be450b3b38beaa9266d6ffb8a8, SHA-256 2a3be898be6d7ac61d045a41492374d9fedb2ed3bf91734e4e07f0f20053355c. Repository validation is PUBLIC_REPOSITORY_INTEGRITY=PASS.

## 5. Live boundary and next action

Checkpoint 858 / Research 522 / Validation 214 / MC-0030 Message 015 close harness implementation, independent pretrial adversarial review and the bounded durability repair. Live routing is checkpoint 858 / p-one-owner-execution-ready; MC-0030 phase is R0_P01_OWNER_EXECUTION_READY and next_expected_actor is chatgpt / chatgpt-37.

Attempt 001 remains NOT STARTED. No production marker, real Arm-A owner probe key or real owner-sensitive setup exists. No WebAuthn registration/assertion, owner SSH/recovery signing or Arm C attestation occurred, and no owner result was observed. Synthetic pretrial proofs do not establish owner realizability or a P01 result.

Next is ChatGPT-orchestrated owner execution under the committed reviewed implementation. The first real owner-sensitive action will be preceded by the durable Attempt-001 claim and preserved start snapshot. This task does not begin that execution.

R0-P02 remains PASS; R0-P03 remains pending; no physical target is selected. GOVERNED_LEDGER_KERNEL_V02 remains retained. Specification 028 remains authoritative and latest_experiment_outcome remains INCOMPLETE. Production implementation, migration, Runtime Bridge extraction and authority switch remain unauthorized.

```text
R0_P01_HARNESS_PRETRIAL_QUALIFICATION=PASS
R0_P01_HARNESS=QUALIFIED_FROZEN
DISPOSITION=ACCEPT_AFTER_BOUNDED_REPAIR
ATTEMPT_001=NOT_STARTED
OWNER_RESULT=NOT_OBSERVED
NEXT=R0_P01_OWNER_EXECUTION
```
