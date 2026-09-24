# Research 277: R8-C Decision-Relevant Assurance Probe Protocol

**Date:** 2026-09-24
**Status:** PREREGISTERED / NO RESULT OBSERVED / WARRANT-F V0.2 OWNER DECISION HELD / NO PHYSICAL MIGRATION
**Parent candidate:** Research 276 / WARRANT-F V0.2
**Thread:** MC-0028
**Scope:** Freeze the empirical questions, fixtures, interpretation rules and architecture-change criteria for the eight decision-relevant probes before observing results.
**Authority:** Probe protocol only. It does not select the assurance architecture, implementation tools, host workflow, branch model, CI provider, or migration procedure.

## 1. Anti-anchoring rule for all probes

The owner has explicitly established all-level target-design freedom.

Therefore every probe result must be classified into one of:

    TARGET_ARCHITECTURE_EVIDENCE
        evidence about whether a semantic architecture mechanism is viable

    TRANSITION_EVIDENCE
        evidence about bridging current operating reality to the target

    CURRENT_IMPLEMENTATION_DEBT
        evidence that today's repository/mechanism is coupled or weak

A current implementation failure MUST NOT be treated as target-architecture falsification unless the probe isolates a requirement that the target architecture itself cannot satisfy.

Likewise, a current GitHub capability PASS MUST NOT silently select GitHub, a branch workflow, or a hosted-runner topology as the target.

## 2. Result classes

Each probe returns exactly one primary class:

    PASS
        preregistered architecture discriminator is satisfied

    AMEND
        evidence materially changes WARRANT-F V0.2

    CURRENT_DEBT_ONLY
        target direction remains viable; current realization requires migration work

    INCONCLUSIVE
        evidence is insufficient for the architecture question

    HARNESS_INVALID
        probe cannot support interpretation because its own method is defective

No failed current mechanism is automatically an architecture failure.

## 3. P-D1: warrant proportionality on real claims

### Question

Can first-class warrants remain selective and useful without turning ordinary ADS testing into unbounded metadata/witness bureaucracy?

### Fixture

Select 12 real candidate assurance claims from the current corpus, before authoring any warrants:

    4 invariant claims
        authority / identity / stale binding / privacy or equivalent

    4 suite claims
        Product/JW1/repository families

    4 cross-boundary claims
        architecture / migration / release-governance style claims

Selection is based on current semantic importance, not ease of warranting.

### Procedure

For each claim:

    classify claim grain
    state claimed scope
    identify existing witness sources
    author minimum viable warrant
    identify unwitnessed remainder
    estimate recurring re-witness triggers
    for one real suite, run sampled mutation adequacy

### Recorded metrics

    warrant feasible without semantic distortion
    witness provenance class
    authoring effort
    recurring maintenance triggers
    PARTIALLY_WARRANTED use
    uncovered scope
    mutation kill rate for sampled suite

### Architecture criteria

PASS if:

    all 12 claims can be represented without one-claim-per-test expansion

    all 4 invariant claims have at least one executable sensitivity witness

    no invariant claim is described as fully warranted when witnessed scope is narrower

    suite warrant can distinguish deliberate seeded defects from surviving tests

    expected recurring re-witness burden is bounded by semantic changes/health triggers,
    not ordinary unrelated test edits

AMEND if:

    warrant semantics require per-test first-class claims

    invariant witnesses are infeasible for material claims

    suite warrants cannot produce useful sensitivity evidence

    or ordinary maintenance would routinely require owner/gate ceremony unrelated to
    assurance meaning

No numeric time budget is frozen because current authoring speed is not a target constraint; the probe records time only as comparative evidence.

## 4. P-D2: ratchet on real history

### Question

Can the base-revision ratchet distinguish weakening from legitimate lineage-preserving evolution without making ordinary architecture refactors owner-gated?

### Fixture

Create a frozen sample of real historical changes affecting:

    tests
    check scripts
    workflows
    schema/validator contracts

The sample must include known examples of:

    tightening
    weakening
    rename/move
    split/merge
    test deletion
    input-scope narrowing
    dependency/lock change
    neutral formatting/refactor

Before running the ratchet classifier, create an independent semantic label for each sampled change.

### Criteria

PASS if:

    every independently labelled material weakening is classified WEAKEN or REVIEW

    no lineage-preserving rename/split/merge with carried witnesses is classified as
    an unexplained silent weakening

    no candidate change can remove its own required base witness and become PASS

    batched owner-decision semantics can bind one exact policy-diff digest

