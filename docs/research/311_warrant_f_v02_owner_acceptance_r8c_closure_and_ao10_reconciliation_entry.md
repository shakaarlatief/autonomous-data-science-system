# Research 311: WARRANT-F V0.2 Owner Acceptance, R8-C Closure, and AO-10 Reconciliation Entry

**Date:** 2026-09-24
**Status:** R8-C ASSURANCE ARCHITECTURE ACCEPTED / WARRANT-F V0.2 ACCEPTED / R8-A ENGINEERING AMENDMENT ACCEPTED / MC-0028 RESOLVED / SPECIFICATION 028 RECONCILIATION AND AO-10 DESIGN UNBLOCKED / NO PHYSICAL MIGRATION
**Parent program:** Research 240 whole-repository architecture evolution
**Assurance requirements:** Research 273
**Independent designs:** Research 274 FACET / MC-0028 Message 001 WARRANT
**Comparative synthesis:** Research 275 WARRANT-F V0.1
**Final reconciled candidate:** Research 276 WARRANT-F V0.2
**Decision-relevant probe protocol:** Research 277
**Probe reconciliation:** Research 308
**Whole-system clarifications:** Research 309 and Research 310
**Owner decision:** ACCEPT
**Repository base before acceptance:** 78b3e7f2d88e1ab6b51a9dfb85cfdc604d6c074c
**Scope:** Record the project owner's explicit acceptance of WARRANT-F V0.2 as the R8-C semantic assurance architecture, accept the carried R8-A Engineering-environment amendment, resolve MC-0028, preserve all empirical limitations and downstream obligations, and move the project to Specification 028 reconciliation plus concrete AO-10 realization design without authorizing physical migration or authority switch.

## 1. Owner decision

The project owner explicitly chose:

    I ACCEPT.

This accepts WARRANT-F V0.2 as the target R8-C semantic assurance architecture direction.

The decision follows the completed empirical program:

    decision-relevant probes      8 / 8 reconciled
    PASS                          7
    scoped INCONCLUSIVE           1 / P-H only
    unresolved AMEND              0
    active HARNESS_INVALID        0

The evidence-based recommendation in Research 308 was ACCEPT.

The owner has now made that decision.

## 2. Accepted assurance architecture

The accepted semantic architecture includes the reconciled Research 276 rules WF-A1 through WF-A36.

Its core primitives remain:

    CLAIM
    VERIFIER
    WARRANT
    GATE POLICY
    PROFILE
    EVIDENCE
    DECISION
    PLANNER

The architecture accepts, among other things:

    selective first-class assurance claims rather than one claim per test
    explicit warrants for why verifiers are decision-relevant
    executable sensitivity/specificity evidence where warranted
    exact subject and revision binding
    freshness and provenance requirements
    base-revision assurance-policy ratchet
    explicit trust semantics
    executor capability modeling
    execution-surface / trust separation
    provider and workflow mechanism freedom
    consumer-side result adaptation
    exact-result promotion semantics
    non-self-mutating decision evidence
    oracle-retirement qualification
    deterministic and stochastic assurance separation
    preregistered stochastic decision-grade campaigns
    public-development / private-held-out stochastic evidence separation
    no retry-to-green
    profile composition without profile ownership of consequence semantics
    selective retention of decision-grade evidence and cited attempts
    assurance / orchestration / delivery separation

## 3. Accepted-state semantics remain mechanism-neutral

Acceptance does not make any current Git branch or workflow the permanent target.

Accepted state remains a semantic exact-subject role.

The target architecture does not currently select:

    branch model
    pull-request model
    merge queue
    direct-push policy
    GitHub Actions
    CI provider
    runner provider
    host-protection mechanism
    identity provider
    status/check publisher
    exact Python test framework
    exact evidence store
    deployment provider
    release topology
    current current_routing / CURRENT_STATE carrier design
    current repository-integrity aggregate implementation

Those remain concrete realization questions.

Current mechanisms may remain migration constraints, evidence, compatibility obligations or temporary bridges. They have no preservation right merely because they are current.

## 4. Accepted assurance / AO / delivery boundary

