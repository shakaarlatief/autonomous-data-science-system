# Validation 264 candidate: R0-P03 S1 reviewer transport, protected custody and role-separation qualification plan

**Date:** 2026-10-20
**Status:** PROSPECTIVE_PLAN / NO_REAL_BATCH / NO_PRIVATE_CUSTODY_SELECTED / NO_MUTATION_AUTHORIZATION
**Scope:** Specify an engineering evidence path for qualifying **S1** without exposing actual historical gold, designer information or scoring artifacts during engineering trials. Complements Research 596 and the V0.4 method candidate; not a passed validation or an endorsed particular filesystem/process architecture.
**Authority:** Operational planning only. Does not authorize creating private data stores, connecting external reviewer apps, uploading protected records, changing repo topology, restructuring CI or launching a real contaminated-content review.

## 1. Why S1 needs independent work

Research 593–596's fictional method reviews identified and progressively clarified source-status distinctions, but did not test whether a real reviewer can receive exact, immutable permitted evidence; retain a confidential tamper-evident result; resume after interruption; separate private hints from an author-visible packet; or obtain an independent challenge and authorization with durable provenance.

The scientific S1 prerequisite remains **positive, witnessed qualification** of these mechanisms. Source pin `c57556a8bf993a1d327e9197acb7b7c745071cd8` and counts (406 candidate, 2,133 review-only) are *future scope identifiers*, not permission to inspect any real member now. Checkpoint 898, Specification 028, Research 513/559/576 and the prior nine-case old W5 cohort remain fixed.

## 2. Design degrees of freedom and trust boundaries

No existing folder, branch practice, Git repository, process, secret store, test harness or workflow is treated as a required final structure. We may replace, split, consolidate or redesign the entire implementation and working procedure when evidence supports it. Conversely, an imagined better architecture is not proof of readiness.

The trust boundaries to preserve are:

1. **Public engineering coordination:** Research methods, safe test harnesses, nonanswer-bearing progress, exact code and hash receipts. Must not contain the real reviewer-private ledger or dangerous source-to-gold correlations.
2. **Restricted reviewer intake:** receives only approved exact source batches with provenance, permitted modality and independently logged exposure; must not leak to the fresh author.
3. **Restricted reviewer/challenge output:** full source-specific contamination, conflicts, protected snippets, unresolved decisions and original/updated reviewer evidence; must have separately qualified controlled access, durable readback and reproducible resumption.
4. **Neutral author release:** exact permitted original sources/excerpts and bound, verified actual interface rendering; not an annotated extract or hidden answer-containing metadata.
5. **Independent reference and scored experiment:** distinct later custody and roles; cannot silently share reviewer context or become an extension of this S1 engineering work.

A normal ChatGPT Temporary Chat, a public Git commit, arbitrary cloud attachment or the private Codexless runtime repo does not automatically qualify any restricted boundary. User-controlled review, threat analysis and explicit route authorization are needed.

## 3. Candidate architectures to compare, not preselect

These are hypotheses for the eventual qualified S1 implementation, **not** a decision to retain current infrastructure:

| Candidate | Potential advantage | Qualification risk / required proof |
| --- | --- | --- |
| Dedicated owner-local encrypted reviewer workspace and versioned restricted ledger | Local custody, controllable raw bytes and deterministic readback | Identity/access segregation, key handling, backup/recovery, attachments/logs and process permissions must be evidenced; local disk alone is not a secrecy proof |
| Purpose-specific managed restricted reviewer service and append-only encrypted output journal | Policy-enforced role admission and structured event provenance possible | Requires complete service trust boundary, auth/key lifecycle, secret-safe logs, recovery, reviewer separation, audited public receipt and authority approval; avoid broad host access |
| Owner-mediated batch exchange to a separately bounded reviewer session with isolated results storage | Reduces complexity for initial qualified small batches | Manual transcript, Temporary Chat files, UI capture and copy/paste can leak protected notes; session persistence and private readback must be proven before protected content |
| Alternative architecture discovered during tests | May improve isolation, robustness and scientific repeatability | Reevaluate all trust gates rather than treating the first three candidates as exhaustive |

No recommendation of a specific provider, folder location, Git branch, retained secret, schema backend or service is approved until tested against the real requirements. A small synthetic-only demonstrator may use an intentionally disposable simulated reviewer ledger *outside the real corpus*.

## 4. Qualification matrix and evidence standards

| Gate | Required pre-real-source evidence | Fail-closed outcome |
| --- | --- | --- |
| Actor and role admission | Declared actual reviewer, challenger and authorizer; tested available context, prior exposure, role exclusion, identity permissions and scope | `S1_REVIEWER_OR_CHALLENGER_UNQUALIFIED` |
| Manifest and delivery | Exact pinned-blob identity, SHA-256, sizes, mode, supported representation and provenance; complete received bytes compared with expected roster; replay protection | `S1_SOURCE_DELIVERY_UNVERIFIED` |
| Full disclosure/renderer parity | Loaded/navigable/inert link policy; captured exact author-facing content, assets and generated metadata; no unfrozen external downloads | `S1_RENDERING_OR_LINK_BOUNDARY_UNVERIFIED` |
| Protected storage | Owner-approved restricted location and role ACL, append-only record integrity, tamper signals, backup, restart/recovery, confidential exported logs and access isolation | `S1_REVIEWER_CUSTODY_UNQUALIFIED` |
| Incomplete/interrupted batch | Crash/resume from exact source+scope+reviewer version, partial and unsupported flags, no duplicate acceptance of stale unfinished entries | `S1_RESUMPTION_UNQUALIFIED` |
| Secondary independent challenge | Challenger restricted read scope, actor exclusion from later blind author/evaluator, evidence of actual independent contest and disagreement retention | `S1_CHALLENGE_BOUNDARY_UNQUALIFIED` |
| Public receipt anti-leakage | Verified no protected source-specific names or statements; cumulative differencing/join test against prior visible receipts and known roster metadata | `S1_PUBLIC_RECEIPT_UNSAFE` |
| Exact author packet release | Independent approved authorization actor and exact manifest; no private annotations; context complete; generated citation/search/download metadata safely controlled | `S1_AUTHOR_PACKET_RELEASE_UNQUALIFIED` |
| Semantic reviewer contract | V0.4 or later accepted as a bounded **source-disposition method**; no unresolved material false-PASS | `S1_METHOD_NOT_ACCEPTED` |

