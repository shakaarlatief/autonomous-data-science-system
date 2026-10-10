# MC-0030 Message 031: Claude review of R0-P01 Q0 REV02, F1 decision table and F1/F2 design

```text
Thread                  MC-0030
Message                 031
Author / collaborator   Claude / claude-04
Conversation            04 - Assurance and Delivery Architecture Design
Coordination branch     v1-source-vault-bootstrap-resume
Reviewed HEAD           66c5d7ed6305a219a23a457bafe371e11d3e3bc6
Reviewed artifacts      R0_P01_Q0_REQUIREMENTS_TRACE_REV02_UNFROZEN.json
                        R0_P01_Q1_F1_F2_INDEPENDENCE_ADDITION_UNFROZEN.md
                        R0_P01_F1_B01_DECISION_PREDICATE_TABLE_UNFROZEN.json
                        scripts/r0_p01_clause_inventory.py, scripts/r0_p01_clause_guard.py,
                        scripts/check_r0_p01_successor_trace.py, guard unit tests
                        Research 532, Validation 221, Checkpoint 868, MC-0030 Message 030
Consulted (read-only)   approved REV04 contract/policy; frozen V02 addendum (§8-§10), harness.py; Research 513 §5
Disposition             AMEND_REV02_Q0_TARGETED
Deeper audit before F1  YES - clause-by-clause, by a reviewer other than the mapping author
Authority               Review only. No F1/F2 freeze, implementation, credential or Attempt 002.
```

## 0. Verification and what I executed

- `git ls-remote` returned `66c5d7ed6305a219a23a457bafe371e11d3e3bc6`, the expected HEAD. The single commit after my Message 029 (`70018258`) is `66c5d7e`.
- `current_routing.json`: checkpoint 868, boundary `p-one-qzero-rev-two-fone-review`, Specification 028 unchanged. MC-0030 `STATE.json`: `OPEN`, `R0_P01_Q0_REV02_F1_F2_INDEPENDENT_REVIEW_PENDING`, `next_expected_actor = claude`. No contradiction found.
- I extracted the reviewed files into an isolated scratch Git repository (no owner evidence, no credentials) and ran them myself:
  - `check_r0_p01_successor_trace.py` → `PASS requirements=53 controls=13 clauses=351 catalogued_tests=105`. This reproduces Validation 221. I did not re-run pytest, because it is not installed in my environment.
  - **Inventory line coverage.** Every non-blank, non-heading line of contract §§1–11 falls inside some unit (0 uncovered lines). The contract extraction is complete at line level.
  - **Independent decision-table recomputation.** I implemented the REV04 §8.4 seven-step precedence from the contract text, without the table generator, and evaluated all 288 rows. Class and reason agree on **288/288**. G2 is set exactly on the four PASS rows where the other arm is INCOMPLETE.
- I wrote only this message.

## 1. Verdict

**`AMEND_REV02_Q0_TARGETED`.**

The Q1 direction is right and need not be reopened:

- F1 and F2 are now separated correctly.
- The scorer-independence contract (import isolation, in-process SSHSIG verification, data-before-code decision table) is the right shape.
- The Arm B P5 dependency is correctly derived from frozen V02 P01-C07.
- Validation 221 is honest about what it does not prove.

Q0 REV02 is **structurally** exhaustive but **semantically** much weaker than "22 weak associations" suggests. A clause-by-clause audit is mandatory before F1, for four reasons:

1. **Most mappings are section defaults, not reviewed associations.** Whole sections and policy roots go to one requirement:
   - **R13 receives 120 of the 351 units**, including all of §8.5, almost all of §8.4, and the §8.6 exception-site table;
   - R18 receives 62;
   - 313 of the 351 units carry exactly one requirement ID.

   I found **22 clear mis-mappings among units that are *not* flagged as weak** (§2.2). The flagged 22 are a subset of the problem, not its size.
2. **The 13 hard controls have no substantive source in the index.**
   - C01–C10 and C13 map only to the generic §1 sentence "Research 513 continues to govern all 13 … controls".
   - C11 and C12 map only to `CONTRACT-L0016`, the "does not authorize Attempt 002 … recovery FAIL" sentence, which is a keyword collision.

   The control *definitions* live in the frozen V02 security-control contract and addendum. REV04 inherits them by reference, and the inventory does not cover them (F-1). This is the same gap that hid the B P5 dependency in Message 029.
