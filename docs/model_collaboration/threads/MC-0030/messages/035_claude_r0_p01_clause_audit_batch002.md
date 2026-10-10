# MC-0030 Message 035: Claude independent clause audit, batch Q0-AUDIT-002 (V02 addendum §2–§9)

```text
Thread                  MC-0030
Message                 035
Author / reviewer       Claude / claude-04 (independent clause auditor)
Conversation            04 - Assurance and Delivery Architecture Design
Coordination branch     v1-source-vault-bootstrap-resume
Campaign start HEAD     7f056f0cd33d7232eac5646a7b870624c9e23b4b
Batch                   Q0-AUDIT-002 / V02_ADDENDUM / 65 units / V02_ADDENDUM-L0024 .. V02_ADDENDUM-L0215
Batch unit-list SHA-256 recomputed from the plan's ordered IDs: match
Source                  experiments/r0_p01_owner_acceptance_v01/implementation_contract_addendum_v02.md
Source SHA-256          1d5344ad16498517c4178959d34d2c4966baa054d3ef1e1f5c75f4396dab0dd6 (Git blob, matches inventory)
Cross-checked against   REV04 contract (sha 9160a30c...), V01 security-control contract, Q0 REV02 trace R01-R40/C01-C13,
                        REV03 test catalogue, clarification_vectors_v02.json, harness.py (read-only)
Disposition             AMEND_AUDIT_BATCH002
Authority               Message 034. Audit record only. No F1/F2 freeze, inventory edit, credential or Attempt 002.
```

## 0. Verification and method

- `git ls-remote` returned `7f056f0cd33d7232eac5646a7b870624c9e23b4b` at campaign start, the expected HEAD. `scripts/check_r0_p01_clause_audit_receipts.py` returned `PASS batches=1/18 units=49/1022 accepted=39 pending=10` before this message, and `scripts/check_r0_p01_f1_audit_rev03.py` passed on the same tree.
- All 7 source SHA-256 values equal the inventory; the inventory SHA-256 equals the plan's `source_inventory_sha256`; all 18 batch unit-list hashes recompute.
- For this batch: the 65 IDs, in plan order, hash to the plan value; every unit's `text_sha256` equals the exact source lines; units plus the 14 recorded V02 exclusions (lines 3–8, 12, 14, 16, 18 outside numbered sections; 95/96 and 183/184 table syntax) cover every non-blank, non-heading line of the addendum, so nothing in the file is silently unindexed.
- Each unit was read in full, against its own section, against the V01 rule it refines, and against REV04. Candidate mappings in the inventory were empty and REV02 hints were not used as evidence. Reviewed IDs are my own associations to Q0 REV02 rule text.
- `ACCEPTED` = disposition and mapping settled by this reviewer. `PENDING` = reviewed, but a named blocker must be resolved before the mapping can support F1. Neither is F1 approval.
- **Status vocabulary for disposition column:** `INH` = INHERITED_UNCHANGED; `SUP:Lnnnn` = SUPERSEDED_BY_REV04 at REV04_CONTRACT-Lnnnn; `N/A` = NOT_APPLICABLE_TO_SUCCESSOR. `V02:` and `R4:` abbreviate V02_ADDENDUM and REV04_CONTRACT line IDs.

## 1. Verdict

**`AMEND_AUDIT_BATCH002`**: 65/65 units reviewed; **53 ACCEPTED, 12 PENDING**. Ten V02 lines outside the numbered sections were audited too (§3): three are normative and should become units.

The V02 architecture clarifications AC-1..AC-6 and P01-C01..C07 are internally consistent with REV04. REV04 replaces exactly four kinds of V02 value here: the statement context, the acceptance-ID prefix, the binary VERIFY output and the Attempt-001 key identities. Nothing in this batch conflicts with B01/B02 or Research 513 hard gates.

New findings beyond Message 033:

1. **B02-A1. AC-4 ADMIT predicates are only partly tested.** ADMIT has five predicates (V02:L0046). The control set exercises *unconsumed ID* (C07 class B) and *role* only for a non-owner key (C12). It never exercises ADMIT denial of a **genuinely signed** statement whose `signer_set_version` is stale after rotation (the explicit sentence at V02:L0032), or whose `semantic_base_digest` no longer equals the recomputed base. C10 and C08 test *tampering under an old proof*, which fails at VERIFY and never reaches ADMIT. A9 (RECOVERY over an ordinary statement) is the third missing ADMIT negative.
2. **B02-A2. Scenario isolation has no requirement rule text.** V02:L0137 requires separate per-arm, per-attempt, per-scenario ledgers with separate consumed-ID registries and no state leakage. No R row states it, and no catalogue test asserts it. Combined with A6(a) (no persistent/production ledger).
3. **B02-A3. The successor acceptance-ID strings are not enumerated.** REV04:L0025 fixes the prefix `R0-P01-002-` and requires "arm/item-specific grammar" as a structural VERIFY gate, but no approved text gives the exact ordinary and security ID strings that replace V02 `R0-P01-<ARM>-<TRIAL>` and `R0-P01-<ARM>-SEC-<KEY>`. Structural VERIFY (R01), A3 and the C04 view bytes all depend on them.
4. **B02-A4. Dependency policy clash (excluded line 18).** V02 line 18 confines implementation to the Python standard library and Node built-ins. R36's in-process SSHSIG verifier needs Ed25519 verification, which the Python standard library does not provide, and R39 contemplates hash-pinned dependencies. Neither the approved REV04 text nor a reviewed decision says which governs.
5. **A9 source identity and semantics (requested by Research 534).** See V02:L0060 below.

