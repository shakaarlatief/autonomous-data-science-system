# Research 437: DRP-03 successor requirements decomposition and first-principles candidate families V0.1

**Date:** 2026-10-02
**Status:** CHATGPT INITIAL DESIGN FROZEN / PUBLIC-EVIDENCE ONLY / MULTIPLE CANDIDATE FAMILIES / NO SELECTION / CLAUDE COUNTER-DESIGN NEXT
**Parent:** Research 436 / Research 435 / Research 315
**Scope:** Perform the first public-evidence-only requirements/failure decomposition required by Research 436, separate actual Project-system needs from inherited DRP-03 implementation assumptions, and freeze materially different successor semantic architecture families before independent/adversarial Claude review.
**Authority:** Initial design research only. This record does not select a successor architecture, expose hidden R2 semantic details, authorize a semantic pilot, modify the frozen R2 result, resume dependent DRPs, implement AO-10, amend Specification 028, migrate repository state, retire an oracle, or switch authority.

## 1. Evidence boundary

This record intentionally does not inspect:

    Key A hidden semantic bytes
    Key B hidden semantic bytes
    hidden R2 disagreement item identities
    hidden grouping pairs
    hidden STATE answers
    hidden private precedents
    private R2 comparison details beyond the public-safe aggregate projection

Inputs are limited to public durable evidence including:

    Research 315 Integrated Project-System V0.3
    Research 318 DRP-09 PASS
    Research 320 DRP-05a PASS / DRP-05b PASS_DETECTIVE_FIRST
    Research 323 DRP-01 PASS
    Research 326 / 327 DRP-03 R1 result and prospective redesign
    Research 330 R2 V0.3 protocol
    Research 435 R2 construct-underdetermined aggregate result
    Research 436 owner route
    Specification 028 and its current temporal authority

No hidden cause is inferred from an aggregate disagreement count.

## 2. Start from operational questions, not ontology preservation

The Project system does not intrinsically need the current DRP-03 fields.

It needs reliable answers to consequential operational questions.

A minimum problem statement is:

1. **Authority:** What governing decision, policy, specification, acceptance, deferral or transition is currently applicable to the exact subject/revision?
2. **Normative consequence:** What does that governing change require, prohibit, constrain, permit, sequence, defer, supersede or otherwise cause?
3. **Action admissibility:** Given the intended ActionShape and consequence, what conditions must hold before advancement or admission?
4. **Realization:** What source-owned facts show that a required effect/control/capability exists?
5. **Evidence and qualification:** What evidence, assurance claims, qualification decisions and activation receipts are required, and who owns those requirements?
6. **Temporal state:** Which facts are current, stale, superseded, deferred or scope-qualified?
7. **Transition safety:** What must survive migration, cutover, rollback, compatibility or authority replacement?
8. **Reconstruction:** Can a future collaborator/system reconstruct the above without silently inventing authority?
9. **Economics:** Can normal project work maintain the required semantics without creating a bypass incentive or a second hand-maintained requirements database?
10. **Failure visibility:** When meaning is genuinely unresolved, can the system expose review rather than fabricate a machine-authoritative answer?

These questions are requirements.

A canonical `ObligationUnit`, one five-way normative kind, or one realization-state enum are possible answers, not requirements.

## 3. Evidence-backed architectural constraints

The following constraints currently have independent empirical or accepted architectural support.

### RQ-1: minimal shared semantics, not a universal Project type system

DRP-01 supports a bounded shared substrate around:

    semantic_identity
    exact_subject_revision_binding
    provenance_descriptor
    governing_lifecycle_reference
    obligation_reference
    governed_relation_reference

It simultaneously rejects domain-internal state as automatically shared.

Successor design should therefore justify every cross-domain semantic primitive by a real seam.

### RQ-2: path and carrier shape are not authority

DRP-01 and the accepted project-knowledge architecture preserve:

    path != identity
    path != authority
    carrier location != unique semantic ownership

Any successor must bind consequential meaning to exact semantic subject/revision and provenance, not infer authority from location or recency.

### RQ-3: structured action consequences should be deterministic where possible

DRP-05a supports provider-neutral deterministic ActionShape normalization for the tested real Git-centered corpus.

