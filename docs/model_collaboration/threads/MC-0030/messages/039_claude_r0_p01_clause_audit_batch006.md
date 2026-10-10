# MC-0030 Message 039: Claude independent clause audit, batch Q0-AUDIT-006 (V01 implementation contract §12–§15)

```text
Thread                  MC-0030
Message                 039
Author / reviewer       Claude / claude-04 (independent clause auditor)
Conversation            04 - Assurance and Delivery Architecture Design
Coordination branch     v1-source-vault-bootstrap-resume
Parent HEAD             3af203ffeaafe3d1f3985f2bb4de81da02d8fbf7 (Message 038)
Batch                   Q0-AUDIT-006 / V01_CONTRACT / 35 units / V01_CONTRACT-L0373 .. V01_CONTRACT-L0472
Batch unit-list SHA-256 recomputed from the plan's ordered IDs: match
Source                  experiments/r0_p01_owner_acceptance_v01/implementation_contract.md
Source SHA-256          b3b90d851e25a4b906f6e094e6366ca42baca7fceb7c38c253f8220bc70b1202 (Git blob, matches inventory)
Cross-checked against   V02 addendum, REV04 contract, Q1 implementation-boundary candidate and Q1 F1/F2 independence
                        addition (both UNFROZEN, read as context only), Q0 REV02 trace
Disposition             AMEND_AUDIT_BATCH006
Authority               Message 034. Audit record only. No F1/F2 freeze, inventory edit, credential or Attempt 002.
```

## 0. Verification and method

- The branch head before writing was `3af203ff…` (my Message 038, parent `18308cc7…`, one added file). The receipt checker returned `PASS batches=5/18 units=281/1022`.
- Source hash unchanged. The 35 IDs hash to the plan value; every `text_sha256` matches. This batch completes V01_CONTRACT; together with batches 004–005 all 165 V01_CONTRACT units are reviewed.
- Method and notation as before. The Q1 documents are unfrozen proposals. I use them only to show *where* a V01 rule would be displaced; they are not approved authority, so they cannot be a SUPERSEDED_BY_REV04 basis.

## 1. Verdict

**`AMEND_AUDIT_BATCH006`**: 35/35 reviewed; **29 ACCEPTED, 6 PENDING**.

The classification and result-integrity rules (§12 tail, §13, §15) are preserved or cleanly superseded by REV04 G1 and the successor start-marker rule. The pending units are all in §14, the *implementation boundary*. Its V01 rules are still formally inherited (REV04 does not address them), but the successor design cannot satisfy them as written.

Findings:

1. **B06-A1. The successor implementation boundary has no approved rule text.**
   - V01 §14 limits the implementation to exactly three files (harness.py, webauthn_server.mjs with the embedded client, score.py) and a fixed read list.
   - The successor requires an isolated independent scorer that may not import the core/owner/RP modules (R36), a blind second oracle, a preclaim static page and routes (R22), separate RP receipt streams (R35), guard/KAT artifacts (R37) and Windows-native qualification code (R38).
   - The only layout proposals are the **unfrozen** Q1 candidate (five logical units plus an oracle). Nothing approved replaces V01 §14.
   - F1/F2 must either supersede §14 explicitly in an approved artifact (file/module set, import-graph rule, per-role read lists including what the blind oracle author may *not* read) or the successor is in literal violation of an inherited rule.
2. **B02-A4 now has inventoried source units.** V01:L0432 ("No project dependency file may change") and V01:L0434 ("Only Python standard library and Node built-ins") are the indexed form of the V02 line-18 clash recorded in Message 035. The Python standard library has no Ed25519, so an in-process SSHSIG scorer (R36) needs either a reviewed pure-Python implementation or a reviewed dependency exception with pinned hashes (R39). The test-only Playwright virtual authenticator (R40) also needs an explicit test-scope exception.
3. **B06-F1. "Must not read any later owner-trial result" (V01:L0447) versus the result-informed successor.** REV04 openly declares itself result-informed (R4:L0016, L0064). It *requires* reading the preserved Attempt 001 public snapshot to build the old-digest set (R4:L0182, R23). So for Attempt 001 results the V01 rule is superseded by disclosed design, which I record as superseded with that basis. For Attempt 002 the rule's intent survives through F2 freezing before any claim (R24, R34). This should be stated as rule text so that a reviewer can tell permitted Attempt-001 reads from forbidden ones.

