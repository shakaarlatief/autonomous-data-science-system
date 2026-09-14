# Research 146: MC-0016 Adversarial Candidate Review Disposition and Candidate 01 Design Amendments

**Date:** 2026-09-14
**Status:** CLAUDE ADVERSARIAL REVIEW ACCEPTED WITH CALIBRATED CORRECTIONS / CANDIDATE 01 AMENDED / TWO NARROW DESIGN POINTS RETURNED TO CLAUDE / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Reconcile Claude MC-0016 Message 001 against Requirements V0.2 and Candidate 01, preserve valid defects and calibration corrections, amend the candidate before implementation, and decide whether one final narrow Claude turn is warranted.
**Authority:** Supporting Research 124 candidate-design evidence. Requirements V0.2 remain frozen. This record does not select a target architecture or authorize authority migration.
**Declared references:** `research:124`, `research:143`, `research:144`, `research:145`, `path:docs/model_collaboration/threads/MC-0016/messages/001_claude_adversarial_candidate_01_review.md`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`, `checkpoint:490`

## 1. Overall disposition

Claude Message 001 is a strong adversarial review and materially improves Candidate 01. The most useful contribution is not a wholesale family change. It is the identification of several places where Candidate 01 stated a correct architectural intention without yet specifying the governance rule that makes the intention safe in practice.

The review does **not** establish that Object-Primary/H3 should reopen now. It does establish that Candidate 01 must close several seams before implementation becomes useful evidence.

The main accepted findings are:

```text
ACCEPT
    action-contract prose/structure precedence was under-specified
    joint-authority creation/admission governance was under-specified
    consolidation/current-state fidelity needed an operational verification mechanism
    routine derived refresh needed an explicit incremental/locality rule
    rollback needed a concrete post-switch-safe mechanism
    capture backlog pressure should be observable
    long-paused workstreams need active-surface salience semantics
    profile/special-object growth should be measured as a possible H3 reopening signal

CALIBRATE / REASSIGN
    KA-R31 and KA-I12 concern required reconstruction cost, not full-rebuild cost
    KA-R46 concerns semantic identity continuity, not the complexity of rebuilding its index
    rollback mechanics belong most directly to KA-R44 transition safety, not KA-R43 migration preservation
    JOINT_AUTHORITY under-specification is a real candidate defect, but it does not by itself mean KA-R14 lacks ordinary replacement/supplement/conflict semantics
```

## 2. One-home-per-fact rule inside a governed procedure

Claude correctly identifies an ambiguity in Research 144 Section 7. Candidate 01 said the structured action contract was an "authoritative projection" while also saying the prose remained authoritative. That leaves two normative homes for the same constraint if the prose and structured contract disagree.

Candidate 01 is amended with this rule:

> **For every semantic fact that participates in an exact action contract, the structured contract is the sole normative encoding of that fact. Human-readable prose may explain, motivate or illustrate the constraint, but it may not independently add, remove, reorder or redefine a machine-governed mandatory constraint.**

Consequences:

```text
constraint facts
    one authoritative home: structured action contract

human-readable contract rendering
    generated from or keyed to the structured contract

explanatory prose
    non-normative with respect to facts already represented in the contract

new mandatory constraint discovered during editing
    must be added to the structured contract before the procedure can remain
    qualified for exact-fidelity consequential execution

prose/contract disagreement
    document defect; do not arbitrate at action time
```

Each material constraint receives a stable local constraint ID. Where prose explains a constraint, it references that ID. This removes the need for a model to decide which of two conflicting copies is authoritative.

This amendment closes the main design ambiguity Claude attached to KA-R09.

## 3. Consequence-shaped action-contract assurance

Claude is also right that "one model pass is not enough" is too vague by itself.

Candidate 01 now uses an assurance ladder:

```text
LEVEL 1 - DETERMINISTIC CONTRACT CHECK
    always required for governed exact-fidelity actions
    verify preconditions, required constraint IDs, ordering, prohibitions,
    required verification/postconditions and source revision binding

