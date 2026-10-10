# MC-0030 Message 042: Claude independent clause audit, batch Q0-AUDIT-009 (REV04 contract §10–§11)

```text
Thread                  MC-0030
Message                 042
Author / reviewer       Claude / claude-04 (independent clause auditor)
Conversation            04 - Assurance and Delivery Architecture Design
Coordination branch     v1-source-vault-bootstrap-resume
Parent HEAD             951873d79c0900ed96c25769861eb9965da452db (Message 041)
Batch                   Q0-AUDIT-009 / REV04_CONTRACT / 26 units / REV04_CONTRACT-L0266 .. REV04_CONTRACT-L0300
Batch unit-list SHA-256 recomputed from the plan's ordered IDs: match
Source                  docs/research/r0_p01_successor_design/R0_P01_CONTRACT_V03_UNFROZEN_DRAFT.md
Source SHA-256          9160a30c481c1c67c2ec857238f5a04b44f618b2ef589ef4f1c514eb3b3d6175 (B01/B02-approved REV04; matches inventory)
Cross-checked against   B01/B02 owner acceptance records, REV04 outcome policy, Q0 REV02 trace, REV03 test catalogue,
                        Messages 033 and 035–041
Disposition             ACCEPT_AUDIT_BATCH009
Authority               Message 034. Audit record only. No F1/F2 freeze, inventory edit, credential or Attempt 002.
```

## 0. Verification and method

- The branch head before writing was `951873d7…` (my Message 041, parent `db596ec7…`, one added file). The receipt checker returned `PASS batches=8/18 units=446/1022`.
- Source hash equals the approved REV04 SHA. The 26 IDs hash to the plan value; every `text_sha256` matches. This batch completes REV04_CONTRACT: 156/156 units across batches 007–009. The 19 out-of-section lines (3–8 and 304–316) are audited in §3.
- Convention B07-S1 applies (`INH*` = approved successor text retained). For the §11 blocker bullets, `ACCEPTED` means *the mapping of the blocker to requirements is settled*. It does **not** mean the blocker is resolved; B03–B10 remain open qualification work.

## 1. Verdict

**`ACCEPT_AUDIT_BATCH009`**: 26/26 reviewed; **26 ACCEPTED, 0 PENDING**.

§10.1 (the Message 023/025 acceptance matrix) and §11 (the canonical blocker list) are consistent with §1–§10 and with each other. Each R1–R9 and T1–T3 matrix item has a matching catalogue test.

**Cross-reference of campaign findings to the approved §11 blockers.** This keeps reconciliation from treating already-tracked work as new:

| Campaign finding | Already inside an approved §11 blocker? | Assessment |
|---|---|---|
| B02-A3 successor acceptance-ID strings | **Yes**: B05 "Freeze exact successor context/project/prefix grammar" (L0293) | Tracked open work, not an omission. It stays PENDING at the affected units until frozen. |
| A1/A3 rejection-layer test sensitivity | Partly: B05 "rejection-layer receipts" (L0293) | B05 asks for the receipts, not that each vector *reaches* the claimed layer. A1/A3 add that. |
| B05-A1 NOT_REALIZABLE capability predicate | **No**: B06 covers the preflight browser, not capability evidence; B04 covers "WebAuthn terminal outcomes", not NOT_REALIZABLE | New; G1-critical. |
| B07-A3 precheck failure classification | Partly: B03 "immutable preconditions" and B04 "complete exception-site inventory" | The *classification* conflict between L0066 and L0206 is not named. New. |
| B08-A1 ambiguous abort/Node-exit rule | Partly: B06 "Windows Node child Ctrl+C safety" | The frozen tie-break rule demanded by L0215 is not named. New. |
| B07-A2 complete T3 table | Partly: B09 "T1/T2/T3 explanation" | B09 covers owner explanation, not the pinned per-role byte table bound by the claim. New. |
| B02-A1 AC-4 ADMIT negatives; A9 | No | New test obligations under existing C/R rules. |
| B02-A2 scenario isolation; A6 non-production and anti-weakening | Partly: B08 full synthetic composition; L0087 for anti-weakening | Rule text missing. |
| B02-A4 dependency policy; B06-A1 implementation boundary | No (Q1 candidate only, unfrozen) | New governance items for F1/F2. |

