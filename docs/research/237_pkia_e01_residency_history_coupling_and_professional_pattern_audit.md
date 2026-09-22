# Research 237: PKIA-E01 Residency History, Coupling and Professional Pattern Audit

**Date:** 2026-09-22
**Status:** PKIA-E01 RESIDENCY AUDIT COMPLETE / TOPOLOGY CANDIDATE SYNTHESIS NEXT / CLASSIFICATION STILL PENDING
**Evolution case:** `PKIA-E01`
**Case opening:** Research 236 / Checkpoint 567
**Frozen baseline:** Research 218
**Related physical boundary:** Research 177
**Governing implementation contract:** Specification 028
**Repository audit base:** `62ba6b729b34fbb736b19dc2a48fb38a148688a3`
**Scope:** Determine what earlier ADS work actually decided about architectural residency and reuse, measure present repository coupling, and compare that evidence with established professional distribution/scaffolding patterns before selecting any topology.

## 1. Executive finding

The repository evidence supports a precise conclusion:

> ADS previously made a deliberate V1 decision to keep the Candidate 01 implementation repository-local and separate from the ADS product runtime, but it did not perform a first-principles comparison of reusable-framework residency and project-instantiation topologies comparable to the current PKIA-E01 question.

The current implementation is neither purely generic nor irreducibly ADS-specific. It is a mixed project-local realization containing:

1. broadly reusable semantic/control algorithms;
2. repository-layout and package-path assumptions;
3. ADS migration/compatibility knowledge;
4. ADS-specific schema namespace choices and current project artifacts.

That mixture is consistent with Research 177's stated V1 intent. It also means that "extract the current folder unchanged into a package" and "keep everything exactly where it is" are both weaker formulations than the real architecture question.

Professional external patterns confirm that full materialization from a reusable upstream source into a self-contained project is an established engineering pattern. They also show multiple ways to preserve or omit an upstream relationship after generation. This validates T4/T5 as serious candidates, but does not yet establish that either is correct for ADS.

## 2. What earlier ADS architecture work did decide

### 2.1 Repository-native project authority was intentional

Research 124 framed the target as persistent project understanding with a stable project-controlled bootstrap. Candidate 01 then selected repository-native semantic sources as project authority.

That decision primarily concerns where a concrete project's durable knowledge and authority can be inspected and reconstructed. It does not by itself prove that every generic mechanism used to interpret that project must have the same ownership lifecycle or source repository.

Research 130 strengthened this distinction when KA-R02 was refined from "repository-native bootstrap" to **stable project-controlled bootstrap**, explicitly noting that the authority may still be the repository while the entry mechanism need not be file-only.

### 2.2 Research 177 deliberately separated development infrastructure from ADS product code

Research 177 made the important boundary explicit:

```text
project-development knowledge infrastructure
    !=
ADS product-domain runtime
```

It therefore selected:

```text
tools/project_knowledge/
schemas/project_knowledge/
docs/project_knowledge/
```

instead of placing the machinery under `src/ads_system/`.

Its reasons were concrete and legitimate for V1:

```text
version-controlled with the project
testable in the project
portable with the repository
no second distribution required
reuse of the repository-managed Python environment
clear separation from product runtime
```

Research 177 also called these physical choices deliberately reversible and stated that later extraction into a standalone package remained possible if another project needed the same tooling.

### 2.3 Specification 028 froze the V1 implementation assumption

Specification 028 then made repository-local tooling part of the production implementation and migration contract.

That was a valid implementation freeze for the selected candidate. It was not accompanied by an explicit comparative experiment over project-native, shared-runtime, hybrid, full-materialization and split-control topologies.

### 2.4 Research 206 through Research 218 optimized inside the repository boundary

The W5 information-architecture sequence deeply examined:

```text
natural-owner placement
physical folder/file roles
epistemic families
subject navigation
selective item carriers
generated views
historical navigation
authoring rules
migration sequencing
```

The design question was repeatedly framed as the future **repository** information architecture for ADS.

That work is therefore highly relevant to how an ADS-local instance should be organized, but it does not close the higher-level question now raised by PKIA-E01: whether all framework implementation, project instance state and project knowledge share one natural source/ownership topology.