## 2. Per-unit audit record (65 units)

### AC-1 Envelope, statement and record

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V02_ADDENDUM-L0024 | Only the pre-decision canonical semantic proposal is hashed as `envelope_digest`; decision, view digest, proof, base digest, signer version, issued_at and provenance are excluded | R01, R02, C03 | INH | R4:L0031 (T1: envelope digest does not hash the view). Test: T-STATEMENT-GOLDEN must assert the excluded fields are absent from the canonical envelope. | ACCEPTED |
| V02_ADDENDUM-L0026 | The statement has exactly nine fields | R01 | INH | R4:L0025 preserves the nine field names; only context *value* and ID prefix change (see L0097). Exactly-nine must be asserted (no extra field) by structural VERIFY. | ACCEPTED |
| V02_ADDENDUM-L0028 | The durable record holds envelope, statement, proof and renderer/provenance; no proof hashes itself | R01, R16 | INH | R4:L0134 preserves V02 evidence fields. The Research 511/512 narrative sentences are interpretive history, not test rules. | ACCEPTED |

### AC-2 Signer authorization

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V02_ADDENDUM-L0032 | `signer_set_version` is always signed; ADMIT requires equality with the current version; a proof valid under an older set cannot authorize new admission after rotation | C10, C11, R01 | INH | C10 tests a *tampered* version under the old proof (VERIFY layer). Nothing tests a *genuinely signed* V1 statement presented for ADMIT after V2 took effect. | **PENDING** B02-A1 |
| V02_ADDENDUM-L0034 | Signer-set state enters the semantic base only for trust-root-changing acceptances; never for P0 or ordinary trials | C08, C11, C12, R33 | INH | Consistent with C03 V02:L0127. P0/S vectors must not contain `signer_set`; P5/P6 template vectors must (R4:L0026). | ACCEPTED |

### AC-3 Semantic-base hygiene

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V02_ADDENDUM-L0038 | The base binds governing state, never repository state; `fixture.semantic_base.source_revision` is excluded from base and selector | C09, C08 | INH | This is the rule C09 exists to protect. Its test is defective (A2, Message 033); the rule itself is settled. Golden base JSON in clarification_vectors_v02.json indeed omits source_revision. | ACCEPTED |
| V02_ADDENDUM-L0040 | Each dependency carries effect_id, status, lineage_head, contract_revision; identity/version kept against ABA staleness; unrelated metadata excluded | C08, R36 | INH | Recommendation B02-R1: C08 mutates only `lineage_head`; add non-gating per-field vectors (status, contract_revision) so the projection is shown to bind all four fields. | ACCEPTED |

### AC-4 Verify versus admit

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V02_ADDENDUM-L0044 | VERIFY is stateless and arm-cryptographic; it consumes nothing and reads no ledger state | R14, R01, C01 | SUP:L0126 | Output domain is now tri-state VALID/INVALID/VERIFIER_ERROR (R4:L0126) with structural pre-checks first (R4:L0132). Statelessness is retained. | ACCEPTED |
| V02_ADDENDUM-L0046 | ADMIT is stateful: VERIFY=VALID, unconsumed ID, current signer version, current recomputed base, appropriate current role, plus record/envelope/statement digest consistency | C01, C07, C10, C12, R36 | INH | Only "unconsumed ID" (C07B) and "role vs non-owner key" (C12) are tested. Missing ADMIT negatives: stale signed version, stale signed base, RECOVERY over ordinary (A9). The independent scorer must replay ADMIT (R36). | **PENDING** B02-A1 |
| V02_ADDENDUM-L0048 | The first admitted decision consumes its ID for any decision; only ACCEPT applies effects; unadmitted statements consume nothing; a revision is a new acceptance | C07, C11, C12, R25 | INH | V02:L0238 (failed role ADMIT changes no ID or version) is the tested instance. T-TRANSITION-STATE should also assert AMEND/REJECT consume without applying effects. | ACCEPTED |

### AC-5 Historical trust and compromise

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V02_ADDENDUM-L0052 | Historical records verify under the signer set at their own sequence position; issued_at is never order or boundary | C12, C13 | INH | R4:L0132 adds that the successor's historical P0 check uses only the successor context and version. | ACCEPTED |
| V02_ADDENDUM-L0054 | Boundary b: records at seq <= b stay historical; later otherwise-valid records of the affected credential become REVIEW_REQUIRED / GOVERNING_OWNER; no retroactive invalidation | C13 | INH | Direct definition of C13's two-row expectation (V02:L0246). | ACCEPTED |
| V02_ADDENDUM-L0056 | C13 takes DECLARATION_TRUSTED_SYNTHETIC_INPUT; it tests classification, not declaration authority, which stays roadmap-stage R1 work | C13 | INH | "R1" here is the roadmap stage, not requirement R01. Unchanged by REV04. | ACCEPTED |

### AC-6 P01 trust roles

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V02_ADDENDUM-L0060 | PRIMARY authorizes ordinary acceptance and ordinary rotation; RECOVERY authorizes only recovery transitions and **never** ordinary acceptance; genesis explicit; transitions prospective | C11, C12, R04 | INH | **A9 exact source identity: this unit, second sentence.** Proposed result semantics: in a synthetic-only scenario whose V1 RECOVERY member is a test-double key, a mathematically valid test-double signature over an ordinary S-type statement gives VERIFY=VALID under that key and ADMIT denial `CURRENT_ROLE_DENIED`; no ID consumed, no state change. No owner proof is used or requested. This is a conformance test, not a 14th control. | **PENDING** A9 |