## 2. Per-unit audit record (26 units)

### §10 test matrix (tail) and §10.1 acceptance matrix

| Unit | Normative meaning | IDs | Disp. | Concerns / tests | Status |
|---|---|---|---|---|---|
| REV04_CONTRACT-L0266 | Evidence audit: exact prior-file-byte hash chain; deletion/mutation/reorder detectable with an external final digest; no resume; interaction floor versus reported count; browser landmarks | R16, R27 | INH* | T-HASH-CHAIN, T-INTERACTION-FLOOR, T-LANDMARKS. | ACCEPTED |
| REV04_CONTRACT-L0267 | No cross-process resume and no Ctrl+C handler: uninterrupted A→B→C, abort during SSH/Node/browser/pause, preserved class and marker, no reissue on restart | R31, R17 | INH* | T-NO-RESUME, T-PAUSE-ABORT. | ACCEPTED |
| REV04_CONTRACT-L0268 | Complete synthetic A→B→C run with all 13 controls and 1/2/4/30 burdens, then the independent scorer; failure/interrupt/negative runs; old Attempt 001 proofs cannot satisfy successor policy | R20, R32, R29 | INH* | T-SYNTHETIC-A-B-C, T-NO-POOL. | ACCEPTED |
| REV04_CONTRACT-L0269 | Documentation and authorization: integrity checks, exact fixture vectors, scoring/KAT policy hashes, Research 513 approval if G1/G2 kept, owner policy consent before freeze, attestations of no private-key or real-proof access by models | R37, R21, R19 | INH* | Research 513/G1-G2 approval and policy consent are now on record (B01/B02). | ACCEPTED |
| REV04_CONTRACT-L0274 | R1 false-REOPEN cases: realizable-then-abort → INVALID_INCOMPLETE; A and B completed no-proof → REOPEN; A eligible, B aborted → PASS with G2; A nonviable, B incomplete → INVALID_INCOMPLETE; P0 S versus Ctrl+C distinguished | R11, R12 | INH* | T-EVIDENCE-G1, T-G1-G2-TABLE. | ACCEPTED |
| REV04_CONTRACT-L0275 | R2/R3: enumerate six integrity and three instrument flags, summary/kind consistency, contradictory/missing flags; VERIFIER_ERROR → INVALID_INSTRUMENT with attempt_integrity false; integrity+instrument → INTEGRITY; narratives never change the code | R13 | INH* | T-FLAG-PRECEDENCE, T-SCORER-PRECEDENCE. | ACCEPTED |
| REV04_CONTRACT-L0276 | R4 policy schema: one canonical unresolved_blockers list byte-equal to §11 IDs; seven nonoverlapping rows; one precedence per branch; no retry after PASS; ALL_REQUIRED cap; pending is not final | R18, R13 | INH* | Byte equality is checked in the policy batches (010–013). | ACCEPTED |
| REV04_CONTRACT-L0277 | R5/R8 interrupt: S/other closes only the event; dependents FAIL/unexecuted; Ctrl+C at prompts aborts the attempt; Node Ctrl+C on Windows leaves durable receipts or explicit absence; stable G1 class | R17, R26, R38 | INH* | T-CTRL-C-SSH, T-CTRL-C-NODE. B08-A1 supplies the missing tie-break rule. | ACCEPTED |
| REV04_CONTRACT-L0278 | R6 atomic evidence crash cases: temp/fsync/rename crash, orphan, collision, truncated final, link mismatch, deleted/reordered files, replaced digest without witness, missing witness; owner receipt before scoring | R16, R38 | INH* | T-ATOMIC-SNAPSHOTS, T-WIN-MOVEFILE-WRITETHROUGH. | ACCEPTED |
| REV04_CONTRACT-L0279 | R7: any PASS_WITH_SELECTION, with or without G2, blocks every new claim, including "qualify B" | R18 | INH* | T-NO-POST-PASS, T-B02-POST-PASS-DENIED. | ACCEPTED |
| REV04_CONTRACT-L0280 | R9 details: successor-context historical verifier, rejection_layer, old set includes mutated non-owner negatives, preclaim scan excludes KAT verifier, UA mismatch non-blocking, CDP authenticator ≠ Windows Hello, no production inference from synthetic labels | R23, R22, R40, R36, R01 | INH* | — | ACCEPTED |
| REV04_CONTRACT-L0281 | T1: four RP-consumed NotAllowedError/cancel/timeout B assertions → B COMPLETED; with A COMPLETED/nonviable → REOPEN; A eligible + B completed cancellations → PASS without G2; NotSupportedError → capability; other faults instrument | R07, R11, R12 | INH* | T-EVIDENCE-CANCEL. The NotSupportedError branch depends on B05-A1 (recorded at L0150/L0200). | ACCEPTED |
| REV04_CONTRACT-L0282 | T2: every exception site maps to one action via an independently checked inventory; typo/CONFIRM re-prompts; setup input never coerced; tool unavailability is instrument; intact-chain exception versus integrity; abort-versus-Node-exit ordering tested | R15 | INH* | T-ERROR-SITE-INVENTORY, T-INPUT-REPROMPT. | ACCEPTED |
| REV04_CONTRACT-L0283 | T3: missing final-head receipt sets only the disclosure flag; witness presence cannot change class; proven chain break must | R13, R16 | INH* | T-WITNESS-DISCLOSURE. | ACCEPTED |

