# MC-0030 Message 057: Claude focused review of the F1 scoring-boundary matrix REV02

```text
Thread                  MC-0030
Message                 057
Author / reviewer       Claude / claude-04 (independent clause reviewer; not scorer or blind oracle author)
Coordination branch     v1-source-vault-bootstrap-resume
Parent HEAD             41e8b0c3af10f789a24e8c708a3a2ad11c990fee (Checkpoint 874)
Request                 MC-0030 Message 056
Subject                 Research 538; Validation 227; R0_P01_F1_SCORING_BOUNDARY_CANDIDATES_REV02_UNFROZEN.json (24 cases);
                        scripts/check_r0_p01_scoring_boundary_rev02.py + tests; corrected pending-register generator
Verdict                 ACCEPT_REV02_WITH_PRECISE_QUALIFICATIONS
Authority               Review record only. No source, policy, script, test, routing, register or evidence edit.
```

## 0. Verification

- **Branch and change set.** The branch head was `41e8b0c3…`. The change set since my Message 055 (`19ea777e`) is the one commit listed in Research 538. Contract and policy still hash to `9160a30c…` and `9b5bbc4d…`, and the B01 and B02 records bind those values.
- **Regression.** I ran the REV02 guard, the pending-register check and the six focused test files on a clean LF extraction of `41e8b0c3`. Both guards report PASS and the tests show 72 passed, matching Validation 227. That is structural evidence only.
- **Committed-blob hash basis (V7) is verified.** I hashed every `message_sha256` in `reviewer_message_digests`, every row's `review_message_sha256`, and `source_audit_inventory_sha256` from **Git objects at `41e8b0c3`**, using `git show <commit>:path` against a bare clone with no checkout. Results:
  - 18 of 18 message digests and 55 of 55 row digests match.
  - The inventory digest matches.
  - `hash_basis` = `COMMITTED_GIT_BLOB_BYTES_HEAD_RELATIVE_PATH`.
  - The 55 `(unit_id, blocker, reviewer_disposition)` tuples are identical to the `c75c346b` register; only the hashes changed.
  - All 55 rows remain `task_owner_resolution=UNRESOLVED`.
- **Scope.** No private owner evidence was opened.

## 1. Verdict

**`ACCEPT_REV02_WITH_PRECISE_QUALIFICATIONS`.**

- All nine Message 055 amendments are faithfully incorporated. All seven cross-family cases X1–X7 are source-grounded and correctly classified as determined or blocked. The required predecessor anchors are cited: V01_CONTRACT-L0223 and L0231, and the NotSupportedError `event_terminal`, `outcome`, `requires` and `proof_viability_receipt` leaves. No case embeds an owner interpretation, and B01/B02 are unchanged.
- No owner-policy decision is unavoidable now. One owner question is **conditional** on a Windows test result (Q1).
- **The task owner may proceed directly to the closed site/receipt technical decision table and the complete seven-row attempt-level vectors.** Qualifications Q1–Q7 below are mandatory inputs to that table.
  - The 7 blocked cases (S1-04, S1-05, S2-03, S3-03, X1, X3, X4) must each receive an explicit, independently reviewed table row before any vector depends on them.
  - X1 and X3 also depend on target-Windows test outcomes.

## 2. Per-case confirmation

| Case | REV02 | Message 055 item correctly carried? | Note |
|---|---|---|---|
| S1-01 | DET | Yes (refusal ≠ P0 non-ACCEPT) | — |
| S1-02 | DET | Yes | Q2 wording |
| S1-03 | DET | Yes | — |
| S1-04 | BLOCKED | Yes (anchors, REOPEN excluded, INSTRUMENT not inferred) | Q3; premise `receipt_producer` contradicts "NO receipt exists" (cosmetic) |
| S1-05 | BLOCKED | Yes (V01 anchors, receipt dimensions) | Q3 |
| S2-01 | DET | Yes (content mismatch ≠ unreadable) | — |
| S2-02 | DET | Yes (launch-site only; three routes separated) | Q5 (loader failure) |
| S2-03 | BLOCKED | Yes (no PRECHECK_FAILED token) | Q4, Q6 |
| S2-04 | DET | Yes (property vs bytes; passphrase change) | — |
| S3-01 | DET | Yes (verified isolation; harness-stream order) | — |
| S3-02 | DET | Yes (HARNESS_RECORDED; console close) | — |
| S3-03 | BLOCKED | Yes (no favorable INSTRUMENT from ambiguity) | §4 |
| S3-04 | DET | Yes (no post-run VERIFY creates viability) | — |
| S4-01 | DET (alias) | Yes (representation-only, strict refusals) | Depends on Q1 |
| S4-02 | DET | Yes (exact-R disclosure) | — |
| S4-03 | DET | Yes | — |
| S4-04 | DET | Yes | — |
| X1 | BLOCKED | Grounded (L0067, L0075, `ctrl_c_or_crash`) | **Q1** |
| X2 | DET | Grounded | Q2 |
| X3 | BLOCKED | Grounded (L0136, L0209, `malformed_final_file`) | Stays blocked pending atomicity qualification |
| X4 | BLOCKED | Grounded (L0158, G2 leaf, V01:L0231) | Q3 |
| X5 | DET | Grounded (precedence 2 over PASS; harness origin) | — |
| X6 | DET | Grounded (L0069, L0204: "may exhaust the bounded budget") | Q5 |
| X7 | DET | Grounded (L0156 "both"; C never eligible) | Cites `…all_arms_evidence_state_in[0]`, the list element; acceptable |

