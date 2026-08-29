# Research 103: Repository Knowledge Discoverability and Risk-Scaled Verification Audit

**Date:** 2026-08-29  
**Status:** IMPLEMENTATION OPENED / GOVERNING METHOD RECONCILIATION  
**Research class:** DEVELOPMENT_METHOD / KNOWLEDGE_ARCHITECTURE / VERIFICATION_EFFICIENCY  
**Scope:** Whole-repository audit of knowledge preservation, topic discoverability, checkpoint granularity and Cockpit verification cost as the ADS repository grows.  
**Interaction environment:** ChatGPT  
**Interaction session:** `chatgpt-10`  
**Branch:** `v1-cockpit-design-exploration`

## 1. Trigger

Two scaling concerns converged during the Project Cockpit design exploration.

First, a very small Conversation rail refinement took roughly twenty minutes because the complete 78-test Cockpit browser suite was repeatedly run while the implementation was still being iterated.

Second, the project owner asked whether the growing body of foundations, research memos, specifications, checkpoints and specialized ledgers was still actively linked into a topic-oriented knowledge library so that a future model can find governing evidence without being reminded of document numbers or prior chat history.

The audit therefore examines the development system itself rather than the ADS product design.

## 2. Sources audited

The audit reviewed the current and historical preservation architecture, including:

```text
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/research/064_rapid_iteration_repository_preservation_audit_and_checkpoint_hygiene.md
docs/checkpoints/README.md

docs/KNOWLEDGE_MAP.md on v1-cockpit-design-exploration
docs/KNOWLEDGE_MAP.md on v1-frontend-spike

docs/CURRENT_STATE.md
docs/current_routing.json

docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/methodological_knowledge/COVERAGE_MAP.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/model_collaboration/REVIEW_INBOX.md

.github/workflows/cockpit-reintegration-fidelity.yml
frontend/e2e/cockpit-reintegration*.spec.ts
```

The inventories of current foundations, specifications and Research 001-102 were also reviewed to test whether substantive knowledge remained present even where routing quality had drifted.

## 3. Finding: substantive durability remains strong

The repository has not lost the major accumulated ADS knowledge.

The architecture still separates:

```text
canonical/current knowledge
foundational rationale
bounded research evidence
explicit specifications
historical checkpoints
experiment/status ledgers
collaboration provenance
exact implementation provenance
Git history
```

Specialized domains also retain their own durable indexes and contracts. Examples include the Methodological Knowledge Universe coverage map, Source Universe bootstrap, Phase-C Cockpit decision ledger and exact implementation manifest.

Therefore the main scaling problem is not missing storage. It is discoverability and routing quality.

## 4. Finding: the global Knowledge Map materially drifted

Foundation 014 established `docs/KNOWLEDGE_MAP.md` as the primary human/model navigation layer for the repository. Its role was to map important topics to the canonical, foundational, research, specification and historical artifacts that discuss them.

That broad library role existed clearly on the promoted `v1-frontend-spike` branch, with project-wide topic families covering system vision, project state, reusable knowledge, runtime/persistence/tooling, retrieval/MethodologicalHorizon, recommendation/disposition/provenance, Methodological Knowledge Universe, Source Universe, Project Cockpit, multi-model development and open questions.

On the current `v1-cockpit-design-exploration` branch, however, `KNOWLEDGE_MAP.md` gradually became dominated by the current Cockpit continuation route and recent Research 097-102 / Checkpoint 258-264 state.

The underlying files remained present, but the global topic library was effectively displaced by a second current-state document.

This is a real discoverability regression. A new session could reconstruct the immediate Cockpit boundary but had a weaker path to unrelated or older ADS knowledge unless it already knew what to search for.

The project owner's memory of a categorized "library" is therefore accurate.

## 5. Finding: the threshold for structural map protection has been crossed

Research 064 previously concluded that the preservation architecture was sound and stronger indexing machinery should be deferred until concrete discoverability pressure appeared.

That pressure now exists:

```text
100+ research memos
24 foundations
24 specifications
260+ checkpoints
multiple specialized ledgers/indexes
one global map that drifted into stage-specific status duplication
```

The appropriate response is still not a semantic database or generated mega-catalog. The problem is narrower: restore the intended global routing layer and protect it structurally.

## 6. Finding: checkpoint principles were sound, practice became too granular

`docs/checkpoints/README.md` already distinguishes meaningful state boundaries from ordinary commits and says that micro visual corrections, small geometry/copy refinements and implementation fixes inside the same accepted hypothesis do not inherently require new numbered checkpoints.

Recent Cockpit iteration nevertheless drifted toward checkpoint-per-fix behavior. Several small presentation refinements could have remained iterations inside one open human-review boundary.

The strengthened operational rule is:

> Keep an open review/checkpoint boundary while a cluster of small iterations answers the same question. Record material iterations inside that boundary. Advance the checkpoint number only when project state, authority, accepted conclusion, risk boundary or continuation point materially changes.

