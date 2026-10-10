# R0-P01 Prospective Successor Contract V03: UNFROZEN DRAFT

**Date:** 2026-10-10
**Status:** DESIGN DRAFT / NOT EXECUTABLE / NOT FROZEN / PEER REVIEW NEXT
**Scope:** Candidate complete, separately identifiable owner-authenticity qualification, after preserved Attempt 001 AMEND. No sensitive operation or new experiment is authorized.
**Intended identities:** Protocol R0-P01-V02; contract R0-P01-CONTRACT-V03; Attempt 002; new independent owner-local evidence.
**Parent:** Research 513, Research 518, Research 521, Research 525, Validation 216 and MC-0030 Message 019.
**Authority:** Research-only proposed contract. None of the V01/V02 contracts, Attempt 001 observations or scorer rules are retroactively amended.

## 1. Non-negotiable experiment family invariants

Research 513 continues to govern all 13 negative/positive controls and the zero-miss criterion; arms A SSH Ed25519, B localhost ES256 WebAuthn with UV, and C weaker non-cryptographic chat-role comparator; three small trials with 1, 2 and 4 effects, one large with 30 effects; independent owner decision and detached proof; cryptographic VERIFY distinct from semantic ADMIT; history and role enforcement; no proof/identity pooling; and zero manual metadata edits or secret exposure.

Frozen burden thresholds: median small signing mechanical time <=60 seconds, each small <=120 seconds except a contemporaneously qualified infrastructure-only receipt as defined by V02, and large <=120 seconds without exception. Trial decision/preview ordering, inventory estimate (97 acceptances, 157 effects, counts by effects 1:62, 2:17, 3:11, 4:7), projected acceptance limit 100, projected mechanical minutes 90, A/B selection differences of 10 s (median small), then 15 s (large), then B tie-break remain unchanged. No owner-view coaching for ACCEPT, AMEND, REJECT or self-rated friction.

This document **does not** authorize Attempt 002. The original started Attempt 001 remains irrevocably AMEND, with recovery FAIL, S02 130.8491039001383 seconds, incomplete B/C, and old marker/raw/backups/keys unchanged. Post-result changes are declared as result-informed, prospectively tested and independently reviewed. GOVERNED_LEDGER_KERNEL_V02 is still unselected as physical target; R0-P02 PASS and R0-P03 pending; Specification 028 and unrelated INCOMPLETE scientific outcome unchanged.

## 2. Proposed irreversible identity and old-evidence relation

1. The new exclusively created owner-local start marker has fixed attempt ID "002", prospective source-review HEAD, exact fixture/contract/harness/scorer hashes, UTC creation observation, old marker exact-file SHA-256 and old final snapshot exact-file SHA-256. It must be persisted **before** fresh owner key creation or browser registration. The owner explicitly approves the separate attempt in advance. No reusing, deleting or resetting the original marker.
2. The *correct* old final raw file hash is `a48e066adea499eb17e4d6240cb459df315b91f444fdee4f42ab880bddc60296`; marker rehashed independently read-only on 2026-10-10: `864f4b1a7be30e312abd5dcdb9359090dd8aa8ddbfa321e823261d63c9971281`. All future hash values must be machine-emitted and independently checked, never trusted merely because printed in this design draft. Both old hashes are provenance, never security evidence replacing trust.
3. Target directories are isolated from the repo and Attempt 001: candidate owner private key directory `%LOCALAPPDATA%\ADS-R0-P01\attempt-002\arm-a` and public evidence `%LOCALAPPDATA%\ADS-R0-P01-Owner-Evidence-002`; no path is created now. Attempt 002 evidence and claim must be exclusive-create, append-only, no overwrite. Never upload owner public proof records wholesale or reveal personally linkable public IDs without owner authorization.
4. Fresh owner-protected PRIMARY and RECOVERY Ed25519 keys must be generated through native interactive OpenSSH prompts after the claim and under owner control. Require nonempty passphrases and no agent caching. The fresh two public IDs must differ from each other and all Attempt 001 public signer IDs; compare against pre-existing nonsecret records **locally**, without reading any old private key. Do not silently reuse Attempt 001 recovery key for B. Arm B's designated recovery member is the **new** Attempt 002 Arm-A recovery key.
5. No signature offers trusted signing or key-birth time merely by its SSHSIG bytes. The chronology is established by an honest owner action plus durable, tamper-evident local observation sequence. Do not misstate owner-machine wall-clock time as a cryptographic guarantee.
6. Preserve the original nine-field SignedAcceptanceStatement exactly: `context`, `project_id`, `acceptance_id`, `envelope_digest`, `shown_digest`, `decision`, `semantic_base_digest`, `signer_set_version`, `issued_at`. Update fixed context to proposed `ADS-R0-P01-002-OWNER-ACCEPTANCE-V01` and acceptance IDs to proposed `R0-P01-002-<ARM>-<ITEM>`. Exact final strings are not yet frozen. Keep V02 C01 canonical JSON and semantic-base rules, AC-1..AC-6, synthetic project identity, and equivalent effect texts. `issued_at` is fixture provenance, not a signed timestamp oracle.
7. Prequalify **all** valid successor candidate statements for the three possible decisions on ordinary S01/S02/S03/L01 and the three security proofs P0/P5/P6. Ensure none has the exact same SHA-256 statement digest as any **actual** Attempt 001 statement, and require old valid proof against new statement to fail. The old-digest set and digest of its sorted elements must be derived mechanically from publicly preserved Attempt 001 evidence, not handwritten.

