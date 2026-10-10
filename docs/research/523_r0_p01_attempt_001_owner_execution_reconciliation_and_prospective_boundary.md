# Research 523: R0-P01 Attempt 001 owner execution, AMEND reconciliation, and prospective boundary

**Date:** 2026-10-10
**Status:** OWNER ATTEMPT 001 PRESERVED / FROZEN SCORER AMEND / PROSPECTIVE TRIAGE NEXT
**Parent:** Research 522 / Validation 214 / Checkpoint 858 / MC-0030 Message 015
**Probe:** R0-P01, contract R0-P01-CONTRACT-V02
**Scope:** Preserve the executed owner Attempt 001, exact immutable evidence, independent frozen scoring, owner feedback, and prospective R0-P01 AMEND boundary.
**Candidate:** GOVERNED_LEDGER_KERNEL_V02, not selected as physical target
**Authority:** Interpretation of completed owner observations only. No result-guided retroactive modification, re-execution, new attempt authorization, physical-target selection, production implementation, migration, Runtime Bridge extraction, Specification 028 amendment, or authority switch.
**Interaction:** ChatGPT / chatgpt-37; owner-sensitive credential interactions performed solely by the human at native local prompts.

## 1. Evidence and immutable attempt boundary

Attempt 001 began on 2026-10-10 under the committed, reviewed freeze HEAD `89736b2515fa80f1c21be3350e112663e1e58a92` on `v1-source-vault-bootstrap-resume`. The implementation identities remain those frozen in Research 522 / Validation 214. The production create-only marker at `%LOCALAPPDATA%\ADS-R0-P01\attempt-001.started.json` was present after the interruption. The public evidence directory `%LOCALAPPDATA%\ADS-R0-P01-Owner-Evidence-001` held 25 append-only snapshots, `raw-0000.json` through `raw-0024.json`, and the marker recorded the claim.

Final raw file exact-byte SHA-256:
`a48e066adea499eb17e4d6240cb459df315b91f444fdee4f42ab880bdcc60296`.

Frozen scorer canonical-object digest (`raw_sha256`, a different byte basis from the raw file):
`7b92c9c743d14384847ec75e1da814043cda13ed593faca4c07db5e843b44faf`.

The owner created an independent, hash-verified backup of the 25 snapshots and marker at `%LOCALAPPDATA%\ADS-R0-P01-Evidence-Backup-20261010-081030`. Every copied snapshot hash matched the original, the marker matched, JSON parsing succeeded for all snapshots, and numbering was contiguous. ChatGPT later independently confirmed the final original and backup raw-file hashes via Codexless Runtime Bridge. Do not include raw files, credential material, private key paths, or passphrases in the repository. These local locations are evidence references, not repository content.

The final snapshot includes `ATTEMPT_001_STARTED_BEFORE_OWNER_SENSITIVE_SETUP` and `OWNER_RUN_INTERRUPTED`, with `attempt_integrity_failure=false`, `post_observation_tuning=false`, and `secret_exposure=false`. These are recorded flags; no inference of broader absence beyond the checked record is made. The final event was preserved by the harness exception path. The owner pressed Ctrl+C in a running PowerShell terminal while trying to copy the displayed localhost address, which interrupted execution after the Arm-A phase and before WebAuthn registration. Ctrl+C is a human workflow interruption here, not an invented external infrastructure exemption.

## 2. Frozen scoring result

Execute the unchanged `experiments/r0_p01_owner_acceptance_v01/score.py` against `raw-0024.json`, with `python -B` and an authorized runtime allowing temporary public verification files. Independent full cryptographic reverification completed with:

```text
R0_P01_ATTEMPT_001_CLASSIFICATION=AMEND
REASON=VIABLE_PROOF_WITHOUT_FULL_ELIGIBILITY
SELECTED_ARM=null
A_PROOF_VIABLE=true
A_SELECTION_ELIGIBLE=false
A_REALIZABILITY=REALIZABLE
B_PROOF_VIABLE=false
B_REALIZABILITY=null
B_SETUP=SETUP_INTERRUPTED
C_PROOF_VIABLE=false
C_REALIZABILITY=null
C_SETUP=SETUP_INTERRUPTED
```

Arm C is a weaker platform-attestation comparator, not an eligible cryptographic mechanism even if completed. The current classification is a failed full-selection gate, not a declaration that exact-statement cryptography itself is impossible.

An initial independent `score.py` call in the Runtime Bridge `readOnly` command profile returned `INVALID / RESULT_IDENTITY_PROVENANCE_OR_EVIDENCE_DEFECT`, because SSH public-proof verification uses `tempfile.TemporaryDirectory`; that command profile could not create temporary files. An isolated Python probe confirmed `FileNotFoundError: No usable temporary directory`. Independent re-verification of all previously VALID SSH proofs returned false in this unsuitable sandbox. Re-running the *same unchanged scorer and evidence* using the authorized `inherit` / `:workspace` profile, where temporary public verifier files are permitted, returned the valid `AMEND` result above. The read-only-sandbox artifact is a diagnostic caveat, not an observed original-owner failure or an authorization to change the scorer.

