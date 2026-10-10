# Research 531: R0-P01 successor Q0 source trace and Q1 exact-freeze architecture candidate

**Date:** 2026-10-10
**Status:** Q0 STATIC SOURCE TRACE QUALIFIED / Q1 DESIGN UNFROZEN / INDEPENDENT REVIEW NEXT
**Scope:** Convert the separately owner-approved Research 513/V03 REV04 P01 successor obligations into a reproducible requirements-to-test trace, and prepare an implementation-neutral Q1 exact-freeze boundary proposal for independent critique.
**Parent:** Research 530 / Checkpoint 866 / explicit B01-B02 owner approval receipts / Research 513 and frozen V02
**Validation:** Validation 220, Q0 static trace and mutation tests only
**Collaboration:** MC-0030 Message 028
**Authority:** Non-secret research, traceability, test harness of source hashes and unfrozen implementation design only; no new owner attempt, private credentials, exact fixture freeze, physical architecture selection, production implementation or authority switch.

## 1. Sources actually inspected

The active branch was read as `v1-source-vault-bootstrap-resume`, base and published HEAD `323acf5238a344c4f27d3eded36ecd558efa135d`. The old frozen fixture, result contract, 13-control security specification, V02 audit/addendum, original harness/scorer/Node code, Research 513 and approved REV04 draft/policy and B01/B02 receipts were consulted **read-only**. The original owner's private-key directories and raw Attempt 001 proof contents were not inspected.

The original fixture was independently checked to have 13 unique control names and S01/S02/S03/L01 effects 1/2/4/30. The frozen projected volume is 97 acceptances and 157 effects with effect-count distribution 62 one, 17 two, 11 three, 7 four. Its result contract retains 60-second median small, 120-second per-small and per-large limits, and its proof-viability predicate uses controls 1–10. The exact frozen old source file hashes were recorded in Q0 to detect inadvertent drift.

Approved source bytes were recomputed:

| Accepted source | SHA-256 exact bytes |
|---|---|
| V03 REV04 successor contract | `9160a30c481c1c67c2ec857238f5a04b44f618b2ef589ef4f1c514eb3b3d6175` |
| Finite REV04 stopping policy | `9b5bbc4d2c4802fc80b46bcaa3d003640c33e8e4784d39ef7995dbf193dff86c` |

The accepted draft JSON still contains predecision status fields. The separately published B01/B02 human acceptance records, not an in-place mutation to source, authorize prospective qualification design.

## 2. Concrete artifacts and results

1. `docs/research/r0_p01_successor_design/R0_P01_Q0_REQUIREMENTS_TRACE_UNFROZEN.json`: **34 requirements**, 13 individually indexed controls C01–C13, original trial corpus sizes, seven read-only V02 source SHA-256 identities, approved REV04 hashes, source-reference aliases, evidence obligations and 64 unique **future** synthetic test IDs. Each requirement remains `QUALIFICATION_REQUIRED`; none is claimed implemented.
2. `scripts/check_r0_p01_successor_trace.py`: read-only pure Python guard that compares trace IDs/control names/trial sizes/inventory/timing limits/approval receipts and exact source-byte hashes. It does not import old harness/score, read owner proof or execute any key operation. Its source may be redesigned if better justified; it is not a scored experiment.
3. `tests/unit/test_r0_p01_successor_trace_guard.py`: ten unit tests, including negative mutations to requirements, control names, timing, volume, human approval and lifecycle claims, plus duplicate-key JSON rejection. All ten passed under an isolated writable pytest base directory. First read-only run could not initialize pytest's tempfile; a second run with the authorized writable profile reached nine passing tests and one tempfile permission error; the final isolated-base run passed all ten. These infrastructure errors are **not** hidden, and no scored P01 result was involved.
4. `docs/research/r0_p01_successor_design/R0_P01_Q1_IMPLEMENTATION_BOUNDARY_CANDIDATE.md`: a **nonbinding**, complete component and exact-freeze design proposal, comparing compact and ports/adapters decompositions with provisional technical preference for testable separate pure semantics, platform adapters, evidence and independent scorer.

The Q0 manifest exact SHA-256 is `5f3f079e6e1f0c0ca0f36b986a4b7f9c2e56ae85ff179aaac1fbb5f76345d15f`. Its status is UNFROZEN. All 64 named synthetic test IDs are future work obligations, **not 64 tests passed**.

## 3. Why source traceability is not implementation qualification

The guard compares authority/evidence **inputs**, not the behavior of a new signer, RP, browser, event scheduler, immutable snapshot writer or scorer. A passing synthetic/fixture hash test alone cannot show cryptographic verification or prove that an owner saw what was signed. Independently authored expected outputs and actual synthetic crypto/Node/Windows full runs are required.

The original V02 code is allowed as a *reference to inspect*, but its hardcoded Attempt 001 identifiers, Boolean crypto failure conflation, generic exception-to-integrity handling, fragile process interruption and single native SSH unlock are known to require prospective changes. No historical source was modified or imported as a success oracle.

## 4. Open Q1 choices before a freeze

The proposed Q1 split is deliberately revisable at any level. A small coordinator plus isolated verification modules is simpler; a more modular pure-canonical-state / owner-run / native-SSH / WebAuthn-RP / evidence-writer / independent-scorer decomposition exposes the isolation needed to test exact statement bytes, errors and interrupted state. Neither is preselected. The independent reviewer must challenge unnecessary services, duplicated semantics, shared-oracle risks and implementation burdens.

A future fixture must freeze exact statement, rendered bytes, T3, synthetic key-template slots and P5/P6 expected effects, replay/negative cases, role/compromise history, per-arm terminal-state predicates, all 13 control outputs, Windows lifecycle/atomic evidence behavior and B02 policy plus human acceptance source hashes. The tests must be reproducible and qualified before any real credential action. Virtual CTAP2 is a test double for the crypto verifier path, not live Windows Hello usability. Synthetic role receipts for C are not real human user-role provenance.

Key open technical risks remain target-Windows atomic no-overwrite writes and fsync, correct Node RP receipt preservation during Ctrl+C, unambiguous error-site mapping for a future implementation, independent oracle separation, and the feasibility of a complete synthetic A/B/C run without false owner-UX claims. A later block must be recorded as a blocker, not a silent eligibility adjustment.

## 5. Next justified action

Request one bounded **independent Claude critique of Q0 trace and Q1 design** through MC-0030 Message 028, with authority to write its own message 029 only. If accepted, determine the implementation decomposition based on reasons and begin authoring the **actual exact prospective fixture/oracle expected vectors**, followed by synthetic implementation and independent qualification. A Q1 design review cannot itself freeze owner-facing code or authorize an Attempt 002 claim.

Historical Attempt 001 remains AMEND, R0-P02 PASS, R0-P03 pending, physical target unselected, Specification 028 and related authority state unchanged. The specific third human execution approval remains mandatory in the future.

```text
RESEARCH_531=Q0_TRACE_QUALIFIED_Q1_UNFROZEN
Q0_REQUIREMENTS=34
Q0_GUARD_UNIT_TESTS=10_PASS
Q1_ARCHITECTURE=PROVISIONAL_NOT_SELECTED
EXACT_FIXTURE_FREEZE=NOT_YET
REAL_OWNER_ATTEMPT_002=NOT_AUTHORIZED
NEXT=MC0030_INDEPENDENT_Q0_Q1_CRITIQUE
```
