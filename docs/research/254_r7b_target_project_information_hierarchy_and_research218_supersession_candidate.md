# Research 254: R7-B Target Project Information Hierarchy and Research 218 Supersession Candidate

**Date:** 2026-09-22
**Status:** R7 TARGET HIERARCHY RECOMMENDED / RESEARCH 218 PHYSICAL TREE SUPERSESSION CANDIDATE / OWNER DECISION REQUIRED / NO PHYSICAL MIGRATION
**Parent program:** Research 240
**Information-model basis:** Research 253
**Repository base:** 8ee7f1c27d9b6c07bcc9d1938a3145d320084eeb
**Scope:** Convert the accepted R7-A information model into a coherent physical Project information hierarchy, authoring decision tree and compatibility/supersession plan. This is a target recommendation only.

## 1. Recommended target

R7 recommends a **Project System / Project Knowledge separation** inside the already accepted Project plane.

Conceptually:

    project/
        README.md

        system/
            <JW1 Project Development System>
            <machine contracts/control state/generated views/captures>

        knowledge/
            README.md

            governance/
                direction/
                architecture/
                    rationale/
                    specifications/
                decisions/
                planning/

            evidence/
                research/
                qualification/
                provenance/

            operations/
                engineering/
                collaboration/

            history/
                milestones/

        <active JC3 research execution area, exact path deferred>
        <historical executable/archive area, exact path deferred>

The exact internal layout of JW1 and the exact physical homes for active experiment workspaces / preserved historical executables remain R8 realization questions.

The Project **information hierarchy** is the knowledge/ subtree.

## 2. Why project/knowledge/ is now appropriate

A folder named docs/project_knowledge/ was cognitively ambiguous because almost everything under docs/ was project knowledge in ordinary language, while that directory actually contained infrastructure for the Project Knowledge Architecture.

Under the new Level-1 architecture:

    product/
    project/

the meaning becomes unambiguous:

    project/knowledge/
        durable information about building/governing ADS

while:

    project/system/
        machinery that manages/governs/reconstructs that project information

This allows the old implementation meaning of project_knowledge to disappear.

The future Project Development System should not be named project_knowledge merely because its first implementation grew out of that program.

## 3. Why four primary knowledge classes

The physical root of the Project knowledge corpus is intentionally small:

    governance/
    evidence/
    operations/
    history/

These classes are designed to remain useful when ADS has many more products, workspaces, contributors, providers, research programs, releases, architectural transitions, operational environments and years of accumulated history.

They answer different questions:

    governance/
        What currently governs the project?

    evidence/
        Why do we believe or accept it?

    operations/
        How do we build, verify, release, secure and collaborate on the project?

    history/
        What must remain reconstructable even though it is no longer active authority?

This is a stronger organizing principle than mixing artifact types, domain names and lifecycle stages at one root.

## 4. Governance hierarchy

Recommended:

    knowledge/governance/
        direction/
        architecture/
            rationale/
            specifications/
        decisions/
        planning/

### 4.1 direction/

Own current project intent:

    vision
    product/project scope
    principles
    goals
    requirements at project-governance level
    non-goals
    roadmap direction where durable

This is not a dumping ground for all current status.

### 4.2 architecture/

Own durable architecture knowledge.

#### rationale/

Deep accepted architectural reasoning that is useful beyond one decision.

This is the natural successor role for the useful part of today's Foundations family.

A rationale record is not automatically normative implementation contract.

#### specifications/

Current governed implementable contracts.

This is the natural successor role for current Specifications where those specifications remain current.

Executable schemas/contracts may additionally live with their owning workspace; the Project knowledge record points to / governs them rather than duplicating bytes.

### 4.3 decisions/

Own first-class decisions whose independent identity/lifecycle is justified.

The T3 selective-per-item rule applies.

Not every sentence-level decision receives a file.

### 4.4 planning/

Own durable current planning information that merits project authority, such as:

    accepted open questions
    architecture backlog items
    roadmap/stage obligations
    explicit deferred decisions

This replaces multiple root registries without requiring one file per trivial item.

## 5. Evidence hierarchy

Recommended:

    knowledge/evidence/
        research/
        qualification/
        provenance/

### 5.1 research/

Own bounded investigations, comparisons, design studies and empirical inquiries.

