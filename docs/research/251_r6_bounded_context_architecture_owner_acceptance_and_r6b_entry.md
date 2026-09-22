# Research 251: R6 Bounded-Context Architecture Owner Acceptance and R6-B Entry

**Date:** 2026-09-22
**Status:** R6 BOUNDED-CONTEXT / WORKSPACE ARCHITECTURE ACCEPTED / R6-B CURRENT-TO-TARGET MAPPING UNBLOCKED / NO PHYSICAL MIGRATION
**Parent program:** Research 240
**Accepted basis:** Research 249-250
**Owner decision:** ACCEPT
**Repository base before acceptance:** 26de53ff02df8b9a32ad195d211f634f0a9be500
**Scope:** Record explicit owner acceptance of the R6 responsibility/bounded-context/workspace architecture and authorize the non-destructive R6-B mapping stage. This does not authorize physical repository migration.

## 1. Owner decision

The owner explicitly chose:

    ACCEPT

This accepts the R6 target model in Research 250.

## 2. Accepted Product bounded contexts

    PC1  Project Intelligence
    PC2  Methodological Knowledge
    PC3  Evidence and Artifact Provenance
    PC4  Reasoning Orchestration
    PC5  Analytical Execution
    PC6  Product Interaction and Access
    PC7  Runtime Platform and External Boundary

## 3. Accepted Product workspace direction

    PW1  Core Product Runtime Workspace
         strong target workspace

    PW2  Product Interaction Workspace Family
         strong target workspace family

The accepted direction is a professional modular runtime, not premature microservice decomposition.

Logical contexts must remain explicit and extraction-ready even where they initially share a workspace.

## 4. Accepted Project bounded contexts

    JC1  Project Direction, Architecture and Memory
    JC2  Project Development Control System
    JC3  Research and Qualification
    JC4  Engineering, Verification and Delivery
    JC5  Collaboration and Contribution
    JC6  Historical Preservation

## 5. Accepted Project workspace direction

    JW1  Project Development System Workspace
         strong target workspace

JC1, JC3, JC4, JC5 and JC6 remain first-class responsibility contexts but do not automatically become executable packages/workspaces.

## 6. Accepted dependency invariant

    Project plane
        MAY inspect / build / test / qualify / release Product

    Product runtime
        MUST NOT depend on Project plane for runtime correctness

Immutable build/version/provenance metadata may cross this boundary only under explicit asymmetric ownership / generated-contract rules.

## 7. Accepted workspace/extraction discipline

A bounded context is not automatically a package, workspace, service or repository.

Extraction from the modular runtime requires evidence such as:

    independent scaling
    independent availability/fault domain
    materially distinct security boundary
    incompatible runtime/dependency needs
    independent release cadence
    sustained independent ownership/team boundary
    operational isolation requirement
    reusable distribution requirement
    demonstrated change-coupling benefit

## 8. R6-B authorization

R6-B may now perform:

    current artifact inventory -> accepted responsibility/context mapping

The mapping may classify current material as:

    direct target fit
    split across multiple target owners
    merged into another target owner
    implementation detail inside a workspace
    cross-workspace/project engineering concern
    historical-only
    superseded/replaced
    externalized
    retired
    unresolved pending R7/R8

R6-B must not move files yet.

## 9. Still prohibited

    physical migration
    package/workspace renaming in-place
    current folder deletion
    PSMF extraction
    authority switch
    W5-F0 resume
    AO-10 implementation

## 10. Current state

    R6_RESPONSIBILITY_MODEL=ACCEPTED
    R6_BOUNDED_CONTEXT_MODEL=ACCEPTED
    R6_WORKSPACE_DIRECTION=ACCEPTED
    R6_B_CURRENT_TO_TARGET_MAPPING=UNBLOCKED
    PHYSICAL_MIGRATION_AUTHORIZED=false
    R7=DOWNSTREAM_OF_R6B
    ROOT_ENTRY_REVIEW_BOUND=12
    ROOT_INTEGRATION_CONTRACTS=0
    NEXT=R6B_CURRENT_TO_TARGET_MAPPING
