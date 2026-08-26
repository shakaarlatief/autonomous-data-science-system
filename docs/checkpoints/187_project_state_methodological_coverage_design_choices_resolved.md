# Checkpoint 187: Project-State Methodological Coverage Diagnostic Design Choices Resolved

**Date:** 2026-08-24  
**Status:** Question A successor design choices resolved; Specification 022 not frozen  
**Checkpoint class:** SCIENTIFIC DESIGN BOUNDARY  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Preserves the deliberate design resolution for the first project-state-to-methodological-horizon coverage diagnostic after the Checkpoint 186 architecture/evaluation review.  
**Authority:** Design checkpoint only. It does not freeze Specification 022, authorize implementation or provider execution, promote benchmark knowledge into accepted methodological authority, select final production navigation policy, or modify/rescore Specifications 015-021.  
**Design session:** 05  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 05 - Selective Context Promotion & Reasoning Vertical Slice  
**Branch:** `v1-methodological-navigation-coverage-diagnostic`  
**PR:** #68, draft  
**Starting integration head:** `0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e`

## Starting boundary

Research 031 / Checkpoint 186 established that the next architecture-representative evaluation should begin from evolving project state and primarily isolate:

```text
A. path discovery / methodological coverage
B. applicability / missing context
```

rather than repeating downstream supplied-action disposition calibration.

The exact Checkpoint 186 review head was:

```text
934db7d0ce4e95ddde774f94da5bf3361defd03f
```

and passed:

```text
Current routing consistency               32758338857  success
V1 disposition semantics diagnostic       32758338596  success
V1 autonomous live experiment launcher CI 32758338571  success
V1 blocking calibration diagnostic        32758338582  success
Checkpoint metadata                       32758338499  success
V1 reasoning context value                32758338559  success
```

PR #67 was then marked ready and merged unchanged into `v1-frontend-spike` at:

```text
0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e
```

The successor design branch was created from that exact promoted merge.

## Primary design record

```text
docs/research/032_project_state_to_methodological_horizon_coverage_diagnostic_design.md
```

Initial Research 032 commit:

```text
1fb81168dbfed919783c22d503c8c81236a88e17
```

Draft PR:

```text
#68  Design project-state methodological coverage diagnostic
```

## Resolved experiment architecture

The preferred first successor experiment class is now concretely shaped as:

```text
Project-State-to-Methodological-Horizon Coverage Diagnostic
```

The practical comparison is:

```text
GENERIC
    canonical evolving project state
        -> one strong reasoner call
        -> surfaced methodological concerns

ADS_HORIZON
    same canonical evolving project state
        -> deterministic generic state projection
        -> accepted hybrid retrieval
        -> one-hop governed relation expansion
        -> deterministic applicability / missing-context evaluation
        -> explained bounded MethodologicalHorizon
        -> one strong reasoner call
        -> surfaced methodological concerns
```

A third `ORACLE_HORIZON` condition is retained only as a diagnostic upper bound for failure attribution.

No provider-based navigation call is selected for the first experiment.

## Resolved benchmark shape

The first diagnostic should use:

```text
28 benchmark methodological KnowledgeAssets
4 heterogeneous ProjectStateEpisodes
3 scored snapshots per episode
3 repetitions per condition/snapshot
3 conditions
108 planned reasoner outputs
```

The episode families are:

```text
E1 future binary prediction
E2 static tabular prediction without temporal deployment
E3 probability-sensitive decision problem
E4 data-quality and measurement shift
```

This is intentionally broader and more state-driven than the ten-asset microstate fixtures used by Specifications 013-021.

## Oracle / treatment separation

The design now requires three distinct frozen artifacts:

```text
methodological_universe_v1
coverage_oracle_v1
oracle_representation_map_v1
```

The treatment universe is what ADS may navigate.

The hidden oracle defines evaluator truth without treatment stable keys.

The evaluator-only representation map is applied only after reasoning for scoring and failure attribution.

Neither evaluator artifact may enter retrieval, Horizon construction, prompts, or reasoner inputs.

## Intentional catalog gaps

Exactly two evaluator-expected concerns should be deliberately absent from the treatment universe.

This permits direct separation of:

```text
METHODOLOGICAL UNIVERSE GAP
NAVIGATION GAP
REASONING / USE GAP
```

Catalog-gap misses do not count as navigation failures. Open-world recovery remains measurable in every condition.

## Common-state fairness

All conditions must receive the same canonical Foundation-018-aligned project-state payload.

The common state must not contain:

```text
oracle IDs
stable-key hints
requested reasoning functions
candidate methodological concern menus
candidate action menus
expected dispositions
hidden evaluator rationales
```

