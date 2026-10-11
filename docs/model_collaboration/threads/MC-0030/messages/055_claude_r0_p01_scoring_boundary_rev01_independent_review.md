# MC-0030 Message 055: Claude independent review of the F1 scoring-boundary matrix REV01

```text
Thread                  MC-0030
Message                 055
Author / reviewer       Claude / claude-04 (independent clause reviewer; not scorer or blind oracle author)
Coordination branch     v1-source-vault-bootstrap-resume
Parent HEAD             c75c346b17f3f420b4eb58d73dcefda775dfdd63 (Checkpoint 873)
Request                 MC-0030 Message 054
Subject                 Research 537; R0_P01_F1_SCORING_BOUNDARY_CANDIDATES_REV01_UNFROZEN.json (17 cases);
                        Validation 226; scripts/check_r0_p01_scoring_boundary_candidates.py and its tests
Verdict                 AMEND_REV01_TARGETED
Authority               Review record only. No source, policy, script, test, routing or evidence edit. F1/F2 unfrozen.
```

## 0. Verification

- The branch head was `c75c346b…` as expected.
- The REV04 contract and policy files hash to `9160a30c…` and `9b5bbc4d…`, the exact bytes bound by the B01 and B02 acceptance records (B01 L0015–L0016; B02 L0015–L0016). The inventory carries the same values. There is no source drift.
- `check_r0_p01_scoring_boundary_candidates.py` passes (17 cases: 12 SOURCE_DETERMINED, 5 CANDIDATE_BLOCKED), and all 9 of its unit tests pass. I treat that as structural evidence only; see §5.
- Each case was compared against the REV04 contract and policy, the B01/B02 records, the V01 contract and V02 addendum, and my own audit Messages 033 and 035–052. The 18 pending-register rows tagged B05-A1, B07-A3, B08-A1 or B11-A1 were reconciled against the cases' citations.
- `R4:` = REV04_CONTRACT line; `P:` = REV04_POLICY leaf; `V01:` / `V02:` = predecessor lines.

**Exception consequences used throughout** (B02 items 3–5; R4:L0241–L0242; P:`cases[4..6].next`):

| Class | Exceptional successor claim |
|---|---|
| INVALID_INTEGRITY | Never |
| INVALID_INSTRUMENT | Possible on a repaired defect, keeping the unchanged hypothesis (the only favorable exception path) |
| AMEND / REOPEN / INVALID_INCOMPLETE | Only with a genuinely new falsifiable hypothesis. P:`cases[5].next` states NO_INSTRUMENT_REPAIR_EXCEPTION for INCOMPLETE |

So the exception-sensitive errors are false INSTRUMENT (wrongly favorable) and false INTEGRITY (wrongly forfeits all exceptions). False REOPEN versus INVALID_INCOMPLETE leaves exception rights unchanged, but it reverses the scientific conclusion: REOPEN reopens the owner-authenticity assumptions (R4:L0249).

## 1. Verdict and summary

**`AMEND_REV01_TARGETED`.**

- I found no contradiction in the B01/B02-approved text that only an owner can resolve. No case needs to be rejected.
- Five matrix-level problems need amendment before any expected-output vectors are written:
  1. **Arm-level labels slide toward global class claims.** Several SOURCE_DETERMINED cases name an INVALID_* class while their precondition omits a load-bearing provenance fact: Windows process-group isolation, the HARNESS_RECORDED origin of a flag, or delivery of the challenge to the client.
  2. **Predecessor rules can't be cited.** B05-A1 omits the inherited rule most relevant to S1-04: V01:L0231 makes "cannot return an assertion bound to the exact challenge" NOT_REALIZABLE. The guard's regex forbids citing V01 or V02 units at all.
  3. **Mandatory cross-family situations are missing** (§3). The most serious is a Ctrl+C racing the third native SSH invocation. That can be recorded as budget exhaustion, a terminal event, instead of an in-flight attempt abort, which produces false COMPLETED evidence and potentially a false REOPEN.
  4. **Two blocked cases are over-blocked.** S4-01 is representation-only: B01 item 2 itself says "budget exhaustion". S2-03 is mostly decided by R4:L0203 and L0206 once evidence sufficiency is fixed.
  5. **The guard and tests have green paths that mask the gaps** (§5). Separately, the pending-register reproducibility test fails on an LF checkout because it hashes CRLF working-tree bytes.

