# MC-0030 Message 033: Claude independent clause audit, batch Q0-AUDIT-001 (V01 security-control contract)

```text
Thread                  MC-0030
Message                 033
Author / reviewer       Claude / claude-04 (independent clause auditor)
Conversation            04 - Assurance and Delivery Architecture Design
Coordination branch     v1-source-vault-bootstrap-resume
Reviewed HEAD           fe240ba8c983589baefaf6c222176bf126facf36
Batch                   Q0-AUDIT-001 / V01_CONTROLS / 49 units
Batch unit-list SHA-256 e11e647ce69c4e47354b282e1143fcbc00ca4c814fd307ea5bea0c4809d75597 (recomputed: match)
Source                  experiments/r0_p01_owner_acceptance_v01/security_control_contract.md
Source SHA-256          aad6e99387da888662c3a2d66bb573cb4b35db6f0d6a29371417700ce4222705 (Git blob, matches inventory)
Cross-checked against   V02 addendum AC-3..AC-6, P01-C06..C09, C14 (V02_ADDENDUM-L0024..L0290);
                        approved REV04 contract (REV04_CONTRACT-L0012..L0207); Q0 REV02 trace; REV03 test catalogue
Disposition             AMEND_AUDIT_BATCH001
Role separation         I am not, and will not be, the author of the blind second golden-vector
                        implementation or the independent scorer.
Authority               Audit record only. No F1/F2 freeze, inventory edit, credential or Attempt 002.
```

## 0. Verification and audit method

- `git ls-remote` returned `fe240ba8c983589baefaf6c222176bf126facf36`, the expected HEAD. Routing is at checkpoint 869, boundary `p-one-inherited-clause-audit-first-batch`. MC-0030 `STATE.json` is `OPEN`, `R0_P01_F1_INHERITED_AUDIT_BATCH001_PENDING`, `next_expected_actor = claude`. No contradiction found.
- **Structural checks I ran on an isolated extracted copy:**
  - The batch's 49 IDs hash to the plan's `unit_id_list_sha256` (`"\n".join(ids)+"\n"`).
  - All 49 `text_sha256` values match the exact source lines.
  - The 49 units plus five excluded preamble lines (3, 4, 5, 7, 9) cover every non-blank, non-heading line of the file.
  - No other `V01_CONTROLS` units exist in the inventory.
- **Method.** Each unit was read against its V01 section, then traced to:
  - its V02 refinement (addendum P01-C06 control table, C07 rotation, C08 recovery, C09 compromise, AC-3..AC-6, C14 normalization);
  - its REV04 successor treatment (structural pre-checks, tri-state VERIFY, owner ACCEPT rule, bounded SSH invocations, fresh keys, rejection layers).

  The automatic `candidate_requirement_ids` and prior REV02 hints were **not** used as evidence. Requirement IDs below are the reviewed associations, using Q0 REV02 IDs.
- **Status vocabulary.** `ACCEPTED` means the disposition and mapping are reviewed and settled. `PENDING` means the unit is reviewed, but a named blocker must be resolved before its mapping can be approved for F1.

## 1. Verdict

**`AMEND_AUDIT_BATCH001`.**

All 49 units plus the 5 excluded preamble lines are audited below:

- 39 units `ACCEPTED`;
- 10 units `PENDING`, each with a concrete blocker;
- 3 excluded preamble lines (5, 7, 9) are normative and must be added as units;
- 2 excluded preamble lines (3, 4) are correctly non-normative.

The 13-control *definition set* is complete and internally consistent with V02 and REV04, so I do not return `REOPEN_CONTROL_COVERAGE`. The amendments concern **test vectors that do not exercise what the control claims**, inventory scope, unit splitting and missing requirement rule text.

Two findings matter beyond bookkeeping:

1. **C02's frozen V02 vector never exercises signature verification** (A1). V02 P01-C06 row 2 XORs the *first* proof byte:
   - For SSH, the first byte of the decoded SSHSIG blob is the `"SSHSIG"` magic preamble, so the mutation is rejected by the parser.
   - For WebAuthn, the first byte of the DER signature is the `0x30` SEQUENCE tag, so the mutation is rejected by DER decoding.

   C02 therefore PASSes even if the cryptographic check were absent. It is a structural rejection, not a forged-proof rejection.
2. **C09's frozen V02 vector is tautological** (A2). It adds an *in-memory* `repository_note` that no verifier or semantic-base computation reads, so it cannot detect the whole-repository binding that V01 line 77 says the control exists to prevent.

Both corrections are **strengthenings within unchanged predicates**, which V01 §14 line 145 and REV04 L0087 permit, prospectively for the successor. Neither touches Attempt 001.

