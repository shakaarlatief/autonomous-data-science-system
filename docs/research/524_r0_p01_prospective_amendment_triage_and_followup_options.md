# Research 524: R0-P01 prospective AMEND triage and follow-up options

**Date:** 2026-10-10
**Status:** PROSPECTIVE TRIAGE / INDEPENDENT CRITIQUE NEXT / NOT A TRIAL FREEZE
**Scope:** Distinguish owner-input friction, measured timing, interrupted WebAuthn setup and actual cryptographic architecture failure, then compare defensible post-result options without changing the executed probe.
**Parent:** Research 523 / Validation 215 / Checkpoint 859 / MC-0030 Message 016
**Probe:** R0-P01 owner authenticity and acceptance burden
**Candidate:** GOVERNED_LEDGER_KERNEL_V02, still unselected
**Authority:** Research recommendation only; no new credential setup, no new trial, no revision of Attempt 001, no physical-target selection, production implementation, migration, Specification 028 amendment, Runtime Bridge extraction, or authority switch.
**Interaction:** ChatGPT / chatgpt-37; the human remains the only owner-credential operator.

## 1. Immutable observed basis

Attempt 001 is permanently consumed and backed up. The unchanged frozen score on original public evidence, run under a verifier execution profile permitting **temporary public verification files**, returned `AMEND / VIABLE_PROOF_WITHOUT_FULL_ELIGIBILITY`. It did not pass all selection gates and did not falsify owner-exclusive exact-statement cryptography.

| Observed fact | Supported inference | Unsupported leap |
|---|---|---|
| Arm A: 12/13 security controls PASS, P0 and P5 VALID | Exact-statement signing and many rejection/rotation controls worked | Full selection eligibility |
| Arm A P6 INVALID; native OpenSSH incorrect passphrase; owner recalls using primary passphrase | Credential choice is a plausible human/operator cause; incorrect passphrase was rejected | Recovery credential was proven usable or original failure is now PASS |
| S01/S02/S03/L01 all recorded successful cryptographic proofs | Primary signing was operationally realizable | Every latency gate passed |
| S02 mechanical 130.8491039001383 seconds; no recorded external-infrastructure interruption | Individual-small 120-second gate failed | Permission to subtract chat, screenshot, thinking or unknown delay |
| Small median 5.868030599784106 seconds, L01 5.499281600117683 seconds | Routine signing generally fast in this trial | Real consequential semantic comprehension proved |
| B registration interrupted at localhost handoff; C not executed | B and C unqualified | B incapable or C adequate |
| P0 friction 2/5 and owner requests contextual justification/history/consequences | Owner UI has an explanatory-context requirement | Signed-view implementation can ignore provenance |

Initial independent scorer INVALID in Runtime Bridge `readOnly` was a verifier environment false negative: Python `tempfile.TemporaryDirectory` for public SSH proof checking could not operate in that sandbox. Unchanged evidence/scorer under the authorized temporary-file-capable `:workspace` profile returned AMEND. Validation 215 preserves this diagnostic; it is not a second owner trial.

## 2. Triage by cause and consequence

**Recovery passphrase.** The owner regards entering the first passphrase instead of the second as a small mistake. The OpenSSH prompt is generic, and the harness's immediate instruction merely says to use the native prompt. A simple explicit role cue before recovery signing is proportionate: `RECOVERY authorization: use the separate recovery-key passphrase created during setup, not the primary-key passphrase.` No relaxation of different primary/recovery keys, role enforcement, no-agent policy, verification, admission or 13-control zero-miss gate. The exact location of the cue relative to hashed owner-view bytes must be prospectively specified, so it cannot silently redefine sign-what-you-see.

**S02 burden.** The original 130.849 seconds remains a true measured failure, regardless of why it happened. Pretrial neutral instructions may explain when mechanical timing begins and that seeking advice after submitting a decision does not pause it. The original thresholds stay exactly median small <=60 seconds, each small <=120 seconds without a qualifying external-infrastructure exception, L01 <=120 seconds, three small successful, and zero manual metadata edits. Never invent an exception or remove observed elapsed time.

**Localhost/terminal interruption.** Ctrl+C in a running PowerShell terminal interrupts the foreground harness. Future instructions should explain using the browser address bar, VS Code link activation if available, or an equivalent noninterrupting way to open `http://localhost:8765`. Any actual WebAuthn registration, challenge, UV ceremony or assertion belongs inside the properly claimed new trial, not an unrecorded readiness test.

**Owner explanation and comprehension.** Generic synthetic effects test signing burden, not whether a person understands genuine irreversible decisions. Future owner reviews need accessible purpose, source/provenance, prior discussion and acceptance history, alternatives, dependencies and possible consequences. Explanatory content must be visibly distinguished from authoritative payload, and any required governing decision facts must be bound to the exact signed view. This is a separate owner-interface and comprehension workstream, not evidence that current SSH cryptography failed. A meaningful comprehension study requires its own preregistered tasks and metrics.