### §3 P01-C01 Digests and canonical bytes

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V02_ADDENDUM-L0064 | All digests SHA-256, lowercase 64-hex, no prefix; shown_digest over exact displayed UTF-8 bytes | R01, R02 | INH | Unchanged in REV04. | ACCEPTED |
| V02_ADDENDUM-L0066 | Canonical JSON: UTF-8, no BOM/trailing newline, sorted keys by code point, compact separators, ordered arrays, no NaN/Infinity, no unnecessary ASCII escaping; probe-only scheme | R01, R36 | INH | I checked fixture.json: all ASCII, no control characters, so the escaping clause has no live effect. Recommendation B02-R2: for dual-implementation determinism (R36) F1 should add a fail-closed domain guard (printable ASCII in keys and values) instead of relying on "JSON-required escaping", which differs between encoders outside that domain. | ACCEPTED |
| V02_ADDENDUM-L0068 | Arm B challenge = unpadded base64url of the raw 32-byte statement SHA-256; Arm C uses lowercase hex | R06, R30 | INH | REV04 preserves (R4:L0108 "binds canonical statement digest exactly"). | ACCEPTED |

### §4 P01-C02 Envelope and statement sources

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V02_ADDENDUM-L0072 | The ordinary envelope for S01/S02/S03/L01 is constructed exactly as specified | R01 | INH | Framing sentence for L0074. | ACCEPTED |
| V02_ADDENDUM-L0074 | Exact ordinary envelope: schema `R0-P01-ENVELOPE-V01`, project, acceptance_id `R0-P01-<ARM>-<TRIAL>`, item/title/summary/effects, dependency selector | R01, C03 | SUP:L0025 | Only the acceptance-ID grammar is replaced (prefix `R0-P01-002-`). The exact successor string, and whether the envelope schema label stays `R0-P01-ENVELOPE-V01`, are not stated in approved text. | **PENDING** B02-A3 |
| V02_ADDENDUM-L0091 | Effects keep all fields and order; selector = BASE-A and BASE-B sorted, nothing else; class, consequence, issued_at, source_revision excluded | R01, C08, R36 | INH | Matches the golden canonical envelope. | ACCEPTED |
| V02_ADDENDUM-L0093 | Statement field sources are fixed by the table | R01 | INH | Framing for L0097–L0105. | ACCEPTED |
| V02_ADDENDUM-L0097 | context = fixture.statement_context (`ADS-GOVERNING-ACCEPTANCE/v1`) | R01, C06 | SUP:L0025 | Successor context `ADS-R0-P01-002-OWNER-ACCEPTANCE-V01`, checked structurally before crypto (R4:L0132). | ACCEPTED |
| V02_ADDENDUM-L0098 | project_id = envelope.project_id = fixture.project_id | R01, C06 | INH | REV04 keeps a fixed synthetic project ID as a structural check. | ACCEPTED |
| V02_ADDENDUM-L0099 | acceptance_id = envelope.acceptance_id | R01, C07 | INH | Source rule unchanged; value grammar per L0074. | ACCEPTED |
| V02_ADDENDUM-L0100 | envelope_digest = C01 digest of the exact envelope | R01, R02, C03 | INH | — | ACCEPTED |
| V02_ADDENDUM-L0101 | shown_digest = C01 digest of the exact displayed view | R02, C04 | INH | R4:L0031–L0033: T3 chrome is outside these bytes. | ACCEPTED |
| V02_ADDENDUM-L0102 | decision = captured owner ACCEPT/AMEND/REJECT, never inferred from proof or transport | R03, C05 | INH | R4:L0035 and L0194 (uncaptured input re-prompts). | ACCEPTED |
| V02_ADDENDUM-L0103 | semantic_base_digest = digest of the C03 projection recomputed from scenario state | R01, C08, C09 | INH | — | ACCEPTED |
| V02_ADDENDUM-L0104 | signer_set_version = current scenario version at decision/admission | R01, C10, C11 | INH | — | ACCEPTED |
| V02_ADDENDUM-L0105 | issued_at = exact trial.issued_at; fixed timestamps for P0/P5/P6 | R01, R33 | INH | Provenance only (AC-5). Successor templates (R4:L0026) must fix these strings. | ACCEPTED |
| V02_ADDENDUM-L0107 | V0.1 renderer verbatim; labels from the envelope; exact indentation and LF rules; displayed bytes = hashed bytes; no wrapper may substitute | R02, R36 | INH | R4:L0035 requires an independent byte freeze of the successor renderer (T-RENDER-GOLDEN). Acceptance-ID text in the view changes with B02-A3. | ACCEPTED |

### §5 P01-C03 Semantic base and expected values

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V02_ADDENDUM-L0111 | The ordinary base is exactly the following object | C08, R01 | INH | Framing for L0113. | ACCEPTED |
| V02_ADDENDUM-L0113 | Base object: grammar_version, predicate_semantics_version, dependencies with four fields | C08, R01, R36 | INH | Matches canonical_semantic_base_json in clarification_vectors_v02.json. | ACCEPTED |
| V02_ADDENDUM-L0123 | Resolve BASE-A/B in isolated scenario state, never a repository revision; all identities and versions must match before signing/admission; missing/duplicate/mismatched fail closed | C08, C09, R15 | INH | REV04:L0208 refines "fail closed" into INTEGRITY classification when frozen identities are violated. | ACCEPTED |
| V02_ADDENDUM-L0125 | Expected ordinary V1 base digest `76a7391f...`; independently recompute and compare before owner display; mismatch blocks, never repaired | C08, R36, R37 | INH | The base contains no context, project or key, so the digest is reusable if the successor fixture keeps the same base. F1 must state retained-or-replaced explicitly. REV04:L0206: a pre-claim mismatch blocks without consuming a claim. | ACCEPTED |
| V02_ADDENDUM-L0127 | Trust-root grammars additionally include signer_set | C11, C12, R33 | INH | — | ACCEPTED |
| V02_ADDENDUM-L0129 | signer_set = {version, members_digest} | C11, C12, R33 | INH | Template slots per R4:L0026. | ACCEPTED |
| V02_ADDENDUM-L0133 | Trust selector adds `trust_root_subject`; no live version or digest in the selector; no owner-signed compromise declaration in C13 | C11, C12, C13, R33 | INH | — | ACCEPTED |