Current chronological Research IDs may be preserved where they carry useful provenance.

However research/ is no longer expected to be the universal landing place for every durable project fact.

Promoted conclusions update governance/operations/Product owners.

### 5.2 qualification/

Own evidence that a mechanism, architecture, release, migration or behavior satisfies a declared gate/contract.

Examples:

    test campaigns
    adversarial reviews
    acceptance results
    audit results
    release qualification
    migration parity evidence

A checkpoint that primarily proves a gate belongs here rather than in one universal checkpoint family.

### 5.3 provenance/

Own durable evidence whose main value is exact implementation/source/migration provenance rather than broader research interpretation.

Examples:

    frozen implementation provenance
    source-bound migration evidence
    final legacy-navigation preservation evidence
    exact artifact/digest bindings needed for later reconstruction

This is selective.

Ordinary Git history is not copied here.

## 6. Operations hierarchy

Recommended:

    knowledge/operations/
        engineering/
        collaboration/

### 6.1 engineering/

Own durable procedures/policies for:

    repository engineering
    development environments
    build/CI operation
    verification operation
    secure development
    dependency/supply-chain governance
    release/change/configuration management
    local/private operational boundaries
    incident/recovery procedures

Executable configuration remains with the mechanism/tool that enforces it.

The knowledge record explains the durable operational contract.

### 6.2 collaboration/

Own durable collaboration/contribution procedures:

    contributor workflow
    human/model handoff
    review policy
    bounded write authority
    collaboration-provider operating policy
    continuity/handoff procedure where human-readable

Active mechanized thread/control state belongs to project/system, not here.

Completed review output may belong to evidence/qualification or history depending continued relevance.

## 7. History hierarchy

Recommended root:

    knowledge/history/
        milestones/

### 7.1 milestones/

Own selective historical project-state records whose value is reconstruction of meaningful transitions.

This is the successor role for the subset of today's Checkpoints that are genuinely project-history milestones.

Not every implementation action produces a milestone.

### 7.2 Historical records do not all move here

A completed research record can remain under evidence/research if it is still load-bearing evidence.

A superseded architecture record may remain in governance with explicit supersession if readers still need it to understand the current contract.

A historical artifact moves to history only when its **primary current responsibility** becomes historical reconstruction.

This avoids treating lifecycle age as the sole placement rule.

## 8. Checkpoint family disposition

The universal current checkpoints/ family is not retained as a mandatory future information family.

Current checkpoint responsibilities split prospectively:

    owner/architecture decision boundary
        -> governance/decisions or architecture

    research/experiment result
        -> evidence/research or evidence/qualification

    verification/acceptance boundary
        -> evidence/qualification

    meaningful historical project-state snapshot
        -> history/milestones

    purely mechanical transition already reconstructable elsewhere
        -> no new durable target carrier unless retention evidence requires it

The current numbered checkpoint corpus remains historical evidence during migration.

No mass rewrite is implied.

## 9. Foundation family disposition

The universal foundations/ root is not retained as a top-level Project-knowledge class.

Its durable role becomes:

    governance/architecture/rationale/

when a foundation contains accepted deep architectural reasoning that remains useful.

Some current foundations may instead map to Product-owned knowledge, operations policy, evidence or history depending content.

The **concept of deep durable rationale survives**.

The current folder as universal peer does not.

## 10. Specification family disposition

The specification role survives strongly but moves under:

    governance/architecture/specifications/

for Project-governed architecture/contracts.

A Product workspace may also own executable contracts close to implementation.

The Project specification record must not duplicate executable truth; it governs scope/meaning and references the owning executable contract where applicable.

## 11. Research family disposition

The research role survives under:

    evidence/research/

This placement fixes the earlier root-level category mixing.

Research is now explicitly evidence, not one of several peer roots beside product/subsystem areas.

## 12. Decision/question/backlog disposition

The T3 selective-item principle remains.

Target:

    governance/decisions/
    governance/planning/

Aggregate browsing/index surfaces should become generated or curated navigation after current governing items are migrated/dispositioned.

No path-based identity is introduced.

## 13. Current-state, continuity and navigation target

### 13.1 CURRENT_STATE

Long-term role:

    compact generated orientation view
    owned/generated by project/system

