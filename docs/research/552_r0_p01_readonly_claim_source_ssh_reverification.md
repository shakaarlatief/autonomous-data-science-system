# Research 552: independently reverified SSH proof against the durable synthetic claim source

**Date:** 2026-10-12
**Status:** SOURCE_AS_PRESENTED_CRYPTOGRAPHIC_REVERIFICATION_PASS / PRODUCER_ORIGIN_UNATTESTED / F1_UNFROZEN
**Scope:** Bounded R0-P01 SSH claim consumer that binds a **separately supplied trust context and selected claim nonce** to a coherent read-only snapshot of an existing synthetic issuer journal and re-verifies actual admitted SSH proofs with native OpenSSH.
**Parent:** Research 540, 544-551; Checkpoint 887; owner-accepted B01/B02 and simplified accident/replacement policy.
**Authority:** Experimental implementation/qualification evidence only. It is not an owner authentication ceremony, external issuer/host attestation, anti-rollback witness, final physical design, F1/F2 freeze, or Attempt 002 authorization.

## Question and rationale

Checkpoint 887 qualified a real `ssh-keygen -Y verify` proof-observation path, but an externally supplied source-shaped receipt remains easy to fabricate. The next test must check **where the proof came from**, not just whether a receipt field says VALID.

The bounded new consumer `experiments/r0_p01_successor_synthetic/independent_ssh_claim_source.py` reads the existing `SyntheticClaimStore` journal **without issuing, signing, admitting or mutating a claim**. Its inputs are distinct from the presented journal: trusted synthetic issuer ID, historical canonical statement template, public enrolled signer, governed/ungoverned policy, exact selected run nonce, expected signed acceptance identity and permitted scratch area. The code constructs the expected issuer genesis, compares exact stored genesis bytes, reconstructs every expected run-bound statement from template and nonce, validates claim identities, sequence, statuses, recorded proof bytes/hash and relevant auxiliary authorization/observation records.

For **every journal row claiming ADMITTED**, the consumer independently invokes the existing actual OpenSSH observation module against the reconstructed expected statement and trusted public key. A malformed or invalid earlier admission blocks a later row's apparent success. Unadmitted or superseded claims return `NOT_RUN`, never fabricated proof success. An unknown selected nonce fails visibly rather than choosing an arbitrary ADMITTED row. The journal is opened in SQLite `mode=ro` and a read transaction supplies a coherent snapshot.

The returned immutable `SSHClaimAssessment` contains precisely: trusted-context-derived genesis digest, selected nonce, sequence, acceptance ID, recorded journal status, independently calculated expected-statement digest, admitted-proof-record digest when available, proof-verification result, and an unconditional `source_origin_authenticated=False`. It deliberately has **no F1 event-terminal status, REALIZABLE/NOT_REALIZABLE conclusion, complete arm state, or owner-authentication claim**.

## Adversarial evidence

**22 new executable non-owner tests** pass. The cases cover an issued-but-unadmitted claim, a genuine synthetic Ed25519 admission reverified through real OpenSSH, an independent fresh Python consumer process with no access to the signer worker, wrong external issuer/signer/acceptance/nonce, missing journal, fake ADMITTED status with no proof, tampering with signed decision/nonce/signer/signature while recomputing unkeyed record hashes, rewriting expected statement and its SHA-256, an unrelated corrupt admitted historical row, a superseded claim, synthetic procedural authorization records, modified authorization and observation contents with new hashes, verifier failure, and read-only source contents before/after verification.

The complete bounded regression is **431/431 focused PASS**: 168 new-plus-prior SSH/F1 reference cases, 179 earlier cryptographic/admission/measurement cases and 84 structural/provenance guards, with separately reported test groups. This is a focused/subsystem set, **not** a complete integrated V3 or independent frozen scored experiment. Exact commands and repository-gate results belong in Validation 240.

## Trust and epistemic limitations

**Proved at this boundary:** The selected SSH signature is cryptographically valid over the particular trusted, reconstructed run-bound statement **as presented by a coherent instance of the local synthetic journal**, with selected nonce and public signer taken from independently supplied inputs. Arbitrary JSON status/verification labels, stale nonce selectors and corrupted source records cannot substitute for those checks under the tested path.

**Not proved:** The database writer or issuer is independently authenticated. The supplied synthetic "trusted controller" policy label is not a real owner consent proof. Cryptographic validity of a signature does not prove that the original acceptance was durably admitted by an authentic issuer: a hostile party possessing an already-valid proof could attempt to reconstruct a self-consistent journal. An unwitnessed valid historical snapshot might be rolled back/replayed wholesale; the reader does not independently know the newest head. Local source integrity, public trust-root provisioning, authentic producer identity, signer exclusivity, external witnesses, owner presence, real SSH passphrase prompts, platform WebAuthn, browser/RP issuance/consumption and a complete four-event F1 run remain outside scope.

A dedicated **adversarial limitation witness** also takes a genuinely valid synthetic SSH signature and inserts it directly into a local `ADMITTED` journal row **without calling the issuer's admission operation**. The reader rightly verifies the proof as VALID *as presented*, yet still returns `source_origin_authenticated=False`. This demonstrates, rather than merely hypothesizes, the missing independent origin/admission-authentication guarantee.

The consumer checks the native OpenSSH program's bounded English output contract. Its schema and SQLite storage are **replaceable experiments**, not D-036 target physical-architecture commitments. New and existing implementation/test work was authored within this same ChatGPT session and has not received a separate blind-scoring review.

## Next legitimate work

Advance from **read-only verification of evidence as presented** to producer-authenticated, externally reconstructible source evidence and actual bounded event lifecycle. Specify and test a trust anchor independent of caller-produced receipt JSON and, where necessary, independent of the mutable local issuer journal. Source-authentic terminal-event observation needs explicit issuance/invocation/consumption or completion facts and failure/interrupt semantics, particularly for the RP/browser WebAuthn path. The full B01 scorer can only be qualified once those inputs are actually sourced, with independence appropriate to risk. Keep the effort proportional; do not invent owner retry restrictions or authorize a real owner trial.

```text
RESEARCH_552=SSH_CLAIM_SOURCE_AS_PRESENTED_REVERIFICATION_PASS
NEW_TESTS=22
FOCUSED_TOTAL=431
PRODUCER_ORIGIN_AUTHENTICATED=NO
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