Successor semantics should prefer deterministic normalization for effect classes that can be mechanically represented and route unsupported shapes to review rather than use unconstrained model inference.

### RQ-4: current AO reality is detective-first

DRP-05b found:

    MEDIATED      0
    COOPERATIVE  53
    UNMEDIATED   12

The semantic design must not depend on a universal preventive interception path.

A valid owner/governance act remains temporally valid even if Project-system bookkeeping is incomplete. Missing structured semantics may block dependent accepted-state advancement where policy permits, but bookkeeping does not outrank owner authority.

### RQ-5: assurance policy owns assurance requirements

DRP-09 supports the separation:

    AO provides subject/consequence/context
    WARRANT-F/effective policy derives mandatory claims

Semantic obligation machinery must not silently absorb assurance policy authority.

### RQ-6: retrospective free-form obligation reconstruction is not authoritative

DRP-03 R1 established broad disagreement in proposition selection and unit grouping.

The accepted source remains authority. Retrospective model extraction may support review/migration but cannot silently mint authoritative obligation meaning.

### RQ-7: natural-owner facts and derived projections remain the preferred direction

R1's simple deterministic state fixtures and the broader WMR-H architecture support source-owned realization/evidence/qualification/activation facts with generated state views rather than hand-maintained copied statuses.

R2's later STATE disagreement means the current fact-validity/state contract is not sufficiently determined. It does not by itself falsify the broader "source facts -> derived view" principle.

### RQ-8: adoption economics is a correctness constraint

Research 315 already requires machine/control metadata to be generated, natural-event authored, or consequentially justified.

Any successor that is semantically elegant but routinely too costly to author, review or repair is not a successful architecture.

### RQ-9: transition and lineage requirements remain real

Specification 028 remains current authority. Accepted R8/AO work requires authority-preserving migration, compatibility, rollback/recovery, exact lineage and explicit cutover semantics.

A successor semantic model must support these operational needs or show that another architecture owns them better.

## 4. Inherited DRP-03 assumptions that are not requirements

The following have no preservation right:

    one canonical ObligationUnit as the central machine unit
    a mandatory binary normative/non-normative first decision
    exactly five mutually exclusive normative kinds
    materiality as one authored boolean
    realization_required as one authored boolean
    MUST_JOIN / MUST_SPLIT as canonical unitization truth
    one canonical partition of related normative meaning
    one global realization-state enum
    DEFERRED as a member of the same state axis as realization progression
    one zero-context fresh-author reproducibility claim
    LLM semantic authors as the authority source
    a single central obligation domain that owns all normative semantics

They may survive later evidence. They are not assumed.

## 5. Public failure decomposition

### 5.1 R1

R1 showed that free-form retrospective reconstruction from accepted prose was not sufficiently reproducible.

Public evidence:

    proposition-set F1   0.4983
    grouping F1          0.6753
    state agreement      0.4521 on matched propositions

This motivated stable item IDs, proposal-time birth and stronger state rules.

### 5.2 R2

R2 removed much of the R1 paraphrase problem and strengthened the protocol, but the construct still failed.

Public aggregate evidence:

    binary normativity kappa              0.774540330104 < 0.80
    normative positive specific agreement 0.865209471767 >= 0.80
    normative-kind kappa                  0.502907383797 < 0.75
    material positive specific agreement  0.841737393909 < 0.90
    grouping-constraint agreement         0.068333333333 < 0.80
    ambiguity                             0.104333868379 > 0.10
    STATE exact structural agreement      18 / 24
    STATE fact-validity disagreement      1 fixture
    STATE final-state disagreement        5 fixtures

Interpretation is deliberately limited.

We can say:

    the current combined construct is not sufficiently determined

We cannot say from public aggregates alone:

    which author is right
    which hidden items are wrong
    which exact taxonomy boundary caused a disagreement
    which exact grouping rule failed in practice
    which exact STATE fixture rule needs repair

### 5.3 Structural design concern

The current construct asks semantic authors to solve several distinct problems at once:

    detect normative meaning
    assign semantic consequence kind
    judge materiality
    decide realization requirement
    infer aggregation/grouping
    validate realization/deferral/evidence facts
    collapse valid facts into one state

A failure in any upstream judgment can propagate into downstream judgments.

