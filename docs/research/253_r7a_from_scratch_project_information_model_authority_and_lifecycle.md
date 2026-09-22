# Research 253: R7-A From-Scratch Project Information Model, Authority, and Lifecycle

**Date:** 2026-09-22
**Status:** R7-A INFORMATION MODEL FROZEN / PHYSICAL HIERARCHY NOT YET SELECTED / R7-B TARGET HIERARCHY NEXT
**Parent program:** Research 240
**Accepted architecture basis:** Research 248-252
**Repository base:** ba752ca13c186cccb4f5a459bc9becd41dd2201f
**Scope:** Derive the future Project-plane information model from first principles for a professional, long-lived ADS project before selecting a physical hierarchy or mapping the current docs tree into it.

## 1. Problem statement

The future Project information architecture must support a project that is:

    long-lived
    architecture-intensive
    research-driven
    multi-workspace
    multi-model / multi-contributor
    partially automated
    provenance-sensitive
    capable of substantial historical accumulation
    expected to survive chat/model/provider changes
    expected to remain reconstructable from the repository itself

The architecture must not be a cleaned-up version of today's docs/ tree.

It must answer:

    What information classes does a professional ADS project actually need?
    Which information can govern current behavior?
    Which information is evidence only?
    Which information is operational procedure?
    Which information is temporary/candidate state?
    Which information is historical?
    What is generated rather than authored?
    How does a cold-start human or agent find current authority?
    How do we prevent navigation from becoming a second authority?
    How do we preserve deep rationale without forcing all history into active context?

## 2. Information architecture is not one taxonomy

R7 separates six dimensions that must not be collapsed into folder names.

### 2.1 Responsibility

Who owns the meaning?

Accepted Project contexts:

    JC1 Project Direction, Architecture and Memory
    JC2 Project Development Control System
    JC3 Research and Qualification
    JC4 Engineering, Verification and Delivery
    JC5 Collaboration and Contribution
    JC6 Historical Preservation

### 2.2 Information role

What function does this carrier perform?

    GOVERNING
    EVIDENCE
    PROCEDURE
    CURRENT_STATE_SOURCE
    NAVIGATION
    CAPTURE
    GENERATED_VIEW
    HISTORICAL_RECORD

### 2.3 Maturity

How far has the content progressed?

    CANDIDATE
    ACCEPTED
    SUPERSEDED
    RETIRED

Exact executable metadata vocabularies remain governed by Specification 028 / future amendment. These terms are R7 conceptual roles, not an automatic schema replacement.

### 2.4 Time/lifecycle

Is the information:

    active/current
    paused but expected to resume
    completed but still load-bearing
    historical-only
    superseded

### 2.5 Semantic subject

What durable subject matter does the carrier substantively develop or govern?

This is orthogonal to physical location and artifact role.

### 2.6 Carrier/identity

What repository carrier currently holds the information, and does the information need first-class semantic identity?

Path and semantic identity remain distinct.

## 3. Durable information classes

R7 derives four primary durable information classes plus three non-durable/control classes.

## 3.1 I1 Governance and Current Authority

Purpose:

    define what the project is trying to do
    define constraints and governing principles
    record accepted architecture and owner decisions
    define current requirements/specifications
    define current planning/priority/open obligations where they are authoritative

Typical record roles:

    project charter / vision
    principles
    architecture decisions
    specifications
    accepted rationale
    owner decisions
    current roadmap/plan
    durable open question with active authority
    durable architecture backlog item

Primary owner:

    JC1

Authority expectation:

    may contain current governing truth

Key rule:

    concise summaries/navigation may point here, but may not duplicate unique governing truth elsewhere.

## 3.2 I2 Evidence and Qualification

Purpose:

    preserve why a conclusion, architecture, product behavior or project decision is justified

Includes:

    bounded research
    experiments and evaluations
    qualification results
    adversarial reviews
    benchmark evidence
    migration evidence
    implementation provenance where it substantiates a decision
    reproducibility records

Primary owner:

    JC3

Secondary participation:

    JC4 for verification/release evidence
    JC5 for review/collaboration evidence

Authority expectation:

    evidence can constrain current decisions but is not automatically governing policy

Key rule:

    promoted conclusions must update the governing owner rather than forcing every future reader to infer current policy from old evidence.

## 3.3 I3 Engineering and Operational Knowledge

Purpose:

    explain how the ADS project is built, verified, released, secured, operated and contributed to

Includes durable:

    repository engineering procedures
    development environment procedures
    CI/verification policy
    release/change procedures
    secure-development policy
    operational runbooks
    contributor workflow
    collaboration procedures
    local/private boundary operations
    incident/recovery procedures

Primary owners:

    JC4
    JC5

