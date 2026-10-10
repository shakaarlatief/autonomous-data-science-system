# MC-0030 Message 038: Claude independent clause audit, batch Q0-AUDIT-005 (V01 implementation contract §6.1–§12)

```text
Thread                  MC-0030
Message                 038
Author / reviewer       Claude / claude-04 (independent clause auditor)
Conversation            04 - Assurance and Delivery Architecture Design
Coordination branch     v1-source-vault-bootstrap-resume
Parent HEAD             18308cc72004c6fb5df40e90bdf2331fef1d14d4 (Message 037)
Batch                   Q0-AUDIT-005 / V01_CONTRACT / 65 units / V01_CONTRACT-L0180 .. V01_CONTRACT-L0371
Batch unit-list SHA-256 recomputed from the plan's ordered IDs: match
Source                  experiments/r0_p01_owner_acceptance_v01/implementation_contract.md
Source SHA-256          b3b90d851e25a4b906f6e094e6366ca42baca7fceb7c38c253f8220bc70b1202 (Git blob, matches inventory)
Cross-checked against   V02 addendum, REV04 contract, REV04 outcome policy (capability rows), B01 decision-predicate table,
                        Q0 REV02 trace, REV03 test catalogue
Disposition             AMEND_AUDIT_BATCH005
Authority               Message 034. Audit record only. No F1/F2 freeze, inventory edit, credential or Attempt 002.
```

## 0. Verification and method

- The branch head before writing was `18308cc7…` (my Message 037, parent `99519011…`, one added file). The receipt checker returned `PASS batches=4/18 units=216/1022`.
- Source hash unchanged. The 65 IDs hash to the plan value; every `text_sha256` matches.
- Method and notation as in Messages 035–037. Precedence: V02 refines V01 where explicit (V02 line 14), and REV04 supersedes both. Per Message 037 B04-S1, a V02 refinement is recorded as INHERITED_UNCHANGED with the V02 line cited.

## 1. Verdict

**`AMEND_AUDIT_BATCH005`**: 65/65 reviewed; **62 ACCEPTED, 3 PENDING**.

The WebAuthn verification checks, Arm C rules, measurement definitions, eligibility gates, selection rule and legacy-volume baseline are all preserved unchanged by REV04 and V02. They map cleanly to R06, R08–R10, R27–R30.

New finding:

**B05-A1. The NOT_REALIZABLE capability predicate is referenced but never enumerated (high consequence).**

- REV04 requires NOT_REALIZABLE to rest on "actual platform capability evidence" under a "frozen capability predicate" (R4:L0108, L0150, L0200). The policy JSON's `not_realizable` and `CAPABILITY_NOT_REALIZABLE` rows require a "frozen … independent capability receipt".
- I found no artifact that lists which observations qualify or what the receipt contains. The substance exists only in V01 here:
  - L0223: standard registration response methods unavailable;
  - L0231: cannot create an ES256 credential with UV, or cannot return an assertion bound to the exact challenge;
  - L0229: the API-availability check.
- **Why it matters.** Under G1, REOPEN requires both A/B states to be COMPLETED or **NOT_REALIZABLE**. Otherwise the result is INVALID_INCOMPLETE. A loosely defined capability predicate is the one path by which an interrupted or abandoned B setup could be relabelled NOT_REALIZABLE and turn INVALID_INCOMPLETE into REOPEN, which is exactly what G1 exists to prevent.
- **Required before F1.** An enumerated, closed predicate, for example:
  - `PublicKeyCredential` absent post-claim;
  - `NotSupportedError` on `create()` with ES256-only parameters and UV required;
  - a successful `create()` whose response lacks `getPublicKey`, `getPublicKeyAlgorithm` or `getAuthenticatorData`, or returns a non-ES256 algorithm;
  - a platform-reported UV-unavailable result.

  Each needs an exact receipt schema. Owner cancellation, timeout or NotAllowedError must be explicitly excluded (V02:L0264, R4:L0108).

  Virtual-authenticator tests (R40) should exercise each predicate branch and each excluded look-alike.

Other observations (non-blocking):

