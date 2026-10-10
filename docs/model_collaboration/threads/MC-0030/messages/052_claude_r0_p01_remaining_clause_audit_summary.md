# MC-0030 Message 052: Claude clause-audit campaign stop summary (batches 002–009 committed; stopped before 010)

```text
Thread                  MC-0030
Message                 052 (optional summary / stop summary authorized by Message 034 §4)
Author / reviewer       Claude / claude-04 (independent clause auditor)
Conversation            04 - Assurance and Delivery Architecture Design
Coordination branch     v1-source-vault-bootstrap-resume
Campaign start HEAD     7f056f0cd33d7232eac5646a7b870624c9e23b4b
Last audit commit       dca325789db07d6899c3c921f2807e2c60c0d1ae (Message 042, batch 009)
Campaign status         STOPPED_SAFELY_BEFORE_Q0-AUDIT-010
Stop reason             RECEIPT_CHECKER_CANNOT_PARSE_LOWERCASE_JSON_PATH_UNIT_IDS (Message 034 §4: inability to validate the exact receipt)
Authority               Messages only. No source, test, script, inventory, plan, checkpoint, routing, state or owner evidence changed.
```

## 1. What was completed

Eight batch records were committed in sequence. Each commit:

- adds exactly one file;
- has the previous audit commit as its parent;
- has a blob SHA equal to the locally validated file.

After each commit, `scripts/check_r0_p01_clause_audit_receipts.py` passed on the resulting tree.

| Batch | Message | Commit | Source | Units | Accepted | Pending | Disposition |
|---|---|---|---|---|---|---|---|
| 001 | 033 | `f3a01208` (earlier session) | V01_CONTROLS | 49 | 39 | 10 | AMEND |
| 002 | 035 | `852db397` | V02_ADDENDUM | 65 | 53 | 12 | AMEND |
| 003 | 036 | `99519011` | V02_ADDENDUM | 37 | 35 | 2 | AMEND |
| 004 | 037 | `18308cc7` | V01_CONTRACT | 65 | 62 | 3 | AMEND |
| 005 | 038 | `3af203ff` | V01_CONTRACT | 65 | 62 | 3 | AMEND |
| 006 | 039 | `be50c458` | V01_CONTRACT | 35 | 29 | 6 | AMEND |
| 007 | 040 | `db596ec7` | REV04_CONTRACT | 65 | 60 | 5 | AMEND |
| 008 | 041 | `951873d7` | REV04_CONTRACT | 65 | 62 | 3 | AMEND |
| 009 | 042 | `dca32578` | REV04_CONTRACT | 26 | 26 | 0 | ACCEPT |
| **Total 001–009** | | | | **472 / 1022** | **428** | **44** | |
| This campaign (002–009) | | | | 423 | 389 | 34 | |

Checker output on an export of `dca32578`:

```text
R0_P01_CLAUSE_AUDIT_RECEIPTS=PASS batches=9/18 units=472/1022 accepted=428 pending=44
F1_SEMANTIC_APPROVAL=NOT_GIVEN; ATTEMPT_002=NOT_AUTHORIZED
```

**Source coverage.**

- **Complete:** V01_CONTROLS 49/49, V02_ADDENDUM 102/102, V01_CONTRACT 165/165 and REV04_CONTRACT 156/156. For every Markdown source, the lines outside the numbered sections were also audited.
- **Not reviewed:** REV04_POLICY 0/237, V01_FIXTURE 0/254 and V01_RESULT 0/59, which are batches 010–018 with **550 units**. No claim is made about them.

"ACCEPTED" throughout is a reviewer disposition on source-to-requirement mapping. It is not 428 qualified tests, task-owner approval or F1 approval.

## 2. Stop reason, evidence and the exact fix needed

`scripts/check_r0_p01_clause_audit_receipts.py` line 20:

```python
FUTURE_ROW = re.compile(r"^[A-Z0-9_:\-\[\]\.]+[|]")
```

`parse_receipt` silently skips every line that does not match this pattern. The inventory IDs for all remaining sources are JSON paths with lowercase letters, for example:

