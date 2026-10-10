# R0-P01 Q1 amendment: independent oracle and distinct F1/F2 freeze contracts

**Date:** 2026-10-10
**Status:** UNFROZEN DESIGN AMENDMENT FOLLOWING CLAUDE MESSAGE 029 / REVIEW STILL REQUIRED
**Scope:** Reconcile Q-1/Q-2/Q-4 blocking gaps and Q-3/Q-5/Q-9 engineering corrections at the prospective specification stage, without freezing an implementation or creating an owner claim.
**Parent:** Claude MC-0030 Message 029 / Research 531 / Validation 220 / accepted REV04 B01/B02 / historical P01-C07
**Authority:** Technical design candidate and test-index amendments only. No exact F1 or F2 acceptance, owner credentials, Attempt 002, physical candidate selection, production implementation or project authority change.

## 1. Decision and interpretation

ACCEPT Claude's three blocking findings Q-1 clause omissions, Q-2 under-specified independence and Q-4 conflated freezes. ACCEPT Q-3's Arm B P5 dependency, following exact frozen V02 P01-C07: B V2 PRIMARY is Arm A PRIMARY and B V2 RECOVERY is Arm A RECOVERY, so absent current-attempt A setup/public members leaves B P5 FAIL with UNEXECUTED_ROTATION_TARGET_ABSENT. B P6 retains FAIL/UNEXECUTED_RECOVERY_MEMBER_ABSENT if same-attempt A RECOVERY is missing. Never create substitute members or use previous attempt keys. This is a prospective fixture clarification, not a change to the accepted B01/B02 result policy or original 13 controls. The independent scorer must instantiate each P5/P6 proposed target from actual public setup receipts and compare the exact statement/envelope; negative vectors swap roles, substitute nonmembers and replay A as B even when signers overlap.

The original Q0 trace, Q1 candidate and Message 029 remain historical. The prospective successor now uses a distinct REV02 trace index and this additional Q1 amendment; neither is a retrospective rewrite of already published records.

## 2. Q-1: source-exhaustive clause index, mapping review and test catalogue

The revised trace `R0_P01_Q0_REQUIREMENTS_TRACE_REV02_UNFROZEN.json` contains **53** explicit requirements (C01..C13 and R01..R40), of which nineteen are the missing Q-1 requirements and Q-2/Q-9 engineering obligations. Every C row has an explicit positional `control_key` binding through `security_control_key_bindings`. The test catalogue contains **105** distinct *planned* test IDs, each with test layer, expected-oracle source, forbidden shared component(s) and unexecuted state.

The source inventory algorithm `scripts/r0_p01_clause_inventory.py` enumerates **351** individual units from the approved committed Git blobs: 166 contract passages/list/table/fenced units in sections 1..11 and 185 JSON leaves across the normative policy roots. Each includes an exact source location/key path and SHA-256. The guard rejects an omitted/renamed/changed unit, unmapped unit, orphan requirement, mismatched control key, missing test-catalogue entry, unbounded owner authorization or false PASS/freeze metadata. Committed blob hashing is independent of Windows CRLF checkout conversions.

**Important limit:** source enumeration is mechanically comprehensive for the declared sections/policy roots, but the present clause-to-requirement assignments are PROVISIONAL SEMANTIC CANDIDATES, not fully independently reviewed. The index records mapping status REVIEW_REQUIRED and **22 weak section-only associations**. The section-default linkage and source-term hints are an aid to human reviewers and cannot establish that all individual obligations are accurately represented. No F1 freeze until an independent reviewer checks every normative clause's substantive mapping, resolves all weak mappings, identifies omitted nested normative blocks, confirms security control source coverage and explicitly accepts the test catalogue/oracles. Guard PASS demonstrates coverage-shape only, not semantic completeness.

The Q0 older SHA/hash validator now checks committed Git blob bytes and a public SHA-256 known answer. It never imports V02 owner-signing code or touches any original private evidence. Negative guard tests must mutate source index, mappings, catalogue, crypto controls and F1/F2 status in memory.

## 3. Q-2: enforceable scorer and oracle independence

**Adopt candidate B for detailed Q1 specification only**, as five logical units plus a separate test-only independent oracle. Physical module layout, programming languages, CI/CD and branch workflows remain revisable on merit until F2:

| Unit | Allowed upstream dependencies | Independence rule |
|---|---|---|
| `p01_spec` | Immutable F1 data, approved source and decision receipts | No runtime scorer/harness imports; source of test cases, not executable authority |
| `p01_core` | Spec, pure canonical/digest/renderer/state semantics | No private credentials, local RP, native GUI or global owner state |
| `p01_owner` | Spec + core + native SSH and evidence writer | Cannot override scoring or synthesize cryptographic proof after user declines |
| `p01_rp` | Spec + Node built-in crypto + its own append-only receipt stream | Never imports owner Python core, never stores real owner secrets or shares a mutable receipt writer |
| `p01_score` | Frozen F1 data, public immutable receipts, independent canonical/crypto implementation | **FORBIDDEN to import** p01_core, p01_owner or p01_rp directly or transitively. Explicit module/import graph enforcement in CI and F2 |
| `p01_oracle` | Separate author/language, F1 spec only | Test-only independent second canonical/renderer implementation; never shipped to real owner runner |

For F1 golden canonical statement, T1/T2/T3 view, role and P5/P6 template bytes, two separately authored implementations (e.g. Python and Node built-in primitives) must agree **byte-for-byte** before a vector is accepted. Disagreement blocks F1 and triggers explicit specification resolution; never pick the implementation whose output happens to match the future harness. Freeze canonical expected bytes/hashes, challenge contexts and source versions before production scorer implementation.

The scorer independently parses OpenSSH SSHSIG armour/length-prefixed binary, hashes the exact canonical signed statement with the declared hash algorithm, reconstructs namespace-bound signed data, verifies Ed25519 in-process with an independent implementation, and recomputes role-specific ledger admission. Do not reuse the harness `ssh-keygen -Y verify`, its temporary public files, its `verify()`, or any self-reported VERIFY/ADMIT/arm-success field. Negative corpus includes corrupt armour, malformed string lengths, wrong namespace, wrong hash algorithm, replay, wrong role and signed-but-unapproved trust root. WebAuthn ES256 verification and clientDataJSON origin/challenge/UV/UP/credential-ID checks must be implemented independently of the Node RP verifier, backed by public vectors. External library selections and hash-pinned dependencies need review before F2.

The classification oracle is **data before scorer code**: `R0_P01_F1_B01_DECISION_PREDICATE_TABLE_UNFROZEN.json` currently enumerates **288** predicate-lattice rows over six feasible per-arm (evidence_state, viable, eligible) combinations, integrity and instrument flags, and volume pass/fail. It is an **unreviewed draft**, not frozen expected truth; it omits numeric 10-second/15-second arm tie-break values, individual source-flag causality, full evidence-chain classification and B02 exception authorization, which need separately prospectively authored oracle vectors. An independent reviewer must verify the table against the original family and accepted REV04 before F1. The future scorer must be tested against frozen data and an independently authored oracle, never generate its own expectations.

Scorer output requires pinned canonical JSON serialization, explicit numeric/float reproducibility semantics and byte-for-byte comparison across repeated scoring on unchanged snapshots and cross-platform executions. A pending verifier environment remains nonfinal and cannot grant a new attempt.

## 4. Q-4: explicit F1 versus F2 freezes

**F1: pre-implementation fixture and independent expected-oracle freeze.** Freeze protocol/context/identity grammar; exact T1/T2/T3 and canonical nine-field serialization; all 13 original security control vectors; fully mapped normative clause index and bidirectional test catalogue; synthetic-public-member templates for P0/P5/P6 and their jointly generated/checked vector bytes; deterministic B01/B02 decision and stopping tables; flag origins, terminal outcomes, error *category vocabulary*, G1/G2 and full selection/timing/volume oracle, owner-readable instruction bytes and approved source/receipt hashes. F1 is reviewed and committed **before** the implementation under test is used to produce qualifying expected answers. F1 must not pretend to enumerate source-specific exception locations or runtime versions that are not yet chosen.

**F2: post-synthetic-qualification source/evidence freeze.** Bind the F1 exact hash, reviewed application and independent scorer source hashes, complete generated source-site error/exit/Node/browser map (zero unaccounted sites), pinned actual Python/Node/OpenSSH/Chromium/crypto dependencies, CI and target Windows test receipts, full synthetic A/B/C result and independently scored expected outputs, public evidence-writer/Node stream conformance receipts, security transcript scans, nonsecret operator-visible test instructions and known-answer gate logs. The source-site map is derived **from the actual implementation** then independently reviewed, not promised generically at F1. A change after F2 requires a new prospective F2 plus review before requesting Q6.