Git remains the exact implementation history underneath that aggregated narrative.

## 7. Finding: full Cockpit verification is too coarse for active iteration

The existing Cockpit workflow triggered on a broad set of design-lab and regression paths and always ran the complete `cockpit-reintegration*.spec.ts` browser suite.

That is appropriate for integrated acceptance, but inefficient while tuning a narrowly bounded visual surface.

The method had conflated:

```text
Did this local change work and preserve adjacent invariants?

with

Is the complete integrated Cockpit still source-faithful and safe to accept/promote?
```

Those questions need different verification scopes.

## 8. Decision: Development Method v0.6 risk-scaled verification

Development Method v0.6 introduces:

```text
V0  documentation / provenance only
    relevant structural/routing/metadata validators

V1  targeted
    exact regression for one isolated change + adjacent invariant(s)

V2  subsystem
    relevant regressions for one coherent subsystem

V3  full integrated
    complete source-faithful Cockpit suite for shared/cross-cutting/uncertain changes

V4  promotion / release
    V3 + relevant provenance, routing, metadata, build and promotion gates
```

Rules:

```text
unknown blast radius -> V3
shared core mechanism -> V3
pull request / explicit integration boundary -> V3 or V4 as appropriate
explicit [full-cockpit] commit marker -> force V3
small visual iteration -> V1/V2 before human review
human acceptance of a meaningful boundary -> broader gate required to close it
```

A V1/V2 pass must never be described as a full Cockpit pass.

## 9. Decision: human review moves earlier for low-risk visual tuning

For localized visual refinements:

```text
implement
-> targeted/subsystem deterministic check
-> human visual review
-> refine with the same narrow check if needed
-> run one broader/full gate when the meaningful review boundary closes
```

This avoids paying integrated acceptance cost for designs the human may immediately reject. Cross-cutting changes may still require V3 before human review.

## 10. Decision: conservative automated test selection

The Cockpit workflow gains:

```text
scripts/select_cockpit_verification.py
```

The selector may narrow verification only for high-confidence local path families. Any mixed, shared or unknown change falls back to the complete Cockpit suite.

The workflow also gains branch-level concurrency cancellation so obsolete in-progress verification is cancelled when a newer push supersedes it.

Documentation/checkpoint-only pushes may enter V0 and avoid Node/Chromium installation entirely.

## 11. Decision: restore an evergreen topic library

`docs/KNOWLEDGE_MAP.md` is restored to two distinct responsibilities:

```text
Current continuation route
    the small set of artifacts needed to resume the exact current boundary

Evergreen topic library
    durable project-wide topic -> source routing independent of active stage
```

The evergreen library defines seventeen topic families spanning system vision, project state, reusable knowledge, evaluation/falsification, V1 runtime/persistence, retrieval/MethodologicalHorizon, recommendation/calibration, Methodological Knowledge Universe, Source Universe, development/continuity, Cockpit architecture, visual grammar, interaction states, Conversation Workspace, Cockpit provenance/fidelity, Cockpit shell/rail and canonical history.

Each topic points to governing canonical sources and deeper evidence rather than copying substantive contents. Specialized indexes remain specialized and are linked rather than duplicated.

## 12. Decision: protect the map structurally, not semantically over-automate it

A lightweight validator checks:

```text
required evergreen topic markers exist
topic identifiers are unique
each required topic routes to repository artifacts
literal/globbed routed paths resolve
current continuation and evergreen-library sections remain present
```

It does not infer which document is semantically authoritative. Authority remains governed by document status, scope and chronology.

This is intentionally simpler than embeddings, a graph database or automatic semantic tagging.

## 13. Decision: coherent repository writes

When several canonical/routing files represent one logical state transition, commit them coherently where practical rather than as a long chain of one-file commits.

This reduces transient contradictory routing states, redundant CI starts, noisy history and continuity windows between dependent writes.

Independent changes should remain separate.

## 14. Continuity correction

The audit also found `docs/CONTINUITY.md` still naming an older ChatGPT session while current routing had already moved to `chatgpt-10`.

Development Method v0.6 aligns Continuity with provider-neutral provenance and makes the evergreen Knowledge Map part of standard new-session reconstruction.

## 15. Alternatives deliberately not selected

Not introduced now:

```text
vector database over repository docs
a second generated semantic knowledge catalog
a mega-ledger containing every checkpoint/research relation
a Research memo for every frontend tweak
a complete browser gate after every implementation commit
```

These add complexity without addressing the diagnosed failure as directly as better routing and risk-scaled verification.

## 16. Expected effect

```text
knowledge remains deeply preserved
important topics become easier to discover
micro-iterations produce less checkpoint noise
small frontend changes receive fast relevant verification
full integrated fidelity remains mandatory at meaningful acceptance/promotion boundaries
```

The goal is not fewer safeguards. It is to apply each safeguard where its evidence is actually informative.