It summarizes current governing sources and active control state.

It contains no unique accepted truth.

### 13.2 current routing

Long-term role:

    machine-readable cold-start anchor
    exposed at stable true-root path or stable true-root indirection
    generated/validated by project/system

Exact future filename is R8 work.

### 13.3 CONTINUITY

The current monolithic role splits:

    human continuity procedure
        -> knowledge/operations/collaboration/

    live machine continuation/routing state
        -> project/system

    historical handoff snapshots
        -> knowledge/history/milestones/ only when independently valuable

### 13.4 KNOWLEDGE_MAP

Long-term role:

    generated navigation projection
    plus preserved immutable historical-routing evidence at cutover

The current hand-maintained live map is not the target canonical architecture.

Research 217 semantic subject architecture supplies one navigation dimension.

## 14. Project Development System boundary

The following do **not** belong in project/knowledge/ as ordinary durable knowledge:

    generated indexes/views
    current routing state
    control-plane state
    workstream graph state
    framework instance policy
    framework lineage
    source declarations
    transition records used as executable control state
    capture queue
    machine schemas/contracts for JW1
    compatibility shadow state

They belong to project/system/ or to an executable owner referenced by that system.

Human-readable architecture/operating contracts about the system belong in Project knowledge.

This prevents the durable knowledge corpus from turning into an implementation data directory.

## 15. Active research execution boundary

R7 distinguishes:

    research evidence
        durable Project knowledge

from:

    experiment/research execution workspace
        active project work

Therefore active code/data/harnesses do not automatically live under knowledge/evidence/research/.

Only durable reports, protocols, manifests/results needed as Project information belong there.

Exact active-workspace path is deferred because R7 is an information-architecture stage.

## 16. Historical executable boundary

Likewise:

    knowledge/history/
        durable historical records

is distinct from:

    preserved executable historical workspace
        e.g. a byte-preserved prototype/reproduction package

The latter may require a Project archive/reproduction area in R8.

Do not place virtual environments, caches, generated build artifacts or ordinary stale code in knowledge/history.

## 17. Authoring decision tree

For every new durable Project artifact:

    Q1. Is this Product-owned runtime/product knowledge?
        YES -> Product owner, not Project knowledge.

    Q2. Is this executable Project-system state, generated view, machine
        contract or capture?
        YES -> project/system or its owning executable workspace.

    Q3. Is this active experiment/research execution rather than durable
        information?
        YES -> active research workspace, not knowledge corpus.

    Q4. What is the durable information's primary responsibility?

        governs current project
            -> knowledge/governance/

        supports/qualifies a conclusion
            -> knowledge/evidence/

        tells contributors/agents how to operate the project
            -> knowledge/operations/

        exists primarily for historical reconstruction
            -> knowledge/history/

    Q5. Does an existing canonical owner already match?
        YES -> update it.

    Q6. Does independent lifecycle/authority/provenance/identity justify a
        new carrier?
        YES -> create bounded carrier.

    Q7. Does the carrier need semantic-subject memberships?
        Add only subjects it substantively develops/governs.

    Q8. Rebuild navigation/current views.
        Never copy unique accepted truth into a summary/index.

## 18. Naming policy

Target defaults:

    lowercase_snake_case for ordinary files/directories
    conventional README.md allowed
    stable human IDs retained where they add real provenance/readability
    semantic IDs remain separate from paths
    no mass rename solely for aesthetics

Current numbered Research/Specification/Checkpoint IDs may be preserved during migration where references/history make renaming expensive.

Future families need not inherit numbering unless ordered provenance remains materially useful.

## 19. Subject/navigation impact

Retain:

    source-owned memberships
    controlled vocabulary
    polyhierarchy
    preferred subject route
    generated subject index
    structural/resolver facets separate

Reconsider before cutover:

    exact 18 current subjects
    current cockpit/source-universe-specific leaves
    any subject whose meaning depended on a superseded current folder/domain
    preferred routes after physical migration

Subject vocabulary changes must use stable IDs/aliases/merge redirects where continuity requires them.

## 20. Research 218 disposition

R7-B recommends:

    SUPERSEDE THE PHYSICAL INFORMATION ARCHITECTURE OF RESEARCH 218

