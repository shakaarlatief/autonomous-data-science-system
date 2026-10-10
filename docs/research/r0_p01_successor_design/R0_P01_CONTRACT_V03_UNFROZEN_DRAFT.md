# R0-P01 Prospective Successor Contract V03: UNFROZEN DRAFT

**Date:** 2026-10-10
**Status:** REVISED UNFROZEN DRAFT 02 / MESSAGE 021 RECONCILED / NOT EXECUTABLE / NOT FROZEN
**Scope:** Candidate complete, separately identifiable owner-authenticity qualification, after preserved Attempt 001 AMEND. No sensitive operation or new experiment is authorized.
**Provisional identities:** Protocol R0-P01-V01-I1 (REQUIRES family-level approval); contract R0-P01-CONTRACT-V03; Attempt 002. No final protocol identity has been frozen.
**Parent:** Research 513, Research 518, Research 521, Research 525, Validation 216 and MC-0030 Message 019.
**Authority:** Research-only proposed contract. None of the V01/V02 contracts, Attempt 001 observations or scorer rules are retroactively amended.

## 1. Non-negotiable experiment family invariants

Research 513 continues to govern all 13 negative/positive controls and the zero-miss criterion; arms A SSH Ed25519, B localhost ES256 WebAuthn with UV, and C weaker non-cryptographic chat-role comparator; three small trials with 1, 2 and 4 effects, one large with 30 effects; independent owner decision and detached proof; cryptographic VERIFY distinct from semantic ADMIT; history and role enforcement; no proof/identity pooling; and zero manual metadata edits or secret exposure.

Frozen burden thresholds: median small signing mechanical time <=60 seconds, each small <=120 seconds except a contemporaneously qualified infrastructure-only receipt as defined by V02, and large <=120 seconds without exception. Trial decision/preview ordering, inventory estimate (97 acceptances, 157 effects, counts by effects 1:62, 2:17, 3:11, 4:7), projected acceptance limit 100, projected mechanical minutes 90, A/B selection differences of 10 s (median small), then 15 s (large), then B tie-break remain unchanged. No owner-view coaching for ACCEPT, AMEND, REJECT or self-rated friction.

This document **does not** authorize Attempt 002. The original started Attempt 001 remains irrevocably AMEND, with recovery FAIL, S02 130.8491039001383 seconds, incomplete B/C, and old marker/raw/backups/keys unchanged. Post-result changes are declared as result-informed, prospectively tested and independently reviewed. GOVERNED_LEDGER_KERNEL_V02 is still unselected as physical target; R0-P02 PASS and R0-P03 pending; Specification 028 and unrelated INCOMPLETE scientific outcome unchanged.

## 2. Proposed irreversible identity and predecessor relationship

