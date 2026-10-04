# Research 503: R0 realization requirements and independent physical-architecture design charter

**Date:** 2026-10-04
**Status:** R0 CHARTER FROZEN / INDEPENDENT PHYSICAL ARCHITECTURE DESIGN NEXT
**Parent:** Research 502 / D-036
**Selected logical target:** THIN_CENTRED_HYBRID_V03
**Frozen substantive base:** c459e9c8ac4435b80d4ac9d2bdb215aa72c13adc
**Collaboration thread:** MC-0030
**Scope:** Freeze the realization-stage requirements, design freedom, evaluation dimensions, and independent-design protocol before any concrete physical architecture candidate is selected.
**Authority:** Realization-design charter only. Specification 028 remains current operational authority. No physical architecture, implementation, migration wave, branch strategy, storage choice, or cutover is selected here.

## 1. Purpose

R0 converts the selected logical architecture into a professional physical/software realization design.

The question is not:

> How do we fit V03 into the current repository architecture?

The question is:

> What physical architecture, repository structure, software boundaries, development workflow, validation system, and migration strategy best realize V03 as one professional Project system?

Current implementation and repository structure are evidence, migration inputs, and compatibility constraints where genuinely live.

They are not the target by default.

## 2. Unbounded physical design freedom

R0 may redesign from first principles:

    files and folders
    canonical-source organization
    schemas and serialization
    package/module boundaries
    storage/indexing
    generated views
    caches
    APIs
    CLI
    UI
    control-plane boundaries
    execution surfaces
    local/cloud division
    tests
    test hierarchy
    CI/CD
    branch strategy
    merge/review workflow
    collaboration procedures
    state persistence
    recovery mechanisms
    migration tooling
    rollback tooling
    observability
    deployment topology
    documentation architecture.

No current mechanism has preservation rights merely because it exists.

A current mechanism survives only because it is demonstrably the best or an intentionally temporary compatibility layer.

## 3. Fixed logical invariants from V03

R0 must preserve at least:

    accepted J1 meaning is the sole normative semantic authority;
    unaccepted model inference is never authority;
    generated projections are not authority;
    accepted machine effects receive closed accounting;
    completion authority is governing-side or exact accepted-domain-contract authority;
    realizers cannot self-certify governing completion;
    J2 source facts remain natural-owner facts;
    J3 operational truth is mechanically derived;
    evidence/freshness predicates have one versioned executable semantic source;
    same-revision evaluation remains acyclic;
    feedback enters through later revisions/snapshots;
    lineage supports carry-forward, replace, split, merge, repartition, retire and reinstate;
    realization succession is explicit and does not silently carry across semantic change;
    realization initialization is an ordered zero-to-many collection;
    generated orientation remains non-authoritative;
    REVIEW_REQUIRED has a resolving owner;
    detective findings route review and do not mutate authority;
    hybrid completeness never silently claims unreconciled legacy;
    current operational authority remains singular until explicit cutover.

Any physical proposal that cannot preserve these is invalid unless it explicitly triggers architecture AMEND/SUPERSEDE/REOPEN.

## 4. R0 requirements

### Authority and acceptance

R0-R01. Bind the exact owner-visible acceptance package, source carrier/revision, decision payload, accepted effect payload, provenance, and effective boundary.

R0-R02. Make acceptance authenticity independently verifiable and tamper-evident without requiring chat history.

R0-R03. Prevent generated views, caches, indexes, model proposals, and runtime status from becoming accidental competing authority.

R0-R04. Make historical accepted meaning immutable while allowing prospective governed succession.

### Identity, completion and lineage

R0-R05. Provide stable accepted-effect identities independent of file path and implementation grouping.

R0-R06. Bind exact completion-contract authority and revision.

R0-R07. Represent completion criteria/components without turning implementation structure into governing semantic structure.

R0-R08. Support deterministic many-to-many realization coverage.

R0-R09. Support all qualified lineage forms, including crossing N:M repartition and reinstate.

R0-R10. Preserve semantic-portion closure, effective-boundary atomicity, and no-silent-loss rules.

R0-R11. Represent realization succession, default OPEN_RESET, explicit carry-for-revalidation, and deferral rebinding.

### J2, predicates, J3 and orientation

R0-R12. Let natural owners publish exact J2 facts without owning J1 meaning.

R0-R13. Provide a versioned predicate registry or equivalent single semantic source for shared executable predicates.

R0-R14. Derive J3 deterministically from accepted semantics plus current source facts.

R0-R15. Support regression when evidence, source revision, qualification, activation, or completion authority becomes stale or changes.

R0-R16. Generate orientation and next-gap views reproducibly and non-authoritatively.

R0-R17. Route REVIEW_REQUIRED to an exact resolving owner/category.

### Control compilation and execution

R0-R18. Compile accepted effects into executable control artifacts without making compilation output authoritative.

R0-R19. Represent REQUIRE, PROHIBIT, GATE, AUTHORIZE, DEFER, LIFECYCLE and SEQUENCE consequences cleanly.

R0-R20. Bind standing enforcement or explicit DETECTIVE_ONLY disposition.

R0-R21. Bind authorization exercise to exact authority and governed execution receipts.

### Storage, rebuild and integrity

R0-R22. Make authoritative state reconstructible from durable sources after loss of caches/generated views.

R0-R23. Define exact hash/revision bases and avoid worktree-vs-Git-blob ambiguity.