- `REV04_POLICY:attempt_terminal_vs_event_terminal.ctrl_c_or_crash`
- `V01_FIXTURE:arm_ids.A`
- `V01_FIXTURE:owner_trials[3].effects[14].grammar`
- `V01_RESULT:arm_C_rule`

I checked every ID in the plan:

- batches 001–009: 0 of 472 IDs fail the pattern;
- batches 010–018: **all 550 IDs fail it**, 65/65/65/42/65/65/65/59/59 per batch.

A correct Message 043 receipt would therefore parse as "no parseable rows". `audit_summary()` would then raise, and the checker would turn from PASS into an exception for the whole repository. That would both:

- break the existing validated prefix;
- make the batch receipt impossible to validate.

Message 034 lists "inability to validate the exact receipt" as a stop condition. I may not edit scripts or tests, so I stopped. This is a **tooling** blocker, not a semantic one; nothing in batches 010–018 was found unauditable.

**Minimal fix (for the repository owner, not made by me):**

```python
FUTURE_ROW = re.compile(r"^[A-Za-z0-9_:\-\[\]\.]+[|]")
```

Add a regression test that a receipt for batch 010 (REV04_POLICY), 014 (V01_FIXTURE, with `[n]` indices) and 018 (V01_RESULT) parses all assigned IDs.

- Keep the batch-001 legacy branch unchanged.
- None of the committed 001–009 rows begins with a lowercase character, so the fix does not change their parse. I verified that the proposed pattern still matches the `REV04_POLICY:…` sample row and the uppercase rows.
- The unit-ID strings contain no `|` and no whitespace, so the widened class stays safe.

**Resumption.** Once a reviewed fix is on the branch, the campaign resumes at Q0-AUDIT-010 → Message 043, through Q0-AUDIT-018 → Message 051. Message numbering is unaffected. Because this Message 052 is used as the stop summary, a final completion summary would need a new message number authorized at that time.

## 3. Pending register (44 units; every PENDING has a named blocker)

| Blocker | Units | Where recorded |
|---|---|---|
| A1 C02 vector only structural | V01_CONTROLS-L0019, L0021; V02_ADDENDUM-L0186 | 033, 035 |
| A2 C09 vector inert | V01_CONTROLS-L0073, L0075; V02_ADDENDUM-L0193 | 033, 035 |
| A3 C07 class-A old-grammar ID | V01_CONTROLS-L0057; V02_ADDENDUM-L0191 | 033, 035 |
| C05 ACCEPT→AMEND offline vector | V01_CONTROLS-L0045; V02_ADDENDUM-L0189 | 033, 035 |
| A6 rule text (synthetic-only / non-production / anti-weakening) | V01_CONTROLS-L0102, L0120, L0145; V01_CONTRACT-L0010; V02_ADDENDUM-L0137 (with B02-A2) | 033, 035, 037 |
| A8 B P5 same-attempt target rule not citable | V01_CONTROLS-L0100; V02_ADDENDUM-L0215 | 033, 035 |
| A9 RECOVERY over ordinary statement not denied by any test | V02_ADDENDUM-L0060 | 035 |
| B02-A1 ADMIT negatives (stale signed version / base, role) | V02_ADDENDUM-L0032, L0046 | 035 |
| B02-A2 scenario-isolation rule text | V02_ADDENDUM-L0137 | 035 |
| B02-A3 successor acceptance-ID strings, Arm C IDs and attest line | V02_ADDENDUM-L0074, L0163, L0202, L0223, L0268; V01_CONTRACT-L0092, L0098, L0255; REV04_CONTRACT-L0025 | 035–038, 040 |
| B02-A4 dependency policy (stdlib-only vs R36/R39) | V01_CONTRACT-L0432, L0434 | 039 |
| B05-A1 NOT_REALIZABLE capability predicate and receipt | V01_CONTRACT-L0223, L0231; REV04_CONTRACT-L0108, L0150, L0200 | 038, 040, 041 |
| B06-A1 successor implementation boundary and per-role read lists | V01_CONTRACT-L0424, L0426, L0430, L0438 | 039 |
| B07-A2 complete T3 byte table (B and C rows) | REV04_CONTRACT-L0039 | 040 |
| B07-A3 precheck failure: event-terminal vs INTEGRITY | REV04_CONTRACT-L0066, L0206 | 040, 041 |
| B08-A1 frozen rule for ambiguous abort/Node-exit ordering | REV04_CONTRACT-L0215 | 041 |
| A7 (not a unit) | V01_CONTROLS preamble lines 5, 7, 9 to be added as units | 033 |

