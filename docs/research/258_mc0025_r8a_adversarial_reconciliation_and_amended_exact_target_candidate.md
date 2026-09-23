# Research 258: MC-0025 R8-A Adversarial Reconciliation and Amended Exact-Target Candidate

**Date:** 2026-09-23
**Status:** MC-0025 CLAUDE REVIEW RECONCILED / R8-A AMENDMENT RECOMMENDED / OWNER DECISION REQUIRED / NO PHYSICAL MIGRATION
**Parent program:** Research 240
**Original R8-A recommendation:** Research 257
**Claude review:** MC-0025 Message 001
**Review commit:** 14bb28f0094a7a30d4f29798e916bb4ee77fdda7
**Reconciliation base:** 14bb28f0094a7a30d4f29798e916bb4ee77fdda7
**Scope:** Reconcile Claude's adversarial review of Research 257, distinguish genuine architecture amendments from representation-stage and migration-stage work, and freeze the amended R8-A candidate for explicit owner decision.
**Authority:** Recommendation only. Research 257 remains historical proposal evidence. No physical move, Specification 028 amendment, AO-10 implementation, W5-F0 resume, PSMF extraction or authority switch is authorized.

## 1. Reconciliation result

Claude returned:

    R8A_ADVERSARIAL_DISPOSITION=AMEND

with:

    5 amendments before representation
    4 amendments before file-level migration
    11 clarifications
    0 reopen findings

ChatGPT agrees with the overall disposition.

The review does not undermine:

    G-DUAL
    Product / Project Level-1 split
    R6 bounded contexts
    PW1 / PW2 / JW1 workspace directions
    R7 Project information hierarchy
    AO-3 through AO-9 semantics
    operations/engineering six-subarea model and bound 8

The amended candidate remains the same architecture family and the same basic physical realization. The amendments remove one unnecessary cross-plane dependency-resolution coupling, sharpen framework/instance and engineering/system seams, make break-glass recovery independent of generated state, and restore lifecycle gates that Research 257 under-specified.

Recommended owner disposition:

    AMEND

## 2. AM-1 accepted: Product and Project Python dependency resolution are independent

Research 257 proposed:

    one repository-level uv workspace
    one root uv.lock
    product/runtime as a workspace member
    project/system as a workspace member

That is replaced by two independently resolved Python projects:

    product/runtime/
        pyproject.toml
        uv.lock
        .python-version
        ...

    project/system/
        pyproject.toml
        uv.lock
        .python-version
        ...

The root:

    pyproject.toml

may remain only for repository-wide tool configuration whose root residency is independently justified. It MUST NOT make Product and Project members of one uv workspace and MUST NOT own their runtime dependency resolution.

There is no root:

    uv.lock
    .python-version

under the amended target.

Research 239 established strong lifecycle-independence evidence for the Project Development System / PSMF mechanism. The Product runtime and Project system are not mutually imported runtime packages.

A shared resolver would therefore create coupling at a layer that the semantic dependency rule does not detect:

    no import dependency
        but
    one dependency solution

Current uv documentation confirms that a uv workspace shares one lockfile and that uv lock operates on the whole workspace. The workspace feature is designed for packages managed together.

The amended design instead makes the independently evidenced lifecycle boundary independently resolvable.

Cross-plane compatibility, where genuinely relevant, is qualified by:

    project/engineering/
        cross-workspace checks / integration qualification

rather than forced by a shared dependency solution.

Each Python project owns:

    requires-python
    .python-version when operationally useful

Repository-wide policy may constrain supported Python lines through governance/engineering checks, but divergence between Product and Project does not require root-file churn or shared resolution.

### 2.1 Amended true-root inventory

Recommended tracked root becomes:

    .github/
    .gitignore
    README.md
    project_anchor.json
    pyproject.toml
    product/
    project/

Count:

    7

Review bound:

    12

Result:

    ROOT_PRESSURE=PASS

The root pyproject survives only as a bounded external-tool/configuration anchor. If later migration proves no repository-wide Python tool reads it, it should be removed rather than retained ceremonially.

## 3. AM-5 accepted: JW1 responsibility boundaries are not pre-created empty modules

Research 257 named ten JW1 responsibility/module boundaries.

The amended rule is:

> These names freeze responsibility boundaries and dependency expectations, not a requirement that ten directories exist immediately.

Physical module directories are created when realized capability justifies them.

Current/qualified mechanisms may migrate into realized modules.

Prospective AO-10 capabilities remain logical responsibilities until implementation gives them a concrete module shape.

R8 migration must label JW1 capability families as one of:

    RETAINED_QUALIFIED
    PARTIALLY_REALIZED
    PROSPECTIVE

