# Research 532: Claude Message 029 reconciliation, Q0 REV02 and F1/F2 boundaries

**Date:** 2026-10-10
**Status:** CLAUDE Q-1/Q-2/Q-4 BLOCKERS ACCEPTED / PROSPECTIVE DESIGN AMENDED / SEMANTIC REVIEW NEXT
**Scope:** Reconcile Message 029 against frozen P01-C07, the approved V03 REV04 inputs and the new Q0/Q1 design, without modifying approved contract bytes or claiming a new fixture freeze.
**Parent:** Research 531 / Validation 220 / Checkpoint 867 / MC-0030 Message 029 / Research 513 / human B01/B02 acceptance
**Validation:** Validation 221, static design and 17 tests only
**Collaboration:** MC-0030 Message 030
**Authority:** Nonsecret design correction and future qualification planning only. No F1/F2 freeze, new owner trial, real credential, physical candidate selection or Specification 028 amendment.

## Finding dispositions

**Q-1 ACCEPT:** The 34-row Q0 trace was not source-exhaustive. New independent deterministic clause extractor inventories 166 contract text units in sections 1–11 and 185 normative JSON policy leaves. New Q0 REV02 adds nineteen requirement rows, 53 total, control-key position binding, 105 planned test catalogue entries with named layers/oracle-source/forbidden shared modules, and a read-only source-unit guard. The guard now hashes committed Git blobs to avoid CRLF transformations and checks a public SHA-256 known answer. It rejects missing normative units, orphan rows, changed source clause hashes and mismatched test catalogue. **The associations have NOT been independently reviewed.** Twenty-two section-only weak associations are explicitly flagged; no semantic-coverage approval is claimed.

**Q-2 ACCEPT:** Independent oracle is now an explicit contract, not only a principle: two separately authored canonical/renderer implementations must produce byte-identical golden vectors; the scorer must be isolated from core, owner-run and RP imports and independently parse/verify SSHSIG Ed25519 *in-process*, independent of the owner harness's native ssh-keygen path, and verify WebAuthn ES256 without importing RP code. CI must check import graph and fault vectors after actual sources exist. The first **candidate, not frozen** B01 decision predicate table is independently specified as data before any successor scorer implementation: 288 finite combinations. This does not yet encode every numeric arm timing tie-break, source-flag provenance or B02 exception case; reviewers must refine it before F1.

**Q-4 ACCEPT:** F1 freeze, **before scorer/owner-run implementation**, binds exact canonical fixture, P0/P5/P6 public-template synthetic golden vectors, separately adjudicated dual-implementation oracle outputs, complete normative index, test catalogue, 13 controls, B01/B02/selection/volume decision tables, flag schema, error categories and approved source/receipt hashes. F2 freeze, **after** full synthetic qualification but before a real owner claim, binds F1, implementation/scorer source, complete program-derived exception-site map, pinned runtime versions, two-stream Windows crash/RP evidence and full A/B/C independent test reports. Attempt 002 would eventually bind F2 and additionally requires a third express human start authorization.

**Q-3 CONFIRMED:** Frozen V02 P01-C07 has B rotation V2 PRIMARY=Arm A PRIMARY and RECOVERY=Arm A RECOVERY. Therefore B's P5 is impossible without both same-attempt A public members and receives FAIL/UNEXECUTED_ROTATION_TARGET_ABSENT. This is analogous to approved P6 failure on absent same-attempt A RECOVERY. A scorer must reconstruct rotation/recovery effect/statement from registered public key identities and reject swapped member roles/cross-arm replay. This prospective clarification leaves B01/B02 unchanged.

**Q-5 ACCEPT FOR FUTURE QUALIFICATION:** Proposed two independent hash-linked evidence streams, RP and harness, with one writer per stream and a harness snapshot binding last durable RP head. The scorer must reconcile both and a nonsecret final witness should cover both. **Implementation and Windows durability are not qualified yet.**

**Q-6/Q-7/Q-8/Q-9 ACCEPT AS TEST OBLIGATIONS:** Synthetic Windows ConPTY and native process groups, target-machine synthetic conformance, write-through/no-overwrite snapshot promotion, virtual CTAP2 UV/foreign credential/nonpresence negatives, Arm C test-double isolation, deterministic cross-OS scorer bytes, hash-pinned offline dependencies, secret/transcript scan. No current passing result is claimed for these planned tests.

## Actual delivered bounded evidence

The Q0 REV02 source index records 351 proposed mapped clauses. The guard passes against committed approved blobs and seven historical baseline artifacts. The 17 in-memory unit tests PASS under isolated allowed temporary-directory profile, including seven new deliberate faults to clause coverage, catalogue, controls, unapproved freeze metadata and blob-based hashing. The 288-row B01 classification candidate has six feasible per-arm evidence/viability/eligibility triplets, flags and volume, with structurally unique cases and hand-selected scenario assertions. This is **not** a complete independently verified scoring oracle.

Trace source hashes, source/approval status and original V02 files remain identical; original Attempt 001 remains permanent AMEND. No private key, owner evidence or real marker was opened, generated, modified or scored.

## Next review gate and limits

Message 030 requests a targeted independent technical recheck of the new extraction/guard, 22 weak semantic mappings, missing normative spans, the separate frozen F1/F2 obligations, P5 dependency correctness and soundness/exhaustiveness of the proposed 288-row decision basis. The reviewer may demand source-specific mapping corrections, more independent vector work or further separation of implementation surfaces. No new physical or Research 513 family architecture discussion is required merely for these findings.

We must not freeze F1 until (a) every mapping is independently qualified as substantively faithful, (b) dual vector oracles actually exist/agree, (c) the complete numeric/flag/B02 decision oracle is independently reviewed, and (d) exact fixture and error category grammar are qualified. F2 and the third human owner authorization come still later.

```text
RESEARCH_532=Q0_REV02_AND_F1_F2_DESIGN_RECONCILED
Q0_REQUIREMENTS=53
CLAUSE_UNITS=351
CLAUSE_WEAK_MAPPINGS=22
TEST_OBLIGATIONS=105_NOT_IMPLEMENTED
UNIT_TESTS=17_PASS
F1_TABLE=288_CASES_UNFROZEN
F1=NOT_FROZEN
F2=NOT_FROZEN
ATTEMPT_002=NOT_AUTHORIZED
NEXT=INDEPENDENT_Q0_REV02_F1_DESIGN_RECHECK
```