LEVEL 2 - STRUCTURED EXECUTION PLAN
    proposed consequential action is represented as a plan referencing the activated
    constraint IDs before free-form instructions or mutation dispatch

LEVEL 3 - FINAL-OUTPUT CONFORMANCE
    if final natural-language guidance can semantically alter the plan, require an
    independent verification path before high-consequence dispatch

independent verification path
    may be a separately prompted/model-isolated verifier, a human reviewer, or another
    project-qualified mechanism; it may not be the same unverified generative pass
```

The architecture does not require two-model review universally. Deterministic conformance is the first line of defense. Independent semantic verification is required only where a free-form transformation can materially alter a high-consequence contract and deterministic checks cannot establish equivalence.

## 4. Non-circular joint-authority admission rule

Claude's most important architectural challenge concerns the `JOINT_AUTHORITY` exception. Candidate 01 must not repeat the earlier mistake of pretending a hand-set semantic label is a mechanized classifier.

The candidate is amended to make **no joint-authority declaration the default**. A joint-authority semantic source may be promoted only when all of these are evidenced:

```text
J1  two or more current canonical sources overlap on the same governed action/scope/time
    and each contributes non-redundant mandatory governing content;

J2  ordinary source-owned relations such as SUPPLEMENT, SPECIALIZE, CORRECT or REPLACE,
    followed by deterministic closure, cannot represent the complete governing-set semantics;

J3  there exists at least one set-level authoritative fact that is not already owned by a
    member source and is not derivable from the member relations alone, for example a
    closed all-members-required set, set-level ordering/precedence, set-level effective
    interval, set-level conflict state or durable continuity of the governing set itself;

J4  that set-level fact must be queried or activated independently for correct consequential
    behavior, so leaving it implicit would produce ambiguity or repeated heuristic synthesis;

J5  creation is an explicit promotion decision with evidence and a review receipt;
    the validator rejects duplication of the same set-level fact in member sources;

J6  if J1-J4 cannot be established clearly, the result is UNRESOLVED rather than automatic
    creation of a joint-authority object.
```

This is deliberately a **governed admission test**, not a claim of fully automatic semantic classification. The frozen requirements do not require mechanized ontology induction. They require explicit authority semantics and fail-visible uncertainty.

The first prototype must include a deliberately difficult case that attempts to satisfy J1-J4 and a near-miss case that must remain source-local plus derived closure.

## 5. Consolidation fidelity becomes an executable contract

Claude correctly identifies that Research 144 cited Research 129's F1-F9 fidelity dimensions without yet turning them into a checkable consolidation mechanism.

Candidate 01 is amended with a `must-preserve manifest` for consequential consolidation or promotion. Before a detail-rich source set can be made latent, the consolidation operation identifies the material units that its declared view must preserve.

Depending on the source/view class, the manifest includes:

```text
governing constraint IDs
current authority / supersession facts
limitations and uncertainty
material disagreements / minority evidence
dependency / resume / reopen conditions
temporal qualifiers
rejected rationale whose retention prevents rediscovery
source/provenance links
other view-specific must-preserve units
```

The candidate synthesis must map every manifest unit to one of:

```text
PRESERVED_DIRECTLY
PRESERVED_BY_SYNTHESIS_AT <location>
INTENTIONALLY_LATENT_WITH_RECOVERABLE_SOURCE <source>
NOT_APPLICABLE_WITH_REASON
```

Missing coverage blocks high-consequence promotion. Structured units are checked deterministically. Unstructured semantic units require source-grounded independent verification or human review proportional to consequence.

This closes the design-level mechanism gap behind Claude's KA-R17 concern while leaving empirical fidelity qualification pending.

## 6. Derived current state is split into deterministic core and derived narrative

Claude is correct that today's `CURRENT_STATE.md` contains editorial judgment that cannot honestly be called a purely deterministic materialized view.

Candidate 01 is refined so the future current-state surface has two semantic layers:

```text
CURRENT-STATE CORE
    deterministic projection of canonical workstream, authority, route, freshness,
    unresolved-risk and qualification facts