1. The intended successor is still only a draft. Proposed **protocol identity** is R0-P01-V01-I1 (I1 means a prospective Research-513-family interpretation); this identity is conditional on explicit independent approval of the G1/G2 incomplete-evidence interpretation. Contract revision remains R0-P01-CONTRACT-V03 and the proposed new claim is Attempt 002. If I1 is rejected, the reviewer must choose the final exact protocol identity and classification policy *before freeze*. R0-P01-V02 is removed to avoid confusing the protocol with historical V02 contract files.
2. After independent fixture/implementation qualification and a separate explicit owner execution decision, one owner-local, exclusively created start marker would claim Attempt 002 **before** first real owner-sensitive action. It binds exact protocol ID, contract, fixture, harness and scorer hashes, platform/provenance, prior claim hash, prior public snapshot hash and owner authorization reference. No marker is created by this draft. Attempt 001 remains irreversibly consumed.
3. Verified historical exact raw-0024.json SHA-256: `a48e066adea499eb17e4d6240cb459df315b91f444fdee4f42ab880bddc60296`. Independently checked Attempt 001 marker exact-file SHA-256: `864f4b1a7be30e312abd5dcdb9359090dd8aa8ddbfa321e823261d63c9971281`. Machine-recompute before final freeze; never use transcribed strings alone as evidence. Their exact-byte basis differs from frozen scorer canonical-object SHA-256.
4. Fresh owner-protected PRIMARY and RECOVERY SSH Ed25519 keys would be generated only after claim via native interactive OpenSSH with nonempty passphrases, outside repository and agent, under a new attempt-local directory. The new public IDs must differ from one another and all old Attempt 001 public signer IDs in a local nonsecret comparison. Do not read old private keys or publish personally linkable fingerprints in the public repository.
5. Arm B uses an attempt-specific new WebAuthn registration under the same localhost RP and **the new Arm-A RECOVERY key as its P6 recovery member**. If Arm A key setup never generated that key, B's P6 security control is FAIL/unexecuted (missing recovery member), never silently skipped or substituted with the old Attempt 001 key.
6. Preserve the nine existing SignedAcceptanceStatement fields: `context`, `project_id`, `acceptance_id`, `envelope_digest`, `shown_digest`, `decision`, `semantic_base_digest`, `signer_set_version`, `issued_at`. Proposed context is `ADS-R0-P01-002-OWNER-ACCEPTANCE-V01` and acceptance prefix `R0-P01-002-`. Fixed context, synthetic project ID and arm/item-specific acceptance-ID grammar are mandatory **VERIFY-side structural checks**, before cryptographic verification. Reject any other context, project or prefix even if someone signs it using a valid fresh key.
7. Do **not** attempt exhaustive preregistration of future statements containing real owner public keys: P5 and P6 trust-root rotation effects depend on unknown keys created only after claim. Freeze full golden vectors for key-independent cases and **synthetic-key-instantiated** P0/P5/P6 trust-case vectors plus canonical templates with explicit public-member slots. Check exact runtime instantiated bytes under the frozen template. At signing time locally compare actual new canonical statement SHA-256 with the public old-proof statement digest set; refuse matches. Derive the old digest set mechanically from preserved nonsecret Attempt 001 observations; commit a sorted-set count/hash and source description, not privately linkable identities. This comparison is defense in depth; primary replay protection is exact successor context/project/prefix enforcement plus new keys.
8. New public evidence directory and start marker are exclusive-create and separate from the repository and all Attempt 001 directories; no owner-sensitive operation occurs during drafting or review. Evidence cannot imply a trusted cryptographic key-creation time: chronology is **harness-observed keygen after recorded claim**, supported by append-only host-local receipts rather than any timestamp guarantee embedded in an SSHSIG.

## 3. Three-tier presentation and exact digest semantics

- **T1 governing payload:** The semantic envelope is canonicalized to produce `envelope_digest`. The separately rendered **owner-view bytes** are bound by `shown_digest`. The envelope digest does **not** hash a rendered view. Changes to T1 envelope content necessarily affect rendered view and the signed statement as prescribed by AC-1.
- **T2 non-authoritative decision context:** future explanations, provenance, dependencies, history, options and consequences can be visibly displayed and covered by `shown_digest` only. They must not silently enter the semantic envelope. The synthetic successor does **not** introduce variable T2 content or claim to test real consequential comprehension. Future R1 owner-view context and rare recovery-key durability remain requirements.
- **T3 procedural chrome:** frozen role-specific credential instructions, timing guidance, safe browser navigation, and nonsecret friction prompts appear **outside** the exact owner-view delimiters and outside `envelope_digest` and `shown_digest`. The prospective qualified contract/harness pins their static byte table and emits it identically for the designated event role. No agent-generated dynamic coaching and no owner decision suggestion.

Before a new owner trial, independently freeze exact UTF-8 renderer bytes, whitespace/LF, delimiters, canonical statement encoder, T3 table hashes and golden vectors. The canonical statement preview follows decision capture inside mechanical timing; the owner independently chooses ACCEPT/AMEND/REJECT.

Candidate T3 wording, subject to byte-level qualification:

```text
These proposals are synthetic; choose the decision you actually intend.
You may request explanations before submitting your decision.
Mechanical timing begins when you submit a decision and includes statement preview,
credential input, possible owner-selected retry and deterministic verification.
PRIMARY authorization uses this attempt's PRIMARY-key passphrase.
RECOVERY authorization uses this attempt's separate RECOVERY-key passphrase.
The localhost page opens automatically after server readiness. If it does not,
type the printed address into your browser while leaving this terminal running.
Pressing Ctrl+C in this window stops the attempt.
A stopped claimed attempt is still preserved and receives a scored result.
Never share private keys, passphrases or authenticator secrets with any model.
```

For an owner-selected SSH retry under section 4, the fixed T3 text is:

```text
No signature was produced for this statement.
Type R to retry this same statement (attempts left: N), or S to stop this event.
```

N is the deterministic nonsecret count of remaining invocations (not model-generated). S or any unrecognized response stops the proof event without another subprocess. This is a prospective UX requirement and must not change the governing bytes or the timer.

## 4. Single owner proof event with owner-confirmed bounded SSH re-invocation