### §11 Canonical blockers

| Unit | Normative meaning | IDs | Disp. | Concerns / tests | Status |
|---|---|---|---|---|---|
| REV04_CONTRACT-L0287 | The policy's unresolved_blockers must contain exactly these IDs, with no competing list; they are approvals and conformance work, not open design criticisms | R37, R21 | INH* | — | ACCEPTED |
| REV04_CONTRACT-L0289 | B01: family approval of evidence_state, G1, G2, mechanical INVALID reasons and provisional identity R0-P01-V01-I1; no reinterpretation of Attempt 001 | R21, R11, R12 | INH* | Satisfied by the B01 owner acceptance record. | ACCEPTED |
| REV04_CONTRACT-L0290 | B02: owner policy approval before freeze; separate execution assent only after qualified implementation | R21, R18 | INH* | Policy part satisfied by B02; execution assent outstanding. | ACCEPTED |
| REV04_CONTRACT-L0291 | B03: native Windows SSH qualification with synthetic keys (R/S path, preconditions, existing signature, prompt visibility, event versus attempt termination, no secret logging) | R38, R05 | INH* | Open. Expected classifications await B07-A3. | ACCEPTED |
| REV04_CONTRACT-L0292 | B04: pinned SSH/WebAuthn KATs, temp-file verifier tests, tri-state VERIFY, complete exception-site inventory, flag origins, WebAuthn terminal outcomes, deterministic precedence | R14, R15, R13 | INH* | Open. B08-A1 belongs here. | ACCEPTED |
| REV04_CONTRACT-L0293 | B05: freeze successor context/project/prefix grammar, key-independent vectors, synthetic-key P0/P5/P6 templates, old digest coverage, old-key inequality, rejection-layer receipts | R01, R23, R33, R36 | INH* | Open. This is where B02-A3 and A1/A3 are discharged. | ACCEPTED |
| REV04_CONTRACT-L0294 | B06: preclaim page and scan, launch/UA receipts, post-claim readiness, same-attempt A recovery dependency, Windows Node Ctrl+C safety, durable receipts; synthetic and target tests | R22, R35, R38, R33 | INH* | Open. | ACCEPTED |
| REV04_CONTRACT-L0295 | B07: crash-atomic Windows snapshots, previous-byte hashes, gap detection, owner final-head witness, no rollback or resume claim | R16, R38 | INH* | Open. | ACCEPTED |
| REV04_CONTRACT-L0296 | B08: full synthetic A→B→C composition with all controls, burdens, failure/abort branches, G1/G2 counterexamples, all INVALID flags, seven-case policy, PASS terminality; independent score matches pinned fixture; no pooling | R20, R32, R29 | INH* | Open. B02-A2 isolation tests belong here. | ACCEPTED |
| REV04_CONTRACT-L0297 | B09: owner decision packet (burden, T1/T2/T3, trained-owner caveat, persistent authenticator, key disposal, reboot consuming a claim, no automatic third attempt, future R1 work); no key ceremony from the draft | R21, R29 | INH* | Open. B08-R2 disclosures belong here. | ACCEPTED |
| REV04_CONTRACT-L0298 | B10: nonexecuting P03 design may proceed; any change to Research 513 probe ordering needs prospective approval; physical kernel stays a candidate, logical THIN_CENTRED_HYBRID_V03 stays selected; Specification 028, migration and authority unchanged | R21 | INH* | Programme-level boundary; it also supplies partial text for A6's non-production rule. | ACCEPTED |
| REV04_CONTRACT-L0300 | All freeze-blocking checks must be independently qualified; the draft, its policy and these bullets are not owner assent or a verified scorer | R21, R36, R37 | INH* | — | ACCEPTED |

