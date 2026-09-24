# Research 276: Owner Total-Architecture-Freedom Clarification and WARRANT-F V0.2 Reconciliation

**Date:** 2026-09-24
**Status:** OWNER DESIGN-FREEDOM CLARIFICATION ACCEPTED / CLAUDE MESSAGE 003 RECONCILED / WARRANT-F V0.2 CANDIDATE FROZEN / DECISION-RELEVANT PROBE DESIGN NEXT / NO OWNER ASSURANCE DECISION / NO PHYSICAL MIGRATION
**Parent requirements:** Research 273
**Independent candidates:** Research 274 FACET; MC-0028 Message 001 WARRANT
**Prior synthesis:** Research 275 WARRANT-F V0.1
**Comparative critique:** MC-0028 Message 003 / commit b6ac1d492216265e1351e420179d149928bffa8e
**Owner clarification:** no current architecture, workflow, collaboration procedure, branch model, test/CI/CD arrangement, execution surface, tool capability distribution, repository interaction pattern, or other implementation practice has preservation rights merely because ADS uses it today
**Candidate:** WARRANT-F V0.2
**Scope:** Record the owner's all-level design-freedom clarification, correct the current-versus-target ambiguity exposed by Message 003, reconcile Claude's 33 amendments, and freeze the target assurance architecture candidate before decision-relevant empirical probes.
**Authority:** Architecture candidate and design-freedom clarification only. This does not authorize physical migration, host-policy mutation, Specification 028 amendment, AO-10 implementation, branch-strategy cutover, or assurance implementation cutover.

## 1. Owner clarification: freedom applies at every level

The project owner clarified that the repeated redesign freedom is not limited to:

    files
    folders
    metadata
    representation
    tests
    CI/CD

It also applies to:

    repository workflow
    branch strategy
    push/pull/merge procedure
    PR versus direct-push procedure
    promotion procedure
    accepted-state carrier
    repository count/topology where not otherwise justified
    local versus remote execution
    hosted versus local runners
    Git-provider integration
    collaboration procedure
    model/agent execution surfaces
    tool and connector use
    release/deployment mechanics
    operational work practices

The governing rule is therefore:

> No current implementation, working procedure, host mechanism, tool surface, or collaboration habit has target-architecture preservation rights merely because it exists today.

This rule applies at every architecture layer unless a mechanism is independently justified by target requirements.

## 2. Accepted architecture is current authority, not immutable inheritance

The clarification does NOT erase prior accepted architecture decisions.

Accepted R5/R6/R7/R8-A/R8-B decisions remain the current design authority until explicitly amended.

But they are not metaphysically immutable.

If later evidence materially invalidates an accepted decision:

    use AO-4
        ->
    KEEP / CLARIFY / AMEND / SUPERSEDE / REOPEN

Therefore two ideas coexist:

    CURRENT MECHANISM
        has no preservation right

    ACCEPTED ARCHITECTURE
        remains governing until explicitly changed
        but may itself be changed through governed evidence/decision

This prevents both accidental inheritance and architecture anarchy.

## 3. Three layers must never be conflated

From this point forward every architecture discussion must distinguish:

### CURRENT OPERATING REALITY

What ADS happens to use now.

Examples:

    direct pushes to the coordination branch
    current branch names
    current GitHub workflows
    current local/remote tool surfaces
    current shared identities
    current Python environments

This is evidence and a migration constraint.

It is not the target merely because it is current.

### TRANSITION / MIGRATION BRIDGE

Temporary mechanisms needed because the target is not yet installed.

Examples:

    detective post-push assurance
    old/new shadow validators
    temporary compatibility readers
    current-oracle retention
    temporary branch-role mapping
    temporary local/host execution bridges

These mechanisms may disappear after cutover.

### TARGET ARCHITECTURE

The architecture selected from requirements and evidence without current-mechanism preservation bias.

It may use:

    a different branch model
    a different promotion model
    a different CI provider
    different identities
    different repository workflow
    different execution surfaces
    different test organization
    different tooling

The target may be stronger than the transition system.

## 4. Reinterpretation of Claude X1

Claude correctly found that Research 275's preventive G2 language implicitly assumed a workflow ADS does not currently use.