The table contains **qualification questions**, not passing receipts. A tool's presence or a synthetic document's PASS does not satisfy protected-storage, reviewer or author release requirements.

## 5. Safe first engineering prototype and attack cases

The first implementation exercise may proceed using **invented content only**, after a separate engineering work boundary is accepted. It should produce an isolated, versioned candidate artifact, not mutate real source eligibility rosters or the current scored-experiment state.

Candidate proof obligations, with no actual historical ADS source data:

- Generate a fixed fake manifest and verify bytes, blob identity and receipt against intentional partial/truncated/mismatched batches.
- Simulate a fully inspectable source with a protected fake annotation injected through a dynamically loaded asset; show that a frozen source hash alone cannot authorize release.
- Test an inert citation versus a navigable URL and a material off-file exception; prove that irrelevant inaccessible citations do not create false automatic holds while material context does.
- Test a co-dependent pair as one conditional candidate bundle and verify that either missing or prohibited dependency holds the atomic release without suppressing both narrow historical source claims.
- Produce separately typed semantic disposition, independent challenged status, author-release gate and author-world sufficiency records; ensure `CANDIDATE_FULL / PROPOSED` is representable while exposure is held.
- Simulate compound blocker (missing final section + known protected section), maintaining both facts and persistent prohibition through delivery retry.
- Verify confidential ledger write, exact readback, restart/crash recovery and actor access rejection in the *chosen simulated* store; do not claim this qualifies a future real repository or external chat without route and permissions proof.
- Attempt public aggregate differencing, alias/download filename, search snippet and citation label leaks; require fail-closed behavior rather than assuming absence after one regex pass.
- Append challenger disagreement and revised authority claim, then verify invalidation of dependent candidate span, bundle, render and authorization.
- Test both invalid admissions and inappropriate exclusion of a harmless nonnormative observation, a proposal with unproven later deployment, or a safe independent span within an otherwise prohibited file.

The extent of usable automation and generated results should remain clearly labeled **synthetic engineering tests**, not independent semantic adjudication.

## 6. Explicit architecture evolution triggers

At every S1 design/implementation gate, actively check whether any of the following require structural redesign rather than another patch on the existing system:

- Reviewer output includes unexpected protected fields in logs, transcripts, tracing, backups or generated UI metadata.
- The proposed boundary cannot actually separate reviewer, challenger, future author and coordinator access.
- Protected storage is inaccessible from a qualified independent reviewer, or a restart loses/reorders crucial dispositions.
- The source representation loses exactness, external assets change after hashing, or UI-derived disclosures bypass file-level controls.
- Cumulative receipts leak classification through joins despite per-message sanitization.
- Tool/window limits prevent complete, attestable coverage of the declared source families.
- A supposedly static schema does not express conflicting evidence, bundle cycles or dependent invalidation without ambiguous untyped states.
- A superior validated custody or batch architecture becomes feasible, even if the current design technically works.

Record each trigger, evidence, alternatives and decision authority. Do not automatically expand working roots, ACLs, credential scope or private-to-public publication to solve a blocked gate. An architecture change may replace workflows, directory structures, testing and branches as needed, but is still subject to independently evidenced role and science constraints.

## 7. Concrete next work and handoff

**First bounded work unit:** perform a source-free S1 candidate architecture and transport/custody threat review; select only the *test harness and simulated storage* for an engineering qualification trial, and run it with synthetic objects. This is distinct from choosing the final restricted reviewer custody for real protected content.

**Before real source intake:** the owner and qualified reviewers must explicitly approve the actual trusted actor, content source, access path, confidential output destination, key/custody procedure and independent challenge route; confirm exact manifest/renderer checks; and accept a guarded readback/recovery test. If these cannot be verified, preserve HOLD with the specific failed gate.

**S0 method status:** V0.4 is a proposal awaiting a bounded separate challenge; it need not block source-free S1 architectural analysis, but it blocks **actual reviewer source classification** until independently accepted.

**S3/S4:** no primary task packet, neutral reference, task author, old W5 gold or scoring is in scope.

```text
VALIDATION_264=PROSPECTIVE_S1_QUALIFICATION_PLAN_NOT_EXECUTED
S1_ARCHITECTURE=NOT_SELECTED
S1_REAL_CUSTODY=NOT_APPROVED
S1_REAL_SOURCE_DELIVERY=NOT_AUTHORIZED
S1_SIMULATED_ENGINEERING_TRIAL=NOT_RUN
S0_V04_METHOD=UNREVIEWED_PROPOSAL
AUTHOR_WORLD=NOT_FROZEN
B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