Authority expectation:

    may be operationally governing within its scope

Key rule:

    implementation/configuration that mechanically enforces the rule should live with its executable owner; the durable human-readable contract belongs here only when it has independent informational value.

## 3.4 I4 Historical Record

Purpose:

    preserve information whose primary current value is provenance, reconstruction or reproducibility rather than active governance

Includes selectively:

    retired prototypes
    superseded-but-important architecture records
    frozen implementation sources needed for fidelity recovery
    historical milestone snapshots
    completed collaboration records
    historical migration evidence
    obsolete but load-bearing experiment reproduction material

Primary owner:

    JC6

Authority expectation:

    not current authority

Key rule:

    historical preservation must never imply active architectural peer status.

## 3.5 I5 Capture / Candidate Information

Purpose:

    preserve unreviewed or not-yet-promoted understanding without contaminating current authority

Includes:

    captures
    candidate notes
    provisional annotations
    unresolved migration candidates

Primary executable owner:

    JC2 / JW1

Authority expectation:

    non-authoritative until promotion

Durability:

    temporary or selectively durable depending workflow

## 3.6 I6 Generated Navigation and Current-State Views

Purpose:

    give humans/agents fast access to the current project without creating a second canonical source

Includes generated:

    current-state views
    subject indexes
    identity/authority indexes
    workstream views
    source catalogs
    cold-start machine routing material
    risk/obligation views

Primary executable owner:

    JC2 / JW1

Authority expectation:

    derived, non-authoritative

Key rule:

    every generated view must remain rebuildable from governed sources at its declared revision boundary.

## 3.7 I7 Executable Project-Control State

Purpose:

    hold state that belongs to the Project Development System itself rather than the human knowledge corpus

Includes:

    project-system configuration
    instance policy
    control state
    declarations
    transition records
    framework lineage
    machine contracts/schemas
    compatibility/migration state

Primary owner:

    JC2 / JW1

This is information, but it is **system state**, not ordinary project documentation.

## 4. Fundamental separation: project knowledge versus project system

R7 adopts the following strong distinction:

    DURABLE PROJECT KNOWLEDGE
        human-reviewable governing/evidence/operations/history carriers
        owned by JC1/JC3/JC4/JC5/JC6

    PROJECT DEVELOPMENT SYSTEM
        executable JC2 machinery
        machine contracts
        control state
        generated views
        captures
        framework materialization

These may reference one another.

They must not be physically or conceptually conflated.

This resolves a major ambiguity in the current repository, where the phrase project_knowledge refers both to the overall information problem and to a particular implementation subsystem.

## 5. Authority model

R7 does not infer authority from folder placement.

A carrier's authority must be explicit enough to distinguish at least:

    current governing source
    operational procedure
    qualified evidence
    candidate/capture
    derived/generated view
    historical record
    superseded/retired source

The deeper Candidate 01 rule remains:

    physical path != authority

Authority is resolved from source metadata/contracts and accepted project governance.

## 6. Promotion model

The durable lifecycle becomes:

    DISCUSSION / LOCAL WORK
        ->
    CAPTURE / CANDIDATE
        ->
    REVIEW / RESEARCH / QUALIFICATION
        ->
    PROMOTION DECISION
        ->
    GOVERNING / OPERATIONAL OWNER
        or
    EVIDENCE ONLY
        or
    HISTORICAL ONLY
        or
    RETIRE

Promotion does not copy the same truth into multiple canonical homes.

If evidence changes a governing conclusion:

    update/supersede the governing owner
    preserve evidence as evidence
    link the relationship
    do not make evidence itself the new policy by implication

## 7. Current-state model

R7 rejects a manually maintained giant current-state document as the long-term architecture.

Future current orientation should be assembled from:

    governing current sources
    active work/control state
    accepted open obligations
    current routing
    current workspace/project status

through a compact generated view.

A human-authored current-state narrative may exist when useful, but it must not become the only place where current truth lives.

The current CURRENT_STATE.md remains operational authority until cutover; this is a target-design statement only.

## 8. Cold-start model

The Project information architecture must support two cold-start paths.

### Human cold start

A stable repository entry explains:

    what ADS is
    what is Product versus Project
    how to run/build/contribute
    where current project authority is
    where deeper architecture/evidence/history lives

### Machine/agent cold start

A stable machine-readable root anchor locates:

    current project routing
    current authority boundary
    current generated orientation view
    Project Development System version/instance
    next governed continuation entry

Neither entry point contains unique substantive truth.

## 9. Navigation model

R7 preserves the empirical architectural result of Research 217, not necessarily its exact old vocabulary.

Accepted durable principles:

    controlled semantic subjects
    source-owned subject membership
    polyhierarchy
    optional preferred route
    semantic subjects distinct from structural/resolver facets
    generated subject navigation
    no central member registry