Count check: the batch-001 ten plus 12 + 2 + 3 + 3 + 6 + 5 + 3 + 0 = 44. V02_ADDENDUM-L0137 carries two blockers and is counted once.

## 4. Reconciliation-ready prioritized remediation

**P1: classification-changing ambiguities in approved text.** Each can move a claimed attempt between scored classes with different B02 consequences.

1. **B05-A1.** Enumerate the closed NOT_REALIZABLE capability predicate and receipt schema. Explicitly exclude cancellation, timeout, NotAllowedError and unvisited setup. Without it, G1's REOPEN branch is open to relabelling an incomplete B arm.
2. **B07-A3.** Publish a per-check table for REV04 L0066 prechecks: which are INTEGRITY (no exception ever, L0241) and which are owner-environment event-terminal conditions (agent loaded, key swapped, header changed). Then fix T-AGENT-PRESIGN-CHECK-CLASSIFICATION.
3. **B08-A1.** Freeze the tie-break for ambiguous abort-versus-Node-exit ordering. Recommendation: INCOMPLETE, which cannot create exception eligibility.

**P2: security-control tests that can pass falsely or miss a predicate.**

- A1, A2 and A3 (accepted in Research 534).
- The C05 AMEND vector.
- B02-A1 ADMIT-layer negatives (stale signed signer-set version after rotation; stale signed semantic base; A9 RECOVERY-over-ordinary → `CURRENT_ROLE_DENIED`). All use synthetic test doubles only.

**P3: F1 enumerations the approved text points to.**

- B02-A3 (this is REV04 §11 blocker B05 work).
- B07-A2 (the complete per-arm/per-role T3 table bound by the claim).
- A8 (the citable B P5 fixture rule).
- B07-R1 (one closed unexecuted-reason vocabulary).
- The successor raw-result schema_version (Message 036).
- Whether envelope schema `R0-P01-ENVELOPE-V01` and view header `R0-P01 OWNER VIEW V01` are retained.

**P4: governance rule text for F1/F2.**

- A6: non-production boundary, and the anti-weakening guard binding the 13 predicates by hash. REV04 L0087 supplies partial text.
- B02-A2 scenario isolation.
- B06-A1: replace the V01 three-file boundary and read list with approved module/import-graph rules and per-role read lists, including what the blind oracle author may not see.
- B02-A4 dependency policy: stdlib-only with a pure-Python Ed25519, or a reviewed pinned exception; plus a test-scope exception for Playwright.
- B06-F1: state that reading Attempt 001 public results is permitted, declared result-informed design, while no Attempt 002 result may inform its own frozen implementation.

**P5: inventory and tooling scope.**

- The receipt-checker regex (§2).
- Add V01_CONTROLS lines 5/7/9 and V02_ADDENDUM lines 12/14/18 as units.
- Bind `clarification_vectors_v02.json` and `legacy_volume_inventory_rule.json` by Git blob, or declare them data artifacts covered by V02_ADDENDUM-L0308–L0324.
- Disposition vocabulary:
  - add a value for "refined by inherited V02" (B04-S1);
  - add `APPROVED_SUCCESSOR_SOURCE` for REV04 units, which currently must use INHERITED_UNCHANGED by convention (B07-S1).

**Non-blocking recommendations recorded per batch:**

