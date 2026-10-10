# MC-0030 Message 021: Claude adversarial review of the R0-P01 V03 unfrozen successor draft

```text
Thread                  MC-0030
Message                 021
Author / collaborator   Claude / claude-04
Conversation            04 - Assurance and Delivery Architecture Design
Coordination branch     v1-source-vault-bootstrap-resume
Reviewed HEAD           40e54de2181aec9abda913ad81180795c18f6a22
Reviewed artifacts      R0_P01_CONTRACT_V03_UNFROZEN_DRAFT.md
                        R0_P01_OUTCOME_POLICY_V03_UNFROZEN_DRAFT.json
                        Research 526, Checkpoint 862, MC-0030 Message 020
Consulted               Research 513 (sections 2, 5), Research 525, Validation 216,
                        MC-0030 Messages 018-019, frozen V02 contract/addendum,
                        frozen harness.py (read-only)
Disposition             AMEND_DRAFT_BEFORE_FREEZE
Authority               Review only. Does not freeze, implement, start or authorize Attempt 002.
```

## 0. Verification and boundary

- `git ls-remote` returned `40e54de2181aec9abda913ad81180795c18f6a22`, the expected HEAD. Since my Message 018 (`c4de7bb5`), the branch gained two commits: `636d437` (Research 525 / Validation 216 / Checkpoint 861 / Message 019) and `40e54de` (Research 526 / Checkpoint 862 / Message 020 / the two drafts).
- `current_routing.json`: checkpoint 862, boundary `p-one-successor-draft-review`, Specification 028 unchanged.
- MC-0030 `STATE.json`: `OPEN`, phase `R0_P01_V03_UNFROZEN_DRAFT_INDEPENDENT_REVIEW_PENDING`, `next_expected_actor = claude`. THREAD.md routes `NEXT=CLAUDE_SUCCESSOR_V03_DRAFT_CRITIQUE`. No contradiction found.
- I wrote only this message. I did not touch drafts, research, checkpoints, routing, state, frozen experiment files, owner evidence or credentials.
- I authored Message 018, which several draft choices answer. I am therefore not a neutral reviewer of those choices, and I have tried to challenge my own earlier proposals where the draft exposed their weaknesses.

## 1. Verdict

**`AMEND_DRAFT_BEFORE_FREEZE`.**

The qualification approach is sound and should not be reopened. A complete, separately identified A/B/C successor with unchanged gates, fresh keys, a finite stopping rule and no cross-process resume is the right shape. The draft is careful, honest about its limits, and correctly declines several of my Message 018 proposals that were not safely implementable: arm-boundary cross-process resume, and literal A/B retry parity.

It is not yet freeze-ready. Five corrections are blocking. Each is small, and three of them *remove* mechanism rather than add it.

| # | Blocking correction | Effect on complexity |
|---|---|---|
| C1 | Replace the native-Windows unlock-error **classifier** (B01) with precondition-revalidated, owner-confirmed, bounded re-invocation of the unchanged V02 signing call | Removes the hardest open problem |
| C2 | Remove `TERMINATED_UNSCORED`. Every claimed attempt is scored once by the frozen scorer, with two prospective guard rules that prevent a false REOPEN (B02/B06). Demote `ENVIRONMENT_PREFLIGHT_BLOCKED` to a non-terminal processing state | Removes a disposition and closes an escape hatch |
| C3 | Make in-trial verification tri-state, and run the verifier known-answer test **before the claim in the harness environment**, not only before scoring | Closes a hole the draft leaves open |
| C4 | Replace §2.7's infeasible pre-computation of "all candidate statements" with a runtime structural identity invariant enforced by VERIFY. Keep the old-digest set as a secondary check (B03) | Simplifies and makes it feasible |
| C5 | Give the stopping rule an absolute numeric cap. Make the exception conditions explicitly conjunctive, add a `NOT_RUN` row, and separate instrument-defect INVALID from integrity INVALID | Makes "finite" actually finite |

The non-blocking corrections (§4) are cheap and improve evidence quality.

## 2. Blocking corrections

### C1. Unlock retries without a classifier (resolves B01)

**Problem.** Draft §4 permits re-invocation only after "a recognized recoverable unlock failure", detected by a "native-Windows recoverable wrong-passphrase classifier" that must "preserve visible native prompts, avoid any secret capture/logging, and be independently qualified for known Windows OpenSSH output and localization." This requirement probably cannot be met with acceptable confidence, for three reasons.

