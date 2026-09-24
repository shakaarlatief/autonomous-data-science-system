# Research 291: P-D1 Warrant-Proportionality Claim-Set Freeze

**Date:** 2026-09-24
**Status:** CLAIM SET FROZEN / WARRANTS NOT YET AUTHORED / P-D1 HARNESS NOT YET BUILT
**Parent protocol:** Research 277
**Candidate:** WARRANT-F V0.2
**Probe:** P-D1
**Frozen source commit:** 1a095044282622f2ce9e2bd38b90d77b8be8a4a2
**Scope:** Freeze the twelve real candidate assurance claims required by Research 277 before authoring any P-D1 warrant or sampled-mutation implementation.
**Authority:** Claim-selection freeze only.

## 1. Selection rule

Research 277 requires:

    4 invariant claims
    4 suite claims
    4 cross-boundary claims

Selection must be based on semantic importance rather than ease of warranting.

The source commit above is frozen before any P-D1 warrant text or witness harness is authored.

Current tests and scripts are evidence of the claims, not target-mechanism preservation requirements.

## 2. Invariant claims

### I1 AUTHORITY_NONCANONICAL_NEVER_GOVERNS

Property:

    candidate
    historical
    derived
    evidence
    capture

sources must not establish canonical governing authority.

Current evidence family:

    tools/project_knowledge/authority.py
    tests/unit/test_project_knowledge_authority.py

### I2 IDENTITY_DUPLICATE_CURRENT_OWNER_REJECTED

Property:

    two simultaneously current canonical owners of one semantic identity
    must not silently resolve as one current identity

Current evidence family:

    tools/project_knowledge/identity.py
    tests/unit/test_project_knowledge_identity.py

### I3 CAPTURE_STALE_PROMOTION_TARGET_REJECTED

Property:

    promotion from capture/candidate state must bind the exact current
    canonical target revision and reject stale target assumptions

Current evidence family:

    tools/project_knowledge/capture.py
    tests/unit/test_project_knowledge_capture.py

### I4 PUBLIC_PRIVATE_NONLEAKAGE

Property:

    public Project outputs must reject private paths/values and must not
    echo detected private values in public diagnostics

Current evidence family:

    tools/project_knowledge/privacy.py
    tests/unit/test_project_knowledge_privacy.py

## 3. Suite claims

### S1 PRODUCT_REASONING_CONTRACT_SUITE

Scope:

    provider-neutral reasoning request/result semantics
    deterministic canonical input/digest behavior
    methodological-basis constraints
    duplicate stable-key rejection

Current evidence family:

    src/ads_system/application/reasoning.py
    tests/unit/test_reasoning.py

### S2 PRODUCT_CONTEXT_SELECTION_SUITE

Scope:

    bounded context selection
    reasoning-function filtering
    hard budget behavior
    no unnecessary materialization
    duplicate request-function rejection

Current evidence family:

    src/ads_system/application/context_selection.py
    tests/unit/test_context_selection.py

### S3 JW1_PROJECT_KNOWLEDGE_SEMANTIC_SUITE

Scope:

    Project-system authority
    identity
    capture/promotion
    privacy/nonleakage semantics

Current evidence family:

    tools/project_knowledge/
    tests/unit/test_project_knowledge_authority.py
    tests/unit/test_project_knowledge_identity.py
    tests/unit/test_project_knowledge_capture.py
    tests/unit/test_project_knowledge_privacy.py

### S4 REPOSITORY_INTEGRITY_AGGREGATE_SUITE

Scope:

    current family-aware repository contracts
    Project-knowledge validation
    checkpoint metadata
    Knowledge Map
    model-collaboration state
    current routing

Current evidence family:

    scripts/repository_integrity.py
    scripts/check_repository_integrity.py
    tests/unit/test_repository_integrity.py
    tests/unit/test_repository_integrity_aggregate.py

This suite claim is explicitly current-mechanism evidence only.

Its individual invariants remain subject to later retain/amend/supersede/retire classification.

## 4. Cross-boundary claims

### C1 PRODUCT_RUNTIME_INDEPENDENT_OF_PROJECT

Property:

    operational Product behavior must not require Project-plane code for
    runtime correctness

Current architecture evidence:

    Research 250
    Research 258
    Research 276

Current empirical evidence:

    Research 288 / P-D3

### C2 JW1_INDEPENDENT_OF_ENGINEERING

Property:

    JW1 semantic behavior must not depend on project/engineering
    assurance/orchestration machinery

Current architecture evidence:

    Research 258
    Research 273
    Research 276

Current empirical evidence:

    Research 288 / P-D3

### C3 ASSURANCE_ORACLE_SEMANTIC_PARITY_BEFORE_RETIREMENT

Property:

    a current assurance mechanism may lose migration-oracle duty only
    after retained invariants have a qualified successor, known-bad
    sensitivity is preserved, known-good specificity is preserved where
    applicable, unexplained successor-weaker divergence is resolved, and
    release is explicitly dispositioned

Current architecture evidence:

    Research 273
    Research 276
    Research 277

Future direct empirical discriminator:

    P-D4

### C4 DECISION_EVIDENCE_EXACT_SUBJECT_BINDING

Property:

    evidence used for a governed decision must bind the exact subject and
    must not remain admissible after a material bound input changes

Current architecture evidence:

    Research 273
    Research 275
    Research 276

Existing bounded empirical evidence includes:

    representation-probe Git-blob binding
    P-D6 harness binding
    P-D3 harness/source binding
    P-D5 harness/source binding

This claim does not select Git commits as the universal future subject type.

## 5. Anti-convenience check

The set was not chosen solely from one package or one easy-to-mutate test family.

It spans:

    Product semantics
    JW1 semantics
    repository engineering
    public/private boundary
    Product/Project dependency boundary
    Engineering/JW1 dependency boundary
    migration-oracle retirement
    exact decision-evidence binding

The suite claims deliberately include both narrow Product suites and broad
Project/repository suites.

## 6. What is still unfrozen

This record does NOT yet define:

    warrant text
    witness implementations
    witness provenance classification
    fully/partially warranted status
    mutation operators
    mutation sample
    measured maintenance burden
    P-D1 result thresholds beyond Research 277

Those are authored only after this claim-set freeze.

## 7. Current state

    P_D1_CLAIM_SET=FROZEN
    CLAIM_COUNT=12
    INVARIANT_CLAIMS=4
    SUITE_CLAIMS=4
    CROSS_BOUNDARY_CLAIMS=4

    WARRANTS_AUTHORED=false
    P_D1_HARNESS_BUILT=false
    P_D1_RESULT=NOT_OBSERVED

    COMPLETED_VALID_DECISION_PROBES=4_OF_8
    OWNER_ASSURANCE_DECISION=HELD
    NEXT=AUTHOR_P_D1_WARRANTS_AND_HARNESS