That is a real defect in the transition story.

It is NOT evidence that the target must preserve today's direct-push workflow.

Therefore Message 003 X1 is reconciled as follows:

    current direct-push reality
        -> requires an explicit transition bridge if it remains during migration

    target accepted-state advancement
        -> remains free to use a stronger preventive admission model

    current branch names
        -> do not become semantic architecture

    current lack of branch protection
        -> does not limit the target

## 5. Generalize branch role into accepted-state subject role

Message 003 WF-A29 says gate subjects should be defined by JW1 branch role.

That is still one level too physical under the owner's clarification.

WARRANT-F V0.2 generalizes it to:

    ACCEPTED_STATE SUBJECT ROLE

An accepted-state subject is the exact repository/version-control subject that currently carries the governed accepted project state.

A concrete realization may be:

    Git branch
    protected branch
    merge-queue result
    content-addressed commit/ref
    promoted integration ref
    another version-control mechanism justified later

The assurance architecture depends on the semantic role and exact subject identity, not on a permanent branch name or branch workflow.

Current branch-role mapping is one provider realization.

## 6. Preventive target, detective bridge

The target architecture keeps preventive admission as the stronger default:

    candidate subject
        ->
    assurance gate
        ->
    ADMIT / REFUSE / REVIEW_REQUIRED
        ->
    accepted-state advancement

But while current ADS operating mechanics permit direct advancement without pre-admission enforcement:

    accepted-state subject advances
        ->
    immediate equivalent post-admission qualification
        ->
    SATISFIED
        or
    QUARANTINED

This detective mode is:

    TRANSITION_BRIDGE=true
    TARGET_REQUIREMENT=false

unless later evidence independently justifies retaining it as defense in depth.

It must never be presented as equivalent to prevention.

## 7. Execution-surface and agent capability neutrality

The owner's side note about ChatGPT, Claude, Codex, Claude Code and local/Git-host access is relevant at the realization layer.

Different collaborators/executors can have different capabilities.

For example, depending on the active environment:

    local filesystem/process access
    local Git
    Git-host API access
    hosted CI execution
    browser/remote-provider access
    repository write scopes
    cloud/runtime access

WARRANT-F V0.2 therefore adds:

> Assurance semantics are executor-neutral; execution planning is capability-aware.

Separate dimensions:

    ACTOR / COLLABORATOR
        who is requesting or authoring work

    EXECUTION SURFACE
        local machine
        hosted runner
        Git-host API
        remote runtime
        other future executor

    CAPABILITY SET
        read/write repository
        execute local processes
        mutate host settings
        access secrets
        access deployment target
        publish status
        etc.

    TRUST CLASS
        what assurance weight evidence from that execution has

No current product-model/tool pairing becomes permanent architecture.

Examples:

    ChatGPT having local access today
        does not mean local execution is ChatGPT-owned

    Claude currently writing through GitHub
        does not mean GitHub API is Claude-owned

    Codex or Claude Code having local execution
        does not imply a permanent executor assignment

A planner/provider adapter may choose an execution surface because it satisfies a capability/trust requirement, not because of the model name.

## 8. Claude Message 003 disposition

Claude returned:

    WARRANT_F_DISPOSITION=AMEND
    UPSTREAM_ARCHITECTURE_REOPEN=NO
    ENGINEERING_PYTHON_PROJECT=AMEND
    EMPIRICAL_PROBE_REQUIRED=YES
    PHYSICAL_MIGRATION_AUTHORIZED=NO

ChatGPT accepts the AMEND disposition.

All 33 amendments are retained in substance, with the following reconciliation changes:

    WF-A11
        detective post-admission mode classified as transition bridge,
        not target preservation of direct-push workflow

    WF-A29
        generalized from branch role to accepted-state subject role

    WF-A9 / host feasibility
        current GitHub capability is one provider feasibility input,
        not a target constraint

    WF-A30
        threat model remains explicit, but future identity/authority design
        is unconstrained by the current shared identity arrangement

Everything else is accepted as written unless later empirical evidence falsifies it.

## 9. WARRANT-F V0.2 primitive model

