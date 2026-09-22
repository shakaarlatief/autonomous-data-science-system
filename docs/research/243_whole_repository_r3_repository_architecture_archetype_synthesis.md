# Research 243: Whole-Repository R3 Repository Architecture Archetype Synthesis

**Date:** 2026-09-22
**Status:** R3 CANDIDATE SET FROZEN / NO ARCHETYPE SELECTED / R4 PROFESSIONAL-PATTERN AND STRESS-TEST REVIEW NEXT
**Parent program:** Research 240
**Evidence base:** Research 241-242
**Repository base:** 371a45001e6fb987362a07f8c9fe3cc71992b2b3
**Scope:** Construct serious replacement architecture families from the R0-R2 responsibility, lifecycle, dependency and qualification evidence. The candidates are architectural models rather than cosmetic folder proposals.

## 1. Candidate-design rules

R3 follows five rules.

### R3-R01: current paths do not receive incumbency privilege

No candidate receives credit merely for minimizing moves.

Migration cost will matter later, but it does not define the desired architecture.

### R3-R02: current concepts may disappear

A candidate may eliminate or replace current concepts such as:

    generic tools/
    generic schemas/
    generic scripts/
    root prototype_v0/
    one central tests/
    one central experiments/

if a stronger ownership model exists.

### R3-R03: conventional tooling constraints remain real

First-principles design does not mean ignoring ecosystems.

Python packaging, Alembic, pytest, Node/Vite, Playwright, GitHub Actions and repository-host conventions are real constraints/costs.

A candidate must explain when convention is worth keeping and when ownership clarity justifies deviation.

### R3-R04: knowledge/evidence is not an afterthought

ADS uses durable repository knowledge as project memory and authority.

A candidate that designs software cleanly but leaves project knowledge/evidence as an unstructured remainder is incomplete.

### R3-R05: PSMF is an input, not the root template

The project-development framework relationship must fit the candidate.

It must not force the rest of ADS into the same physical pattern.

## 2. Cross-candidate questions

Every candidate must answer:

    What is the primary top-level organizing principle?

    What is a first-class workspace?

    Where do subsystem-local tests live?

    Where do repository-wide/integration tests live?

    Where do schemas/contracts live?

    Where do persistence migrations live?

    What happens to generic scripts/tools buckets?

    How are active experiments distinguished from durable evidence?

    How are historical prototypes preserved?

    Where does the project-development system live?

    Where does durable project knowledge/history live?

    How does PSMF materialization fit?

    How does a new contributor infer ownership from the tree?

## 3. Candidate A: Refined Artifact-First Repository

### 3.1 Principle

Retain conventional repository-wide artifact families as the primary physical organization.

Conceptually:

    repository/
        src/
        tests/
        schemas/
        scripts/
        migrations/
        experiments/
        docs/
        tools/
        frontend/
        ...

The current structure would be improved substantially, but not replaced by vertical subsystem namespaces.

### 3.2 Project-development system

It remains distributed by artifact type:

    tools/<project-system>/
    schemas/<project-system>/
    tests/<project-system>/
    docs/<project-system>/
    experiments/<project-system>/

The name project_knowledge may still change.

### 3.3 Tests and schemas

Tests remain centralized.

Schemas remain centralized.

Ownership is expressed through subdirectories/names and semantic metadata rather than co-location.

### 3.4 Persistence

migrations/ may remain root-level because Alembic convention and root Python workspace make the arrangement straightforward.

### 3.5 Experiments/history

experiments/ remains the primary execution/evidence family.

prototype_v0 may move underneath a history/prototypes subfamily or remain as a documented exception.

### 3.6 Strengths

    strongest Python/ecosystem familiarity
    simple pytest discovery
    simple root build configuration
    low configuration duplication
    easy repository-wide searching by artifact type
    smallest conceptual distance from current operational tooling

### 3.7 Structural risks

    strong subsystems remain horizontally scattered
    schemas/tests/scripts continue to mix owners
    project-development PSMF materialization has no single obvious boundary
    root remains a mix because frontend is still a workspace peer of artifact roots
    ownership must be reconstructed from naming and conventions

### 3.8 Falsifier