## 2. Per-unit audit record (all 49 units)

Notation:

- `INH` = `INHERITED_UNCHANGED`
- `SUP` = `SUPERSEDED_BY_REV04`
- `N/A` = `NOT_APPLICABLE_TO_SUCCESSOR`
- `V02:Lnnnn` = `V02_ADDENDUM-Lnnnn`
- `R4:Lnnnn` = `REV04_CONTRACT-Lnnnn`
- `Layer` = expected `rejection_layer` under REV04 L0180

### §1 VALID_ACCEPTANCE (C01)

| Unit | Normative meaning | Reviewed IDs | Disp. | Basis / successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTROLS-L0013 | One owner-authenticated baseline proof (P0) over the exact SignedAcceptanceStatement, made with the *current* registered credential | C01, R25, R04 | INH | V02:L0161/L0185. R4:L0087: the owner must ACCEPT P0, and a non-ACCEPT is a failed positive control that is not retried. Successor keys are fresh (R4:L0023/L0024). | ACCEPTED |
| V01_CONTROLS-L0015 | PASS iff (i) independent VERIFY = VALID **and** (ii) the acceptance ID was unconsumed, i.e. the first ADMIT succeeds | C01, R14, R36 | INH | V02:L0185, L0044 (stateless VERIFY), L0046/L0048 (stateful ADMIT, first admitted decision consumes the ID). R4:L0126: tri-state VERIFY. A `VERIFIER_ERROR` is not a C01 FAIL; it ends the run as `INVALID_INSTRUMENT` (R4:L0128). "Independent" in the successor means the in-trial verifier *and* the scorer's separate in-process re-verification (R36). | ACCEPTED |

### §2 FORGED_OR_AGENT_PREPARED_PROOF_REJECTS (C02)

| Unit | Normative meaning | Reviewed IDs | Disp. | Basis / successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTROLS-L0019 | Mutate proof bytes without any owner credential use | C02 | INH | V02:L0186 fixes the vector as "XOR the first raw proof byte". **A1:** that byte is the SSHSIG magic or the DER tag, so the mutation is structurally invalid and never reaches signature math. | **PENDING**: F1 must add a structurally valid signature-value mutation (A1) |
| V01_CONTROLS-L0021 | PASS iff VERIFY rejects | C02, R14 | INH | Layer must be recorded. With the V02 vector it is STRUCTURAL. The control name claims forged-proof rejection, which requires a CRYPTOGRAPHIC rejection of a well-formed proof. | **PENDING** (A1) |
| V01_CONTROLS-L0023 | The harness must never manufacture a replacement valid proof | C02, R26, R05, R07 | INH | A cross-cutting anti-fabrication rule, broader than C02. It matches V02:L0186 ("never replace it with a valid forged proof"), V02:L0196, V02:L0246 ("do not request another owner proof"), R4:L0070 (no fourth invocation), and the REV04 no-replacement-assertion rule. Recommend stating it once as a cross-cutting requirement rule rather than only under C02. | ACCEPTED |

### §3 CHANGED_ENVELOPE_REJECTS (C03)

| Unit | Normative meaning | Reviewed IDs | Disp. | Basis / successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTROLS-L0027 | Change one semantic envelope field after proof creation and reuse the original proof | C03 | INH | V02:L0187 (append `" [MUTATED]"` to the base effect text). Successor fixture identifiers must be re-pinned in F1. | ACCEPTED |
| V01_CONTROLS-L0029 | Recompute `envelope_digest` attacker-consistently, so that the presented statement is internally consistent but differs from what was signed | C03 (pattern also governs C04, C08) | INH | This is the rule that makes C03, C04 and C08 *cryptographic* tests rather than digest-mismatch tests. F1 test assertion: the presented digest equals the recomputed digest of the mutated object. | ACCEPTED |
| V01_CONTROLS-L0031 | PASS iff the original proof rejects against the changed statement | C03 | INH | Expected layer: CRYPTOGRAPHIC. A structurally valid modification must reach crypto rejection (R4:L0180). | ACCEPTED |

### §4 CHANGED_SHOWN_VIEW_REJECTS (C04)

| Unit | Normative meaning | Reviewed IDs | Disp. | Basis / successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTROLS-L0035 | Change one byte of the exact displayed owner view, recompute `shown_digest`, reuse the proof | C04, R02 | INH | V02:L0188 ("first displayed byte R→X") is tied to the V02 view header. The successor renderer and header bytes must be re-pinned, and the mutated byte must be chosen from the frozen successor view. | ACCEPTED |
| V01_CONTROLS-L0037 | PASS iff the original proof rejects | C04 | INH | Expected layer: CRYPTOGRAPHIC. | ACCEPTED |

