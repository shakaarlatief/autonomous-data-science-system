# Research 537: R0-P01 source-bound F1 scoring-boundary reconciliation candidates REV01

**Date:** 2026-10-11
**Status:** UNFROZEN PROSPECTIVE CROSS-SOURCE SCENARIO MATRIX / INDEPENDENT CHALLENGE REQUIRED
**Parent:** Research 536 / Validation 225 / Checkpoint 872 / MC-0030 Message 053
**Scope:** Begin *substantive* technical reconciliation of reviewer scoring findings B05-A1, B07-A3, B08-A1, B11-A1 without choosing an unapproved policy interpretation or writing a scorer.
**Authority:** Public, nonsecret research, source-sensitive synthetic test planning and reviewer collaboration only; no owner proof, Attempt 002, F1/F2 freeze, B01/B02 amendment or physical architecture decision.

## 1. Exact governing source and authority

Human acceptance of B01 and B02 was separately recorded on 2026-10-10, binding the *actual* committed REV04 contract bytes (SHA-256 `9160a30c481c1c67c2ec857238f5a04b44f618b2ef589ef4f1c514eb3b3d6175`) and exact REV04 policy bytes (SHA-256 `9b5bbc4d2c4802fc80b46bcaa3d003640c33e8e4784d39ef7995dbf193dff86c`). The historical `not approved` fields embedded in those preapproval drafts have no power to revert the later human B01/B02 receipts; preserve the source bytes and model the later approval separately.

The independent 18-batch clause audit covers 1,022/1,022 source IDs. Claude's reviewer-level outcomes are 967 ACCEPTED, 55 PENDING. Research 536 and `R0_P01_F1_PENDING_AUDIT_RECONCILIATION_REV01_UNFROZEN.json` preserve all 55 row-level open findings. **No source-level reviewer acceptance implies a passing runtime security test, frozen scorer vector or task-owner semantic approval.**

The machine-readable companion `docs/research/r0_p01_successor_design/R0_P01_F1_SCORING_BOUNDARY_CANDIDATES_REV01_UNFROZEN.json` contains **17 source-bound scenario candidates** across 4 families: **12 SOURCE_DETERMINED** (the specified narrow behavior follows the approved text under stated trustworthy preconditions) and **5 CANDIDATE_BLOCKED** (a critical predicate, event order, terminology or evidence rule is not yet approved). This is a **review matrix**, not a model implementing an owner's live scored result and not an expected-output oracle. It is guarded by `scripts/check_r0_p01_scoring_boundary_candidates.py`, which checks actual original source hashes and exact normatively indexed unit references. The structural checker cannot decide semantic correctness. Ranges, incomplete or source-hash-mismatched data must fail closed.

## 2. B05-A1: frozen capability evidence before NOT_REALIZABLE

**Already governed:** REV04 §7 and §8.4 (L0108, L0146–L0156), policy `evidence_state.not_realizable`, `evidence_state.completed` and `webauthn_assertion_failure_table`. Owner refusal, registration not reached, and cancelled/timeout WebAuthn assertion are **not** evidence that WebAuthn is unrealizable. A genuinely consumed same-attempt assertion whose RP receipt proves NotAllowedError/timeout is an event-terminal **no-proof** observation, not a legitimate owner signature. `COMPLETED` requires all P0/S01/S02/S03 unique terminal event receipts, whereas `NOT_REALIZABLE` demands genuine capability evidence.

**Unresolved:** The approved contract has *not* frozen the closed capability predicate, contemporaneous source/actor/binding of independent evidence, capability scope (registration versus assertion), causality or what to do with assertion-time NotSupportedError **after** successful registration. It is unsafe to infer `NOT_REALIZABLE` from a single DOMException name, then trigger G1 REOPEN instead of INVALID_INCOMPLETE or an evidenced instrument fault. Scenarios S1-04 and S1-05 remain blocked even though S1-01..03 articulate known necessary conditions.

**Required F1 adjudication:** Define an independently producible and replayable evidence receipt with source identity, browser/OS/credential-operation scope, timestamp domain, challenge/attempt ID if applicable, trusted platform capability probe protocol and counterexample tests for refusal/timeout/cancel/not-visited/expired/no receipt. Explicitly determine whether an assertion-time NotSupportedError following known registration is a genuinely unsupported capability, a temporary instrument failure, or unresolved evidence. Freeze a negative table that cannot grant a favorable B02 exception from missing receipts. If any treatment substantively broadens G1/B02 meanings, obtain fresh **targeted human policy interpretation approval**, distinct from later Attempt 002 execution consent.

## 3. B07-A3: SSH pre-signing check versus verified attempt integrity

**Already governed:** REV04 L0066 lists all pre-invocation controls, L0203 distinguishes missing runtime/tool, L0206 defines independently evidenced identity, key/header/agent/fixture violations as `INTEGRITY`, L0164–L0165 establish integrity precedence, and L0151–L0154 strictly define completed proof-event receipts. A proven postclaim public-key substitution/header alteration violates trusted identity, **not** a harmless event stop. Conversely, an unavailable OpenSSH executable with an independently intact evidence chain is a technical instrument failure, not falsified owner behavior. Preclaim KAT failure makes **no** claim.