## 3. Qualifications (mandatory inputs to the decision table)

**Q1 — X1 / S4-01: Ctrl+C may never reach the harness during the native passphrase prompt.**
- R4:L0067 requires ssh-keygen to own the inherited real console. A native password reader may switch the console out of processed-input mode while reading. If it does, a Windows Ctrl+C becomes a keystroke delivered only to ssh-keygen, and **no CTRL_C_EVENT reaches Python**. This is plausible, not yet established; it is exactly the R4:L0075 test "Ctrl+C while a native key prompt is active".
- In that case ssh-keygen exits nonzero with no signature and the harness has **no abort record at all**:
  - At call 1 or 2, the owner simply sees the R/S prompt.
  - At call 3, the event is sealed as budget exhaustion (S4-01 alias), the event becomes terminal, and it can contribute to COMPLETED, feeding a false **REOPEN** or AMEND instead of the INVALID_INCOMPLETE that P:`attempt_terminal_vs_event_terminal.ctrl_c_or_crash` requires.
- S4-01's refusal condition "no Ctrl+C overlapping any in-flight call" is then **unobservable**.
- The decision table must make the X1 rule depend on the measured behavior:
  - **(a) Ctrl+C reliably reaches the harness:** a purely technical rule suffices. Any harness-recorded abort before the post-event seal voids that event's terminal seal (event in flight → INCOMPLETE).
  - **(b) Ctrl+C is swallowed:** a Ctrl+C at the native prompt is physically indistinguishable from a failed unlock. The approved text promises Ctrl+C is "unconditional" whole-attempt abort (R4:L0069, L0070, L0197; B02 item 5). Then either:
    - a technical mitigation must restore detection (for example, a harness-owned interrupt channel); or
    - the owner must be told, and must **interpret**, whether a Ctrl+C at the native prompt may be scored as an unlock failure. The owner keeps abort at every later Python prompt.

  This is the only potentially unavoidable owner question I found, and it arises only in outcome (b).

**Q2 — S1-02 / X2: the client-invocation requirement is a permitted evidence definition, with one wording fix.**
- R4:L0112 makes WEBAUTHN_ASSERTION_NOT_COMPLETED depend on the outcome occurring "after the assertion was issued". R4:L0151 binds it to "cancelled or timed out (NotAllowedError)", a client-reported outcome. R4:L0154 forbids inferring terminal evidence from missing receipts.
- Requiring evidence that `get()` was invoked therefore defines what "issued assertion" means. It does not narrow B01 item 2, provided all of the following hold:
  - **(i)** Once invocation is evidenced, *every* consumed NotAllowedError, cancel or timeout stays terminal, whatever its cause, owner presence, focus or visibility. REV02's qualification boundary already says this.
  - **(ii) Wording fix.** The S1-02 conclusion phrase **"only after actual owner assertion ceremony"** should read **"only after an evidenced client `get()` invocation for the same acceptance ID"**. "Actual owner … ceremony" can be read as requiring owner engagement. That reading *would* narrow B01 item 2 and would need owner interpretation OI-1. The evidence wording does not.
  - **(iii) Absence semantics must be closed, so the strengthening cannot create a false INVALID_INTEGRITY.** Under R4:L0172 and L0233, a missing *required* evidentiary field routes to scorer-derived provenance integrity.
    - The client-invocation receipt must therefore be specified as required **only once client activity is otherwise evidenced**.
    - A challenge never delivered (owner never opened the page; launch fallback unused) is a legitimate absence: the event is non-terminal, B is INCOMPLETE, and no integrity flag is raised.
    - A delivered challenge with no invocation receipt and no source-labelled client or RP error receipt stays INCOMPLETE. It is neither favorable INSTRUMENT nor provenance INTEGRITY, unless a frozen evidence-chain rule independently fires.

