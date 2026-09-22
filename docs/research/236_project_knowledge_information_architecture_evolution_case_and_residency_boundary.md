# Research 236: Project-Knowledge Information-Architecture Evolution Case Opening and Residency Boundary

**Date:** 2026-09-22
**Status:** GOVERNED EVOLUTION CASE OPEN / EVIDENCE BOUND / CLASSIFICATION PENDING / W5-F0 AND AO-10 REMAIN HELD
**Evolution case:** `PKIA-E01`
**Governing evolution architecture:** Research 223 / AO-4 Governed Evolution Cases
**Primary frozen baseline:** Research 218 / W5 final information architecture
**Related physical-boundary baseline:** Research 177 / selected Candidate 01 physical architecture
**Governing implementation contract:** Specification 028
**Current project-development authority:** current continuity architecture
**Interaction:** ChatGPT / `chatgpt-29` / `29 - Project Knowledge Information Architecture Evolution`
**Scope:** Reconsider the physical information architecture from first principles, beginning one layer above the internal ADS repository hierarchy: the residency, ownership, reuse, instantiation and evolution boundary of the project-development knowledge/control architecture itself.

## 1. Why this EvolutionCase is now open

Checkpoint 566 required a governed AO-4 EvolutionCase against Research 218 before AO-10 or W5-F0 continues.

The immediate owner challenge is more fundamental than folder placement:

> Where should the project-development knowledge/control architecture itself live, and what relationship should exist between a reusable generic architecture and a concrete project-specific instance?

The question includes the project-knowledge substrate, reconstruction, activation/orchestration, workstream/control behavior, architecture-evolution governance, collaboration routing and related project-development infrastructure. It does not concern the ADS product runtime itself except where repository boundaries interact.

Research 218 remains the accepted frozen baseline while this case is evaluated. Opening this case does not silently amend or supersede Research 218, Research 177 or Specification 028.

## 2. AO-4 case record

```text
case identity
    PKIA-E01

trigger sources
    explicit_owner_architecture_challenge
    scale_or_maintenance_pressure
    new_empirical_evidence_from_activation_orchestration

trigger state
    OBSERVED

primary affected contract / semantic owner
    Research 218 physical information architecture

exact affected Research 218 blob
    345db82a0e64983e5b223910667de0f95ed4db3b

related affected physical-boundary contract
    Research 177 selected Candidate 01 physical architecture

exact affected Research 177 blob
    9e8219be6f803252fd4bf7bfd4dbc5ae8a697486

related governing implementation contract
    Specification 028

exact affected Specification 028 blob
    70db025eefa69a8dec43b04dfdae87f5700754c9

case-opening repository head
    770ad49c9d503f213eeac3d66c611ad38e31ca5b

current accepted architecture
    Research 218 remains frozen baseline
    Candidate 01 remains selected
    Specification 028 remains governing
    current continuity remains operational authority

candidate classification
    CLASSIFICATION_PENDING

final disposition
    NOT YET DECIDED

owner decision
    REQUIRED LATER FOR MATERIAL KEEP / CLARIFY / AMEND / SUPERSEDE / REOPEN

affected-scope control state
    W5-F0 remains paused
    AO-10 remains held
    no authority switch
```

## 3. Existing evidence already establishes a real boundary question

Research 177 explicitly concluded that project-development knowledge infrastructure is infrastructure around development of ADS, not an ADS product-domain subsystem. It therefore kept the production implementation out of `src/ads_system/` and placed it in repository-local `tools/project_knowledge/`, with related schemas and documentation in repository-local homes.

Research 177 also made two materially different statements at once:

1. repository-local implementation was the preferred V1 physical boundary;
2. later extraction into a standalone package remained possible if another project needed the same tooling.

Specification 028 subsequently froze repository-local tooling as part of the V1 implementation and migration contract.

Research 206 through Research 218 then concentrated on the future physical and authoring architecture **within the ADS repository**. They deeply evaluated natural-owner placement, hybrid physical organization, subject navigation, item carriers, history, generated views and migration behavior. The current evidence does not show a comparably explicit first-principles comparison of the higher-level residency/instantiation topologies now under challenge.

The later activation/orchestration program materially strengthens the reason to ask this question. Research 219 through Research 235 introduce responsibilities such as event ingress, reconstruction activation, control-obligation screening, collaboration routing, Git lifecycle, architecture-evolution feedback, preservation and realization traceability. Many of these responsibilities are project-development concerns that are not intrinsically specific to data science or to the ADS product runtime.

This does not prove that they belong outside the ADS repository. It proves that the repository-local assumption deserves explicit evaluation rather than being inherited accidentally from where the architecture was developed.

## 4. Fundamental decomposition to test

The investigation must distinguish at least three conceptual layers before deciding physical residency:

```text
A. GENERIC PROJECT-DEVELOPMENT FRAMEWORK / MECHANISMS
   reusable algorithms, schemas, control semantics and tooling that
   could in principle serve more than one project

B. PROJECT-SPECIFIC ARCHITECTURE INSTANCE / CONFIGURATION
   the concrete policies, subjects, authority rules, workstreams,
   project identity, control state and extensions of one project

C. PROJECT KNOWLEDGE / EVIDENCE
   the actual project's research, specifications, decisions,
   operational records, checkpoints, implementation evidence and history
```