### §6 P01-C04 Isolated scenarios and ledger order

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V02_ADDENDUM-L0137 | Deterministic in-memory ledgers per arm and attempt; five scenarios; own consumed-ID registry and trust history; no leakage; no persistent production ledger | C01, C07, C11, C12, C13, R20 | INH | No R row carries the isolation/no-leak rule or the no-production-ledger rule (A6(a)); no catalogue test asserts it. | **PENDING** B02-A2; A6 |
| V02_ADDENDUM-L0139 | Each scenario starts at seq1 GENESIS V1 with public members and synthetic/TOFU provenance; owner confirms initial public IDs; no model supplies a secret | R04, R19, R15 | INH | R4:L0195 (CONFIRM prompt re-prompts without integrity flag). Setup occurs only after claim (R4:L0023). | ACCEPTED |
| V02_ADDENDUM-L0141 | BASE_SECURITY admits P0 at seq2; failed mutations append nothing; BURDEN runs S01→S02→S03→L01; ROTATION/RECOVERY copy P0 historically at seq2 and transition at seq3; COMPROMISE uses C09 positions | C01, C11, C12, C13, R08 | INH | Event order unchanged (R4:L0081–L0083). | ACCEPTED |
| V02_ADDENDUM-L0143 | Transitions verify under pre-transition state; only admitted ACCEPT applies the new version; AMEND/REJECT consume the ID only; a non-ACCEPT security transition is a failed control with no replacement proof | C11, C12, R25 | INH | R4:L0087. | ACCEPTED |

### §7 P01-C05 Trust members and setup receipts

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V02_ADDENDUM-L0147 | A member is exactly the following object | C11, C12, R04 | INH | Framing. | ACCEPTED |
| V02_ADDENDUM-L0149 | Member = {role, kind, public_id} with the two enumerated role and kind values | C11, C12, R04 | INH | — | ACCEPTED |
| V02_ADDENDUM-L0153 | Members sorted by role, kind, public_id; members_digest = SHA-256 of the canonical sorted array | C11, C12, R36 | INH | — | ACCEPTED |
| V02_ADDENDUM-L0155 | SSH public_id = prefix + SHA-256 of decoded key blob (comment ignored, type validated); WebAuthn public_id = prefix + SHA-256 of SPKI DER after real ES256/P-256 import; credential ID kept separately | R04, R06, R23 | INH | R23 (old/new public-ID inequality) compares these values. REV04 L0023/L0138 narrow *publication*: these IDs stay in owner-local evidence and are not published to the repository. | ACCEPTED |
| V02_ADDENDUM-L0157 | V1 = SIGNERS-P01-V1; A PRIMARY/RECOVERY = owner Ed25519 keys; B PRIMARY = registered WebAuthn, RECOVERY = Arm-A recovery; public-only receipts; nonempty passphrase, no agent | R04, R23, R19, C12 | SUP:L0023 | Fresh attempt-local keys created after claim (R4:L0023); B recovery must be the same-attempt Arm-A RECOVERY (R4:L0024, L0110). Passphrase/no-agent rules unchanged (R4:L0066). | ACCEPTED |