The assurance semantic model is now:

    CLAIM
        what must be true
        selective, not one per test
        owns consequence floor

    VERIFIER
        mechanism that observes evidence about a claim

    WARRANT
        why that verifier can support the claim
        plus bounded sensitivity/specificity evidence

    GATE POLICY
        required claims
        actual consequence >= claim floor
        trust requirement
        freshness
        threshold
        waiver policy

    PROFILE
        invocation shorthand only
        no semantic policy duplication

    EVIDENCE
        exact-subject-bound observation
        outcome + trust + provenance + freshness

    DECISION
        deterministic gate adjudication

    PLANNER
        execution mechanism only
        not semantic authority

## 10. Warrant granularity

Adopt WF-A1 through WF-A4.

### Invariant warrant

For targeted high-consequence invariants:

    targeted seeded failures
    specificity near-misses where relevant
    re-witness on verifier/input/witness change

### Suite warrant

For broader owner test suites:

    selective suite claim
    preregistered sampled mutation adequacy
    cadence/health-triggered re-witness
    not every ordinary test edit

Coverage honesty:

    witnessed scope < declared scope
        -> PARTIALLY_WARRANTED

A blocking use of a partially warranted claim requires an explicit governed acceptance of the gap.

Witness provenance preference:

    historical defect
    old-oracle known-bad
    mutation-generated
    hand-authored

in that order where available.

## 11. Self-weakening ratchet

Adopt WF-A5 through WF-A8.

Candidate changes are evaluated against effective base assurance policy.

Weakening includes:

    removing required claim
    lowering consequence
    lowering threshold
    reducing trust
    narrowing declared inputs/platforms
    deleting required verifier coverage
    weakening witnesses
    widening waiver authority

Legitimate lineage-preserving rename/split/merge is NEUTRAL if base witnesses carry forward and still behave correctly.

Owner decisions may batch one policy-diff digest.

The ratchet governs assurance semantics.

It does not assume a particular Git branching model.

## 12. Trust model

Adopt WF-A9 with terminology:

    T0 LOCAL_UNATTESTED

    T1 LOCAL_RECORDED

    T2a ISOLATED
        fresh controlled execution on exact subject

    T2b AUTHENTIC
        accepted decision originates from the governed producer definition
        and cannot be substituted by an unqualified status publisher
        under the declared threat model

    T2
        T2a + T2b

    T2_ISOLATED_ONLY
        T2a without T2b

    T3
        stronger externally consumable artifact/evidence provenance

The current GitHub/shared-identity arrangement is evidence about today's T2b feasibility only.

Target identity/provider design remains open.

## 13. Lifecycle

Retain:

    F0 AUTHOR FEEDBACK

    G1 CHANGE

    G2 ADMISSION / PROMOTION

    G3 ARTIFACT

    G4 RELEASE

    G5 ACTIVATE

    G6 LIVE

    G7 CUTOVER

    M1 DRILLS

    M2 REVALIDATE

G2 is defined semantically as accepted-state advancement, not as one Git operation.

Add:

    G2-D DETECTIVE BRIDGE
        transitional only when current operating reality allows
        accepted-state advancement before prevention

WF-A10 HEAD_FULL remains an M2 duty.

If target/provider mechanics cannot guarantee exact-result admission, the realization must introduce the necessary separate integrated-state barrier.

## 14. Consumer-side adaptation and workspace isolation

Adopt WF-A12 through WF-A17.

Default:

    Product
        emits Product-native result

    JW1
        emits JW1-owned result contract

    Engineering adapter
        converts native result to neutral assurance evidence

Adapter warrants cover:

    native fail
    crash/collection failure
    zero tests
    skipped-only
    truncated/unparseable result
    zero matching claim results

Direct neutral evidence emission is allowed for Engineering/Research-owned verifiers.

It is not imposed on Product/JW1.

## 15. Engineering environment amendment candidate

WARRANT-F V0.2 recommends:

    project/engineering/
        independent Python project
        independent lock

Binding constraints:

    no co-installation of Product and JW1 into Engineering

    JW1 invoked via CLI/result contract, not path dependency

    small kernel runtime dependency budget

    one engineering-owned bootstrap entry prepares all required environments

    root Python project is removed if no independently justified
    repository-wide runtime remains

This is still:

    R8A_AMENDMENT_CANDIDATE=true