## 3. Arm A findings

Twelve of thirteen frozen security controls are PASS. The sole failure is `RECOVERY_CREDENTIAL_DRY_RUN=FAIL`. P0 and ordinary rotation P5 were signed and marked VALID; the P6 recovery record was marked INVALID. Every other security control, including forgery/mutation, replay, semantic-base, signer-set, ordinary rotation, and compromise-boundary checks, passed.

The owner subsequently explained that at P6 they continued entering the *primary* key passphrase, not the distinct *recovery* key passphrase created at initial setup. This is an owner-reported explanation strongly consistent with the observed native OpenSSH `incorrect passphrase supplied to decrypt private key` error. It is not independent proof of the precise keystrokes and does not convert FAIL to PASS. OpenSSH correctly rejected the input. The owner regards the mistake as minor and does not request a substantial architecture or security-policy redesign. The current harness prints `Use the native OpenSSH prompt; the harness does not receive your passphrase.` and the native prompt is generic; it does not issue an explicit immediate `RECOVERY passphrase, not PRIMARY` instruction. A short purpose label is a candidate prospective presentation-only improvement, not a proof of an architectural defect.

The completed burden trials all recorded ACCEPT, zero manual metadata edits, zero physical device switches, and two user-visible interactions each. Their observed mechanical times are:

| Trial | Effects | Mechanical seconds | Observed proof | Friction |
|---|---:|---:|---|---:|
| S01 | 1 | 5.1785007999 | valid / completed | 1/5 |
| S02 | 2 | 130.8491039001 | valid / completed | 1/5 |
| S03 | 4 | 5.8680305998 | valid / completed | 1/5 |
| L01 | 30 | 5.4992816001 | valid / completed | 1/5 |

The three-small-trial median was 5.8680305998 seconds. S02 exceeded the frozen 120-second individual gate; no infrastructure-only interruption receipt was recorded for that trial. Do **not** subtract any elapsed time retrospectively, assign a cause the trace does not prove, or reclassify owner/model discussion as an external infrastructure exception. The 30-effect L01 mechanical signing duration was within its 120-second gate, but fast signing of generic synthetic effects does not establish meaningful review of real consequential content. The original security baseline P0 received owner friction rating 2/5 and a non-secret contextual-feedback note; P5/P6 ratings were 1/5. The owner reported that a future genuine authorization view should explain context, history, why the decision is needed, and consequences. That is a useful owner-experience requirement, not permission to rewrite the frozen view.

## 4. Interrupted B and C arms

Arm B displayed the localhost WebAuthn setup instruction but did not complete registration: `SETUP_INTERRUPTED` and `realizability=null`. Arm C was not reached: `SETUP_INTERRUPTED` and `realizability=null`. Therefore neither WebAuthn viability nor the comparator's user-role provenance behavior can be inferred from Attempt 001.

The PowerShell Ctrl+C during localhost-address copying ended the owner-run process. Its exact temporal order and the recovery-signing failure are separately preserved. This does not authorize an unchanged second attempt.

## 5. Decision and prospective boundary

**Dispositions:** Preserve the original scorer result `AMEND`; retain the broad owner-exclusive exact-statement cryptographic architecture as *not falsified* by Attempt 001; do not grant full P01 PASS_WITH_SELECTION; do not treat the human passphrase mistake as a major architectural failure; keep security recovery test and every timing gate intact for the original result.

The smallest candidate prospective ergonomic adjustment is a clearly printed role-specific recovery-key instruction immediately before the native OpenSSH prompt. This is not a retroactive correction or a reason to weaken cryptographic controls. Separately, review whether the broader acceptance context and measurement logistics require a *prospectively defined* follow-on protocol, particularly genuine high-consequence review and interactions while a mechanical timer is running. Assess whether a new bounded experiment is necessary and what its exact attempt identity, owner role, fixtures, controls, thresholds, blindness, interruption policy and scorer would be. Do not assume a new attempt or reset a marker.

A future governed AMEND/refreeze decision should distinguish:
1. presentation and instruction clarifications from changes to authentication and authority;
2. validity of cryptographic proof from actual owner comprehension and decision quality;
3. recorded mechanical time from non-qualifying interruptions;
4. evidence that the underlying architecture survives from the still-missing full Arm-A/Arm-B selection qualification;
5. small scoped improvements from unnecessary architecture redesign.

R0-P02 remains PASS; R0-P03 remains pending. GOVERNED_LEDGER_KERNEL_V02 is retained only as a leading candidate, not selected. Specification 028 and the unrelated scientific-experiment `INCOMPLETE` routing remain unchanged. No production implementation, migration, extraction, cutover, or authority switch is authorized.

```text
RESEARCH_523=R0_P01_ATTEMPT_001_RECONCILED
ATTEMPT_001=PERMANENTLY_CONSUMED_AND_PRESERVED
R0_P01_RESULT=AMEND
NEXT=PROSPECTIVE_R0_P01_AMEND_TRIAGE
```
