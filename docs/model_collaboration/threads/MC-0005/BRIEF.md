# MC-0005 Brief: Development Method v0.7 Repository Information Architecture Review

**Thread:** MC-0005  
**Date opened:** 2026-08-29  
**Topic:** Adversarial second-model review of the finalized ADS repository information architecture and canonical knowledge-preservation surfaces  
**Authority:** Neutral review brief. It requests critique of the frozen v0.7 result but does not make the reviewer or its future message authoritative.  
**Coordination branch:** `v1-cockpit-design-exploration`  
**Exact review target:** `c834d8298b86a0185ffcc0ffa62d0e9c178cc2ad`

## Why this review exists

The project owner explicitly asked whether a second strong model should review the repository architecture after the project had accumulated a large amount of durable knowledge.

The target architecture is consequential because it determines how future ChatGPT, Claude and other collaborators reconstruct current state, discover older knowledge, distinguish authority from history, and preserve new work as the repository grows.

This is therefore a justified second-model review even though the architecture has already passed its deterministic validation gates.

The review is **non-blocking** for the current Cockpit product human-review gate. It may expose a future Level-2 correction, but the existence of a pending review does not itself reopen Checkpoint 266.

## Frozen candidate under review

Review exactly:

```text
c834d8298b86a0185ffcc0ffa62d0e9c178cc2ad
```

Do not silently substitute a later descendant.

The candidate's intended responsibility split is:

```text
README.md
    stable repository landing page

docs/README.md
    structural repository/documentation guide

docs/CURRENT_STATE.md
    sole human-readable live project state

docs/current_routing.json
    sole machine-readable live routing pointer

docs/KNOWLEDGE_MAP.md
    evergreen semantic subject -> knowledge library

docs/CONTINUITY.md
    cross-session reconstruction / recovery procedure

docs/DEVELOPMENT_METHOD.md
    operational Level-2 development / preservation / verification method

docs/MAJOR_CHANGES.md
    selective structural history

docs/VISION.md
    stable canonical target-system direction

docs/PRINCIPLES.md
    stable working principles

docs/DECISIONS.md
    explicit accepted decisions and supersession history

docs/OPEN_QUESTIONS.md
    current canonical unresolved-question register
```

The Knowledge Map permits one source to belong to multiple subjects and mechanically requires all numbered Foundations, Specifications and Research records to have at least one semantic route. Numbered checkpoints use semantic range coverage plus direct links for especially important milestones.

## Required review questions

Do not begin from an assumption that the architecture is good. Search for failure modes.

Evaluate at least:

1. Are the global files assigned genuinely distinct jobs, or is important overlap/duplication still present?
2. Is `CURRENT_STATE.md` the right owner of human-readable live state, with `current_routing.json` as the machine pointer?
3. Is `docs/KNOWLEDGE_MAP.md` correctly semantic-only, or should current routing or structural information live there too?
4. Is `docs/README.md` the right structural table of contents, or does that create unnecessary indirection?
5. Are `VISION.md`, `PRINCIPLES.md`, `DECISIONS.md`, `OPEN_QUESTIONS.md`, `MAJOR_CHANGES.md`, `DEVELOPMENT_METHOD.md` and `CONTINUITY.md` all justified as separate canonical surfaces?
6. Are the authority/supersession/history rules understandable enough that a future model will not treat old checkpoints/research as current truth?
7. Does exhaustive semantic routing of numbered Foundations/Specifications/Research scale well, or will the Knowledge Map itself become an unmaintainable bottleneck?
8. Is semantic checkpoint-range routing a good compromise, or is it too coarse to recover older decisions reliably?
9. Do specialized indexes such as the Cockpit decision ledger, implementation manifest, methodological coverage map, Source Universe material and collaboration inbox compose cleanly with the global map?
10. Are the validators protecting real invariants, or are any of them likely to become brittle maintenance tax?
11. Does the V0-V4 verification scheme and micro-checkpoint aggregation remain coherent with the information architecture?
12. Are important repository artifact families or authority layers missing?
13. If the repository grows by an order of magnitude, what is the first part of this architecture most likely to fail?
14. What simpler alternative architecture is strongest, and why should or should not ADS adopt it?
15. Which findings, if any, are **must-fix now**, **should improve later**, or **acceptable trade-offs**?

## Required review behavior

A useful review should include:

```text
overall disposition
strongest parts
must-fix findings
non-blocking improvements
strongest plausible failure mode
strongest alternative architecture considered
scaling assessment
validator/maintenance assessment
what evidence would change the reviewer's position
```

Agreement is not the goal. Calibrated criticism is.

## Minimal governing read set

Start from the exact frozen target and read:

```text
README.md
docs/README.md
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/CURRENT_STATE.md
docs/current_routing.json
docs/KNOWLEDGE_MAP.md
docs/VISION.md
docs/PRINCIPLES.md
docs/DECISIONS.md
docs/OPEN_QUESTIONS.md
docs/MAJOR_CHANGES.md
docs/research/103_repository_knowledge_discoverability_and_risk_scaled_verification_audit.md
docs/research/104_repository_information_architecture_and_exhaustive_knowledge_routing_refinement.md
docs/checkpoints/266_repository_information_architecture_and_exhaustive_knowledge_routing.md
```

Inspect specialized indexes or validators when needed to test a claim rather than trusting their summaries.

## Write scope

Claude may write only:

```text
docs/model_collaboration/threads/MC-0005/messages/**
```

Expected first durable message:

```text
docs/model_collaboration/threads/MC-0005/messages/001_claude_v07_information_architecture_review.md
```

Do not modify the candidate architecture directly. ChatGPT remains task owner and will disposition findings separately after the review.