- **B05-R1.** V01:L0229 placed the API-availability check "before an owner trial". REV04 forbids any `navigator.credentials` / `PublicKeyCredential` reference in the preclaim readiness mode (R4:L0104), so the successor performs this check only after the claim, as the first B setup step. Recorded as superseded on timing.
- **B05-R2.** Selection boundaries are inclusive ("differ by at least 10 s / 15 s", V01:L0349–L0350). T-SELECT-EXACT-10 and T-SELECT-EXACT-15 exist and must test exactly 10.000 s and 15.000 s on the unrounded values (V02:L0274).

## 2. Per-unit audit record (65 units)

### §6.1 RP and §6.2 statement binding

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTRACT-L0180 | RP: URL/origin `http://localhost:8765`, rpId localhost, ES256/COSE -7 only, UV required, attestation none, residentKey preferred, attachment omitted | R06 | INH | V02:L0256; R4:L0108 preserves every value. | ACCEPTED |
| V01_CONTRACT-L0189 | Omitting attachment lets the owner use a platform or cross-device authenticator | R06, R27 | INH | Cross-device use is measured as device_switches (L0312). | ACCEPTED |
| V01_CONTRACT-L0191 | No real credential operation before the V01 freeze | R22, R24 | SUP:L0106 | Successor analogue: no registration/assertion before the Attempt 002 claim; preclaim mode is non-credential (R4:L0104, L0106). | ACCEPTED |
| V01_CONTRACT-L0195 | For every assertion the following holds | R06 | INH | Framing. | ACCEPTED |
| V01_CONTRACT-L0197 | challenge = SHA256(canonical statement bytes) | R06 | INH | V02:L0068 (raw 32 bytes, unpadded base64url). | ACCEPTED |
| V01_CONTRACT-L0199 | The verifier must independently check the following | R06, R36 | INH | Framing. | ACCEPTED |
| V01_CONTRACT-L0201 | Checks: type webauthn.get, exact base64url digest challenge, origin, rpIdHash, UP, UV, registered credential ID, ES256 over authData‖SHA256(clientDataJSON) | R06, R36, R40 | INH | V02:L0262 adds malformed-structure rejection and signCount non-gating. R40 negatives: UV=false, foreign credential. | ACCEPTED |
| V01_CONTRACT-L0211 | Registration uses attestation none and accepts only ES256 | R06 | INH | — | ACCEPTED |
| V01_CONTRACT-L0213 | To avoid project-specific crypto/CBOR code, the client must use platform response methods | R06, R39 | INH | Dependency-minimization rule; consistent with V02 line 18. | ACCEPTED |
| V01_CONTRACT-L0215 | getPublicKey(), getPublicKeyAlgorithm(), getAuthenticatorData() | R06 | INH | V02:L0256 ("three frozen browser response methods"). | ACCEPTED |
| V01_CONTRACT-L0219 | Public key transported as SPKI DER and imported with Node built-in crypto | R06 | INH | V02:L0155 (WebAuthn public_id from SPKI DER). | ACCEPTED |
| V01_CONTRACT-L0221 | Registration verifier checks clientDataJSON challenge/origin/type and authData rpIdHash plus UP/UV before storing the credential | R06, R40 | INH | V02:L0258. | ACCEPTED |
| V01_CONTRACT-L0223 | If the browser cannot expose these methods, B is NOT_REALIZABLE; no hidden library or hand-written COSE/CBOR parser | R06, R11 | INH | One of the substantive capability-predicate branches, but no frozen receipt schema exists (B05-A1). | **PENDING** B05-A1 |
| V01_CONTRACT-L0225 | No accepted algorithm may be silently broadened beyond ES256 | R06 | INH | — | ACCEPTED |