Research 309 and Research 310 clarify the composition but do not expand the semantic acceptance beyond the candidate.

The accepted integration direction is:

    AO / JW1
        determine project process, governing transitions and lifecycle routing

    WARRANT-F
        determines whether an exact consequence is admissible under the applicable assurance policy

    Engineering / Delivery
        performs governed mutation only after the required control and assurance decisions exist

Assurance decisions can re-enter AO as project events.

AO may activate assurance when a transition requires an assurance profile.

Neither subsystem silently absorbs the other.

## 5. R8-A Engineering environment amendment is now accepted

Research 276 carried one prospective amendment to the previously accepted R8-A target.

The owner ACCEPT decision now accepts that amendment.

Target direction:

    project/engineering/
        independently resolved Python project
        independent lock

with these constraints:

    Product and JW1 are not co-installed into Engineering merely to run assurance
    JW1 is invoked through a CLI/result contract rather than a path dependency
    assurance-kernel runtime dependencies remain deliberately small
    one Engineering-owned bootstrap entry prepares the required environments
    a root Python project is removed unless an independently justified repository-wide runtime remains

This is an architectural target amendment only.

No file move, package split, lockfile replacement, root-project deletion or environment migration is authorized by this acceptance record.

## 6. Empirical limitations remain binding

Acceptance does not erase the limitations of the probe program.

### P-H current host capability

P-H remains scoped INCONCLUSIVE.

Therefore:

    CURRENT_GITHUB_T2_CAPABILITY=UNKNOWN
    TARGET_PROVIDER_SELECTED=false
    HOST_OR_PROVIDER_QUALIFICATION_REQUIRED_BEFORE_DEPENDENT_CUTOVER=true

GitHub and current Git-host mechanisms are neither selected nor rejected as the target by this result.

### P-D4 current oracle succession

P-D4 established that the current routing invariants can survive representation change.

It did not authorize immediate retirement of the current routing oracle.

Therefore:

    CURRENT_ROUTING_ORACLE=RETAIN_AS_MIGRATION_ORACLE

until:

    production successor exists
    translated semantics are implemented
    shadow qualification passes
    explicit release/retirement decision occurs

### P-S stochastic qualification

The historical Prototype V0 evidence contains only two independent item clusters.

Therefore:

    CURRENT_PROTOTYPE_STOCHASTIC_BLOCK_STATUS=OBSERVE_ONLY

Decision-grade stochastic BLOCK use must follow the accepted preregistered item-cluster design and public/private item separation.

The preserved conservative feasibility result remains:

    J = 29 independent items
    R = 2 paired repeats
    116 total candidate + baseline treatment executions

for the frozen MDE 0.10, tau=2*sigma feasibility discriminator.

This is a feasibility result, not an order to run that campaign immediately.

## 7. Realization-stage qualification remains downstream

Acceptance of semantic architecture is not production qualification.

Concrete realization must still qualify at least:

    gate evaluator behavior for missing / stale / contradictory evidence
    affected-scope fallback
    exact-result promotion realization
    artifact provenance
    non-self-mutating evidence-store realization
    provider-adapter semantics
    assurance-kernel mutation testing
    deployment / recovery implementation evidence

If those probes expose a semantic architecture defect, AO-4 remains available for KEEP / CLARIFY / AMEND / SUPERSEDE / REOPEN.

## 8. Specification 028 remains current until reconciled

Specification 028 is not silently amended by this owner acceptance.

It remains the current implementation/migration authority until a governed reconciliation produces accepted prospective changes.

R8-A, R8-B and R8-C now create explicit reconciliation obligations against Specification 028.

The next stage must determine which current clauses are:

    RETAIN
    GENERALIZE
    AMEND
    SUPERSEDE
    RETIRE_AFTER_SUCCESSOR_QUALIFICATION

The reconciliation must include architecture, representation, assurance, control-evidence, environment, provider-neutrality, migration-oracle and authority-transition implications.

## 9. AO-10 status after acceptance

The R8-C owner-decision blocker is now removed.

AO-10 is therefore:

    UNBLOCKED_FOR_RECONCILIATION_AND_DESIGN