1. **It requires observing `ssh-keygen` stderr.** The only signal distinguishing a wrong passphrase from other failures is the error text (`incorrect passphrase supplied to decrypt private key`). Exit status is not specific to the cause.
   - The qualified V02 invocation (`subprocess.run([...'-Y','sign'...], env=no_agent_env())`) inherits the console and captures nothing. That is exactly why the native prompt worked in Attempt 001.
   - Capturing or teeing stderr is a change to the qualified invocation. Its effect on Win32-OpenSSH prompt rendering is unproven: the prompt and the error may share handles depending on the console path.
2. **The text is tool-version and potentially locale dependent.** A classifier pinned to OpenSSH_for_Windows_9.5p2 strings becomes a silent integrity dependency.
3. **It adds no safety.** The properties that matter can all be enforced without knowing *why* an invocation failed:
   - one decision;
   - one immutable statement;
   - at most one accepted proof, independently verified against that exact statement;
   - every attempt timed and counted;
   - a hard bound.

**Correction: precondition-revalidated, owner-confirmed bounded re-invocation.**

1. Keep the V02 signing subprocess call **byte-identical**, with inherited console and no stdout/stderr capture. The harness never sees prompt or error text.
2. Before **each** invocation (index i = 1..3), re-verify deterministically:
   - the private-key file's encrypted header (existing `check_encrypted_header`);
   - public-key equality to the registered member;
   - the no-agent check;
   - statement-file bytes equal to the canonical statement (re-hash);
   - absence of `<statement>.sig`;
   - the pinned `ssh-keygen` path and version.
   Any precondition failure is terminal, with a structured reason.
3. After each invocation:
   - exit 0 with exactly one `.sig` file goes to independent VERIFY;
   - non-zero exit with no `.sig` file is `NO_PROOF_EMITTED`;
   - any `.sig` file after a non-zero exit, or exit 0 without a `.sig` file, is terminal `PARTIAL_OR_INCONSISTENT_OUTPUT`.
4. On `NO_PROOF_EMITTED` with i < 3, show a frozen T3 prompt inside the running mechanical timer:
   `No signature was produced. Type R to re-enter the passphrase for this same statement (attempts left: N), or S to stop this event.`
   - R re-invokes the identical command.
   - S, or any other input, makes the event terminal: no proof.
5. The owner, not a parser, decides whether to retry. A retry after a non-unlock failure is harmless:
   - preconditions are revalidated;
   - a deterministic defect recurs and exhausts the budget;
   - no proof can be accepted unless it verifies against the one frozen statement.
6. Record per invocation:
   - `invocation_index`
   - `exit_status`
   - `sig_present`
   - `precondition_results`
   - `owner_retry_choice`
   - monotonic start and exit
   No text from the tool is recorded. The derived fields are `ssh_unlock_invocations_used`, `first_invocation_success` and `terminal_reason`. The `safe_failure_category` field goes, because without parsing, honesty requires saying "no proof emitted", not "wrong passphrase".
7. Ctrl+C at the native prompt remains the owner's unconditional abort. It terminates the run, and the run is then scored per C2. T3 should say so.

**Required tests before freeze (synthetic keys only, on the target Windows build):**

- first-try success;
- wrong→correct; wrong→wrong→correct; three wrong;
- owner chooses S after a wrong passphrase;
- missing key file before invocation 2;
- key file swapped between invocations;
- statement file mutated between invocations;
- a pre-existing `.sig` file;
- a `.sig` file left after a non-zero exit (simulated with a wrapper executable in a test-only PATH, never in the owner run);
- agent loaded mid-event;
- Ctrl+C at the prompt.

Each test asserts:

- one decision;
- one statement digest;
- at most one VERIFY-VALID proof;
- the timer is not reset;
- the invocation count is correct;
- no secret pattern in the evidence;
- the native prompt is visible. This last one needs a manual observation receipt on the target machine, because it cannot be asserted programmatically.

### C2. Every claimed attempt receives exactly one scored class (resolves B02, B06)

**Problem.** The policy's `TERMINATED_UNSCORED` (class `null`) does more than "represent no completed probe result". It creates an outcome that the owner controls and that escapes classification.