**Per-case tally:** 8 CONFIRMED_AS_STATED, 9 AMEND_PRECONDITION_OR_CONCLUSION, 0 REJECT_UNSUPPORTED, 0 NEEDS_OWNER_INTERPRETATION. Two optional owner-interpretation questions arise only if the task owner wants a *different* outcome from what the approved text gives (§4).

## 2. Per-case decision record

| Case | Determination in REV01 | Review status |
|---|---|---|
| S1-01 | SOURCE_DETERMINED | CONFIRMED_AS_STATED |
| S1-02 | SOURCE_DETERMINED | AMEND_PRECONDITION_OR_CONCLUSION |
| S1-03 | SOURCE_DETERMINED | CONFIRMED_AS_STATED |
| S1-04 | CANDIDATE_BLOCKED | AMEND_PRECONDITION_OR_CONCLUSION |
| S1-05 | CANDIDATE_BLOCKED | CONFIRMED_AS_STATED |
| S2-01 | SOURCE_DETERMINED | CONFIRMED_AS_STATED |
| S2-02 | SOURCE_DETERMINED | AMEND_PRECONDITION_OR_CONCLUSION |
| S2-03 | CANDIDATE_BLOCKED | AMEND_PRECONDITION_OR_CONCLUSION |
| S2-04 | SOURCE_DETERMINED | AMEND_PRECONDITION_OR_CONCLUSION |
| S3-01 | SOURCE_DETERMINED | AMEND_PRECONDITION_OR_CONCLUSION |
| S3-02 | SOURCE_DETERMINED | AMEND_PRECONDITION_OR_CONCLUSION |
| S3-03 | CANDIDATE_BLOCKED | CONFIRMED_AS_STATED |
| S3-04 | SOURCE_DETERMINED | AMEND_PRECONDITION_OR_CONCLUSION |
| S4-01 | CANDIDATE_BLOCKED | AMEND_PRECONDITION_OR_CONCLUSION |
| S4-02 | SOURCE_DETERMINED | CONFIRMED_AS_STATED |
| S4-03 | SOURCE_DETERMINED | CONFIRMED_AS_STATED |
| S4-04 | SOURCE_DETERMINED | CONFIRMED_AS_STATED |

### B05-A1: capability evidence

**S1-01 — CONFIRMED_AS_STATED.**
- *Basis:* R4:L0108 and V02:L0264 say owner cancellation or timeout during registration is SETUP_INTERRUPTED. V02:L0284 says unresolved realizability is null, never NOT_REALIZABLE. P:`evidence_state.not_realizable` and P:`guards.G1_REOPEN` complete the chain.
- *Representation note:* "owner refusal" must mean refusing setup or registration, not a recorded non-ACCEPT P0 decision. The latter is the enumerated terminal outcome `P0_NON_ACCEPT_DECISION` (P:`evidence_state.terminal_outcomes[2]`) and *does* count toward COMPLETED. The condition "P0 terminal evidence absent" already excludes it, but the slug invites misreading.
- *Second note:* the qualification boundary is right not to infer INVALID. If Arm A is eligible, the result is PASS with G2 (P:`guards.G2_UNCONTESTED_SELECTION`), not INVALID.

**S1-02 — AMEND_PRECONDITION_OR_CONCLUSION.**
- *Basis:* R4:L0108 says the assertion is consumed on the first response, cancel *or timeout*. R4:L0151, L0154 and B01 item 2 make that a terminal no-proof event. P:`webauthn_assertion_failure_table.NotAllowedError_or_owner_cancel_or_timeout.requires`.
- *Adversarial scenario:* the RP issues the P0 challenge, but the page script fails or the tab is lost before `navigator.credentials.get()` runs. After 120 s the RP records a timeout and consumes the pending record.
  - By the literal reading this is a "consumed" assertion, so WEBAUTHN_ASSERTION_NOT_COMPLETED becomes event-terminal.
  - That counts toward COMPLETED. With Arm A non-viable and resolved, G1 gives **REOPEN**, where the owner never saw a ceremony.