The prospective SSH policy uses at most **three native signing subprocess invocations** under one immutable captured owner decision, canonical statement, statement file, key role, acceptance ID, shown-view digest, semantic base and monotonic timer. It replaces the earlier unimplementable wrong-passphrase error classifier. It is expressly a `RESULT_INFORMED_PROSPECTIVE_CHANGE` after the preserved Attempt 001 recovery failure.

1. **Before every invocation, including retries:** require a verified encrypted native-key header, the originally registered public ID, no agent caching, a pinned executable path/version, byte equality of the on-disk canonical statement with its frozen digest, no existing `.sig` file and no changed attempt trust-root/member/role state. Any failed check is terminal; preserve the safe reason, do not ask to sign. Never read/decrypt the key in a model.
2. Use the **V02 subprocess invocation shape** unchanged: native `ssh-keygen -Y sign` with the same namespace, inherited real console, protected key path, one canonical file, no captured/tee'd stdout or stderr, agent-disabled environment. Fresh attempt paths/statement bytes necessarily differ, so “unchanged” means invocation API/console behavior rather than byte-for-byte identical argv values. Keep the actual passphrase prompt owned by OpenSSH, never the model.
3. **After invoking:** exit code 0 plus exactly one expected signature-file candidate proceeds to independent tri-state VERIFY; nonzero exit and no signature file are the only condition permitting the **owner** to choose a bounded re-invocation; nonzero with any signature file or zero exit without exactly one file is terminal `PARTIAL_OR_INCONSISTENT_OUTPUT`. Even after exit 0, malformed or cryptographically rejected signature is terminal, not an unlock retry. A command that did not produce a signature need not be called “wrong passphrase”; record only `NO_PROOF_EMITTED`.
4. After nonzero/no-signature with index 1 or 2, show the fixed T3 retry-or-stop prompt while the original mechanical timer continues. Explicit input R allows the *next* revalidation and invocation; S, Ctrl+C or anything else stops event. No automatic retry after a process/tool failure; the owner decides. A deterministically recurring non-secret tool failure may exhaust the bounded budget but cannot synthesize a valid acceptance proof.
5. At index 3, terminal `PROOF_NOT_CREATED` on nonzero/no-signature. No fourth invocation, no statement modification, no new decision, fresh key or reattempt inside the same claim. Every result and owner-selected retry choice is appended as safe evidence. The user's ability to interrupt the whole attempt with Ctrl+C is unconditional. No optional SIGINT confirmation handler is designed or permitted for this successor.
6. Record index, subprocess exit status, presence/absence of expected signature file, rechecked preconditions, owner retry/stop choice and monotonic start/exit timestamps. Count all visible invocations and choices. Derived `ssh_sign_invocations_used`, `first_invocation_success`, `terminal_reason` replace any claim that a specific passphrase mistake was machine-diagnosed.
7. The final signing mechanical interval runs from captured owner decision through proof emission (if any) and local VERIFY resolution; no timer reset on retries or across question prompts. A verified proof is accepted at most once and only if it matches the identical signed statement and currently authorized role. Fail closed on any verifier/environment failure as section 8 requires.
8. **No literal WebAuthn retry parity:** B has a single credential assertion event. Its platform/OS decides inner PIN or biometric retries, whose count is generally unavailable; record `platform_uv_attempt_count=null`. B's P6 is SSH using the same newly created Attempt 002 Arm-A RECOVERY key, hence this same bounded SSH policy governs that one recovery proof.

Before freezing, test with synthetic credentials on the actual Windows/OpenSSH build: first success, one/two failures then success, all three failures, owner S, key swap, statement mutation, agent-loaded-between-invocations, nonzero with partial file, exit 0 missing file, unexpected executable/tool fault, Ctrl+C while a native key prompt is active, and a manually observed native-prompt visibility receipt. All paths must preserve one owner decision, one statement, at most one verified signature and zero logged secrets.

## 5. Event order, positive and negative controls

Per realizable cryptographic arm, unchanged logical sequence:

```text
setup -> P0 and controls 1..10 -> S01 -> S02 -> S03 -> L01
      -> P5 primary trust-root rotation -> P6 recovery rotation
      -> control 13 compromise-boundary classification
```

P0, P5, P6 require the actual owner to ACCEPT the synthetic security transitions; the owner can choose otherwise, but it is preserved as a failed positive-control observation rather than retried. S01/S02/S03/L01 permit the owner's actual ACCEPT/AMEND/REJECT, proof over exact decision. Negative controls 2..10 and 13 re-use existing proofs and in-memory synthetic copies and must NEVER ask the owner for another proof. No control has its predicate weakened or dropped.