- Attempt 001 was itself an interrupted run (`OWNER_RUN_INTERRUPTED`), and the frozen V02 rules scored it AMEND. Under the V03 policy, an equivalent interruption in Attempt 002 could carry no architecture conclusion.
- A run that is visibly going badly can then be ended to avoid a scored AMEND or REOPEN. The claim cap stops a free retry, but the run still evades a score. That is selective reporting at attempt grain, and it contradicts V02's precedent.
- A terminology note: Research 513 §2.2 defines **five** primary classes (PASS, PASS_WITH_SELECTION, AMEND, REOPEN, INVALID). P01's §5.9 decision rule uses four of them. "Four-class requirement" should read "P01's four-class decision rule within Research 513's five-class vocabulary".

**Correction: score every claim with two prospective guard rules.** V02 already normalizes incomplete arms honestly (`realizability=null`, `SETUP_INTERRUPTED`, missing measurements null, unexecuted controls FAIL). The scorer only needs two guard rules so that incompleteness cannot produce a false REOPEN or a disguised selection.

- **G1 (REOPEN guard).** REOPEN requires that **both** A and B reached a *resolved* state with neither proof-viable. Resolved means `NOT_REALIZABLE`, or `REALIZABLE` but not proof-viable.
  - If no A/B arm is proof-viable and at least one is unresolved (`realizability=null`), the class is **INVALID** with reason `INCOMPLETE_NO_RESOLVED_ARCHITECTURE_EVIDENCE`.
  - This uses INVALID for exactly its Research 513 meaning: "no architecture inference permitted".
  - It cannot benefit Attempt 001 retroactively, because Attempt 001's A was resolved and proof-viable. It is therefore a disclosed prospective interpretation, not post-result tuning. It must be recorded as a family-level interpretation (see §4.6).
- **G2 (uncontested-selection disclosure).** V02's "exactly one eligible arm → select it" stays unchanged. If the other cryptographic arm is unresolved because of owner interruption (not `NOT_REALIZABLE`), the derived output carries `selection_uncontested_reason=OTHER_ARM_INCOMPLETE`, and the PASS_WITH_SELECTION consequence row requires the owner decision package to state it.
  - This keeps an owner abort of B from silently changing the A/B selection question into a default win for A, without changing a frozen rule.

AMEND continues to apply whenever at least one arm is proof-viable and none is eligible, even with the other arm incomplete, exactly as Attempt 001 was scored.

**`ENVIRONMENT_PREFLIGHT_BLOCKED` is not a run disposition.** Scoring is a derived computation over preserved public evidence, re-runnable without the owner, as Attempt 001's readOnly episode showed. Recast it as a non-terminal processing state, `SCORING_PENDING_QUALIFIED_ENVIRONMENT`:

- evidence is frozen;
- the scorer is re-run unchanged once its known-answer test passes in a qualified profile;
- the run then receives its one class.

It never consumes or releases a claim, and it never appears in the consequence table. The draft's clause "if discovered before owner claim, no marker is consumed" belongs to C3's pre-claim harness check, not to scoring.

**Resulting policy dispositions:** one claimed run yields exactly one of `INVALID`, `REOPEN`, `AMEND`, `PASS_WITH_SELECTION`, plus the `NOT_RUN` row from C5. Nothing else.

**Required tests:** scorer branch tests on synthetic raw records:

- A viable / B interrupted → AMEND or PASS (with G2 flag);
- A resolved not viable / B interrupted → INVALID (G1);
- both resolved not viable → REOPEN;
- nothing resolved (abort before the first proof) → INVALID (G1);
- integrity flag → INVALID regardless;
- C completion never changes the class.

### C3. In-trial verification must be tri-state, and the known-answer test must precede the claim

**Problem.** The draft places the synthetic known-answer test (KAT) only before *scoring*. But each burden trial's success, and its mechanical endpoint, are decided by **in-trial local VERIFY** in the owner run.

- In the frozen `harness.py`, `verify()` catches `OSError` and returns `False`. A verifier environment failure is therefore indistinguishable from a bad owner proof.
- If the owner's run environment had the temporary-file problem that hit the scorer, every valid owner proof would be recorded as an INVALID trial. That is an irreversible false owner failure under a consumed claim.
- The draft's §8 guarantee ("Preflight problems do not silently become owner signature INVALID") holds for the scorer but not for the harness.

**Correction.**