- *Required amendment (technical, no owner needed):* the precondition must require durable evidence that the ceremony was *issued to and invoked by the client*: an RP-side delivery record plus a client get() invocation receipt. An RP-side expiry without any client invocation receipt is not terminal. It stays INCOMPLETE, or maps to the instrument table if a client or RP error receipt exists (P:`…other_DOMException_or_client_RP_error.outcome`; R4:L0154 "untrusted event flags do not silently become completed").
- *Separate risk (not a defect in the case):* as far as I know, browsers also return NotAllowedError for causes other than the owner, such as no matching credential or, in some implementations, an unfocused document.
  - B01 item 2 accepts NotAllowedError as owner-equivalent, so F1 must not reclassify these cases unilaterally.
  - F1 should record disclosure-only discriminators: browser-monotonic get() start and reject times, focus state at the call, and allowCredentials match. See owner question OI-1 in §4.

**S1-03 — CONFIRMED_AS_STATED.** P:`evidence_state.incomplete` explicitly covers "NotAllowedError without a durable issued-and-consumed assertion receipt", and R4:L0154 says "a missing RP receipt cannot be inferred as cancellation". The higher-precedence note is correct. If the browser–RP discrepancy has a source-labelled RP error receipt, the instrument table applies; if the evidence is merely missing, scorer-derived provenance rules apply (R4:L0172).

**S1-04 — AMEND_PRECONDITION_OR_CONCLUSION.** It stays blocked, but the sources decide more than the case concedes, and its source basis is incomplete.
- *Missing anchors:*
  - V01:L0231 ("cannot return an assertion bound to the exact challenge → NOT_REALIZABLE") and V01:L0223 (missing response methods → NOT_REALIZABLE). Both are open B05-A1 pending rows.
  - R4:L0112 ("NotSupportedError … can support NOT_REALIZABLE only under the frozen capability predicate").
  - P:`webauthn_assertion_failure_table.NotSupportedError.event_terminal` = **false**.
  - P:`…NotSupportedError.proof_viability_receipt`, also an open pending row.
- *What the sources already determine, absent the frozen receipt:*
  - B cannot be NOT_REALIZABLE (P:`evidence_state.not_realizable`: "NotSupportedError only with frozen independent capability receipt").
  - The P0 event is not terminal (`event_terminal:false`), so B cannot be COMPLETED.
  - B's evidence_state is therefore the residual INCOMPLETE, and **REOPEN is source-excluded** for that attempt (P:`guards.G1_REOPEN`).
  - INSTRUMENT is *not* entailed, because NotSupportedError is a named, not an "other", DOMException (R4:L0201), and P:`raw_flag_schema.default_missing_flags` forbids a favorable default.
- *Genuinely open:*
  - (a) The receipt grammar, shared with S1-05.
  - (b) Whether a receipt obtained *after a verified ES256/UV registration in the same claim* may support NOT_REALIZABLE. V01:L0231 points toward yes for real assertion inability. A just-demonstrated registration capability makes the case anomalous.
