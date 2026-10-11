# MC-0030 Message 059: Claude independent review of the F1 site/receipt decision table REV01

```text
Thread                  MC-0030
Message                 059
Author / reviewer       Claude / claude-04 (independent clause reviewer; not scorer or blind oracle author)
Coordination branch     v1-source-vault-bootstrap-resume
Parent HEAD             3f18d7d810213b7b69476748559521abe45bf18b (Checkpoint 875)
Request                 MC-0030 Message 058
Subject                 Research 539; Validation 228; R0_P01_F1_TECHNICAL_SITE_RECEIPT_DECISIONS_REV01_UNFROZEN.json (D01-D15);
                        R0_P01_F1_REVIEWED_REV02_CASE_PINS_V01_UNFROZEN.json; scripts/check_r0_p01_f1_site_decisions.py + tests
Verdict                 AMEND_TECHNICAL_TABLE_TARGETED
Authority               Review record only. No source, policy, script, test, routing or evidence edit. F1/F2 unfrozen.
```

## 0. Verification

- **Branch and sources.** The branch head was `3f18d7d8…`. Contract and policy still hash to `9160a30c…` and `9b5bbc4d…`, and the B01 and B02 records bind those values.
- **Pins are grounded in Git, independently recomputed.** From a bare clone, `git show 41e8b0c3:…REV02_UNFROZEN.json` hashes to `9466563e…`, equal to `committed_git_blob_sha256`. I recomputed all 24 canonical case hashes and premise maps from that blob, and 24 of 24 match `pinned_case_sha256` and `case_premises_exact`. The REV02 file at `3f18d7d8` is byte-identical to the reviewed blob. `41e8b0c3` is the commit I reviewed in Message 057.
- **Regression.** On a full-history clone at `3f18d7d8` the site guard reports PASS and the focused regression shows 84 passed. On a history-less extraction the guard fails closed, because it cannot read `41e8b0c3`; CI must therefore never use a clone shallow enough to exclude that commit.

## 1. Verdict

**`AMEND_TECHNICAL_TABLE_TARGETED`.** Most rows are supported, but four changes are needed before rows D04, D05, D06 and D15 can feed complete vectors.

1. **D04/D05: the setup-only NOT_REALIZABLE rule is not a lawful pure technical disambiguation. I correct my own Message 057 Q3 here.**
   - Every WebAuthn assertion is necessarily post-registration: `allowCredentials` holds only the registered ID (V02:L0260), and registration precedes P0 (R4:L0082).
   - The B02-approved policy places NotSupportedError in the **assertion** failure table with `outcome: CAPABILITY_NOT_REALIZABLE` and `proof_viability_receipt: NOT_REALIZABLE` (P:`webauthn_assertion_failure_table.NotSupportedError.*`). R4:L0112 states the same rule in the assertion-receipt context, and R4:L0200 does so without any phase restriction. V01:L0231 explicitly includes "cannot return an assertion bound to the exact challenge".
   - A rule that assertion-time NotSupportedError *always* leaves B INCOMPLETE therefore makes an approved table row unreachable *by rule*. That changes approved semantics.
   - The lawful technical form is: **absent a qualifying assertion-time independent capability receipt, B is INCOMPLETE; with one, NOT_REALIZABLE per the approved row.** The receipt must be non-credential (no owner replacement assertion: R4:L0089, L0108, L0114). If no adequate receipt can be defined, the row becomes *evidentially* unreachable, which is a technical fact, not a prohibition.
   - Adopting setup-only *as a rule* would require a separately requested owner interpretation, which I am not recommending (OI-5 in §4).
2. **D06 needs scorer-side consistency.** As written, a harness-side INSTRUMENT classification can be overridden by a scorer-derived INTEGRITY flag for the same fact.
   - The start claim binds "platform/provenance" (R4:L0021). `post_observation_tuning` compares "frozen artifact hashes" (R4:L0225), and `provenance_mismatch` covers "frozen head/contract identity mismatch" (R4:L0228).
   - Unless F1 states that the native OS runtime identity is *not* a frozen artifact for those scorer-derived flags, a post-claim OpenSSH update fires INTEGRITY at precedence 1 and defeats the L0203 reading.
