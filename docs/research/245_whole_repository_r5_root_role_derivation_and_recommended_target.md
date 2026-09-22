# Research 245: Whole-Repository R5 Root-Role Derivation and Recommended Target Architecture

**Date:** 2026-09-22
**Status:** R5 RECOMMENDED TARGET FROZEN / OWNER ACCEPTANCE REQUIRED / NO PHYSICAL MIGRATION
**Parent program:** Research 240
**Evidence basis:** Research 241-244
**Repository base:** 29206af186579294a59353e1b14c1104bad94334
**Scope:** Convert Candidate G's role-first bounded-workspace rules into an exact root-role model for ADS and determine whether one target architecture is strong enough to recommend for owner disposition.

## 1. R5 result

R5 recommends a specific instantiation of Candidate G:

    PRODUCT / PROJECT DUAL-PLANE
    ROLE-FIRST BOUNDED-WORKSPACE ARCHITECTURE

Short identifier in this research only:

    G-DUAL

This is the recommended target architecture.

It is **not owner-accepted yet**.

No physical migration is authorized by this recommendation.

## 2. First-principles distinction

The repository currently contains two fundamentally different worlds.

### Plane P: the thing being built

This is the **ADS product/system** itself:

    runtime/domain/application code
    user-facing interfaces
    product persistence
    product integrations
    product-owned schemas/contracts
    product-owned methodological/source knowledge
    product tests
    future services/apps/packages

### Plane J: the project that builds and governs it

This is the **ADS development project**:

    project-development control system
    project authority
    architectural knowledge
    research/evidence
    decisions
    continuity/reconstruction
    collaboration governance
    repository engineering
    qualification
    historical development material

Research 177 already established one important part of this distinction:

> project-development knowledge infrastructure is infrastructure around development of ADS, not an ADS product-domain subsystem.

PSMF strengthens that boundary.

R0-R4 show that the present root obscures it by mixing product workspaces, project-development infrastructure, artifact-type buckets, evidence families and historical programs as peers.

G-DUAL makes the distinction explicit.

## 3. Recommended root roles

Ignoring tool-required root files for the moment, the durable logical root should have **two primary architectural parents**:

    product/
    project/

The physical names are recommended, not yet owner-accepted.

They are intentionally ordinary words.

### 3.1 product/

Owns everything whose primary responsibility is the **operational ADS system/product**.

A concern belongs here when the answer to the following is yes:

> If we stopped developing ADS as a project but wanted to retain/run/build the ADS product, is this thing fundamentally part of that product or its product-owned assets?

Examples expected to resolve here after R6:

    current src/ads_system runtime
    frontend/Cockpit product surface
    product persistence/migrations
    product APIs/CLIs/services
    Source Universe product capability
    retrieval/runtime capabilities
    product-owned methodological knowledge assets
    product exchange contracts
    product-local tests
    future deployable applications/packages

### 3.2 project/

Owns everything whose primary responsibility is **developing, governing, understanding, qualifying or preserving the ADS project** rather than executing the ADS product.

A concern belongs here when the answer is yes:

> Does this exist because humans/agents are building, governing, researching, validating, reconstructing or preserving ADS as a project?

Examples expected to resolve here after R6/R7:

    PSMF materialized project-development system
    ADS-specific project-system instance policy/extensions
    project architecture and authority
    current state / continuity / routing
    project research and qualification evidence
    project decisions and checkpoints
    repository-wide engineering/governance tooling
    model collaboration governance
    project-wide integration/acceptance checks
    historical prototypes/programs retained as development evidence

This distinction is semantic ownership, not merely visibility.

## 4. True repository root

The recommendation does **not** attempt to force every file under product/ or project/.

A small number of files/directories may remain at the Git repository root when their responsibility is genuinely repository bootstrap/host integration or when external tools strongly expect root placement.

Expected examples:

    README.md
    .gitignore
    .github/
    root workspace/package-manager configuration when needed
    dependency lockfiles when workspace-wide
    editor/runtime version anchors when repository-wide

The criterion is:

> root placement must be justified by repository bootstrap/tooling semantics, not by lack of a better owner.

This prevents "clean root" aesthetics from fighting ecosystems.

## 5. Recommended workspace rule

product/ and project/ are **role parents**, not packages.

Inside them, only evidence-backed lifecycle/build boundaries become workspaces.

Current strong workspace candidates:

    product
        ADS Python runtime workspace
        frontend application workspace

    project
        project-development system workspace

Future capabilities do not automatically become workspaces.

Source Universe, retrieval or persistence remain internal capabilities unless independent build/dependency/lifecycle evidence later justifies extraction.

This preserves Candidate G's anti-over-modularization rule.

## 6. Recommended disposition of current root concepts

This section gives **target-role dispositions**, not immediate moves.

### .github/

Target role:

    TRUE ROOT / HOST INTEGRATION

Reason:

    GitHub gives this path repository-host semantics.

No reason exists to hide it merely for symmetry.