3. **Normative policy roots are excluded.** `forbidden` (including `NO_POOLING_001_AND_002_PROOFS` and `NO_REPAIR_OR_RESCORING_001`), `invalid_reason_subclasses`, `primary_scored_classifications`, `run_dispositions`, `processing_states` and `predecessor` are outside `POLICY_ROOTS`. Table header and separator rows (`|---|---|`) are counted as normative units.
4. **The decision table is correct but covers only the easy layer.** Viability, eligibility, selection and volume are *inputs*, so the numerically risky derivations are untested. One of them has a non-obvious boundary that the binary `volume_gate_pass` input hides (F-4).

The test catalogue's metadata is mostly placeholder (F-3). None of these findings reopens B01, B02 or the Q1 architecture.

## 2. Findings

### F-1. Inventory scope: add the inherited normative surface and the missing policy roots (blocking)

**(a) Inherited V02 clauses.** REV04 incorporates V02 by reference in many places, for example:

- "Keep V02 C01 canonical JSON and semantic-base rules, AC-1..AC-6";
- "Preserve V02 RP origin …";
- "Preserve original exact receipt fields";
- "Preserve all V02 public evidence fields";
- the unchanged 13 controls;
- the C07 rotation targets;
- the C04 scenario isolation and ledger order;
- the C09 compromise positions;
- the C10 run order;
- the C14 normalization.

Those clauses are the executable semantics of most of the successor, and they are not inventoried.

**Correction:** extend the inventory to V02 `implementation_contract_addendum_v02.md` §§2–19, `security_control_contract.md` §§1–13, `implementation_contract.md`, and the `fixture.json` and `result_contract.json` leaves. Give each unit one disposition:

| Disposition | Meaning |
|---|---|
| `INHERITED_UNCHANGED` | Maps to a requirement |
| `SUPERSEDED_BY_REV04 §x` | Cites the superseding unit. Examples: single-shot SSH → §4; generic exception→integrity → §8.6; Attempt-001 identifiers → §2 |
| `NOT_APPLICABLE_TO_SUCCESSOR` | Not carried forward, with a reason |

The guard should then require that every C row cites at least one `INHERITED_UNCHANGED` control-definition unit.

**(b) Policy roots.** Add to `POLICY_ROOTS`:

- `forbidden`
- `invalid_reason_subclasses`
- `primary_scored_classifications`
- `run_dispositions`
- `processing_states`
- `predecessor`

Give `optional_nonbinding_diagnostics` an explicit `NON_NORMATIVE` disposition instead of silently dropping it. Recording why each remaining top-level key (`schema`, `status`, `draft_*`, approval booleans) is non-normative would also let the guard fail on any *new* top-level key.

**(c) Table structure.** Drop separator rows. Attach the header row's text to each data-row unit as context rather than making the header a mapped unit. Today 5 separators and 5 headers are "normative units", and the separators are mapped to R13.

### F-2. Mapping quality: section defaults must be replaced by reviewed per-unit mappings (blocking)

Of the 22 flagged warnings, I agree with the flags. For example, `CONTRACT-L0012` carrying 17 requirement IDs is a section-level catch-all.

The larger problem is in unflagged rows. Clear errors I verified:

| Unit(s) | Current mapping | Correct mapping |
|---|---|---|
| §8.4 evidence-state rows L0150–L0152 | R13 | **R11** |
| §8.4 G1 L0156; precedence rows L0166, L0167, L0170 | R13 | **R12** (+R11) |
| §8.2 L0128 VERIFIER_ERROR handling | R13 | **R14** (+R13) |
| §8.1 L0120 pre-claim KAT | R13, R24 | **R14**, R24 |
| §8.5 L0180 rejection layer | R13 | **C02–C10** |
| §8.5 L0182 old-digest set | R13 | **R23** |
| §8.5 L0184 forbidden-API scan scope | R13 | **R22** |
| §8.5 L0186 virtual CTAP2 limits | R13 | **R40**, R06 |
| §8.6 exception-site rows L0194–L0211 | R13 | **R15**, plus R03 (input rows), R05 (SSH rows), R07 (WebAuthn rows), R17 (interrupt row) |
| §8.6 L0198 Ctrl+C row | R13, **R32** (scorer determinism) | R17 |
| §7 L0112 Windows Node Ctrl+C isolation | **R22** (pre-claim browser) | R17, R35, R38 |
| §8.3 L0132 domain isolation | R13 | R01, R23 |
| §8.3 L0136 crash-atomic snapshots | R13 | R16, R35 |
| §8.3 L0138 named witness | R13 | R16, R35 |
| §2 L0026 templates and old-digest set | R01 only | + R23, R33 |
| §6 L0098 interactions, consultation, receipts | R08 only | + R27, R28 |
| policy `browser_node_interrupt.*` | R07 | R17, R35 |
| policy `rejection_layer_values[*]` | R13 | control rows |
| C11, C12 ← L0016 | keyword collision | §2.5/§7 dependency units plus inherited V02 C07/C08 units (F-1) |
| R19 ← L0012 only | generic | §8.3 L0134 ("Never log a private key…"), §2.4 |
| R34 (F1/F2) ← L0264 "C5 policy schema" | unrelated | no REV04 source (see below) |
| R35 (two streams) ← L0172 instrument summary | unrelated | no REV04 source (see below) |

