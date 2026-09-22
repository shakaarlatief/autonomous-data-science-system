# Research 244: Whole-Repository R4 Professional-Pattern Review and Future-Growth Stress Test

**Date:** 2026-09-22
**Status:** R4 COMPLETE / D-F CONVERGENCE IDENTIFIED / NEW SYNTHESIS CANDIDATE G OPEN / R5 TARGET-ARCHITECTURE SELECTION NEXT
**Parent program:** Research 240
**Candidate basis:** Research 243
**Repository base before review:** 781bec2cdc6a0268918688e631f7ff5a57222761
**Scope:** Challenge the six internally derived repository archetypes against current professional tooling/patterns and future ADS growth scenarios without treating any external convention as authority.

## 1. Review discipline

External sources are used to answer:

    what professional tooling actually permits
    which conventions are strong defaults
    which layout choices are optional
    where mature monorepo guidance emphasizes ownership
    how experiment and documentation lifecycles can be separated

External sources do not select the ADS architecture.

The target must still fit ADS's own:

    lifecycle evidence
    authority model
    project-memory role
    PSMF topology
    multi-language tooling
    future-growth expectations

## 2. External evidence set

### E1. Python Packaging User Guide: src layout

Source:
https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/

Relevant evidence:

    src layout deliberately separates importable package code from
    repository-root files

    it helps prevent accidentally importing the in-development copy

    it makes the installed package the thing being tested/used

Implication for ADS:

    src/ads_system is not arbitrary clutter merely because it is a root
    artifact-type directory

    within a Python workspace, src layout is a strong professional convention

This supports preserving src layout **inside whatever workspace ultimately owns ads_system**.

It does not require the ADS repository root itself to remain artifact-first.

### E2. pytest good integration practices

Source:
https://docs.pytest.org/en/stable/explanation/goodpractices.html

Relevant evidence:

    pytest explicitly supports both:
        tests outside application code
        tests as part of application code

    it recommends src layout strongly in common new-project cases

Implication for ADS:

    the professional question is not "central tests or co-located tests?"

    both are supported patterns

    test placement should follow the kind of test and ownership boundary

This directly supports a hybrid:

    subsystem/package-local unit and contract tests
    repository-wide integration/acceptance/governance tests

when the architecture justifies that split.

### E3. uv workspaces

Source:
https://docs.astral.sh/uv/concepts/projects/workspaces/

Relevant evidence:

    uv supports one repository containing multiple Python packages

    each workspace member has its own pyproject.toml

    members can be applications or libraries

    one workspace can share a lockfile

    uv presents workspaces as useful when a codebase grows into multiple
    interconnected packages

    it also states that workspaces are not appropriate for every case,
    including members that need conflicting requirements or separate
    environments

Implication for ADS:

    multiple first-class Python workspaces/packages are technically viable

    we do not need to keep every Python concern inside one root package
    merely for uv convenience

    but we also should not manufacture packages where lifecycle/dependency
    evidence does not justify them

This supports evidence-driven workspace boundaries rather than strict verticalization.

### E4. Nx monorepo folder-structure guidance

Source:
https://nx.dev/docs/kb/folder-structure

Relevant evidence:

    Nx treats folder structure as a convention rather than a tooling mandate

    it distinguishes flat package layouts from grouped apps/libs layouts

    for larger workspaces, grouping improves navigability

    it explicitly recommends grouping by application/business scope rather
    than primarily by technical type

    code that changes together should sit together

Implication for ADS:

    professional monorepo practice supports ownership/co-change-driven grouping

    a flat set of technical artifact roots is not the only professional model

    generic wrappers such as apps/libs are useful only when their semantics fit

This strongly supports the R2 concern that ADS should not group unlike things merely because they share an artifact type.

### E5. npm workspaces

Source:
https://docs.npmjs.com/misc/workspaces/

Relevant evidence:

    npm workspaces support multiple nested local packages managed from
    one top-level package

Implication for ADS:

    if ADS later grows multiple JavaScript applications/packages, the frontend
    need not remain an isolated one-off root by necessity

    today's one frontend workspace does not itself justify converting the
    repository into a JavaScript-style apps/packages monorepo

### E6. Alembic script location

Source:
https://alembic.sqlalchemy.org/en/latest/tutorial.html

Relevant evidence:

    Alembic's migration script_location is configurable

    the generated directory name is conventional rather than a semantic
    requirement

Implication for ADS:

    migrations/ being at repository root is a tooling choice, not a hard
    Alembic constraint

    a future persistence workspace could own its migration environment
    without fighting Alembic's architecture