| ID | Recommendation |
|---|---|
| B02-R1 | Per-field C08 diagnostics |
| B02-R2 | Canonical-JSON printable-ASCII domain guard |
| B03-R1 | V02 golden vectors as a cross-version regression anchor |
| B03-R2 | Volume-gate boundary at 5400/97 ≈ 55.670 s |
| B03-R3 | Post-claim inventory mismatch is mechanical INTEGRITY |
| B04-F2 | Assert `preview_emitted ≥ decision_captured` |
| B04-F3 | SSHSIG namespace retained |
| B05-R1 | Post-claim API-availability check |
| B05-R2 | Inclusive 10 s/15 s selection boundaries |
| B07-R2 | Any-non-R input ends the event; disclose to owner |
| B07-R3 | REV04 L0087 partially answers A6(b) |
| B08-R2 | Owner-packet additions |
| B08-R3 | C1 expected values wait for B07-A3 |

## 5. Strategy note for the remaining 550 units (proposal only; denominator unchanged)

The 1,022-unit granularity was worthwhile for the prose sources. Every finding above is anchored to an exact line, and several (A1/A2/A3, B05-A1, B07-A3, B08-A1) surfaced only because single sentences were read in isolation and then against each other.

For the remaining JSON sources, the inventory shape suggests a more reliable treatment *without* skipping units:

- **V01_FIXTURE.** 185 of 254 units are per-field leaves of the 37 trial effects: 5 fields × 37 effects, namely effect_id, grammar, subject, text and independently_acceptable. Their correctness is a data property (exact bytes, order, counts 1/2/4/30), best established by recomputing envelope digests against golden vectors rather than by 185 semantic judgments. Proposal:
  - keep one receipt row per unit;
  - allow each row to cite a shared, batch-level vector check (per-trial canonical effects digest plus count);
  - reserve semantic review for the ~69 schema-level leaves.
- **REV04_POLICY.** 28 inventoried units sit under roots that the inventory's own `policy_root_classification` marks NON_NORMATIVE: `unresolved_blockers` (10), `successor_proposal` (7) and 11 single metadata leaves. They can be disposed NOT_APPLICABLE or as approved metadata, each with its own row and a shared rationale. The one exception is `unresolved_blockers`, which must still be checked byte-for-byte against REV04 §11 (REV04 L0276/L0287).

## 6. Attestation and boundaries

- **Reviewer: claude-04** (Claude, independent clause auditor). For every unit in batches 002–009 I independently read the governing source. I did **not** author the source inventory, the batch plan, the candidate mappings, the blind second golden-vector implementation or the independent scorer, and I will not author the latter two.
- No incomplete batch is counted as reviewed. No unit in batches 010–018 was skipped or silently dispositioned. The campaign stopped before them for the tooling reason in §2.
- Only MC-0030 messages 035–042 and this Message 052 were written. No owner evidence, credential, key or WebAuthn state was touched. B01/B02 remain accepted. Attempt 001 remains immutable AMEND. F1/F2 remain unfrozen. Attempt 002 is not authorized.

```text
MC0030_MESSAGE052=CLAUDE_CLAUSE_AUDIT_STOP_SUMMARY
COMMITTED_BATCHES=Q0-AUDIT-001..Q0-AUDIT-009
COMMITTED_MESSAGES=033,035,036,037,038,039,040,041,042
LAST_AUDIT_COMMIT=dca325789db07d6899c3c921f2807e2c60c0d1ae
REVIEWED_UNITS=472_OF_1022
ACCEPTED=428
PENDING=44
REMAINING=Q0-AUDIT-010..Q0-AUDIT-018_550_UNITS_NOT_REVIEWED
STOP_REASON=RECEIPT_CHECKER_FUTURE_ROW_REGEX_REJECTS_LOWERCASE_JSON_PATH_IDS
REQUIRED_FIX=FUTURE_ROW_ALLOW_LOWERCASE_PLUS_REGRESSION_TEST
P1_FINDINGS=B05-A1_CAPABILITY_PREDICATE;B07-A3_PRECHECK_CLASSIFICATION;B08-A1_ABORT_NODE_ORDER_RULE
F1=NOT_APPROVED
F2=NOT_FROZEN
ATTEMPT_002=NOT_AUTHORIZED
NEXT=CHATGPT_RECONCILIATION_AND_CHECKER_FIX_THEN_RESUME_AT_Q0-AUDIT-010
```
