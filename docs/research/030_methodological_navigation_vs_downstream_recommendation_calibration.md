# Research 030: Methodological Navigation versus Downstream Recommendation Calibration

**Date:** 2026-08-24  
**Status:** Architectural clarification after Specification 021  
**Authority:** Research and interpretation guidance only. This memo does not rescore Specification 021, change its frozen `FAIL`, or modify accepted foundations/specifications. It clarifies what the recent GENERIC / SELECTIVE experiments do and do not say about the long-term ADS architecture.  
**Design session:** 05  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 05 - Selective Context Promotion & Reasoning Vertical Slice

## Purpose

Specification 021 produced a complete frozen `FAIL`, but subsequent design review exposed a risk of interpreting that bounded result too broadly.

The core ADS vision remains the one preserved in Foundations 006, 017, 019, 020 and Research 028:

```text
strong LLM reasoning
    + system-owned structured project state
    + broad explicit reusable methodological knowledge
    + methodological navigation
    + selective context construction
    + execution / evidence / state update
```

The system is intended to reduce the burden currently carried by a human who must repeatedly remember analytical paths, ask the LLM about them, notice omissions, track what has already happened, and bring forgotten considerations back into the conversation.

The key interpretation boundary is therefore:

```text
methodological navigation / coverage
    !=
downstream disposition calibration over an already supplied action set
```

## 1. Two different research questions

### Question A: methodological navigation and coverage

Given an evolving project state:

```text
what methodological areas might matter?
what expert questions should be raised?
what methods / models / diagnostics / risks / assumptions / alternatives exist?
which are applicable?
which are relevant?
which concrete actions should enter consideration?
what has already been resolved or superseded?
what newly becomes relevant when project state changes?
```

This is close to the central product value proposition of ADS.

A mature test of Question A must not hand both conditions the important methodological option set in advance. It must evaluate whether the system itself can surface and account for the relevant methodological pathways without depending on the human to remember them.

### Question B: downstream recommendation/disposition calibration

Given a project microstate in which the important decision space is already concretely supplied:

```text
candidate actions
requirements
active downstream scopes
dependencies
resolver relations
defer triggers
sequencing relations
```

can the reasoner correctly classify every action as:

```text
BLOCKING_REQUIRED
RECOMMENDED
DEFER
NOT_NOW
```

and explain the decision correctly?

Specifications 015, 019, and 021 primarily test this downstream question.

## 2. Why Specification 021 is not a full test of methodological navigation

Specification 021 deliberately holds major upstream navigation problems fixed.

Every condition receives:

```text
same user task
same project evidence
same explicit requested reasoning function
same requirement menu
same downstream-scope menu
same scope DEPENDS_ON requirement relations
same candidate action menu
same action RESOLVES requirement relations
same defer-trigger menu
same action WAITS_FOR trigger relations
same structured output schema
```

The GENERIC condition differs from SELECTIVE mainly by receiving no reusable methodological asset payload.

Therefore GENERIC is not being asked to reconstruct the complete methodological option space from raw project state. The benchmark has already supplied much of the decision structure that a mature methodological-navigation brain would ultimately help discover or organize.

The valid bounded Specification 021 question is therefore closer to:

> Once the relevant decision space is already represented, does adding the selected exact-revision methodological payload improve disposition and rationale quality?

It does not answer:

> Does an explicit methodological universe and navigation brain help ADS remember, discover, organize, and surface the right analytical pathways in the first place?

## 3. Current SELECTIVE is only an early selector seam

The accepted Specification 013 selector receives an explicit `MethodologicalContextRequest` containing:

```text
task_id
requested_reasoning_functions
max_assets
```

It selects Horizon assets whose `reasoning_functions` intersect the requested functions, with bounded `REQUIRES_CONCEPT` support closure.

Still explicitly outside the accepted seam are:

```text
natural-language task -> reasoning-function inference
project-state -> reasoning-function inference
general semantic relevance judgment
open-world concern discovery
general recommendation/prioritization
final required/blocking policy
```

The current selector is therefore a first mechanical proof that a broad system-side Horizon can be projected into a small exact model-facing context pack once the reasoning need is already known. It is not the completed methodological-navigation brain.

## 4. Current knowledge corpus is a benchmark fixture, not the envisioned knowledge universe

The current repeated V1 corpus contains ten deliberately heterogeneous assets:

```text
bagging
class-imbalance
ecdf
gradient-boosted-trees
histogram
missing-data
prediction-moment
prediction-time-feature-eligibility
random-forest
temporal-validation
```

This fixture exists to stress representation, retrieval, Horizon, selective-context, and downstream reasoning seams. It is not representative coverage of the long-term methodological universe.

The intended universe remains much broader, including methods, question templates, decision frameworks, invariants, failure modes, investigation patterns, interpretation knowledge, follow-up/dependency knowledge, and cross-cutting professional methodology across the data-science lifecycle.

## 5. Correct interpretation of existing SELECTIVE evidence

### Specification 014