At minimum, current evidence indicates:

    semantics        RETAINED_QUALIFIED
    views            RETAINED_QUALIFIED
    preservation     RETAINED_QUALIFIED
    transitions      PARTIALLY_REALIZED
    reconstruction   PARTIALLY_REALIZED

    activation       PROSPECTIVE / AO-10 held
    evolution        PROSPECTIVE executable realization
    continuity       PROSPECTIVE executable realization

Exact code-file mapping remains a later file-level disposition task.

## 4. AM-6 accepted with refinement: framework mechanism versus ADS instance integration

A generic adapters area can straddle the PSMF framework/instance seam.

The amendment is accepted, but the discriminator is project generality, not merely interface versus concrete implementation.

Framework-owned code under:

    project/system/src/ads_project_system/

may contain:

    generic adapter ports/interfaces
    reusable provider/tool adapter implementations
    generic Git/filesystem mechanisms
    reusable collaboration/runtime integration mechanisms

only when their behavior is project-agnostic and suitable for PSMF materialization/upgrades.

ADS instance-owned policy/state under:

    project/system/instance/

owns:

    provider/tool selection
    ADS-specific routing policy
    ADS-specific endpoint/integration policy
    local bridge binding/configuration
    project-specific capability enabling/disabling
    project-specific credentials references
    project-specific overrides/extensions

Concrete code is not automatically instance-owned merely because it talks to a provider. A reusable provider adapter may remain framework mechanism. What MUST NOT happen is an upstream framework refresh overwriting ADS-specific integration policy.

The representation stage must preserve this seam explicitly.

## 5. AM-7 accepted: permanent transition management replaces a one-time migration concept

Research 257's migration responsibility mixes:

    reusable successor-transition mechanism
    current one-time R8 migration work

The amended stable JW1 responsibility is:

    transitions

It owns reusable mechanism for:

    authority-preserving successor bridges
    compatibility/shadow transitions
    transition validation
    cutover/rollback mechanism
    transition receipts/evidence production
    repeated architecture-successor transitions

One-time R8 migration plans, manifests, execution state and temporary scaffolds remain Project-instance execution state/evidence. They do not become permanent framework mechanism merely because the first transition needs them.

This retains AO-7 semantics while giving the permanent capability a lifecycle-neutral name.

Exact persistent representation of transition state remains an R8 representation-stage decision.

## 6. AM-9 accepted: cold start has a generate-independent break-glass path

Generated orientation is an accelerator, not a required dependency for recovery.

The amended machine cold-start contract is:

    project_anchor.json
        ->
    authored/canonical Project-system control or authority locator
        ->
    governing Project knowledge

with no generated artifact required.

A generated orientation may provide a faster normal path:

    project_anchor.json
        ->
    generated current orientation

but failure, absence or staleness of generated orientation MUST NOT prevent recovery.

The human root README similarly links directly to:

    project/README.md
    project/knowledge/README.md
    governing/recovery procedure

and may additionally link to generated current orientation.

The representation stage must choose control-state representation so the generate-independent path is directly readable/inspectable without running the generator it may be repairing.

project_anchor.json remains a deliberate bounded JSON serialization choice for the stable root locator. It is not evidence that all Project-system state should be JSON.

## 7. AM-2 accepted: PC7 remains one context/module family with explicit internal seams

The R8-A Product target retains:

    runtime_platform/

as the PC7 module family, but requires explicit internal boundaries for at least:

    persistence
    integrations
    security
    operations

These are internal seams, not automatically separate packages/workspaces/services.

They exist so later lifecycle/deployment evidence can split them without first disentangling an undifferentiated platform module.

Product-facing API/CLI presentation contracts belong to PC6 Product Interaction and Access.

Use-case/application ownership stays with the initiating Product context.

Shared server/transport hosting mechanics may be implemented by PC7 where they are genuinely technical runtime mechanism.

A generic API folder MUST NOT become a semantic owner merely because transport code is shared.

## 8. AM-3 accepted: semantic validation and repository validation have different owners

The amended boundary is:

    project/system / JW1
        owns semantic validation
        "does this governed artifact/control state satisfy the
         Project-system semantic/machine contract?"

    project/engineering
        owns repository/cross-workspace validation and invocation
        "does the repository and its workspaces satisfy structural,
         integration, publication and integrity constraints?"

Direction:

    project/engineering MAY invoke JW1 validation
    JW1 MUST NOT depend on project/engineering

This preserves PSMF materializability: ADS-specific repository engineering cannot become a framework dependency.

Repository-integrity entrypoints therefore live with engineering even when one component they invoke is a JW1 semantic validator.

## 9. AM-4 accepted: active research requires terminal disposition; reproductions require admission

Every bounded workspace under:

    project/research/