3. **The pins froze text that Message 057 asked to change.** Q2(ii) ("only after actual owner assertion ceremony") and the Q7 cosmetics are pinned verbatim in S1-02 and S1-04. The D03 row states the correct scope, but the pinned REV02 conclusion still carries the B01-narrowing reading.
   - Either issue a REV03 text revision, re-review and re-pin it, or add an explicit, guarded supersession field in the table ("D03 governs S1-02 terminal scope").
4. **Guard hardening for the decision table itself** (§5). Row semantics, the native-Windows blocking status and the per-row evidence lists are unpinned.

No owner-policy decision is unavoidable now. Q1(b) remains conditional on the L0075 result.

## 2. Row decisions

| Row | Decision | Can support complete vectors? |
|---|---|---|
| D01 Ctrl+C at native SSH prompt | ACCEPT AS BLOCKED, plus mitigation constraints | Only as both-branch parameterized vectors; not freezable until L0075 |
| D02 RP-only timeout, no `get()` | ACCEPT | Yes |
| D03 consumed NotAllowedError after `get()` | ACCEPT; pin conflict (item 3) | Yes, after the S1-02 supersession or re-pin |
| D04 NotSupportedError after registration | **AMEND** (item 1) | After revision |
| D05 capability receipt | **AMEND**: phase must include an assertion-time non-credential receipt | After revision; receipt grammar still to be closed |
| D06 OpenSSH runtime replaced | **AMEND** (item 2), plus evidence additions | After scorer-flag exclusion is frozen |
| D07 process-creation failure | ACCEPT | Yes |
| D08 missing-DLL nonzero exit | ACCEPT, with disclosure and vector obligation | Yes |
| D09 agent loaded before P0 | ACCEPT WITH CLOSURE (baseline timing, key scope) | Yes, after closure |
| D10 passphrase re-encryption | ACCEPT WITH CLOSURE (rotation permitted) | Yes, after closure |
| D11 normal three-call exhaustion | ACCEPT AS BLOCKED | Only parameterized until L0075 |
| D12 snapshot promotion atomicity | ACCEPT AS BLOCKED | Only parameterized until L0136 |
| D13 unorderable RP/owner abort | ACCEPT (conservative, within L0215 delegation) | Yes |
| D14 late success after harness stop | ACCEPT | Yes |
| D15 G2 with false capability | ACCEPT CONDITIONAL on D04 revision | After D04 |

## 3. Per-row findings

**D01 — Ctrl+C at the native SSH prompt (R4:L0067, L0069, L0070, L0075; P:`ctrl_c_or_crash`).** Correctly blocked, and it correctly refuses to infer absence of Ctrl+C from a nonzero exit.
- *Mitigation constraint:* R4:L0070 and L0114 forbid any SIGINT **confirmation** handler. A non-confirming interrupt *recorder*, or an out-of-band interrupt channel, is not excluded, but it must not add any prompt.
- *Race window:* "observes abort before sealing" leaves a gap. Python raises KeyboardInterrupt asynchronously, so the event seal can be written and the abort raised a few bytecodes later from the same keypress. The seal must be **provisional** until the harness passes an explicit post-event interrupt checkpoint. An abort observed before that checkpoint voids the seal: the event is in flight, so INCOMPLETE.

**D02 — RP-only timeout without client `get()` (R4:L0108, L0151, L0154).** This is an evidence definition and does not narrow B01. A never-delivered challenge is a legitimate absence, not provenance INTEGRITY. Higher-precedence chain violations still win. This closes the Q2(iii) absence semantics.

**D03 — consumed NotAllowedError after client `get()` (R4:L0151, L0154, L0199).** The row correctly forbids owner-presence, focus or voluntary-cancel requirements, so B01 item 2 is preserved. The only defect is the conflict with the pinned S1-02 text (§1 item 3).