- *Adversarial scenario:* B registers successfully. The browser profile or policy then changes and get() throws NotSupportedError. A self-asserted local "capability receipt" makes B NOT_REALIZABLE, and with A completed but non-viable, G1 gives **REOPEN** (false negative architecture evidence). If A is instead eligible, the result is PASS **without** the G2 `OTHER_ARM_INCOMPLETE` disclosure, which INCOMPLETE would have triggered.
- *Recommendation (technical, inside R4:L0112's delegated "frozen capability predicate"):* NOT_REALIZABLE may rest only on capability evidence produced by a frozen, replayable probe. That probe must be independent of the owner ceremony and repeatable within the same claim. A post-registration NotSupportedError without such a probe stays INCOMPLETE. The owner should be told that this is the chosen predicate.

**S1-05 — CONFIRMED_AS_STATED** as a blocked hypothetical. Add V01:L0223 and V01:L0231 to `source_basis`. The receipt must name its producer, browser/OS/authenticator scope, phase (registration or assertion), monotonic and UTC binding, and claim/attempt ID. It also needs negative cases for refusal, timeout, cancel, not-visited, expired and absent receipt (Research 537 §2 lists these; the guard does not enforce them).

### B07-A3: SSH pre-sign checks

**S2-01 — CONFIRMED_AS_STATED.**
- *Basis:* R4:L0066 requires "the originally registered public ID". R4:L0206 says old/new key identity → INTEGRITY. P:`raw_flag_schema.flag_origin.integrity.attempt_integrity_failure` = HARNESS_RECORDED. Precedence 1 applies regardless of the other arm.
- *Evidence-standard note:* "independently proven replaced" must exclude a read failure, such as a file locked by antivirus or cloud sync. The precheck must record *content mismatch* separately from *unreadable*. Otherwise the same symptom yields INTEGRITY and forfeits every exception (B02 item 3).

**S2-02 — AMEND_PRECONDITION_OR_CONCLUSION.** The same physical fault (a missing or broken OpenSSH binary) has three source routes, and the case asserts only one:
- (i) R4:L0066 checks the pinned executable path and version **before** invoking, and says "any failed check is terminal". No terminal outcome is enumerated for this, so the arm becomes INCOMPLETE and the class is **INVALID_INCOMPLETE** unless a flag is raised.
- (ii) R4:L0203 covers launch failure after the claim: INSTRUMENT, which in practice can only be `harness_exception_with_intact_chain`, a SCORER_DERIVED flag that requires the site to be in the §8.6 inventory (R4:L0213). That gives **INVALID_INSTRUMENT**, the favorable exception path.
- (iii) The binary launches but exits nonzero with no signature. R4:L0068–L0069 make this NO_PROOF_EMITTED and owner R/S, and L0069 explicitly says "a deterministically recurring non-secret tool failure may exhaust the bounded budget". That is a **terminal no-proof event**, which counts toward COMPLETED and can feed **REOPEN**.

The conclusion holds only for route (ii). Amend the precondition to "process creation fails with no exit status, detected at launch, and the site is in the §8.6 inventory". F1 must fix which check detects a missing or replaced binary first. Detecting it at precheck without a flag leads to INCOMPLETE; detecting it at launch leads to INSTRUMENT. That choice is exception-relevant, so it needs independent review, but it is technical (R4:L0213 delegates site disposition).

Route (iii) is approved text. The mitigation is the preclaim KAT with the same ssh-keygen (R4:L0120), plus disclosure-only per-invocation durations. It is not a reclassification.

**S2-03 — AMEND_PRECONDITION_OR_CONCLUSION.** It should stay blocked, but narrowed. The seven L0066 checks are mostly source-mapped:

| L0066 check | Source disposition |
|---|---|
| Registered public ID | INTEGRITY (L0206 "old/new key … identities") |
| Encrypted header | INTEGRITY (L0206 "public key header"; see S2-04 for the definition problem) |
| No agent caching | INTEGRITY (L0206 "agent change") |
| Statement byte equality | INTEGRITY (L0206 "untrusted view/statement") |
| Trust-root, member or role state | INTEGRITY (L0206 "unauthorized trust-root or signer-set membership") |
| Pinned executable | INSTRUMENT (L0203) |
| No existing `.sig` | Usually a downstream symptom of PARTIAL_OR_INCONSISTENT_OUTPUT (L0068, L0205) |

- *What remains open:* only evidence sufficiency, meaning proven violation versus unreadable or indeterminate.
- *Adding a new terminal outcome such as `PRECHECK_FAILED` to the approved list* would enlarge COMPLETED and enable REOPEN. That changes B02-approved policy bytes, so it would need owner approval. I recommend against it: a precheck failure without a flag stays INCOMPLETE.
- *False-INTEGRITY scenario:*
  - After postclaim keygen, the owner habitually runs `ssh-add`, so the Windows agent service holds the new key before P0.
  - The no-agent check fails, and by L0206's literal "agent change" this is INVALID_INTEGRITY, with no exception ever (B02 item 3).
  - Whether a pre-existing agent load (as opposed to a change during the attempt) is an L0206 "change" is unresolved. The approved text points to INTEGRITY.
  - F1 should not soften it. The owner authorization package must disclose this consequence, and F1 should define the check site and evidence (R4:L0254 disclosure duty).

**S2-04 — AMEND_PRECONDITION_OR_CONCLUSION.** R4:L0066 requires a "verified **encrypted** native-key header", which is a property check, while the case's "altered" reads as byte change. L0206's "public key header" refers to the *public* key; mapping it to the private-key encryption header is an inference.
- *Adversarial scenario:* between events the owner runs `ssh-keygen -p` to change the passphrase. The private-key file bytes change (new KDF salt), but it stays encrypted with the same public key.
  - A byte-equality check yields INVALID_INTEGRITY (no exception).
  - The property check passes.
- *Amendment:* define "altered" as a violation of the frozen property: unencrypted, wrong key type, or a public key that differs from the registered ID. Whether a passphrase change mid-attempt is permitted is not stated anywhere. Deciding it is technical if it is treated as non-violating; prohibiting it needs owner disclosure.

### B08-A1: Ctrl+C versus Node/RP fault

**S3-01 — AMEND_PRECONDITION_OR_CONCLUSION.** The conclusion is right only when the ordering is established **within the harness stream**: the abort is recorded, the harness then initiates cleanup, then it observes the child exit. It also requires verified console isolation of the RP (R4:L0112's `CREATE_NEW_PROCESS_GROUP` "only if target Windows test verified", P:`browser_node_interrupt.candidate_process_isolation`).
- *Adversarial scenario (no isolation):* Ctrl+C reaches Node and Python together. The harness, blocked in an RPC read, receives a connection reset *before* Python raises KeyboardInterrupt.
  - It records an RPC failure "observed before any owner KeyboardInterrupt/abort was recorded" (P:`raw_flag_schema.node_rp_failure`, temporal), so `node_rp_failure` is true.
  - The class becomes **INVALID_INSTRUMENT**, a favorable repair exception for an owner abort, which B02 item 5 and R4:L0242 forbid ("cannot be relabelled as instrument defect").
- *Amendment:* make verified isolation an explicit precondition, and state that observation order is the harness's own record order, not occurrence order. Without isolation, the case belongs to S3-03.
- *Minor:* in the F1 test text, "other arm resolved" is unnecessary. Either arm INCOMPLETE gives INVALID_INCOMPLETE if neither arm is viable (P:`guards.scorer_precedence[2]`).

**S3-02 — AMEND_PRECONDITION_OR_CONCLUSION.** `integrity.node_rp_failure` is **HARNESS_RECORDED** (P:`raw_flag_schema.flag_origin.integrity.node_rp_failure`). A "trusted RP process-failure receipt" from the RP's own stream cannot set it, and the scorer cannot derive it.
- *Scenario:* the owner closes the console window, which sends CTRL_CLOSE_EVENT to every process on that console. The harness dies with no abort record, and RP receipts show abnormal termination.
  - A scorer that derived `node_rp_failure` from the RP stream would yield a favorable INSTRUMENT.
  - Under the flag-origin rule, the correct result is INCOMPLETE.
- *Amendment:* require a harness-recorded fault receipt, ordered before any abort record in the harness stream, with isolation verified.
- *Interaction worth a vector:* a genuine RP fault *after* Arm A is already eligible still gives INVALID_INSTRUMENT at precedence 2, overriding PASS, and opens the repair-exception path. That is approved, but it is the highest-value false-favorable target, so the evidence standard above matters most there.

**S3-03 — CONFIRMED_AS_STATED** as blocked. The sources narrow it:
- R4:L0215 limits the outcome to "a specific `instrument_failure` or `INCOMPLETE` outcome … by a frozen rule, never a discretionary downgrade to integrity".
- R4:L0242, P:`cases[5].next` and P:`raw_flag_schema.default_missing_flags` all reject favorable instrument relabelling of an abort.

Choosing **INCOMPLETE on unorderable races** is therefore within L0215's delegation, so an expert technical decision can make it, provided the rebuttal standard of S3-02 is frozen (a harness-recorded fault ordered before the abort in the harness stream, with isolation verified). That rule must not erase a genuinely proven pre-abort fault. Choosing **INSTRUMENT on ambiguity** would widen exception eligibility against the B02 anti-relabelling clause and should not be adopted without an explicit owner interpretation (OI-2). My earlier "prefer INCOMPLETE" remains a reviewer recommendation, not approved policy.

**S3-04 — AMEND_PRECONDITION_OR_CONCLUSION.** "Count only actually evidenced terminal assertion" leaves open a recovered receipt of a *successful* assertion whose in-run VERIFY never happened.
- If a scorer later verifies it as VALID, the event becomes terminal VALID, and the arm can become proof-viable. That turns INVALID_INCOMPLETE into AMEND by inventing a completed proof assessment after the process ended.
- R4:L0094 makes the C13 interval end only at in-run VERIFY, R4:L0114 forbids cross-process resumption, and R4:L0128 says an independent re-check "must never change the already consumed attempt's classification". Read together, only terminal **no-proof** receipts (WEBAUTHN_ASSERTION_NOT_COMPLETED) and in-run VERIFY results may count.
- *Amendment (technical):* a recovered success receipt without in-run VERIFY is not terminal and leaves the event INCOMPLETE. Its proof bytes are preserved for disclosure only.

### B11-A1: SSH proof budget

**S4-01 — AMEND_PRECONDITION_OR_CONCLUSION.** It should move from blocked to source-determined *representation-only*.
- R4:L0070 (`PROOF_NOT_CREATED`), R4:L0151 ("exhausted bounded unlock attempts"), R4:L0154 ("exhausted SSH unlocks"), P:`evidence_state.terminal_outcomes[4]` (`SSH_UNLOCK_BUDGET_EXHAUSTED`) and **B01 item 2** ("native SSH owner S/budget exhaustion is likewise terminal") all denote one predicate: index 3, nonzero exit and no signature, after explicit R at indices 1 and 2.
- A raw-token-preserving bijective alias neither enlarges nor shrinks the COMPLETED set, so no owner interpretation is needed. Canonicalize on the policy enumeration (the one P:`evidence_state.completed` references), and keep `PROOF_NOT_CREATED` as the raw contract site label.
- The alias must be refused when any of these hold: fewer than 3 per-call receipts; any call with a signature file or exit 0 (→ PARTIAL or VERIFY); a missing or non-R choice after call 1 or 2 (→ OWNER_S_EVENT_STOP); any 4th-call record (→ integrity provenance); or **any owner interrupt overlapping call 3** (§3 X1).
- Under L0069, a recurring tool failure may legitimately reach this state; disclose per-call durations.

**S4-02 — CONFIRMED_AS_STATED.** R4:L0060, L0069 and L0197 say only exact `R` retries. *Disclosure note:* "exact R" means a mistyped `r` or a trailing space ends the event permanently. That is approved, so the T3 prompt text and the owner package should state it.

**S4-03 — CONFIRMED_AS_STATED.** R4:L0068 and L0205 apply. Without a separately recorded identity-breach flag it is not integrity.

**S4-04 — CONFIRMED_AS_STATED.** R4:L0154 and L0172 apply. A free-text label is not a receipt, and missing required evidence routes to scorer-derived provenance rules, never to a favorable instrument path.

## 3. Missing mandatory, scoring-sensitive cross-family situations

The 17 cases omit these, and each can flip the class. I recommend adding them as candidate cases, not as oracles.

**X1 — Ctrl+C racing the third SSH invocation (B08 × B11 × G1).**
- R4:L0067 requires an inherited real console, so ssh-keygen receives Ctrl+C. It exits nonzero with no signature. If the harness records the exit before KeyboardInterrupt surfaces, call 3 is recorded as budget exhaustion, a terminal event.
- P:`attempt_terminal_vs_event_terminal.ctrl_c_or_crash` requires "event_in_flight INCOMPLETE".
- *Consequence:* false COMPLETED, and potentially a false **REOPEN** instead of INVALID_INCOMPLETE.
- R4:L0075 already demands the native-prompt Ctrl+C test. The scoring rule and vector are missing.

**X2 — NotAllowedError from non-owner causes, or RP-only timeout (B05 × G1).** See S1-02.

**X3 — Ctrl+C during snapshot promotion (B08 × integrity precedence).**
- R4:L0136 and P:`snapshot_evidence.write_protocol` depend on a Windows atomic no-overwrite rename that is still unqualified.
- If interruption leaves a malformed final-name file, the result is `provenance_mismatch` and **INVALID_INTEGRITY**, with no exception, where INVALID_INCOMPLETE was due.
- The class is safe only if the atomicity test passes. The vector must exist before freeze.

**X4 — False NOT_REALIZABLE suppressing G2 disclosure (B05 × G2).** See S1-04. Because PASS ends the family (B02 item 3), the G2 flag is the owner's only signal that the alternative arm was never assessed.

**X5 — Late instrument flag overriding an eligible arm (B08 × precedence).** See S3-02.

**X6 — Tool fault exhausting the SSH budget (B07 × B11 × G1).** See S2-02 route (iii).

**X7 — Arm C relevance.** P:`guards.G1_REOPEN.REOPEN_only_if_all_arms_evidence_state_in` says "all arms". C has no evidence_state, so this must be read as A/B (consistent with R4:L0156 and my earlier B11-R1). A vector should pin it.

**General.** All seven precedence rows need complete attempt-level vectors that fix the other arm's state, proof viability and every raw flag. Research 537 §6 acknowledges this.

## 4. Technical decision versus owner interpretation

**An expert technical decision can resolve these without the owner** (with independent review and disclosure):
- the S4-01 alias;
- the S2-03 site table, without adding terminal outcomes;
- the S2-02 detection-site choice;
- the S2-04 property-check definition;
- the S1-02 "issued-to-client" receipt requirement;
- the S3-04 no-post-hoc-VERIFY rule;
- the S3-01 and S3-02 isolation and harness-origin preconditions;
- the S1-04/S1-05 capability predicate, kept conservative;
- the S3-03 INCOMPLETE-on-unorderable-race rule with a frozen rebuttal standard;
- all of §3's vectors.

These clarify delegated freeze items (R4:L0112 "frozen capability predicate", L0213 site inventory, L0215 "frozen rule") or encode evidence requirements the approved text already states.

**Explicit, separately requested human interpretation would be needed only for:**
- **OI-1:** narrowing B01 item 2, so that a durably consumed NotAllowedError counts as owner no-proof only when presentation of the ceremony is evidenced. This changes the approved terminal set.
- **OI-2:** any rule resolving S3-03 races, or unclassified precheck failures, *toward* INVALID_INSTRUMENT. This widens the exception eligibility constrained by B02 item 4–5 and R4:L0242.
- **Optional OI-3:** softening L0206's literal INTEGRITY treatment of agent or header "change" (S2-03, S2-04). I do not recommend this. Disclose it instead.

None of these is required to proceed with the technical remediation.

## 5. Guard and test assurance gaps (not edited)

| # | Gap | Effect |
|---|---|---|
| V1 | The guard pins no per-case determination. Thresholds are ≥12 cases, ≥3 per gate and ≥4 blocked (script L0095). | The guard still PASSes with S3-03, the key B02 race case, deleted (4 blocked and 3 B08 cases remain), or with any blocked case relabelled SOURCE_DETERMINED provided ≥4 stay blocked. The pinning lives only in the test file (count and ID-subset asserts), so the standalone guard's PASS line in Validation 226 is weaker than stated. |
| V2 | The "blocked" marker is a keyword match on "cannot" / "require" / "unresolved" (script L0087–L0094), with no inverse check. | It does not discriminate. 3 of the 12 SOURCE_DETERMINED cases (S1-02, S1-03, S4-04) already contain those words. |
| V3 | `test_scoring_class_sensitive_cases_remain_blocked`, second assertion, is vacuous: no slug contains `INVALID_INSTRUMENT`. It is also logically inverted: it would *forbid* a blocked INSTRUMENT-slugged case. | Gives false assurance about INSTRUMENT handling. |
| V4 | `CONTRACT_REF` accepts only `REV04_CONTRACT-Lnnnn` (script L0025). | Predecessor V01/V02 units cannot be cited at all, so open B05-A1 rows V01_CONTRACT-L0223 and L0231 are structurally excluded. P:`…NotSupportedError.proof_viability_receipt` (an open row) is also uncited. There is no check that every open register row for a gate is either cited or explicitly dispositioned. |
| V5 | No machine-readable premise fields: other-arm state, proof viability, raw flags, isolation verified, flag origin, receipt producer. `test_source_determined_cases_do_not_claim_entire_scored_result` checks 4 substrings in 4 cases. | S2-01, S2-02, S2-04 and S3-02 name INVALID_* classes, and the S3-01 test text names one, with no structural premise check. |
| V6 | `accepted_decisions` is checked as strings only. | The guard never confirms that the B01/B02 records bind the hashed bytes. They do: B01 L0015–L0016, B02 L0015–L0016. |
| V7 | **The pending-register reproducibility test fails on an LF checkout.** | `test_r0_p01_pending_review_register.py::test_register_is_byte_reproducible_from_review_corpus` fails at `c75c346b`. Its `message_sha256` values are SHA-256 of *CRLF-converted* bytes: for Message 033, the committed LF bytes give `d46897a9…` while the register stores `f6f8a876…`, the CRLF variant. The register then disagrees with the repository's Git content on Linux or CI. Hash Git blob bytes (`git show HEAD:path`), as the inventory does, or normalize EOL. |

**Bounded hardening, for the task owner to implement if accepted:**
1. Pin case IDs and determinations in the guard.
2. Allow `V01_CONTRACT`, `V02_ADDENDUM` and `V01_CONTROLS` refs.
3. Require each open gate row to be cited or dispositioned.
4. Add explicit premise fields (`other_arm_state`, `raw_flags`, `isolation_verified`, `flag_origin`, `receipt_producer`). A case naming an attempt-level class must populate them.
5. Replace the keyword heuristic with an explicit `blocked_reason` field.
6. Fix or remove the vacuous assertion.
7. Fix the EOL basis of the register hashes.

## 6. Minimal prospective remediation plan

1. **REV02 of the matrix:**
   - Apply the 9 amendments.
   - Add X1–X7 as candidate cases.
   - Move S4-01 to source-determined representation-only.
   - Keep S1-04 (sub-question b), S1-05, S2-03 (evidence sufficiency) and S3-03 blocked.
2. **Technical decision records,** each independently reviewed:
   - the capability predicate;
   - the SSH precheck site table with evidence fields;
   - the RP ordering rule (harness-stream order, isolation precondition, INCOMPLETE default with a frozen rebuttal);
   - the terminal-token alias;
   - the no-post-hoc-VERIFY rule.
3. **Guard and test hardening** per §5.
4. **Owner package disclosures:** agent/`ssh-add` and passphrase-change consequences, exact-`R` input, NotAllowedError's coarse attribution, and the G2 dependence on correct NOT_REALIZABLE. Raise OI-1, OI-2 or OI-3 only if the task owner wants outcomes different from the approved text.
5. **Only then:** independently authored seven-row attempt-level vectors, then separately bounded scorer and blind-oracle work.

## 7. Attestation and boundaries

- **Reviewer: claude-04.** I read the cited source units directly and reproduced the guard, its tests and the register test at `c75c346b`. I did not author the matrix, guard, tests, scorer or oracle, and I will not author the scorer or blind oracle.
- Nothing here approves F1, modifies B01/B02, chooses an authority-dependent scored result or authorizes Attempt 002.
- The 55 pending audit rows remain UNRESOLVED. Only this message file was written.

```text
MC0030_MESSAGE055=SCORING_BOUNDARY_REV01_INDEPENDENT_REVIEW
VERDICT=AMEND_REV01_TARGETED
CASES=17;CONFIRMED=8;AMEND=9;REJECT=0;NEEDS_OWNER=0
HIGH_RISK=X1_CTRLC_THIRD_SSH_CALL;S1-02_RP_ONLY_TIMEOUT_REOPEN;S3-01_NO_ISOLATION_FALSE_INSTRUMENT;S1-04_POST_REGISTRATION_NOT_REALIZABLE;S2-03_AGENT_FALSE_INTEGRITY;X3_SNAPSHOT_ATOMICITY_FALSE_INTEGRITY
OWNER_INTERPRETATION_OPTIONAL=OI-1_NOTALLOWED_NARROWING;OI-2_INSTRUMENT_ON_AMBIGUITY;OI-3_SOFTEN_L0206
GUARD_GAPS=V1..V7;V7_PENDING_REGISTER_TEST_FAILS_ON_LF_CHECKOUT
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