### 2.5 Research 219 through Research 235 widened the reusable-looking surface

The activation/orchestration program added or formalized responsibilities such as:

```text
event ingress
bounded control context
control-obligation screening
progressive reconstruction and activation
process/workstream/collaboration/tool routing
authority and action-contract preflight
pre-dispatch conformance
postflight preservation
architecture-evolution feedback
Git lifecycle control
interaction continuity and recovery
accepted-obligation realization traceability
```

These responsibilities were discovered through ADS, but many are not inherently data-science-specific.

This does not establish that they should become a separate framework. It establishes that "this is only ADS-local documentation tooling" is no longer an adequate description of the design space.

## 3. What earlier work did not decide

The historical search from Research 124 through Research 218 found no explicit first-principles comparison answering all of the following together:

```text
Should generic project-control mechanisms have an independent canonical home?
Should a project depend on that home after initialization?
Should the full framework be materialized into a project?
Should a generated project retain an upstream lineage/update contract?
Should project-local extensions be allowed to diverge?
Can improvements flow from projects back to a generic source?
What must remain available to reconstruct a project if the framework source disappears?
Should an unrelated second project be able to use the architecture without copying ADS semantics?
```

The statement in Research 124 that no external framework should be copied wholesale referred to importing third-party prior art as ADS's successor architecture. It is not evidence against maintaining our own reusable generic source and materializing an instance from it.

## 4. Current implementation size and shape

At the audit base:

```text
tools/project_knowledge          54 Python source files   ~331 KB
schemas/project_knowledge         9 schema files          ~31 KB
docs/project_knowledge           31 non-cache files       ~375 KB
project-knowledge-focused tests  37 Python test files     ~476 KB
```

This is already substantial enough that residency is a real engineering lifecycle question rather than a cosmetic folder preference.

The activation/orchestration architecture is not yet a comparable production package. Much of it currently exists as governed research/contracts and therefore should not be treated as already-decoupled runtime code.

## 5. Current coupling decomposition

### 5.1 Broadly reusable mechanism layer

The following responsibilities are structurally reusable beyond ADS in their present conceptual form:

```text
typed immutable semantic records
declaration parsing and validation
semantic identity and transition handling
authority closure and conflict handling
workstream DAG semantics
scope normalization
capture/promotion mechanics
source/revision descriptors
deterministic derived-view mechanics
current-state projection mechanics
risk/obligation projection mechanics
Git-snapshot-based reproducibility
```

The `pure_*.py` functions and core model/authority/identity/workstream code especially resemble framework mechanisms rather than ADS product logic.

### 5.2 Repository-layout coupling

A static scan found repository/path coupling literals in 23 of 54 Python files. Many are intentional generator-closure bindings rather than defects, but they prove that the current package is not location-neutral.

Examples include hard-coded expectations for:

```text
tools/project_knowledge/
schemas/project_knowledge/
docs/project_knowledge/generated/
docs/project_knowledge/captures/
```

View definitions also bind their exact implementation file paths as part of deterministic generator provenance. A future extraction/materialization design must preserve equivalent provenance without assuming that the current path strings are universal.

### 5.3 ADS continuity and migration coupling

`services/compatibility.py` knows the legacy/live ADS compatibility surfaces directly:

```text
docs/current_routing.json
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/project_knowledge/generated/compatibility_shadow/
```

This is not generic framework behavior in the same sense as identity closure or workstream DAG validation. It is an ADS migration adapter against a specific continuity architecture.

A reusable design could still support compatibility adapters, but the adapter and the engine should not be confused.

### 5.4 ADS historical-fixture coupling

`services/discovery.py` contains explicit exclusions for numerous ADS research fixture families, including Candidate 01 probe, baseline and qualification directories.

This is strong evidence of an instance/migration-policy layer currently embedded inside the implementation package.

Again, this is not a defect under the V1 contract. It is evidence about where a future reuse boundary might naturally split.

### 5.5 Schema namespace coupling

All nine current JSON Schemas use IDs under:

```text
https://schemas.ads.local/project-knowledge/...
```

and the project-boundary profile contains a `PROJECT_INTEGRATION_BOUNDARY` constant.