is:

    ACTIVE / PROGRAM-SCOPED

and on completion MUST receive one explicit disposition:

    PROMOTE_IMPLEMENTATION
    PRESERVE_EXECUTABLE_REPRODUCTION
    RETAIN_EVIDENCE_ONLY_WHERE_INDEPENDENTLY_REDERIVABLE
    ARCHIVE_WITH_EXPLICIT_OWNER
    RETIRE

No completed research workspace remains in project/research merely because nobody classified it.

Admission to:

    project/reproductions/

requires the explicit:

    PRESERVE_EXECUTABLE_REPRODUCTION

disposition plus a stated reproducibility/reconstruction reason.

project/reproductions is not a stale-code archive.

ARCHIVE_WITH_EXPLICIT_OWNER does not create a generic archive bucket. Its target must be independently justified under the accepted History/natural-owner rules.

## 10. AM-8 accepted: continuity/recovery responsibilities get an explicit three-way discriminator

The target retains the existing names but freezes this placement rule:

    JW1 continuity capability
        mechanized interaction continuity
        interruption/resume state machine
        recovery routing
        break-glass activation mechanism

    knowledge/operations/engineering/recovery/
        human operational recovery procedure
        incident/runbook procedure
        backup/restore procedure
        development-environment recovery procedure

    knowledge/operations/collaboration/
        contributor/model handoff
        collaboration continuity
        relay/return procedure

A carrier is placed by primary responsibility.

Cross-cutting subject/navigation metadata may expose related recovery material without duplicating authority.

## 11. Clarifications accepted

### CL-1 cross-context Product orchestration

Within the modular Product runtime, a cross-context use case is owned by the context that initiates/owns the business behavior and reaches other contexts through explicit published contracts.

There is no new repository-global application owner.

### CL-2 API transport

Product-facing contract is PC6; use-case ownership stays in the initiating Product context; shared technical hosting/transport mechanics may be PC7.

### CL-3 rename rule

Rename when the current name is semantically wrong for the accepted responsibility.

Do not rename merely because a name is historical.

Therefore ads_system is retained, project_knowledge is not retained as JW1 package identity, and ads_project_system remains the local ADS JW1 package identity.

A future extracted generic PSMF upstream may use a generic package name.

### CL-4 Project-named root anchor

The root machine anchor is Project-named because repository development/reconstruction cold start is a Project-plane responsibility.

The Product runtime does not need this anchor for runtime correctness.

JSON is intentionally selected only for this tiny versioned locator contract.

### CL-5 Project system versus Project knowledge direction

    project/system
        owns executable machine contracts/mechanisms

    project/knowledge
        owns durable human-reviewable meaning about the Project system

Knowledge carriers may conform to schemas from the system.

The system may read knowledge carriers.

Neither relationship makes knowledge an importable runtime package or gives generated system state authority over canonical knowledge.

### CL-6 AO-6 policy versus mechanics

    JW1
        owns branch/workstream purpose semantics and routing policy

    project/engineering
        owns Git-host/CI/protection/enforcement mechanics

### CL-7 KA-R52 ownership split

    obligation identity / accepted MUST
        governance knowledge

    governed deferral / blocking reason / reactivation condition
        governance/planning knowledge

    current realization status
        Project-system control state

These are bound by typed identity/relation semantics.

No new Project knowledge class is required.

### CL-8 verification and security

    operations/engineering/verification
        procedure for executing/interpreting qualification

    evidence/qualification
        qualification result/evidence

    governance security material
        policy/required constraints

    operations/engineering/security
        secure-development and response procedure

### CL-9 root-anchor freshness

The stable machine anchor requires a deterministic repository-engineering check that verifies schema/version validity, target existence, declared role compatibility and no stale locator after path transition.

The anchor itself remains authored rather than generated.

### CL-10 JW1 retained versus prospective capability

Section 3 makes this distinction explicit.

### CL-11 representation honesty

Physical responsibility areas do not imply many files, one file, one row set, one database, one graph or one event log.

The representation stage decides that per information/control class.

The intentional bounded representation decision already selected at R8-A is:

    root project_anchor.json

The exact generated human-orientation serialization, generated machine-orientation serialization, instance control-state storage, receipt/evidence storage and amended schema serialization remain unresolved.

## 12. Additional migration guard accepted from the review

The current docs tree has the repository's highest path-reference density.

Before any physical move, the file-level migration design must treat reference integrity as a first-class dependency graph:

    inbound Markdown links
    declared semantic/path references
    collaboration trigger paths
    checkpoint/research citations
    validator path contracts
    scripts/tests/workflows
    generated-view source paths
    compatibility aliases/shims where required

A move whose target ownership is correct can still be operationally unsafe if references are not qualified.