AMEND if any material weakening is admitted as neutral/strengthening, or if legitimate
lineage-preserving changes systematically require owner decisions despite valid witness carry-forward.

Classification disagreements are preserved rather than silently adjudicated after the fact.

## 5. P-D3: boundary independence / absence execution

### Question

Are the accepted Product/JW1/Engineering dependency boundaries realizable without hidden runtime dependence?

### Important interpretation guard

The current repository has not yet been physically migrated to R8-A.

Therefore:

    current-layout coupling
        -> CURRENT_IMPLEMENTATION_DEBT

unless it demonstrates a semantic need for the forbidden dependency.

The target architecture is falsified only if the relevant behavior cannot be expressed without the forbidden dependency in a bounded target-shaped fixture.

### Procedure

Two layers:

    Layer A current-state observation
        run/import representative Product behavior with Project tooling unavailable
        run/invoke representative JW1 behavior with Engineering unavailable

    Layer B target-shaped isolation fixture
        construct minimal environment boundaries matching accepted R8-A roles
        exercise representative Product and JW1 semantic entrypoints through
        allowed contracts only

### Criteria

PASS if target-shaped fixture succeeds and deliberate forbidden-dependency injection is detected.

CURRENT_DEBT_ONLY if current layout fails but target-shaped fixture succeeds.

AMEND if representative required Product/JW1 behavior inherently requires a forbidden dependency under the target-shaped fixture.

HARNESS_INVALID if the fixture does not actually remove or detect the dependency.

## 6. P-D4: current-oracle successor feasibility

### Question

Can a current validation family be retired by semantic parity rather than implementation/output preservation?

### Fixture

Use one real current oracle family with material accepted history.

Before successor design:

    freeze a known-bad corpus
        real historical defect if available
        mutation-generated cases
        malformed cases

    freeze a known-good corpus
        historical accepted heads/cases that the old oracle passed

Record digests before successor implementation.

### Procedure

    run old oracle on frozen corpora
    specify successor claims/warrants
    implement only enough successor behavior for the probe
    compare sensitivity and specificity
    include one translated representation case where applicable

### Criteria

PASS if:

    successor rejects every known-bad case the old oracle rejects

    successor accepts every known-good case the old oracle accepts,
    except explicitly preregistered intentional semantic differences

    translated-case semantics preserve the same invariant

    no unique requirement is discovered that depends on retaining the old mechanism shape

AMEND if semantic parity requires a different claim/warrant architecture.

CURRENT_DEBT_ONLY if the old oracle is too layout-bound to survive migration but its invariant is cleanly transferable.

## 7. P-D5: adapter fidelity

### Question

Can Product/JW1 native results be safely adapted into neutral assurance evidence without importing Engineering contracts into their semantic ownership?

### Fixture

Use:

    one native Python test-result path
    one JW1-owned result path

Cases:

    pass
    fail
    crash/collection error
    zero collected
    skipped only
    truncated/unparseable
    claim maps to zero matching results

### Criteria

PASS if the consumer-side adapter maps each case to the preregistered neutral state without Product/JW1 importing Engineering assurance code.

Required mappings:

    native pass           -> PASS evidence
    native fail           -> FAIL evidence
    crash/collection      -> HARNESS_INVALID
    zero collected        -> INCOMPLETE
    skipped only          -> INCOMPLETE
    truncated/unparseable -> HARNESS_INVALID
    zero claim matches    -> UNVERIFIED

An intentionally faulty adapter must be caught by its witness cases.

AMEND if the neutral evidence model cannot be adapted without violating workspace ownership.

## 8. P-H: current host capability study

### Question

Which trust/enforcement properties can the current GitHub installation support today?

This is provider feasibility evidence only.

### Read-only only

No branch protection, ruleset, workflow, identity, permission or repository setting may be changed.

Inspect as available:

    current branch protection state
    current checks/status producer identity information
    whether required status checks can be bound to a specific producer/app
    whether gate definitions can be sourced from a protected base/location
    current branch/ref mutation surfaces exposed by the integration
    current repository/default-branch metadata

### Interpretation

Possible result:

    CURRENT_GITHUB_CAN_REALIZE_T2
    CURRENT_GITHUB_CAN_REALIZE_T2A_ONLY
    CURRENT_GITHUB_CAPABILITY_INSUFFICIENT_OR_UNKNOWN

None selects GitHub as target provider.

