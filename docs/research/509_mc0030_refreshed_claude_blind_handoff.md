# Research 509: refreshed MC-0030 Claude blind handoff after R0 amendment

**Date:** 2026-10-04
**Status:** REFRESHED CLAUDE BLIND HANDOFF FROZEN / MESSAGE 001 NEXT
**Parent:** Research 503-508
**Selected logical target:** THIN_CENTRED_HYBRID_V03
**Collaboration thread:** MC-0030
**Neutral R0 basis:** Research 503 + Research 506 + Research 507
**ChatGPT independent position:** Research 504 + Research 508, hidden from Claude
**Scope:** Supersede the stale Research 505 handoff and freeze the exact Claude independent-design task after the semantic-organization and external-execution amendments.
**Authority:** Collaboration-routing record only. No physical architecture is selected.

## 1. Supersession

Research 505 / Checkpoint 842 were correct at the time they were frozen, but they predate the owner clarification that produced Research 506-508.

They are therefore superseded for launch purposes by this handoff.

Do not send the old Research 505 prompt to Claude.

## 2. Claude independent task

Claude must independently derive the strongest physical/software realization architecture for the already owner-selected:

    THIN_CENTRED_HYBRID_V03.

The design must cover the whole Project System, not only semantic storage.

Claude must answer the complete neutral R0 basis:

    Research 503
        original R0-R01 through R0-R44

    Research 506
        standalone Runtime Bridge ownership boundary input

    Research 507
        R0-R45 through R0-R62
        semantic organization/navigation
        external execution infrastructure.

## 3. First-principles freedom

Claude may redesign from first principles:

    repository topology
    files/folders
    canonical sources
    schemas and serialization
    storage/index/cache strategy
    package/module boundaries
    APIs / CLI / UI
    AO physical realization
    WARRANT-F / CI/CD realization
    semantic organization/navigation
    execution/provider boundaries
    branch/merge/review workflow
    collaboration procedures
    concurrency
    recovery/rebuild
    public/private boundaries
    migration/rollback
    observability
    deployment
    architecture documentation.

Existing mechanisms are evidence and current-authority constraints where genuinely live, not target constraints.

## 4. Semantic organization requirement

Claude must explicitly address the still-open semantic-organization problem.

Research 217's:

    18 subjects
    6 navigation parents
    polyhierarchy
    preferred_subject
    source-owned memberships

are evidence and one comparator only.

Claude must consider materially different approaches, including:

    controlled subject/facet systems
    typed-relational / graph-like organization
    search/retrieval-first organization
    hybrids.

Claude must distinguish:

    information-role ownership
    governing semantic authority
    semantic discovery/navigation
    probabilistic/generated retrieval.

Generated search/similarity must not silently become governing authority.

## 5. Runtime Bridge / external execution requirement

Claude must treat Research 506 as neutral design input.

The question is not:

    how should ADS absorb the current Runtime Bridge?

The question is:

    what provider-neutral execution/tool boundary should the professional Project System have,
    and how should Codexless Runtime Bridge fit as reusable infrastructure?

Claude must address:

    generic bridge versus ADS-specific policy/capabilities
    generic product versus host-private deployment state
    project/workspace policy
    provider capability discovery
    normalized execution/evidence receipts
    Runtime Bridge / GitHub / Claude / local / future provider coexistence
    degradation/fallback
    portability
    whether any Runtime Bridge extraction is needed before physical-target selection.

No standalone Runtime Bridge repository is assumed selected merely by Research 506.

## 6. Permitted current-branch reads

Before Message 001 is committed, Claude may read these current files by exact path:

    docs/research/503_r0_realization_requirements_and_independent_design_charter.md
    docs/research/506_codexless_runtime_bridge_standalone_product_boundary.md
    docs/research/507_r0_semantic_organization_and_external_execution_amendment.md
    docs/model_collaboration/threads/MC-0030/BRIEF.md
    docs/model_collaboration/threads/MC-0030/THREAD.md
    docs/model_collaboration/threads/MC-0030/STATE.json
    docs/current_routing.json

For substantive project history and selected logical architecture, Claude may inspect the repository at frozen ref:

    c459e9c8ac4435b80d4ac9d2bdb215aa72c13adc

including Research 500-502, D-036 and earlier evidence as necessary.

## 7. Blind exclusions

Before Message 001 is durably committed, Claude must not inspect, search into, list into, summarize or derive from:

    docs/research/504_chatgpt_independent_r0_physical_realization_candidate_a.md
    docs/research/508_chatgpt_r0_candidate_a_amended_requirements_addendum.md
    docs/checkpoints/841_chatgpt_r0_physical_candidate_frozen.md
    docs/checkpoints/844_r0_amendment_and_chatgpt_addendum_frozen.md
    docs/ARCHITECTURE_PROGRAM_OVERVIEW.md
    docs/CURRENT_STATE.md
    any summary or derivative of ChatGPT Candidate A
    any future comparative MC-0030 artifact.

Claude must not use broad current-branch repository search that could surface those files.

If accidental exposure occurs, stop and report exactly what was exposed.

## 8. Required independent output

Message 001 must provide:

    one coherent preferred whole-system physical/software architecture

    at least two materially different alternatives

    repository/software boundaries

    canonical source-of-truth/storage design

    owner acceptance/authenticity mechanism

    J1/J2/J3 realization

    completion and anti-self-certification realization

    semantic organization/navigation/discovery architecture

    AO physical realization and activation/retrieval boundary

    lineage/repartition/realization succession

    shared predicate/versioning design

    generated-view/index/cache strategy

    external executor/provider architecture
    including Runtime Bridge placement

    CLI/API/runtime surfaces

    tests

    CI/CD and WARRANT-F realization

    branch/merge/review/concurrency design

    multi-model/tool collaboration

    public/private design

    recovery/rebuild design

    migration/shadow/cutover design

    Project System / ADS Product separation

    observability

    architecture evolution

    current-mechanism reuse/refine/reimplement/retire dispositions

    material risks/falsifiers

    smallest decision-relevant empirical probes before physical target selection.

## 9. Write boundary

Claude may write exactly one independent response under:

    docs/model_collaboration/threads/MC-0030/messages/**

Recommended exact path:

    docs/model_collaboration/threads/MC-0030/messages/001_claude_independent_r0_physical_architecture.md

Use the Claude-side GitHub connector for this bounded write.

Do not modify any other repository path.

## 10. Stop boundary

After committing Message 001:

    report exact commit SHA
    report exact written path
    state whether blindness remained intact
    disclose accidental exposure if any
    summarize the preferred architecture at a high level
    stop.

Do not:

    inspect ChatGPT Candidate A after Message 001 unless explicitly authorized
    begin comparative review
    select the physical target
    implement
    migrate
    amend Specification 028
    switch authority.

## 11. Current boundary

    MC0030=OPEN
    PHASE=R0_CLAUDE_INDEPENDENT_DESIGN_AMENDED
    NEXT_ACTOR=claude

    NEUTRAL_R0=RESEARCH_503_PLUS_506_PLUS_507
    CHATGPT_CANDIDATE=RESEARCH_504_PLUS_508
    CLAUDE_BLIND_TO_CHATGPT_CANDIDATE=true

    PHYSICAL_ARCHITECTURE_SELECTED=false
    IMPLEMENTATION_STARTED=false
    MIGRATION_AUTHORIZED=false
    SPECIFICATION_028_AUTHORITY=UNCHANGED

    NEXT=CLAUDE_MESSAGE_001
