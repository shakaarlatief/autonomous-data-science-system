# Research 032: Project-State-to-Methodological-Horizon Coverage Diagnostic Design

**Date:** 2026-08-24  
**Status:** Successor experiment design choices resolved; Specification 022 not frozen  
**Authority:** Research/design only. This document resolves the principal design questions left open by Research 031. It does not freeze Specification 022, authorize implementation, authorize provider execution, modify accepted foundations, promote benchmark knowledge into methodological authority, or rescore Specifications 015-021.  
**Design session:** 05  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 05 - Selective Context Promotion & Reasoning Vertical Slice

## 1. Starting boundary

Research 031 and Checkpoint 186 established that the next architecture-representative evaluation should move upstream from supplied-action disposition calibration and begin from evolving project state.

The architecture-review PR was validated at exact head:

```text
934db7d0ce4e95ddde774f94da5bf3361defd03f
```

with successful current-routing, checkpoint-metadata, reasoning-context, disposition-semantics, blocking-calibration, and autonomous-launcher checks.

PR #67 was then merged unchanged into `v1-frontend-spike` at:

```text
0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e
```

The successor design branch is:

```text
v1-methodological-navigation-coverage-diagnostic
```

Specification 021 remains immutable `FAIL` evidence. No result from Specifications 015-021 is modified or rescored by this design.

---

## 2. Scientific seam to isolate

The next experiment should answer a narrower version of Question A:

> Given evolving authoritative project state with no methodological answer menu, can the ADS navigation path surface and account for materially important methodological concerns more reliably than a strong generic reasoner, without unacceptable irrelevant expansion?

The primary tested layers are:

```text
A. PATH DISCOVERY / COVERAGE
B. APPLICABILITY / MISSING CONTEXT
```

The experiment should instrument but not advancement-gate:

```text
C. concrete option generation
D. prioritization / disposition
E. downstream model-facing context value beyond the supplied Horizon
```

This prevents another experiment from silently collapsing several architecture seams into one final prose or recommendation score.

---

## 3. Resolution 1: common ProjectStateProjection

Both practical conditions must begin from the same canonical project-state projection.

The projection is a Foundation-018-aligned, storage-neutral snapshot containing only project facts and history that a real ADS project could legitimately know at that point.

The first design should include selected instances of:

```text
Objective
Constraint
Deliverable
Definition
Dataset
Variable
Question
Assumption
Finding
Claim
Decision
Artifact reference
Relation
Event / state-transition summary
```

The projection must preserve:

```text
episode_id
snapshot_id
project objective / intended use
data and variable facts
current findings and claims
current unresolved questions
accepted decisions and constraints
relevant recent state-transition facts
```

It must not contain:

```text
oracle IDs
oracle importance classes
methodological stable keys
requested reasoning-function labels
candidate methodological concern menus
candidate action menus
expected dispositions
condition labels
hidden evaluator rationales
```

For every matched observation, the common visible project-state payload must be byte-equivalent after canonical serialization across `GENERIC`, `ADS_HORIZON`, and `ORACLE_HORIZON`, except for condition-neutral request nonces when operationally necessary.

### 3.1 ADS retrieval projection

`ADS_HORIZON` may derive retrieval inputs from the common project state, but that transformation must be deterministic and generic.

The first design therefore selects:

```text
canonical ProjectStateProjection
    -> deterministic object-type-aware textual projection
    -> accepted retrieval seam
```

The deterministic projector may expose fields such as object type, title, description, known facts, and relation summaries.

It must not contain case-specific methodological keywords, oracle concept names, manually supplied stable keys, or hidden reasoning-function labels.

No provider call is allowed for state-to-query generation in Specification 022.

---

## 4. Resolution 2: controlled methodological universe

The first diagnostic should use a deliberately bounded benchmark universe of exactly:

```text
28 methodological KnowledgeAssets
```

This is large enough to create meaningful cross-neighborhood navigation and distractors while remaining manually auditable.

The 28 assets should cover approximately fourteen methodological neighborhoods, including:

```text
problem / target definition
unit of observation and dataset structure
prediction moment and feature availability
data leakage
validation design
repeated-entity generalization
preprocessing isolation
missingness and production-data alignment
class prevalence and metric choice
model-family comparison / baselines
probability calibration
threshold / cost-sensitive decision rules
final-test protection
shift / measurement / subgroup robustness
```

Existing accepted fixture assets may be reused when they fit exactly. New benchmark-only assets may be added where necessary.