### §5 DECISION_SUBSTITUTION_REJECTS (C05)

| Unit | Normative meaning | Reviewed IDs | Disp. | Basis / successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTROLS-L0041 | Replace ACCEPT with REJECT in the presented statement and reuse the proof | C05, R25 | INH | V02:L0189. Precondition: P0 is an ACCEPT. If the owner chose otherwise, C01 fails and C05 is `FAIL / UNEXECUTED_DEPENDENCY_ABSENT` or must operate on the actual decision; F1 must state which (R25/R26). | ACCEPTED |
| V01_CONTROLS-L0043 | PASS iff VERIFY rejects | C05 | INH | Expected layer: CRYPTOGRAPHIC. | ACCEPTED |
| V01_CONTROLS-L0045 | AMEND substitution is "equivalent" and needs no second owner proof | C05 | INH | **Ambiguity:** this line is read either as "one mutation suffices" or as "test AMEND too, offline". An offline AMEND vector costs nothing and removes the ambiguity. | **PENDING**: F1 decision; recommend both ACCEPT→REJECT and ACCEPT→AMEND offline vectors |

### §6 CROSS_PROJECT_REPLAY_REJECTS (C06)

| Unit | Normative meaning | Reviewed IDs | Disp. | Basis / successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTROLS-L0049 | Replace `project_id` with `OTHER-PROJECT-SYNTHETIC` and reuse the proof | C06, R01 | INH | V02:L0190 (`fixture.wrong_project_id`). Under R4:L0132 the successor rejects a wrong project **structurally** before crypto, and R4:L0180 accepts this. Recommend a non-gating diagnostic that also runs the cryptographic verifier on the mutated statement, so the crypto path is shown to reject too (A4). | ACCEPTED |
| V01_CONTROLS-L0051 | PASS iff verification rejects | C06 | INH | Expected layer: STRUCTURAL (REV04). Cross-*attempt* (old-context) replay is a separate REV04 requirement (R01/R23), not a redefinition of C06. | ACCEPTED |

### §7 ACCEPTANCE_ID_REPLAY_REJECTS (C07)

| Unit | Normative meaning | Reviewed IDs | Disp. | Basis / successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTROLS-L0055 | C07 consists of two distinct replay classes | C07 | INH | Normative framing for L0057/L0060. | ACCEPTED |
| V01_CONTROLS-L0057 | Class A: the same proof attached to a different `acceptance_id` must be rejected **by cryptographic verification** | C07, R01 | INH | V02:L0191 uses replacement ID `R0-P01-<ARM>-SEC-ACCEPTANCE_ID_REPLAY_REJECTS`, which is *old* grammar. Under the REV04 prefix rule (R4:L0132) that ID fails **structurally**, so the "cryptographic verification must reject" requirement of line 58 is no longer exercised. **A3:** F1 must specify a successor-grammar replacement ID, for example `R0-P01-002-<ARM>-SEC-ACCEPTANCE_ID_REPLAY_REJECTS`. | **PENDING** (A3) |
| V01_CONTROLS-L0060 | Class B: an exact consumed statement and proof presented again may still VERIFY, but **ADMIT** must reject the repeated ID | C07, R36 | INH | V02:L0191 B; AC-4 (V02:L0046/L0048). Successor: the scorer must independently replay admission (R36), not trust a harness flag. Expected layer: ADMIT. | ACCEPTED |
| V01_CONTROLS-L0063 | C07 PASS requires both classes | C07 | INH | Conjunction. Two rejection layers must be recorded (A3 and ADMIT). | ACCEPTED |

### §8 SEMANTIC_BASE_MISMATCH_REJECTS (C08)

| Unit | Normative meaning | Reviewed IDs | Disp. | Basis / successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTROLS-L0067 | Change `semantic_base_digest` and reuse the proof | C08 | INH | V02:L0192 refines this to an attacker-consistent mutation (change `lineage_head` in a copied base and recompute the digest), applying the L0029 pattern. **Scope note:** C08 tests tamper-under-old-proof (a VERIFY reject). A *genuinely signed* stale base is the separate ADMIT stale-base rule (AC-4, V02:L0046), which C08 does not cover. | ACCEPTED |
| V01_CONTROLS-L0069 | PASS iff VERIFY rejects | C08 | INH | Expected layer: CRYPTOGRAPHIC. | ACCEPTED |

### §9 UNRELATED_REPOSITORY_LANDING_DOES_NOT_INVALIDATE (C09)