## 2. Per-unit audit record (35 units)

### §12 Legacy-volume estimate (tail) and classification

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTRACT-L0373 | Projected burden = 97 × selected median small mechanical seconds / 60 | R09 | INH | V02:L0312; R4:L0100. Message 036 B03-R2: binding at median > 5400/97 ≈ 55.670 s. | ACCEPTED |
| V01_CONTRACT-L0375 | If the source digest no longer matches, refreeze the inventory before classification | R09, R13, R37 | SUP:L0206 | Pre-claim: block without consuming a claim. Post-claim: mechanical integrity flag, never an indefinite "pending refreeze" (Message 036 B03-R3; R4:L0144, L0206, L0209). | ACCEPTED |
| V01_CONTRACT-L0377 | If projected acceptances >100 or projected burden >90 minutes, then | R09 | INH | Framing for L0379. | ACCEPTED |
| V01_CONTRACT-L0379 | No PASS_WITH_SELECTION; bounded batch/class design required; disposition AMEND | R09, R12 | INH | R4:L0169 (precedence row 6). With the inventory fixed at 97, only the minutes test can trigger. | ACCEPTED |
| V01_CONTRACT-L0383 | …unless a stronger preregistered reason requires REOPEN/INVALID | R12, R13 | INH | Now a mechanical precedence table: INVALID rows 1–3, REOPEN row 4, AMEND rows 5–6 (R4:L0162–L0170). | ACCEPTED |
| V01_CONTRACT-L0385 | Proof viability is intentionally weaker than selection eligibility | R10, R12 | INH | — | ACCEPTED |
| V01_CONTRACT-L0387 | An arm is proof-viable when | R10, R12 | INH | Framing for L0389. | ACCEPTED |
| V01_CONTRACT-L0389 | REALIZABLE; controls 1–10 PASS; ≥1 owner-authenticated small proof succeeds; no secret exposure | R10, R12, R19 | INH | V02:L0288 identical. B01 decision table tests (T-VIABILITY-*). | ACCEPTED |
| V01_CONTRACT-L0394 | Classification then follows result_contract.json | R12 | INH | Pointer; the result contract is audited in batch 018. | ACCEPTED |
| V01_CONTRACT-L0396 | No proof-viable A/B arm → REOPEN | R12, R11 | SUP:L0156 | G1: REOPEN only if both A/B evidence states are COMPLETED or NOT_REALIZABLE; otherwise INVALID_INCOMPLETE. Owner-accepted (B01). | ACCEPTED |
| V01_CONTRACT-L0399 | ≥1 proof-viable, none eligible → AMEND | R12 | INH | R4:L0168 (row 5). | ACCEPTED |
| V01_CONTRACT-L0402 | Eligible selected arm but volume gate triggers → AMEND | R12, R09 | INH | R4:L0169 (row 6). | ACCEPTED |
| V01_CONTRACT-L0405 | Eligible selected arm within volume → PASS_WITH_SELECTION | R12, R10 | INH | R4:L0170 (row 7), plus the mandatory G2 flag when the other arm is INCOMPLETE. | ACCEPTED |
| V01_CONTRACT-L0408 | Preserves Research 513's distinction between an unusable architecture and a viable path needing bounded work | R12 | INH | Rationale for REOPEN versus AMEND. | ACCEPTED |

### §13 Result integrity

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTRACT-L0412 | Produce a machine-readable result conforming to result_contract.json | R12, R16 | INH | The successor raw schema adds REV04 flags and evidence_state (Message 036, V02:L0282). | ACCEPTED |
| V01_CONTRACT-L0414 | No credential secret is ever part of that result | R19 | INH | — | ACCEPTED |
| V01_CONTRACT-L0416 | Proof artifacts and public keys needed for independent verification may be preserved | R16, R36 | INH | Kept in owner-local evidence; the public repository receives no identifying public IDs (R4:L0138). | ACCEPTED |
| V01_CONTRACT-L0418 | Raw owner-trial results are frozen before architectural interpretation | R16, R32 | INH | R4:L0136–L0138 (hash-linked snapshots, owner final-head witness before scoring). | ACCEPTED |
| V01_CONTRACT-L0420 | No post-result threshold, fixture, selection-rule or control change within the same attempt | R13, R10 | INH | Violation is the `post_observation_tuning` integrity flag (R4:L0164, L0225). | ACCEPTED |

