# R0-P01 Q1: prospective exact-fixture and implementation boundary candidate

**Date:** 2026-10-10
**Status:** UNFROZEN Q1 TECHNICAL PROPOSAL / NO OWNER CLAIM
**Scope:** Define the proposed testable software boundaries, fixture-freeze sequence, independence requirements and open technical decisions for the B01/B02-approved R0-P01 successor.
**Parent:** Research 530 / Checkpoint 866 / Research 513 / Q0 requirement trace and approved REV04 proposal
**Authority:** Nonsecret design proposal only. No fixture, implementation or scorer freeze, real owner key/signature, WebAuthn registration, Attempt 002, physical architecture selection or project authority switch.

## 1. Governing source authority

The Research 513 frozen family gates remain unchanged: 13 hard security controls, exact owner-visible statement, three small trials with 1/2/4 effects, one large with 30 effects, median small mechanical <=60 seconds, each small <=120 seconds with its previously bounded infrastructure condition, large <=120 seconds, zero manual metadata edits and exposure, projected count <=100 and owner mechanical burden <=90 minutes. Existing inventory is 97 projected acceptances, 157 effects, distribution 62/17/11/7.

The human has independently accepted B01 (prospective evidence-state, G1/G2 and mechanical INVALID classification) and B02 (finite stopping policy, maximum two new claims, ALL_REQUIRED exceptions and no post-PASS claim). Their exact source identity is preserved through the Checkpoint 866 owner decision receipts. Approved REV04 contract SHA-256: 9160a30c481c1c67c2ec857238f5a04b44f618b2ef589ef4f1c514eb3b3d6175. Approved policy JSON SHA-256: 9b5bbc4d2c4802fc80b46bcaa3d003640c33e8e4784d39ef7995dbf193dff86c.

The historical V02 fixture and implementation are comparison references, NOT fixed successor file-layout, coding, process, testing or operational requirements. Their original owner evidence and Attempt 001 AMEND cannot be changed, pooled with a later claim or rescored to green. The approved JSON still has predecision UNAPPROVED lifecycle fields; do not overwrite it. A later versioned manifest must bind both approved proposal bytes and the separate human acceptance receipt.

## 2. Implementation choices remain open at every level

Candidate A is a small single coordinator with separate verification libraries. It minimizes component count but makes the owner-input, platform, exception and evidence-boundary blast radius larger.

Candidate B separates pure canonical semantics, owner-view renderer, immutable event/state core, native credential adapters, append-only evidence writer and independently implemented scorer. It makes exact error-site audit, field provenance, replay control and crash testing more tractable while increasing integration complexity. Candidate B is provisionally preferred FOR REVIEW ONLY. Neither candidate is a frozen architecture.

Repo folders, branch rules, CI/CD, language, operating procedures and model/code collaboration may be replaced whenever quality and independent qualification justify it. Source authority, owner-only credential control and previously approved experiment gates remain mandatory.

## 3. Component responsibility and trust contract

| Boundary | Responsible behavior | Required independent proof |
|---|---|---|
| Fixture/compiler | New distinct attempt context/project/acceptance-ID grammar, canonical SignedAcceptanceStatement with nine fields, synthetic P0/P5/P6 key-member templates | Full golden bytes, structural old-proof rejection, test-key binding and negative vectors |
| Owner view | Renderer displays same UTF-8 bytes that shown_digest commits; envelope_digest binds canonical envelope, procedural T3 outside signed view | Byte-for-byte renderer oracle, whitespace and mutation tests |
| State and admission | Independent scenario GENESIS, P0, P5/P6 historical roles, replay registry, valid VERIFY distinct from ADMIT, compromise sequence policy | All 13 controls with actual rejection-layer evidence, no self-authorizing rotation |
| Owner-run coordinator | Exclusive real claim only after third future human authorization; one captured decision and one timed event, native calls, no auto-reissue or cross-process resume | Event-state machine and source-site complete error mapping |
| SSH adapter | Native inherited terminal prompt, passphrase never captured, max three owner-chosen R/S invocations, prior statement/key/agent rechecked | Synthetic real native SSH prompting, aborts, partial file and timer tests |
| WebAuthn adapter | Localhost RP, ES256 + UV/UP, fresh single-use digest-bound assertion, durable RP issuance/consumption receipts and native Windows Ctrl+C safety | Virtual-CTAP2 full crypto verifier path plus separately qualified Windows process behavior |
| Evidence | Exclusive claim; atomic no-overwrite snapshot promotion and exact previous-file hash; owner postrun nonsecret final witness | Crash/tamper tests, absence-of-witness disclosure without result change |
| Independent scorer | Independently reconstructs canonical proof, signer history, controls and burden; computes source-derived flags and G1/G2; does not trust harness success claims | Independent fixed expected-results corpus and malicious/untrusted evidence cases |
| Weaker C comparator | ChatGPT user-role digest attestation remains non-cryptographic and never selectable | Synthetic role receipt explicitly marked a test double, not claim of real human platform provenance |