because its target tree is explicitly built around the now-rejected flat mixed docs/ hierarchy.

Retain as evidence/deeper semantic contract where still supported:

    path != semantic identity
    path != authority
    physical parent != exclusive semantic parent
    source-local natural ownership
    controlled source-owned semantic subjects
    selective first-class identity
    one declaration per carrier
    no mass historical retrofit
    capture != promotion
    generated navigation contains no unique truth
    historical navigation evidence before legacy-map retirement

Supersede/reopen physically:

    docs/ as the universal Project-information root
    top-level coexistence of epistemic families and subsystem/domain homes
    docs/project_knowledge/ as infrastructure home
    prospective docs/decisions, docs/open_questions, docs/architecture_backlog paths
    root-level Foundations/Specifications/Research/Checkpoints as peer information classes

This is a prospective disposition only until the owner accepts R7.

## 21. Research 177 / Specification 028 consequence

If R7 is accepted:

Research 177's selected physical paths:

    tools/project_knowledge
    schemas/project_knowledge
    docs/project_knowledge
    tests/...

become migration-source paths, not future target paths.

Specification 028 still governs current implementation/migration semantics until explicitly amended.

R8 must identify exact path-sensitive clauses, schemas, tests and generated-view contracts that require amendment for:

    project/system/
    project/knowledge/
    Product workspace relocation
    generated/capture relocation
    subject catalog relocation

No Specification 028 text is silently rewritten by R7.

## 22. Why this is more professional than the old hierarchy

The old physical model mixed:

    artifact type
    epistemic stage
    subsystem/domain
    governance registry
    infrastructure
    compatibility surfaces

at the same physical level.

The new model uses:

    Level 1
        Product vs Project responsibility

    Project Level 2
        system vs durable knowledge vs non-information execution/archive

    Project knowledge Level 3
        governance vs evidence vs operations vs history

    lower levels
        natural subresponsibility / artifact role

    semantic overlay
        controlled subjects + structural facets + identity/authority metadata

This makes each level answer one clear question.

## 23. Stress test against future growth

### Hundreds or thousands of research records

Remain under evidence/research with semantic-subject navigation and generated indexes.

They do not crowd the Project root.

### Many architecture decisions/specifications

Remain under governance with selective first-class carriers and generated browsing.

### Multiple engineering domains

Operations/engineering may develop subareas by stable responsibility only when volume/lifecycle warrants them.

### Many collaborators/models

Collaboration procedures remain operations/collaboration; active mechanized thread state stays in project/system; completed review evidence transitions to evidence/history.

### Long project history

Only material whose primary value becomes historical reconstruction moves to history.

Git remains the full low-level historical substrate.

### Large Project Development System

Its executable data/code scales under project/system without contaminating the human knowledge corpus.

### New Product subsystems

Their product-owned knowledge stays with Product owners rather than creating Project-knowledge domain folders.

## 24. Recommended owner decision

Recommended decision:

    ACCEPT

meaning:

    accept project/knowledge/ as the durable Project knowledge corpus;
    accept governance/evidence/operations/history as its four primary classes;
    accept Project-system separation;
    accept the authoring/lifecycle/navigation model;
    accept prospective supersession of Research 218's physical tree;
    authorize R8 detailed migration/amendment planning;
    do NOT authorize physical migration yet.

If accepted, R8 may design the exact target paths, current-file disposition manifest, compatibility strategy, Specification 028 amendments, migration order, validation gates and rollback plan.

## 25. Current state

    R7A_INFORMATION_MODEL=FROZEN
    R7B_TARGET_HIERARCHY=RECOMMENDED
    TARGET_PROJECT_INFORMATION_ROOT=project/knowledge
    PRIMARY_CLASSES=governance,evidence,operations,history
    PROJECT_SYSTEM_ROOT=project/system
    CURRENT_STATE_TARGET=generated_view
    LEGACY_KNOWLEDGE_MAP_TARGET=generated_navigation_plus_historical_evidence
    RESEARCH218_RECOMMENDED_DISPOSITION=SUPERSEDE_PHYSICAL_RETAIN_SEMANTIC_EVIDENCE
    OWNER_DECISION=PENDING
    R8=BLOCKED_ON_OWNER_R7_DECISION
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=OWNER_R7_TARGET_DECISION