**Requirement provenance.** R34–R40 come from Message 029 engineering obligations, not from REV04. The guard's "orphan requirement without approved-source clause" rule therefore forces them onto unrelated REV04 units, and that rule is what manufactured several of the errors above.

**Correction:**

- Allow a second provenance type, `REVIEW_DERIVED_ENGINEERING`, which cites an MC-0030 message and section.
- The guard requires each requirement to have either a REV04 or V02 unit **or** recorded review provenance.
- The rows R22–R40 currently carry titles as `rule`. Each needs a testable rule statement with a pass criterion, like R01–R21.

**Review mechanics.**

- Replace the single `mapping_review` constant with a per-unit record: status `APPROVED`/`REJECTED`, reviewer identity, review message reference.
- The guard requires all units `APPROVED` before an F1 status is allowed.
- The reviewer must not be the mapping author.
- Units containing several obligations must carry several requirement IDs, or be split. Thirteen long single-paragraph units with a single mapping are prime candidates, for example L0136 at about 1,900 characters.

### F-3. Test catalogue: layers and independence fields are placeholders (blocking for F1)

**Oracle and forbidden-code fields.**

- 101 of 105 tests have the same `oracle_source`: `F1_INDEPENDENT_EXPECTED_VECTOR_OR_DECISION_TABLE`.
- 98 have `forbidden_shared_code: ["p01_score"]`, and the remaining 7 have `["p01_owner", "p01_core", "p01_rp"]`.

These values do not encode per-test independence, and in places they invert it:

- For harness and core tests (T-CTRL-*, T-SSH-*, T-ATOMIC-*), the constraint that matters is that **expected values must not be computed by `p01_core`/`p01_owner`**, the code under test. Forbidding `p01_score` is irrelevant there.
- **T-VECTOR-NVERSION** forbids `p01_core`, yet it *is* the comparison of `p01_core` against `p01_oracle`. The real constraint is "`p01_oracle` source never imports or reads `p01_core`".

**Correction:** split the field into two:

- `expected_value_origin`: frozen F1 vector ID, decision-table row set, or N-version agreement;
- `must_not_derive_from`: the modules the expectation must be independent of.

Define the semantics in the catalogue header.

**Layer errors.**

| Test(s) | Current layer | Should be | Reason |
|---|---|---|---|
| T-SSH-PROMPT, T-SSH-ABORT, T-SSH-RETRY-PRECONDITION | `PURE` | `WINDOWS_NATIVE` | Need native `ssh-keygen` under ConPTY |
| T-ATOMIC-SNAPSHOTS | `PURE` | `WINDOWS_NATIVE` | Filesystem semantics |
| T-CTRL-C-NODE, T-CTRL-C-SSH | `INTEGRATED_SYNTHETIC` | `WINDOWS_NATIVE` | Console control events |
| T-KAT-SSH, T-KAT-WEBAUTHN | `PURE` | integrated | REV04 requires the KAT in the actual harness environment |
| T-TARGET-MACHINE-SYNTHETIC | `WINDOWS_NATIVE` | `OWNER_MACHINE_MANUAL` | It is not CI |

**No test uses the `OWNER_MACHINE_MANUAL` layer**, yet REV04 §4 mandates "a manually observed native-prompt visibility receipt". Add T-NATIVE-PROMPT-VISIBILITY (`OWNER_MACHINE_MANUAL`, F2).

### F-4. Decision table: correct as far as it goes; three oracle layers are missing (blocking for F1)

The 288-row table is right. The six feasible per-arm triplets are correct: INCOMPLETE ∧ eligible is infeasible, because eligibility needs S01–S03 successes, which makes P0/S01–S03 terminal. My independent recomputation agrees on all rows. But it is the thinnest layer of the oracle. F1 needs three more data tables, each frozen before the scorer exists:

**(a) Viability and eligibility derivation oracle.**