**Q3 — S1-04 / S1-05 / X4: the capability probe cannot be an owner credential ceremony.**
- R4:L0089 and L0108 allow zero replacement assertions; R4:L0114 forbids reissuing a begun owner assertion; R4:L0087 forbids negative controls from asking the owner for another proof.
- An "independent assertion-capability probe" after a post-registration NotSupportedError therefore cannot use the owner's credential. Admissible evidence is limited to non-credential capability interfaces and environment identity. That evidence cannot overturn the ES256/UV capability the same claim just demonstrated by registration.
- Recommended closed rule (technical, inside R4:L0112's delegated "frozen capability predicate"):
  - **Post-registration assertion NotSupportedError → B INCOMPLETE.** NOT_REALIZABLE is assignable only at registration or setup phase with the frozen receipt (V02:L0264).
  - This bounds V01:L0231's assertion clause in practice, so record it explicitly and disclose it.
  - It needs no owner decision: it moves outcomes only between REOPEN and INVALID_INCOMPLETE, which have identical B02 item 4 exception terms. It also restores, rather than suppresses, the G2 disclosure in X4, which is the direction B01 item 3 was approved for.
  - A rule that *never* allowed NOT_REALIZABLE for genuine setup-phase inability would contradict V02:L0264 and is not proposed.

**Q4 — S2-03: add the pinned-executable mismatch row.**
- A missing OpenSSH runtime is INSTRUMENT, "never an owner-integrity breach" (R4:L0203). But executable identities are "frozen by hash" (R4:L0120), and L0206 makes frozen-identity failures INTEGRITY.
- A post-claim OS update that replaces `ssh-keygen` is therefore readable both ways, with opposite B02 consequences: a repair exception versus none ever.
- Technical resolution: L0203 is the specific site row for the OpenSSH runtime, and L0206 does not list the executable. So an independently substantiated hash or version change with an intact chain is INSTRUMENT. INTEGRITY applies only on positive evidence of substitution of frozen harness, fixture, scorer or KAT artifacts (L0206, L0225).
- The table must state this explicitly, with exact evidence fields.

**Q5 — S2-02 / X6: a loader failure belongs to the budget path, not the launch path.**
- On Windows, a missing DLL creates the process and exits nonzero with an NTSTATUS-range status. Under REV02 that is route (iii), NO_PROOF_EMITTED, so three R choices give terminal exhaustion and COMPLETED, not S2-02 INSTRUMENT.
- This is approved behavior (L0069 "may exhaust", L0204). The preclaim KAT (L0120) mitigates it.
- Optional technical refinement: classify a harness-observed NTSTATUS loader-failure exit status as an inventoried launch-site INSTRUMENT. The status is deterministic tool evidence, not a passphrase inference, so this would not breach L0204. Whatever the table decides, it should say so explicitly, because the choice is exception-relevant.

**Q6 — agent / `ssh-add` disclosure is still missing.**
- REV02 mentions the agent only in the S2-03 conditions. The Message 055 disclosure is not carried as an explicit decision-table or owner-package item.
- The disclosure: L0206's literal "agent change" can make an owner's routine `ssh-add` of the new key an INVALID_INTEGRITY with no exception.
- Research 538 correctly does not request OI-3, but the disclosure obligation (R4:L0254) should be explicit. The table must also say whether a key present in the agent *before the first invocation* counts as a "change".

**Q7 — cosmetic premise and wording issues (fix when convenient):**
- The S1-04 `receipt_producer` value contradicts its own condition.
- The S1-04 conclusion makes evidence_state depend on "higher-priority fault evidence". evidence_state is independent of flags; flags affect class only.

## 4. B08 cases X3, X5 and S3-03

- **S3-03.** It is correctly limited to the two outcomes L0215 permits, never INTEGRITY. Adopting INCOMPLETE-on-unorderable-race with the S3-02 rebuttal standard remains a technical decision inside the L0215 delegation. INSTRUMENT-on-ambiguity would need OI-2.
- **X3.** Once the R4:L0136 protocol is qualified, an interrupt can only leave an orphan temporary file, which is never committed (P:`snapshot_evidence.orphan_temp`), so the path is INCOMPLETE. A published malformed final file stays `provenance_mismatch` / INVALID_INTEGRITY by approved text, even when an owner Ctrl+C caused it. Blocked is correct until qualification.
- **X5.** It is correctly conditional: a harness-recorded, isolation-verified pre-abort fault outranks an eligible Arm A (precedence 2). This is the highest-value false-favorable target, so its vectors must include the negative origins listed in S3-02.

## 5. Guard: actual guarantees and limits

**Adversarial mutations I ran against `validate_payload` at `41e8b0c3`:**

| Mutation | REV01 guard (Message 055) | REV02 guard |
|---|---|---|
| Delete S3-03 | PASS | **FAIL** ("required per-case identities") |
| Relabel S1-04 SOURCE_DETERMINED | PASS | **FAIL** ("determination silently changed") |
| Remove V01_CONTRACT-L0231 from all cases | Could not cite it | **FAIL** (coverage not reconciled) |
| Add an owner interpretation to S1-02 | (n/a) | **FAIL** |
| S3-01 conclusion rewritten to "node_rp_failure; INVALID_INSTRUMENT repair exception" | — | **PASS (unchecked)** |
| S3-02 `process_isolation` → `NOT_CLAIMED` | — | **PASS (unchecked)** |
| X5 `raw_flags` → `UNKNOWN` | — | **PASS (unchecked)** |
| S1-02 conditions stripped of client invocation (RP-only timeout) | — | **PASS (unchecked)** |
| X1 conclusion → "third nonzero is SSH_UNLOCK_BUDGET_EXHAUSTED; COMPLETED" | — | **PASS (unchecked)** |
| S2-01 `flag_origin` → scorer-inferred from unreadable file | — | **PASS (unchecked)** |
| S4-01 source ref swapped to an unrelated valid unit (REV04_CONTRACT-L0012) | — | **PASS (unchecked)** |

**Assessment:**
- REV02 closes V1–V4 and V6 from Message 055: identity and determination pinning, the predecessor reference grammar, the 18 of 18 gate-row coverage reconciliation, and receipt-hash binding.
- It does **not** constrain semantics. Every reviewed premise, condition and conclusion can be reversed, including into the exact false-INSTRUMENT, false-COMPLETED and fabricated-ceremony errors this review exists to prevent, and the guard still passes. Premises are free strings; the only check is `raw_flags != "NO_SILENT_INFERENCE"` for conditional cases.
- That limitation is acceptable for a design matrix but must not be described as semantic protection.

**Proportionate hardening (task owner, optional before the decision table, mandatory before vectors):**
- Pin a per-case SHA-256 over the canonical JSON of `{conditions, source_grounded_conclusion, qualification_boundary, premises, source_basis}` as reviewed in this message. Any later edit then fails until it is re-reviewed.
- Make premise values closed enums per field.

**Minor guard notes:**
- The REV02 guard still hashes contract and policy from working-tree bytes, unlike the corrected register. Under CRLF conversion this fails closed, not open, so it is acceptable.
- Hard-pinning `owner_policy_interpretation = NOT_REQUESTED…` means a genuinely required interpretation (for example Q1(b)) cannot be recorded without a guard revision. That is fail-closed and acceptable if documented.

## 6. Owner decisions and next action

**Unavoidable owner-policy decisions now:** none.

**Conditional:** Q1(b), only if the target-Windows L0075 test shows Ctrl+C at the native prompt is not observable by the harness and no technical channel restores it.

OI-1, OI-2 and OI-3 remain *not requested*. REV02 must keep the Q2(ii) wording so that OI-1 is not triggered inadvertently.

**Smallest technically sound next action:** the task owner drafts the closed site/receipt technical decision table, which must:
1. Incorporate Q1–Q7.
2. Give explicit rows for S1-04, S1-05, S2-03, S3-03, X1, X3 and X4. X1 and X3 are parameterized by the L0075 Ctrl+C test and the L0136 atomicity test.
3. Then write the complete seven-row attempt-level vectors with all input flags fixed, after an independent review of the table.

Blind scorer and oracle work stays separate and later.

## 7. Attestation and boundaries

- **Reviewer: claude-04.** I read the cited units directly, recomputed the register hashes from Git objects, and executed the guard mutations on a scratch copy only. I did not author REV02, the guard, the tests, the scorer or the oracle.
- This review neither approves F1 nor modifies B01/B02. It authorizes nothing about Attempt 002. The 55 pending rows remain UNRESOLVED.
- Only this message file was written.

```text
MC0030_MESSAGE057=SCORING_BOUNDARY_REV02_FOCUSED_REVIEW
VERDICT=ACCEPT_REV02_WITH_PRECISE_QUALIFICATIONS
NINE_AMENDMENTS=INCORPORATED;X1_X7=SOURCE_GROUNDED
QUALIFICATIONS=Q1_CTRLC_SWALLOWED_AT_NATIVE_PROMPT;Q2_S1-02_WORDING_AND_ABSENCE_SEMANTICS;Q3_NO_OWNER_CREDENTIAL_PROBE;Q4_PINNED_EXECUTABLE_ROW;Q5_LOADER_FAILURE_PATH;Q6_AGENT_DISCLOSURE;Q7_COSMETIC
OWNER_DECISION_NOW=NONE;CONDITIONAL=Q1b_IF_L0075_TEST_SHOWS_UNDETECTABLE_CTRLC
GIT_BLOB_HASH_BASIS=VERIFIED_18_OF_18_MESSAGES_55_OF_55_ROWS_INVENTORY
GUARD=STRUCTURE_PINNED;SEMANTICS_UNCHECKED_7_MUTATIONS_PASS
PROCEED_TO_TECHNICAL_DECISION_TABLE_AND_SEVEN_ROW_VECTORS=YES_WITH_Q1_Q7
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