## 3. REV04 lines outside numbered sections (excluded by extraction, audited here)

| Lines | Content | Normative? | Finding |
|---|---|---|---|
| 3, 4, 7 | Date, draft status, parents | No | METADATA |
| 5 | Scope: candidate successor qualification; no sensitive operation or experiment authorized | Restated | Covered by L0016 and L0300. |
| 6 | Provisional identities R0-P01-V01-I1, CONTRACT-V03, Attempt 002; no final identity frozen | Restated | Covered by L0020. |
| 8 | Authority: research-only; V01/V02 contracts, Attempt 001 observations and scorer rules not retroactively amended | **Yes** (no retroactive amendment) | Substantively restated by L0016 and by V02 line 14. No new unit is strictly needed; F1 could cite it as the explicit non-retroactivity rule. |
| 304–316 | Status block: RESEARCH_513_INTERPRETATION and OWNER_STOPPING_POLICY = NOT_YET_APPROVED; contract freeze and implementation not authorized | Historical | Stale relative to the B01/B02 records. R21 already provides that the approved proposal is immutable even if stale draft flags remain. Keep excluded; it must not be read as a live denial of B01/B02. |

## 4. Machine-checkable receipt

```text
BEGIN_AUDIT_RECEIPT
REV04_CONTRACT-L0266|INHERITED_UNCHANGED|R16,R27|ACCEPTED||REV04_CONTRACT-L0266
REV04_CONTRACT-L0267|INHERITED_UNCHANGED|R31,R17|ACCEPTED||REV04_CONTRACT-L0267
REV04_CONTRACT-L0268|INHERITED_UNCHANGED|R20,R32,R29|ACCEPTED||REV04_CONTRACT-L0268
REV04_CONTRACT-L0269|INHERITED_UNCHANGED|R37,R21,R19|ACCEPTED||REV04_CONTRACT-L0269
REV04_CONTRACT-L0274|INHERITED_UNCHANGED|R11,R12|ACCEPTED||REV04_CONTRACT-L0274;REV04_CONTRACT-L0156
REV04_CONTRACT-L0275|INHERITED_UNCHANGED|R13|ACCEPTED||REV04_CONTRACT-L0275
REV04_CONTRACT-L0276|INHERITED_UNCHANGED|R18,R13|ACCEPTED||REV04_CONTRACT-L0276;REV04_CONTRACT-L0287
REV04_CONTRACT-L0277|INHERITED_UNCHANGED|R17,R26,R38|ACCEPTED||REV04_CONTRACT-L0277;REV04_CONTRACT-L0215
REV04_CONTRACT-L0278|INHERITED_UNCHANGED|R16,R38|ACCEPTED||REV04_CONTRACT-L0278
REV04_CONTRACT-L0279|INHERITED_UNCHANGED|R18|ACCEPTED||REV04_CONTRACT-L0279
REV04_CONTRACT-L0280|INHERITED_UNCHANGED|R23,R22,R40,R36,R01|ACCEPTED||REV04_CONTRACT-L0280
REV04_CONTRACT-L0281|INHERITED_UNCHANGED|R07,R11,R12|ACCEPTED||REV04_CONTRACT-L0281;REV04_CONTRACT-L0151
REV04_CONTRACT-L0282|INHERITED_UNCHANGED|R15|ACCEPTED||REV04_CONTRACT-L0282
REV04_CONTRACT-L0283|INHERITED_UNCHANGED|R13,R16|ACCEPTED||REV04_CONTRACT-L0283
REV04_CONTRACT-L0287|INHERITED_UNCHANGED|R37,R21|ACCEPTED||REV04_CONTRACT-L0287
REV04_CONTRACT-L0289|INHERITED_UNCHANGED|R21,R11,R12|ACCEPTED||REV04_CONTRACT-L0289;R0_P01_B01_OWNER_ACCEPTANCE_20261010.md
REV04_CONTRACT-L0290|INHERITED_UNCHANGED|R21,R18|ACCEPTED||REV04_CONTRACT-L0290;R0_P01_B02_OWNER_ACCEPTANCE_20261010.md
REV04_CONTRACT-L0291|INHERITED_UNCHANGED|R38,R05|ACCEPTED||REV04_CONTRACT-L0291
REV04_CONTRACT-L0292|INHERITED_UNCHANGED|R14,R15,R13|ACCEPTED||REV04_CONTRACT-L0292
REV04_CONTRACT-L0293|INHERITED_UNCHANGED|R01,R23,R33,R36|ACCEPTED||REV04_CONTRACT-L0293
REV04_CONTRACT-L0294|INHERITED_UNCHANGED|R22,R35,R38,R33|ACCEPTED||REV04_CONTRACT-L0294
REV04_CONTRACT-L0295|INHERITED_UNCHANGED|R16,R38|ACCEPTED||REV04_CONTRACT-L0295
REV04_CONTRACT-L0296|INHERITED_UNCHANGED|R20,R32,R29|ACCEPTED||REV04_CONTRACT-L0296
REV04_CONTRACT-L0297|INHERITED_UNCHANGED|R21,R29|ACCEPTED||REV04_CONTRACT-L0297
REV04_CONTRACT-L0298|INHERITED_UNCHANGED|R21|ACCEPTED||REV04_CONTRACT-L0298
REV04_CONTRACT-L0300|INHERITED_UNCHANGED|R21,R36,R37|ACCEPTED||REV04_CONTRACT-L0300
END_AUDIT_RECEIPT
```