Most schema structure is conceptually reusable, but the current namespace deliberately identifies an ADS-local realization. A genuine cross-project framework would need to decide whether schema identity is framework-owned, project-owned, parameterized, versioned separately, or materialized with an instance-specific namespace.

### 5.6 Project-local knowledge remains naturally local

Nothing in this audit weakens the case for keeping the actual project's authoritative knowledge with the project.

Research, specifications, decisions, checkpoints, workstream state, operational procedures, evidence and current project authority benefit strongly from project-local Git provenance and reconstruction.

The open question concerns the machinery and reusable architecture around that knowledge, plus the exact shape of the project-local instance.

## 6. Professional analogue patterns

This audit uses external patterns as mechanism evidence only. None is adopted as an ADS design template.

### 6.1 GitHub repository templates: one-time full materialization

GitHub documents template repositories as a way to generate a new repository with the template's directory structure and files. Repositories created from a template start new history rather than behaving as ordinary forks.

Sources:

```text
https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository
https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template
```

Transfer:

```text
generic source
    -> full materialization
    -> independent project repository
```

This is direct professional precedent for T4. It does not by itself solve later framework updates.

### 6.2 Cookiecutter: remote/local template to independent generated project

Cookiecutter explicitly creates projects from project templates. Templates may live locally, in archives, or in remote VCS repositories, and generation writes an output project tree.

Sources:

```text
https://cookiecutter.readthedocs.io/en/stable/
https://cookiecutter.readthedocs.io/en/latest/overview.html
```

Transfer:

```text
external reusable template
    -> parameterized generation
    -> materialized project
```

This again validates full materialization as an ordinary engineering topology. Cookiecutter is stronger as initialization precedent than as an update-lineage precedent.

### 6.3 Copier: materialization with an optional governed update lineage

Copier explicitly supports both project generation and later synchronization from an evolved versioned template. Its update flow records generation answers, uses Git-versioned templates, attempts to preserve project evolution, and exposes conflicts rather than assuming template state can overwrite the project safely.

Sources:

```text
https://copier.readthedocs.io/en/stable/generating/
https://copier.readthedocs.io/en/stable/updating/
```

Transfer:

```text
versioned generic source
    -> materialize project
    -> project evolves locally
    -> optional explicit template update
    -> reconcile project and template evolution
```

This is particularly relevant to T5. It shows that self-contained materialization and later upstream synchronization are not mutually exclusive.

### 6.4 Backstage Software Templates: centralized scaffolding into project repositories

Backstage Software Templates load code skeletons, apply parameters and actions, and can publish generated results to GitHub or GitLab.

Sources:

```text
https://backstage.io/docs/features/software-templates/
https://backstage.io/docs/features/software-templates/adding-templates/
```

Transfer:

```text
central organization-level scaffolding capability
    -> governed inputs/actions
    -> project repository creation
```

This is relevant where the generic architecture becomes an organizational project-bootstrap capability rather than a runtime dependency of every generated project.

### 6.5 Git submodules: pinned external dependency with separate history

Git documents submodules specifically for using another separately developed project from within a parent project while keeping histories separate. The parent records a particular submodule commit.

Source:

```text
https://git-scm.com/book/en/v2/Git-Tools-Submodules
```

Git's own discussion highlights the trade-off between using a shared external library, copying source into the project, and keeping a separate project embedded/pinned through a submodule.

Transfer:

```text
project
    -> explicit dependency on exact external repository revision
```

This is evidence for T2/T3-like dependency topologies. It also makes external availability, multi-repository ergonomics and local customization/upgrade mechanics first-class concerns.

### 6.6 GitHub forks: independent repository with an explicit upstream relationship

GitHub describes forks as separate repositories that start from an upstream repository, have their own settings/permissions, and remain connected to the upstream for collaboration and synchronization.

Sources:

```text
https://docs.github.com/en/pull-requests/reference/forks
https://docs.github.com/en/pull-requests/how-tos/work-with-forks
```

Transfer:

```text
upstream repository
    <-> explicitly related downstream repository
```

This is useful lineage evidence but may be a poor direct fit for independent project instances, because a project's semantic identity is not necessarily "a fork of the framework." The pattern is evidence for explicit upstream relation mechanics, not a recommendation to use GitHub fork networks.