ORIENTATION NARRATIVE
    optional derived synthesis over canonical sources
    explicitly non-authoritative as a source of unique project truth
    carries provenance/freshness and must-preserve fidelity contract
```

If narrative generation discovers a new conclusion, that conclusion becomes a capture candidate and must be promoted to a canonical source before later current-state views may rely on it as accepted truth.

If narrative fidelity cannot be established, the safe degraded output is the deterministic core plus source links, not a stale or silently authoritative narrative.

## 7. Routine refresh versus full rebuild

Claude's scaling concern is valid, but its downgrade of KA-R31 and KA-I12 overstates what those requirements demand. Requirements V0.2 explicitly bind **required reconstruction cost** to sublinear historical growth and explicitly allow periodic automated global rebuild under KA-R33.

Candidate 01 therefore makes this distinction explicit:

```text
ordinary local change
    dependency-aware incremental refresh of affected persistent structural views

normal reconstruction
    bounded materialized/current views; no whole-history rescan

periodic repair / qualification / migration
    automated full rebuild may scan the complete authoritative history
```

A source-to-derived dependency index is itself generated from source declarations and generator contracts. Full rebuild cost is measured because it matters economically, but linear full-rebuild cost does not by itself violate KA-R31/KA-I12.

Disposition:

```text
KA-R31  remains DESIGN_COVERED
KA-I12  remains DESIGN_COVERED
KA-R33  receives a sharper incremental-refresh mechanism and remains qualification-pending
```

## 8. Identity lookup boundedness

Claude's identity-index concern is useful but belongs to the interaction between KA-R46 and scale/rebuild economics rather than showing that representation-independent identity is undesigned.

Candidate 01 now requires:

```text
normal identity lookup
    query generated current-target identity index directly
    never scan historical tombstones on the normal path

identity transition chain
    preserve complete authoritative transition history
    generated index materializes current target / split successors
    cycle and dangling-target validation required

full rebuild
    may scan all identity transitions and flatten/resolve chains into the current index
```

Thus historical identity-transition volume may grow, while ordinary identity resolution remains bounded by the current index.

Disposition:

```text
KA-R46 remains DESIGN_COVERED
identity lookup/rebuild behavior becomes explicit qualification material
```

## 9. Paused-workstream salience

Claude's Cockpit example exposes a real active-surface issue. `PAUSED` must not mean "always load forever."

Candidate 01 now distinguishes durable workstream state from bootstrap salience:

```text
PAUSED workstream
    remains durably queryable and keeps pause reason / return condition / parent / target

mandatory ordinary bootstrap
    includes it only when its parent/task intersects it, its return condition is satisfied,
    an explicit review trigger is due, or another governed rule activates it

otherwise
    it remains behind a generated paused-workstream view and does not occupy the mandatory
    active-route payload
```

An optional `review_after` or equivalent trigger is allowed when the return condition cannot be machine-observed. This is not a new lifecycle state.

## 10. Capture backlog is a saturation signal

Candidate 01's falsification and consolidation rules are amended to include the opposite capture failure mode identified by Claude.

Observe at least:

```text
unreviewed capture count
oldest unreviewed capture age
high-consequence capture backlog
capture accumulation by workstream/subject
promotion / retirement throughput
captures repeatedly retrieved but never resolved
```

Capture backlog pressure is a valid consolidation/review trigger. No backlog metric may auto-promote candidate knowledge into authority.

## 11. Rollback becomes a concrete export-and-switch mechanism

Claude is correct that "rollback proof" was under-specified. The most direct frozen requirement affected is KA-R44, while KA-R43 primarily governs semantic preservation during migration.

Candidate 01 now requires a **rollback exporter** before authority switch:

```text
before M7
    successor canonical state -> legacy-compatible authority representations
    must be generatable for every current/migration-critical accepted fact
    parity and integrity checks must pass