Reject A if R4 shows that ADS's major subsystems increasingly require independent qualification, materialization or ownership boundaries that artifact-first placement obscures.

## 4. Candidate B: Strict Vertical Subsystem Repository

### 4.1 Principle

Major bounded systems own nearly all of their implementation artifacts.

Conceptually:

    repository/
        systems/
            ads-runtime/
                implementation/
                tests/
                contracts/
                migrations/
                docs/

            frontend/
                implementation/
                tests/
                design/
                docs/

            project-development-system/
                implementation/
                tests/
                contracts/
                instance-policy/
                docs/

            repository-governance/
                implementation/
                tests/
                contracts/

        evidence/
        project-memory/
        host-integration/

Exact names are placeholders.

### 4.2 Tests and schemas

Unit/contract tests and schemas are primarily co-located with owners.

Only genuinely cross-system integration/acceptance tests remain centralized.

### 4.3 Persistence

Database migrations live under the persistence-owning system/capability, not at generic root.

### 4.4 Scripts/tools

Generic scripts/ and tools/ disappear except for truly repository-wide bootstrap utilities.

Operational code moves to the system it operates.

### 4.5 Experiments/history

Experiments may be co-located with their owning system during active development, while durable cross-system evidence moves to an evidence layer.

Historical prototypes become explicitly historical workspaces rather than permanent peer systems.

### 4.6 PSMF

The materialized framework has a clean bounded home under the project-development system.

### 4.7 Strengths

    strongest ownership visibility
    high change locality
    clean PSMF subsystem boundary
    schemas/tests naturally follow owners
    scales conceptually as number of systems grows

### 4.8 Structural risks

    may create nested build/tooling complexity
    Python/pytest/Alembic conventions require deliberate configuration
    risks duplicating subsystem-local tooling/configuration
    cross-cutting concerns may be awkward or duplicated
    may overstate boundaries before deployment/release boundaries are mature

### 4.9 Falsifier

Reject B if professional-pattern review or ADS stress tests show that the system boundaries are not stable enough to justify nested workspaces and the operational cost materially outweighs ownership clarity.

## 5. Candidate C: Apps / Packages / Platform Monorepo

### 5.1 Principle

Use a conventional large-monorepo vocabulary based on executable applications, reusable packages and shared platform/tooling.

Conceptually:

    repository/
        apps/
            frontend/
            future deployable applications

        packages/
            ads-core/
            reusable-knowledge/
            project-development-framework-instance?
            other reusable libraries

        platform/
            persistence/
            repository-governance/
            integrations/

        tests/
            cross-package integration/acceptance

        evidence/
        project-memory/
        history/

Again, names are provisional.

### 5.2 Tests and contracts

Package-local unit tests/contracts can be co-located.

Cross-package integration tests remain centralized.

### 5.3 Persistence

Could live as a platform capability or with the package/application that owns the database model.

This candidate therefore still requires a persistence-ownership decision.

### 5.4 Project-development system

Could be a package if treated primarily as reusable code, or a first-class platform/project-system workspace if package vocabulary is too narrow.

This ambiguity is a key test.

### 5.5 Strengths

    familiar modern monorepo mental model
    good future fit if ADS grows many apps and reusable packages
    supports multiple language workspaces cleanly
    distinguishes deployables from reusable code

### 5.6 Structural risks

    may force ADS concepts into generic software-company categories
    project-development system is not obviously an app/package/platform
    project knowledge/evidence can become second-class
    domain/application boundaries may not match deployment/package boundaries
    "platform" can become a new miscellaneous bucket

### 5.7 Falsifier

Reject C if significant ADS responsibilities repeatedly fail to map naturally to app/package/platform without artificial naming or catch-all buckets.

## 6. Candidate D: ADS Bounded-Context Hybrid

### 6.1 Principle

Derive a small number of stable ADS-specific top-level architectural roles from actual responsibility and lifecycle evidence instead of copying artifact or generic monorepo taxonomy.

The physical root would distinguish, conceptually:

    product systems / user-facing execution
    project-development system
    evidence / experimentation
    project knowledge / authority / history
    repository engineering / host integration
    historical material

The exact names and whether each role deserves a physical root remain open.

### 6.2 Internal rule