### §8 P01-C06 Controls 1–10 and P0

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V02_ADDENDUM-L0161 | Exactly one owner-authenticated P0 per cryptographic arm, with C02 schema/selector and the listed substitutions | C01, R25 | INH | R4:L0087. | ACCEPTED |
| V02_ADDENDUM-L0163 | P0 template: acceptance_id `R0-P01-<ARM>-SEC-VALID_ACCEPTANCE`, SECURITY_BASELINE item, one SEC-BASE-001 effect, decision ACCEPT, fixed issued_at | C01, R01, R25 | SUP:L0025 | Acceptance-ID grammar replaced; exact successor string not enumerated. Other fields inheritable. | **PENDING** B02-A3 |
| V02_ADDENDUM-L0179 | Effect text is one string; capture the owner's actual decision; no manufactured ACCEPT; no rescue baseline | R25, R03, C01 | INH | R4:L0087 (preserved failed positive control). | ACCEPTED |
| V02_ADDENDUM-L0181 | Result keys are the 13 frozen keys; controls 2–10 reuse P0 without new signed IDs; each mutation applied independently to an unmodified copy | C02, C03, C04, C05, C06, C07, C08, C09, C10, R37 | INH | T-CONTROL-KEY-BINDING. Independence of mutations should be asserted (fresh copy per control). | ACCEPTED |
| V02_ADDENDUM-L0185 | Control 1: VERIFY=VALID and first ADMIT succeeds | C01 | INH | — | ACCEPTED |
| V02_ADDENDUM-L0186 | Control 2: XOR first raw proof byte; VERIFY rejects; never a valid forged proof | C02 | INH | First byte is the SSHSIG magic / DER tag: STRUCTURAL rejection only. | **PENDING** A1 |
| V02_ADDENDUM-L0187 | Control 3: append " [MUTATED]" to SEC-BASE-001.text, recompute envelope_digest, reuse P0; VERIFY rejects | C03 | INH | Expected layer CRYPTOGRAPHIC (R4:L0180). | ACCEPTED |
| V02_ADDENDUM-L0188 | Control 4: change first displayed byte R→X, recompute shown_digest, reuse P0; VERIFY rejects | C04 | INH | The V02 view starts with header `R0-P01 OWNER VIEW V01`; F1 must confirm the successor view's first byte is still `R`. Layer CRYPTOGRAPHIC. | ACCEPTED |
| V02_ADDENDUM-L0189 | Control 5: ACCEPT→REJECT in the presented statement; VERIFY rejects | C05 | INH | Research 534 keeps the C05 disposition open until the ACCEPT→AMEND offline vector exists. | **PENDING** C05_AMEND_VECTOR |
| V02_ADDENDUM-L0190 | Control 6: project_id → fixture.wrong_project_id; VERIFY rejects | C06, R01 | INH | Gating rejection is STRUCTURAL under REV04; A4 adds a non-gating crypto diagnostic (accepted in Research 534). | ACCEPTED |
| V02_ADDENDUM-L0191 | Control 7: (A) replacement ID `R0-P01-<ARM>-SEC-ACCEPTANCE_ID_REPLAY_REJECTS` rejects; (B) second ADMIT of P0 rejects | C07, R01 | INH | Class A ID is old grammar: STRUCTURAL rejection under REV04, so the crypto property is unexercised. | **PENDING** A3 |
| V02_ADDENDUM-L0192 | Control 8: BASE-A.lineage_head → BASE-A-1 in a copied base, recompute digest, reuse P0; VERIFY rejects | C08 | INH | Layer CRYPTOGRAPHIC. See B02-R1 for per-field coverage. | ACCEPTED |
| V02_ADDENDUM-L0193 | Control 9: add separate in-memory `repository_note`; P0 VERIFY remains VALID | C09 | INH | Inert input: the test cannot fail (harness.py line 456 confirms). | **PENDING** A2 |
| V02_ADDENDUM-L0194 | Control 10: signer_set_version → SIGNERS-P01-V999-SYNTHETIC, reuse P0; VERIFY rejects | C10 | INH | The field is not a structural pre-check field, so rejection reaches CRYPTOGRAPHIC. The ADMIT-side counterpart is B02-A1. | ACCEPTED |
| V02_ADDENDUM-L0196 | Negative controls must really verify the changed statement; no ADMIT of changed proposals; missing P0 makes dependents FAIL, never NOT_APPLICABLE | C02, C03, C04, C05, C06, C07, C08, C09, C10, R26, R36 | INH | R4:L0069 (`FAIL / UNEXECUTED_DEPENDENCY_ABSENT`), L0180 (rejection_layer). | ACCEPTED |

### §9 P01-C07 Ordinary rotation and P5 (first part; L0217 is in batch 003)

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V02_ADDENDUM-L0200 | Fresh ROTATION V1 state; C02 schema, C03 trust selector, one independently acceptable effect | C11 | INH | — | ACCEPTED |
| V02_ADDENDUM-L0202 | P5 template: `R0-P01-<ARM>-SEC-TRUST_ROOT_ROTATION_DRY_RUN`, TRUST-ROTATE-001, rotation text with target public IDs, fixed issued_at, required ACCEPT | C11, R33, R01 | SUP:L0025 | ID grammar replaced; R4:L0026 template with public-member slots. Exact successor ID string not enumerated. | **PENDING** B02-A3 |
| V02_ADDENDUM-L0215 | Substitute exact public IDs; A's V2 = PRIMARY Arm-A recovery, RECOVERY Arm-A original primary; B's V2 = Arm-A primary and Arm-A recovery; V1 PRIMARY signs P5; VERIFY and role-correct ADMIT before version change | C11, R33, R04 | INH | **This is the exact basis for A8.** REV04 states the same-attempt dependency only for P6 (L0024/L0110); for P5 the successor must also use the *same-attempt* new Arm-A keys and give `FAIL / UNEXECUTED_ROTATION_TARGET_ABSENT` if absent. T-B-P5-TARGET-DEPENDENCY exists but has no citable fixture rule yet. | **PENDING** A8 |

## 3. V02 lines outside numbered sections (excluded by extraction, audited here)

| Line | Content (abridged) | Normative? | Finding |
|---|---|---|---|
| 3, 4, 8 | Date, status, authority | No | Keep excluded as METADATA. |
| 5, 6 | Protocol R0-P01-V01; contract R0-P01-CONTRACT-V02 | No (identity metadata) | Successor identities are R4:L0006/L0020. The same values appear in the normative result schema at V02:L0282 (batch 003), where they matter. |
| 7 | Scope: no change to architecture, arms, controls, thresholds or selection | Yes, duplicated | Fully restated by V02:L0333 and R4:L0012/L0014. No new unit needed. |
| 12 | Read together with fixture, V01 contracts, result contract, **clarification_vectors_v02.json** and **legacy_volume_inventory_rule.json** | **Yes** | **Add as unit** (R37, R34). Scope gap: those two JSON files are named governing inputs but are not inventory sources. Their key values are restated in V02:L0308–L0324 (batch 003), but F1 should bind them by Git-blob hash or declare them data artifacts covered by those units. |
| 14 | V02 supersedes V0.1 only where it explicitly defines a detail; V0.1 files stay historical | **Yes** | **Add as unit** (R37). This is the precedence rule needed to audit V01_CONTRACT batches 004–006; I apply it there. |
| 16 | Kernel retained; AC-1..AC-6 are clarifications; compromise-authority matrix open R1 issue | Partly | Covered by V02:L0056 and R4:L0016 (kernel unselected as physical target). No new unit needed. |
| 18 | Implementation confined to harness.py, webauthn_server.mjs, score.py with **Python stdlib and Node built-ins**; owner operations outside implementation | **Yes** | **Add as unit.** Clash B02-A4 with R36 (in-process SSHSIG needs Ed25519, absent from the Python stdlib) and R39 (hash-pinned dependencies). F1 must state the successor dependency policy: either keep stdlib-only and implement Ed25519 in pure Python under dual review, or record a reviewed supersession with pinned hashes. |