post-switch stabilization window
    successor remains the only write authority
    legacy-compatible surfaces are regenerated from successor state
    no dual-authority writes

rollback
    freeze authoritative writes
    regenerate legacy authority surfaces from the exact successor head
    run semantic parity + repository integrity
    explicitly switch authority back only after successful validation
```

If accepted successor semantics cannot be represented in the legacy architecture without material loss, M7 is forbidden until a lossless fallback representation or retention bridge exists. Git history alone is not treated as sufficient rollback for post-switch work.

This closes the design-level rollback mechanism while leaving real rollback qualification pending.

## 12. Complexity growth as H3 reopening evidence

Claude is right that Candidate 01 already has meaningful profile breadth. The exact number `10` is not frozen as an architectural law, but complexity growth is now explicitly measured:

```text
active profile-type count
profile-type growth over implementation rounds
identity-transition object count
joint-authority object count
special semantic-object count / canonical-source count
schema migration fan-out when a profile changes
```

H3/Object-Primary should reopen if the selective profile system converges toward a general object substrate in both breadth and maintenance mechanics and an object-primary representation demonstrably simplifies the same hard cases without unacceptable migration/capture/inspectability cost.

## 13. Coverage disposition relative to Claude's 43/50 + 16/17 result

Claude's exact-target review is preserved as valid evidence. At the reviewed commit, several mechanisms were genuinely under-specified. Its requirement-level downgrade, however, mixes three different questions:

```text
requirement semantic coverage
candidate internal design completeness
scaling/qualification behavior
```

The task-owner disposition is:

```text
KA-R09   ACCEPT PARTIAL AT REVIEW TARGET
          amended by sole-normative contract rule + assurance ladder

KA-R14   KEEP DESIGN_COVERED
          ordinary replacement/supplement/conflict semantics were present;
          JOINT_AUTHORITY governance is a candidate defect fixed separately

KA-R17   ACCEPT PARTIAL AT REVIEW TARGET
          amended by must-preserve manifest + coverage verification

KA-R31   KEEP DESIGN_COVERED
          Claude conflated required reconstruction with periodic full-rebuild cost;
          routine incremental refresh is nevertheless added under KA-R33 economics

KA-R43   KEEP DESIGN_COVERED
          forward migration preservation was specified;
          rollback belongs primarily to KA-R44

KA-R44   PARTIAL AT REVIEW TARGET (new calibrated assignment)
          now amended by rollback exporter / explicit reverse switch

KA-R46   KEEP DESIGN_COVERED
          identity continuity semantics were present;
          bounded current lookup is now made explicit as a scale/index refinement

KA-I12   KEEP DESIGN_COVERED
          same reconstruction-versus-rebuild calibration as KA-R31
```

After the amendments in this record and Research 144, the task-owner working position returns Candidate 01 to **50/50 KA-R and 17/17 KA-I design-covered**, while all remain qualification-pending. This renewed full mapping is itself still reviewable and is not a qualified pass.

## 14. Why one more Claude turn is worthwhile

Claude explicitly requested one short follow-up if ChatGPT supplied concrete answers to the two most architecture-sensitive findings:

```text
B  prose/structured-contract normative precedence
D  non-circular JOINT_AUTHORITY admission/governance
```

Those answers now exist. A second broad review would have low marginal value. One narrow Message 003 is warranted to test only whether these two amendments actually close the defects or merely restate them more precisely.

The follow-up may additionally flag a material error in the requirement-scope calibration above, but it should not reopen every prototype-phase issue.

```text
RESEARCH146=MC0016_MESSAGE001_RECONCILED
CANDIDATE_01=AMENDED
REQUIREMENTS_V02=UNCHANGED_FROZEN
TASK_OWNER_DESIGN_MAPPING=50_KA_R__17_KA_I
FINAL_QUALIFIED_PASSES=0
MC0016_MESSAGE003=NARROW_FOLLOWUP_WARRANTED
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=CLAUDE_REVIEW_OF_PRECEDENCE_AND_JOINT_AUTHORITY_AMENDMENTS
```