Within each true bounded system:

    co-locate implementation
    local contracts
    local tests
    local configuration
    local migrations where naturally owned
    local operating documentation where appropriate

Keep only genuinely cross-system things at repository level:

    integration/acceptance tests
    repository governance
    shared exchange contracts
    durable project-wide authority/evidence
    host-specific root configuration

### 6.3 Project-development system

PSMF maps cleanly:

    generic upstream
        ->
    one bounded project-local project-development system
        framework materialization
        instance policy/extensions
        local control state
        subsystem contracts/tests

The final name remains open.

### 6.4 Product/runtime

The Python runtime and frontend may remain distinct technical workspaces while being grouped under a higher-order product/system role if evidence supports that relationship.

This avoids pretending that "same repository category" requires "same package/toolchain."

### 6.5 Experiments

Active experimental execution is separated conceptually from durable evidence.

A completed experiment may stop being an active executable workspace while its evidence remains part of project history.

### 6.6 Historical prototypes

prototype_v0 can remain reproducible historical evidence without defining a permanent root convention for future prototypes.

### 6.7 Strengths

    strongest fit to R2 evidence without forcing one universal convention
    can preserve ecosystem-native tooling inside bounded workspaces
    distinguishes real systems from artifact/lifecycle families
    makes project-development system first-class
    allows project knowledge/evidence to remain first-class
    supports future growth without one giant systems/ wrapper for unrelated roles

### 6.8 Structural risks

    custom taxonomy requires excellent definitions
    bad category naming could recreate today's ambiguity
    contributors cannot rely solely on generic monorepo expectations
    governance must prevent new catch-all roots
    requires more design work before implementation

### 6.9 Falsifier

Reject D if its stable top-level roles cannot be defined with crisp placement rules that remain understandable to a cold-start contributor without project-specific oral knowledge.

## 7. Candidate E: Polyrepo-Oriented Architecture

### 7.1 Principle

Use repository boundaries more aggressively for independently evolving concerns.

Possible independent repositories might eventually include:

    ADS product/runtime
    frontend application
    generic project-development framework
    historical/prototype programs
    private/local operational systems

The ADS repository would contain only material that is authoritative to ADS itself plus explicitly materialized dependencies where project sovereignty requires them.

### 7.2 PSMF

PSMF already contains one carefully justified polyrepo relationship:

    generic framework repository
        ->
    materialized local ADS instance

This does not imply every strong workspace should become a separate repository.

### 7.3 Strengths

    strongest lifecycle isolation
    independent release/permission/dependency boundaries
    clean external reuse
    smaller repositories per concern

### 7.4 Structural risks

    cross-repository atomic changes become harder
    project-wide provenance becomes more complex
    contributor reconstruction requires more repositories
    CI/integration coordination cost rises
    over-fragmentation is especially dangerous while ADS architecture is still evolving

### 7.5 Falsifier

Reject repository extraction for any concern whose lifecycle/dependency evidence does not justify the coordination cost.

## 8. Candidate F: Workspace-First Hybrid Monorepo

R2 suggests one additional family beyond Research 240's original minimum set.

### 8.1 Principle

Treat independently buildable/qualifiable workspaces as first-class, while retaining repository-wide artifact families only for genuinely cross-workspace concerns.

Conceptually:

    repository/
        workspaces/
            ads-runtime/
            frontend/
            project-development-system/

        integration/
            tests/
            shared-contracts/

        evidence/
        project-memory/
        engineering/
        history/

This differs from strict vertical B because not every domain/capability becomes a nested subsystem.

Only concerns with real build/lifecycle/qualification independence become workspaces.

### 8.2 Why R2 created this candidate

The evidence shows three especially strong boundaries:

    root ADS Python package
    frontend Node workspace
    project-development mechanism

But it does not yet justify making every Source Universe, retrieval, persistence or methodology concern its own workspace.

F therefore attempts to capture the proven boundaries without over-modularizing.

### 8.3 Strengths

    evidence-driven workspace count
    supports multiple toolchains
    cleaner than artifact-first for strong subsystems
    less fragmentation than strict vertical systems
    PSMF fits naturally