A = owner-only passphrase-encrypted Ed25519 SSHSIG. B = localhost `http://localhost:8765`, rpId localhost, COSE ES256 -7, attestation none, UV/UP required, registered credential ID equality, exact digest-challenge binding and deterministic independent verification. Original one permitted unchanged interrupted registration setup repeat is preserved; failed assertion has **zero** replacement assertions. C = original two user-authored ChatGPT role attestations S01 and L01, ineligible as the sole cryptographic choice. The C statement namespace changes with successor but its known unverifiability does not.


## 6. Timing, burden, and diagnostic observations

The single original C13 mechanical interval starts at the exact instant an owner decision is captured and ends only at deterministic local proof VERIFY result, whether success or failure. It includes canonical statement and preview, child-process startup, all native unlock opportunities, signature emission and verification. Keep full unrounded monotonic duration and preserve unmodified S02 from Attempt 001. Owner semantic review begins after full exact view display and ends at decision; no upper gate. Repeated familiarity with trial text must be disclosed when comparing with Attempt 001.

Add non-gating monotonic markers `decision_captured`, `preview_emitted`, `credential_process_started[i]`, `credential_process_exited[i]`, `proof_emitted` (nullable), `verify_completed`. All subinterval durations must be nonnegative, nested inside total, and consistent with an identical monotonic clock. For WebAuthn browser event capture, use the browser monotonic clock without falsely stitching its absolute origin to the PowerShell monotonic clock; record a local total per event and stable UTC provenance separately.

For each event collect actual interaction counts (including unlock re-entry), device switches, owner-selected subjective friction 1..5, nonsecret friction note, and manual metadata edits including setup. Optional `consulted_before_decision` is observation only, not a gate. Owner questions asked before submitting a decision remain part of ungated review. They must never be misclassified as an infrastructure-only receipt after decision. Preserve original exact receipt fields and narrow external-infrastructure-only predicate. Such receipts never waive small median or L01 duration, only the existing individual-small maximum when all original requirements are satisfied.

Projected mechanical burden continues to be 97 times the selected median small time divided by 60, with the untouched >100 acceptance and >90 projected minutes test. Zero edit and no leaked owner credential remain unconditional.

## 7. WebAuthn readiness, role dependencies and process lifecycle

A distinct non-credential pre-claim readiness mode may check that the exact `http://localhost:8765` origin serves only a static probe page, listener/port is reachable, secure-context state is usable, and JavaScript can roundtrip a random **non-credential** nonce. That mode must expose no WebAuthn registration/assertion endpoints and no `navigator.credentials` or `PublicKeyCredential` capability/availability references. A source-level forbidden-API test and a browser receipt are required. Record which exact browser and user-agent reached the page and the launch method; use the **same** launch method for the actual post-claim owner session, with no assumption that Chrome and Edge credential stores are interchangeable.

Only after the new attempt start claim may the real RP enable registration and assertion ceremonies. Wait for listener readiness before automatically opening the exact localhost address. Print the literal URL regardless, as a manual fallback if launch fails. The owner must explicitly decide and perform any registration/UV/action; a browser open is not consent and cannot sign.

Preserve V02 RP origin `http://localhost:8765`, rpId localhost, ES256/COSE -7, UV/UP required, attestation none and omitted authenticatorAttachment, preferred residentKey. Registration challenge is a random 32-byte fresh nonce, pending once, consumed/expired in 120 seconds with proper origin/rpIdHash/flags and actual public key confirmation. Assertion challenge binds canonical statement digest exactly; one unused pending record, consumed first response/cancel/timeout, with no failed assertion retry. The original narrow single repeat of an **interrupted unchanged registration step** remains, using a new challenge and complete chronological receipts. `NOT_REALIZABLE` requires actual platform capability evidence; owner cancellation/timeouts are `SETUP_INTERRUPTED` and never substituted as platform impossibility.

**Explicit A→B recovery dependency:** Arm B security control P6 uses the newly created Arm-A RECOVERY key from the *same* Attempt 002, never an old key or B platform key. If A setup did not create the recovery member, mark B recovery control `FAIL / UNEXECUTED_RECOVERY_MEMBER_ABSENT`, even if B's main WebAuthn arm otherwise registered. Preserve the complete A/B per-control denominator.