- Inputs: per-arm 13 control results (PASS/FAIL/UNEXECUTED); S01/S02/S03/L01 success and terminal outcome; unrounded mechanical seconds (or null); infrastructure receipts (valid/invalid/absent); metadata edits; secret exposure; required-field presence; friction-rating validity.
- Outputs: `proof_viable` and `selection_eligible`.
- Boundary vectors:
  - median exactly 60.000 (passes) versus 60.000001;
  - a small trial exactly 120.000 versus 120.000001;
  - a small trial over 120 with a valid infrastructure receipt (max check exempt, but its raw value still in the median);
  - L01 over 120 with a receipt (never exempt);
  - a null measurement (fails, never zero);
  - an empty friction note (allowed) versus a null rating (fails).

**(b) Selection and volume oracle, with a coupling the binary input hides.** Projected minutes are `97 × median_small(selected arm) / 60`. The ≤90-minute gate is therefore equivalent to **selected median ≤ 5400/97 ≈ 55.670 s**, which is *tighter* than the 60 s eligibility gate. Consequences:

- Any eligible arm with median in (55.670, 60] passes eligibility and fails volume, giving AMEND.
- Because volume is evaluated on the **selected** arm, the frozen selection rule can pick an arm that fails volume while the other would pass. Example: both eligible, A median 54 s, B median 58 s, |Δmedian| < 10 s, |ΔL01| < 15 s → B tie-break → 97 × 58/60 ≈ 93.8 min → **AMEND**, although A would give ≈ 87.3 min.

This follows the frozen rules (I am not proposing to change them). But the oracle must contain these cases explicitly, together with:

- exact 10.000 s and 15.000 s deltas (the rule says "at least 10" and "at least 15", so equality selects by the metric);
- the both-eligible tie to B;
- the projected-acceptance gate, which is constant 97 ≤ 100 and should be asserted as such.

The owner-facing authorization package (B09) should state plainly that the volume gate implies a ~55.7 s median ceiling.

**(c) B02 stopping-policy oracle.**

- Inputs: claims used (0, 1, 2); prior class and reason; the five `ALL_REQUIRED` conditions; hypothesis type (instrument repair or new mechanism); PASS terminality.
- Output: permitted next action.
- Cases must include:
  - `NOT_RUN`;
  - PASS (with or without G2) → no claim;
  - `INVALID_INTEGRITY` → no exception;
  - `INVALID_INSTRUMENT` → repair may keep the hypothesis;
  - `INVALID_INCOMPLETE` / AMEND / REOPEN → a new hypothesis is required;
  - four of five conditions true → denied;
  - cap reached → denied.

This table is small, but it is the oracle for the owner-approved B02 policy and does not exist yet.

**Minor point.** Decision-table rows where an eligible arm's volume fails while the other arm is INCOMPLETE produce AMEND with no G2-style disclosure. That matches the approved text, where G2 attaches to PASS. Recording `other_arm_incomplete` as a disclosure field on AMEND rows as well would cost nothing and helps the owner package.

### F-5. Oracle independence: assign authorship and blindness explicitly (should fix before F1)

"Two separately authored implementations" is not independent if one collaborator writes both.

**Correction:**

- Name the authors in the F1 plan. For example, `p01_core` by Codex under ChatGPT orchestration, and `p01_oracle` by a different collaborator (Claude, or a fresh, separately prompted Codex session). The oracle author works from F1 specification text only, with a blindness attestation on the MC-0029 D-1 Evaluator B pattern: no access to `p01_core` source or its outputs before the oracle is committed.
- Apply the same separation to the derivation and B02 tables in F-4 and to the scorer.
- My recomputation in §0 is one small independent data point for the 288-row layer. It is not a substitute for this procedure.

### F-6. Two-stream evidence: define the tail rule (should fix)

The RP must persist a ceremony receipt **before** acknowledging it to the harness, so a crash between those two steps leaves RP receipts *after* the last head the harness bound. That is legitimate, not a chain break.

**Correction:** freeze the scorer rule:

- RP receipts beyond the last harness-bound head are admissible when (i) their own chain verifies, and (ii) the owner final witness covers the RP head.
- Without the witness, they are scored as disclosed-unwitnessed evidence, consistent with `final_head_witness_absent` being disclosure-only.
- A harness-bound RP head that does **not** appear in the RP stream is a chain break (integrity).

Add T-RP-TAIL-AFTER-CRASH.

### F-7. One intra-REV04 inconsistency the clause audit should have surfaced (should fix in F1)