R0-R24. Support deterministic full rebuild and incremental refresh with equivalence qualification.

R0-R25. Detect stale, conflicting, orphaned, cyclic, partially migrated, or incompletely accounted states fail-visibly.

R0-R26. Preserve public/private boundaries under normal and degraded operation.

### Concurrency, recovery and workflow

R0-R27. Define optimistic concurrency or equivalent stale-write protection for governing and realization mutations.

R0-R28. Make interruption and recovery resumable without chat-only truth.

R0-R29. Support multi-model/multi-tool collaboration without provider-specific semantic authority.

R0-R30. Define professional branch/merge/review/CI procedures appropriate to authoritative project mutations rather than inheriting current habits automatically.

### Migration and compatibility

R0-R31. Treat Specification 028/current implementation as migration source and current authority, not target structure.

R0-R32. Inventory legacy live semantics by responsibility and accepted obligation, not file order.

R0-R33. Preserve one operational authority at a time through shadow operation and bounded migration.

R0-R34. Require semantic parity, lineage closure, reverse-reference safety and rollback evidence per migration wave.

R0-R35. Keep compatibility surfaces only while they serve an explicit transition requirement.

R0-R36. Support untouched/fresh confirmation against the real implementation before authority switch.

### Maintainability and professional quality

R0-R37. Separate Project-system implementation from ADS Product runtime unless a justified interface requires contact.

R0-R38. Minimize duplicated semantic logic across validators, runtime, generated views and assurance.

R0-R39. Keep normal owner/developer workflows understandable without requiring ontology/schema expertise.

R0-R40. Make operational diagnostics actionable and attributable rather than producing generic invalid states.

R0-R41. Support bounded extension when new domains require new semantics without turning the kernel into a universal type system.

R0-R42. Provide professional architecture documentation and machine-verifiable contracts from the same accepted design boundary.

R0-R43. Keep deployment and operating burden proportionate to demonstrated need.

R0-R44. Preserve portability and avoid unnecessary dependence on one model provider, cloud, database, IDE, or orchestration product.

## 5. Alternative-family requirement

Before selecting a physical architecture, R0 must compare materially distinct realization families.

At minimum, candidate exploration must include designs that differ on major physical ownership choices, such as:

    repository-native declarations with generated indexes;
    dedicated structured semantic records with human-readable rendered carriers;
    append-only/event-oriented accepted-semantic records with derived current snapshots;
    embedded relational/index storage with repository-bound authoritative exports;
    deliberate hybrids.

These examples are exploration prompts, not privileged finalists.

A candidate may introduce a better family not listed here.

## 6. Evaluation dimensions

Every candidate must be scored/reasoned against:

    semantic fidelity to V03
    authority clarity
    failure visibility
    rebuildability
    concurrency safety
    migration safety
    rollback
    owner burden
    developer burden
    testability
    CI/CD ergonomics
    collaboration ergonomics
    fresh-agent reconstruction
    public/private behavior
    observability
    extensibility
    performance/scalability
    operational complexity
    portability
    long-run maintenance
    implementation risk.

Locally elegant solutions may be rejected if they weaken the whole Project system.

## 7. Reuse policy

Existing mechanisms may receive one of:

    PROMOTE_NEARLY_AS_IS
    REFINE_AND_PROMOTE
    REIMPLEMENT_BEHIND_SAME_CONTRACT
    KEEP_AS_COMPATIBILITY_ONLY
    KEEP_AS_TEST_OR_REFERENCE_ONLY
    RETIRE_AFTER_SUCCESSOR
    RETIRE_IMMEDIATELY_WHEN_SAFE.

The burden is on preservation, not replacement.

## 8. Architecture-change trigger policy

During R0 and later realization, evidence is actively classified:

    CONFORMANCE_DEFECT
    KEEP
    CLARIFY
    AMEND
    SUPERSEDE
    REOPEN.

A difficult implementation does not automatically mean the logical architecture is wrong.

Conversely, selected status does not protect V03 from material falsification.

## 9. Independent design protocol

R0 physical architecture is high impact and anchoring-sensitive.

MC-0030 therefore uses:

    INDEPENDENT_THEN_COMPARATIVE.

Sequence:

    1. freeze this neutral R0 charter;
    2. ChatGPT independently authors one physical architecture candidate from the charter;
    3. freeze ChatGPT candidate;
    4. Claude independently authors a physical architecture from the same selected V03 + neutral R0 charter while blind to the ChatGPT candidate;
    5. freeze Claude position;
    6. expose both for comparative critique;
    7. reconcile into one candidate or explicit competing finalists;
    8. run discriminating probes where architecture choice depends on uncertain mechanics;
    9. seek owner decision only when the physical target is decision-ready.

No current physical representation is a target constraint in either independent pass.

## 10. Current boundary

    SELECTED_LOGICAL_TARGET=THIN_CENTRED_HYBRID_V03
    R0_CHARTER=FROZEN
    PHYSICAL_ARCHITECTURE_SELECTED=false
    IMPLEMENTATION_STARTED=false
    PHYSICAL_MIGRATION_AUTHORIZED=false
    SPECIFICATION_028_AUTHORITY=UNCHANGED

    MC0030=OPEN
    NEXT=CHATGPT_INDEPENDENT_PHYSICAL_ARCHITECTURE_CANDIDATE