**No cross-process resumption.** Between-arm same-process pauses may use a simple owner `Enter` prompt outside scored events; the process must remain alive and all prior state valid. No restarted process may reissue a begun owner proof, registration or assertion under an already claimed attempt, even if numbered snapshots or hashes appear intact. Do not introduce a SIGINT confirmation handler at all. Ctrl+C remains unconditional abort, and the new one-claim classification still applies after a retained abort. Interruption is not automatically an infrastructure exception. Preserve available evidence and seal the terminal outcome where possible.

## 8. Tri-state verification, preclaim KAT, evidence and authoritative scoring

### 8.1 Preclaim verifier known-answer gate

**Immediately before** the exclusively created owner start marker and before any real key/credential action, the **same harness process and effective tool/permission environment** that will conduct the live proofs must execute frozen synthetic known-answer tests: one valid and one mutated SSHSIG; one valid and one mutated WebAuthn ES256 assertion checked by the actual Node verification code; and temporary-public-file creation/deletion. All vectors and executable identities are frozen by hash. The harness uses only synthetic test key material. If any KAT fails, it must abort with `PRECLAIM_ENVIRONMENT_BLOCKED` and **create no Attempt 002 marker**, evidence owner event or new credential. No owner actions should have occurred and the owner is informed of the blocked setup.

A second KAT is required in the actual authorized **independent scoring** profile before interpreting captured owner proof results. If that scorer environment fails its KAT after a claim was consumed, return only non-terminal `SCORING_PENDING_QUALIFIED_ENVIRONMENT`. The public evidence remains frozen. The *same unchanged qualified scoring logic* may be re-run on those bytes in a safe verifier environment; no new owner proof or claimed attempt is involved. Pending is neither a fifth P01 scored class nor an opportunity to drop an unfavorable scored run.

### 8.2 Tri-state VERIFY and irreversible trial semantics

In-trial `VERIFY` returns exactly `VALID`, `INVALID`, or `VERIFIER_ERROR`. `INVALID` means the verifier completed an independent deterministic rejection of a signature or structure. `VERIFIER_ERROR` means the verifier could not validly decide, including temporary-directory failure, unavailable executable/Node process, non-deterministic tool failure or an exception. Do not turn OSError into a negative owner proof as V02's boolean helper did.

On `VERIFIER_ERROR`, preserve available owner proof bytes and event provenance, set attempt-integrity failure with `INVALID_INSTRUMENT / VERIFIER_ENVIRONMENT` (if attributable to a substantiated instrument issue), stop further owner ceremonies and finalize the claimed attempt as **INVALID**, not a failed recovery control or owner-chosen decision. An uncompromised signature can be independently rechecked later but must never change the already consumed attempt's classification. Authentication role mismatch, structurally invalid statement, unauthorized signature and failed exact binding produce true `INVALID` if the verifier operated correctly, with its associated frozen control/trial outcome.

### 8.3 Structural domain isolation, evidence integrity and interaction floor

Before crypto VERIFY, enforce exact prospective statement `context`, `project_id`, and `acceptance_id` grammar/prefix for **all** positive and negative verification cases. Historical old-context verification when required for trust history is deliberately performed by its own historical verifier/policy and must not be conflated with the current successor acceptance verifier. Template-relative P5/P6 vectors use synthetic public members; runtime instantiation remains exact and locally checked against archived statement digests.

Preserve all V02 public evidence fields: canonical statement and owner view, proper trust-root/signer-set state, public verification material, proof or null, exact signed/semantic/display digests, independent verify/admit decisions, safe failure/measurement and runtime receipts. Never log a private key, passphrase, SSH stderr/stdout from real signing, agent content or authenticator private material. Preserve event artifacts exclusively and append-only.

Improve tamper evidence without pretending to implement a resume journal: each raw snapshot after the first carries `previous_snapshot_sha256` computed from the **exact previous raw JSON file bytes**; the first carries null. A consumer with an independently retained trusted final digest can detect intermediate deletion/edit/reorder; no claim that a self-contained chain alone prevents wholesale replacement or proves currentness. The start claim binds fixture/harness/score hashes and T3 text hashes. This does not authorize recovery after process exit.

Alongside the owner's reported interaction count, record `mechanical_interaction_floor` computed by the harness: the minimum observed required decision, each SSH signing invocation, each retry choice and B assertion/browser interactions measurable by the system. It is a lower bound rather than a false complete count; report disagreement without changing the original numeric eligibility gate. Record WebAuthn browser-monotonic `assertion_call_started` and `assertion_call_resolved` in its own monotonic time domain; never mathematically subtract Python and JavaScript clock origins.

### 8.4 Scoring every claimed attempt (G1/G2)

