# Research 508: ChatGPT R0-CANDIDATE-A addendum for amended R0 obligations

**Date:** 2026-10-04
**Status:** CHATGPT INDEPENDENT ADDENDUM FROZEN / REMAINS HIDDEN FROM CLAUDE
**Parent:** Research 504, 507
**Candidate:** R0-CANDIDATE-A / Repository-Native Control Record Graph
**Scope:** Extend ChatGPT's already-frozen independent physical candidate so it answers the neutral R0-R45 through R0-R62 amendment before Claude begins its blind independent design.
**Authority:** Candidate evidence only. No physical target is selected.

## 1. Independence note

This addendum is authored by ChatGPT after owner clarification and Research 507, but before Claude's independent Message 001.

Claude must remain blind to:

    Research 504
    Research 508
    Checkpoint 841
    this candidate's summaries/derivatives

until Claude's independent design is durably frozen.

## 2. Candidate-A semantic organization proposal

Candidate A does **not** adopt the Research 217 18-subject hierarchy as the primary future semantic architecture by default.

It proposes a layered **Semantic Discovery and Navigation Fabric** whose dimensions remain separate.

### Layer 1: authoritative information position

R7-style information role / bounded responsibility remains the primary answer to:

    what kind of Project information is this?
    who naturally owns it?
    where does its governing lifecycle belong?

This is not a semantic subject taxonomy.

### Layer 2: governed semantic descriptors and typed relations

Where stable cross-document semantics materially help control, retrieval or impact analysis, source/owner-governed descriptors may declare:

    concern/facet identities
    typed relations
    exact governed references
    optional preferred human-navigation placement.

These declarations are explicit and inspectable.

They do not require one universal subject tree.

### Layer 3: generated retrieval indexes

The system may generate:

    full-text index
    lexical facets
    optional embedding/vector similarity
    relation adjacency
    responsibility/lifecycle filters
    recent/currentness filters
    task-oriented candidate sets.

These are disposable and rebuildable.

Similarity/search score is never semantic authority.

### Layer 4: generated human/agent views

Human and agent orientation may combine:

    information role
    governed facets/relations
    currentness
    workstream
    lifecycle
    semantic retrieval
    explicit authority links.

The same canonical knowledge can therefore appear in several generated navigation views without duplicating authority.

## 3. Candidate-A stance on subjects

A controlled subject vocabulary remains a viable **facet** if comparative evidence shows that it improves human navigation and fresh-agent reconstruction enough to justify its authoring/evolution burden.

The Research 217 vocabulary is one comparator.

Candidate A does not assume:

    exactly 18 subjects
    exactly 6 parents
    one preferred_subject field
    subject membership as the only semantic organization.

Possible outcome:

    governed subject/facet catalog
        + typed relations
        + hybrid lexical/semantic retrieval
        + generated task-specific views.

But that outcome must earn selection empirically.

## 4. AO integration

AO may use semantic discovery to surface candidate context.

The activation path distinguishes:

    candidate retrieval
        non-authoritative recall mechanism

    governing activation
        explicit obligations, accepted relations, current workstream/process rules, and deterministic control facts.

Therefore a high semantic similarity score cannot itself authorize or prohibit action.

AO should preserve:

    why a knowledge item was retrieved
    which deterministic rule, if any, caused activation
    provenance to the source.

## 5. Semantic-organization probes proposed by Candidate A

Before physical-target selection, compare at least:

    S1 controlled-subject/facet baseline
        derived fairly from Research 217

    S2 typed-relational + responsibility/lifecycle navigation

    S3 hybrid S2 + lexical/semantic generated retrieval.

Use real Project tasks covering:

    owner/human browse-to-answer
    fresh-agent reconstruction
    AO candidate-context retrieval
    impact analysis
    migration planning
    cross-cutting architecture evolution.

Measure:

    answer correctness
    missed relevant sources
    irrelevant source burden
    explicit provenance
    authoring/maintenance burden
    deterministic versus probabilistic dependence
    resilience when generated indexes are deleted.