**D04/D05 — NotSupportedError after registration and the capability receipt.**
- Retained: no owner-credential probe; the self-labelled error is insufficient; absence of a receipt gives INCOMPLETE; flags affect class, not evidence_state (this resolves Q7).
- Revised: the phase restriction, per §1 item 1. The D05 `phase` must admit an assertion-time receipt produced by a frozen non-credential probe:
  - same browser, profile, OS and authenticator scope;
  - claim, acceptance and clock bound;
  - replayable;
  - negative controls for refusal, cancel, timeout, not-visited, expired and absent receipt.
- Registration success plus assertion NotSupportedError should be a *recorded* fact that the receipt must explain; for example, the probe shows the capability absent for this credential operation.
- *Counterexample to the current D04 text:* on a platform where `get()` with the registered credential is genuinely unsupported (V01:L0231's case), the current rule forces INVALID_INCOMPLETE instead of the REOPEN the approved table allows.
- *Exception-right consequence:* none. B02 item 4 gives REOPEN and INVALID_INCOMPLETE identical exception terms. The issue is changing an approved class mapping, not exception rights.

**D06 — native OpenSSH runtime replaced after the claim (R4:L0066, L0120, L0203, L0206).** The INSTRUMENT reading is supported: L0203 is the specific runtime site, "never an owner-integrity breach", and L0206 does not enumerate the native executable. Three additions are needed:
- **(a)** The scorer-flag exclusion in §1 item 2.
- **(b)** Evidence fields for the benign path:
  - Authenticode signer and version of the new binary;
  - the Windows servicing or update history entry;
  - a policy that Windows Update was deferred for the claim window, as a preclaim condition, disclosed.
- **(c)** An explicit statement that the INSTRUMENT class does **not** by itself grant the B02 exception. B02 item 4 and R4:L0174 and L0241 require separate, independently substantiated defect-and-repair review.
  - This closes the false-favorable path: if an owner deliberately induces an update to escape an unfavorable partial run, the event is still scored INSTRUMENT, but the exception fails substantiation. A demonstrated deliberate change is `post_observation_tuning`, which is INTEGRITY.
  - Replacement of protected harness, fixture, scorer or KAT artifacts keeps INTEGRITY precedence.

**D07 — process-creation failure (R4:L0203, L0213, L0165).** Supported. Typical sites:
- file removed between precheck and launch;
- access denied, including AppLocker;
- a bad executable image.

A missing binary is normally caught earlier by the L0066 pinned-path precheck, which is the D06 site.

**D08 — missing DLL with nonzero exit (R4:L0068–L0070, L0204).** The literal and conservative reading is supported: the process image ran and exited nonzero with no signature, so this is the budget path. Two obligations:
- Record the raw exit status, for example `0xC0000135`, as a disclosure-only field.
- Include a vector showing that a recurring tool fault can reach terminal exhaustion and contribute to COMPLETED, and hence to REOPEN when the other arm is also non-viable and resolved. The owner package must disclose this; L0069 approves it.

**D09 — agent loaded before P0 (R4:L0066, L0067, L0206, L0254).** It must not soften L0206, and it does not. Close it as follows:
- **(a) Baseline timing.** The baseline is taken *immediately after the post-claim keygen*, in the same process, with the new public ID not present in the agent. "After setup", as currently worded, would let an `ssh-add` made during setup escape the "change" test. That would turn INTEGRITY (no exception) into INCOMPLETE (exception possible with a new hypothesis), a B02-relevant softening.
- **(b) Key scope.** The no-agent-caching check concerns the **registered public ID**. Signing already runs agent-disabled (L0067). Unrelated old agent entries, including Attempt 001 keys, are not a violation. This is a scope definition, not a weakening.
- **(c) Unreadable agent state.** It never yields INTEGRITY. Precheck inability leaves the event non-terminal, so the arm is INCOMPLETE.
- **(d) Disclosure.** An `ssh-add` of the new key after keygen means INVALID_INTEGRITY with no exception. Disclose this together with the exact-R rule.

**D10 — passphrase re-encryption (R4:L0066, L0206).** Supported: bytes alone are not proof. Close it this way: no source prohibits passphrase rotation, and L0066 checks the *encrypted property*, so freeze rotation as **permitted (no flag)** and disclose it. Introducing a prohibition would add a new INTEGRITY trigger, increasing forfeiture, and would need owner approval. Not recommended.

**D11 — normal three-call exhaustion (R4:L0068–L0070; P:`terminal_outcomes[4]`).** Correctly blocked on L0075 observability. The alias is otherwise representation-only, as already accepted.

**D12 — snapshot promotion atomicity (R4:L0136, L0138, L0209).** Correctly blocked. The orphan-temp versus published-malformed distinction is source-exact, and integrity precedence is preserved. The `qualification: ["Q1"]` label is wrong; X3 was never part of Q1 (§5).

**D13 — unorderable RP/owner abort (R4:L0112, L0215, L0242; P:`flag_origin…node_rp_failure`).** Supported. L0215 delegates the choice to "a frozen rule". INCOMPLETE-on-unorderable is consistent with L0242, P:`cases[5].next` and P:`default_missing_flags`. A harness-recorded, isolation-verified pre-abort fault keeps INSTRUMENT.
- Disclose the residual: without isolation, a genuine RP fault that coincides with an owner Ctrl+C is scored INCOMPLETE, and the owner loses a repair exception they might otherwise have had.
- Labels Q2/Q7 are mis-mapped (§5).

**D14 — late success after harness stop (R4:L0094, L0114, L0128, L0154).** Supported. The row correctly preserves earlier in-run results.

**D15 — G2 with false capability (R4:L0156, L0158; P:G2 leaf).** Supported once D04 is revised: B is INCOMPLETE *whenever no qualifying receipt exists*, so the PASS carries `OTHER_ARM_INCOMPLETE`.

## 4. Owner-policy questions

**None is unavoidable now.**
- **Q1(b) remains conditional.** It arises only if L0075 shows Ctrl+C at the native prompt is unobservable and no recorder or out-of-band channel restores observability. The question would then be: "May a Ctrl+C during the native passphrase prompt be scored as an unlock failure, given the approved unconditional whole-attempt abort?"
- **New OI-5 is not recommended.** Setup-only NOT_REALIZABLE as a *rule* would make the B02-approved assertion-table NotSupportedError row unreachable, and would require owner interpretation. The technical receipt route in §1 item 1 avoids it.
- **OI-1 to OI-3 remain not requested.**
- **D10's possible prohibition** of passphrase rotation would need owner approval and is not recommended.

## 5. Guard: guarantees and limits

**The required adversarial check passes.** Changing a reviewed REV02 conclusion (S3-03 → "INVALID_INSTRUMENT") *together with* its local pin fails: "stored semantic hash not grounded in independently reviewed Git source". The historical-blob design is sound.

**Mutations to the decision table that still pass (unchecked):**

| Mutation | Result |
|---|---|
| D04 decision → "NotSupportedError alone makes B NOT_REALIZABLE; G1 may REOPEN" | PASS |
| D06 `expected_class` → `INVALID_INTEGRITY` | PASS |
| D13 decision → "unorderable race sets node_rp_failure; INVALID_INSTRUMENT" | PASS |
| D12 status `BLOCKED_NATIVE_WINDOWS_TEST` → `NEEDS_INDEPENDENT_TECHNICAL_DECISION` | PASS |
| D11 evidence `native_L0075_interrupt_observability_pass` removed | PASS |
| D12 source `REV04_CONTRACT-L0136` removed | PASS |
| `native_qualification_required` emptied | PASS |
| D15 `expected_class` → `PASS_WITH_SELECTION` (no G2) | PASS (only literal `PASS` / `REOPEN` are rejected) |
| D03 exception → "require owner focus and voluntary cancel" (B01 narrowing) | PASS |
| D01 `owner_action` → `NONE`; D01 Q1 label removed (Q1 still on D11/D12/D14) | PASS |
| D13 status → `CANDIDATE_TECHNICAL_REVIEW` | FAIL (caught: sensitive-row clearing) |

**Word- and count-only checks:**
- Q coverage is satisfied by labels: D12, D13 and D14 carry Q labels unrelated to their content.
- Evidence and sources need only `len ≥ 2`.
- `expected_class` is checked only against the exact strings `PASS` / `REOPEN`.
- `owner_action` and `native_qualification_required` are free.
- Test `test_table_requires_explicit_evidence_per_site` only checks an empty list.

**Proportionate hardening (before vectors):**
1. Pin D-row semantics by Git-blob hash *after* this review's amendments are applied and re-reviewed, using the same historical-blob method.
2. Pin per-row `decision_status`, in particular D01, D11 and D12 = `BLOCKED_NATIVE_WINDOWS_TEST`.
3. Require `native_qualification_required` ⊇ {L0075, L0136}.
4. Require the L0075 and L0136 anchors and evidence fields on D01, D11 and D12.
5. Make `expected_class` a closed enum.
6. Correct the Q-label mapping.

## 6. Next action

1. **Table REV02:**
   - D04/D05 revised to the assertion-time receipt form.
   - D06 scorer-flag exclusion, evidence fields and the exception-gate statement.
   - D09 baseline and key scope; D10 rotation permitted.
   - D01 provisional-seal checkpoint and no-confirmation constraint.
   - D08 raw-exit disclosure.
   - Q-label corrections.
   - The S1-02 / S1-04 text resolved, either by REV03 plus re-pin or by a guarded supersession.
2. **A brief independent confirmation** of those deltas only.
3. **Then the complete seven-row attempt-level vectors** using D02, D07, D08, D13 and D14; D03, D09 and D10 once their closures are applied; and, once revised, D04/D05/D06/D15. D01, D11 and D12 are present only as explicit two-branch parameterized vectors, not freezable until the L0075 and L0136 target-Windows qualifications are recorded.

## 7. Attestation and boundaries

- **Reviewer: claude-04.** I read the cited units directly, recomputed the pins from Git objects, and ran guard mutations on a scratch clone only. I did not author the table, pins, guard, tests, scorer or oracle.
- This review gives no F1 approval and no B01/B02 change, and authorizes nothing about Attempt 002. The 55 pending rows remain UNRESOLVED. Only this message file was written.

```text
MC0030_MESSAGE059=SITE_DECISION_TABLE_REV01_INDEPENDENT_REVIEW
VERDICT=AMEND_TECHNICAL_TABLE_TARGETED
ACCEPT=D02,D03,D07,D08,D13,D14;ACCEPT_WITH_CLOSURE=D09,D10;ACCEPT_BLOCKED=D01,D11,D12;AMEND=D04,D05,D06;CONDITIONAL=D15
CORRECTION=MESSAGE057_Q3_SETUP_ONLY_RULE_WITHDRAWN_ASSERTION_TIME_RECEIPT_ROUTE
PIN_GROUNDING=VERIFIED_24_OF_24_FROM_41e8b0c3_BLOB_9466563e
PIN_CONFLICT=S1-02_Q2ii_AND_S1-04_Q7_TEXT_FROZEN_UNFIXED
OWNER_DECISION_NOW=NONE;CONDITIONAL=Q1b_IF_L0075_UNOBSERVABLE;OI-5_NOT_RECOMMENDED
GUARD=REV02_PINS_ROBUST;TABLE_ROW_SEMANTICS_STATUS_EVIDENCE_UNPINNED
VECTORS_READY=D02,D07,D08,D13,D14;AFTER_CLOSURE=D03_PIN,D09,D10;AFTER_REVISION=D04,D05,D06,D15;PARAMETERIZED_ONLY=D01,D11,D12
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