It becomes accepted only with the eventual owner R8-C disposition.

## 16. Evidence publication and storage

Adopt WF-A18 and the non-self-mutating decision-evidence invariant.

Decision-grade assurance evidence about a source subject must not mutate that subject.

Storage technology remains open.

Requirements:

    content-addressable or otherwise exact identity
    immutable after publication
    protected under declared threat model
    resolvable without depending solely on one CI UI
    public/private separation
    AC8 leak qualification before public publication

Control receipts whose semantics are the authority state a commit establishes remain governed separately by WMR-H.

## 17. Oracle retirement

Adopt WF-A19 through WF-A21.

Every current mechanism remains only until its actual retained invariant has a qualified successor.

Retirement evidence includes:

    known-bad sensitivity leg
    known-good specificity leg
    old/new shadow results
    translated cases where representation changes
    explicit owner release

Known-bad corpus is frozen before successor implementation.

Current-layout oracle qualification completes before physical cutover where the old oracle cannot operate after migration.

This sequencing obligation is migration-specific.

It does not constrain the target representation.

## 18. Stochastic and AI assurance

Adopt WF-A22 through WF-A27.

Decision-grade campaigns require:

    preregistered effect size / MDE
    justified sample size
    paired candidate/baseline items by default
    item-clustered inference where repeated samples exist
    one primary decisive metric per claim
    multiplicity rule if more than one decisive metric
    no retry-to-green
    public-development versus private-held-out release corpus distinction
    replay-staleness workflow
    explicit model-identity limitations
    calibrated judge where used

If available sample size cannot support the declared effect:

    OBSERVE only

not REVIEW/BLOCK.

## 19. Kernel boundary and AO restoration

Adopt WF-A28.

Kernel trusted computing base:

    catalog
    effective-policy + ratchet
    evaluator
    record validation
    result adapters

Outside kernel:

    scheduler
    clock
    campaign manager
    deployment mutator
    workflow-state mutation
    cutover execution
    activation execution
    host enforcement adapter

Boundary:

    assurance
        decides admissibility

    AO / JW1
        decide and execute governed transitions

    delivery engineering
        performs governed mutation only after consuming a valid decision

This restores FACET's boundary.

## 20. Threat model

Adopt WF-A30.

Current in-scope baseline:

    accidental human error
    AI-agent overreach/shortcutting
    stale or mis-bound evidence
    dependency/action supply-chain compromise
    public/private leakage

Current baseline does not claim protection against:

    malicious actor already holding owner-level host authority

Future target architecture is free to strengthen identity separation and authority boundaries.

If it does, the declared threat model evolves accordingly.

## 21. Profiles and claims

Adopt WF-A31 and WF-A32.

Profiles are invocation shorthands only.

They do not own:

    consequence
    thresholds
    freshness
    trust requirements

First-class claims remain selective:

    blocking
    cross-component
    release
    migration
    authority
    security
    governance

Ordinary tests are grouped under suite claims.

## 22. Attempt retention

Adopt WF-A33.

Compact attempt records cited by a decision-grade decision inherit that decision's retention class.

Raw bundles may expire when permitted if:

    retained digest/reference is sufficient
    governing retention policy allows expiry

## 23. Capability-aware execution planning

New owner-clarification amendment:

    WF-A34 EXECUTOR CAPABILITY MODEL

Every planned verifier/mutator execution declares needed capabilities such as:

    repository read
    repository write
    local process execution
    network access
    host-status publication
    secret access
    host-settings mutation
    artifact publication
    deployment-target access

The planner resolves an eligible execution surface.

No collaborator/model name is a capability contract.

New amendment:

    WF-A35 EXECUTION SURFACE != TRUST

Having local access, hosted execution, or Git-host API access is not itself a trust classification.

Trust depends on:

    isolation
    subject binding
    producer authenticity
    policy provenance
    permission boundary

New amendment:

    WF-A36 PROVIDER / WORKFLOW MECHANISM FREEDOM

Git branches, PRs, merge queues, direct pushes, workflow files and GitHub Actions are possible realization mechanisms only.

The target architecture is expressed in semantic state transitions and exact subjects first.

## 24. Decision-relevant empirical probes

