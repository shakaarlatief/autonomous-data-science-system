# MC-0026 Brief: Independent R8-B Representation and Content Architecture Design

**Thread:** MC-0026
**Date opened:** 2026-09-23
**Review mode:** INDEPENDENT_THEN_COMPARATIVE
**Coordination branch:** v1-source-vault-bootstrap-resume
**Frozen independent-design base:** 1fe4bbe4b2658532359411825d3b1d819a6c4c68
**Claude interaction:** claude-03
**Claude conversation title:** 03 - Project Knowledge Architecture Foundations and Design Method
**Authority:** Collaboration evidence only. Research 260 freezes the shared problem/requirements. No representation target has been selected. No physical migration is authorized.

## 1. Purpose

Produce an independent future representation/content architecture for the Project plane from the shared frozen requirements in Research 260.

This collaboration is intentionally independent before comparative reconciliation.

ChatGPT will separately derive its own candidate from the same frozen base. Claude must not inspect any later ChatGPT representation candidate before writing Message 001.

The objective is not to preserve current Markdown, JSON, declaration metadata, JSON Schema, generated-view layouts, model-collaboration message format or any other current carrier convention.

Current artifacts are evidence only.

## 2. Frozen independent-design boundary

Use exact commit:

    1fe4bbe4b2658532359411825d3b1d819a6c4c68

Read at minimum from that exact revision:

    docs/research/260_r8b_from_scratch_representation_requirements_and_independent_design_protocol.md
    docs/research/259_r8a_owner_amendment_acceptance_and_from_scratch_representation_freedom.md
    docs/research/258_mc0025_r8a_adversarial_reconciliation_and_amended_exact_target_candidate.md
    docs/research/256_r7_owner_amendment_acceptance_research218_supersession_and_r8_entry.md
    docs/research/253_r7a_from_scratch_project_information_model_authority_and_lifecycle.md
    docs/research/222_ao3_progressive_control_closure_architecture.md
    docs/research/223_ao4_architecture_evolution_and_frozen_contract_governance.md
    docs/research/224_ao5_anchored_interaction_continuity_and_independent_recovery.md
    docs/research/225_ao6_purpose_bound_git_lifecycle_and_workstream_orchestration.md
    docs/research/226_ao7_authority_preserving_successor_orchestration_bridge.md
    docs/research/235_ao9_p7_owner_decisions_and_ao9_closure.md
    docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md

You may inspect current implementation/files at that exact revision for behavioral, migration or negative evidence.

Do not treat current file shape as target architecture.

## 3. Independence rule

Before writing Message 001:

    do not read commits after
        1fe4bbe4b2658532359411825d3b1d819a6c4c68

    except:
        this MC-0026 thread contract itself

In particular, do not read any later ChatGPT representation candidate, research synthesis or checkpoint that selects representation mechanisms.

If later routing/current-state files are needed only to discover the thread, read the thread and then return to the frozen base for substantive design evidence.

State any unavoidable exposure explicitly.

## 4. Core design question

Design the representation architecture from first principles:

> What should be the canonical, authored, machine-structured, generated, query, event/receipt and cache representations for the future Project knowledge and Project Development System, given the accepted Product/Project architecture and Research 260 requirements?

The design may freely select or reject:

    Markdown
    structured Markdown
    TOML
    YAML
    JSON
    JSONL / NDJSON
    JSON Schema
    other schema languages
    SQLite
    relational storage
    graph structures/databases
    event logs
    source-local metadata
    metadata sidecars
    bounded registries
    generated indexes
    FTS/search indexes
    vector/semantic indexes
    hybrid combinations

Do not select technology by familiarity or prestige.

## 5. Required design outputs

Map all Research 260 classes RC1-RC12.

For each class provide:

    canonical or derived role
    representation
    authority semantics
    lifecycle
    identity model
    relation model
    provenance model
    read/write pattern
    Git behavior
    concurrency/stale-write behavior
    recovery behavior
    schema/version strategy

Also specify:

### A. Durable human knowledge

How governance/evidence/operations/history is authored.

Whether machine metadata is:

    inline/front matter
    sidecar
    central/bounded registry
    absent unless needed
    hybrid