### §6.3 Realizability and §6.4 Recovery

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTRACT-L0229 | Before an owner trial, check WebAuthn API availability and attempt one explicit owner-authorized probe registration | R06, R22 | SUP:L0104 | API checks are forbidden in preclaim mode (R4:L0104); they happen post-claim as the first B setup step (B05-R1). The one-registration rule, with its single unchanged repeat, is kept (R4:L0108). | ACCEPTED |
| V01_CONTRACT-L0231 | If the environment cannot create an ES256 UV credential or cannot return an assertion bound to the exact challenge, B is NOT_REALIZABLE | R06, R11 | INH | This is the capability predicate's substance. REV04 requires it frozen with receipts, but it is not enumerated (B05-A1). | **PENDING** B05-A1 |
| V01_CONTRACT-L0233 | Label NOT_REALIZABLE | R11 | INH | Value retained in evidence_state (R4:L0150). | ACCEPTED |
| V01_CONTRACT-L0235 | No substitution by passkey login, OAuth, browser account approval or any non-equivalent identity signal | R06, R04 | INH | — | ACCEPTED |
| V01_CONTRACT-L0239 | B uses the preregistered Arm-A recovery Ed25519 key as its offline recovery credential | C12, R04 | SUP:L0024 | Must be the same-attempt new Arm-A RECOVERY; absent → `FAIL / UNEXECUTED_RECOVERY_MEMBER_ABSENT` (R4:L0024, L0110). | ACCEPTED |
| V01_CONTRACT-L0241 | This is an intentional heterogeneous signer-set test | C11, C12 | INH | V01_CONTROLS L0100 permits heterogeneous sets. | ACCEPTED |
| V01_CONTRACT-L0243 | B primary signs the ordinary rotation (P5); the recovery credential signs the recovery rotation (P6) | C11, C12, R33 | INH | V02:L0215, L0236. | ACCEPTED |
| V01_CONTRACT-L0245 | No WebAuthn private credential material is exported | R19 | INH | — | ACCEPTED |

### §7 Arm C

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTRACT-L0249 | Arm C is a weaker comparator only | R30, R04 | INH | R4:L0012, L0089. | ACCEPTED |
| V01_CONTRACT-L0251 | It measures the friction of the owner's platform-separated user role versus agent execution identity | R30 | INH | — | ACCEPTED |
| V01_CONTRACT-L0253 | One small and one large comparator event | R30 | INH | V02:L0268 fixes these as S01 and L01. | ACCEPTED |
| V01_CONTRACT-L0255 | Line `R0-P01 PLATFORM ATTEST <acceptance_id> <statement_sha256>` | R30, R01 | SUP:L0089 | The successor C namespace changes; the IDs and whether the literal prefix is kept are not enumerated. | **PENDING** B02-A3 |
| V01_CONTRACT-L0257 | The owner must send that exact line as a user-authored ChatGPT message | R30 | INH | V02:L0270. | ACCEPTED |
| V01_CONTRACT-L0259 | The result records the following | R30 | INH | Framing. | ACCEPTED |
| V01_CONTRACT-L0261 | Expected line, observed line, match, platform separation, interaction count, friction note | R30, R27 | INH | V02:L0270 adds a task-owner provenance receipt. | ACCEPTED |
| V01_CONTRACT-L0268 | C is not cryptographic proof, depends on platform provenance and is not repository-verifiable | R30 | INH | — | ACCEPTED |
| V01_CONTRACT-L0270 | Therefore (connective) | R30, R10 | INH | Framing for L0272–L0276. | ACCEPTED |
| V01_CONTRACT-L0272 | selection_eligible = false | R30, R10 | INH | T-C-NONSELECTABLE. | ACCEPTED |
| V01_CONTRACT-L0274 | …under all outcomes | R30, R10 | INH | — | ACCEPTED |
| V01_CONTRACT-L0276 | C can never by itself produce PASS_WITH_SELECTION | R30, R10, R12 | INH | R4:L0261 "C completion cannot change class". | ACCEPTED |

