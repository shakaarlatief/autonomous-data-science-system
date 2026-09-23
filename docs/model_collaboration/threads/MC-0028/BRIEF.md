# MC-0028 Brief: Independent Assurance Architecture Design

**Thread:** MC-0028
**Date opened:** 2026-09-23
**Review mode:** INDEPENDENT_THEN_COMPARATIVE
**Coordination branch:** v1-source-vault-bootstrap-resume
**Frozen independent base:** cac7a699eb012c5a02e1c5fab349ebc9e5726145
**Claude interaction:** claude-03
**Claude conversation title:** 03 - Project Knowledge Architecture Foundations and Design Method
**Authority:** Collaboration evidence only. No assurance architecture is accepted by opening this thread.

## 1. Purpose

Independently derive a professional target assurance / verification / testing / CI-CD / delivery architecture from Research 273.

This stage is intentionally mechanism-neutral at entry.

The current repository's:

    34 GitHub Actions workflows
    17 check/integrity/normalization scripts
    65 tracked Python tests
    current pytest layout
    current repository-integrity aggregator
    current GitHub provider/topology

are evidence only.

They do not receive target status.

## 2. Independence protocol

Claude must use the exact frozen base:

    cac7a699eb012c5a02e1c5fab349ebc9e5726145

for substantive repository evidence.

Claude may read:

    docs/research/273_r8c0_from_scratch_assurance_requirements_claim_failure_and_design_protocol.md
    docs/research/272_wmrh_v03_owner_acceptance_mc0027_closure_and_assurance_entry.md

and earlier accepted architecture/evidence available at that base as needed.

Claude must NOT inspect any later ChatGPT assurance-architecture proposal before writing Message 001.

If later commits exist on the branch:

    do not read them for substantive assurance design
    do not infer ChatGPT's candidate from filenames or summaries

The goal is genuine independent architecture derivation, followed later by controlled comparison.

## 3. Design freedom

Everything below the accepted responsibility/semantic boundaries is redesignable.

Claude may propose:

    test topology
    claim/evidence representation
    local command architecture
    CI logical topology
    release gates
    delivery/CD topology
    provider boundaries
    artifact/provenance flows
    security/supply-chain controls
    migration/shadow qualification
    evidence retention
    failure/retry policy
    branch/PR enforcement
    mechanism families

without preserving current implementation shapes.

Do not preserve GitHub Actions merely because it exists today.

Do not remove GitHub Actions merely to demonstrate from-scratch thinking.

Select roles and mechanisms from requirements.

## 4. Hard upstream constraints

Retain unless the candidate finds material falsification evidence:

    Product / Project Level-1 split
    Product runtime independence from Project plane
    independent Product / Project dependency resolution
    JW1 semantic-validation responsibility
    project/engineering repository/cross-workspace assurance responsibility
    engineering may invoke JW1
    JW1 must not depend on engineering
    WMR-H V0.3 accepted representation architecture
    stable break-glass anchor
    current assurance mechanisms have no target-preservation right
    current assurance mechanisms retain migration-oracle duty until released
    enforced invariants must be extracted before replacement
    Specification 028 remains unchanged for now
    AO-10 remains held
    no physical migration

If an upstream accepted contract is materially invalidated, say so explicitly rather than silently designing around it.

## 5. Required candidate coverage

The candidate must cover at least:

    assurance primitive / claim model
    claim-to-evidence binding
    local developer feedback
    Product-local test/evaluation ownership
    JW1 semantic validation
    project/engineering orchestration
    cross-workspace qualification
    repository architecture/integrity checks
    deterministic versus stochastic/AI assurance
    migration/shadow/equivalence qualification
    build/dependency integrity
    security/privacy/supply-chain assurance
    artifact/release provenance
    CI logical topology and lifecycle triggers
    CD/deployment logical topology
    live/post-deployment qualification
    recovery/rollback drills
    failure/retry/flaky-test policy
    evidence retention/publication
    provider-specific integration boundary
    current-mechanism migration/oracle strategy
    cost/latency/scalability controls
    exact areas intentionally left undecided

## 6. Required challenge

Do not merely instantiate Research 273 mechanically.

Challenge whether:

    claim-first is sufficient or needs another first-class abstraction
    ten lifecycle gates are the right conceptual granularity
    assurance should use one orchestrator or federated owners
    local and CI execution should share one logical command graph
    release and deploy evidence should share one evidence plane
    stochastic/AI evaluation belongs in normal CI
    repository governance should be a blocking aggregate
    build provenance is warranted before distribution/deployment exists
    hosted CI is needed for trusted evidence
    current historical workflows should be retired, archived or retained as live oracles

Name the architecture's biggest failure modes and falsifiers.

## 7. Professional external evidence

Claude may independently use current professional standards/guidance.

Do not adopt a framework wholesale.

Research 273 already identifies useful cross-check classes such as:

    NIST SSDF
    SLSA
    NIST AI RMF / TEVV

Claude may add or reject relevance from other credible sources.

## 8. Required output

Write exactly:

    docs/model_collaboration/threads/MC-0028/messages/001_claude_independent_assurance_architecture.md

Include:

    architecture name
    design principles
    logical components
    ownership
    claim/evidence lifecycle
    local / CI / release / deploy / runtime flow
    deterministic and stochastic assurance
    migration from current mechanisms
    security/supply-chain approach
    open decisions
    falsifiers
    comparison-ready summary

End exactly with:

    INDEPENDENT_ASSURANCE_CANDIDATE=COMPLETE
    UPSTREAM_ARCHITECTURE_REOPEN=YES|NO
    CURRENT_MECHANISM_PRESERVATION_REQUIRED=YES|NO
    PROVIDER_LOCK_IN_REQUIRED=YES|NO
    PHYSICAL_MIGRATION_AUTHORIZED=NO

## 9. Write boundary

Claude may write only:

    docs/model_collaboration/threads/MC-0028/messages/**

Do not modify:

    Research 273
    current routing
    CURRENT_STATE
    Specification 028
    current workflows/tests/checks
    prior collaboration threads
    Product or Project implementation

    MC0028=OPEN
    MODE=INDEPENDENT_THEN_COMPARATIVE
    INDEPENDENT_BASE=cac7a699eb012c5a02e1c5fab349ebc9e5726145
    NEXT=INDEPENDENT_CANDIDATES