This is migration cost, not evidence that R7 ownership is wrong.

## 13. Amended exact target

The owner-decision candidate is now:

    ROOT
        .github/
        .gitignore
        README.md
        project_anchor.json
        pyproject.toml       # repository-wide tool config only; no uv workspace
        product/
        project/

    product/
        runtime/
            pyproject.toml
            uv.lock
            .python-version
            alembic.ini
            migrations/
            src/
                ads_system/
                    project_intelligence/
                    methodological_knowledge/
                    evidence_provenance/
                    reasoning/
                    execution/
                    runtime_platform/
                        <explicit persistence / integrations /
                         security / operations seams>
            tests/

        interaction/
            web/
                package.json
                package-lock.json
                ...

    project/
        system/
            README.md
            pyproject.toml
            uv.lock
            .python-version
            src/
                ads_project_system/
                    <realized capability modules only>
            contracts/
                schemas/
            instance/
                <representation-stage realization>
            generated/
                <derived artifacts; exact representation pending>
            tests/

        engineering/
            checks/
            tests/
            tooling/

        research/
            <active program-scoped workspaces only>

        reproductions/
            <explicitly admitted preserved executable reproductions>

        knowledge/
            governance/
                direction/
                architecture/
                    rationale/
                    specifications/
                decisions/
                planning/

            evidence/
                research/
                qualification/
                provenance/

            operations/
                engineering/
                    repository/
                    environments/
                    verification/
                    security/
                    release/
                    recovery/
                collaboration/

            history/
                milestones/

Root count:

    7 <= 12
    PASS

## 14. What remains unresolved after this amendment

R8-A still deliberately does not decide:

    Project knowledge carrier serialization by class
    Project-system control-state persistence
    receipt persistence
    transition-state persistence
    generated-view serialization
    graph/database/vector-cache use
    exact declaration/schema evolution under Specification 028
    exact current-file disposition
    exact compatibility/shadow paths
    migration order
    cutover execution

These belong to subsequent R8 stages.

## 15. Owner decision

Recommended:

    AMEND

Meaning:

    accept Research 257's architecture family and exact target as amended
    by Research 258

    accept independent Product/Project dependency resolution

    accept the framework/instance adapter seam

    accept permanent transition-management responsibility

    accept generate-independent cold start

    accept PC7 internal seams

    accept semantic-validation versus repository-validation ownership

    accept mandatory research-workspace disposition and reproduction admission

    accept the three-way continuity/recovery discriminator

    accept the eleven clarifications

    retain AO-3 through AO-9 semantics unchanged

    do not authorize physical migration

If accepted, the next stage is the representation architecture, followed by the Specification 028 delta and only then the file-level migration manifest.

## 16. Current state

    MC0025_MESSAGE001=RECONCILED
    R8A_DISPOSITION_RECOMMENDED=AMEND
    R8A_REOPEN_REQUIRED=false

    ROOT_TARGET_ENTRIES=7
    ROOT_BOUND=12
    ROOT_PRESSURE=PASS

    PRODUCT_PROJECT_UV_WORKSPACE_SHARED=false
    PRODUCT_RUNTIME_LOCK=product/runtime/uv.lock
    PROJECT_SYSTEM_LOCK=project/system/uv.lock
    ROOT_UV_LOCK=false
    ROOT_PYTHON_VERSION=false

    JW1_RESPONSIBILITIES=ACCEPTED_LOGICAL_BOUNDARIES
    EMPTY_FUTURE_MODULE_RESERVATION=false
    PSMF_FRAMEWORK_INSTANCE_SEAM=EXPLICIT
    PERMANENT_TRANSITION_CAPABILITY=transitions
    GENERATED_ORIENTATION_REQUIRED_FOR_RECOVERY=false

    PC7_INTERNAL_SEAMS=REQUIRED
    JW1_ENGINEERING_VALIDATION_BOUNDARY=EXPLICIT
    RESEARCH_TERMINAL_DISPOSITION=REQUIRED
    REPRODUCTION_ADMISSION=EXPLICIT
    CONTINUITY_RECOVERY_DISCRIMINATOR=EXPLICIT

    AO3_AO9_SEMANTICS=RETAINED
    REPRESENTATION_ARCHITECTURE=HELD_PENDING_OWNER_DECISION
    FILE_LEVEL_MIGRATION=HELD
    SPECIFICATION028=UNCHANGED
    AO10=HELD
    W5_F0=PAUSED
    PHYSICAL_MIGRATION_AUTHORIZED=false
    AUTHORITY_SWITCH_ALLOWED=false
    OWNER_DECISION=PENDING
    NEXT=OWNER_R8A_AMENDMENT_DECISION
