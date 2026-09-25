# Research 333: Codexless Runtime Bridge Product Vision, Repository Strategy, and Native GitHub Coexistence Update

**Date:** 2026-09-25
**Status:** OWNER PRODUCT VISION PRESERVED / CURRENT SAME-CONVERSATION COEXISTENCE OBSERVED / DEDICATED FUTURE WORKSTREAM REQUIRED / CURRENT AO-10 ROUTE UNCHANGED
**Scope:** Preserve the project owner's clarified vision for the custom Codexless Runtime Bridge as a substantial independently valuable software project, reconcile that vision with the historical ADS/local-runtime repository split, and record the current observation that the native ChatGPT GitHub connector and Codexless Runtime Bridge can now both execute in the same conversation.
**Authority:** Owner vision and current empirical environment evidence. This record does not choose the final public-product repository topology, provider strategy, upstream relationship, release architecture, or ADS integration boundary. It does not interrupt MC-0029 or authorize publication of the private runtime repository.

## 1. Product vision

The custom connector was never intended to be only a workaround for one missing ChatGPT capability.

Its durable value is that the project controls the capability surface, semantics, safety constraints, authority rules, error behavior, workflow composition and future expansion.

Research 105 through Research 123 already show this evolution from bounded local execution into a much broader runtime with evidence for local files, commands, flexible multi-repository authority, semantic Git, explicit Codex escalation, task/thread handoff, Browser integration, image and document access, PDF routing/rendering, Office-file handoff, runtime release/restart/rollback, protected GitHub authentication, GitHub parity, CI evidence publication, Actions orchestration, Git reference lifecycle and repository governance.

The exact target architecture remains open. The important preserved intent is that Codexless Runtime Bridge is potentially a serious reusable software product in its own right, not merely an ADS-internal helper.

## 2. Historical coexistence constraint

Research 123 and Validation 034 preserve a real historical ChatGPT host limitation:

    custom developer MCP / Codexless projected and callable
        while
    native GitHub connector failed to remain available in the same conversation

Repeated fresh-chat testing made same-conversation coexistence unreliable enough that Research 123 correctly treated it as a current platform constraint.

That limitation materially influenced the GitHub parity stage. Reproducing native GitHub capability inside Codexless meant ADS did not need to sacrifice local/runtime capabilities merely to gain remote GitHub access.

The historical evidence remains valid for the environment in which it was collected and must not be rewritten as though the failures never happened.

## 3. Current coexistence observation

Validation 211 records a materially different current result in chatgpt-30.

Within the same conversation:

    Codexless Runtime Bridge
        workspace authority read PASS
        project-context resolution PASS
        direct local repository read PASS

    native GitHub connector
        authenticated user lookup PASS
        ADS repository lookup PASS

    later interleaving
        additional Codexless repository/runtime reads PASS
        additional native GitHub repository/file reads PASS

Therefore the old coexistence limitation is no longer safe as an unquestioned statement about the current observed host.

Current interpretation:

    historical coexistence failure
        VERIFIED HISTORICAL EVIDENCE

    current same-conversation coexistence
        VERIFIED IN AT LEAST ONE CURRENT INTERACTION

    platform-wide / cross-client / repeated-chat coexistence
        NOT YET REQUALIFIED

The owner recalls that the earlier investigation used approximately ten separate chats and repeatedly failed, with only one connector family effectively available at a time. That recollection is consistent with the durable Research 123 / Validation 034 evidence.

A future dedicated stage should run a new controlled multi-chat and multi-surface matrix before declaring the old limitation fully retired.

## 4. Why this does not make the custom bridge obsolete

One reason for reproducing GitHub inside Codexless was continuity when native GitHub and custom MCP could not coexist. That reason is weaker if the new host behavior persists.

But a more fundamental reason remains: we control the bridge.

Research 123 first implemented the captured native GitHub action surface and then intentionally added selected beyond-parity families:

    Repository Administration
    CI Evidence Publication
    GitHub Actions Orchestration
    Git Reference Lifecycle
    Repository Branch-Safety Governance

This demonstrates the ability to add capabilities absent from a provider-owned connector, enforce stronger preconditions and expected-revision guards, shape semantic mutation surfaces, preserve no-replay behavior after mutation uncertainty, keep credentials/transport server-owned, and combine local and remote work.

The future architecture should evaluate native and custom providers as complementary or competing execution surfaces. Native availability does not by itself eliminate the value of Codexless.

## 5. Provider strategy is now a wider design space

Because both providers can currently coexist, future architecture may choose native GitHub for simple remote-only work, Codexless for local-plus-GitHub workflows, Codexless with native fallback, provider-neutral routing, selected dual-provider verification, or another evidence-derived design.

None is accepted here.

Future qualification should compare latency, availability, failure rate, freshness, result fidelity, pagination/continuation, schema quality, capability breadth, mutation safety, concurrency guards, uncertainty semantics, authentication friction, cross-device behavior, local/remote composability, recovery/fallback behavior, operational complexity and maintenance burden.

The native connector may be faster or simpler because it is platform-hosted. That is a hypothesis, not current evidence. Codexless may be stronger for tasks needing richer preflight/readback or project-controlled semantics. That must also be measured.

## 6. Current repository reality

Three distinct identities must not be conflated.

### ADS public repository

    shakaarlatief/autonomous-data-science-system