1. `verify()` returns `VALID`, `INVALID` or `VERIFIER_ERROR`. `INVALID` is reserved for a completed cryptographic or structural rejection. Any exception, temporary-file failure, missing tool or unexpected subprocess condition is `VERIFIER_ERROR`.
2. An in-trial `VERIFIER_ERROR` stops the run with `attempt_integrity_failure=true` and reason `VERIFIER_ENVIRONMENT`, giving INVALID under C2 and C5's instrument-defect route. It is never recorded as owner proof failure. The proof bytes, if any, are preserved for later re-verification.
3. Immediately **before** creating the claim, in the same process and environment that will run the trials, execute the frozen KATs:
   - a valid SSHSIG and a mutated SSHSIG;
   - a valid ES256 WebAuthn assertion verification and a mutated one, through the Node RP verifier;
   - a temporary-directory create/destroy round trip.
   Any failure aborts before the claim. No marker is consumed and no owner-sensitive action has occurred.
4. Keep the scorer KAT as the draft specifies, feeding C2's `SCORING_PENDING_QUALIFIED_ENVIRONMENT`.

**Required tests:**

- forced temporary-directory failure during in-trial verify gives `VERIFIER_ERROR`, never a trial `success=false`;
- the pre-claim KAT failure path creates no marker file;
- KAT vectors are frozen by hash.

### C4. Statement identity: enforce structurally, not by exhaustive pre-computation (resolves B03)

**Problem.** Draft §2.7 requires prequalifying "all valid successor candidate statements for the three possible decisions on ordinary S01/S02/S03/L01 and the three security proofs P0/P5/P6" before freeze. That is infeasible for P5 and P6.

- The V02 rotation and recovery envelopes embed the target signer members' public IDs in the effect text: "Rotate SIGNERS-P01-V1 -> SIGNERS-P01-V2; PRIMARY: <target public_id>; …".
- Under the draft's own §2.4, those keys are created only after the claim. Their statements, and so their digests, do not exist at freeze time.

The exhaustive digest comparison is also redundant. Once `context` and the acceptance-ID prefix change, no successor statement can equal an Attempt-001 statement except through a SHA-256 collision.

**Correction.**

1. **Primary mechanism (structural, enforced by VERIFY).** The frozen successor VERIFY rejects any statement whose `context` is not exactly the frozen successor context, whose `project_id` is not the frozen synthetic project, or whose `acceptance_id` lacks the frozen successor prefix.
   - The frozen V02 `verify()` checks field set, types and digest syntax but **not** the context value. The successor adds this check.
   - Old-context statements then fail VERIFY even if someone re-signs them with a fresh key. This is the real cross-attempt replay barrier, and a single negative test proves it.
2. **Golden vectors.** Freeze full vectors (envelope, view, statement, digests) for every *key-independent* event: P0 and S01/S02/S03/L01 for each decision value. Freeze *templates* for P5 and P6 with placeholder member IDs, plus full vectors instantiated with fixed synthetic test keys.
3. **Secondary check (defense in depth, runtime).** Derive the old-statement digest set mechanically and locally from Attempt-001 public evidence. Commit only its element count and the SHA-256 of the sorted, newline-joined set (privacy-preserving, per Research 525). Before each owner invocation, the harness asserts that the statement digest is not in the set.
4. **Key-identity check.** The fresh-key public-ID inequality against Attempt 001 stays local and non-published, as the draft says. Its realistic purpose is catching an owner accidentally copying old key files into the new directory, not cryptographic collision. The draft's honest provenance limit in §2.5 is correct. The precise claim is: "keys were produced by harness-invoked `ssh-keygen` after the recorded claim, as observed by the harness". Nothing stronger.
5. **Wording fix in §3, T1.** The draft says "Both envelope_digest and shown_digest bind the exact rendered proposal." Under AC-1, `envelope_digest` binds the **canonical envelope**, which is semantic payload and not rendering. `shown_digest` binds the **rendered bytes**. Freeze the precise sentence, because exact-statement binding semantics depend on it.

**Required tests:**

- an old-context statement with a valid fresh-synthetic-key signature fails VERIFY;
- an Attempt-001-format acceptance ID fails;
- a statement in the old-digest set is refused before invocation;
- the P5/P6 templates instantiated with synthetic keys reproduce the frozen vectors;
- the cross-project statement is rejected.

### C5. Make the stopping rule finite

**Problems in the policy JSON.**