This strengthens the R2 conclusion that migration placement should follow persistence ownership unless root-level convenience wins explicitly.

### E7. DVC experiment versioning

Sources:
https://dvc.org/blog/ml-experiment-versioning/
https://dvc.org/blog/dvc-2-0-pre-release/

Relevant evidence:

    experiment metadata/state can be versioned without requiring a permanent
    visible branch/folder for every experiment

    experiments can remain lightweight and later be promoted into normal
    Git workspace/branch state

Implication for ADS:

    "an experiment happened" does not imply "a permanent top-level executable
    experiment workspace must remain forever"

    active experiment execution and durable accepted evidence are distinct
    lifecycle states

DVC is not being selected as ADS tooling here.

The useful evidence is the professional lifecycle pattern.

### E8. Diátaxis documentation architecture

Source:
https://diataxis.fr/

Relevant evidence:

    documentation can be organized systematically around user needs rather
    than as one undifferentiated artifact bucket

Implication for ADS:

    there is professional precedent for treating documentation architecture
    itself as a designed information system

    however ADS docs include project authority/evidence/history beyond normal
    product documentation, so Diátaxis cannot simply replace Research 218

This supports R7 first-principles design rather than flat accumulation.

## 3. Professional-pattern conclusions

The external review produces seven useful conclusions.

### P1. Ecosystem-native sublayouts should usually survive inside workspaces

Python src layout, pytest discovery and Alembic can all operate inside a bounded workspace.

Therefore:

> choosing subsystem/workspace-first repository architecture does not require abandoning professional Python conventions.

The real design decision is the **workspace boundary**, not whether src layout is professional.

### P2. No professional rule requires all tests at repository root

pytest officially supports both external and in-package tests.

Therefore centralized tests must be justified by integration/repository scope, not by an assumed Python rule.

### P3. No professional rule requires one repository-wide schemas directory

Nothing in the reviewed tooling creates that requirement.

The R2 evidence that schemas/ contains unrelated owners therefore remains significant.

### P4. Modern monorepo guidance favors ownership/scope over technical-type grouping at scale

Nx explicitly recommends grouping projects by application/business scope and keeping things that change together near one another.

This weakens pure artifact-first A as ADS grows.

### P5. Workspaces are a mechanism, not an architecture goal

uv and npm both support multi-project workspaces.

Neither says every concern should become a package/workspace.

This weakens strict vertical B and prevents over-modularization.

### P6. Root-level migrations are optional

Alembic supports configurable script locations.

Persistence ownership should decide placement.

### P7. Active experiments and durable historical evidence can have different representations

DVC's experiment lifecycle supports the conceptual separation already emerging from ADS history.

This materially weakens a permanent "every experiment remains a peer executable folder" model.

## 4. Future-growth stress scenarios

R4 evaluates the candidates against twelve future scenarios.

### S1. Multiple user-facing applications

ADS gains:

    Cockpit web app
    local desktop surface
    API/service surface
    automation/CLI surface

Need:
    clear app/workspace ownership without flattening them beside schemas/tests.

### S2. Multiple Python packages

ADS gains independently testable Python libraries/services.

Need:
    package boundaries, isolated tests/contracts and shared dependency handling.

### S3. PSMF materialization

The generic project-development framework is materialized into ADS and has local instance policy/extensions.

Need:
    one clear project-local boundary
    no external runtime authority
    framework-local contracts/tests
    clean project-specific extension seam.

### S4. Very large project knowledge

Research, specifications, evidence, decisions, operations and system knowledge grow by an order of magnitude.

Need:
    a systematic Level-3 information architecture
    no giant flat docs root.

### S5. High experiment volume

Many modeling/runtime/interface experiments run in parallel.

Need:
    active execution that does not permanently pollute repository root
    explicit promotion/retirement to durable evidence.

### S6. Historical programs accumulate

prototype_v0 is joined by later major discarded/falsification programs.

Need:
    historical reproducibility without treating obsolete programs as active peers.

### S7. More integrations and private/local execution

Public ADS coordinates cloud/local/private capabilities.

Need:
    clear public/private authority boundaries
    no generic "integration" dumping ground.

### S8. Cold-start contributor or agent

A new human or model opens the repository with no chat history.

Need:
    root categories communicate ownership and lifecycle directly.

### S9. Selective CI / affected execution

Repository becomes larger and full test execution is expensive.

Need:
    first-class project/workspace boundaries that CI can target.

### S10. Independent framework update

PSMF upstream changes while ADS changes independently.