The successor should therefore test whether some of these responsibilities can be:

    separated
    made orthogonal
    authored explicitly
    moved to natural owners
    derived mechanically
    represented as relations instead of categories
    removed when no operational decision requires them

This is a design hypothesis, not an R2 item-level diagnosis.

## 6. Design axes

Candidate architectures can be compared along independent axes.

### AX-1: authority birth

    retrospective inference
    proposal-time model draft
    proposal-time structured authoring
    owner/governance acceptance of text + semantic declaration
    domain-native acceptance with only shared references

### AX-2: semantic representation

    exclusive category
    orthogonal dimensions
    typed relations
    executable control contract
    domain-native semantics

### AX-3: aggregation

    canonical ObligationUnit
    optional named unit
    relation-connected atomic clauses
    no grouping at all

### AX-4: operational state

    one state enum
    orthogonal predicates/facts
    context-specific derived views
    no global realization state

### AX-5: LLM role

    authoritative interpreter
    candidate drafter
    calibrated/qualified semantic author
    independent verifier
    ambiguity resolver
    advisory detector only
    no LLM on the authoritative path

### AX-6: domain ownership

    central obligation subsystem
    thin shared normative substrate + bounded domain models
    domain-native contracts composed by AO
    generated cross-domain control projection

These axes should be evaluated by operational sufficiency and evidence, not aesthetic preference.

## 7. Candidate family A: strengthened declaration-unit model

This is the conservative comparator.

Retain:

    AcceptanceDeclarationSet
    normative selection
    five-way normative-kind taxonomy
    realization-required subset
    ObligationUnits
    natural-owner realization facts
    derived state

Strengthen development/operation with:

    explicit worked examples
    positive and negative examples
    boundary examples
    decision tables
    author qualification/calibration
    short real inter-author pilots before scaling
    explicit disagreement-review workflow

Potential advantage:

    lowest conceptual change
    preserves much of existing AO-10 candidate work

Primary risk:

    the ontology itself may be underdetermined, so better instructions may only train authors to imitate examples rather than make the semantics intrinsically stable

Cheap falsifier:

    a small development pilot deliberately concentrated on normative-kind and grouping boundary cases after a finite calibration package

If agreement remains poor after principled calibration, do not scale this family.

## 8. Candidate family B: normative atoms with orthogonal dimensions

Replace one mutually exclusive `normative_kind` with a small set of independent properties on accepted addressable semantic atoms.

Illustrative dimensions, not frozen fields:

    authority_effect
        none / creates / amends / supersedes / retires / permits

    realization_mode
        self_effecting / external_realization_required / standing_enforcement

    ordering_effect
        none / prerequisite / hold / sequence / cutover_gate

    operational_scope
        subject / transition / action class / workstream / policy scope

    evidence_requirement
        none / evidence / qualification / activation / policy-derived

    blocking_effect
        none / advisory / review / prevents_admission_when_enforceable

A semantic atom may express multiple dimensions without being forced into one category.

Potential advantage:

    separates concepts currently compressed into one five-way choice
    supports deterministic operational projection from explicit dimensions

Primary risk:

    dimensional explosion and higher authoring burden
    dimensions may still hide ambiguous boundaries

Cheap falsifier:

    compare exclusive-kind classification against orthogonal-dimension classification on the same difficult development atoms and measure both agreement and operational information sufficiency

## 9. Candidate family C: relation-first normative consequence graph

Retain mechanically addressable accepted semantic atoms but eliminate canonical `ObligationUnit` grouping as a required truth.

Represent consequence through typed relations such as:

    REQUIRES_EFFECT
    CONSTRAINS
    PRECEDES
    GATES
    DISPOSITIONS
    SUPERSEDES
    REALIZED_BY
    EVIDENCED_BY
    QUALIFIED_BY
    ACTIVATED_BY
    DEFERRED_BY

The exact relation vocabulary is not selected here.

Multiple clauses may point to the same effect/control without being declared "one obligation".

One clause may participate in several relations when operationally justified.

Potential advantage:

    directly attacks the 6.8% grouping-constraint problem by asking whether canonical grouping is needed at all
    preserves polyhierarchy and avoids forcing one partition onto multi-role semantics