| Unit | Normative meaning | Reviewed IDs | Disp. | Basis / successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTROLS-L0073 | Introduce a synthetic unrelated carrier or repository metadata change outside every statement field | C09 | INH | **A2:** V02:L0193 adds only in-memory metadata that nothing reads, so the control cannot fail and cannot detect what L0077 targets. | **PENDING** (A2) |
| V01_CONTROLS-L0075 | PASS iff the unchanged statement and proof still verify exactly | C09 | INH | Positive control. In the successor it should also assert that the recomputed `semantic_base_digest` is unchanged (AC-3, V02:L0038) and that a fresh-ledger ADMIT succeeds. | **PENDING** (A2) |
| V01_CONTROLS-L0077 | Purpose: prevent accidental whole-repository binding | C09 | INH | Normative purpose clause (AC-3: the base binds governing state, never repository state). It defines what the test must be capable of detecting, and is the basis for A2. | ACCEPTED |

### §10 SIGNER_SET_MISMATCH_REJECTS (C10)

| Unit | Normative meaning | Reviewed IDs | Disp. | Basis / successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTROLS-L0081 | Change `signer_set_version` and reuse the proof | C10 | INH | V02:L0194 (`SIGNERS-P01-V999-SYNTHETIC`). REV04 does not structurally pre-check the version, so rejection is cryptographic. A genuinely signed but non-current version is the AC-2 ADMIT rule (V02:L0032), outside C10. | ACCEPTED |
| V01_CONTROLS-L0083 | PASS iff VERIFY rejects | C10 | INH | Expected layer: CRYPTOGRAPHIC. | ACCEPTED |

### §11 TRUST_ROOT_ROTATION_DRY_RUN (C11)

| Unit | Normative meaning | Reviewed IDs | Disp. | Basis / successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTROLS-L0087 | Construct a synthetic signer-set rotation envelope | C11, R33 | INH | V02:L0200/L0202 envelope; R4:L0026 key-slot templates instantiated at runtime from same-attempt public members; scorer re-instantiation (R33). | ACCEPTED |
| V01_CONTROLS-L0089 | The **current** PRIMARY signs the exact rotation statement (P5) | C11, R25, R05 | INH | For A this is the SSH primary (bounded invocations, R4:L0064–L0070). For B it is the WebAuthn primary (single assertion, R4:L0073). The owner must ACCEPT (R4:L0087). | ACCEPTED |
| V01_CONTROLS-L0091 | "PASS only if" introduces the conjunction L0093 | C11 | INH | Framing. | ACCEPTED |
| V01_CONTROLS-L0093 | Four conjuncts: (a) the current proof verifies; (b) the proposed new signer's public fingerprint is visible in the rendered effect; (c) the candidate or new signer alone cannot authorize the rotation; (d) the version changes only after the current proof is admitted | C11, R02, R33 | INH | (a) V02:L0215; (b) a sign-what-you-see obligation, so the T1 view bytes must contain both target member IDs (R02); (c) V02:L0217 role-admission predicate evaluated *without* a new owner proof; (d) V02:L0215 "VERIFY and role-correct ADMIT must succeed before the version changes". **Split required:** four independently testable assertions, one test each. | ACCEPTED (split requested) |
| V01_CONTROLS-L0098 | Arm A's target signer *may* be the recovery key | C11, R33 | SUP | Made exact by V02:L0215 (A: V2 PRIMARY = A recovery, RECOVERY = A primary), applied to fresh same-attempt keys by R4:L0023 and R4:L0026. The permissive "may" is superseded by the exact V02 target set. | ACCEPTED |
| V01_CONTROLS-L0100 | Arm B's target *may* be the Arm-A primary; heterogeneous signer sets are allowed | C11, R33 | SUP | Made exact by V02:L0215 (B: V2 PRIMARY = A primary, RECOVERY = A recovery) with R4:L0023. The resulting dependency (B P5 is impossible without same-attempt A members, giving `FAIL / UNEXECUTED_ROTATION_TARGET_ABSENT`) exists only as the Research 532/533 fixture clarification. There is **no REV04 unit to cite** for it. | **PENDING**: record the clarification as a citable F1 fixture unit |
| V01_CONTROLS-L0102 | No production trust root changes | C11, R20 | INH | A probe-boundary rule. No current requirement row states "synthetic trust roots only; no production trust-root mutation" as testable rule text (R20 mentions only "no production authority switch" as evidence). | **PENDING**: add rule text (A6) |

### §12 RECOVERY_CREDENTIAL_DRY_RUN (C12)