`ADS_HORIZON` may derive retrieval text only through a deterministic generic object-type-aware projection of that same state.

Case-specific methodological keywords are forbidden from the projector.

## Matched compute decision

The first treatment selects:

```text
non-provider navigation
+ one reasoner call
```

for `ADS_HORIZON`.

`GENERIC`, `ADS_HORIZON`, and `ORACLE_HORIZON` therefore receive the same reasoner-call opportunity.

This avoids confounding explicit system-side navigation with extra LLM inference compute.

## Reasoner output boundary

The reasoner should discover concerns without a supplied candidate menu.

The bounded structured result should permit no more than twelve concern records, each representing either:

```text
CURRENT
MISSING_CONTEXT
```

with explicit grounding to supplied project-object identities and a concrete missing-context question when applicable.

The model must remain free to surface an important concern that is not represented in its supplied Horizon.

## Evaluation design

Matching should use:

```text
deterministic normalization / aliases
    -> blinded semantic adjudication for unmatched concerns
```

The judge must not receive condition identity, retrieval traces, Horizon source, methodological payload, or advancement thresholds.

The primary metric families are:

```text
critical-path recall
weighted represented-concern recall
per-episode minimum recall
critical omission counts
repeated / catastrophic omission reliability
newly activated path recall
surface latency
missing-context recognition and question correctness
false activation / persistence / unsupported expansion
noise ratio
```

Separate attribution metrics preserve:

```text
Horizon recall
navigation gaps
reasoning/use gaps
catalog-gap recovery
```

## Critical reliability rule

`CRITICAL_VALIDITY` concerns receive the strictest treatment.

Specification 022 should require:

```text
zero catastrophic represented-critical omissions
```

where catastrophic means an active represented critical concern is missed in all three repetitions at a scored snapshot.

This is stricter than mean-only scoring without requiring perfect stochastic recall in every individual repetition.

Exact aggregate/per-episode floors remain to be frozen prospectively in Specification 022.

## Expansion guardrail

The benchmark must include deliberate non-activation states.

In particular, E2 should ensure that a date-like field does not automatically justify temporal validation when deployment is explicitly non-temporal.

The eventual frozen contract must include both absolute ADS noise limits and relative non-expansion versus GENERIC.

## Outcome taxonomy selected for Specification 022 design

```text
PROMOTE_STATE_DRIVEN_NAVIGATION_SEAM
    all frozen absolute + expansion gates pass
    and at least one prospectively frozen positive value signal exists

SAFE_BUT_NOT_DIFFERENTIATED
    all frozen absolute + expansion gates pass
    but zero positive value signals exist

FAIL
    complete integrity-valid experiment fails a frozen required gate

INCOMPLETE / INTEGRITY FAILED
    preserve evidence without scientific advancement classification
```

`SAFE_BUT_NOT_DIFFERENTIATED` is deliberately legitimate. The benchmark must not be rewritten merely because GENERIC performs strongly.

## Historical integrity

Nothing in Research 032 or this checkpoint changes:

```text
Specification 015   FAIL
Specification 016   DISPOSITION_BOUNDARY_SUPPORTED
Specification 017   INCOMPLETE
Specification 019   FAIL
Specification 020   BLOCKING_BOUNDARY_SUPPORTED
Specification 021   FAIL
```

Specification 021 remains the valid bounded answer to its supplied-action disposition question.

Question A remains a different upstream capability.

## Deliberate non-selections

Checkpoint 187 does not yet freeze:

```text
Specification 022
exact 28 asset payloads/stable keys
exact project-state objects and transitions
exact hidden oracle items
exact two catalog-gap concepts
exact evaluator representation mapping
retrieval top-k / Horizon size
model/provider/reasoning settings
token/retry budgets
semantic-judge settings
absolute metric thresholds
positive-signal thresholds
gate identifiers
random seed / request ordering
```

No provider call is authorized.

## Exact continuation

```text
1. reconcile README / CURRENT_STATE / KNOWLEDGE_MAP / current_routing to Checkpoint 187 and PR #68
2. validate the exact reconciled design head
3. prospectively author and freeze the exact Specification 022 treatment universe, project-state episodes, hidden oracle, representation map, runtime treatment, metrics, thresholds, seeds, and advancement gates
4. add provider-free contract/integrity tests before any provider-backed execution
5. do not implement or run Specification 022 before its scientific contract is frozen
6. do not modify or rescore Specifications 015-021
7. any eventual provider-backed execution must use the governed Specification 018 launcher and a separately authorized frozen live source
```