### src/

Target role:

    ABSORB INTO PRODUCT WORKSPACE

Current:

    src/ads_system/

Target principle:

    preserve professional Python src layout
    inside the ADS runtime workspace

Therefore the **src layout survives**, while generic root-level src/ does not need to remain the repository-wide organizing principle.

### frontend/

Target role:

    ABSORB INTO PRODUCT PLANE AS A WORKSPACE

Its own Node toolchain remains valuable.

Its internal split between production frontend, design-lab and historical design evidence remains R6 work.

### migrations/

Target role:

    ABSORB INTO PRODUCT PERSISTENCE OWNER

Alembic does not require root placement.

Its exact location should follow the runtime/persistence workspace while retaining the migration environment semantics.

### tests/

Target role:

    SPLIT

    owner-local unit/contract tests
        -> owning product/project workspace

    cross-workspace integration/acceptance/governance tests
        -> project-wide verification/integration owner

The target does not retain one universal tests/ merely by convention.

### schemas/

Target role:

    SPLIT BY AUTHORITY/CONSUMER

    project-development schemas
        -> project-development system

    product interchange schemas
        -> owning product capability or product-wide contract owner

    repository/project governance schemas
        -> owning project governance capability

    genuinely cross-plane contracts
        -> explicit integration contract owner

No generic schema bucket survives without a semantic reason.

### scripts/

Target role:

    SPLIT / ABSORB / RETIRE AS APPROPRIATE

    subsystem operation
        -> subsystem

    repository engineering/governance
        -> project engineering/governance

    historical research probe
        -> evidence/history or retire from active tooling

A script's file type is not an owner.

### tools/

Target role:

    REMOVE AS A DEFAULT ARCHITECTURAL CATEGORY

Current tools/project_knowledge is a first-class subsystem, not miscellaneous tooling.

Under G-DUAL it belongs under the project plane as the project-development system.

A future generic tools/ directory is allowed only if multiple genuinely repository-wide utilities exist whose natural owner really is repository tooling.

### experiments/

Target role:

    REPLACE UNIVERSAL PERMANENT BUCKET WITH LIFECYCLE MODEL

During active work, experiment execution should be owned by the capability/program it tests or by a clearly bounded project research program.

After qualification:

    durable result/evidence
        -> project evidence/knowledge architecture

    reusable production mechanism
        -> product/project owner

    obsolete executable experiment
        -> retire or preserve as historical material if reproduction value warrants it

This does not select DVC or any specific experiment tool.

### prototype_v0/

Target role:

    PRESERVE AS HISTORICAL DEVELOPMENT EVIDENCE
    BUT REMOVE ITS CURRENT PATTERN AS FUTURE CONVENTION

Its exact future path is R7/R8 work.

The likely semantic owner is project history/evidence, not product active architecture.

### docs/

Target role:

    SPLIT BY SEMANTIC OWNER; DO NOT RETAIN AS THE WHOLE INFORMATION ARCHITECTURE BY DEFAULT

Expected distinction:

    project authority/architecture/history
        -> project knowledge architecture

    product-local technical documentation
        -> owning product workspace/capability where appropriate

    product-owned methodological/source knowledge
        -> product-owned knowledge capability, not project documentation

    generated project-control views
        -> project-development system / project knowledge boundary

Research 218 is therefore genuinely subordinate to G-DUAL.

## 7. Why product/project is stronger than systems/apps/packages

The apps/packages/platform pattern is excellent when the dominant repository question is software deployability/reuse.

ADS has a different additional first-class distinction:

    ADS product runtime
        versus
    infrastructure/knowledge/governance used to build ADS

Calling both packages or systems loses that distinction.

Likewise, a top-level systems/ parent would put:

    frontend
    runtime
    project-development system

under one apparent class even though one governs the project that contains the others.

G-DUAL exposes that asymmetry rather than hiding it.

## 8. Why project/ is not a dumping ground

This is a critical risk.

project/ is acceptable only if its internal architecture is itself principled.

R6/R7 must distinguish at least:

    project-development system
    project knowledge/authority
    evidence/research lifecycle
    repository engineering/verification
    historical material

These are not allowed to become arbitrary siblings without definitions.

The existence of project/ therefore **does not solve Research 218 automatically**.

It establishes the correct higher-order owner inside which R7 must design the project information architecture.

## 9. Product-owned knowledge versus project knowledge

This distinction prevents a major future ambiguity.

### Product-owned knowledge

Knowledge the ADS product operates on or exposes as part of its functionality.

Examples may include:

    methodological knowledge
    source-universe content/models
    reusable knowledge bundles
    product data/model assets

Primary owner:

    product

### Project knowledge

Knowledge about developing/governing ADS itself.

Examples:

    architecture research
    specifications
    decisions
    checkpoints
    continuity
    implementation evidence
    operational development procedures

Primary owner:

    project

This means "knowledge" is not one physical category for the entire repository.

