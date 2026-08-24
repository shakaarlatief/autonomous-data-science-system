# Specification 022: V1 Project-State-to-Methodological-Horizon Coverage Diagnostic

**Version:** 0.1  
**Date:** 2026-08-24  
**Status:** Frozen bounded scientific contract before implementation or provider execution  
**Scope:** Prospectively test whether deterministic ADS methodological navigation from evolving project state improves reliable coverage of materially important represented methodological concerns relative to a strong generic reasoner, without unacceptable expansion, while separately exposing catalog gaps, navigation gaps, applicability/missing-context failures, and downstream reasoning/use failures.  
**Authority:** Governs Specification 022 implementation and evaluation until its result is preserved. It does not modify or rescore Specifications 015-021, promote benchmark knowledge into accepted methodological authority, select a final production navigation/ranking policy, authorize project mutation or execution, select a final provider/model, or authorize a live provider run.  
**Design session:** 05  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 05 - Selective Context Promotion & Reasoning Vertical Slice

## 1. Starting boundary

The experiment branch is:

```text
v1-methodological-navigation-coverage-diagnostic
```

It begins from promoted V1 integration merge:

```text
0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e
```

Research and design boundary:

```text
docs/research/030_methodological_navigation_vs_downstream_recommendation_calibration.md
docs/research/031_methodological_navigation_coverage_architecture_and_evaluation_review.md
docs/research/032_project_state_to_methodological_horizon_coverage_diagnostic_design.md
docs/checkpoints/187_project_state_methodological_coverage_design_choices_resolved.md
```

The exact reconciled Checkpoint 187 candidate head before Specification 022 fixture/specification authoring is:

```text
ad8a2c6acb4e7522fdf3c565f7ccb5d65a2a557e
```

It passed:

```text
Checkpoint metadata                       32762957742  success
Current routing consistency               32762957786  success
V1 autonomous live experiment launcher CI 32762957710  success
V1 disposition semantics diagnostic       32762957679  success
V1 reasoning context value                32762957681  success
V1 blocking calibration diagnostic        32762957707  success
```

Historical scientific evidence remains immutable:

```text
Specification 015   FAIL
Specification 016   DISPOSITION_BOUNDARY_SUPPORTED
Specification 017   INCOMPLETE
Specification 019   FAIL
Specification 020   BLOCKING_BOUNDARY_SUPPORTED
Specification 021   FAIL
```

## 2. Frozen scientific question

> Given the same evolving authoritative project state, the same strong reasoner, the same reasoning effort and output budget, and no supplied methodological answer menu, does a deterministic ADS navigation path through a controlled methodological universe improve reliable coverage of important represented methodological concerns relative to direct generic reasoning, without unacceptable irrelevant expansion?

This experiment primarily tests:

```text
A. path discovery / methodological coverage
B. applicability / missing context
```

It does not use downstream recommendation/disposition quality as its advancement target.

## 3. Frozen failure-attribution model

The experiment MUST preserve three distinct failure classes:

```text
METHODOLOGICAL_UNIVERSE_GAP
    an evaluator-expected concern has no representation in the frozen treatment universe

NAVIGATION_GAP
    an evaluator-expected represented concern is absent from the ADS MethodologicalHorizon

REASONING_USE_GAP
    a represented concern is present in the supplied Horizon but absent from the final reasoner output
```

A catalog gap MUST NOT be counted as a navigation gap.

## 4. Frozen contract artifacts

All scientific fixtures live under:

```text
tests/fixtures/methodological_navigation/
```

Exact files:

```text
spec022_methodological_universe_v1.json
spec022_project_state_episodes_v1.json
spec022_coverage_oracle_v1.json
spec022_oracle_representation_map_v1.json
spec022_contract_fixture_manifest_v1.json
```

Canonical JSON uses:

```python
json.dumps(
    value,
    sort_keys=True,
    separators=(",", ":"),
    ensure_ascii=False,
).encode("utf-8")
```

Frozen canonical SHA-256 values:

```text
coverage oracle
    e6774d8caed623d913a44a2bca1e6ed4861aa2e2b13a72f44f3df85f834b9eec

methodological universe
    2e907c0de7dc5bfb01fbf4fef61de18f96ff6000b4a034aded7fb17ff1ff231e

oracle representation map
    186b554abbb5814333dc9b80611f3524ae5580242708b7add65897bb51374e49

project-state episodes
    8650dac2f3332b29553cc8d076c40067361c51bdb489220f6e9101e11b09cc45
```