## 4. Amendments and recommendations (batch-level)

- **B02-A1 (AC-4 ADMIT negatives).** Add offline, synthetic-key conformance vectors, none needing an owner proof:
  - (a) a test-double PRIMARY signs a V1-version statement; rotate the synthetic scenario to V2; ADMIT → deny on signer-set version, VERIFY still VALID;
  - (b) a test-double PRIMARY signs a statement over the V1 base; advance the scenario's BASE-A lineage; ADMIT → deny on semantic base;
  - (c) A9.

  Record `rejection_layer=ADMIT` and assert no ID consumption.
- **B02-A2 (scenario isolation).** Add rule text to R20 or a new row: per-arm/per-attempt/per-scenario ledgers, independent consumed-ID registries, no cross-scenario state, no persistent or production ledger. Add a test: consuming an ID in BASE_SECURITY must not consume it in ROTATION, and an A-arm consumption must not affect B.
- **B02-A3 (successor ID strings).** F1 must enumerate every successor acceptance ID: 4 ordinary per arm, P0/P5/P6 per arm, the C07 class-A replacement, the Arm C IDs. It must also state whether envelope schema `R0-P01-ENVELOPE-V01` and view header `R0-P01 OWNER VIEW V01` are retained. Structural VERIFY, A3 and the C04 first-byte assumption all depend on this.
- **B02-A4 (dependency policy).** Resolve V02 line 18 against R36/R39 before F2.
- **B02-R1, B02-R2** (non-blocking): per-field C08 diagnostics; canonical-JSON printable-ASCII domain guard.
- **Scope:** add V02 lines 12, 14, 18 as units; bind the two referenced JSON files.

## 5. Machine-checkable receipt