Research 513 §2.2 specifies **five project-level** classes, including PASS; R0-P01 §5.9 uses **four specific primary classes**: `PASS_WITH_SELECTION`, `AMEND`, `REOPEN`, `INVALID`. The proposed incomplete-case refinement G1/G2 requires a prospectively reviewed explicit **family-level interpretation approval**, before freezing. It is not silently active merely because recorded in this draft.

After qualified scorer processing, **every claimed Attempt 002 yields exactly one** of those P01 classes. An owner abort does not evade classification. Preclaim owner decline or failed preclaim KAT consumes no claim and is *not* a scored attempt. A temporary verifier processing blocker is pending, not a terminal result. Once a qualified scorer is available, the consumed claim must be finally classified and preserved.

Proposed primary-class precedence:

1. Secret exposure, result-affecting post-observation tuning, evidence tampering, owner identity/provenance failure or material admission/control leakage => `INVALID`, reason `INVALID_INTEGRITY`.
2. A substantiated in-trial verifier/harness/environment failure that prevents a trustworthy owner proof determination, or independently proven irrecoverable instrument-generated evidence defect => `INVALID`, reason `INVALID_INSTRUMENT`. This is **not** a fabricated negative owner cryptographic outcome.
3. If *neither* A nor B is proof-viable, check whether both have **resolved** realizability (`REALIZABLE` but proof-not-viable, or `NOT_REALIZABLE`). If either cryptographic arm is unresolved due to setup interruption/owner abort, return `INVALID`, reason `INVALID_INCOMPLETE` (G1), with no architecture inference. If both resolved and neither viable, return `REOPEN` under the inherited rule. The weaker C arm never rescues A/B.
4. If at least one A/B proof-viable but no arm meets the full unchanged 13-control/burden requirements, return `AMEND`, even if the other cryptographic arm is incomplete (as for original Attempt 001).
5. If at least one eligible arm, apply unchanged A/B selection/tie-break and unchanged volume gates. Projected burden/acceptance count above either gate yields `AMEND`, otherwise `PASS_WITH_SELECTION`. If exactly one arm is eligible **because the other is unresolved from interruption**, attach `selection_uncontested_reason=OTHER_ARM_INCOMPLETE` (G2) and require an explicit warning in the future owner physical-target decision package; G2 never silently improves eligibility.

Normalizing unexecuted controls to FAIL and missing timings to null remains mandatory, without treating an unobserved B as `NOT_REALIZABLE`. Positive/negative controls are all mandatory for actual eligibility; C always nonselectable. Scorer itself must be independently tested over every G1/G2 branch, compromised evidence, unavailable but *resolved* arm, positive viable arm with interrupted opposite, and complete no-viable architecture. One final result per claim, no A/P6/S02 graft from earlier attempts.

## 9. Finite stopping policy, INVALID reasons and consent order

The machine-readable companion `R0_P01_OUTCOME_POLICY_V03_UNFROZEN_DRAFT.json` records the same **candidate** rules. It remains `UNFROZEN_NOT_EXECUTABLE`; no result table is binding until an independent review and explicit owner **stopping-policy approval before the protocol freeze**, followed later by a distinct execution authorization.

- **NOT_RUN_PRECLAIM:** The owner declines or defers before a new claim. No attempt exists, Attempt 001 remains AMEND, and any future physical-target package must address that unresolved P01 outcome. It is not a score or a free hidden attempt.
- **Absolute cap:** At most two **new** owner claim events in this specific post-001 successor family: the proposed Attempt 002 and at most one exceptional Attempt 003. This cap is distinct from historical consumed Attempt 001. No automatic second new claim, even after INVALID. **Beyond this bound a separately governed Research 513 family-preregistration amendment, new scientific justification and explicit owner decision are required**, not another exception to the same policy.
- **Exception rule:** every enumerated condition is `ALL_REQUIRED`, never OR. Common requirements: documented bounded testable cause and remedy; new explicit owner consent; independent exact prospective freeze and qualification; new exclusive identity/keys/evidence; remaining numerical allowance. For `INVALID_INSTRUMENT`, an independently substantiated and repaired verifier/harness defect may retain the unchanged original mechanism hypothesis. For ordinary `AMEND`, `REOPEN` or `INVALID_INCOMPLETE`, any exceptional successor must have a genuinely new falsifiable mechanism hypothesis, not simply improved operator familiarity. `INVALID_INTEGRITY` has **no exception under this follow-up policy**.
- **An owner abort still scores.** Owner consent and right to stop are absolute, but an abort after claim must be preserved as a scored attempt and counts against the numerical cap; `INVALID_INCOMPLETE` cannot be relabelled as instrument defect to grant a convenient retry.
- **Processing pending is not final:** `SCORING_PENDING_QUALIFIED_ENVIRONMENT` is temporary computation status on sealed evidence, and changes neither claim count nor required final classification. A clean preclaim verifier KAT failure creates no marker.