No fixture may be changed after provider outputs are observed. Any pre-execution correction requires a new frozen checkpoint and exact digest history.

## 5. Frozen treatment methodological universe

Exactly 28 benchmark KnowledgeAssets are frozen:

```text
target-definition
unit-of-observation
prediction-moment
prediction-time-feature-eligibility
data-leakage
temporal-leakage
train-validation-test-separation
temporal-validation
repeated-entity-generalization
group-aware-validation
preprocessing-fit-isolation
feature-selection-isolation
missing-data
production-missingness-alignment
class-imbalance
minority-sensitive-metrics
linear-logistic-baseline
nonlinear-model-comparison
probability-calibration
proper-scoring-rules
threshold-selection
asymmetric-error-costs
final-test-protection
selection-evaluation-separation
distribution-shift
measurement-regime-change
subgroup-robustness
revalidation-after-data-change
```

The full exact titles, purposes, retrieval profiles, applicability expressions, revision identities, relations, and provenance are frozen in `spec022_methodological_universe_v1.json`.

The bundle kind is `BENCHMARK_FIXTURE`. It MUST NOT silently create accepted reusable methodological authority outside the experiment.

## 6. Frozen intentional catalog gaps

Exactly two evaluator-expected concerns are deliberately absent from the 28-asset universe:

```text
E1-C09
    complete outcome-observation / label-maturity window

E3-C10
    capacity-constrained operational decision policy
```

Their representation-map entries contain:

```text
stable_keys = []
```

They are scored as open-world catalog-gap recovery, not as ADS navigation failures.

## 7. Frozen project-state benchmark

Exactly four evolving episodes and three scored snapshots per episode are frozen:

```text
E1  Future binary prediction
    E1-S0
    E1-S1
    E1-S2

E2  Static tabular prediction without temporal deployment
    E2-S0
    E2-S1
    E2-S2

E3  Probability-sensitive decision problem
    E3-S0
    E3-S1
    E3-S2

E4  Data-quality and measurement shift
    E4-S0
    E4-S1
    E4-S2
```

Total scored project states:

```text
12
```

Every condition receives the same canonical snapshot payload for a matched observation.

The project state contains only project facts, project objects, and state-transition information. It MUST NOT contain:

```text
oracle IDs
oracle importance labels
methodological stable-key hints
requested reasoning-function labels
candidate methodological concern menus
candidate action menus
expected dispositions
hidden evaluator rationales
condition labels
```

## 8. Frozen common project-state serialization

The reasoner receives the project snapshot as deterministic JSON with keys sorted recursively.

The ADS retrieval query is built from the same snapshot through the following generic deterministic text projection:

```text
EPISODE: <episode_id>
SNAPSHOT: <snapshot_id>
TRANSITION: <transition_summary>
FACT: <fact_key>=<canonical scalar value>
... facts ordered by fact_key ascending
OBJECT: <object_id> | <object_type> | <title> | <description>
OBJECT_FACT: <object_id> | <fact_key>=<canonical scalar value>
... objects ordered by object_id ascending; object facts by key ascending
RELATION: <relation_id> | <type> | <source_id> | <target_id>
... relations ordered by relation_id ascending
```

The projector MUST NOT add case-specific keywords, methodological names, stable keys, evaluator labels, synonyms, manual expansions, or provider-generated query text.

## 9. Frozen navigation treatment

`ADS_HORIZON` uses no provider call before the reasoner.

The pre-reasoner path is:

```text
canonical project state
    -> deterministic projection in Section 8
    -> lexical retrieval
    -> dense retrieval
    -> equal-weight RRF
    -> current accepted benchmark revisions
    -> one-hop outbound relation expansion
    -> Specification-012 applicability evaluation
    -> bounded explained MethodologicalHorizon
```

### 9.1 Retrieval channels

Reuse the accepted retrieval implementations and semantic passage projection.

Lexical channel:

```text
SqliteFtsKnowledgeRetrieval
retain top 6
```

Dense channel:

```text
fastembed==0.8.0
BAAI/bge-small-en-v1.5
384 dimensions
query_embed for queries
passage_embed for documents
CPUExecutionProvider
threads = 1
exact normalized cosine similarity
retain top 6
```