Provides positive bounded evidence that SELECTIVE can preserve measured reasoning quality relative to FULL_HORIZON while reducing provider input-token burden substantially.

This supports the architecture:

```text
what the SYSTEM knows
    !=
what the LLM receives on every reasoning call
```

### Specifications 015 / 019 / 021

Provide bounded evidence about downstream recommendation/disposition behavior after much of the relevant action space and task structure are already supplied.

Their GENERIC controls are valuable because they prevent ordinary model capability from being misattributed to explicit methodological context.

However, they cannot establish that the methodological-navigation brain itself is unnecessary.

### Specification 021 specifically

The complete `FAIL` remains immutable.

It establishes that under the frozen supplied-action benchmark:

```text
all conditions achieved perfect deterministic disposition/pointer behavior
SELECTIVE did not show a prospectively frozen positive recommendation-value signal over GENERIC
one absolute SELECTIVE semantic case gate failed
```

The valid conclusion is narrow:

> Explicit selected methodological payload did not demonstrate downstream recommendation-quality advantage once the benchmark had already supplied the relevant decision structure.

Do not generalize this into a rejection or demotion of broad methodological navigation or coverage accounting.

## 6. Why familiar knowledge can still be valuable even when the LLM already knows it

The long-term knowledge universe is not justified only by storing facts unknown to the model.

A strong LLM may know many relevant methods and safeguards while failing to surface one critical consideration on a particular run.

ADS should eventually make omission states inspectable:

```text
unknown to system
known but not retrieved
retrieved but inapplicable
applicable but judged low relevance
relevant but not recommended
recommended but skipped
resolved
still open
blocking
```

Systematic coverage and process navigation can therefore add value even when the model already possesses the underlying conceptual knowledge parametrically.

Novel, recent, organization-specific, project-learned, and source-authoritative knowledge remain additional future value categories, not replacements for systematic methodological coverage.

## 7. Current implementation status of Question A

Some infrastructure exists:

```text
reusable knowledge representation                    EXISTS
lexical retrieval                                    EXISTS
bounded semantic/hybrid comparator evidence          EXISTS
one-hop relation expansion                           EXISTS
three-valued applicability / missing context         EXISTS
first explained MethodologicalHorizon                EXISTS
explicit reasoning-function -> context selection     EXISTS
```

Major parts remain unsolved or only bounded experiments:

```text
raw project state -> methodological needs            NOT SOLVED GENERALLY
project state -> requested reasoning functions       NOT SOLVED
broad semantic relevance                             NOT SOLVED
open-world methodological concern discovery          NOT SOLVED
broad option/action generation                       NOT SOLVED
coverage accounting across a real project            NOT SOLVED END-TO-END
general prioritization                               NOT SOLVED
dynamic re-navigation as state changes               NOT SOLVED END-TO-END
```

Question A is therefore partially scaffolded, not completed.

## 8. Evaluation implication

Future evaluation should distinguish at least:

```text
A. PATH DISCOVERY / COVERAGE
    Can ADS surface the important methodological considerations from project state?

B. APPLICABILITY / RELEVANCE
    Does it correctly include, exclude, defer, or request missing context?

C. CONCRETE OPTION GENERATION
    Does it construct a strong and sufficiently broad decision/action set?

D. PRIORITIZATION / DISPOSITION
    Given concrete options, does it correctly recommend, block, defer, or deprioritize them?

E. MODEL-FACING CONTEXT VALUE
    Given a known reasoning need, which exact knowledge should enter the model context and what value does that context add?
```

These should not be collapsed into one score or treated as interchangeable evidence.

A future architecture-representative test of Question A should compare a strong generic control with ADS on realistic heterogeneous and evolving project states while withholding the answer-space scaffolding that the recommendation experiments deliberately provide.

## 9. Architectural guardrail

Until stronger system-level evidence exists, do not infer from downstream GENERIC / SELECTIVE parity that ADS should default to unassisted generic recommendation generation.

The standing architectural hypothesis remains:

```text
SYSTEM-OWNED PROJECT STATE
        ↓
METHODOLOGICAL NAVIGATION / COVERAGE
        ↓
EXPLAINED PROJECT-SPECIFIC HORIZON
        ↓
SELECTIVE CONTEXT WHEN USEFUL
        ↓
STRONG LLM REASONING
        ↓
PROPOSALS / INVESTIGATIONS / ACTIONS
        ↓
EVIDENCE / STATE UPDATE
        ↓
RE-NAVIGATION
```

GENERIC remains an essential experimental control. It is not an architectural replacement for methodological navigation.

## 10. Next design consequence

After Specification 021 evidence is preserved correctly, do not immediately run another recommendation-disposition benchmark over the same ten assets.

First perform a deliberate architecture/evaluation review centered on the still largely untested system-level value proposition:

> Can ADS reduce the human burden of remembering and surfacing the important methodological pathways across a heterogeneous evolving data-science project?

Any successor experiment should be derived from that review rather than from a desire to make SELECTIVE beat GENERIC on the already-bounded supplied-action task.