### B. Semantic identity/authority model

How stable IDs, authority role, lifecycle, subject membership and typed relations are represented without making paths authoritative or introducing universal metadata.

### C. Independent cross-object facts

When a relation gets its own record and where it lives.

### D. Project-system instance policy

How ADS-specific policy/configuration is represented without contaminating generic PSMF mechanism.

### E. Durable Project-control facts

How workstream state, obligations, authority regime, transition state and continuity state are represented.

Address:

    direct recovery
    stale writes
    Git review
    concurrent changes
    machine writes

### F. Control receipts/events

Decide what is persisted, at what granularity and in what representation.

Avoid both:

    no observability
    persist-everything event spam

### G. Captures/candidates

Define representation and promotion behavior.

### H. Contracts/schemas

Select a schema/validation strategy.

Current JSON Schema is evidence, not a requirement.

### I. Generated views

Specify human and machine output representations and manifest/freshness strategy.

### J. Search/query

Decide whether relational/SQLite, graph, FTS and vector layers are:

    canonical
    derived
    optional
    rejected

### K. Cold start / recovery

The design must preserve the Research 258 generate-independent break-glass path.

### L. PSMF seam

Show exactly which representation contracts belong to reusable framework mechanism versus ADS instance policy/state.

### M. Migration/Specification 028

Identify which current Representation 028 choices would likely be:

    RETAIN
    GENERALIZE
    AMEND
    SUPERSEDE

Do not create the final amendment set yet.

### N. Strongest alternative

Provide at least one materially different viable alternative and explain the trade-off.

### O. Falsifiers

State evidence that would cause you to amend or reject your own design.

## 6. Evaluation obligations

Explicitly assess the design against RR-01 through RR-18.

Do not collapse this into one numeric score.

Identify any requirement that remains partially satisfied or requires empirical qualification.

## 7. External research

You may use current authoritative external sources when they materially discriminate mechanisms.

Separate:

    ADS repository evidence
    external mechanism facts
    your architecture inference

Do not substitute generic industry fashion for ADS requirements.

## 8. Required output path

Write exactly one response:

    docs/model_collaboration/threads/MC-0026/messages/
        001_claude_independent_r8b_representation_architecture.md

Include:

    exact frozen base
    interaction claude-03
    conversation title
    independence/exposure statement
    selected candidate name
    complete RC1-RC12 mapping
    RR-01..RR-18 conformance discussion
    strongest alternative
    falsifiers

End with exactly:

    R8B_INDEPENDENT_CANDIDATE=<name>
    CURRENT_FILE_FORMAT_PRESERVATION_REQUIRED=YES|NO
    CANONICAL_GRAPH_DATABASE=YES|NO
    CANONICAL_PROJECT_SQL_DATABASE=YES|NO
    DERIVED_RELATIONAL_QUERY_LAYER=YES|NO|OPTIONAL
    SOURCE_LOCAL_STRUCTURED_METADATA=YES|PARTLY|NO
    BOUNDED_CANONICAL_REGISTRY=YES|PARTLY|NO
    EVENT_OR_RECEIPT_PERSISTENCE=NONE|SELECTIVE|BROAD
    GENERATED_VIEWS_AUTHORITATIVE=YES|NO
    BREAK_GLASS_REQUIRES_GENERATION=YES|NO
    SPEC028_REPRESENTATION_AMENDMENT_EXPECTED=YES|NO
    READY_FOR_COMPARATIVE_RECONCILIATION=YES|NO

## 9. Write boundary

Claude may write only:

    docs/model_collaboration/threads/MC-0026/messages/**

Do not modify routing, Research 260, Specification 028, current implementation, schemas, generated views, tests or any other collaboration thread.

    MC0026=OPEN
    MODE=INDEPENDENT_THEN_COMPARATIVE
    FROZEN_BASE=1fe4bbe4b2658532359411825d3b1d819a6c4c68
    CLAUDE_CANDIDATE=NEXT
    CHATGPT_CANDIDATE=INDEPENDENT_IN_PARALLEL
    PHYSICAL_MIGRATION_AUTHORIZED=false