The investigation must not assume that these three layers share one natural lifecycle or one natural repository merely because they currently coexist.

It must also not assume that reuse requires a permanent shared runtime dependency.

## 5. Full materialization is a first-class candidate

A specific owner clarification must remain in the design space:

> A generic architecture may exist outside a project as a complete reusable source, while applying it to a project may materialize a complete self-contained copy/instance inside that project. The instantiated project may then be fully independent of the external source and may become substantially larger through project-specific state, knowledge, history, policy and extensions.

Conceptually:

```text
generic framework
    ->
materialize / instantiate
    ->
project-local complete architecture
    + project-specific configuration
    + project knowledge
    + project-specific evolution
```

This topology is distinct from both a thin local configuration over a permanently external shared runtime and a project-native architecture with no reusable upstream source.

The investigation must evaluate whether framework-to-project updates, project-to-framework contributions, intentional divergence, migration and lineage are needed or desirable. It must not assume continuous coupling after materialization.

## 6. Candidate topology families that must be compared

The case must include genuinely different topology families. At minimum:

```text
T1 PROJECT-NATIVE ONLY
   complete architecture exists and evolves only inside each project

T2 SHARED EXTERNAL RUNTIME
   projects depend on an external common framework/runtime

T3 HYBRID EXTERNAL ENGINE + LOCAL INSTANCE STATE
   generic mechanisms external, project-specific architecture/state local

T4 FULL MATERIALIZATION / TEMPLATE
   generic architecture maintained externally as reusable source;
   each project receives a complete self-contained local instance

T5 FULL MATERIALIZATION + GOVERNED UPSTREAM RELATIONSHIP
   complete local instance remains self-contained, while selected
   framework upgrades and/or project-derived generic improvements may
   cross an explicit migration/contribution boundary

T6 SPLIT CONTROL REPOSITORY OR SERVICE
   material project-control/knowledge responsibilities live outside the
   main project repository in a companion repository/service
```

These are starting families, not a frozen exhaustive taxonomy. Stronger variants may be added when evidence warrants them.

## 7. Evaluation dimensions

The topology decision must be evaluated before the internal folder hierarchy is redesigned.

At minimum evaluate:

```text
project self-containment and reconstructability
generic reuse across unrelated projects
authority clarity
version/provenance integrity
framework and project lifecycle independence
upgrade and migration safety
intentional divergence
project-to-framework feedback
bootstrap from zero
offline/local usability
external dependency and availability risk
security and trust boundary
tool/runtime portability
human inspectability
AI-agent inspectability
Git/repository ergonomics
testability and reproducibility
multi-project maintenance cost
project-specific extensibility
risk of accidental coupling
risk of uncontrolled forks
long-term scaling
ability to survive framework retirement or provider change
```

A topology that is elegant in abstraction but makes one concrete project unreconstructable without hidden external infrastructure is not automatically professional. Conversely, copying all machinery into every project is not automatically professional merely because it maximizes local self-containment.

## 8. What is not yet being changed

This case does not currently change:

```text
Candidate 01 semantic identity model
authority-resolution semantics
one natural authoritative owner principle
workstream semantics
capture/promotion semantics
subject architecture
Research 218 internal hierarchy
Specification 028
W5 migration state
AO-10 obligations
current continuity authority
```

Any of these may be challenged later only if evidence from the residency investigation independently reaches them.

## 9. Required evidence sequence

The next work should proceed in this order:

1. reconstruct the historical reasons for repository-local placement and determine exactly which residency alternatives were and were not evaluated;
2. decompose the current project-knowledge and activation/orchestration implementation into generic, project-specific and ADS-specific responsibilities;
3. audit the current repository for actual coupling points between those responsibilities;
4. research professional analogue patterns for reusable frameworks, generators/templates, vendored/self-contained instances, project-local control metadata and governed upgrades without copying any external framework wholesale;
5. construct and stress-test serious topology candidates against current ADS and at least one hypothetical unrelated project;
6. only after the topology boundary is understood, reconsider Research 218's internal physical hierarchy;
7. use independent review when candidate alternatives are concrete enough for another collaborator to provide marginal epistemic value;
8. obtain an explicit owner disposition under AO-4 before realization.

## 10. Collaboration disposition

Claude review is not required merely to open the case.

The preferred collaboration point is after the repository-local evidence audit and an initial topology candidate packet exist. At that point an independent-then-comparative or adversarial review can challenge the residency assumptions and candidate trade-offs without spending scarce review effort on an underspecified question.

If independent review is used, the collaboration request should preserve a neutral problem statement and an exact pre-candidate review target before exposing the ChatGPT candidate synthesis.

## 11. Current case state

```text
PKIA_E01=OPEN
TRIGGER_STATE=OBSERVED
EVIDENCE_BOUND=true
CLASSIFICATION=CLASSIFICATION_PENDING
RESEARCH218=FROZEN_BASELINE_RETAINED
RESEARCH177=RELATED_PHYSICAL_BOUNDARY_UNDER_REVIEW
SPECIFICATION028=UNCHANGED
W5_F0=PAUSED
AO10=HELD
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=RESIDENCY_HISTORY_AND_COUPLING_AUDIT
```