Primary risk:

    relation selection may simply move the ambiguity from grouping into edge typing
    graph complexity may hurt adoption economics

Cheap falsifier:

    take difficult multi-clause real development cases and ask whether independent authors can produce relations that answer the required AO questions more reproducibly than MUST_JOIN/MUST_SPLIT while using equal or lower authoring effort

## 10. Candidate family D: minimal operational control contract

Reduce the machine-authoritative semantic surface to only the facts needed for consequential control.

Example control primitives:

    exact governed subject/revision
    authority event
    applicability/scope
    explicit prerequisite
    explicit prohibition/permission
    explicit hold/deferral
    required external effect/control
    required evidence/qualification reference
    transition/cutover condition
    explicit waiver/override authority

Rich accepted prose, principles and rationale remain authoritative human Project knowledge.

An LLM may scan them for suspected omissions, but its interpretation is:

    REVIEW / CONTROL_OBSERVATION

not machine authority.

Potential advantage:

    minimizes semantic discretion and metadata
    aligns with DRP-09's policy ownership and DRP-05's deterministic-control preference

Primary risk:

    the core may be too small to support lineage, reconstruction or nuanced future governance
    important normative meaning may remain unstructured until too late

Cheap falsifier:

    replay a bounded set of real consequential decisions/actions and test whether every required AO admission/reconstruction question can be answered from the minimal contract without reaching back into unconstrained prose interpretation

## 11. Candidate family E: domain-native contracts with shared references

Remove the general obligation subsystem as a primary semantic owner.

Examples:

    WARRANT-F owns assurance requirements
    transition architecture owns cutover/rollback gates
    workstream engine owns work dependencies
    authority/lifecycle model owns supersession/acceptance
    specification contract owns normative specification clauses
    AO composes these through shared semantic references

The shared substrate may retain:

    obligation_reference
    governed_relation_reference

as cross-domain handles without requiring one universal obligation ontology.

Potential advantage:

    follows DRP-01's minimal-shared-substrate evidence
    keeps semantics close to natural owners
    avoids forcing unlike normative concepts into one lifecycle

Primary risk:

    cross-domain orchestration may fragment
    AO may need a common query contract that recreates the obligation model indirectly

Cheap falsifier:

    define a small set of cross-domain AO queries and test whether domain-native contracts can answer them through a thin shared interface without semantic duplication or special-case branching

## 12. Candidate family F: accepted semantic atoms plus generated operational projection

This family separates authoritative meaning capture from operational orchestration.

At the governing event:

    accepted source text
        +
    minimal accepted semantic atoms/relations
        ->
    immutable accepted semantic declaration

From those accepted semantics and natural-owner facts:

    deterministic generator
        ->
    AO operational controls
    transition gates
    obligation/reference views
    realization predicates
    bounded current orientation

The generated projection is not additional authority.

LLMs may:

    draft candidate atoms/relations before acceptance
    explain consequences
    detect likely omissions
    flag unresolved ambiguity

but the authoritative structured semantics are those actually bound to the governing act.

Potential advantage:

    preserves explicit authority birth
    keeps AO operational data generated
    supports a small semantic source with multiple downstream views
    can combine the strongest parts of B, C, D and E

Primary risk:

    the accepted semantic atom/relation layer may still be too expensive or ambiguous to author
    generated operational logic may become complex enough to hide semantic policy

Cheap falsifier:

    small real proposal-to-acceptance replay measuring semantic authoring burden, inter-author reproducibility, generated-control determinism and ability to reconstruct the accepted consequence without prose-only inference

## 13. Families are not mutually exclusive

A strong successor may combine elements.

Examples:

    B + C
        orthogonal atom dimensions + typed relations

    C + F
        relation-first accepted semantics + generated AO projection

    D + E
        minimal cross-domain control interface over domain-native contracts

    B + C + D + F
        minimal accepted atoms/relations whose deterministic projection exposes only the operational controls AO needs

The purpose of the family freeze is to prevent premature convergence, not to create artificial mutually exclusive products.

## 14. Initial cross-family invariants