**Independent verification environment.** Successor scorer preflight must validate the ability to create transient **public** verifier files without reading/sending any owner's private key or invoking private signing. A sandbox-induced re-verification failure cannot be classified as credential failure without separating environment from evidence.

## 3. Alternatives and decision

| Alternative | Disposition | Reason |
|---|---|---|
| Retroactively declare PASS from successful controls/low median | REJECT | Violates recovery, S02 and completeness gates |
| Re-run only P6 and S02 to graft successes onto Attempt 001 | REJECT | Selective retry-to-green and incompatible evidential identity |
| REOPEN the entire cryptographic architecture because of the wrong passphrase | REJECT | Unsupported by successful exact-proof trials and owner's assessment |
| Keep P01 at AMEND and do reversible P03 research, deferring owner work | CONDITIONAL FALLBACK | Preserves evidence but leaves physical owner-authenticity selection unresolved |
| Design a separate, complete, properly frozen successor qualification with small operator-UX changes | **PREFERRED PROSPECTIVE CANDIDATE** | Can close security/timing/WebAuthn gaps without rewriting or cherry-picking Attempt 001 |

The preferred option is NOT yet authorized. Learning from Attempt 001 is unavoidable in a repeated human trial. Record this known repeated-participant effect, disclose it in any new result, and never claim independent first-exposure generalizability. A separately frozen successor can still test whether the revised workflow is operationally feasible.

## 4. Constraints on a possible successor

1. Freeze a distinct protocol revision, attempt identity, acceptance-ID namespace, immutable exclusive start marker, evidence directory, and source/scorer hashes. Attempt 001 marker, 25 snapshots, backup and key material are historical only. No reset, overwrite, marker deletion or silent continuation.
2. Choose and document **fresh vs reused probe credentials** before owner setup. Fresh isolated keys offer clear independent setup, but setup burden, owner safety and comparability must be weighed. No credential operation is authorized by this document.
3. Retain exact owner-authenticated SignedAcceptanceStatement semantics, sign-what-you-see and semantic-base binding, role-scoped VERIFY/ADMIT, all 13 frozen security controls (including recovery and negative controls), 1/2/4/30-effect burden tests, A SSH, B WebAuthn ES256+UV, and C weaker ineligible comparison. Any changed view or renderer must receive fresh prospective hashes and independent pretrial tests.
4. Provide a short, neutral procedure orientation **before** scored interactions, distinguishing synthetic effects, owner decision vs proof, primary/recovery passphrases, timer start/stop, honest friction measurements, external-only interruption receipts, and safe localhost opening. No coaching on which semantic decision or friction rating to provide.
5. Do not change median or maximum time limits, the no-metadata-edit gate, the secret boundary, or zero security misses. No suspension of clocks for chat/help without a separately preregistered measured design that is not compared dishonestly to the original.
6. Browser reachability may be checked with an entirely non-credential synthetic readiness test before starting; real WebAuthn registration/assertion may not be tried or tuned before the new claim. If ES256+UV or exact digest binding is unavailable, preserve the proper availability classification.
7. Do not pool/replace successful records from Attempt 001 with successor records. Evaluate any successor under its full independently predeclared denominator and scorer, preserving both original AMEND and successor outcome side by side.
8. Keep real-decision explanatory-context qualification independent from synthetic signing time. Design and test it separately if architectural selection genuinely depends on it; do not silently promote an unsigned context panel to authority.
9. Require bounded independent adversarial review of this triage, a prospective exact fixture/implementation contract and new attempt boundary, independent qualification before owner-sensitive setup, and an explicit future owner decision to execute. None has occurred.

## 5. Questions for independent adversarial reviewer

Assess whether full independent successor testing is proportionate or whether narrower *separately classified* diagnostics plus eventual P03 research are better. Challenge learning effect, key reuse versus fresh setup, signed-view vs non-governing operator guidance, the risk that synthetic browser preflight secretly consumes a real credential event, and truthful handling of S02. Confirm whether any genuine architectural amendment is justified by these observations. Return a clearly reasoned `ACCEPT_PROSPECTIVE_DIRECTION`, `AMEND_PROSPECTIVE_DIRECTION` or `REOPEN_ARCHITECTURE_QUESTION`. The reviewer may critique but must not execute credentials, modify the original evidence, or authorize a new trial.

R0-P02 remains PASS; R0-P03 pending. GOVERNED_LEDGER_KERNEL_V02 remains a leading but unselected physical realization. Selected THIN_CENTRED_HYBRID_V03 logic and Specification 028 authority remain unchanged; latest unrelated scientific experiment remains INCOMPLETE.

```text
RESEARCH_524=PROSPECTIVE_TRIAGE_COMPLETE
R0_P01_ATTEMPT_001=AMEND_AND_IMMUTABLE
FOLLOWUP_CANDIDATE=FULL_SEPARATE_QUALIFICATION
FOLLOWUP_PROTOCOL_FREEZE=NOT_AUTHORIZED
NEXT=INDEPENDENT_TRIAGE_CRITIQUE
```