### §8 Security controls and §9 burden trials

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTRACT-L0280 | The 13 controls and semantics are frozen in security_control_contract.md | C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, R37 | INH | Audited in batch 001. | ACCEPTED |
| V01_CONTRACT-L0282 | All 13 must PASS for an arm to be eligible | R10 | INH | — | ACCEPTED |
| V01_CONTRACT-L0284 | No result label is hidden from the implementer | R36, R37 | INH | Same as V01_CONTROLS line 7 (Message 033): blindness of the second oracle concerns implementation, not hidden labels. | ACCEPTED |
| V01_CONTRACT-L0288 | Burden trials run for each REALIZABLE A/B arm | R08 | INH | — | ACCEPTED |
| V01_CONTRACT-L0290 | S01 1, S02 2, S03 4, L01 30 effects | R08 | INH | R4:L0012. | ACCEPTED |
| V01_CONTRACT-L0295 | Fixture effects are synthetic and low consequence | R08, R28 | INH | R4:L0032: no claim to test real consequential comprehension. | ACCEPTED |
| V01_CONTRACT-L0297 | The owner reveals no secret during a trial | R19 | INH | — | ACCEPTED |
| V01_CONTRACT-L0299 | Measurements follow | R08, R27 | INH | Framing. | ACCEPTED |
| V01_CONTRACT-L0301 | semantic_review_seconds: full view displayed → decision captured | R08, R28 | INH | R4:L0094. | ACCEPTED |
| V01_CONTRACT-L0305 | mechanical_seconds: decision captured → proof locally verified | R08 | INH | R4:L0094 includes all retries and the verify result. | ACCEPTED |
| V01_CONTRACT-L0309 | interaction_count: user-visible decision/authentication interactions after display | R27 | INH | R4:L0098 (including unlock re-entry) and L0140 (harness mechanical floor as lower bound). | ACCEPTED |
| V01_CONTRACT-L0312 | device_switches: physical device changes needed | R27, R08 | INH | R4:L0098. | ACCEPTED |
| V01_CONTRACT-L0315 | manual_metadata_edits: owner hand-edits to metadata; must be zero | R10, R08 | INH | V02:L0286 includes setup/control edits. | ACCEPTED |
| V01_CONTRACT-L0318 | friction_rating 1 (very low) to 5 (very high) | R27 | INH | V02:L0288 requires integers 1–5 for eligibility. | ACCEPTED |
| V01_CONTRACT-L0322 | friction_note: short non-secret note | R27, R19 | INH | — | ACCEPTED |
| V01_CONTRACT-L0325 | Infrastructure interruptions recorded separately; a small trial >120 s caused only by a recorded interruption is excluded from that single-trial max gate but stays visible | R08 | INH | V02:L0292–L0304 fix the receipt and narrow it; R4:L0098. | ACCEPTED |
| V01_CONTRACT-L0327 | No other timing exclusion is permitted | R08 | INH | — | ACCEPTED |

### §10 Mechanical gates, §11 Selection, §12 Legacy volume

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTRACT-L0331 | A/B eligibility requires the following | R10 | INH | Framing. | ACCEPTED |
| V01_CONTRACT-L0333 | 3/3 small successful; median small ≤60; max small ≤120 absent recorded interruption; L01 ≤120; zero edits; no exposure; 13 controls PASS | R10, R08 | INH | V02:L0288 adds L01 success, field completeness and rating domain. R4:L0014 unchanged. | ACCEPTED |
| V01_CONTRACT-L0341 | Semantic-review time is reported, not gated | R28, R08 | INH | R4:L0094 ("no upper gate"). | ACCEPTED |
| V01_CONTRACT-L0345 | Exactly one eligible arm → select it | R10 | INH | REV04 adds the mandatory G2 disclosure when the other arm is INCOMPLETE (R4:L0158). | ACCEPTED |
| V01_CONTRACT-L0347 | If both are eligible, apply the following | R10 | INH | Framing. | ACCEPTED |
| V01_CONTRACT-L0349 | Median-small difference ≥10 s → lower median | R10 | INH | Inclusive boundary (B05-R2). | ACCEPTED |
| V01_CONTRACT-L0350 | Else L01 difference ≥15 s → lower L01 | R10 | INH | Inclusive boundary (B05-R2). | ACCEPTED |
| V01_CONTRACT-L0351 | Else select B (exact binding with UV, no exportable key, cross-device path) | R10 | INH | The rationale is explanatory; the rule is "else B". T-SELECTION-TIE. | ACCEPTED |
| V01_CONTRACT-L0353 | Thresholds and tie-break are frozen before results | R10 | INH | Restated verbatim as unchanged in R4:L0014. The general anti-tuning guard remains tracked under A6 (V01_CONTROLS-L0145). | ACCEPTED |
| V01_CONTRACT-L0357 | legacy_volume_inventory_rule.json is the only P01 desk-estimate source | R09 | INH | V02:L0308 (Git-blob basis). | ACCEPTED |
| V01_CONTRACT-L0359 | Its source artifact is hash-bound | R09, R37 | INH | V02:L0308–L0310. | ACCEPTED |
| V01_CONTRACT-L0361 | Baseline follows | R09 | INH | Framing. | ACCEPTED |
| V01_CONTRACT-L0363 | 97 acceptances; 157 effects; distribution 62/17/11/7 | R09 | INH | V02:L0312; R4:L0014. Arithmetic check: 62+17+11+7 = 97 and 62+34+33+28 = 157. | ACCEPTED |
| V01_CONTRACT-L0371 | Projected mechanical burden is computed as follows | R09 | INH | Framing; the formula is in batch 006. | ACCEPTED |