Need:
    materialized framework boundary easy to diff/upgrade without touching product runtime.

### S11. Product/runtime architecture evolves

Persistence/retrieval/Source Universe may split or consolidate internally.

Need:
    root architecture stable enough not to reorganize for every internal refactor.

### S12. Another future ADS-like project is initialized

The project-development framework is reused elsewhere, but ADS-specific product/evidence architecture is not copied accidentally.

Need:
    generic framework boundary independent from ADS repository taxonomy.

## 5. Candidate A under stress: REFINED_ARTIFACT_FIRST

Professional tooling supports A strongly for a **single Python package**.

It performs well on:

    simple Python build/test ergonomics
    S11 internal product refactoring
    low configuration overhead

It performs poorly as ADS grows across:

    S1 multiple applications
    S3 PSMF materialization
    S8 cold-start ownership
    S9 selective workspace CI
    S10 independent framework update

The core problem is not that artifact-first is unprofessional.

The problem is that R2 already demonstrates multiple strong owners, while A keeps ownership secondary to artifact type.

R4 disposition:

    KEEP AS BASELINE
    DO NOT CARRY AS LEADING TARGET

## 6. Candidate B under stress: STRICT_VERTICAL_SUBSYSTEM

B performs well on:

    S3 PSMF
    S8 ownership
    S9 selective CI
    S10 independent framework update

But professional workspace guidance weakens its universalism.

uv specifically treats workspaces as appropriate for genuine packages/applications, not as a reason to turn every concern into one.

B risks making:

    persistence
    retrieval
    Source Universe
    repository governance
    every evidence family

into separate nested projects before they have independent build/release lifecycles.

R4 disposition:

    RETAIN AS BOUNDARY MAXIMALIST
    NOT LEADING TARGET

## 7. Candidate C under stress: APPS_PACKAGES_PLATFORM_MONOREPO

C gains professional credibility from Nx/npm conventions.

It performs well on:

    S1 multiple applications
    S2 multiple packages
    S9 selective CI

But ADS contains first-class concerns that do not map cleanly:

    project-development control system
    project authority/memory
    research/evidence
    historical falsification programs

"platform" risks becoming a new tools/ bucket.

"packages" risks treating internal authority/control machinery as if reuse/distribution were its defining property.

R4 disposition:

    RETAIN AS PROFESSIONAL REFERENCE
    DO NOT COPY TAXONOMY WHOLESALE

## 8. Candidate D under stress: ADS_BOUNDED_CONTEXT_HYBRID

D performs strongly across:

    S1 multi-app growth
    S3 PSMF
    S4 project knowledge growth
    S5 experiment lifecycle
    S6 historical programs
    S7 private/local boundaries
    S8 cold-start ownership
    S10 framework updates
    S12 reuse elsewhere

External evidence supports its key principle:

> organize around stable responsibility/scope, then use ecosystem-native
> conventions inside each owner.

Its weakness remains taxonomy risk.

If top-level roles are vague, D simply replaces today's miscellaneous roots with new miscellaneous roots.

R4 disposition:

    LEADING CONCEPTUAL MODEL
    REQUIRES CRISP ROLE DEFINITIONS

## 9. Candidate E under stress: POLYREPO_ORIENTED

PSMF demonstrates that one extra repository can be professionally justified.

But broad extraction performs poorly on:

    S8 cold-start reconstruction
    S11 product refactoring
    atomic changes across still-evolving ADS concerns

No R2 evidence justifies making frontend, persistence, experiments or project memory separate repositories now.

R4 disposition:

    ELIMINATE AS WHOLE-ADS DEFAULT
    RETAIN REPOSITORY EXTRACTION AS A PER-BOUNDARY OPTION
    PSMF REMAINS THE CURRENT JUSTIFIED CASE

## 10. Candidate F under stress: WORKSPACE_FIRST_HYBRID_MONOREPO

F performs strongly on:

    S1
    S2
    S3
    S9
    S10

Professional evidence from uv/npm/Nx supports multiple first-class workspaces.

But F is weaker on:

    S4 project authority/memory
    S5 evidence lifecycle
    S6 historical material

because "workspace" is a build/qualification concept, not a complete repository ontology.

R4 disposition:

    LEADING TECHNICAL MODEL
    INCOMPLETE AS WHOLE-REPOSITORY MODEL

## 11. D-F convergence

R4 finds that D and F solve complementary halves of the problem.

D answers:

> What stable kinds of responsibility should the repository recognize?

F answers:

> Which of those responsibilities deserve first-class technical workspaces?

They should not remain competing candidates.

This produces synthesis Candidate G.

## 12. Candidate G: Role-First Bounded-Workspace Hybrid

**Provisional name:** ROLE_FIRST_BOUNDED_WORKSPACE_HYBRID

This is an architectural rule set, not a final folder tree.

### G1. Root is organized by stable repository role, not artifact type

The top level should distinguish a small number of durable roles such as:

    active systems/workspaces
    project-wide authority/knowledge/memory
    evidence/research lifecycle
    repository engineering/governance
    historical material

Exact names and exact number remain R5 work.

### G2. Only real lifecycle/build boundaries become workspaces

A concern becomes a first-class workspace when evidence supports:

    independent toolchain/package
    independent qualification boundary
    meaningful dependency API
    independent lifecycle
    or PSMF materialization/reuse boundary

Current strong candidates:

    ADS Python runtime
    frontend
    project-development system

This does not imply three permanent top-level folders with those exact names.

### G3. Workspace-local artifacts follow the owner

Within a true workspace, default toward co-locating:

    implementation
    local tests
    local schemas/contracts
    local configuration
    local migrations when owned
    local technical documentation

while respecting ecosystem-native sublayouts such as Python src layout.

### G4. Cross-workspace concerns stay cross-workspace

Keep a distinct repository-level place for genuinely shared concerns such as:

    integration/acceptance tests
    exchange contracts spanning multiple workspaces
    repository integrity/governance
    host/CI configuration

Do not force them into one workspace.

### G5. Evidence has a lifecycle separate from active execution

An experiment/prototype may have:

    active executable state

then later:

    accepted durable result/evidence

and optionally:

    reproducible historical implementation

Those stages need not share one permanent physical shape.

### G6. Project memory/authority is not subordinate to product code

Research, decisions, specifications, checkpoints, continuity and other project authority remain first-class repository concerns.

Their final information architecture is R7.

### G7. Historical material is preserved without permanent active-peer status

prototype_v0 is the current exemplar.

It may remain exactly where it is until a migration is justified.

The target model only says:

> historical reproducibility does not grant permanent active architectural peer status.

### G8. PSMF fits as one bounded project-development workspace/system

The generic upstream may materialize into the project-development system while ADS-specific instance policy remains locally owned.

No product runtime dependency on the upstream is introduced.

## 13. Why G is not yet selected

R4 identifies G as the strongest synthesis, but R5 still has real work.

R5 must define:

    the exact stable top-level roles
    whether "workspace" deserves a physical wrapper
    whether product runtime + frontend share a higher product parent
    where repository engineering ends and project-development system begins
    how active evidence differs physically from durable evidence
    how historical material is exposed
    what remains at true repository root for tooling reasons
    how a cold-start contributor decides placement mechanically

Only after those definitions exist can G be selected or rejected.

## 14. R5 comparison set

Carry forward:

    G  ROLE_FIRST_BOUNDED_WORKSPACE_HYBRID
        leading synthesis

    D  ADS_BOUNDED_CONTEXT_HYBRID
        retained as conceptual fallback/reference

    F  WORKSPACE_FIRST_HYBRID_MONOREPO
        retained as technical fallback/reference

    A  REFINED_ARTIFACT_FIRST
        retained baseline/control

Do not carry as whole-repository targets:

    B  STRICT_VERTICAL_SUBSYSTEM
        too eager to modularize

    C  APPS_PACKAGES_PLATFORM_MONOREPO
        useful professional pattern, taxonomy fit not sufficient

    E  POLYREPO_ORIENTED
        repository extraction remains per-boundary tool, not default

## 15. R4 conclusion

The professional-pattern review does not support returning to today's artifact-first root merely because it is conventional.

It also does not support replacing it with a universal systems/ or apps/packages tree.

The strongest professional principle is:

> make real ownership/lifecycle boundaries first-class, then use native
> ecosystem conventions inside those boundaries.

For ADS, that principle must be combined with first-class project memory/evidence and PSMF self-containment.

Candidate G now expresses that combination.

## 16. Current state

    R4=COMPLETE
    LEADING_SYNTHESIS=ROLE_FIRST_BOUNDED_WORKSPACE_HYBRID
    SELECTED_TARGET=NONE
    OWNER_ACCEPTED_TARGET=NO
    EXTERNAL_PATTERN_REVIEW=COMPLETE_FOR_R5
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=R5_DEFINE_EXACT_ROOT_ROLES_AND_SELECT_TARGET_ARCHITECTURE