The controlled universe is an experiment fixture, not automatic reusable methodological authority.

Governance must distinguish:

```text
BENCHMARK_FIXTURE
    valid treatment/evaluation material
    not automatically accepted methodological knowledge

ACCEPTED methodological authority
    governed separately through the existing knowledge lifecycle
```

The benchmark universe must be frozen before any live provider execution and must not be strengthened after observing model failures.

---

## 5. Resolution 3: evaluator oracle is separate from treatment knowledge

Research 031 identified a leakage risk if the treatment catalog and expected answer are authored as one object.

The successor design therefore selects three separate artifacts:

```text
1. methodological_universe_v1
       treatment knowledge available to ADS

2. coverage_oracle_v1
       evaluator-only methodological truth by episode/snapshot
       contains no treatment stable keys

3. oracle_representation_map_v1
       evaluator-only mapping from oracle concerns
       to zero or more treatment stable keys
```

The runtime must never load `coverage_oracle_v1` or `oracle_representation_map_v1` into retrieval, Horizon construction, prompts, or reasoner inputs.

The representation map is used only after navigation/reasoning for scoring and failure attribution.

This permits all three important states:

```text
represented and expected
represented but not currently expected
expected but intentionally unrepresented
```

The third category is required for catalog-gap evaluation.

All three artifacts must be frozen prospectively before provider execution.

---

## 6. Resolution 4: three-condition design

Exactly three conceptual conditions should be used.

### GENERIC

Receives:

```text
same canonical project state
same common methodological-discovery instruction
same structured output contract
same model
same reasoning effort
same output budget
one reasoner call
no reusable methodological payload
```

The strong model is free to use normal parametric methodological knowledge.

### ADS_HORIZON

Receives:

```text
same canonical project state
same common methodological-discovery instruction
same structured output contract
same model
same reasoning effort
same output budget
one reasoner call

plus

system-selected explained MethodologicalHorizon
constructed from the controlled universe through accepted navigation primitives
```

The pre-reasoner ADS navigation path is:

```text
canonical project state
    -> deterministic generic retrieval projection
    -> accepted hybrid retrieval
    -> accepted-current one-hop relation expansion
    -> deterministic applicability / missing-context evaluation
    -> explained bounded MethodologicalHorizon
```

No LLM navigation call is allowed before the reasoner.

### ORACLE_HORIZON

This is a diagnostic upper-bound condition, not a candidate production architecture.

It receives:

```text
same canonical project state
same common methodological-discovery instruction
same structured output contract
same model
same reasoning effort
same output budget
one reasoner call

plus

only the exact treatment-universe knowledge revisions
that the evaluator-only representation map marks as relevant
for the current snapshot
```

It does not receive:

```text
oracle IDs
importance classes
evaluator rationale
expected wording
expected outputs
unrepresented catalog-gap concerns
```

Interpretation:

```text
ADS_HORIZON misses, ORACLE_HORIZON succeeds
    -> navigation is a likely bottleneck

ADS_HORIZON contains the concern and downstream output still misses it
    -> reasoning/use is a likely bottleneck

both practical and oracle Horizon conditions miss an unrepresented concern
    -> not a navigation failure; inspect catalog-gap recovery separately
```

---

## 7. Resolution 5: evolving benchmark shape

Use exactly four heterogeneous `ProjectStateEpisode` families with three scored snapshots each.

Total scored project states:

```text
4 episodes x 3 snapshots = 12 project-state snapshots
```

### Episode E1: future binary prediction

Primary activation neighborhoods:

```text
prediction moment
prediction-time feature availability
temporal validation
repeated-entity generalization
class prevalence / metric implications
```

The episode should contain at least one transition where a previously plausible design becomes invalid after new deployment or feature-timing evidence appears.

### Episode E2: static tabular prediction without temporal deployment

Primary purpose:

```text
false-activation control
ordinary leakage / validation reasoning
preprocessing isolation
final-test protection
```

A date-like field may exist, but project facts must establish that prediction is not future temporal deployment merely because a date field is present.

### Episode E3: probability-sensitive decision problem

Primary activation neighborhoods:

```text
probability calibration
proper probability evaluation
threshold selection
asymmetric cost / decision utility
held-out selection boundaries
```

The episode should distinguish ranking quality from calibrated probability use and from final decision-threshold selection.

### Episode E4: data-quality and measurement shift

Primary activation neighborhoods:

```text
missingness characterization
production missingness alignment
distribution / measurement shift
subgroup robustness
revalidation
```

The episode should include a state transition where a new collection or measurement regime changes what must be re-examined.

Exact episode facts, object identities, transitions, and oracle items belong in Specification 022 and its frozen fixtures.

---

## 8. Resolution 6: intentional catalog gaps

The first diagnostic should include exactly two evaluator-expected concerns that are deliberately absent from the 28-asset treatment universe.

Purpose:

```text
verify that an explicit catalog is not treated as a closed world
separate knowledge-universe gaps from navigation gaps
measure open-world recovery by the strong reasoner
```

For an intentional catalog-gap oracle item:

```text
representable_by_stable_keys = []
```

Scoring must classify outcomes separately:

```text
CATALOG_GAP_RECOVERED
    reasoner surfaces the concern despite no treatment representation

CATALOG_GAP_MISSED
    concern is not surfaced
```

Catalog-gap misses do not count as ADS navigation failures.

They remain important total-coverage evidence and possible future candidate-knowledge signals.

---

## 9. Resolution 7: reasoner output contract

The reasoner should not choose from a supplied candidate menu.

It should produce at most twelve structured concern records per observation.

Conceptual shape:

```text
MethodologicalCoverageResult
    summary
    concerns[]
        local_concern_id
        title
        explanation
        state
            CURRENT
            MISSING_CONTEXT
        grounding_project_object_ids[]
        missing_context_question | null
    warnings[]
```

Rules:

```text
1 <= number of concerns <= 12
local_concern_id is output-local, not an evaluator ID
no oracle IDs or stable-key selection is requested from the model
CURRENT means materially relevant now from known state
MISSING_CONTEXT means the concern cannot be resolved because a specific needed project fact is absent
MISSING_CONTEXT requires a concrete clarification question
project grounding IDs must reference supplied project objects
```

The model may surface a concern not represented in the supplied Horizon.

That open-world escape hatch is required in every condition.

Layer-C project actions may appear in free-text explanation only as descriptive evidence. They are not scored as the primary experiment output.

---

## 10. Resolution 8: hidden oracle semantics

Each evaluator oracle item should contain conceptually:

```text
oracle_id
canonical_concern
importance_class
acceptable_aliases[]
first_valid_snapshot
last_valid_snapshot or resolution rule
expected_navigation_state by scored snapshot
missing_context_question_semantics when applicable
rationale
grounding_project_object_ids[]
```

Importance classes are fixed as:

```text
CRITICAL_VALIDITY
HIGH_VALUE
USEFUL
OPTIONAL
```

Navigation-state expectations are evaluated separately from importance.

The evaluator should distinguish at least:

```text
ACTIVE / should be surfaced now
MISSING_CONTEXT / should remain visible as unresolved
INACTIVE / should not be surfaced now
RESOLVED / should no longer persist as a current concern
```

These oracle labels are evaluator-only and are never placed in model inputs.

---

## 11. Resolution 9: semantic matching

Exact wording is not a valid requirement for open-ended methodological discovery.

Matching therefore uses a two-stage evaluator:

```text
Stage 1
    deterministic normalization and exact/alias matching

Stage 2
    blinded semantic adjudication for unmatched items
```

The blinded semantic judge receives only:

```text
canonical project state
reasoner-produced concern records
oracle concern descriptions and allowed semantic variants needed for scoring
```

The judge must not receive:

```text
condition name
condition ordering
retrieval trace
Horizon source
methodological payload
provider usage differences
advancement thresholds
```

The judge's role is limited to semantic coverage and state/clarification equivalence. It must not reward preferred prose style.

All matches must remain project-fact grounded.

---

## 12. Resolution 10: metric decomposition

The experiment should preserve separate measurements for the system navigation layer and the final surfaced output.

### 12.1 Universe and navigation attribution

For represented active oracle concerns:

```text
horizon_recall
    expected represented concerns entering ADS_HORIZON

navigation_gap_count
    expected represented concerns absent from ADS_HORIZON

reasoning_use_gap_count
    expected represented concerns present in ADS_HORIZON
    but absent from final reasoner output
```

`GENERIC` has no Horizon and therefore has no `horizon_recall` metric.

### 12.2 Output coverage

Primary output metrics:

```text
critical-path recall
weighted represented-concern recall
per-episode represented recall
critical omission count
catastrophic critical omission count
repeated omission count
newly activated concern recall
surface latency in snapshots
missing-context recognition
missing-context question correctness
```