### §14 Implementation boundary

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTRACT-L0424 | The implementation phase may add only the following | R34, R36, R37 | INH | Not superseded by any approved text; incompatible with the successor's isolated scorer, oracle and preclaim artifacts. | **PENDING** B06-A1 |
| V01_CONTRACT-L0426 | harness.py, webauthn_server.mjs, score.py | R34, R36, R37 | INH | As L0424. The Q1 candidate (unfrozen) proposes p01_core / p01_owner / p01_rp / p01_score plus a test-only oracle. | **PENDING** B06-A1 |
| V01_CONTRACT-L0430 | The WebAuthn client is embedded in webauthn_server.mjs so the implementation stays three files | R06, R22, R34 | INH | The successor also serves a separate preclaim static page and routes (R4:L0104, L0184). The file rule needs explicit successor text. | **PENDING** B06-A1 |
| V01_CONTRACT-L0432 | No project dependency file may change | R39 | INH | Indexed form of B02-A4. | **PENDING** B02-A4 |
| V01_CONTRACT-L0434 | Only Python standard library and Node built-ins | R39, R36 | INH | Clashes with in-process SSHSIG/Ed25519 in the scorer (R36) and test-only Playwright (R40). | **PENDING** B02-A4 |
| V01_CONTRACT-L0436 | The implementation may read the following | R36 | INH | Framing for L0438. | ACCEPTED |
| V01_CONTRACT-L0438 | Read list: Research 512/513, P01 freeze record, fixture, V01 contracts, result contract, inventory rule | R36, R34 | INH | V01-only list. The successor needs per-role read lists: the primary implementer adds V02, REV04 contract/policy and F1; the blind oracle author must *exclude* primary source and outputs (Q1 independence addition, unfrozen). | **PENDING** B06-A1 |
| V01_CONTRACT-L0447 | The implementation must not read any later owner-trial result | R29, R23, R24 | SUP:L0016 | Attempt 001 results are deliberately read under declared result-informed design (R4:L0016, L0064, L0182). Attempt 002 results cannot inform its own frozen implementation (F2 before claim). B06-F1. | ACCEPTED |
| V01_CONTRACT-L0449 | The implementation must not execute a real owner credential operation | R19, R24 | INH | R4:L0258 (all tests synthetic). | ACCEPTED |
| V01_CONTRACT-L0451 | Allowed pretrial checks are the following | R20 | INH | Framing for L0453. | ACCEPTED |
| V01_CONTRACT-L0453 | Syntax; deterministic vectors; mutation logic with synthetic doubles; WebAuthn structural vectors without a real owner credential; schema/classification tests; HTTP startup without ceremonies; redaction checks | R20, R38, R40 | SUP:L0258 | REV04 §10 requires a strictly larger synthetic matrix: integrated A/B/C dry run, virtual CTAP2 ceremonies, Windows-native tests, KAT, fault injection. All synthetic, so the "no real owner credential" limit is preserved. | ACCEPTED |
| V01_CONTRACT-L0461 | Real SSH signing, WebAuthn and ChatGPT attestation begin only after implementation review and freeze | R24, R34, R21 | INH | R4:L0021 plus the separate owner execution decision (R4:L0254). | ACCEPTED |

### §15 Attempt boundary

| Unit | Normative meaning | IDs | Disp. | Basis and successor treatment | Status |
|---|---|---|---|---|---|
| V01_CONTRACT-L0465 | The first owner-visible credential invocation freezes Attempt 001 | R24 | SUP:L0021 | V02:L0316 already moved the boundary earlier; the successor uses an exclusive start marker before the first owner-sensitive action. | ACCEPTED |
| V01_CONTRACT-L0467 | After that point | R17, R18 | INH | Framing for L0469. | ACCEPTED |
| V01_CONTRACT-L0469 | No result-guided repair inside the attempt; a defect requires preservation, explicit classification and prospective refreeze | R17, R18, R12 | INH | REV04 makes the classification mechanical (INVALID_INSTRUMENT/INTEGRITY) and limits any repair to the ALL_REQUIRED exceptional claim (R4:L0241). | ACCEPTED |
| V01_CONTRACT-L0472 | No retry-to-green | R18, R17 | INH | R4:L0240–L0242. | ACCEPTED |