```text
BEGIN_AUDIT_RECEIPT
V02_ADDENDUM-L0024|INHERITED_UNCHANGED|R01,R02,C03|ACCEPTED||V02_ADDENDUM-L0024;REV04_CONTRACT-L0031
V02_ADDENDUM-L0026|INHERITED_UNCHANGED|R01|ACCEPTED||V02_ADDENDUM-L0026;REV04_CONTRACT-L0025
V02_ADDENDUM-L0028|INHERITED_UNCHANGED|R01,R16|ACCEPTED||V02_ADDENDUM-L0028;REV04_CONTRACT-L0134
V02_ADDENDUM-L0032|INHERITED_UNCHANGED|C10,C11,R01|PENDING|B02-A1_ADMIT_STALE_SIGNER_SET_NEGATIVE_MISSING|V02_ADDENDUM-L0032;V02_ADDENDUM-L0194
V02_ADDENDUM-L0034|INHERITED_UNCHANGED|C08,C11,C12,R33|ACCEPTED||V02_ADDENDUM-L0034;V02_ADDENDUM-L0127;REV04_CONTRACT-L0026
V02_ADDENDUM-L0038|INHERITED_UNCHANGED|C09,C08|ACCEPTED||V02_ADDENDUM-L0038;clarification_vectors_v02.json
V02_ADDENDUM-L0040|INHERITED_UNCHANGED|C08,R36|ACCEPTED||V02_ADDENDUM-L0040;V02_ADDENDUM-L0113
V02_ADDENDUM-L0044|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0126|R14,R01,C01|ACCEPTED||REV04_CONTRACT-L0126;REV04_CONTRACT-L0132
V02_ADDENDUM-L0046|INHERITED_UNCHANGED|C01,C07,C10,C12,R36|PENDING|B02-A1_ADMIT_NEGATIVES_SIGNER_SET_BASE_ROLE_MISSING|V02_ADDENDUM-L0046
V02_ADDENDUM-L0048|INHERITED_UNCHANGED|C07,C11,C12,R25|ACCEPTED||V02_ADDENDUM-L0048;V02_ADDENDUM-L0238
V02_ADDENDUM-L0052|INHERITED_UNCHANGED|C12,C13|ACCEPTED||V02_ADDENDUM-L0052;REV04_CONTRACT-L0132
V02_ADDENDUM-L0054|INHERITED_UNCHANGED|C13|ACCEPTED||V02_ADDENDUM-L0054;V02_ADDENDUM-L0246
V02_ADDENDUM-L0056|INHERITED_UNCHANGED|C13|ACCEPTED||V02_ADDENDUM-L0056
V02_ADDENDUM-L0060|INHERITED_UNCHANGED|C11,C12,R04|PENDING|A9_RECOVERY_ORDINARY_ADMIT_DENIAL_TEST_MISSING|V02_ADDENDUM-L0060
V02_ADDENDUM-L0064|INHERITED_UNCHANGED|R01,R02|ACCEPTED||V02_ADDENDUM-L0064
V02_ADDENDUM-L0066|INHERITED_UNCHANGED|R01,R36|ACCEPTED||V02_ADDENDUM-L0066;fixture.json_ascii_checked
V02_ADDENDUM-L0068|INHERITED_UNCHANGED|R06,R30|ACCEPTED||V02_ADDENDUM-L0068;REV04_CONTRACT-L0108
V02_ADDENDUM-L0072|INHERITED_UNCHANGED|R01|ACCEPTED||V02_ADDENDUM-L0072
V02_ADDENDUM-L0074|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0025|R01,C03|PENDING|B02-A3_SUCCESSOR_ACCEPTANCE_ID_STRINGS_NOT_ENUMERATED|V02_ADDENDUM-L0074;REV04_CONTRACT-L0025;REV04_CONTRACT-L0132
V02_ADDENDUM-L0091|INHERITED_UNCHANGED|R01,C08,R36|ACCEPTED||V02_ADDENDUM-L0091
V02_ADDENDUM-L0093|INHERITED_UNCHANGED|R01|ACCEPTED||V02_ADDENDUM-L0093
V02_ADDENDUM-L0097|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0025|R01,C06|ACCEPTED||REV04_CONTRACT-L0025;REV04_CONTRACT-L0132
V02_ADDENDUM-L0098|INHERITED_UNCHANGED|R01,C06|ACCEPTED||V02_ADDENDUM-L0098;REV04_CONTRACT-L0025
V02_ADDENDUM-L0099|INHERITED_UNCHANGED|R01,C07|ACCEPTED||V02_ADDENDUM-L0099
V02_ADDENDUM-L0100|INHERITED_UNCHANGED|R01,R02,C03|ACCEPTED||V02_ADDENDUM-L0100
V02_ADDENDUM-L0101|INHERITED_UNCHANGED|R02,C04|ACCEPTED||V02_ADDENDUM-L0101;REV04_CONTRACT-L0033
V02_ADDENDUM-L0102|INHERITED_UNCHANGED|R03,C05|ACCEPTED||V02_ADDENDUM-L0102;REV04_CONTRACT-L0194
V02_ADDENDUM-L0103|INHERITED_UNCHANGED|R01,C08,C09|ACCEPTED||V02_ADDENDUM-L0103
V02_ADDENDUM-L0104|INHERITED_UNCHANGED|R01,C10,C11|ACCEPTED||V02_ADDENDUM-L0104
V02_ADDENDUM-L0105|INHERITED_UNCHANGED|R01,R33|ACCEPTED||V02_ADDENDUM-L0105;REV04_CONTRACT-L0026
V02_ADDENDUM-L0107|INHERITED_UNCHANGED|R02,R36|ACCEPTED||V02_ADDENDUM-L0107;REV04_CONTRACT-L0035
V02_ADDENDUM-L0111|INHERITED_UNCHANGED|C08,R01|ACCEPTED||V02_ADDENDUM-L0111
V02_ADDENDUM-L0113|INHERITED_UNCHANGED|C08,R01,R36|ACCEPTED||V02_ADDENDUM-L0113;clarification_vectors_v02.json
V02_ADDENDUM-L0123|INHERITED_UNCHANGED|C08,C09,R15|ACCEPTED||V02_ADDENDUM-L0123;REV04_CONTRACT-L0208
V02_ADDENDUM-L0125|INHERITED_UNCHANGED|C08,R36,R37|ACCEPTED||V02_ADDENDUM-L0125;REV04_CONTRACT-L0206
V02_ADDENDUM-L0127|INHERITED_UNCHANGED|C11,C12,R33|ACCEPTED||V02_ADDENDUM-L0127
V02_ADDENDUM-L0129|INHERITED_UNCHANGED|C11,C12,R33|ACCEPTED||V02_ADDENDUM-L0129;REV04_CONTRACT-L0026
V02_ADDENDUM-L0133|INHERITED_UNCHANGED|C11,C12,C13,R33|ACCEPTED||V02_ADDENDUM-L0133
V02_ADDENDUM-L0137|INHERITED_UNCHANGED|C01,C07,C11,C12,C13,R20|PENDING|B02-A2_SCENARIO_ISOLATION_RULE_TEXT_MISSING;A6_NO_PRODUCTION_LEDGER_RULE|V02_ADDENDUM-L0137
V02_ADDENDUM-L0139|INHERITED_UNCHANGED|R04,R19,R15|ACCEPTED||V02_ADDENDUM-L0139;REV04_CONTRACT-L0195;REV04_CONTRACT-L0023
V02_ADDENDUM-L0141|INHERITED_UNCHANGED|C01,C11,C12,C13,R08|ACCEPTED||V02_ADDENDUM-L0141;REV04_CONTRACT-L0082
V02_ADDENDUM-L0143|INHERITED_UNCHANGED|C11,C12,R25|ACCEPTED||V02_ADDENDUM-L0143;REV04_CONTRACT-L0087
V02_ADDENDUM-L0147|INHERITED_UNCHANGED|C11,C12,R04|ACCEPTED||V02_ADDENDUM-L0147
V02_ADDENDUM-L0149|INHERITED_UNCHANGED|C11,C12,R04|ACCEPTED||V02_ADDENDUM-L0149
V02_ADDENDUM-L0153|INHERITED_UNCHANGED|C11,C12,R36|ACCEPTED||V02_ADDENDUM-L0153
V02_ADDENDUM-L0155|INHERITED_UNCHANGED|R04,R06,R23|ACCEPTED||V02_ADDENDUM-L0155;REV04_CONTRACT-L0023;REV04_CONTRACT-L0138
V02_ADDENDUM-L0157|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0023|R04,R23,R19,C12|ACCEPTED||REV04_CONTRACT-L0023;REV04_CONTRACT-L0024;REV04_CONTRACT-L0110
V02_ADDENDUM-L0161|INHERITED_UNCHANGED|C01,R25|ACCEPTED||V02_ADDENDUM-L0161;REV04_CONTRACT-L0087
V02_ADDENDUM-L0163|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0025|C01,R01,R25|PENDING|B02-A3_SUCCESSOR_ACCEPTANCE_ID_STRINGS_NOT_ENUMERATED|V02_ADDENDUM-L0163;REV04_CONTRACT-L0025
V02_ADDENDUM-L0179|INHERITED_UNCHANGED|R25,R03,C01|ACCEPTED||V02_ADDENDUM-L0179;REV04_CONTRACT-L0087
V02_ADDENDUM-L0181|INHERITED_UNCHANGED|C02,C03,C04,C05,C06,C07,C08,C09,C10,R37|ACCEPTED||V02_ADDENDUM-L0181
V02_ADDENDUM-L0185|INHERITED_UNCHANGED|C01|ACCEPTED||V02_ADDENDUM-L0185
V02_ADDENDUM-L0186|INHERITED_UNCHANGED|C02|PENDING|A1_C02_STRUCTURAL_ONLY_VECTOR|V02_ADDENDUM-L0186;REV04_CONTRACT-L0180
V02_ADDENDUM-L0187|INHERITED_UNCHANGED|C03|ACCEPTED||V02_ADDENDUM-L0187;REV04_CONTRACT-L0180
V02_ADDENDUM-L0188|INHERITED_UNCHANGED|C04|ACCEPTED||V02_ADDENDUM-L0188;clarification_vectors_v02.json
V02_ADDENDUM-L0189|INHERITED_UNCHANGED|C05|PENDING|C05_AMEND_VECTOR_DECISION|V02_ADDENDUM-L0189
V02_ADDENDUM-L0190|INHERITED_UNCHANGED|C06,R01|ACCEPTED||V02_ADDENDUM-L0190;REV04_CONTRACT-L0132;REV04_CONTRACT-L0180
V02_ADDENDUM-L0191|INHERITED_UNCHANGED|C07,R01|PENDING|A3_C07A_OLD_GRAMMAR_ID|V02_ADDENDUM-L0191;REV04_CONTRACT-L0132
V02_ADDENDUM-L0192|INHERITED_UNCHANGED|C08|ACCEPTED||V02_ADDENDUM-L0192
V02_ADDENDUM-L0193|INHERITED_UNCHANGED|C09|PENDING|A2_C09_INERT_METADATA_VECTOR|V02_ADDENDUM-L0193
V02_ADDENDUM-L0194|INHERITED_UNCHANGED|C10|ACCEPTED||V02_ADDENDUM-L0194;REV04_CONTRACT-L0132
V02_ADDENDUM-L0196|INHERITED_UNCHANGED|C02,C03,C04,C05,C06,C07,C08,C09,C10,R26,R36|ACCEPTED||V02_ADDENDUM-L0196;REV04_CONTRACT-L0069;REV04_CONTRACT-L0180
V02_ADDENDUM-L0200|INHERITED_UNCHANGED|C11|ACCEPTED||V02_ADDENDUM-L0200
V02_ADDENDUM-L0202|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0025|C11,R33,R01|PENDING|B02-A3_SUCCESSOR_ACCEPTANCE_ID_STRINGS_NOT_ENUMERATED|V02_ADDENDUM-L0202;REV04_CONTRACT-L0025;REV04_CONTRACT-L0026
V02_ADDENDUM-L0215|INHERITED_UNCHANGED|C11,R33,R04|PENDING|A8_B_P5_SAME_ATTEMPT_TARGET_RULE_NOT_CITABLE|V02_ADDENDUM-L0215;REV04_CONTRACT-L0023;REV04_CONTRACT-L0024
END_AUDIT_RECEIPT
```