A shared production crypto primitive cannot itself serve as independent evidence for a correctness claim. Where a library must be shared, an independent oracle reconstructs expected bytes, public proof and admission outcome by a distinct test path.

## 4. Exact-future-fixture preparation before implementation qualification

The next reviewer-qualified fixture should freeze canonical T1/T2/T3 view tables and nine signed fields, issued_at/profile rules, exact synthetic project/attempt namespace, owner decision capture, negative control mutations, full independent 13-control oracle, small/large trials, key-dependent P5/P6 templates instantiated with synthetic keys, and expected signer-set histories.

It must freeze the complete B01 terminal evidence-state definition, WebAuthn RP-consumed NotAllowedError terminal-no-proof rule, capability NotSupportedError requirement, source-derived INVALID flag priority, ordinary owner typo re-prompt and absence-of-final-witness disclosure-only rule. The selected implementation must later demonstrate every source raise/subprocess/Node/browser error is exactly mapped. No unknown exception may become an unexamined integrity, instrument or owner-abort classification.

Preclaim known-answer tests for synthetic SSH and WebAuthn proofs must run in the same harness environment BEFORE a real claim; a failure creates no real marker. The scorer must separately test its own verifier environment. All snapshot partial writes, claim collisions, timestamp domains, Node interruption ordering and state-lifecycle semantics need target Windows tests.

B02 policy and approval receipt hashes are bound in a NEW freeze manifest with truthful lifecycle metadata. The accepted REV04 draft itself is neither rewritten nor treated as executable. Future fixture/oracle outputs must be frozen prospectively before owner observation, with source/test hashes and tool versions; later fixes require explicit prospectively reviewed refreeze, not altering a consumed attempt.

## 5. Bounded work packets and exit gates

Q0 source/requirements alignment: 34 machine-readable requirements, all 13 control names, trial sizes, original inventory, approved exact hashes and read-only reference artifact hashes. Static guard and mutation tests must pass. **This is the only part already implemented here.**

Q1 exact fixture/implementation-design proposal: independent reviewer chooses between or refines candidate decompositions, verifies event taxonomy, exact source/expected oracle separation and canonical identity. The reviewer may reject this proposed layout on technical grounds. No freeze by default.

Q1 exact prospective fixture freeze: dedicated uniquely versioned fixture/oracle source, test vectors and expected output hashes, reviewed before new implementation qualification. All future owner-sensitive paths remain unexecuted.

Q2 independent pure primitives, scorer and synthetic harness: new isolated successor source, source-site error inventory, property/negative tests and independent classification tests. Tests never import original V02 owner-run implementation to assert PASS.

Q3 Windows native and browser qualification: disposable synthetic Ed25519 keys, Node process group/receipt durability, same-directory snapshot atomicity, preclaim noncredential browser reachability, virtual WebAuthn CTAP2 composition. Virtual authenticator evidence does not qualify Windows Hello UX.

Q4 full synthetic A/B/C execution: 13 controls per A/B, all P0/S01/S02/S03/L01/P5/P6 events, role history, canceled assertions, defective verifier, aborted run, tamper and strict B02 stopping scenarios. Comparator C may use marked synthetic platform-role receipts only; never credit as actual human ChatGPT user provenance.

Q5 independent exact scorer/fixture/harness/Node conformance audit and verified source/run hashes, with no real owner trial. Every violation remains visible rather than patched to PASS.

Q6 a **third separate human approval** before any real Attempt 002 owner marker, owner SSH key or WebAuthn registration/signature. B01/B02 do not grant Q6.

## 6. Targeted technical review questions

1. Can the independent scorer reconstruct proof/admission without trusting a harness-provided success or a shared defective helper?
2. Can key-dependent P5/P6 text be instantiated only after synthetic/public member identities exist, while all templates and golden predictions remain exact?
3. Is WebAuthn cancellation terminal only with a durable same-acceptance pending assertion consumption receipt?
4. How does the source-site inventory ensure no generic exception->integrity fallback remains?
5. Can the target Windows filesystem and Node lifecycle actually deliver the promised safe snapshots and interruption receipts?
6. Can the full virtual WebAuthn path be tested without asserting native platform owner-UX success?
7. Does any unnecessary new service or second ledger introduce authority dependence rather than testability?
8. Are all 34 source trace items mapped to independently verifiable expected outcomes instead of circular implementation self-tests?

Review should return a bounded acceptance/amendment verdict and concrete tests, not conduct an owner ceremony or assume this proposal is frozen.

```text
Q1_STATUS=UNFROZEN_CANDIDATE
IMPLEMENTATION_ARCHITECTURE=NOT_SELECTED
EXACT_FUTURE_FIXTURE=NOT_FROZEN
FULL_SYNTHETIC_A_B_C=NOT_EXECUTED
OWNER_ATTEMPT_002=NOT_AUTHORIZED
NEXT=INDEPENDENT_Q0_Q1_DESIGN_CRITIQUE
```