| Result after a consumed claim | Proposed consequence |
|---|---|
| `PASS_WITH_SELECTION` | Qualify only successor observations; present prior Attempt 001 AMEND and practice effect; selection not physical target; wait for P03 and explicit owner target decision |
| `AMEND` | Stop ordinary retries; retain failures; no Attempt 003 unless every exceptional condition and genuinely new hypothesis is approved |
| `REOPEN` | Reopen relevant owner-authenticity assumptions; no automatic rerun |
| `INVALID_INSTRUMENT` | Preserve; independent defect finding and repair may support one separately owner-approved exceptional claim if under cap |
| `INVALID_INCOMPLETE` | Preserve; no inference from unvisited arm and no automatic repeat after owner abort |
| `INVALID_INTEGRITY` | Preserve; no claim exception in this successor policy, requiring a wholly new independent preregistration if further owner work is ever considered |

Any future owner-facing authorization package must disclose post-result protocol changes, expected per-arm time and interaction cost, fresh key setup, owner responsibility for later key removal, possible persistent WebAuthn credential in the authenticator, the fact that aborted attempts are scored, the numerical cap and distinct INVALID branches, alternative of declining, and effect on physical target selection. This approval happens in two separately identifiable stages: **policy before freeze**, **attempt start only after fully qualified implementation**. The owner has not supplied either approval in this chat.

## 10. Required independent test matrix prior to any freeze

All tests use synthetic keys and synthetic user/proof ceremonies. A full compositional synthetic dry run through A, B and C is required, with a virtual or qualified synthetic authenticator for B; if not achievable, disclose a testability blocker rather than treating a mock as live owner UV.

1. **C1 owner-confirmed bounded signing:** first invocation success, failure then success, two failures then success, three failures, owner S stop, native Ctrl+C, missing/swapped key, mutated statement, loaded agent, tampered or partial signature, exit 0 without file, nonzero with file, unknown environment failure, pinned binary mismatch. Every case: one decision and acceptance ID, same statement bytes, max three invocations, one verified proof at most, no timer reset, no passphrase or real stderr logging. Manual native prompt visibility receipt on target Windows build.
2. **C2 G1/G2 scored claims:** A viable + B interrupted => AMEND or PASS per unchanged A gate, with G2 if eligible; A nonviable resolved + B interrupted => INVALID_INCOMPLETE; both nonviable resolved => REOPEN; neither resolved => INVALID_INCOMPLETE; true integrity INVALID_INTEGRITY overrides; instrument INVALID_INSTRUMENT; C completion cannot change class. Every claimed branch eventually has exactly one primary P01 class, no TERMINATED_UNSCORED.
3. **C3 KAT/tri-state:** fail actual harness preclaim temporary-file or SSH/WebAuthn synthetic KAT and confirm no marker/owner event exists; inject a verifier exception mid-event to produce VERIFIER_ERROR and final INVALID_INSTRUMENT, preserving captured public bytes without fabricating owner proof rejection; rerun after scoring-only environment preflight to obtain identical derived result from unchanged public evidence.
4. **C4 structural VERIFY:** freshly signed old-context statement, wrong project, old acceptance prefix, wrong role, bad signed digest, replayed old proof and a runtime statement in prior digest set must reject. Freeze full vectors for key-independent events and synthetic-key-instantiated P0/P5/P6 templates. Runtime new public members must match registered trust set and template.
5. **C5 policy schema:** `ALL_REQUIRED` exceptions, absolute max two new claims including one exceptional claim, no automatic Attempt 003, NOT_RUN preclaim row, separate INVALID_INSTRUMENT/INCOMPLETE/INTEGRITY reasons and appropriate exception gates. Owner policy assent must precede any final freeze, and execution assent must occur after implementation qualification.
6. **B browser preflight:** source-level scan of standalone preclaim server/page shows no WebAuthn API names/routes, record browser UA/launch method and replay same method postclaim after RP readiness, ensure printed URL, genuine postclaim registration/assertion with origin/RP/UV/ES256 validation, expiration/replay/timeout, no second failed assertion, explicit B P6 missing same-attempt A recovery member FAIL.
7. **Evidence audit:** snapshot previous SHA-256 chain measured over exact prior file bytes; deletion/mutation/reordering detectable with an independently retained final head digest. Does not grant process resume. Harness-computed interaction floor vs reported interactions and browser-monotonic assertion landmarks.
8. **No cross-process resume and no Ctrl+C handler:** ordinary uninterrupted A→B→C, owner abort during native SSH/Node/browser operations and between-arm pause, preserved terminal class and exclusive marker; no synthetic reissue of consumed owner proof on process restart.
9. **Complete synthetic integrated run:** run A→B→C with all thirteen controls and 1/2/4/30 burden under qualified test keys, then run independent qualified scorer and confirm the expected primary result and stopping rule. Also exercise full failure/interrupt/negative-control runs and verify old Attempt 001 proof artifacts cannot satisfy successor policy.
10. **Documentation and authorization:** project integrity checks, exact-fixture SHA-256 vectors, scoring and KAT policy hashes, explicit Research 513 interpretation approval if G1/G2 retained, separate owner stopping-policy consent before freeze, source-code attestations for no private-key or real owner proof access by models.