## 3. Machine-checkable receipt

```text
BEGIN_AUDIT_RECEIPT
V01_CONTRACT-L0373|INHERITED_UNCHANGED|R09|ACCEPTED||V01_CONTRACT-L0373;V02_ADDENDUM-L0312;REV04_CONTRACT-L0100
V01_CONTRACT-L0375|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0206|R09,R13,R37|ACCEPTED||REV04_CONTRACT-L0144;REV04_CONTRACT-L0206;REV04_CONTRACT-L0209
V01_CONTRACT-L0377|INHERITED_UNCHANGED|R09|ACCEPTED||V01_CONTRACT-L0377
V01_CONTRACT-L0379|INHERITED_UNCHANGED|R09,R12|ACCEPTED||V01_CONTRACT-L0379;REV04_CONTRACT-L0169
V01_CONTRACT-L0383|INHERITED_UNCHANGED|R12,R13|ACCEPTED||V01_CONTRACT-L0383;REV04_CONTRACT-L0162
V01_CONTRACT-L0385|INHERITED_UNCHANGED|R10,R12|ACCEPTED||V01_CONTRACT-L0385
V01_CONTRACT-L0387|INHERITED_UNCHANGED|R10,R12|ACCEPTED||V01_CONTRACT-L0387
V01_CONTRACT-L0389|INHERITED_UNCHANGED|R10,R12,R19|ACCEPTED||V01_CONTRACT-L0389;V02_ADDENDUM-L0288
V01_CONTRACT-L0394|INHERITED_UNCHANGED|R12|ACCEPTED||V01_CONTRACT-L0394
V01_CONTRACT-L0396|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0156|R12,R11|ACCEPTED||REV04_CONTRACT-L0156;REV04_CONTRACT-L0166;REV04_CONTRACT-L0167
V01_CONTRACT-L0399|INHERITED_UNCHANGED|R12|ACCEPTED||V01_CONTRACT-L0399;REV04_CONTRACT-L0168
V01_CONTRACT-L0402|INHERITED_UNCHANGED|R12,R09|ACCEPTED||V01_CONTRACT-L0402;REV04_CONTRACT-L0169
V01_CONTRACT-L0405|INHERITED_UNCHANGED|R12,R10|ACCEPTED||V01_CONTRACT-L0405;REV04_CONTRACT-L0170;REV04_CONTRACT-L0158
V01_CONTRACT-L0408|INHERITED_UNCHANGED|R12|ACCEPTED||V01_CONTRACT-L0408
V01_CONTRACT-L0412|INHERITED_UNCHANGED|R12,R16|ACCEPTED||V01_CONTRACT-L0412
V01_CONTRACT-L0414|INHERITED_UNCHANGED|R19|ACCEPTED||V01_CONTRACT-L0414
V01_CONTRACT-L0416|INHERITED_UNCHANGED|R16,R36|ACCEPTED||V01_CONTRACT-L0416;REV04_CONTRACT-L0138
V01_CONTRACT-L0418|INHERITED_UNCHANGED|R16,R32|ACCEPTED||V01_CONTRACT-L0418;REV04_CONTRACT-L0136;REV04_CONTRACT-L0138
V01_CONTRACT-L0420|INHERITED_UNCHANGED|R13,R10|ACCEPTED||V01_CONTRACT-L0420;REV04_CONTRACT-L0164;REV04_CONTRACT-L0225
V01_CONTRACT-L0424|INHERITED_UNCHANGED|R34,R36,R37|PENDING|B06-A1_SUCCESSOR_IMPLEMENTATION_BOUNDARY_NOT_APPROVED|V01_CONTRACT-L0424
V01_CONTRACT-L0426|INHERITED_UNCHANGED|R34,R36,R37|PENDING|B06-A1_SUCCESSOR_IMPLEMENTATION_BOUNDARY_NOT_APPROVED|V01_CONTRACT-L0426
V01_CONTRACT-L0430|INHERITED_UNCHANGED|R06,R22,R34|PENDING|B06-A1_SUCCESSOR_IMPLEMENTATION_BOUNDARY_NOT_APPROVED|V01_CONTRACT-L0430;REV04_CONTRACT-L0104;REV04_CONTRACT-L0184
V01_CONTRACT-L0432|INHERITED_UNCHANGED|R39|PENDING|B02-A4_DEPENDENCY_POLICY_STDLIB_VS_R36_R39|V01_CONTRACT-L0432
V01_CONTRACT-L0434|INHERITED_UNCHANGED|R39,R36|PENDING|B02-A4_DEPENDENCY_POLICY_STDLIB_VS_R36_R39|V01_CONTRACT-L0434
V01_CONTRACT-L0436|INHERITED_UNCHANGED|R36|ACCEPTED||V01_CONTRACT-L0436
V01_CONTRACT-L0438|INHERITED_UNCHANGED|R36,R34|PENDING|B06-A1_PER_ROLE_READ_LISTS_NOT_APPROVED|V01_CONTRACT-L0438
V01_CONTRACT-L0447|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0016|R29,R23,R24|ACCEPTED||REV04_CONTRACT-L0016;REV04_CONTRACT-L0064;REV04_CONTRACT-L0182
V01_CONTRACT-L0449|INHERITED_UNCHANGED|R19,R24|ACCEPTED||V01_CONTRACT-L0449;REV04_CONTRACT-L0258
V01_CONTRACT-L0451|INHERITED_UNCHANGED|R20|ACCEPTED||V01_CONTRACT-L0451
V01_CONTRACT-L0453|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0258|R20,R38,R40|ACCEPTED||REV04_CONTRACT-L0258;REV04_CONTRACT-L0268
V01_CONTRACT-L0461|INHERITED_UNCHANGED|R24,R34,R21|ACCEPTED||V01_CONTRACT-L0461;REV04_CONTRACT-L0021;REV04_CONTRACT-L0254
V01_CONTRACT-L0465|SUPERSEDED_BY_REV04:REV04_CONTRACT-L0021|R24|ACCEPTED||REV04_CONTRACT-L0021;V02_ADDENDUM-L0316
V01_CONTRACT-L0467|INHERITED_UNCHANGED|R17,R18|ACCEPTED||V01_CONTRACT-L0467
V01_CONTRACT-L0469|INHERITED_UNCHANGED|R17,R18,R12|ACCEPTED||V01_CONTRACT-L0469;REV04_CONTRACT-L0241
V01_CONTRACT-L0472|INHERITED_UNCHANGED|R18,R17|ACCEPTED||V01_CONTRACT-L0472;REV04_CONTRACT-L0240
END_AUDIT_RECEIPT
```