| Unit | Normative meaning | Reviewed IDs | Disp. | Basis / successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTROLS-L0106 | The recovery public key is registered in the synthetic trust root (V1) **before** the dry run | C12, R04, R23 | SUP | "Preregistered" is superseded by R4:L0023/L0024: a fresh post-claim, same-attempt key, registered as a V1 member at setup (V02:L0157), with local inequality against Attempt 001 IDs (R23). The ordering semantic (member before P6) is retained. | ACCEPTED |
| V01_CONTROLS-L0108 | The owner signs a synthetic recovery-rotation statement (P6) with the recovery Ed25519 key | C12, R05, R25 | INH | V02:L0221/L0223/L0236. Successor: up to three owner-chosen invocations for P6 on both arms (R4:L0064–L0070, R4:L0073), and the owner must ACCEPT (R4:L0087). | ACCEPTED |
| V01_CONTROLS-L0110 | "PASS only if" introduces the conjunction L0112 | C12 | INH | Framing. | ACCEPTED |
| V01_CONTROLS-L0112 | Five conjuncts: (a) the recovery proof verifies; (b) an unregistered key cannot act as recovery; (c) recovery rotates the signer set prospectively; (d) prior accepted proofs stay historically valid; (e) no recovery secret enters the result | C12, R19, R13 | INH | (a) V02:L0236; (b) V02:L0238, a synthetic non-owner key that VERIFIES but is denied at ADMIT (`CURRENT_ROLE_DENIED`); (c) V2R (V02:L0236); (d) P0 re-verified at its V1 position (V02:L0240, AC-5 V02:L0052); (e) the secret boundary (R19) and `secret_exposure` integrity (R4:L0207). **Split required:** five assertions. | ACCEPTED (split requested) |
| V01_CONTROLS-L0118 | For both A and B, the recovery credential is the dedicated Arm-A recovery key | C12, R04, R33 | SUP | R4:L0024/L0110: the *new same-attempt* Arm-A RECOVERY key, never the Attempt 001 key or a B platform key. If absent, the control is `FAIL / UNEXECUTED_RECOVERY_MEMBER_ABSENT`. | ACCEPTED |
| V01_CONTROLS-L0120 | No production recovery path changes | C12, R20 | INH | Same as L0102. | **PENDING** (A6) |

### §13 COMPROMISE_BOUNDARY_DRY_RUN (C13)

| Unit | Normative meaning | Reviewed IDs | Disp. | Basis / successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTROLS-L0124 | Declare a synthetic compromise boundary for the current PRIMARY | C13 | INH | V02:L0244: `DECLARATION_TRUSTED_SYNTHETIC_INPUT`, boundary = 2. V02:L0056: the compromise-declaration *authority matrix* is R1 work, untested by C13. | ACCEPTED |
| V01_CONTROLS-L0126 | Use an already-created, otherwise-valid proof positioned after the boundary | C13, R26 | INH | V02:L0244: the S01 proof at seq3. If no valid S01 proof exists (including a B `WEBAUTHN_ASSERTION_NOT_COMPLETED` or an SSH no-proof event), C13 is FAIL and no new owner proof is requested (V02:L0246, R26). The classification is independent of S01's decision value (V02:L0054, "otherwise-valid records"). | ACCEPTED |
| V01_CONTROLS-L0128 | "PASS only if the harness classifies:" introduces L0130 | C13 | INH | Framing. Successor: the classification must be recomputed independently by the scorer (R36), not only reported by the harness. | ACCEPTED |
| V01_CONTROLS-L0130 | The post-boundary record is classified `REVIEW_REQUIRED`, `resolving_owner = GOVERNING_OWNER` | C13 | INH | V02:L0054/L0246. | ACCEPTED |
| V01_CONTROLS-L0133 | It is neither silently accepted as current nor used to retroactively invalidate pre-boundary records | C13 | INH | V02:L0246: "both rows are required evidence". **Split required:** (i) seq3 is not current; (ii) seq2 (P0) remains historically accepted. | ACCEPTED (split requested) |
| V01_CONTROLS-L0135 | A deterministic policy dry run requiring no extra credential secret | C13, R19 | INH | V02:L0244: no new signed declaration and no owner invocation. | ACCEPTED |

### §14 Zero-miss gate

