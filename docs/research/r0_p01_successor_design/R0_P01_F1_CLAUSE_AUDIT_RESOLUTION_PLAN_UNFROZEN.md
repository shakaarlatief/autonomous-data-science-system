# R0-P01 F1 substantive audit and oracle gap closure plan (unfrozen)

**Date:** 2026-10-10
**Status:** POST-MESSAGE-031 REMEDIATION PROPOSAL / CLAUSE AUDIT NOT COMPLETE
**Scope:** Accept Claude Message 031 F-1 to F-7 at the design level, establish individually reviewable inherited normative-source units, isolate scorer/golden roles, and define the additional oracle and evidence reviews still required before any F1 freeze.
**Parent:** MC-0030 Message 031 / Research 532 / Checkpoint 868 / Research 513 / B01/B02 owner approvals
**Authority:** Nonsecret audit-planning and candidate source/test/oracle artifacts only. No F1/F2 freeze, real P01 claim, owner keys, WebAuthn ceremony, production selection or authority switch.

## 1. Source governance and current limits

Claude Message 031 returned AMEND_REV02_Q0_TARGETED. His independent 288/288 B01 table recomputation confirms the first predicate-layer expected classes/reasons but **not** control-to-viability derivation, numeric selected-arm volume, B02 exception permission or mapping completeness. The previous 22 flagged section-only mappings are not the complete defect count; the other 22 unflagged wrong mappings and missing inherited source clauses must be treated as open.

New extractor: `scripts/r0_p01_audit_inventory_rev03.py`. It inventories the immutable approved REV04 contract/policy and inherited V02 addendum, security-control definitions, V01 implementation contract, fixture and result schema by exact Git-blob SHA-256. The generated `R0_P01_F1_NORMATIVE_AUDIT_INVENTORY_REV03_UNFROZEN.json` contains **1,022 individually identified source units** spanning all seven listed surfaces, including 23 labelled normative policy roots and 13 policy metadata/optional roots requiring explicit non-normative justification. Seven Markdown table headers and seven separator rows are preserved as syntax/context, **not** as normative duties. Another 38 excluded nonblank preamble/out-of-scope lines are explicitly reported for reviewer disposition; the extractor must not silently discard them if any is governing.

No per-unit requirement assignment is accepted automatically. Inherited security-control sections 1–13 carry *unreviewed* suggested C01–C13 anchors. REV04 units may retain historical REV02 hints, labelled unreviewed. Each original inherited unit requires an independent disposition: INHERITED_UNCHANGED (exact C/R targets), SUPERSEDED_BY_REV04 (exact successor unit and reason), or NOT_APPLICABLE_TO_SUCCESSOR (explanation). A unit may cite multiple requirements. No automatic section-default mappings gain reviewer authority. Review-derived R34–R40 engineering requirements are tagged REVIEW_DERIVED_ENGINEERING, with Claude Message 029 as provenance, rather than forced to unrelated REV04 paragraphs. Prior prose-only R22–R40 will require final measurable acceptance conditions and independent expected oracles.

## 2. Bounded audit work and separation of duties

The exact source-unit list is partitioned into 18 non-overlapping audit batches of at most 65 units. `R0_P01_F1_NORMATIVE_AUDIT_BATCH_PLAN_REV03_UNFROZEN.json` binds each batch's ordered unit IDs by SHA-256 and identifies Claude / claude-04 as independent source-to-requirement auditor. Start with **Q0-AUDIT-001: 49 V01 security-control contract units**. This establishes substantive definitions for C01–C13 before judging the inherited addendum and downstream REV04 cross-references. Subsequent batches cover V02 addendum, V01 implementation, REV04 contract/policy and V01 fixture/result leaves.

Each audit receipt must specify each exact unit ID, reviewed requirement key(s), inherited disposition, reviewer identity and message/commit, all corrections, and a reason for any superseded or not-applicable unit. Flag textual passages that require splitting to avoid hiding several obligations under one broad requirement. Reviewers must explicitly decide whether the 38 excluded out-of-scope lines are normative. A completed batch alone cannot change F1 from UNFROZEN; all batches, cross-source supersession resolution, control completeness, exact oracle and test catalogue must converge and pass an independent summary review.

**Independence assignment:** Claude performs the clause audit and **must not** also author the blind second canonical/golden-vector implementation. The principal implementation and oracle will later be developed by distinct task actors or segregated tool sessions with a recorded information-exposure/role-blindness attestation. The oracle author receives *only* the reviewed F1 specification, not principal implementation code or its generated outputs before oracle submission. The future independent scorer also must not import harness/core/RP implementation modules; static import-graph enforcement and in-process SSHSIG/Ed25519 and WebAuthn verification negatives remain mandatory. These are unresolved F1/F2 prerequisites, not claims that a blind oracle already exists.

## 3. Test contract after Claude F-3

A separately versioned `R0_P01_F1_TEST_CATALOGUE_REV03_UNFROZEN.json` includes **117 planned test identifiers**, covering 105 earlier IDs plus native-prompt visibility, RP-tail-after-crash, pre-sign check precedence, and numeric/B02 boundary cases. It exposes `expected_value_origin` and `must_not_derive_from` separately, corrects obvious native/virtual/integrated test layers, includes two OWNER_MACHINE_MANUAL test cases, and requires exact future expected vector/decision identifiers.