Candidate A currently expects S3 to lead, but does not treat that as established.

## 6. External executor architecture

Candidate A adds a first-class provider-neutral package boundary, conceptually:

    project_system.executors

with an interface such as:

    capabilities()
    prepare(action_contract)
    execute(prepared_action)
    inspect(receipt_ref)
    recover(operation_ref)

and normalized outputs:

    ExecutionReceipt
    EvidenceReceipt
    CapabilitySnapshot
    FailureReceipt.

The exact API names are not selected.

## 7. Runtime Bridge placement

Codexless Runtime Bridge sits **outside** the ADS Project-System package as one executor adapter.

Conceptually:

    Project System / AO
        -> executor interface
            -> RuntimeBridgeAdapter
                -> standalone Codexless Runtime Bridge

ADS owns:

    allowed workspace identities
    ADS capability/policy profiles
    exact qualified bridge version
    integration contract
    receipt translation
    ADS-specific capability packs where genuinely necessary.

The standalone Runtime Bridge owns:

    generic local/Git/GitHub/browser/tool execution mechanics
    generic authority enforcement
    generic credential/transport/update/recovery behavior.

Host-private deployment state remains outside the public ADS repository.

## 8. Multi-provider rule

The Project System must remain operable with multiple executor families.

For example:

    Runtime Bridge
    GitHub connector
    Claude-side connector
    local controlled executor
    future cloud executor.

Not every provider needs identical capabilities.

AO chooses only among capabilities allowed by the current governed action and provider policy.

WARRANT-F evaluates the evidence/receipt required for the consequence.

Provider identity cannot substitute for warrant.

## 9. Capability and version binding

An executed action should bind:

    provider identity
    provider version/capability snapshot
    exact action contract
    exact subject/base revision
    execution receipt
    evidence provenance.

If a required capability is absent:

    refuse
    route review
    or use an explicitly allowed alternate provider.

Do not silently degrade a governed action to a weaker mechanism.

## 10. Runtime Bridge extraction consequence

Candidate A does not require Runtime Bridge extraction before ADS R0/R1 completion.

Instead:

    freeze executor contract first
    classify current Runtime Bridge implementation
    design standalone product independently
    migrate generic code/config/state into the correct repositories
    qualify ADS against the standalone release
    then retire duplicated ADS-owned generic internals.

This prevents the generic product from being shaped accidentally around today's ADS implementation details.

## 11. Candidate-A revised risk/probe list

Add:

    P-SEMANTIC-ORG
        compare subject/facet, typed-relational and hybrid retrieval/navigation families

    P-AO-RETRIEVAL
        distinguish recall assistance from governing activation

    P-EXECUTOR
        demonstrate one ActionContract/receipt path through at least two executor families without semantic branching in AO

    P-RB-SCOPE
        classify representative current Runtime Bridge capabilities as generic core, generic optional, ADS-specific, host-private, historical/retire.

These join the Research 504 probes.

## 12. Current disposition

    CHATGPT_R0_CANDIDATE=R0-CANDIDATE-A
    BASE=RESEARCH_504
    AMENDED_REQUIREMENTS_ADDENDUM=RESEARCH_508

    SEMANTIC_ORGANIZATION=PROPOSED_LAYERED_FABRIC_NOT_SELECTED
    RUNTIME_BRIDGE=EXTERNAL_EXECUTOR_ADAPTER_NOT_ADS_SUBSYSTEM
    RUNTIME_BRIDGE_EXTRACTION=DEFERRED_UNTIL_INTERFACE_STABLE

    CLAUDE_EXPOSURE_TO_RESEARCH504_OR_508=FORBIDDEN_UNTIL_MESSAGE001_FROZEN
    PHYSICAL_ARCHITECTURE_SELECTED=false

    NEXT=REFRESH_CLAUDE_BLIND_HANDOFF