## 3. Machine-checkable receipt

```text
BEGIN_AUDIT_RECEIPT
V01_CONTRACT-L0180|INHERITED_UNCHANGED|R06|ACCEPTED||V01_CONTRACT-L0180;V02_ADDENDUM-L0256;REV04_CONTRACT-L0108
V01_CONTRACT-L0189|INHERITED_UNCHANGED|R06,R27|ACCEPTED||V01_CONTRACT-L0189
V01_CONTRACT-L0191|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0106|R22,R24|ACCEPTED||REV04_CONTRACT-L0104;REV04_CONTRACT-L0106
V01_CONTRACT-L0195|INHERITED_UNCHANGED|R06|ACCEPTED||V01_CONTRACT-L0195
V01_CONTRACT-L0197|INHERITED_UNCHANGED|R06|ACCEPTED||V01_CONTRACT-L0197;V02_ADDENDUM-L0068
V01_CONTRACT-L0199|INHERITED_UNCHANGED|R06,R36|ACCEPTED||V01_CONTRACT-L0199
V01_CONTRACT-L0201|INHERITED_UNCHANGED|R06,R36,R40|ACCEPTED||V01_CONTRACT-L0201;V02_ADDENDUM-L0262
V01_CONTRACT-L0211|INHERITED_UNCHANGED|R06|ACCEPTED||V01_CONTRACT-L0211
V01_CONTRACT-L0213|INHERITED_UNCHANGED|R06,R39|ACCEPTED||V01_CONTRACT-L0213
V01_CONTRACT-L0215|INHERITED_UNCHANGED|R06|ACCEPTED||V01_CONTRACT-L0215;V02_ADDENDUM-L0256
V01_CONTRACT-L0219|INHERITED_UNCHANGED|R06|ACCEPTED||V01_CONTRACT-L0219;V02_ADDENDUM-L0155
V01_CONTRACT-L0221|INHERITED_UNCHANGED|R06,R40|ACCEPTED||V01_CONTRACT-L0221;V02_ADDENDUM-L0258
V01_CONTRACT-L0223|INHERITED_UNCHANGED|R06,R11|PENDING|B05-A1_CAPABILITY_PREDICATE_AND_RECEIPT_NOT_ENUMERATED|V01_CONTRACT-L0223;REV04_CONTRACT-L0108;REV04_CONTRACT-L0200
V01_CONTRACT-L0225|INHERITED_UNCHANGED|R06|ACCEPTED||V01_CONTRACT-L0225
V01_CONTRACT-L0229|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0104|R06,R22|ACCEPTED||REV04_CONTRACT-L0104;REV04_CONTRACT-L0108
V01_CONTRACT-L0231|INHERITED_UNCHANGED|R06,R11|PENDING|B05-A1_CAPABILITY_PREDICATE_AND_RECEIPT_NOT_ENUMERATED|V01_CONTRACT-L0231;REV04_CONTRACT-L0150;REV04_CONTRACT-L0156
V01_CONTRACT-L0233|INHERITED_UNCHANGED|R11|ACCEPTED||V01_CONTRACT-L0233;REV04_CONTRACT-L0150
V01_CONTRACT-L0235|INHERITED_UNCHANGED|R06,R04|ACCEPTED||V01_CONTRACT-L0235
V01_CONTRACT-L0239|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0024|C12,R04|ACCEPTED||REV04_CONTRACT-L0024;REV04_CONTRACT-L0110
V01_CONTRACT-L0241|INHERITED_UNCHANGED|C11,C12|ACCEPTED||V01_CONTRACT-L0241
V01_CONTRACT-L0243|INHERITED_UNCHANGED|C11,C12,R33|ACCEPTED||V01_CONTRACT-L0243;V02_ADDENDUM-L0215;V02_ADDENDUM-L0236
V01_CONTRACT-L0245|INHERITED_UNCHANGED|R19|ACCEPTED||V01_CONTRACT-L0245
V01_CONTRACT-L0249|INHERITED_UNCHANGED|R30,R04|ACCEPTED||V01_CONTRACT-L0249;REV04_CONTRACT-L0089
V01_CONTRACT-L0251|INHERITED_UNCHANGED|R30|ACCEPTED||V01_CONTRACT-L0251
V01_CONTRACT-L0253|INHERITED_UNCHANGED|R30|ACCEPTED||V01_CONTRACT-L0253;V02_ADDENDUM-L0268
V01_CONTRACT-L0255|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0089|R30,R01|PENDING|B02-A3_SUCCESSOR_ARM_C_IDS_AND_ATTEST_LINE_NOT_ENUMERATED|V01_CONTRACT-L0255;REV04_CONTRACT-L0089
V01_CONTRACT-L0257|INHERITED_UNCHANGED|R30|ACCEPTED||V01_CONTRACT-L0257;V02_ADDENDUM-L0270
V01_CONTRACT-L0259|INHERITED_UNCHANGED|R30|ACCEPTED||V01_CONTRACT-L0259
V01_CONTRACT-L0261|INHERITED_UNCHANGED|R30,R27|ACCEPTED||V01_CONTRACT-L0261;V02_ADDENDUM-L0270
V01_CONTRACT-L0268|INHERITED_UNCHANGED|R30|ACCEPTED||V01_CONTRACT-L0268
V01_CONTRACT-L0270|INHERITED_UNCHANGED|R30,R10|ACCEPTED||V01_CONTRACT-L0270
V01_CONTRACT-L0272|INHERITED_UNCHANGED|R30,R10|ACCEPTED||V01_CONTRACT-L0272
V01_CONTRACT-L0274|INHERITED_UNCHANGED|R30,R10|ACCEPTED||V01_CONTRACT-L0274
V01_CONTRACT-L0276|INHERITED_UNCHANGED|R30,R10,R12|ACCEPTED||V01_CONTRACT-L0276;REV04_CONTRACT-L0261
V01_CONTRACT-L0280|INHERITED_UNCHANGED|C01,C02,C03,C04,C05,C06,C07,C08,C09,C10,C11,C12,C13,R37|ACCEPTED||V01_CONTRACT-L0280
V01_CONTRACT-L0282|INHERITED_UNCHANGED|R10|ACCEPTED||V01_CONTRACT-L0282
V01_CONTRACT-L0284|INHERITED_UNCHANGED|R36,R37|ACCEPTED||V01_CONTRACT-L0284
V01_CONTRACT-L0288|INHERITED_UNCHANGED|R08|ACCEPTED||V01_CONTRACT-L0288
V01_CONTRACT-L0290|INHERITED_UNCHANGED|R08|ACCEPTED||V01_CONTRACT-L0290;REV04_CONTRACT-L0012
V01_CONTRACT-L0295|INHERITED_UNCHANGED|R08,R28|ACCEPTED||V01_CONTRACT-L0295;REV04_CONTRACT-L0032
V01_CONTRACT-L0297|INHERITED_UNCHANGED|R19|ACCEPTED||V01_CONTRACT-L0297
V01_CONTRACT-L0299|INHERITED_UNCHANGED|R08,R27|ACCEPTED||V01_CONTRACT-L0299
V01_CONTRACT-L0301|INHERITED_UNCHANGED|R08,R28|ACCEPTED||V01_CONTRACT-L0301;REV04_CONTRACT-L0094
V01_CONTRACT-L0305|INHERITED_UNCHANGED|R08|ACCEPTED||V01_CONTRACT-L0305;REV04_CONTRACT-L0094
V01_CONTRACT-L0309|INHERITED_UNCHANGED|R27|ACCEPTED||V01_CONTRACT-L0309;REV04_CONTRACT-L0098;REV04_CONTRACT-L0140
V01_CONTRACT-L0312|INHERITED_UNCHANGED|R27,R08|ACCEPTED||V01_CONTRACT-L0312;REV04_CONTRACT-L0098
V01_CONTRACT-L0315|INHERITED_UNCHANGED|R10,R08|ACCEPTED||V01_CONTRACT-L0315;V02_ADDENDUM-L0286
V01_CONTRACT-L0318|INHERITED_UNCHANGED|R27|ACCEPTED||V01_CONTRACT-L0318;V02_ADDENDUM-L0288
V01_CONTRACT-L0322|INHERITED_UNCHANGED|R27,R19|ACCEPTED||V01_CONTRACT-L0322
V01_CONTRACT-L0325|INHERITED_UNCHANGED|R08|ACCEPTED||V01_CONTRACT-L0325;V02_ADDENDUM-L0292;REV04_CONTRACT-L0098
V01_CONTRACT-L0327|INHERITED_UNCHANGED|R08|ACCEPTED||V01_CONTRACT-L0327
V01_CONTRACT-L0331|INHERITED_UNCHANGED|R10|ACCEPTED||V01_CONTRACT-L0331
V01_CONTRACT-L0333|INHERITED_UNCHANGED|R10,R08|ACCEPTED||V01_CONTRACT-L0333;V02_ADDENDUM-L0288;REV04_CONTRACT-L0014
V01_CONTRACT-L0341|INHERITED_UNCHANGED|R28,R08|ACCEPTED||V01_CONTRACT-L0341;REV04_CONTRACT-L0094
V01_CONTRACT-L0345|INHERITED_UNCHANGED|R10|ACCEPTED||V01_CONTRACT-L0345;REV04_CONTRACT-L0158
V01_CONTRACT-L0347|INHERITED_UNCHANGED|R10|ACCEPTED||V01_CONTRACT-L0347
V01_CONTRACT-L0349|INHERITED_UNCHANGED|R10|ACCEPTED||V01_CONTRACT-L0349;REV04_CONTRACT-L0014
V01_CONTRACT-L0350|INHERITED_UNCHANGED|R10|ACCEPTED||V01_CONTRACT-L0350;REV04_CONTRACT-L0014
V01_CONTRACT-L0351|INHERITED_UNCHANGED|R10|ACCEPTED||V01_CONTRACT-L0351;REV04_CONTRACT-L0014
V01_CONTRACT-L0353|INHERITED_UNCHANGED|R10|ACCEPTED||V01_CONTRACT-L0353;REV04_CONTRACT-L0014
V01_CONTRACT-L0357|INHERITED_UNCHANGED|R09|ACCEPTED||V01_CONTRACT-L0357;V02_ADDENDUM-L0308
V01_CONTRACT-L0359|INHERITED_UNCHANGED|R09,R37|ACCEPTED||V01_CONTRACT-L0359;V02_ADDENDUM-L0310
V01_CONTRACT-L0361|INHERITED_UNCHANGED|R09|ACCEPTED||V01_CONTRACT-L0361
V01_CONTRACT-L0363|INHERITED_UNCHANGED|R09|ACCEPTED||V01_CONTRACT-L0363;V02_ADDENDUM-L0312;REV04_CONTRACT-L0014
V01_CONTRACT-L0371|INHERITED_UNCHANGED|R09|ACCEPTED||V01_CONTRACT-L0371
END_AUDIT_RECEIPT
```

Counts: 65 rows; 62 ACCEPTED; 3 PENDING; 4 SUPERSEDED_BY_REV04; 61 INHERITED_UNCHANGED; 0 NOT_APPLICABLE_TO_SUCCESSOR.

## 4. Attestation and boundaries

- **Reviewer: claude-04** (Claude, independent clause auditor). I independently read the governing source for every unit above. I did **not** author the source inventory, the batch plan, the blind second golden-vector implementation or the independent scorer, and I will not author the latter two.
- A reviewed batch is not an F1-approved batch. No source was edited; PENDING items remain open.
- Only this message file was written. No owner evidence, credential, key or WebAuthn state touched. B01/B02 accepted; Attempt 001 immutable AMEND; F1/F2 unfrozen; Attempt 002 not authorized.

```text
MC0030_MESSAGE038=CLAUDE_AUDIT_BATCH005
DISPOSITION=AMEND_AUDIT_BATCH005
UNITS_AUDITED=65_OF_65
ACCEPTED=62
PENDING=3
KEY_FINDING=B05-A1_NOT_REALIZABLE_CAPABILITY_PREDICATE_NOT_ENUMERATED_G1_RELEVANT
F1=NOT_APPROVED
ATTEMPT_002=NOT_AUTHORIZED
```