**The revised catalogue is a candidate schema, not a corrected F1-final test contract:** expected origins are explicitly REVIEW_PENDING, exact vectors unassigned, and no tests are claimed implemented. Independent auditors must approve every layer and expectation isolation rather than replacing one global placeholder with another.

## 4. B01 selection-volume coupling and F4 candidate oracle

The frozen result contract selects the faster arm only when the small median delta is at least 10 seconds, otherwise uses a 15-second large-trial delta, otherwise chooses B. The selected arm is then subjected to the original projected volume limit. With 97 fixed acceptances and 90 projected owner minutes, the **exact** selected median ceiling is 5400/97 seconds, approximately 55.6701, strictly below the independent 60-second eligibility ceiling.

For example, eligible A with median 54 s and L01 70 s, and eligible B with median 58 s and L01 72 s, produces **B selection** under both frozen tie thresholds but 97 × 58 / 60 = 93.766... projected minutes and thus AMEND. Selecting A instead to rescue PASS would be posthoc optimization and is prohibited.

`R0_P01_F1_NUMERIC_AND_B02_ORACLE_SEEDS_UNFROZEN.json` contains seven selection/volume boundary seeds, twelve viability/eligibility seeds (including exact median 60 and small/large 120 limits and qualified infrastructure receipt), and twelve B02 stopping-policy seeds (including four-of-five conditions denied, cap, integrity and post-PASS denial). These are **31 incomplete reviewable oracle seeds**, not all feasible combinations nor a frozen oracle. The first previously authored 288-row predicate table is retained and independently checked by Claude but likewise UNFROZEN. Full field-level viability, numeric IEEE-754/canonical time serialization, every security/negative state and complete B02 authorization transitions must be independently derived before F1.

A future owner-facing authorization packet must explain that the 90-minute projection imposes the tighter ~55.7-second median requirement on the *selected* arm. It does not change the existing hard gate.

## 5. F-6 RP tail and F-7 pre-sign ambiguity proposals

**RP tail after crash (provisional):** The RP writes/flushes a linked receipt before acknowledging a ceremony. A crash can therefore leave valid RP receipts beyond the last RP head referenced by the harness. These are NOT automatically a chain break. An RP head claimed by the harness but missing from the RP chain **is** integrity evidence. If independently validated RP tail receipts extend beyond the harness's last recorded head, classify them by a future exact, source-verified scoring rule; when a matching final owner witness exists they can be independently corroborated, and when witness is absent disclose the unwitnessed tail without redefining the owner-required missing-witness flag as an integrity breach. A future independent scorer must decide whether the receipt sufficiently proves event-terminal status rather than assuming unacknowledged success. Test T-RP-TAIL-AFTER-CRASH must include both valid tail and contradictory missing bound head.

**Pre-sign check collision (provisional):** REV04 §4.1's `terminal` describes that no further invocation is allowed on a failed precondition within the event. REV04 §8.6's more specific structural-integrity classification is **not** negated. A positively evidenced key/public member/role/agent substitution, changed canonical statement or trust-root mismatch that violates the frozen identity invariant stops the event **and** sets the appropriate integrity source flag. By contrast, native tool unavailability, missing runtime executable or infrastructure interruption without an independently recorded identity breach is instrument/preclaim failure rather than generic integrity. An uncaptured malformed owner input is a re-prompt. Both branch and evidence receipts must be frozen at F1; actual implementation source-site inventory is frozen only at F2. Test T-AGENT-PRESIGN-CHECK-CLASSIFICATION must prevent treating every exit code or missing signature as a proven identity compromise.

Neither proposal rewrites the approved B01/B02 files. If detailed clause audit discovers a genuine contradiction with the owner-approved interpretation or original Research 513 hard gates, stop and seek governed prospective reconciliation rather than silently repairing those bytes.

## 6. Structural validation and remaining gates

The read-only `scripts/check_r0_p01_f1_audit_rev03.py` checks source SHA-256, exact 1,022-unit identity, inherited C01–C13 definitions, 18 disjoint batch hashes, 117 test catalogue keys/layers, and rational volume seeds. Twelve in-memory fault-injection tests PASS, including omitted V01 definitions, excluded policy roots, invalid manual/native test classifications, missing review identity, bad batch coverage and altered projected-volume calculation.

This establishes **structural audit readiness only**. F1 can be proposed for freeze *only after* independent completion of all semantic dispositions, reviewed test/oracle independence, dual-implementation byte agreement and complete F4 numeric/B02 expected results. F2 needs implementation source, exhaustive exception-site map, pinned dependencies and actual native Windows/Node/WebAuthn synthetic receipts. The third distinct explicit owner authorization for real Attempt 002 remains absent.

```text
CLAUDE_MESSAGE031=AMEND_REV02_Q0_TARGETED_RECONCILED_AT_DESIGN_LEVEL
F1_AUDIT_UNITS=1022
INDEPENDENT_AUDIT_BATCHES=18
F1_TEST_IDS=117_PLANNED
F4_ORACLE_SEEDS=31_UNFROZEN
F1=NOT_FROZEN
F2=NOT_FROZEN
ATTEMPT_002=NOT_AUTHORIZED
NEXT=CLAUDE_Q0_AUDIT_BATCH_001
```