It is an asset type whose owner matters.

## 10. PSMF under G-DUAL

The relationship becomes conceptually clean:

    GENERIC PROJECT-DEVELOPMENT FRAMEWORK
                |
                | governed materialization
                v
    ADS/
        project/
            <project-development-system>/
                framework mechanism
                ADS instance policy/extensions
                local control state
                local contracts/tests

The exact subsystem name and internal shape remain R6 work.

The project remains self-contained.

The generic upstream remains non-authoritative.

## 11. Multi-language tooling

G-DUAL is compatible with current ecosystems.

Conceptually:

    product/<python-runtime-workspace>/
        pyproject.toml
        src/ads_system/
        tests/
        migrations/
        ...

    product/<frontend-workspace>/
        package.json
        src/
        tests/e2e/
        ...

    project/<project-system-workspace>/
        Python/package or other tooling as justified
        implementation
        tests
        contracts
        instance policy
        ...

At repository root, a workspace orchestrator may coordinate these.

R6 must determine whether uv workspaces, npm workspaces or simple path-based independent projects are actually needed.

No monorepo tool is selected by R5.

## 12. Placement decision rule

A future contributor should be able to classify a new artifact in this order:

    Q1
    Is this required by repository host/bootstrap tooling at true root?
        YES -> root candidate
        NO  -> continue

    Q2
    Does its primary responsibility belong to the ADS product as an
    operational system or product-owned asset?
        YES -> product/

    Q3
    Does its primary responsibility exist to build, govern, research,
    validate, reconstruct or preserve ADS as a development project?
        YES -> project/

    Q4
    Inside that plane, is there an evidence-backed independent workspace
    owner?
        YES -> that workspace

    Q5
    Is it genuinely cross-workspace within the same plane?
        YES -> explicit plane-level integration/governance owner

    Q6
    Is it historical rather than active?
        YES -> historical lifecycle disposition, not active-owner placement

If these questions cannot classify common artifacts cleanly, G-DUAL is falsified.

## 13. Future-growth stress result

G-DUAL handles the R4 scenarios without creating new root categories:

    multiple frontends/services
        -> product workspaces

    multiple Python packages
        -> product workspaces where justified

    PSMF
        -> project-development workspace

    large project knowledge
        -> project information architecture

    many experiments
        -> owner-local active work + project evidence lifecycle

    many historical programs
        -> project historical lifecycle

    private/local integration
        -> product or project depending responsibility;
           Level-0 external repository boundary remains possible

    cold-start contributor
        -> first decide product versus project

    selective CI
        -> workspace/owner boundaries

    another project using framework
        -> same project-system concept without copying ADS product taxonomy

## 14. Strongest criticism

The strongest criticism of G-DUAL is that product/project may be **too abstract**.

A new contributor might ask:

    Is CI "project"?
    Is methodological knowledge "product"?
    Is a benchmark "product" or "project"?
    Is a local runtime adapter product integration or development tooling?

The architecture succeeds only if R6/R7 answer these with clear ownership rules and examples.

If ambiguity remains high, D/F or a more conventional apps/packages structure should be reconsidered.

## 15. What R5 does not decide

R5 does not yet decide:

    exact names below product/ and project/
    exact name replacing project_knowledge
    exact project/ information hierarchy
    whether product/runtime becomes a uv workspace
    exact frontend internal architecture
    exact active-experiment execution mechanism
    historical archive format
    migration mechanics
    compatibility shims
    physical move order
    final Research 218 disposition

Those are downstream questions.

## 16. Recommended owner disposition

The evidence now supports one root architecture strongly enough for an owner decision:

    RECOMMENDED_TARGET
        G-DUAL
        PRODUCT_PROJECT_DUAL_PLANE_ROLE_FIRST_BOUNDED_WORKSPACE

Recommended decision:

    ACCEPT AS TARGET ARCHITECTURE FOR R6/R7 DETAILED DESIGN

This acceptance would **not** authorize physical migration.

It would authorize the next design stages to treat:

    product/
    project/
    true tool-required root

as the governing Level-1 architecture hypothesis while deriving Level-2 and Level-3 details.

If the owner does not accept it, R5 must remain open.

## 17. Current state

    R5=RECOMMENDED_TARGET_FROZEN
    RECOMMENDED_TARGET=G_DUAL
    OWNER_ACCEPTED_TARGET=NO
    ROOT_ROLES=PRODUCT_PROJECT_TRUE_ROOT
    PHYSICAL_MIGRATION_AUTHORIZED=false
    R6=BLOCKED_ON_OWNER_TARGET_DECISION
    R7=BLOCKED_ON_OWNER_TARGET_DECISION
    RESEARCH218=FROZEN
    RESEARCH177=UNCHANGED
    SPECIFICATION028=UNCHANGED
    W5_F0=PAUSED
    AO10=HELD
    AUTHORITY_SWITCH_ALLOWED=false
    NEXT=OWNER_R5_TARGET_DECISION