## 3. Presentation and sign-what-you-see

- **T1, authoritative payload:** ordered accepted effects, governing identities and semantic dependencies. Both envelope_digest and shown_digest bind the exact rendered proposal.
- **T2, decision context:** non-authoritative purpose, history, provenance, alternatives and consequences. Only shown_digest binds it; it cannot redefine envelope meaning. For this successor synthetic burden benchmark, no variable T2 text is introduced. Later R1 UI work must implement meaningful context with exact source references and explicit presentation.
- **T3, fixed procedural chrome:** timing notice, PRIMARY/RECOVERY credential cue, noninterrupting localhost directions, non-secret friction questions. T3 is visibly *outside* OWNER VIEW delimiters and absent from both digests; its exact bytes/version are statically bound by the proposed implementation/contract freeze, not dynamically generated from ChatGPT.

Before any owner run, freeze the exact T1 view renderer including LF/newlines, delimiters, spacing, Unicode, colors/escapes if any, and complete new golden vectors. The statement preview remains after owner decision and **inside** the mechanical timer. The owner always selects their own decision; no assistant assigns it. Proposed T3 sentences, to be finalized verbatim in the new fixture:

```text
These proposals are synthetic; your decision should represent what you intend to authorize.
Ask questions before submitting a decision if you need context.
The signing timer starts when you submit a decision and includes the statement
preview, passphrase or authenticator use, and local verification.
PRIMARY key: use the PRIMARY passphrase created for this attempt.
RECOVERY key: use the separate RECOVERY passphrase, not the PRIMARY passphrase.
To open the localhost page, leave PowerShell running. Do not use Ctrl+C to copy.
Never share key material or passphrases with ChatGPT, Claude, Codex or Runtime Bridge.
```

This is **not** the final UX selected for consequential owner decisions. Track owner-view context and rare-recovery-passphrase durability as explicit future requirements outside this synthetic P01 signing-cost test.

## 4. Proposed proof event: bounded SSH unlock opportunities

V02's single `ssh-keygen -Y sign` subprocess turned one wrong passphrase into no proof. This is correctly preserved as an original FAIL. To prevent arbitrary one-shot keystroke brittleness in a **future** experiment, propose at most **three** native SSH unlock opportunities within **one identical proof event**. Applies to Arm A P0/S01/S02/S03/L01/P5/P6 and to Arm B's SSH-backed P6.