The owner assurance decision remains blocked on probes whose outcome could change architecture.

Accepted probe set after reconciliation:

    P-D1 WARRANT PROPORTIONALITY
        real selective invariant + suite claims

    P-D2 RATCHET ON REAL HISTORY
        including lineage-neutral and weakening changes

    P-D3 ABSENCE EXECUTION
        Product without Project
        JW1 without Engineering where feasible

    P-D4 ORACLE SUCCESSOR
        known-bad + known-good + translated-case planning
        on one real current oracle

    P-D5 ADAPTER FIDELITY
        native Product/pytest and JW1 result paths
        fail/crash/zero/skipped/truncated cases

    P-H CURRENT HOST CAPABILITY STUDY
        read-only only
        evaluates GitHub as one possible provider realization
        does not constrain target if capability is insufficient

    P-S STOCHASTIC CAMPAIGN POWER STUDY
        preserved result bundles only
        no new live model calls required

Add:

    P-D6 EXECUTION-SURFACE / CAPABILITY SEPARATION
        prove the same assurance semantic request can be represented
        independently of whether an eligible executor is local, hosted,
        Git-host API based, or unavailable
        and that trust classification is not inferred merely from
        executor identity/name

No probe may turn today's workflow into a target requirement merely because it is easy to measure.

## 25. Realization-stage probes remain downstream

After owner architecture acceptance, implementation qualification still includes:

    gate evaluator missing/stale/contradictory cases
    affected-scope fallback
    exact-result promotion realization
    artifact provenance
    non-self-mutating evidence store realization
    provider adapter semantics
    kernel mutation testing
    deployment/recovery implementation evidence

Those qualify a concrete realization.

They do not need to block the semantic architecture decision unless a decision-relevant probe exposes a design defect.

## 26. Current-state use rule

From this checkpoint forward:

> A current-state observation may create:
>
> 1. a requirement,
> 2. a falsifier,
> 3. a migration obligation,
> 4. a compatibility obligation,
> 5. empirical evidence,
>
> but it may not create target architecture merely by being current.

This rule applies to every level, including levels not yet explicitly discussed.

## 27. Current state

    OWNER_TOTAL_ARCHITECTURE_FREEDOM=ACCEPTED_CLARIFICATION

    CURRENT_MECHANISM_PRESERVATION_RIGHT=false
    CURRENT_WORK_PROCEDURE_PRESERVATION_RIGHT=false
    CURRENT_BRANCH_MODEL_PRESERVATION_RIGHT=false
    CURRENT_PUSH_PULL_MERGE_MODEL_PRESERVATION_RIGHT=false
    CURRENT_CI_CD_PRESERVATION_RIGHT=false
    CURRENT_AGENT_TOOL_SURFACE_PRESERVATION_RIGHT=false

    CURRENT_REALITY=EVIDENCE_AND_MIGRATION_CONSTRAINT
    TRANSITION_BRIDGE=EXPLICIT_AND_DISPOSABLE
    TARGET_ARCHITECTURE=REQUIREMENTS_DRIVEN

    MC0028_MESSAGE003=AMEND_ACCEPTED
    WARRANT_F_V0_2=FROZEN_CANDIDATE

    WF_A1_TO_A33=ACCEPTED_WITH_RECONCILIATION
    WF_A34=EXECUTOR_CAPABILITY_MODEL
    WF_A35=EXECUTION_SURFACE_NOT_TRUST
    WF_A36=PROVIDER_WORKFLOW_MECHANISM_FREEDOM

    R8A_ENGINEERING_PYTHON_PROJECT=AMENDMENT_CANDIDATE
    ACCEPTED_STATE=SEMANTIC_SUBJECT_ROLE_NOT_BRANCH_NAME
    G2_D=TRANSITION_BRIDGE_NOT_TARGET_REQUIREMENT

    OWNER_ASSURANCE_DECISION=NOT_READY
    DECISION_RELEVANT_PROBES=8
    PROBE_PROTOCOL=NOT_YET_FROZEN

    SPECIFICATION028=UNCHANGED
    AO10=HELD
    FILE_LEVEL_MIGRATION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=PREREGISTER_R8C_DECISION_RELEVANT_PROBES