| Unit | Normative meaning | Reviewed IDs | Disp. | Basis / successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTROLS-L0139 | The gate applies to A/B only; C is outside it | R10, R04 | INH | Consistent with preamble line 9 (N/A only for C) and REV04 C non-selectability. | ACCEPTED |
| V01_CONTROLS-L0141 | `eligible_security = all 13 controls PASS` | R10, C01–C13 | INH | Result contract `cryptographic_eligibility.all_13_security_controls = PASS`. UNEXECUTED counts as FAIL (V02:L0196, V02:L0284). Proof viability separately uses controls 1–10 (result contract), which this file does not mention. That is consistent, not conflicting. | ACCEPTED |
| V01_CONTROLS-L0143 | One FAIL makes the arm ineligible for PASS_WITH_SELECTION | R10, R12 | INH | Matches the B01 precedence (an eligible arm requires all 13). | ACCEPTED |
| V01_CONTROLS-L0145 | Controls may not be removed, weakened, renamed into success, or marked NOT_APPLICABLE post hoc after owner results | R10, C01–C13 | INH | Policy `forbidden.NO_SILENT_GATE_CHANGES`. **Consistency check against REV04:** REV04's result-informed changes do not alter any control predicate or name. They are structural pre-checks, rejection-layer diagnostics, bounded P6 invocations, same-attempt member rules and B P5/P6 `UNEXECUTED_*` outcomes. They are ceremony- and fixture-level, prospective for a new attempt, and disclosed (R4:L0064, `RESULT_INFORMED_PROSPECTIVE_CHANGE`). A1/A2 below are strengthenings. **Gap:** no Q0 requirement carries this anti-tuning rule as testable text. | **PENDING** (A6) |

### Excluded preamble lines (not in the batch; audited because they may be normative)

| Line | Text (abridged) | Normative? | Disp. | Action |
|---|---|---|---|---|
| 3 | `Status: PROSPECTIVELY FROZEN` | No (file status metadata) | N/A | Keep excluded |
| 4 | `Protocol: R0-P01-V01` | No (identity metadata; successor identity is R4:L0020 provisional `R0-P01-V01-I1`) | N/A | Keep excluded |
| 5 | `Applies to: every REALIZABLE owner-exclusive cryptographic arm` | **Yes**: the scope of all 13 controls | INH | **Add as a unit** → C01–C13, R04. Interplay: for an A/B arm that is NOT_REALIZABLE, V02:L0284 still records controls as FAIL/unexecuted, never NOT_APPLICABLE. That is consistent with line 9. |
| 7 | `The result vocabulary is public. There is no hidden oracle.` | **Yes**: transparency of control labels and predicates | INH | **Add as a unit** → R36. This does not conflict with the blind second-oracle author: blindness is about implementation independence, not hidden expected labels. |
| 9 | `Each control returns PASS or FAIL. NOT_APPLICABLE only for Arm C` | **Yes**: the control-result value domain | INH | **Add as a unit** → C01–C13, R04, R13. REV04 adds `rejection_layer` and `UNEXECUTED_*` *reasons* but keeps the PASS/FAIL domain. |

Heading lines (`## 1. VALID_ACCEPTANCE` … `## 14.`) carry the number↔key binding. They are correctly treated as heading context. The guard should assert that each C row's `control_key` equals its heading text. REV02 `security_control_key_bindings` does this positionally against `fixture.json`, and a heading cross-check would cost one line.

## 3. Amendments required (batch-level)

**A1. C02 must exercise signature verification.** Keep the V02 first-byte vector as a structural-rejection vector, and **add**:

- **(i) Well-formed signature-value mutations.**
  - SSHSIG: flip a bit in the last byte of the Ed25519 signature value inside the `signature` string, keeping all length prefixes and the magic intact.
  - WebAuthn: modify the ECDSA `s` integer while keeping the DER structure valid.
  - Both must be rejected with layer **CRYPTOGRAPHIC**.
- **(ii) An "agent-prepared" proof**, which the control's name covers and V01/V02 never test: a synthetic non-owner key signs the *exact* statement. Verifying it against the registered owner credential gives INVALID. This is distinct from C12(b), which is about the recovery role.

These are strengthenings under unchanged predicates. Tests: T-CTRL-02 gains three expected vectors (structural, cryptographic, agent-prepared).

**A2. C09 must be able to fail.** The unrelated change must enter the inputs from which the successor recomputes the semantic base, for example a repository-level field or commit metadata outside governing state, alongside the unchanged envelope, statement, view and proof. Assert:

- the recomputed `semantic_base_digest` is unchanged;
- VERIFY = VALID;
- a fresh-ledger ADMIT succeeds.