- Capture the owner's decision only once and create a canonical immutable statement once. Reinvoke the *same* native unlock/sign command with the *same* key, statement file, acceptance ID and digest only upon a recognized recoverable unlock failure **and absence of a proof**. No new proposal, identity, or timer reset.
- Each failed opportunity gets a safe append-only diagnostic `attempt_index`, `elapsed_since_decision`, `classified_failure`, `proof_emitted=false`; all attempts count as user-visible interactions and within the existing decision-to-verification monotonic time.
- Fail closed on any file/statement/key mismatch, detected agent cache, malformed proof, unexpected or partial signature output, unknown return status, IO failure, user cancellation, wrong executable or integrity uncertainty. Never retry generic nonzero failures. A fixed native-Windows **recoverable wrong-passphrase classifier** must preserve visible native prompts, avoid any secret capture/logging, and be independently qualified for known Windows OpenSSH output and localization. This exact classifier is a blocking unresolved implementation decision.
- If the first, second, or third attempt produces one valid detached proof, independently VERIFY it and finish. If all three classified attempts fail, preserve terminal proof failure, timing and friction; there is no fourth attempt, replacement key, resubmission or control retry. Report `ssh_unlock_opportunities_used`, `first_unlock_success`, `safe_failure_category`, not a passphrase.
- **Do not claim strict retry parity with B.** WebAuthn platform PIN/biometric retry budgets are opaque and not controllable by this harness. The successor grants exactly one RP assertion ceremony, with no harness-level re-assertion; record `platform_uv_attempt_count=null`. B's separate recovery-key ceremony uses the proposed SSH bound.
- The three-attempt modification is expressly `RESULT_INFORMED_PROSPECTIVE_CHANGE`, not a pre-observation feature or a relaxation of the 13-control gate.

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

## 7. WebAuthn reachability and process lifecycle

A distinct **non-credential** preclaim test may verify only that the exact localhost origin serves a static page, that a JavaScript nonce roundtrip succeeds, and that the page observes `window.isSecureContext`. No preclaim `navigator.credentials.create/get`, `PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable`, WebAuthn compatibility/capability query, UV challenge, private key, registration or assertion. This prevents availability knowledge from informing a last-minute arm tweak. Preclaim infrastructure check is recorded as safe unscored evidence.

After an exclusively claimed successor start, launch the WebAuthn server on localhost, validate readiness, and if the owner chooses, open `http://localhost:8765` through a qualified owner-local browser launch. Print the literal URL as fallback. No process should require Ctrl+C to copy it. Any browser action remains an explicit owner ceremony, never an automated user-presence assertion.

The WebAuthn RP still requires the frozen V02 32-byte cryptographic registration challenge, single-use 120-second expiry, exact origin/rpIdHash, UP/UV flags, ES256 key validation, one registered credential ID and per-assertion exact canonical statement SHA-256 challenge. No automatic resubmission of a failed owner assertion. The single original unchanged registration retry is allowed only for an interrupted setup, with a fresh challenge and complete receipts, not as protocol tuning. Keep `NOT_REALIZABLE` for genuine platform inability, `SETUP_INTERRUPTED` for owner cancellation/timeouts, and never mark an unvisited arm technically infeasible.

**Chosen draft minimum:** No cross-process run resumption. The previous implementation wrote append-only sequential JSON snapshots, **not** a verified hash-chained replayable cursor. If the owner closes the run, an in-progress proof is interrupted and must not be reissued under that same claim. Completed evidence is preserved, the marker remains consumed, and no silent restart is allowed. Permitted breaks, if desired, are only pauses between arms **while the same live process remains running** and outside any timed owner event. Never promise to resume after sleep, reboot, crash or terminal close. A dedicated Windows Ctrl+C confirmation handler may be considered **only after** native child-process SIGINT simulations establish a reliable unconditional abort path; if not qualified, omit the handler, warn that Ctrl+C terminates, and rely on safe browser launch plus clear instructions. Do not introduce an unqualified recovery control plane just for UX.

## 8. Evidence, preflight, scorer and environment limitations

The new start claim and every owner-sensitive event must be durably observed before further side effects where feasible. Create sequential append-only public JSON snapshots with exclusive-create semantics and no overwrites. Preserve partial failures as explicit outcomes; after a crash no ongoing process can reconstruct authority to reissue a proof solely from numbered files. If a later design needs cross-process resumption, it is a new separately tested mechanism requiring identity, hash linkage, authenticated cursor, consumed challenges and exactly-once proof/ID guarantees.