It is not yet:

    AUTHORIZED_FOR_UNBOUNDED_PRODUCTION_IMPLEMENTATION
    AUTHORIZED_FOR_PHYSICAL_MIGRATION
    AUTHORIZED_FOR_AUTHORITY_SWITCH

The immediate AO-10 work is to derive the concrete realization from the accepted R5-R8 architecture and reconcile affected Specification 028 contracts before implementation proceeds beyond appropriately bounded qualification work.

## 10. Whole-architecture self-improvement remains active

Acceptance does not make WARRANT-F V0.2 immutable.

Research 310's controlled self-improvement clarification remains applicable:

    operation / implementation / assurance / owner observation
        ->
    evidence or architecture pressure
        ->
    AO-3 activation
        ->
    AO-4 EvolutionCase
        ->
    CONFORMANCE_DEFECT / KEEP / CLARIFY / AMEND / SUPERSEDE / REOPEN
        ->
    owner decision where normative
        ->
    prospective realization
        ->
    WARRANT-F qualification
        ->
    AO activation

Therefore:

    ACCEPTED
        !=
    FOREVER UNCHANGEABLE

and:

    TARGET ARCHITECTURE
        !=
    CURRENT IMPLEMENTATION MECHANISM

## 11. Future general public architecture vision remains preserved

Research 309 remains a preserved long-term direction.

The professional domain-independent architecture/reference implementation is not extracted now.

ADS remains the primary real implementation, migration, operation and falsification ground from which the genuinely reusable core should later be derived.

R8-C acceptance strengthens that future candidate by adding a qualified assurance/admission architecture that composes with activation/orchestration rather than replacing it.

## 12. MC-0028 closure

MC-0028 is resolved.

Its sequence is now complete:

    Claude independent WARRANT              COMPLETE
    ChatGPT independent FACET               COMPLETE
    comparative WARRANT-F V0.1              COMPLETE
    Claude comparative critique             COMPLETE / AMEND
    ChatGPT WARRANT-F V0.2 reconciliation   COMPLETE
    decision-relevant probe program         COMPLETE
    owner decision                          COMPLETE / ACCEPT

No active Claude obligation remains from MC-0028.

A later independent review may be opened if the concrete AO-10 realization or Specification 028 reconciliation reaches a consequence level where independent review is valuable, but that would be a new governed obligation rather than continuation of MC-0028.

## 13. Still not authorized

This acceptance does not authorize:

    file-level migration
    physical repository migration
    operational authority switch
    current-oracle retirement
    provider/host selection by inheritance
    deployment/cutover
    broad production AO-10 implementation without reconciliation
    general-framework extraction
    silent Specification 028 amendment

## 14. Current state

    R8C=ACCEPTED
    WARRANT_F_V0_2=ACCEPTED
    OWNER_ASSURANCE_DECISION=ACCEPT

    WF_A1_TO_A36=ACCEPTED
    R8A_ENGINEERING_ENVIRONMENT_AMENDMENT=ACCEPTED
    MC0028=RESOLVED

    PROVIDER_WORKFLOW_MECHANISM_FREEDOM=PRESERVED
    ACCEPTED_STATE=SEMANTIC_EXACT_SUBJECT_ROLE
    CURRENT_MECHANISM_PRESERVATION_RIGHT=false

    P_H=SCOPED_INCONCLUSIVE
    PROVIDER_HOST_QUALIFICATION=DOWNSTREAM_REQUIRED

    P_D4=PASS
    CURRENT_ROUTING_ORACLE=RETAIN_UNTIL_QUALIFIED_SUCCESSOR_RELEASE

    P_S=PASS
    CURRENT_PROTOTYPE_DECISION_GRADE_BLOCK=OBSERVE_ONLY

    SPECIFICATION028=UNCHANGED_PENDING_RECONCILIATION
    AO10=UNBLOCKED_FOR_RECONCILIATION_AND_DESIGN
    AO10_PRODUCTION_IMPLEMENTATION_AUTHORIZED=false

    FILE_LEVEL_MIGRATION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    AUTHORITY_SWITCH_ALLOWED=false

    NEXT=SPECIFICATION028_RECONCILIATION_AND_AO10_REALIZATION_DESIGN