## 7. Strong conclusions from the combined audit

### 7.1 Full materialization is professionally legitimate

The owner's T4/T5 idea is not an unusual workaround. Mature developer tooling commonly separates a reusable source/template from a fully generated project.

The architectural question is therefore not whether full materialization is "professional enough." It is whether its trade-offs best fit ADS's stronger requirements for semantic authority, self-hosted reconstruction, controlled evolution and project-specific divergence.

### 7.2 Reuse and runtime dependency are independent decisions

A framework can be reusable without remaining an operational dependency after project creation.

Likewise, a project can be self-contained while retaining provenance about the framework version that originally materialized it.

### 7.3 Self-containment and upgradeability are not mutually exclusive

Copier demonstrates the general mechanism family:

```text
materialized local state
+
recorded upstream/version lineage
+
explicit update operation
+
conflict handling
```

ADS would require stronger authority/provenance controls than a normal template updater, but the topology itself is credible.

### 7.4 The current package has a plausible seam, not a ready-made extraction

The implementation already exhibits a rough separation between reusable algorithms and ADS-specific repository/migration policy, but the separation is incomplete.

A future framework boundary would therefore require design/refactoring. It should not be described as simply moving `tools/project_knowledge/` into another repository.

### 7.5 The current repository-local architecture still has major strengths

Keeping the complete active architecture with the project provides:

```text
single-repository provenance
offline reconstruction
exact version coupling to project state
no package/service availability dependency
simple archival
easy forensic inspection
atomic project + architecture changes where appropriate
```

PKIA-E01 must preserve those benefits or replace them with stronger ones. Reuse alone is not sufficient reason to externalize anything.

## 8. Discriminating scenarios for candidate synthesis

The next candidate comparison must test at least these scenarios:

```text
S1  Fresh unrelated Project B is initialized from zero.

S2  Project B must remain fully reconstructable years later when the
    generic framework source is unavailable.

S3  The generic framework releases a critical correctness fix after
    Project B has heavily customized its local architecture.

S4  Project B intentionally diverges because its governance needs differ.

S5  A project-local discovery appears broadly reusable and should be
    contributed back without making ADS or Project B the generic authority.

S6  One framework version supports many projects with different project
    knowledge, subjects, workstreams and private/public boundaries.

S7  A framework upgrade changes schema or control semantics and therefore
    requires governed migration rather than blind file replacement.

S8  The project is cloned onto a clean machine with no hidden service,
    no prior chat and no access to optional external infrastructure.

S9  The project changes AI provider or loses one orchestration integration.

S10 The generic framework itself is retired, renamed or replaced.

S11 Project-specific evidence must remain immutable/provenance-correct even
    while framework implementation evolves.

S12 A security/correctness problem requires a bounded update across many
    materialized projects without silently overwriting local policy.
```

## 9. Candidate-design implications

The next topology synthesis should treat these as separate axes rather than one yes/no choice:

```text
canonical generic source location
project-local materialization depth
runtime dependency after materialization
lineage metadata
upgrade relationship
project divergence policy
project-to-framework contribution path
schema ownership/versioning
generic vs instance configuration boundary
compatibility/migration adapter ownership
bootstrap and disaster-recovery requirements
```

For example, "full materialization" does not determine whether upgrades exist, and "external engine" does not determine where project knowledge lives.

## 10. EvolutionCase state after the audit

```text
PKIA_E01=OPEN
TRIGGER_STATE=OBSERVED
EVIDENCE_BOUND=true
RESIDENCY_HISTORY_AUDIT=COMPLETE
CURRENT_COUPLING_AUDIT=COMPLETE
PROFESSIONAL_PATTERN_AUDIT=INITIAL_PASS_COMPLETE
CLASSIFICATION=CLASSIFICATION_PENDING
FINAL_DISPOSITION=NOT_DECIDED
RESEARCH218=FROZEN_BASELINE_RETAINED
RESEARCH177=UNCHANGED
SPECIFICATION028=UNCHANGED
AO10=HELD
W5_F0=PAUSED
AUTHORITY_SWITCH_ALLOWED=false
NEXT=SERIOUS_TOPOLOGY_CANDIDATE_SYNTHESIS_AND_STRESS_TEST
```