Add a paired negative fixture showing that the same harness *would* change the digest if a governing dependency changed (C08's lineage_head change already serves). Then a whole-repository binding regression is detectable.

**A3. C07 class A replacement ID** must follow successor grammar, so that rejection is cryptographic as V01 line 58 requires. Record layers: A = CRYPTOGRAPHIC, B = ADMIT.

**A4. C06 diagnostic.** Accept structural rejection as the gating result (R4:L0180), and additionally run the cryptographic verifier on the C06 mutation as a recorded, non-gating diagnostic. Otherwise no test shows that project_id is cryptographically bound for this arm.

**A5. Unit splits.** Split L0093 into 4, L0112 into 5 and L0133 into 2 independently testable assertions. C07 is already split (L0057/L0060). Each split assertion gets its own expected-vector ID in the REV03 catalogue, where T-CTRL-11/12/13 currently have one each.

**A6. Missing requirement rule text.** Add testable rule text, to an existing R row or a new one, for:

- (a) synthetic-only trust roots and recovery paths, with no production mutation (L0102/L0120);
- (b) the anti-tuning gate (L0145, policy `forbidden.NO_SILENT_GATE_CHANGES`): F1 freezes the 13 keys, names and predicates by hash, and any difference from V01 except recorded strengthenings fails the guard.

**A7. Inventory scope.** Add preamble lines 5, 7 and 9 as normative units. Lines 3 and 4 stay excluded with reason `METADATA`.

**A8. Fixture clarification unit.** Record the B P5 `UNEXECUTED_ROTATION_TARGET_ABSENT` rule (and its basis, V02:L0215) as a citable F1 fixture unit, so that L0100 and future scorer tests can reference an exact source.

**A9. Related gap, outside this file's text.** AC-6 (V02:L0060) states that RECOVERY "never [authorizes] ordinary acceptance in P01". No control and no planned test checks that a RECOVERY-signed *ordinary* statement is denied at ADMIT. This is not a change to C12. It belongs to the AC-6 audit batch, but it is recorded here so it is not lost. Suggested test: a recovery-key proof over an S-type statement gives `CURRENT_ROLE_DENIED`.

**C05 decision (L0045).** Recommend testing both ACCEPT→REJECT and ACCEPT→AMEND offline.

## 4. Machine-checkable receipt

```text
# unit_id | disposition | reviewed_requirement_ids | status | blocker
V01_CONTROLS-L0013|INHERITED_UNCHANGED|C01,R25,R04|ACCEPTED|
V01_CONTROLS-L0015|INHERITED_UNCHANGED|C01,R14,R36|ACCEPTED|
V01_CONTROLS-L0019|INHERITED_UNCHANGED|C02|PENDING|A1
V01_CONTROLS-L0021|INHERITED_UNCHANGED|C02,R14|PENDING|A1
V01_CONTROLS-L0023|INHERITED_UNCHANGED|C02,R26,R05,R07|ACCEPTED|
V01_CONTROLS-L0027|INHERITED_UNCHANGED|C03|ACCEPTED|
V01_CONTROLS-L0029|INHERITED_UNCHANGED|C03|ACCEPTED|
V01_CONTROLS-L0031|INHERITED_UNCHANGED|C03|ACCEPTED|
V01_CONTROLS-L0035|INHERITED_UNCHANGED|C04,R02|ACCEPTED|
V01_CONTROLS-L0037|INHERITED_UNCHANGED|C04|ACCEPTED|
V01_CONTROLS-L0041|INHERITED_UNCHANGED|C05,R25|ACCEPTED|
V01_CONTROLS-L0043|INHERITED_UNCHANGED|C05|ACCEPTED|
V01_CONTROLS-L0045|INHERITED_UNCHANGED|C05|PENDING|C05_AMEND_VECTOR_DECISION
V01_CONTROLS-L0049|INHERITED_UNCHANGED|C06,R01|ACCEPTED|
V01_CONTROLS-L0051|INHERITED_UNCHANGED|C06|ACCEPTED|
V01_CONTROLS-L0055|INHERITED_UNCHANGED|C07|ACCEPTED|
V01_CONTROLS-L0057|INHERITED_UNCHANGED|C07,R01|PENDING|A3
V01_CONTROLS-L0060|INHERITED_UNCHANGED|C07,R36|ACCEPTED|
V01_CONTROLS-L0063|INHERITED_UNCHANGED|C07|ACCEPTED|
V01_CONTROLS-L0067|INHERITED_UNCHANGED|C08|ACCEPTED|
V01_CONTROLS-L0069|INHERITED_UNCHANGED|C08|ACCEPTED|
V01_CONTROLS-L0073|INHERITED_UNCHANGED|C09|PENDING|A2
V01_CONTROLS-L0075|INHERITED_UNCHANGED|C09|PENDING|A2
V01_CONTROLS-L0077|INHERITED_UNCHANGED|C09|ACCEPTED|
V01_CONTROLS-L0081|INHERITED_UNCHANGED|C10|ACCEPTED|
V01_CONTROLS-L0083|INHERITED_UNCHANGED|C10|ACCEPTED|
V01_CONTROLS-L0087|INHERITED_UNCHANGED|C11,R33|ACCEPTED|
V01_CONTROLS-L0089|INHERITED_UNCHANGED|C11,R25,R05|ACCEPTED|
V01_CONTROLS-L0091|INHERITED_UNCHANGED|C11|ACCEPTED|
V01_CONTROLS-L0093|INHERITED_UNCHANGED|C11,R02,R33|ACCEPTED|SPLIT_4
V01_CONTROLS-L0098|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0023,L0026(+V02_ADDENDUM-L0215)|C11,R33|ACCEPTED|
V01_CONTROLS-L0100|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0023(+V02_ADDENDUM-L0215)|C11,R33|PENDING|A8
V01_CONTROLS-L0102|INHERITED_UNCHANGED|C11,R20|PENDING|A6
V01_CONTROLS-L0106|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0023,L0024|C12,R04,R23|ACCEPTED|
V01_CONTROLS-L0108|INHERITED_UNCHANGED|C12,R05,R25|ACCEPTED|
V01_CONTROLS-L0110|INHERITED_UNCHANGED|C12|ACCEPTED|
V01_CONTROLS-L0112|INHERITED_UNCHANGED|C12,R19,R13|ACCEPTED|SPLIT_5
V01_CONTROLS-L0118|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0024,L0110|C12,R04,R33|ACCEPTED|
V01_CONTROLS-L0120|INHERITED_UNCHANGED|C12,R20|PENDING|A6
V01_CONTROLS-L0124|INHERITED_UNCHANGED|C13|ACCEPTED|
V01_CONTROLS-L0126|INHERITED_UNCHANGED|C13,R26|ACCEPTED|
V01_CONTROLS-L0128|INHERITED_UNCHANGED|C13|ACCEPTED|
V01_CONTROLS-L0130|INHERITED_UNCHANGED|C13|ACCEPTED|
V01_CONTROLS-L0133|INHERITED_UNCHANGED|C13|ACCEPTED|SPLIT_2
V01_CONTROLS-L0135|INHERITED_UNCHANGED|C13,R19|ACCEPTED|
V01_CONTROLS-L0139|INHERITED_UNCHANGED|R10,R04|ACCEPTED|
V01_CONTROLS-L0141|INHERITED_UNCHANGED|R10,C01,C02,C03,C04,C05,C06,C07,C08,C09,C10,C11,C12,C13|ACCEPTED|
V01_CONTROLS-L0143|INHERITED_UNCHANGED|R10,R12|ACCEPTED|
V01_CONTROLS-L0145|INHERITED_UNCHANGED|R10,C01,C02,C03,C04,C05,C06,C07,C08,C09,C10,C11,C12,C13|PENDING|A6
# excluded preamble lines
V01_CONTROLS-line3|NOT_APPLICABLE_TO_SUCCESSOR|-|ACCEPTED|METADATA
V01_CONTROLS-line4|NOT_APPLICABLE_TO_SUCCESSOR|-|ACCEPTED|METADATA
V01_CONTROLS-line5|INHERITED_UNCHANGED|C01..C13,R04|PENDING|A7_ADD_UNIT
V01_CONTROLS-line7|INHERITED_UNCHANGED|R36|PENDING|A7_ADD_UNIT
V01_CONTROLS-line9|INHERITED_UNCHANGED|C01..C13,R04,R13|PENDING|A7_ADD_UNIT
# counts: 49 batch units (39 ACCEPTED, 10 PENDING); 5 preamble (2 N/A, 3 add-as-unit)
```

## 5. Attestation and boundaries

- **Reviewer:** Claude / claude-04, acting as independent clause auditor. I did not author the inventory, the batch plan or the candidate mappings. I will not author the blind second golden-vector implementation or the independent scorer.
- **Not claimed:** no other batch and none of the other 973 inventory units were audited. F1 is not approved.
- No file other than this message was written. No owner evidence, credential, key or WebAuthn state was touched.
- B01/B02 accepted and not reopened. Attempt 001 immutable AMEND. F1/F2 unfrozen. Attempt 002 not authorized.
- R0-P02 PASS; R0-P03 pending; physical target unselected; Specification 028 unchanged.

```text
MC0030_MESSAGE033=CLAUDE_AUDIT_BATCH001
DISPOSITION=AMEND_AUDIT_BATCH001
UNITS_AUDITED=49_OF_49
ACCEPTED=39
PENDING=10
PREAMBLE_NORMATIVE_TO_ADD=3
KEY_FINDINGS=A1_C02_VECTOR_STRUCTURAL_ONLY;A2_C09_VECTOR_TAUTOLOGICAL;A3_C07A_OLD_GRAMMAR_ID;A9_AC6_RECOVERY_ORDINARY_UNTESTED
CONTROL_DEFINITION_SET=COMPLETE_NOT_REOPENED
F1=NOT_APPROVED
ATTEMPT_002=NOT_AUTHORIZED
NEXT=CHATGPT_RECONCILIATION
```