- §4.1 says that, before each SSH invocation, "any failed check is terminal; preserve the safe reason". That reads as event-terminal.
- §8.6 says "public key header/role/agent change … `INTEGRITY` if frozen structural identity/contract check fails". That reads as attempt-level, with no exception.

For an agent-cache detection or a statement-file mutation between invocations, the two give different outcomes. §8.6 is the more specific and later rule. F1's error-category vocabulary should record the resolution explicitly, presumably §8.6 governs and §4.1 "terminal" means the event stops *and* the integrity flag is set. The resolution should come with a test.

This is not a B01/B02 change. It is an ambiguity that a per-unit semantic review would catch, which is the purpose of F-2.

### F-8. Confirmations

- **Arm B P5 dependency.** Correct per frozen V02 addendum §9 (P01-C07): B's V2 is PRIMARY = Arm-A primary, RECOVERY = Arm-A recovery. The ordinary-rotation negative candidate for B is also the Arm-A primary (V02 `harness.py`), so the same `UNEXECUTED_ROTATION_TARGET_ABSENT` rule covers it. Note for the owner package: B's eligibility is structurally contingent on A setup succeeding in the same attempt.
- **F1/F2 split.** Correct. F1 explicitly excludes source-specific error sites and runtime versions; F2 binds them along with the F1 hash.
- **Blob-basis hashing.** Fixed, using `git show HEAD:path`, which applies no end-of-line conversion. The guard KAT on `abc` is a sensible environment self-check.
- **Windows and virtual-WebAuthn plans.** Adequate as obligations. One additional limitation to record: `NotSupportedError` cannot be produced faithfully by a virtual authenticator, only by stubbing the client API, so T-WEB-CAPABILITY qualifies the client code path, not platform capability detection.

## 3. Minimum corrections before an F1 freeze can be proposed

1. Inventory scope: V02 inherited units with dispositions; the six missing policy roots; explicit `NON_NORMATIVE` dispositions; table header and separator handling (F-1).
2. A per-unit semantic re-mapping by a non-author reviewer, with per-unit approval records; the 22 listed corrections; `REVIEW_DERIVED_ENGINEERING` provenance for R34–R40; full rule text for R22–R40; multi-requirement mapping for dense units (F-2).
3. Test catalogue: `expected_value_origin` and `must_not_derive_from` per test; layer corrections; an `OWNER_MACHINE_MANUAL` native-prompt receipt (F-3).
4. Three further F1 oracle tables: viability/eligibility derivation with numeric boundaries; selection and volume including the 5400/97 s coupling; the B02 stopping policy (F-4).
5. Named oracle authorship with a blindness attestation (F-5); the RP tail rule (F-6); the §4.1/§8.6 resolution (F-7).

**Is a deeper clause-by-clause audit necessary before F1?** **Yes.** The structural guard should stay as the regression net. Semantic approval must come from the per-unit review in item 2. I can perform that audit as a separate bounded task if routed. If I do, I should not also author the oracle, so that roles stay separated (F-5).

## 4. Unchanged boundaries

- B01/B02 accepted and not reopened.
- Attempt 001 immutable AMEND.
- All 13 controls with zero misses, 1/2/4/30 effects, 60/120/120-second gates, volume gates, A/B selection with the B tie-break, C ineligible, no pooling, secret boundary.
- F1 and F2 unfrozen. The third human approval is required before any owner key, marker or ceremony. Attempt 002 is not authorized.
- GOVERNED_LEDGER_KERNEL_V02 unselected; R0-P02 PASS; R0-P03 pending; Specification 028 unchanged.

```text
MC0030_MESSAGE031=CLAUDE_Q0_REV02_F1_F2_REVIEW
DISPOSITION=AMEND_REV02_Q0_TARGETED
DEEPER_CLAUSE_AUDIT_BEFORE_F1=REQUIRED
INVENTORY_LINE_COVERAGE=COMPLETE_FOR_REV04_SECTIONS_1_11
DECISION_TABLE_288=INDEPENDENTLY_RECOMPUTED_288_OF_288_AGREE
BLOCKING=F1_INHERITED_V02_AND_POLICY_ROOTS;F2_SECTION_DEFAULT_MAPPINGS;F3_CATALOGUE_PLACEHOLDERS;F4_MISSING_DERIVATION_SELECTION_VOLUME_B02_ORACLES
ALSO=F5_ORACLE_AUTHORSHIP;F6_RP_TAIL_RULE;F7_SECTION4_VS_8_6
B_P5_DEPENDENCY=CONFIRMED
ATTEMPT_002=NOT_AUTHORIZED
NEXT=CHATGPT_RECONCILIATION
```