This remains the public ADS development and architecture authority and contains the durable reasoning and qualification history that shaped Runtime Bridge.

### Private local-runtime repository

    shakaarlatief/autonomous-data-science-system-local-runtime

Current visibility is private.

Its own README defines it as reviewed non-secret machine-local/runtime implementation evidence and says it is not the project-development authority.

Its candidate-tree layout, activation/publication scripts and release/evidence material reflect rapid experimental engineering and preservation. That history is valuable, but it has no target public-product architecture preservation right.

### Upstream Codexless

    liyana31811/Codexless

Current observed upstream evidence on 2026-09-25:

    public repository
    Apache License 2.0
    README identifies Codexless 0.1.2 Preview

Any public productization of our extended Runtime Bridge must explicitly address provenance, attribution, derivative-work obligations, upstream divergence and possible contribution/reuse paths.

## 7. Do not simply make the private runtime repository public

The private local-runtime repository was designed primarily for implementation preservation, runtime evidence, machine/runtime provenance, release materialization and operational continuity.

Making it public as-is would preserve historical structure rather than derive a professional product architecture.

The future question is:

    What repository and product architecture should a serious reusable
    Codexless Runtime Bridge project have now?

not:

    How do we clean up the current private repo enough to expose it?

The current repo is evidence and a migration source.

## 8. Candidate future repository separation

A plausible starting candidate is:

    public Runtime Bridge product repository
        reusable source, tests, docs, install, security, CI/CD, releases,
        compatibility, changelog and contribution model

    private operational/runtime repository
        machine-specific state, deployment/materialization evidence,
        private operational continuity and host-specific material

    ADS repository
        ADS-specific architecture, integration, qualification and governance

This is a candidate only. A dedicated workstream must compare alternatives such as a clean fork, an upstream extension layer, upstream contributions plus a smaller ADS integration layer, a single public repo with private external state, a multi-package design, or another first-principles architecture.

Repository count and boundaries must follow responsibility, lifecycle, authority, release and contribution needs rather than today's physical layout.

## 9. Dedicated productization workstream

The future stage should begin with requirements and architecture, not file moves.

It should derive and qualify at least product identity, target users/environments, public capability model, local authority/trust, MCP transport, runtime lifecycle, provider abstraction, GitHub strategy, Codex escalation, files/documents, Browser/Office boundaries, secrets/credentials, dependency architecture, install/upgrade/rollback, cross-platform support, diagnostics, tests, CI/CD, releases/versioning, compatibility, security, contribution model, upstream relationship, licensing/NOTICE/attribution, documentation, public/private boundaries, ADS integration and migration from historical runtime evidence.

Existing implementation should be mined for proven capabilities and hard-earned failure evidence, but the target may reorganize or replace it.

## 10. Scheduling relative to current ADS work

This work is important, but it should not opportunistically derail the current AO-10 / MC-0029 qualification sequence.

Preferred scheduling:

    preserve the vision now
        -> complete the current bounded AO-10 / MC-0029 decision sequence
        -> activate a dedicated Runtime Bridge productization /
           repository-architecture workstream at a clean boundary

    unless Runtime Bridge becomes a direct blocker or materially changes
    the active ADS architecture before then

The later workstream should use the stronger Project-system semantics for requirements, authority, identity, provenance, obligations, workstreams, architecture evolution, assurance, migration, cutover, reconstruction and provider selection.

## 11. Dynamic-architecture consequence

The coexistence change is exactly the kind of external capability change the future ADS Project system should detect and route automatically:

    historical assumption
        native GitHub + custom developer MCP coexistence unreliable

    new evidence
        both callable in the same current conversation

    desired system behavior
        detect changed capability
        bind it to affected assumptions/workstreams
        reopen only affected design questions
        preserve historical evidence
        qualify the new environment
        update provider strategy prospectively

The custom bridge itself is subject to the same rule. No capability, repository structure, provider choice or custom mechanism receives permanent preservation rights merely because it was built successfully.

## 12. Preserved owner intent and non-decision boundary

Durable owner intent:

    Codexless Runtime Bridge should eventually be treated as a professional
    software project in its own right.

    Its key advantage is project-owned extensibility and semantic control,
    not merely parity with a provider-owned connector.

    Public/private repository architecture should be designed properly,
    not inherited accidentally from historical ADS development.

    The old native-GitHub/custom-MCP coexistence limitation appears to
    have changed and must be requalified rather than silently assumed.

    A dedicated future stage should handle productization, repository
    architecture, upstream/provenance strategy, provider comparison,
    migration and professional public release.

Nothing here authorizes making the private runtime repo public, creating a new public repo, moving source, changing the active installation, changing GitHub auth, retiring custom GitHub capability, preferring either provider, forking upstream, opening upstream pull requests, or changing MC-0029/R2.

    RUNTIME_BRIDGE_PRODUCT_VISION=PRESERVED
    CURRENT_SAME_CHAT_COEXISTENCE=OBSERVED
    BROADER_COEXISTENCE_REQUALIFICATION=PENDING
    PUBLIC_PRODUCT_REPOSITORY_ARCHITECTURE=UNDECIDED
    DEDICATED_FUTURE_WORKSTREAM=REQUIRED
    CURRENT_AO10_ROUTE=UNCHANGED