Keep public exact owner view, canonical envelope and statement, proof (or null), verifying public key, signer-set version and role, independent VERIFY result, ledger ADMIT and historical trust-state evidence, setup receipts, safe monotonic/wall-clock times, failure class and owner measurements. Preserve all V02 fields, no false null-to-zero normalization. No private-key bytes, passphrase, credential path, browser authenticator secret, hidden identity or SSH-agent contents reach ChatGPT, Claude, Codex, Runtime Bridge, repository, CI logs, public evidence or program arguments.

Before **scoring** any real owner record, in the **same verification permission profile** use fixed synthetic known-answer proofs: valid SSHSIG and valid WebAuthn ES256 assertion must verify, mutated/bad versions of each must reject. If the verifier needs temporary files containing public proof material, demonstrate they can be securely created and destroyed in the actual scoring context. When the synthetic known answers fail, emit a separate `ENVIRONMENT_PREFLIGHT_BLOCKED` processing status without interpreting owner proofs as invalid; do not edit raw evidence or retry the owner. The earlier read-only sandbox `INVALID` was such an environmental false negative.

All 13 security controls stay either PASS or FAIL for A/B, with unexecuted ones explicitly FAIL/unexecuted for eligibility, while C remains NOT_APPLICABLE and never selection-eligible. S01/S02/S03/L01 records preserve actual owner decisions, signatures, and available elapsed times. Scorer independently derives proof viability, arm eligibility and chosen arm, enforces no cross-attempt proof mixing, and evaluates volume and tie-break unmodified. A result does not become PASS because a missing B/C arm or failed P6 was ignored.

## 9. Outcome discipline and stopping rule (separate companion policy)

The companion `R0_P01_OUTCOME_POLICY_V03_UNFROZEN_DRAFT.json` is proposed, not enforceable. If accepted prospectively, the owner permits at most **one new independent Attempt 002** under this follow-up family, and no automatic Attempt 003. Attempt cap counts exclusive start claims, including interrupted owner sessions, not just completed scored runs. Any future exceptional attempt requires a genuinely different falsifiable mechanism hypothesis, explicit owner decision, separately frozen rules and complete evidence, never repeating until green.

| New run disposition | Primary score | Proposed required subsequent action |
|---|---|---|
| COMPLETED_SCORED | PASS_WITH_SELECTION | Report qualification only under successor contract; preserve original AMEND alongside; wait for P03 and explicit physical-target decision |
| COMPLETED_SCORED | AMEND | Stop routine re-execution; owner chooses bounded governing UX/trust-root amendment, deferred decision or new hypothesis, with no automatic Attempt 003 |
| COMPLETED_SCORED | REOPEN | Reopen load-bearing owner-authenticity architecture comparison; no automatic retry |
| COMPLETED_SCORED | INVALID | Preserve evidence/defect, stop, require separate owner-approved prospectively frozen hypothesis before any further attempt |
| TERMINATED_UNSCORED | null | Preserve partial observations, report no architecture conclusion from unattempted arms, do not rerun automatically |
| ENVIRONMENT_PREFLIGHT_BLOCKED | null | Stop processing and qualify verifier environment separately; if discovered before owner claim, no marker is consumed; if after owner claim, preserve consumed claim and evidence |

**REVIEW BLOCKER: Research 513 taxonomy.** Research 513 §2.2 requires exactly one primary class per probe. The candidate `TERMINATED_UNSCORED` and preflight-blocked outcomes represent **no completed probe result**, not a fifth class. That distinction must be independently approved before freeze. For example, A invalid with B interrupted does **not** prove both cryptographic mechanisms infeasible. Conversely, a fully exercised complete experiment with no viable A/B and no integrity failure must return REOPEN under the original scorer. If needed, a disclosed *prospective* family-level interpretation must be authorized; no silent redefinition after observing Attempt 001.

Result priority for COMPLETED_SCORED remains: actual integrity defect INVALID; fully tested no viable cryptographic A/B REOPEN; viable but none selection-eligible AMEND; selected eligible but burden volume above gates AMEND; eligible within volume PASS_WITH_SELECTION. Never insert missing observations to force a class or declare a merely untested B NOT_REALIZABLE.