## 11. Remaining freeze blockers after Message 021 reconciliation

- **B01 PROTOCOL / RESEARCH 513 INTERPRETATION:** G1/G2 scored partial-arm classification and selection disclosure need a separately documented, prospective Research 513 family-level interpretation approval. Research 513's five global classes and P01's four-class branch must stay distinguishable. Provisional successor protocol label R0-P01-V01-I1 remains unfrozen.
- **B02 OWNER STOPPING RULE APPROVAL:** The owner has not accepted the two-new-claim maximum, branch-specific conditions, NOT_RUN and INVALID subtypes. That decision is required **before** any protocol/scorer freeze, distinct from later execution consent.
- **B03 NATIVE WINDOWS OWNER RETRY TESTING:** The classifier is abolished, but retained V02 inherited-terminal `ssh-keygen -Y sign` invocation and explicit R/S re-invocation still require target Windows synthetic tests of precondition mutation, prompt visibility, file residue and abort behavior.
- **B04 PRECLAIM AND IN-TRIAL VERIFY KAT:** Target-environment synthetic SSHSIG and WebAuthn vector tests, tri-state return semantics and deterministic instrument-failure classification must be frozen and independently qualified.
- **B05 NONCE/TEMPLATE IDENTITIES:** Final successor context/project/prefix, synthetic-key P0/P5/P6 templates, new-byte golden vectors, prior digest-list derivation and local public-key inequality checks are not frozen.
- **B06 LOCALHOST USER SESSION:** Noncredential preclaim server and exact browser user-agent/method, postclaim readiness/launch, and virtual/synthetic B full-run testing remain to be built and qualified.
- **B07 SNAPSHOT INTEGRITY:** Prev-snapshot-byte-hash semantics, external final-head witness, append-only crash interruption handling and scorer deterministic replay tests still need implementation and independent qualification. Cross-process resume remains excluded.
- **B08 OWNER AUTHORIZATION PACKET:** Explain remaining limits, actual burden, possible resident WebAuthn credential and cleanup, aborted claim scoring, privacy and two stages of owner decisions.
- **B09 P03 ORDER & DOWNSTREAM UX:** Parallel P03 research may proceed; scored P03 order change requires prospective Research 513 authorization. Real consequential context, explanation and long-term recovery-key durability remain tracked R1 work.

All former C1–C5 blockers have **proposed** technical resolutions, not demonstrated live or frozen conformance. No owner key is created, no attempt marker claimed, no scorer run over a new real owner proof and no production architecture selected.

## 12. Status of revised candidate

```text
DOCUMENT=R0_P01_V03_UNFROZEN_DRAFT_REV02
PEER_MESSAGE_021=RECONCILED_FOR_REVIEW_NOT_FROZEN
PROVISIONAL_PROTOCOL=R0-P01-V01-I1
RESEARCH_513_INTERPRETATION=NOT_YET_APPROVED
OWNER_STOPPING_POLICY=NOT_YET_APPROVED
ATTEMPT_001=AMEND_PRESERVED
ATTEMPT_002=NOT_CLAIMED
OWNER_KEYS=NOT_CREATED
CONTRACT_FREEZE=NOT_AUTHORIZED
IMPLEMENTATION=NOT_AUTHORIZED
NEXT=INDEPENDENT_REVISED_DRAFT_REVIEW_AND_OWNER_POLICY_DECISION
```