However:

> the existing 18-subject vocabulary is NOT automatically frozen as the future R7 vocabulary.

Reason:

Several subject IDs encode current conceptual/product structures such as cockpit-* and source-universe. R6 explicitly allows those current concepts to split, merge or disappear.

Therefore:

    subject architecture pattern
        RETAIN

    exact current subject catalog
        REVALIDATE AGAINST THE NEW TARGET CORPUS BEFORE CUTOVER

Stable IDs may be retained where meaning remains genuinely stable. Others may be aliased, merged, redirected or superseded through governed vocabulary evolution.

## 10. Identity/carrier model

R7 preserves the T3 evidence-backed rule:

    one declaration per ordinary carrier

    first-class independently governed item
        -> own canonical carrier + semantic ID when identity is justified

    no first-class identity need
        -> may remain embedded in a broader carrier

    no mass file-per-fact atomization

The old T3 physical homes under docs/ are not retained.

The identity/carrier rule survives; its physical realization must follow the new R7 hierarchy.

## 11. Historical-navigation model

R7 preserves the T4 result:

    before retiring a live legacy navigation surface,
    preserve exact historical routing evidence sufficient to reconstruct how
    the old project was navigated at the cutover boundary.

The historical routing evidence is:

    evidence
    not current truth
    not a derived view that must remain rebuildable after its legacy input retires

This principle applies to eventual retirement of the current Knowledge Map.

## 12. Artifact role versus physical hierarchy

R7 explicitly rejects a future physical root organized by every artifact role.

The following should **not** all become peers merely because they are useful labels:

    foundations/
    specifications/
    decisions/
    research/
    checkpoints/
    experiments/
    runbooks/
    reviews/
    history/

Instead:

> physical hierarchy should first express a small number of stable information responsibility classes; artifact role is represented one level lower or through metadata where appropriate.

This is the direct correction to the flat mixed architecture that triggered the whole-repository reopening.

## 13. Granularity model

Create a new durable carrier only when one or more materially apply:

    independent authority/lifecycle
    independent revision/provenance
    first-class semantic identity required
    direct external reference needs
    different retention/history treatment
    operational size/volatility would overload the current owner
    mixing would create ambiguous authority

Otherwise update the existing natural owner.

This preserves the anti-megadoc and anti-atomization balance from Research 208.

## 14. Reconciliation model

A professional Project information system requires periodic reconciliation.

Triggers include:

    major architecture decision
    major product/workspace boundary change
    experiment/qualification completion
    framework upgrade
    release milestone
    substantial project information migration
    subject-vocabulary pressure
    evidence of stale/conflicting current authority

Reconciliation checks:

    promoted conclusions reflected in current governing sources
    no duplicate current authority
    superseded material correctly marked
    generated views fresh
    navigation vocabulary coherent
    history separated from active authority
    cold-start routes valid
    load-bearing evidence still reproducible/retrievable

## 15. What R7-A does not select yet

R7-A does not yet select:

    the directory name for the durable Project knowledge corpus
    exact physical top-level subdirectories inside that corpus
    exact replacement for foundations/specifications/research/checkpoints
    exact current-state generated view path
    exact subject catalog path
    exact JW1 Project Development System name
    exact historical archive path
    exact migration mapping for each existing document

Those are R7-B / R8 questions.

## 16. R7-A result

    R7_INFORMATION_CLASSES=FROZEN
    PRIMARY_DURABLE_CLASSES=4
        GOVERNANCE_CURRENT_AUTHORITY
        EVIDENCE_QUALIFICATION
        ENGINEERING_OPERATIONAL_KNOWLEDGE
        HISTORICAL_RECORD

    NON_DURABLE_OR_SYSTEM_CLASSES=3
        CAPTURE_CANDIDATE
        GENERATED_NAVIGATION_CURRENT_STATE
        EXECUTABLE_PROJECT_CONTROL_STATE

    PROJECT_KNOWLEDGE_AND_PROJECT_SYSTEM=SEPARATED
    CURRENT_STATE_TARGET=GENERATED_ORIENTATION_OVER_CANONICAL_SOURCES
    SUBJECT_ARCHITECTURE_PATTERN=RETAIN
    OLD_SUBJECT_VOCABULARY=AUDIT_BEFORE_CUTOVER
    SELECTIVE_IDENTITY_CARRIER_RULE=RETAIN
    HISTORICAL_NAVIGATION_EVIDENCE_RULE=RETAIN
    PHYSICAL_HIERARCHY=UNRESOLVED
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=R7B_PHYSICAL_INFORMATION_HIERARCHY_AND_AUTHORING_MODEL