Counts: 26 rows; 26 ACCEPTED; 0 PENDING; 0 SUPERSEDED_BY_REV04; 26 INHERITED_UNCHANGED; 0 NOT_APPLICABLE_TO_SUCCESSOR.

## 5. Attestation and boundaries

- **Reviewer: claude-04** (Claude, independent clause auditor). I independently read the governing source for every unit above. I did **not** author the source inventory, the batch plan, the blind second golden-vector implementation or the independent scorer, and I will not author the latter two.
- `ACCEPT_AUDIT_BATCH009` is a reviewer disposition on source-to-requirement mapping only. It is not F1 approval and does not resolve any §11 blocker.
- Only this message file was written. No owner evidence, credential, key or WebAuthn state touched. B01/B02 accepted; Attempt 001 immutable AMEND; F1/F2 unfrozen; Attempt 002 not authorized.

```text
MC0030_MESSAGE042=CLAUDE_AUDIT_BATCH009
DISPOSITION=ACCEPT_AUDIT_BATCH009
UNITS_AUDITED=26_OF_26
ACCEPTED=26
PENDING=0
REV04_CONTRACT_COVERAGE=156_OF_156_UNITS_REVIEWED_ACROSS_BATCHES_007_008_009
CROSS_REFERENCE=CAMPAIGN_FINDINGS_MAPPED_TO_SECTION_11_BLOCKERS
F1=NOT_APPROVED
ATTEMPT_002=NOT_AUTHORIZED
```
