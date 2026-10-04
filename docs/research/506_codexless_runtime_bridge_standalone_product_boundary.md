# Research 506: Codexless Runtime Bridge standalone-product boundary and extraction obligation

**Date:** 2026-10-04
**Status:** STANDALONE PRODUCT BOUNDARY ACCEPTED AS R0 INPUT / EXTRACTION DEFERRED
**Parent:** Research 502-505
**Scope:** Preserve the architectural conclusion that Codexless Runtime Bridge is reusable developer infrastructure rather than an ADS-owned subsystem, define the ownership boundary, and record the future professionalization/extraction obligation without interrupting the current R0 Project-System design.
**Authority:** Architecture-program input only. This record does not create a new repository, move code, change Runtime Bridge authority, alter the current private runtime deployment, or authorize extraction.

## 1. Conclusion

Codexless Runtime Bridge should be treated as a potentially standalone reusable software product.

Its generic purpose is broader than ADS:

    ChatGPT / compatible caller
        -> bounded trusted capability surface
        -> local machine / repositories / Git / GitHub / browser / tools / controlled processes.

ADS is one important consumer and proving environment.

The fact that Runtime Bridge was designed and professionalized while working inside ADS does not make ADS the correct long-term ownership boundary for the generic product.

## 2. Target ownership boundary

The long-term target should distinguish three responsibilities.

### A. Standalone generic Runtime Bridge product

A future dedicated repository, provisionally:

    codexless-runtime-bridge

would own the current canonical product architecture for generic capabilities such as:

    bounded workspace authority
    local command execution
    Git operations
    GitHub integration
    browser/tool mediation
    credentials and authorization handling
    capability schemas
    provider-neutral executor surfaces
    installation/update/release machinery
    security/threat model
    recovery and rollback
    versioning
    public documentation
    tests and CI/CD
    extension/capability architecture.

The exact repository name and topology remain open.

### B. Private machine/deployment state

Private host/runtime material should be separately owned.

The current:

    autonomous-data-science-system-local-runtime

may contain a mixture of:

    generic Runtime Bridge implementation
    ADS-specific configuration
    host-specific deployment state
    private ADS evidence
    release/staging material
    historical experiments.

It must be classified before any rename or split.

Possible future outcomes include:

    keep an ADS-specific private companion
    create a generic private deployment/environment repository
    split generic and ADS-specific responsibilities
    retire obsolete material.

No option is selected here.

### C. ADS integration

The ADS repository should ultimately retain only what ADS itself owns, for example:

    ADS requirements on execution infrastructure
    ADS workspace/policy configuration
    ADS-specific capability packs or adapters
    exact qualified Runtime Bridge version/release
    ADS integration tests
    ADS AO integration
    ADS WARRANT-F integration
    ADS-specific qualification evidence
    historical provenance explaining why earlier Runtime Bridge work happened inside ADS.

Generic Runtime Bridge internals should not remain canonically owned by ADS merely because they originated here.

## 3. Historical evidence stays historical

Existing ADS Research/Checkpoint records about Runtime Bridge must not be rewritten or deleted merely to make the future ownership boundary look cleaner.

They remain legitimate historical evidence of how ADS and Runtime Bridge co-evolved.

The forward rule is:

    historical ADS record
        remains historical evidence

    current generic product architecture
        eventually belongs to Runtime Bridge's own product repository

    ADS future records
        govern ADS integration and qualification only.

## 4. Relationship to PSMF

There is a useful analogy with PSMF but the two should not be conflated.

PSMF is approximately:

    generic Project-System framework
        -> materialized project-sovereign Project System.

Runtime Bridge is more naturally:

    generic reusable execution/developer-infrastructure product
        -> configured/extended per project.

A project does not necessarily need its own complete copied Runtime Bridge implementation.

The stronger default is one generic bridge product with bounded project/workspace policies and project-specific adapters where needed.

This remains an R0/R1 design question, not a frozen deployment topology.

## 5. Generic versus project-specific classification

Before extraction, existing Runtime Bridge capabilities should be classified into at least:

    GENERIC_CORE
    GENERIC_OPTIONAL_MODULE
    ADS_CAPABILITY_OR_POLICY_PACK
    HOST_PRIVATE_DEPLOYMENT
    HISTORICAL_OR_EXPERIMENTAL
    RETIRE.

Examples of ADS-specific behavior may include bounded P4/P5/P6-style procedures, phase-specific project controls, exact ADS repository assumptions, or ADS migration actions.

Those should not force the generic product API to know ADS semantics.

## 6. Project-System dependency direction

The future ADS Project System should depend on execution infrastructure through a provider-neutral boundary.

Conceptually:

    Project System / AO
        -> executor or action-adapter contract
            -> Codexless Runtime Bridge
            -> GitHub connector
            -> Claude-side connector
            -> local/direct executor
            -> future executors.

Therefore:

    AO != Runtime Bridge
    Project System != Runtime Bridge
    ADS != Runtime Bridge.

Runtime Bridge may be a powerful preferred adapter without becoming semantic authority or a mandatory universal provider.

## 7. Professionalization requirement

The standalone Runtime Bridge should eventually receive the same architectural discipline used for ADS:

    first-principles scope and architecture
    no preservation rights for current folders/code
    clean public repository
    professional package/module boundaries
    security/threat model
    provider-neutral extension interfaces
    tests
    CI/CD
    releases
    semantic versioning
    changelog
    installation/update lifecycle
    migration from the current implementation
    compatibility policy
    documentation
    contribution/development guidance
    recovery/rollback.

The current implementation is evidence and reusable material, not the target by default.

## 8. Timing

Do not derail R0 by immediately extracting Runtime Bridge.

The correct sequence is:

    1. R0 defines the Project System's external execution/tool boundary.
    2. R1 freezes what ADS actually requires from execution infrastructure.
    3. A dedicated Runtime Bridge extraction/professionalization program inventories current generic versus ADS versus host-private material.
    4. That program designs the standalone product from first principles.
    5. Existing implementation is migrated into the new ownership boundary.
    6. ADS switches to consuming the qualified standalone product through its bounded adapter/configuration surface.

The dedicated program may begin earlier only if R0 requires an empirical Runtime Bridge probe whose result cannot be obtained otherwise.

## 9. R0 consequence

R0 must explicitly evaluate:

    what interface the Project System requires from external execution infrastructure;
    what belongs in AO versus the executor;
    what capabilities are generic versus ADS-specific;
    how workspace/project policy is supplied without hard-coding ADS into the bridge;
    how execution receipts/evidence return to V03/WARRANT-F;
    how local/private deployment state is separated from generic product source;
    whether one installed bridge can safely serve multiple projects;
    what portability/fallback behavior exists when Runtime Bridge is unavailable.

This is now a named R0 obligation.

## 10. Current disposition

    RUNTIME_BRIDGE_GENERIC_PRODUCT_BOUNDARY=ACCEPTED_AS_DESIGN_INPUT
    RUNTIME_BRIDGE_STANDALONE_REPOSITORY=PLANNED_BUT_NOT_CREATED
    ADS_CANONICAL_OWNERSHIP_OF_GENERIC_RUNTIME_BRIDGE=NOT_LONG_TERM_TARGET
    CURRENT_RUNTIME_BRIDGE_IMPLEMENTATION=PRESERVED_AS_EVIDENCE_AND_ACTIVE_TOOL
    CURRENT_ADS_LOCAL_RUNTIME_REPO=CLASSIFICATION_REQUIRED
    EXTRACTION_AUTHORIZED=false

    NEXT=R0_CHARTER_AMENDMENT_AND_CLAUDE_HANDOFF_REFRESH