The owner's right to decline a new attempt, stop a run, or defer P01 is absolute. An owner-facing authorization package before any new claim must clearly explain reason for successor, which amendments are result-informed, potential owner time, fresh credential setup and its risk, incomplete/failed consequences, repeated-participant caveat and the stopping policy. This draft is not consent.

## 10. Independent preregistration test matrix

Every proposed implementation must pass prospective tests with **synthetic test credentials only**, followed by adversarial review and an exact fixture/implementation freeze BEFORE owner keygen:

1. Successor context/ID uniqueness; compare all statement digests with actual public Attempt 001; reject old proof against new statement and vice versa; role separation, cross-project replay, modified view, duplicate admission, stale semantic base, historical rotated signer, compromise boundary.
2. Three unlock opportunities: 1st-try success, wrong-then-correct, twice-wrong-then-correct, three wrong, non-unlock error, partial signature, switched key, unexpected existing statement, localized/unknown error, process interruption. Check only one decision, one statement and at most one final proof; no secrets captured; timers and interactions correctly count *all* opportunities. No generic retry on nonzero exit.
3. Exact sign-what-you-see T1 owner bytes and T3 exclusion; static byte hashes for role/timing/navigation cues; no variable T2 context in synthetic trial. Falsify swapped decision/views and wrong statement.
4. WebAuthn separate reachability-only mode with no WebAuthn APIs; real setup after new claim; valid ES256 UV exact challenge, negative origin/RP/credential/up/uv/counter/replay cases, 120-second expiry, owner interrupted setup and single unchanged registration retry, no second failed assertion.
5. Monotonic subintervals nonnegative and nested in the unchanged total; no timer reset on retries; no receipt exception except strictly valid external infrastructure; pressure not to rush review.
6. Safe browser open and Windows process abort behavior, last-chance private-key secret scanner, start-marker exclusive claim and clean-HEAD artifact identity, evidence append-only, no cross-process event reissue.
7. Scorer environment synthetic known-good and known-bad SSH/WebAuthn proofs in actual profile; all result-class/selection/volume/arm-missing branches, C comparator non-selection, no cross-attempt scoring.
8. Independent reviewer must resolve the numbered BLOCKERS below before a new contract or code is frozen. Any later protocol repair after the owner claim is forbidden.

## 11. Blockers still requiring resolution before freeze

- **B01 Unlock classification:** a native-Windows failure classifier that detects *only* recoverable owner unlock errors and never suppresses the native terminal passphrase prompt; test exact tool/locale variants before freezing.
- **B02 Outcome taxonomy:** non-scored abort/preflight disposition relative to Research 513 four-class requirement, especially no false REOPEN for untested arm.
- **B03 Old/new statement comparison:** exact collection and public hash summary for all actually observed Attempt 001 proofs and candidate successor decisions; new golden vectors derived from frozen fixture.
- **B04 WebAuthn preflight:** exact non-credential page and prohibited API inventory; user-local browser origin and launch tests.
- **B05 User approval:** stopping rule and fresh-key/privacy boundary explicitly authorized before any new owner-sensitive claim.
- **B06 Partial-arm semantics:** fully scored A with absent B/C versus session terminated before any cryptographic proof; preserve distinction without retroactive repair.
- **B07 Abort model:** Windows Ctrl+C/passphrase subprocess behavior, safe same-process breaks, no unsupported cross-process resume.
- **B08 R1 downstream:** genuine owner decision context/history/consequences bound as T2 and rare recovery-key storage/drills explicitly tracked for later real system qualification.
- **B09 P03 order:** design can progress concurrently without scored run; any departure from Research 513 §3 order requires a prospectively approved change before an affected result.

## 12. Status

```text
DOCUMENT=R0_P01_V03_UNFROZEN_SUCCESSOR_DRAFT
ATTEMPT_001=AMEND_PRESERVED
ATTEMPT_002=NOT_CLAIMED
OWNER_KEYS=NOT_CREATED
NEW_CREDENTIAL_PROOF=NOT_AUTHORIZED
CONTRACT_FREEZE=NOT_AUTHORIZED
IMPLEMENTATION=NOT_AUTHORIZED
NEXT=INDEPENDENT_ADVERSARIAL_DESIGN_REVIEW
```