The default importance weights for weighted recall are:

```text
CRITICAL_VALIDITY = 4
HIGH_VALUE        = 2
USEFUL            = 1
OPTIONAL          = 0
```

`OPTIONAL` items remain useful for descriptive coverage/noise analysis but do not improve the main weighted recall score.

### 12.3 Catalog gaps

Report separately:

```text
catalog-gap recovery count
catalog-gap miss count
catalog-gap recovery rate
```

Do not mix catalog gaps into `horizon_recall` or `navigation_gap_count`.

### 12.4 Expansion/noise

Penalize:

```text
false activation count
inactive-concern activation count
resolved-concern persistence count
unmatched / unsupported concern count
duplicate or near-duplicate concern count
noise ratio
output concern count
Horizon size
```

Coverage without expansion control is not success.

---

## 13. Resolution 11: reliability structure and repetitions

Use exactly three repetitions per condition, episode, and snapshot.

Planned reasoner outputs:

```text
3 conditions
x 4 episodes
x 3 snapshots
x 3 repetitions
= 108 reasoner outputs
```

Semantic adjudication may require up to one blinded judge call per reasoner output after deterministic matching.

This scale is intentionally larger than the recent microstate recommendation experiments because the tested value proposition is reliability across heterogeneous evolving states.

Three repetitions permit measurement of:

```text
single-run omissions
majority omissions
concerns missed in all repetitions
between-repetition coverage variance
```

The exact model/provider settings, retry ceiling, output-token budgets, and total attempt ceiling must be prospectively frozen in Specification 022 before any live execution.

---

## 14. Resolution 12: strict critical-omission interpretation

`CRITICAL_VALIDITY` concerns receive the strongest reliability treatment.

The first diagnostic should distinguish:

```text
ordinary critical omission
    a critical concern missing from one repetition

majority critical omission
    a critical concern missing from at least two of three repetitions

catastrophic critical omission
    an active represented critical concern missing from all three repetitions
```

The Specification 022 advancement contract should use zero catastrophic represented-critical omissions as an absolute requirement for `ADS_HORIZON`.

This is intentionally stricter than an average semantic-quality metric but less brittle than demanding perfect critical recall in every single stochastic repetition.

Exact aggregate and per-episode recall floors remain to be frozen in Specification 022.

---

## 15. Expansion control design

The experiment should include deliberate non-activation states so that a high-recall strategy cannot pass by listing everything.

At least one episode must contain a tempting near-neighbor concern that should remain inactive. E2's date-like field without temporal deployment is the canonical example.

The Specification 022 gate should include both:

```text
absolute ADS_HORIZON noise/false-activation limits
relative non-expansion versus GENERIC
```

`ORACLE_HORIZON` is diagnostic and should not define the practical expansion baseline.

The hard twelve-concern output cap is part of the bounded experimental contract, not a proposed final product limit.

---

## 16. Missing-context semantics

Research 031 preserves the important rule:

```text
UNKNOWN != FALSE
```

The first diagnostic should therefore include snapshots where a methodological concern is materially important but cannot yet be resolved because a specific project fact is unknown.

Expected behavior:

```text
retain the concern
mark it MISSING_CONTEXT
ask the concrete question needed to resolve it
```

Incorrect behaviors include:

```text
silently dropping the concern
asserting it is inapplicable without evidence
inventing the missing project fact
asking a generic question unrelated to the actual missing prerequisite
```

The deterministic Horizon applicability state and the final model-surfaced missing-context behavior should both be preserved so navigation and reasoning failures remain attributable.

---

## 17. Time-to-surface semantics

Each active oracle concern has a first valid snapshot.

For every condition/repetition:

```text
surface_latency
    = first snapshot where the concern is surfaced
      - first snapshot where the concern is validly active
```

Interpretation:

```text
0     surfaced immediately when evidence made it current
1+    delayed activation
null  never surfaced during the episode after activation
```

Premature surfacing before the first valid snapshot is a false activation, not negative latency.

Resolved concerns persisting after their valid interval are persistence errors.

---

## 18. Provider-compute fairness

The first diagnostic selects the lower-complexity treatment:

```text
non-provider ADS navigation
    + one strong reasoner call
```

rather than:

```text
LLM navigation call
    + LLM reasoner call
```

This keeps the provider-call opportunity matched across practical conditions and avoids attributing extra inference compute to explicit system architecture.