### 9.2 Fusion

Equal-weight Reciprocal Rank Fusion:

```text
RRF(d) = sum over channels c of 1 / (60 + rank_c(d))
```

Final direct seeds:

```text
top 8 unique assets
```

Tie break:

```text
1. descending RRF score
2. ascending stable_key
```

### 9.3 Relation expansion

Use accepted-current outbound relations only.

```text
one hop only
no recursive expansion
```

Deduplicate by exact stable key/current revision.

### 9.4 Applicability

Reuse Specification 012 exactly:

```text
TRUE / FALSE / UNKNOWN condition truth
POSSIBLY_APPLICABLE
INAPPLICABLE
MISSING_CONTEXT
UNKNOWN != FALSE
```

Known false excludes the candidate. Missing prerequisite knowledge keeps it visible as `MISSING_CONTEXT`.

### 9.5 Horizon bound

The final included `ADS_HORIZON` is capped at exactly:

```text
12 assets
```

Ordering:

```text
1. direct RRF seeds in fused rank order
2. relation-added candidates by source direct rank
3. relation_type ascending
4. stable_key ascending
```

Candidates excluded as `INAPPLICABLE` remain in the execution trace but do not consume the 12 included slots.

If more than 12 included candidates remain, truncate deterministically at 12 and record every omitted candidate and its pre-truncation position.

## 10. Frozen three conditions

Exactly three conditions are frozen.

### GENERIC

Receives:

```text
same common project state
same common discovery instruction
same structured output contract
same model/runtime treatment
one reasoner call
no reusable methodological payload
```

### ADS_HORIZON

Receives everything GENERIC receives plus the Section-9 MethodologicalHorizon.

The model-facing methodological projection contains for each supplied asset:

```text
title
purpose
applicability_state
missing_context_keys
```

The model is not asked to reproduce stable keys or authoritative provenance. Exact supplied identities and payload hashes remain system-owned trace metadata.

### ORACLE_HORIZON

Diagnostic upper bound only.

For the current snapshot, select every treatment-universe asset mapped to an oracle item whose evaluator state is:

```text
ACTIVE
MISSING_CONTEXT
```

Deduplicate exact stable keys and order ascending by stable key.

Do not supply:

```text
oracle IDs
importance classes
evaluator rationales
expected wording
expected state labels
catalog-gap concerns
```

Apply the same deterministic applicability evaluator and the same model-facing projection as ADS_HORIZON.

ORACLE_HORIZON is not a production competitor and does not define the practical expansion baseline.

## 11. Frozen reasoner instruction

All conditions use the same common instruction, except for the condition-specific methodology section described above:

> Review the current project state as a rigorous data-science methodologist. Surface the most important methodological concerns that currently deserve attention, including concerns that require missing information before they can be resolved. Do not assume a supplied list is exhaustive. Do not invent project facts. Focus on concerns that materially affect validity, evaluation, modelling choices, data quality, or defensibility now. Avoid repeating concerns that the project state shows are already resolved. Return at most twelve distinct concerns and ground each one in supplied project-object IDs.

No prompt may name the evaluator oracle, expected concerns, benchmark stable keys, or advancement gates.

## 12. Frozen structured reasoner result

Use an experiment-owned schema conceptually equivalent to:

```text
MethodologicalCoverageResult
    summary: string
    concerns: list[MethodologicalConcern]  # 1..12
        local_concern_id: string
        title: string
        explanation: string
        state: CURRENT | MISSING_CONTEXT
        grounding_project_object_ids: list[string]  # 1..6
        missing_context_question: string | null
    warnings: list[string]
```

Validation MUST enforce:

```text
1 <= concerns <= 12
local_concern_id unique inside the result
title and explanation non-empty
all grounding IDs exist in the supplied snapshot
CURRENT -> missing_context_question is null
MISSING_CONTEXT -> missing_context_question is non-empty
no unknown structured fields
duplicate local IDs invalid
unknown project-object IDs invalid
```

The reasoner may surface concerns absent from its supplied Horizon.

## 13. Frozen evaluator oracle semantics

The hidden oracle uses exactly these importance classes and weights:

```text
CRITICAL_VALIDITY = 4
HIGH_VALUE        = 2
USEFUL            = 1
OPTIONAL          = 0
```

Snapshot states:

```text
ACTIVE
MISSING_CONTEXT
INACTIVE
RESOLVED
```

Unspecified item/snapshot pairs default to `INACTIVE`.

The exact oracle item descriptions, aliases, state transitions, grounding IDs, clarification semantics, and rationales are frozen in `spec022_coverage_oracle_v1.json`.

The runtime treatment MUST NOT load the hidden oracle or representation map into retrieval, Horizon construction, or reasoner prompts.

## 14. Frozen semantic adjudication

Every reasoner output is scored by:

```text
Stage 1
    deterministic case-folded whitespace/punctuation normalization
    exact canonical-concern / acceptable-alias matching

Stage 2
    one blinded semantic judge call for remaining unmatched output/oracle items
```

The judge receives only:

```text
an anonymized observation ID
canonical project state
reasoner-produced concern records
oracle concern descriptions / aliases / expected evaluator states needed for scoring
```

The judge MUST NOT receive:

```text
condition identity
condition order
retrieval trace
Horizon source
methodological payload
representation map
provider usage differences
advancement thresholds
```

The judge returns only semantic matching, state equivalence, missing-context-question equivalence, and unsupported/duplicate determinations. It MUST NOT score prose style.

## 15. Frozen model/runtime treatment

Reuse the accepted ADS-owned `ReasoningRuntime` boundary.

Reasoner:

```text
OpenAI Agents SDK 0.19.4
model                   gpt-5.6-sol
reasoning effort        medium
verbosity               low
max output tokens       5000
tools                    none
```

Semantic judge:

```text
OpenAI Agents SDK 0.19.4
model                   gpt-5.6-sol
reasoning effort        high
verbosity               low
max output tokens       4000
tools                    none
```

No provider call is allowed for retrieval-query construction, applicability evaluation, relation expansion, or Horizon construction.

## 16. Frozen repetitions, ordering, retries, and attempt budget

Exactly:

```text
3 conditions
x 4 episodes
x 3 snapshots
x 3 repetitions
= 108 reasoner observations
```

Every observation receives one blinded semantic-judge evaluation after deterministic pre-matching:

```text
108 judge observations
```

Planned successful provider calls:

```text
216
```

Experiment randomization seed:

```text
2026082403
```

Build the 108 reasoner request descriptors in canonical order:

```text
episode_id
snapshot_id
repetition
condition
```

then shuffle the full request list using Python `random.Random(2026082403).shuffle`.

Judge requests may execute after their corresponding reasoner result is available and MUST use anonymized IDs unrelated to condition.

Retry policy:

```text
maximum one retry per reasoner or judge observation
retry only for transient provider failure or invalid structured output
no content-specific retry instruction
```

Global provider-attempt ceiling:

```text
270
```

If the complete scored design cannot be produced within that ceiling, classify execution as incomplete and do not assign a scientific advancement outcome.

## 17. Frozen metric definitions

### 17.1 Represented expected concern

An oracle item is represented when its representation-map stable-key list is non-empty.

An oracle item is expected current when its snapshot state is:

```text
ACTIVE
MISSING_CONTEXT
```

### 17.2 Output recall

For a condition and observation:

```text
represented_recall
    matched represented expected items
    / represented expected items

critical_recall
    matched represented CRITICAL_VALIDITY expected items
    / represented CRITICAL_VALIDITY expected items

weighted_represented_recall
    sum importance weights for matched represented expected items
    / sum importance weights for represented expected items
```

Aggregate metrics are micro-averaged over their underlying oracle obligations unless explicitly labelled per-episode.

### 17.3 Critical omission reliability

For one represented critical item at one snapshot across three repetitions:

```text
ordinary omission
    missed in at least one repetition

majority omission
    missed in at least two repetitions

catastrophic omission
    missed in all three repetitions
```

### 17.4 Newly activated recall

An item is newly activated at the first scored snapshot where its evaluator state changes from `INACTIVE` or `RESOLVED` to `ACTIVE` or `MISSING_CONTEXT`.

Score recall on that first newly active snapshot.

### 17.5 Missing-context behavior

For oracle items expected `MISSING_CONTEXT`:

```text
recognition correct
    matched concern has output state MISSING_CONTEXT

question correct
    blinded judge says the clarification question requests the missing prerequisite without inventing project facts
```

### 17.6 Expansion/noise

A reasoner concern record is noise if it is:

```text
matched to an oracle item that is INACTIVE
matched to an oracle item that is RESOLVED
matched to an explicit inactive-control concern
unmatched / unsupported by project state
an additional semantic duplicate after the first matching record
```

Count each record at most once as noise.

```text
noise_ratio = noise concern records / all concern records
```

`resolved_persistence_count` and `inactive_false_activation_count` are reported separately.

### 17.7 Horizon attribution

For ADS_HORIZON only:

```text
horizon_recall
    represented expected oracle items for which at least one mapped stable key is present in the included Horizon

navigation_gap_count
    represented expected oracle items with no mapped stable key in the included Horizon

reasoning_use_gap_count
    represented expected oracle items covered by the Horizon but absent from the final reasoner output
```

### 17.8 Catalog gaps

For the two intentional unrepresented oracle items:

```text
CATALOG_GAP_RECOVERED
CATALOG_GAP_MISSED
```

Report recovery count/rate by condition. Catalog gaps never enter Horizon recall or navigation-gap counts.

### 17.9 Surface latency

For each active oracle item and repetition:

```text
surface_latency
    first surfaced snapshot index
    - first active snapshot index
```

Premature surfacing is a false activation, not negative latency. Never-surfaced items have null latency and are reported separately.

## 18. Frozen absolute ADS_HORIZON gates

A complete integrity-valid experiment passes the absolute treatment boundary only if all gates pass.

```text
MN-G01  execution/instrumentation integrity
MN-G02  represented critical Horizon recall >= 0.90
        AND weighted represented Horizon recall >= 0.80
MN-G03  aggregate represented critical output recall >= 0.90
MN-G04  aggregate weighted represented output recall >= 0.85
MN-G05  every episode weighted represented output recall >= 0.75
MN-G06  newly activated represented-concern recall >= 0.80
MN-G07  missing-context recognition accuracy >= 0.85
        AND missing-context question correctness >= 0.80
MN-G08  catastrophic represented-critical omissions = 0
MN-G09  ADS_HORIZON noise ratio <= 0.30
MN-G10  resolved-concern persistence ratio <= 0.15
MN-G11  E2 temporal false-activation records <= 1
         across all 9 ADS_HORIZON E2 reasoner outputs
```

For MN-G10:

```text
resolved-concern persistence ratio
    resolved-item matches
    / all opportunities to persist a previously active represented item after resolution
```

## 19. Frozen practical non-inferiority / expansion gates

ADS_HORIZON must also satisfy:

```text
MN-G12  weighted represented output recall
         >= GENERIC weighted represented output recall - 0.03

MN-G13  represented critical output recall
         >= GENERIC represented critical output recall - 0.03

MN-G14  ADS_HORIZON noise ratio
         <= GENERIC noise ratio + 0.05

MN-G15  mean ADS_HORIZON output concern count
         <= mean GENERIC output concern count + 2.0
```

ORACLE_HORIZON does not define these practical gates.

## 20. Frozen positive system-value signals

Evaluate the following prospectively fixed signals versus GENERIC:

```text
MN-P01  ADS weighted represented recall
         >= GENERIC + 0.05

MN-P02  ADS represented critical recall
         >= GENERIC + 0.05

MN-P03  ADS total majority + catastrophic represented-critical omissions
         at least 2 lower than GENERIC

MN-P04  ADS newly activated represented-concern recall
         >= GENERIC + 0.10

MN-P05  mean of missing-context recognition accuracy
         and missing-context question correctness
         >= GENERIC corresponding mean + 0.10
```

Catalog-gap recovery, prose quality, output length, and ORACLE_HORIZON superiority are not positive system-value signals.

## 21. Frozen advancement outcome taxonomy

### PROMOTE_STATE_DRIVEN_NAVIGATION_SEAM

Assign only if:

```text
all MN-G01 through MN-G15 pass
AND
at least one MN-P01 through MN-P05 signal is true
```

Supported scope if achieved:

> On the frozen four-episode benchmark, deterministic project-state-driven ADS navigation through the controlled methodological universe improves at least one prospectively defined reliability/coverage dimension over a matched strong generic reasoner while satisfying absolute coverage and expansion controls.

It does not establish the full ADS architecture or a final production navigation policy.

### SAFE_BUT_NOT_DIFFERENTIATED

Assign if:

```text
all MN-G01 through MN-G15 pass
AND
zero MN-P01 through MN-P05 signals are true
```

This is a legitimate result and MUST NOT trigger post-hoc benchmark rewriting merely to force an ADS advantage.

### FAIL

Assign if:

```text
the design is complete and execution-integrity-valid
AND
any MN-G02 through MN-G15 gate fails
```

### INCOMPLETE / INTEGRITY FAILED

If MN-G01 cannot pass because required observations, exact treatment identities, fixture integrity, blinded evaluation, or execution provenance are missing/invalid, preserve evidence but assign no scientific advancement classification.

## 22. Frozen MN-G01 integrity requirements

MN-G01 requires all of:

```text
108 valid reasoner observations
108 valid blinded judge observations
exact 3 x 4 x 3 x 3 observation matrix
exact frozen fixture canonical SHA-256 values
same canonical project-state bytes across matched conditions
exact model/runtime treatment by role
no provider-based navigation call
no reasoner tools
no judge tools
no oracle or representation-map leakage into GENERIC or ADS_HORIZON prompts
no condition identity in judge input
ADS_HORIZON built only from frozen universe + deterministic projector + frozen retrieval/expansion/applicability path
ORACLE_HORIZON built only from the evaluator mapping rule in Section 10
all supplied methodology identities/payload hashes recorded system-side
all reasoner outputs schema-valid
all judge outputs schema-valid
provider attempts <= 270
all retry reasons preserved
all raw request/response/usage metadata preserved before interpretation
```

Any integrity violation makes advancement classification invalid rather than converting it into an ordinary FAIL.

## 23. Frozen descriptive and diagnostic outputs

Preserve but do not advancement-gate:

```text
ORACLE_HORIZON coverage metrics
catalog-gap recovery
navigation-gap and reasoning/use-gap decomposition
surface-latency distributions
between-repetition variance
retrieval channel ranks and RRF scores
Horizon size and truncation events
individual semantic-judge matches
generated concrete-action language inside explanations
provider token usage and latency
```

These may inform a later prospectively designed diagnostic but cannot rescore Specification 022.

## 24. Historical-integrity and anti-tuning rules

Specification 022 MUST NOT:

```text
modify or rescore Specifications 015-021
use their individual model outputs to tune Specification 022 truth
change the 28-asset universe after observing live failures
change project-state snapshots after observing live failures
change oracle truth, aliases, representation mapping, thresholds, positive signals, or seed after observing live failures
add case-specific retrieval keywords
add a provider navigation call without a new prospective experiment
weaken GENERIC instructions or compute
count intentional catalog gaps as navigation failures
convert OPTIONAL oracle items into weighted-recall credit
```

Any discovered contract defect before provider execution must be preserved and repaired prospectively with a new exact source boundary.

## 25. Implementation boundary after this freeze

After this specification and all contract fixtures are committed, the next work may implement only the machinery required to execute this frozen design.

Provider-free validation MUST cover at least:

```text
fixture schema / digest validation
28 exact unique assets
4 episodes / 12 exact snapshots
33 exact oracle items
exactly two empty representation mappings
no unknown representation stable keys
project-object grounding integrity
condition/input equality
project-state projector determinism
retrieval/Horizon determinism for a fixed database
no oracle leakage into treatment builders
output-schema validation
judge blinding
metric calculation
MN-G / MN-P outcome classification
retry/attempt accounting
raw-before-interpretation artifact structure
```

No provider call is authorized merely because implementation becomes green.

## 26. Live-execution governance

Any eventual provider-backed run requires, in order:

```text
1. provider-free implementation and integrity tests green
2. exact live-capable source SHA frozen
3. required exact-source CI green
4. separate one-shot authorization in the Specification-018 registry
5. owner-created launch request with exact confirmation
6. governed launcher validation and dispatch
7. raw artifact preservation before scientific interpretation
```

The launcher receives no provider secret.

## 27. Exact continuation

```text
1. preserve this Specification 022 contract and its exact fixture digests in a checkpoint
2. reconcile routing so Specification 022 is the latest frozen specification while the latest completed experiment remains Specification 021 FAIL
3. validate the exact frozen-contract branch head
4. only then implement provider-free Specification 022 machinery and contract/integrity tests
5. do not authorize provider execution at the contract-freeze boundary
6. do not modify or rescore Specifications 015-021
```