Counts: 35 rows; 29 ACCEPTED; 6 PENDING; 5 SUPERSEDED_BY_REV04; 30 INHERITED_UNCHANGED; 0 NOT_APPLICABLE_TO_SUCCESSOR.

## 4. Attestation and boundaries

- **Reviewer: claude-04** (Claude, independent clause auditor). I independently read the governing source for every unit above. I did **not** author the source inventory, the batch plan, the blind second golden-vector implementation or the independent scorer, and I will not author the latter two.
- A reviewed batch is not an F1-approved batch. No source was edited; PENDING items remain open.
- Only this message file was written. No owner evidence, credential, key or WebAuthn state touched. B01/B02 accepted; Attempt 001 immutable AMEND; F1/F2 unfrozen; Attempt 002 not authorized.

```text
MC0030_MESSAGE039=CLAUDE_AUDIT_BATCH006
DISPOSITION=AMEND_AUDIT_BATCH006
UNITS_AUDITED=35_OF_35
ACCEPTED=29
PENDING=6
V01_CONTRACT_COVERAGE=165_OF_165_UNITS_REVIEWED_ACROSS_BATCHES_004_005_006
KEY_FINDINGS=B06-A1_IMPLEMENTATION_BOUNDARY_UNAPPROVED;B02-A4_INDEXED_AT_V01_L0432_L0434;B06-F1_ATTEMPT001_READS_RESULT_INFORMED
F1=NOT_APPROVED
ATTEMPT_002=NOT_AUTHORIZED
```