If a future experiment adds an LLM navigation stage, it must separately address compute-matched controls.

---

## 19. Advancement-gating versus descriptive evidence

Specification 022 should gate only the seam it is designed to test.

### Advancement-gating

```text
execution integrity
represented critical-path reliability
weighted represented coverage
per-episode minimum coverage
missing-context behavior
newly activated path coverage
expansion/noise control
relative practical-condition comparison
```

### Diagnostic / attribution

```text
ADS Horizon recall
navigation gap count
reasoning/use gap count
ORACLE_HORIZON performance
catalog-gap recovery
surface-latency decomposition
```

Some of these diagnostic metrics may participate in positive-value signals, but they should not convert a failed absolute safety/coverage gate into a pass.

### Descriptive only for this experiment

```text
generated concrete project actions
recommendation / disposition labels
prose style
final production ranking behavior
```

---

## 20. Outcome taxonomy

The successor specification should preserve a non-binary result taxonomy.

### PROMOTE_STATE_DRIVEN_NAVIGATION_SEAM

Use only if:

```text
all frozen absolute ADS_HORIZON gates pass
all frozen expansion/non-inferiority gates pass
at least one prospectively defined positive system-value signal versus GENERIC is present
```

This would support only the tested state-to-Horizon navigation seam.

It would not establish the full ADS architecture.

### SAFE_BUT_NOT_DIFFERENTIATED

Use if:

```text
all frozen absolute ADS_HORIZON gates pass
all frozen expansion/non-inferiority gates pass
no prospectively defined positive system-value signal is present
```

This is a legitimate scientific outcome and must not trigger benchmark rewriting merely to force an ADS win.

### FAIL

Use if a complete, integrity-valid experiment fails any frozen absolute or required non-expansion gate.

### INCOMPLETE / INTEGRITY FAILED

If planned evidence is missing or execution integrity fails, preserve the run without assigning a scientific advancement classification.

---

## 21. Prospectively allowed positive-value signals

Specification 022 should freeze exact thresholds before implementation, but positive signals should come only from architecture-representative directions such as:

```text
material reduction in represented critical omissions versus GENERIC
material reduction in repeated/catastrophic omissions
material improvement in weighted represented recall
material improvement in missing-context recognition
material reduction in surface latency after state transitions
```

A positive signal must not be defined from:

```text
better prose style
more concerns listed without regard to relevance
ORACLE_HORIZON outperforming GENERIC
post-hoc selection of whichever metric happened to improve
```

---

## 22. Provider and semantic-judge neutrality

The next specification may reuse the accepted ADS-owned `ReasoningRuntime` and the recent fixed model family for continuity, but this document does not freeze the exact provider/model configuration.

The semantic judge must remain blinded to condition.

No provider call is authorized by this design document.

The governed autonomous live-experiment launcher remains mandatory for any eventual authorized live execution.

---

## 23. What is deliberately not selected yet

Research 032 resolves the architecture/evaluation choices needed to make Specification 022 concrete, but it deliberately does not yet freeze:

```text
exact 28 asset contents and stable keys
exact episode object payloads
exact oracle items and aliases
exact two catalog-gap concerns
exact representation map
exact retrieval top-k and Horizon size
exact model/provider/reasoning-effort settings
exact token budgets and retry ceilings
exact semantic-judge model settings
exact absolute metric thresholds
exact positive-value-signal thresholds
exact advancement gate IDs
exact random seed / request ordering
```

Those are Specification 022 contract details.

They must be fixed before implementation or live provider execution.

---

## 24. Design conclusion

The successor experiment should no longer ask a strong model to classify a methodological decision space that the benchmark has already supplied.

It should test the missing upstream seam:

```text
EVOLVING PROJECT STATE
        ->
DETERMINISTIC SYSTEM-SIDE NAVIGATION
        ->
EXPLAINED METHODOLOGICAL HORIZON
        ->
ONE STRONG REASONER CALL
        ->
SURFACED METHODOLOGICAL CONCERNS
```

against:

```text
EVOLVING PROJECT STATE
        ->
ONE STRONG GENERIC REASONER CALL
        ->
SURFACED METHODOLOGICAL CONCERNS
```

with `ORACLE_HORIZON` retained only as a diagnostic upper bound.

The experiment should explicitly tell us whether a failure comes from:

```text
the methodological universe
the navigation path
the downstream reasoner
```

rather than hiding those failures inside one recommendation score.

Specification 022 remains **not frozen** at the end of Research 032.