### 8.4 Structural risks

    "workspace" can become a technical criterion that misses non-build authority layers
    durable knowledge/evidence still needs a separate coherent architecture
    boundary threshold must be explicit
    future capabilities may oscillate between internal module and workspace

### 8.5 Falsifier

Reject F if build/qualification independence proves to be a poor proxy for stable architectural ownership.

## 9. Cross-candidate non-negotiable questions

R4 must challenge every candidate on these points.

### 9.1 Tests

The target must distinguish:

    owner-local unit/contract tests
        versus
    repository-wide integration/acceptance/governance tests

A one-folder answer is not assumed either way.

### 9.2 Contracts/schemas

The target must distinguish:

    implementation-local contracts
    inter-system exchange contracts
    repository/governance schemas

A universal schemas/ root is neither accepted nor rejected yet.

### 9.3 Scripts/tooling

The target must eliminate the semantic rule:

> "it is executable helper code, therefore it belongs in scripts/ or tools/."

Placement must follow responsibility.

### 9.4 Evidence

The target must define the lifecycle:

    active experiment
        ->
    qualified result
        ->
    durable evidence
        ->
    historical executable material, if still worth retaining

This is necessary to avoid accumulating permanent experiment workspaces indefinitely.

### 9.5 Historical material

Historical truth must remain reconstructable without forcing obsolete structures to remain active architecture peers forever.

### 9.6 Root configuration

Some files may need to stay at repository root because external tools conventionally resolve them there.

That is acceptable when explicitly justified.

"Clean root" is not a sufficient reason to fight tooling.

## 10. Initial comparative pressure from R2

Without selecting a winner, R2 places different pressure on the candidates.

### Candidate A pressure

R2 directly exposes A's weakness:

    tools/project_knowledge
    schemas/project_knowledge
    project-knowledge tests

already form one conceptual qualification unit while being physically scattered.

A must prove that conventional aggregation is worth that cost.

### Candidate B pressure

R2 does not show enough independent workspaces to justify turning every current concern into a vertical system.

B risks over-modularization.

### Candidate C pressure

C has a professional vocabulary but may fit ADS poorly if project authority/evidence and project-development infrastructure do not map naturally to apps/packages/platform.

### Candidate D pressure

D best matches the variety of roles seen in R2, but it has the highest taxonomy-design burden.

### Candidate E pressure

Only PSMF currently has strong enough evidence for an explicit reusable upstream boundary.

Broad polyrepo decomposition is not supported yet.

### Candidate F pressure

F fits the three strongest technical/lifecycle boundaries but must prove that a workspace-first top level can coexist cleanly with project memory/evidence and domain ownership.

## 11. Candidates carried to R4

All six candidates remain alive:

    A  REFINED_ARTIFACT_FIRST
    B  STRICT_VERTICAL_SUBSYSTEM
    C  APPS_PACKAGES_PLATFORM_MONOREPO
    D  ADS_BOUNDED_CONTEXT_HYBRID
    E  POLYREPO_ORIENTED
    F  WORKSPACE_FIRST_HYBRID_MONOREPO

R4 may:

    eliminate candidates
    merge candidates
    refine them
    introduce a missing professional pattern
    identify a hybrid not represented here

No candidate has owner acceptance.

## 12. R4 review plan

R4 should use external professional evidence selectively.

It should examine:

    mature Python project/monorepo conventions
    multi-language monorepos
    workspace-oriented repositories
    co-located versus centralized tests
    schema/contract ownership patterns
    database migration placement
    architecture documentation / ADR / project-memory conventions
    experiment/research artifact lifecycle
    vendoring/materialization/upstream synchronization patterns
    examples of bounded subsystem organization

External patterns are evidence, not authority.

R4 must then stress-test candidates against both:

    current ADS
        and
    plausible future ADS growth

## 13. Current state

    R3=CANDIDATE_SET_FROZEN
    CANDIDATES=6
    SELECTED_ARCHETYPE=NONE
    CURRENT_TREE=EVIDENCE_ONLY
    PHYSICAL_MIGRATION_AUTHORIZED=false
    PSMF=INPUT
    NEXT=R4_PROFESSIONAL_PATTERN_AND_FUTURE_GROWTH_STRESS_TEST