A deficiency becomes a target requirement or alternative-provider/design question, not a reason to weaken the architecture.

## 9. P-S: stochastic campaign power desk study

### Question

Can current preserved ADS experiment evidence support statistically meaningful decision-grade AI/stochastic claims, and what sample scales would be required?

### No new live model calls

Use only preserved result bundles already in the repository.

### Procedure

For suitable repeated/item-level evidence:

    estimate item-level variability
    distinguish item count from repeated samples
    estimate paired candidate-baseline variability where available
    calculate sample size for plausible minimum detectable effects
    identify whether public/private held-out separation is required

If preserved bundles cannot support this calculation:

    classify INCONCLUSIVE

Do not invent independence where item clustering exists.

### Architecture criteria

PASS if at least one realistic campaign shape can support preregistered power/MDE reasoning and paired/item-clustered analysis.

AMEND if the architecture needs a different stochastic-decision model.

INCONCLUSIVE if current evidence is insufficient; this does not falsify the architecture but keeps decision-grade stochastic BLOCK claims disabled until a valid campaign can be designed.

## 10. P-D6: executor capability versus trust separation

### Question

Can one assurance request remain semantically identical across different executor capabilities without inferring trust from model/tool identity?

### Fixture

Define one neutral assurance request:

    exact subject
    verifier
    required capability set
    required trust properties
    expected evidence contract

Evaluate at least these executor descriptions:

    local process-capable executor
    Git-host API-only executor
    hosted CI executor
    executor lacking one required capability

The descriptions are capability records, not ChatGPT/Claude/Codex identities.

### Criteria

PASS if:

    the semantic request is identical across executors

    eligibility changes only from capability/trust properties

    unavailable executor fails selection without changing claim semantics

    local/hosted/Git-API labels alone do not determine T0/T1/T2

    two different model identities with the same declared capability/trust record are
    interchangeable to the planner for this request

AMEND if the architecture needs actor-specific semantic branches.

## 11. Probe execution order

To minimize wasted work:

    P-H
        cheap read-only provider evidence

    P-D6
        capability/trust semantic probe

    P-D3
        boundary isolation

    P-D5
        adapter model

    P-D1
        warrant proportionality

    P-D2
        ratchet history replay

    P-D4
        current-oracle successor

    P-S
        statistical desk study

Order does not change thresholds.

Parallel execution is allowed only where one probe's implementation cannot expose another probe's expected answer.

## 12. Probe evidence discipline

Every implemented probe must include:

    exact source/base binding
    input/fixture digests where material
    negative control
    explicit PASS/AMEND/CURRENT_DEBT_ONLY/INCONCLUSIVE/HARNESS_INVALID result
    no threshold change after observation
    distinction between current-state and target-architecture inference

A harness defect is repaired prospectively.

Failed current implementation is never silently upgraded into target failure.

## 13. Owner-decision rule

WARRANT-F V0.2 becomes owner-decision-ready only after all eight probes are reconciled.

Decision readiness requires:

    no unresolved AMEND result

    no HARNESS_INVALID result

    INCONCLUSIVE results explicitly scoped so they do not falsely support a
    decision-grade claim

    current-debt-only results translated into migration obligations rather than
    target restrictions

The owner decision may still:

    ACCEPT
    AMEND
    REOPEN

## 14. Still not selected

The protocol does not select:

    branch model
    PR model
    merge queue
    direct-push policy
    GitHub Actions
    CI provider
    runner provider
    host protection
    identity provider
    status publisher
    exact Python test framework
    exact evidence store
    deployment provider
    release topology

## 15. Current state

    P_R8C_DECISION_PROTOCOL=FROZEN

    P_D1=WARRANT_PROPORTIONALITY
    P_D2=RATCHET_HISTORY
    P_D3=BOUNDARY_ABSENCE
    P_D4=ORACLE_SUCCESSOR
    P_D5=ADAPTER_FIDELITY
    P_H=CURRENT_HOST_READ_ONLY
    P_S=STOCHASTIC_POWER_DESK_STUDY
    P_D6=EXECUTOR_CAPABILITY_TRUST_SEPARATION

    RESULT_COUNT=0
    THRESHOLDS_CHANGED_AFTER_OBSERVATION=false

    WARRANT_F_V0_2=EMPIRICAL_CANDIDATE
    OWNER_ASSURANCE_DECISION=HELD

    SPECIFICATION028=UNCHANGED
    AO10=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=EXECUTE_P_H