Unless later evidence reopens them, every candidate should preserve:

    exact semantic subject/revision binding
    provenance
    governing lifecycle separation
    owner/governance temporal authority
    no retrospective LLM inference silently becoming authority
    natural-owner source facts where facts have clear natural owners
    derived/generated views not treated as unique accepted truth
    policy-owned assurance requirements
    mediation-realistic control claims
    explicit unresolved/review behavior
    migration/recovery/lineage support appropriate to its claimed scope
    adoption-economics measurement
    development/confirmation evidence separation

These are not an attempt to freeze the whole target architecture. They are the currently supported constraints against which counter-design should argue explicitly if it wants to reopen one.

## 15. Progressive development probes worth considering after reconciliation

No probe is authorized yet.

The following are candidate cheap discriminators.

### SX-01: category-versus-dimensions discriminator

Question:

    Is the low normative-kind reproducibility primarily a consequence of one exclusive category choice?

Compare on difficult real development atoms:

    current five-way kind
    versus
    a small orthogonal-dimension candidate

Measure:

    inter-author agreement
    information sufficiency for downstream AO queries
    authoring effort
    ambiguity/review rate

### SX-02: grouping-versus-relations discriminator

Question:

    Is canonical unit grouping necessary?

Use difficult multi-clause cases.

Compare:

    MUST_JOIN / MUST_SPLIT
    versus
    typed effect/control relations without grouping

Measure:

    reproducibility
    operational query equivalence
    lost information
    authoring burden

### SX-03: state-enum-versus-predicates discriminator

Question:

    Does one realization-state enum introduce avoidable coupling?

Compare:

    single derived state
    versus
    orthogonal predicates such as has_realizer, evidence_valid, qualification_complete, activation_effective, deferral_valid, conflict_present

Then derive context-specific views mechanically.

Measure:

    exact derivation reproducibility
    ambiguity
    ability to answer AO decisions
    handling of multiple simultaneous truths

### SX-04: minimal-control sufficiency replay

Question:

    How little structured semantics does AO actually need?

Replay real consequential decisions/actions using only a minimal operational control contract.

Failure occurs if required admission, lineage, transition or reconstruction questions need unconstrained semantic reinterpretation.

### SX-05: author-contract discriminator

Question:

    What reproducibility property do we actually require from semantic authors?

Development-only comparison among:

    fresh zero-context author
    qualified/calibrated author with examples and counterexamples
    LLM candidate drafter + independent structured validator

The goal is not to make one model agree with itself. It is to determine which author contract is operationally legitimate and whether the architecture depends on training-like calibration.

## 16. Pilot design principle

When a pilot is later authorized, it should be:

    real enough to exercise the production semantic responsibility
    small enough to fail cheaply
    deliberately enriched with difficult boundary cases
    frozen before results
    explicitly development-only
    followed by direct inspection of disagreements
    allowed to change the candidate architecture
    incapable of serving as later untouched confirmation once inspected/tuned

Scale only if the smaller probe leaves a question that genuinely requires scale.

## 17. No initial selection

ChatGPT does not select A, B, C, D, E or F in this record.

A conservative repair remains in the design space because it may be sufficient.

A fundamental replacement remains equally available because the existing construct has no preservation right.

The strongest current direction cannot be chosen responsibly until an adversarial counter-designer challenges:

    whether the operational requirements are complete
    whether any "invariant" is actually inherited assumption
    whether candidate families omit a better architecture
    whether obligation semantics belong in AO at all
    whether relation-first semantics merely relocate subjectivity
    whether explicit authoring creates unacceptable governance burden
    whether the small-probe plan can discriminate candidates without overfitting

## 18. Next boundary

Research 437 is the frozen ChatGPT first-principles candidate-family record required by Research 436 S2.

The next actor is Claude for independent/adversarial counter-design.

Claude should receive:

    Research 436
    Research 437
    public Research 315 / 318 / 320 / 323 / 326 / 327 / 330 / 435
    Specification 028 as needed

Claude must not receive or seek hidden R2 semantic disagreement material.

    RESEARCH437=CHATGPT_INITIAL_CANDIDATE_FAMILIES_FROZEN
    SUCCESSOR_FAMILY_SELECTION=NONE
    HIDDEN_R2_DETAILS=UNSEEN
    PILOT_AUTHORIZED=false
    NEXT=CLAUDE_SUCCESSOR_CONSTRUCT_ADVERSARIAL_COUNTERDESIGN