**Real Attempt 002 claim (Q6, later owner authorization):** exclusive owner-local marker references the exact F2 hash, transitively F1, accepted B01/B02 decisions and historical predecessor hashes. No real owner keygen, passphrase prompt, WebAuthn registration, or claim marker may occur before third explicit human authorization and qualified F2.

## 5. Q-5: one evidence writer per stream

Two independent durable streams are the preferred review candidate:

- The Node RP alone owns append-only `rp-NNNN` receipts for challenge issuance, pending assertion consumption, error and terminal status, with its own previous-exact-file-byte hash link and exclusive crash-safe writes.
- The owner-run harness alone owns `raw-NNNN` snapshots, its previous-exact-file-byte hash link and, at each committed snapshot, the last **durable** RP stream head hash/count observed.
- The scorer independently reopens both chains, reconstructs continuity and cross-chain references, rejects tampering or contradictory acknowledgement, and derives the final flag and event-state data without treating either stream as a second semantic authority.
- The optional postrun owner witness includes both heads and the exclusive claim hash. Witness absence remains SCORER_DERIVED/DISCLOSURE_ONLY; an actual proven breach retains INVALID_INTEGRITY.

For Windows F2 test, evaluate no-overwrite `MoveFileExW` with WRITE_THROUGH (without REPLACE_EXISTING), file flush and same-directory temp promotion; do not assume POSIX directory fsync exists on Windows. Qualify restart/crash/orphan temp cases and Node abort ordering. If the filesystem cannot meet required guarantees, a revised prospective implementation contract is required before F2.

## 6. Windows and synthetic qualification tiers

CI/synthetic Windows: hash-pinned Python/Node/OpenSSH toolchains; ConPTY-owned test driver with disposable passphrase-protected synthetic Ed25519 keys, proving inherited SSH prompt R/S, wrong-to-correct, three failures, SIGINT, swapped-key and agent-precondition rejection with no transcripts containing secrets. Separately test `CREATE_NEW_PROCESS_GROUP` and console Ctrl+C propagation against Node, and forced RP death after durably committed receipts.

WebAuthn: Chromium CDP CTAP2 virtual authenticator for positive ES256/UV/UP and negative UV=false, foreign credential, nonpresence timeout (with frozen 120-second production setting), consumed NotAllowedError RP receipts and exact binding. This cannot qualify native Windows Hello's actual human PIN/biometric experience.

The owner's actual Windows machine requires a **synthetic-only** platform conformance run after F1/F2 prerequisites, with no historical owner keys, no real owner claim marker and no new live credential. Versions and environment must be recorded, and the run is not substituted by CI. All nonstandard tools/dependencies require hash-pinned locks and a no-network owner-run claim.

Arm C S01/L01 synthetic chat-role observations must be stored under a clearly separate comparator schema: missing task-owner receipt or mismatched line fails C alone and cannot influence A/B outcome. Repeat-owner prior practice, original Attempt 001 AMEND, event failure continuation, no proof pooling, interaction floor and timing/volume gates must all be disclosed and tested prospectively.

## 7. What remains blocking

- All 351 candidate clause associations, including 22 weak section-only mappings, require independent substantive adjudication before F1.
- The 288-row B01 classification table and missing numeric tie-break/flag/B02 cases require independent expected-output review. No scorer implementation has been qualified.
- The second canonical implementation and in-process SSHSIG scorer do not yet exist.
- F1 has not been approved/frozen; F2 cannot be frozen without code and Windows/browser synthetic evidence.
- No real Attempt 002 may occur. B01 and B02 remain accepted without modification.

```text
MESSAGE_029=ACCEPT_BLOCKING_CORRECTIONS_AT_DESIGN_LEVEL
Q0_REV02_CLAUSES=351_PROVISIONAL
Q0_REV02_REQUIREMENTS=53
Q0_REV02_TEST_CATALOGUE=105_PLANNED
F1=NOT_FROZEN
F2=NOT_FROZEN
OWNER_ATTEMPT_002=NOT_AUTHORIZED
NEXT=INDEPENDENT_SEMANTIC_MAPPING_AND_F1_ORACLE_REVIEW
```