Counts: 65 rows; 53 ACCEPTED; 12 PENDING; 6 SUPERSEDED_BY_REV04; 59 INHERITED_UNCHANGED; 0 NOT_APPLICABLE_TO_SUCCESSOR.

## 6. Attestation and boundaries

- **Reviewer: claude-04** (Claude, independent clause auditor). I independently read the governing source lines for every unit above. I did **not** author the source inventory, the batch plan, the candidate mappings, the blind second golden-vector implementation or the independent scorer, and I will not author the latter two.
- A reviewed batch is not an F1-approved batch. PENDING items are not repaired here, and no source was edited.
- Only this message file was written. No owner evidence, credential, key or WebAuthn state was touched. B01/B02 remain accepted; Attempt 001 remains immutable AMEND; F1/F2 unfrozen; Attempt 002 not authorized.

```text
MC0030_MESSAGE035=CLAUDE_AUDIT_BATCH002
DISPOSITION=AMEND_AUDIT_BATCH002
UNITS_AUDITED=65_OF_65
ACCEPTED=53
PENDING=12
NEW_FINDINGS=B02-A1_ADMIT_NEGATIVES;B02-A2_SCENARIO_ISOLATION;B02-A3_SUCCESSOR_ID_STRINGS;B02-A4_DEPENDENCY_POLICY
EXCLUDED_LINES_TO_ADD=V02_ADDENDUM_LINES_12_14_18
F1=NOT_APPROVED
ATTEMPT_002=NOT_AUTHORIZED
```