**Unresolved:** The text at L0066 says that *any* pre-sign check failure is "terminal" without distinguishing a terminal **proof event**, a terminal **attempt integrity breach** or an **instrument abort**. The closed `evidence_state.terminal_outcomes` has no generic pre-sign check failure outcome. A blanket answer either way could change exception eligibility. A pre-sign failure is not necessarily `COMPLETED` without an enumerated terminal receipt.

**Required F1 adjudication:** Enumerate every concrete precheck site (header bytes, registered key ID, agent empty, executable version/path, statement digest, sig candidate absence and signer-set/root role), its trusted evidence, precise flag origin and whether the event or attempt stops. Table rows must distinguish (a) proven invariant/identity tamper, (b) tool/environment inability, (c) incomplete or lost evidence, (d) ordinary no-proof and (e) ambiguous source. Independently test contradictory and higher-precedence flags. A single generic exception mapping is forbidden. Scenario S2-03 remains blocked.

## 4. B08-A1: owner Ctrl+C versus RP/Node fault without false instrument exceptions

**Already governed:** REV04 L0112, L0114, L0198 and L0202; policy `browser_node_interrupt` and `raw_flag_schema.node_rp_failure`. Ctrl+C consumes the claimed attempt but is not itself an unexpected RP failure. When a trusted owner-abort receipt clearly precedes a cleanup-induced Node exit, **do not** assert an independent instrumental Node fault. A causally independent RP failure proven before abort is an instrument fault absent a higher-integrity flag. A late RP receipt may substantiate only the particular completed event; it cannot create a missing owner proof or cross-process resume.

**Unresolved:** One approved policy leaf uses the causal term "unprovoked" and another uses the temporal term "before recorded owner abort". `owner_ctrl_c` says "by default", without an explicit rebuttal standard. Python and browser/Node monotonic clocks have different origins, so their raw timestamps alone do not prove ordering. For an unorderable fault/abort race, `INVALID_INSTRUMENT` versus `INVALID_INCOMPLETE` can affect B02 repair-exception eligibility. S3-03 remains blocked; Claude's earlier "prefer incomplete" was a reviewer candidate, **not** owner-approved policy.

**Required F1 adjudication:** Define safe independent event causality from the two append-only chains, trusted happens-before edges and cross-stream uncertainty; specify an explicit default and rebuttal evidence/precedence, ensuring that true independent node failures cannot be erased by a later Ctrl+C and owner aborts cannot be automatically treated as repairable instrument failures. Specify both P0 incomplete and a case with durably completed proof event but missing subsequent events. Independently review against the exact owner-approved B02 class/exception policy before freezing.

## 5. B11-A1: proof-budget terminal naming without changing the scientific observation

**Already governed:** REV04 L0068–L0071 requires **at most three native signing subprocess calls**, with the owner choosing R after nonzero/no-sig calls 1 and 2, one canonical decision/statement and one uninterrupted timer. L0070 labels exhaustion `PROOF_NOT_CREATED`. The *approved policy JSON* `evidence_state.terminal_outcomes[4]` instead lists `SSH_UNLOCK_BUDGET_EXHAUSTED`, and `COMPLETED` requires an enumerated terminal label. Neither term authorizes a fourth invocation or creates a cryptographic proof.

**Candidate resolution, NOT APPROVED:** Store the raw source-site terminal label *as observed*, and define a controlled, bijective schema mapping for this **same evidenced three-call outcome** to one canonical policy terminal value. Prefer an explicit representation-only alias **if** an independent review demonstrates equivalence for every call-count/owner R case and no change to score/exception eligibility. A counterexample must show that owner S, unexpected partial output, owner Ctrl+C, missing per-call receipts and any fourth-call claim cannot receive the exhaustion alias. The exact canonical spelling and trace form remain unresolved until review; S4-01 is a blocked candidate, not an auto-resolved finding.

## 6. Independence, decision prerequisites and next route

The 17 case records are narrow scenario assertions under explicitly named prerequisites, not a complete set of seven scored B01/B02 precedence-vector oracles. A case may assert a local event outcome but intentionally refrain from asserting the global scored class when the other arm, raw integrity flags, and proof viability are unspecified. Any future expected-output table must separately fix all these input dimensions and establish independently authored, reviewable known answers.

Before any F1 freeze, the task owner must: review the unresolved five cases with an independent collaborator; produce a scenario-to-source/proof trace; resolve genuine scoring conflicts without retrospectively modifying B01/B02; create exact negative expected-score vectors, particularly G1 and B02 exception-right counterexamples; and only then release separately bounded scorer implementation and blind oracle work. The 55 pending reviewer source-unit rows remain **UNRESOLVED** in the existing register until an evidence-supported per-unit resolution process formally closes them.

The next action is a *bounded independent Claude critique of this matrix* (MC-0030 Message 054) with Message 055 as the sole authorized output. The user may continue normal ChatGPT–Claude manual relay; the prior one-prompt 18-batch audit exception is now completed. Claude should challenge any unsupported source-based conclusion, omitted cross-case interaction, timing/provenance assumption, B01/B02 incompatibility and false negative. The task owner will then reconcile and decide whether any truly irreducible owner-policy interpretation must be requested. No new real Attempt 002 authorization is implied.

```text
RESEARCH_537=SCORING_BOUNDARY_REV01_CANDIDATES
SCENARIOS=17
SOURCE_DETERMINED=12
CANDIDATE_BLOCKED=5
GATES=B05-A1;B07-A3;B08-A1;B11-A1
B01_B02_ACCEPTED_BYTES=UNMODIFIED
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