- `claim_cap.exception_conditions` lists four conditions without saying whether they are all required or alternatives. Read as alternatives, "new_unreused_attempt_identity" alone would authorize Attempt 003.
- There is no absolute numeric bound. Each exception is admitted by "a genuinely different falsifiable mechanism hypothesis", so the rule is finite only if every future hypothesis is genuinely new. That is the forking-paths risk the rule exists to prevent.
- "INVALID → exception only after new hypothesis" does not fit an *instrument* defect (for example, C3's `VERIFIER_ENVIRONMENT`). There the hypothesis is unchanged and the instrument failed.
- There is no row for the owner declining Attempt 002 altogether.

**Correction.**

1. `exception_conditions` is explicitly `ALL_REQUIRED`.
2. **Absolute cap:** at most two claims in this successor family (Attempt 002 plus at most one exception). Any further P01 owner trial requires a new preregistration record that amends Research 513 §5, not a policy exception.
3. **Split INVALID by cause:**
   - `INVALID_INSTRUMENT` (substantiated harness or verifier defect, or G1 incompleteness): one repaired attempt may be owner-authorized under the cap, with the defect, repair and unchanged hypothesis disclosed.
   - `INVALID_INTEGRITY` (secret exposure, post-observation tuning, evidence tampering): stop. Any continuation goes through the new-preregistration route.
4. **Add `NOT_RUN`:** if the owner declines or defers, P01 remains Attempt 001 AMEND, and the physical-target decision must handle AMEND explicitly under Research 513 §5.9.
5. **Owner approval ordering (B05).** Obtain owner approval of the stopping policy **before the contract freeze**, not only before the claim. The policy determines scorer branches (C2), so the frozen scorer must implement an approved policy. A separate explicit owner decision to start Attempt 002 remains required after qualification.

## 3. Assessment of the remaining review blockers

| Draft blocker | Assessment |
|---|---|
| B01 unlock classifier | Resolved by C1. Drop the classifier requirement. |
| B02 taxonomy | Resolved by C2: no fifth class, no unscored disposition. |
| B03 old/new statements | Resolved by C4: structural primary, digest set secondary. |
| B04 WebAuthn preflight | **Agree with the draft's scope.** It is a separate server mode with no registration or assertion routes and a static page that makes no `navigator.credentials` or `PublicKeyCredential` references, checked by a source-level test that greps the served page and server code for the forbidden API names. Add two things: (a) record the browser user agent and launch method in the pre-claim preflight receipt, and use the **same** launch method after the claim, because `webbrowser.open` opens the default browser and passkey storage differs between Chrome and Edge profiles; (b) the post-claim auto-launch must happen only after the RP readiness check, and the literal URL is always printed. |
| B05 consent | See C5.5. The authorization package must state: which changes are result-informed (unlock invocations, T3 cues, context/ID change, G1/G2); expected owner time per arm; that fresh keys are created on the owner machine and their later disposal is the owner's; that a residual discoverable WebAuthn credential may remain in the owner's authenticator after the attempt; the C2 rule that an abort is still scored; and the C5 cap. |
| B06 partial arms | Resolved by C2 (G1/G2). |
| B07 abort model | **Agree: no cross-process resume.** Further recommend **dropping the optional Ctrl+C confirmation handler entirely** for this attempt rather than leaving it "considered if qualified". It adds a Windows native-child test matrix for a convenience that browser auto-launch already makes unnecessary. Same-process pauses are a plain "press Enter to begin Arm B" prompt outside timed events. **Make the A→B dependency explicit:** B's P6 uses the Attempt-002 Arm-A recovery key, so if A setup never produced that key, B control 12 is `FAIL / unexecuted: recovery member absent`, not skipped. |
| B08 R1 tracking | Agree. |
| B09 P03 order | Agree with Research 525: design may proceed in parallel, and any scored-order change requires a prospective amendment before the affected result. |

## 4. Non-blocking corrections (recommended before freeze)

1. **Interaction count is owner-reported in V02.** `owner_measurements()` asks the owner to type "User-visible interactions after display". The draft says unlock attempts "count as user-visible interactions", but that cannot be guaranteed by self-report. Record a harness-computed `mechanical_interaction_floor` (decision entry + credential invocations + retry choices; for B, assertion ceremonies) beside the owner-reported value. Gates do not use interaction count, so this is evidence quality only.
2. **Hash-link the snapshots.** This is not for resume. Each successor snapshot should carry `previous_snapshot_sha256` (the exact file bytes of the prior snapshot), and the claim record should carry the frozen-artifact hashes including the T3 string table. That makes deletion or edit of an intermediate snapshot detectable from the final one at near-zero cost. The V02 index-by-file-count design gives exclusive create but no linkage.
3. **WebAuthn timing landmarks.** Mirror §6's SSH landmarks with browser-monotonic `assertion_call_started` and `assertion_call_resolved`. Keep the draft's correct refusal to stitch browser and Python clock origins.
4. **T3 text.**
   - Replace "Do not use Ctrl+C to copy" with positive guidance: "The page opens automatically. If it does not, type the address shown into your browser. Pressing Ctrl+C in this window stops the attempt."
   - Add the C1 retry prompt and an abort sentence: "To stop the attempt, press Ctrl+C at any prompt; a stopped attempt is still recorded and scored."
   - The other proposed lines are neutral and acceptable.
5. **Identifier hygiene.**
   - The draft names "protocol R0-P01-V02" next to "contract R0-P01-CONTRACT-V03". "R0-P01-V02" collides visually with V02 contract artifacts, and it implies that Research 513 itself changed.
   - Recommendation: if G1 is adopted as a family-level interpretation, create a short Research-513 interpretation record and name the protocol accordingly, for example `R0-P01-V01-I1`. Otherwise keep protocol `R0-P01-V01` and change only the contract and attempt identifiers.
   - The result `protocol` field and scorer identity must use the frozen choice.
6. **Event names in evidence.** Remove hard-coded `ATTEMPT_001_*` strings and the WebAuthn `user.id` `R0-P01-001-B` from successor code paths, and add a test asserting that no `001` attempt literal appears in the successor harness outputs.

## 5. Freeze-readiness test matrix (additions to draft §10)

All tests use synthetic credentials and run on the owner's target Windows/OpenSSH/Node/browser versions where noted:

1. **C1 unlock matrix** (§2, C1), including the manual native-prompt visibility receipt on the target build.
2. **C2 scorer branch matrix**, including G1/G2 and the `SCORING_PENDING_QUALIFIED_ENVIRONMENT` re-run producing a byte-identical derived output.
3. **C3** forced verifier failure gives `VERIFIER_ERROR` (never trial failure); a pre-claim KAT failure creates no marker.
4. **C4** old-context, old-prefix and old-digest-set refusals; P5/P6 template instantiation vectors.
5. **C5** policy JSON schema test: exceptions `ALL_REQUIRED`, cap = 2, `NOT_RUN` present, INVALID split.
6. **B04** forbidden-API source scan of the preflight mode; a recorded launch-method and user-agent receipt.
7. **§4.2 snapshot chain:** deleting or editing any intermediate snapshot is detected from the final snapshot.
8. **A complete synthetic dry run** of A→B→C with test keys and a virtual or platform test authenticator where available, producing a raw file the frozen scorer classifies as expected. This is the one end-to-end check that the drafted pieces compose.

## 6. What the draft gets right and must keep

- Attempt 001 stays immutable AMEND, with the corrected hash from Validation 216.
- No pooling. All 13 controls with zero misses. 1/2/4/30 effects. 60/120/120-second gates with only the V02 infrastructure receipt. The volume gates, A/B selection and B tie-break, and C's ineligibility.
- One decision and one statement per event; the preview inside the mechanical timer.
- Honest WebAuthn opacity (`platform_uv_attempt_count=null`, no parity claim).
- The T1/T2/T3 separation, with no variable T2 in this synthetic benchmark.
- No cross-process resume.
- Fresh post-claim keys with an honest provenance limit, and local-only comparison with old public IDs.
- The claim cap counts claims, not completed runs.
- `RESULT_INFORMED_PROSPECTIVE_CHANGE` labelling.

## 7. Architecture

Nothing in the draft or this review bears on GOVERNED_LEDGER_KERNEL_V02, AC-1 through AC-6, or THIN_CENTRED_HYBRID_V03. C4's VERIFY-side `context` check is the probe instantiation of the existing domain-separation field, not a new semantic. G1 is a scoring interpretation, not an architectural one. No architecture question is reopened. R0-P02 PASS; R0-P03 pending; Specification 028 unchanged; no physical target selected.

```text
MC0030_MESSAGE021=CLAUDE_V03_DRAFT_REVIEW
DISPOSITION=AMEND_DRAFT_BEFORE_FREEZE
BLOCKING=C1_NO_CLASSIFIER_OWNER_CONFIRMED_REINVOCATION;C2_SCORE_EVERY_CLAIM_G1_G2;C3_TRISTATE_VERIFY_PRECLAIM_KAT;C4_STRUCTURAL_STATEMENT_IDENTITY;C5_ABSOLUTE_CAP
ARCHITECTURE=NOT_REOPENED
ATTEMPT_002=NOT_AUTHORIZED
NEXT=CHATGPT_RECONCILIATION
```
