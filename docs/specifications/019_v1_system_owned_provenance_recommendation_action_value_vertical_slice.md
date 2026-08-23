# Specification 019: V1 System-Owned Provenance Recommendation and Action Value Vertical Slice

**Version:** 0.1  
**Date:** 2026-08-23  
**Status:** Frozen bounded implementation/evaluation contract before Specification 019 implementation or live model calls  
**Scope:** Third recommendation/action-value experiment. It preserves Specification 017's relation-backed scientific benchmark and three-condition comparison while moving exact supplied-context provenance from model-authored output into a deterministic system-owned trace.  
**Authority:** Governs Specification 019 implementation and evaluation until its result is preserved. It does not modify or rescore Specifications 015-017, finalize production recommendation/disposition enums, define the complete Foundation 018 dependency schema, authorize project-state mutation or automatic execution, select a final provider/model, or select a multi-agent architecture.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice

## 1. Starting boundary

The experiment branch is:

```text
v1-recommendation-action-value-system-provenance
```

It was created from canonical integration head:

```text
ecf37585f576a3c4fd84a884dee4650b52ab1519
```

The accepted Specification 018 integration merge is:

```text
9fd2243c38a8f0f010396847f519e115d30b8f58
```

Specification 015 remains immutable `FAIL` evidence.

Specification 016 remains bounded positive evidence with outcome:

```text
DISPOSITION_BOUNDARY_SUPPORTED
```

Specification 017 remains immutable incomplete live evidence with no advancement classification. Its partial outputs and scores may not be used to tune this specification.

Specification 018 is an accepted bounded control-plane capability. It changes how an explicitly authorized frozen experiment can be launched, not the scientific treatment in this specification.

---

## 2. Frozen experiment question

> Given the same project microstate, explicit task profile, candidate action menu, relation-backed sequencing evidence, runtime/model treatment, and evaluation contract, does the accepted SELECTIVE methodological path improve downstream recommendation/action behavior relative to a strong GENERIC reasoner while remaining no more expansion-prone than a compact FULL_HORIZON control, when exact supplied-context provenance is owned by the system rather than requested from the model?

This is a new prospective experiment because Specification 017 did not complete the matched scored design required to answer its scientific question.

The scientific truth is intentionally inherited from Specification 017. The provenance instrumentation is the only substantive contract change.

---

## 3. Frozen machine-readable authority

The Specification 019 fixture is:

```text
tests/fixtures/reasoning/system_owned_provenance_recommendation_action_v1.json
```

It is an overlay on the immutable Specification 017 fixture:

```text
tests/fixtures/reasoning/relation_backed_recommendation_action_v1.json
Git blob SHA eac949c47a01878dcc47dcca1116493a02ba9805
```

The provider-free implementation MUST fail closed if the base fixture no longer has that exact Git blob identity.

The effective benchmark is the exact base fixture plus only the explicit overlay changes frozen in Specification 019.

No implementation may silently copy, relabel, reinterpret, or normalize Specification 017 truth differently.

---

## 4. Frozen inherited scientific content

The following are inherited without change from Specification 017:

```text
four cases RB-01 through RB-04
project evidence
user tasks
requested reasoning functions
candidate action menus
cost units
BLOCKING_REQUIRED / RECOMMENDED / DEFER / NOT_NOW semantics
expected dispositions
expected defer_until_id pointers
available and expected blocked scopes
available and expected clarifications
available defer-trigger menus
semantic judge obligations
GENERIC / SELECTIVE / FULL_HORIZON conditions
SELECTIVE exact stable-key sets
FULL_HORIZON ten-asset context construction
relative non-inferiority margins
expansion gates
positive value signals
reasoner treatment except new experiment nonce/order seed
judge treatment except new experiment order seed
provider attempt budget and retry classes
```

Specification 017 partial live outputs are explicitly excluded from the design basis for all inherited truth.

---

## 5. Conditions

Exactly three conditions are frozen.

### GENERIC

Receives:

```text
same system instruction
same user task
same project evidence
same explicit requested reasoning functions
same candidate action menu
same blocked-scope menu
same clarification menu
same defer-trigger menu
same recommendation result schema
no reusable methodological assets
```

System-owned reusable-knowledge provenance is deterministically empty.

### SELECTIVE

Receives the accepted Specification 013 exact-revision `MethodologicalContextPack` inherited from Specification 017.

Frozen exact selective stable-key sets:

```text
RB-01
    prediction-moment
    prediction-time-feature-eligibility
    temporal-validation

RB-02
    gradient-boosted-trees
    random-forest

RB-03
    histogram
    ecdf

RB-04
    class-imbalance
    missing-data
```

### FULL_HORIZON

Receives all ten exact current accepted revisions in the same explained Horizon using the same compact reasoning projection as Specification 017.

No retrieval or selector treatment is changed.

---

## 6. Frozen relation-backed disposition semantics

Each candidate action must appear exactly once and use exactly one disposition:

```text
BLOCKING_REQUIRED
RECOMMENDED
DEFER
NOT_NOW
```

These are experiment labels only.

### BLOCKING_REQUIRED

Current required work whose unresolved state prevents at least one supplied named downstream scope from being defended.

`defer_until_id` MUST be null.

### RECOMMENDED

Currently justified and useful work that is not a required blocker for a supplied downstream scope.

`defer_until_id` MUST be null.

### DEFER

Allowed only when all are true:

```text
1. the action is already justified or planned;
2. one exact supplied trigger is unresolved;
3. that trigger must happen before the action may legitimately begin;
4. satisfying the trigger makes the action current next work.
```

`defer_until_id` MUST equal the exact supplied trigger ID.

### NOT_NOW

The current objective/state does not materially justify the action and no represented supplied activating trigger makes it current next work after one dependency resolves.

`defer_until_id` MUST be null.

The possibility of future usefulness is insufficient for `DEFER`.

---

## 7. Frozen model-owned structured result

The experiment-owned model result is:

```text
SystemProvenanceRecommendationActionResult
    summary: string
    action_decisions: list[ActionDecision]
        action_id: string
        disposition: BLOCKING_REQUIRED | RECOMMENDED | DEFER | NOT_NOW
        defer_until_id: string | null
        rationale: string
    blocked_scopes: list[string]
    required_clarification_ids: list[string]
    warnings: list[string]
```

The field `methodological_basis` is forbidden.

Validation MUST enforce:

```text
every candidate action appears exactly once
no unknown or duplicate action IDs
blocked_scopes subset of supplied menu
required_clarification_ids subset of supplied menu
DEFER -> exact supplied trigger ID
non-DEFER -> null defer pointer
no unknown trigger IDs
no additional structured-result fields outside the frozen schema
```

A model result is not asked to report what methodological revisions were supplied.

---

## 8. Frozen system-owned provenance record

For every planned reasoner output the system MUST construct before provider execution:

```text
SystemContextProvenance
    condition: GENERIC | SELECTIVE | FULL_HORIZON
    supplied_revisions: list[KnowledgeRevisionPointer]
        stable_key: string
        revision_id: string
    methodology_payload_sha256: lowercase hex SHA-256
    methodology_payload_bytes: integer
```

The provenance record MUST be derived only from the exact methodology payload that will be supplied in that request.

### GENERIC provenance

```text
supplied_revisions = []
```

The payload digest and byte count refer to the canonical empty-methodology payload used by the harness.

### SELECTIVE provenance

The revision pointers MUST exactly match the selected accepted-current revisions rendered into that case's `MethodologicalContextPack`.

### FULL_HORIZON provenance

The revision pointers MUST contain the ten exact accepted-current revisions rendered into the compact full-horizon methodology payload.

The model output MUST have no code path capable of changing or substituting this record.

---

## 9. Frozen benchmark cases

The four cases, all menus, all truth, and all rubrics are inherited byte-for-byte through the locked base fixture.

Case identities remain:

```text
RB-01 VALIDITY_GATE_AND_SEQUENCE
RB-02 COMPACT_MODEL_SHORTLIST_AND_TUNING_SEQUENCE
RB-03 DISTRIBUTION_EVIDENCE_BEFORE_TRANSFORMATION
RB-04 MISSINGNESS_IMBALANCE_DECISION_SEQUENCE
```

Specification 019 does not redefine their expected labels in prose. The locked Specification 017 fixture remains the exact case authority.

---

## 10. Deterministic recommendation metrics

For each successful output compute the inherited metrics:

```text
exact_disposition_accuracy
critical_action_omissions
under_recommendations
over_recommendations
unnecessary_recommended_cost
blocking_scope_false_negatives
blocking_scope_false_positives
required_clarification_false_negatives
required_clarification_false_positives
defer_pointer_errors
```

`unsupported_methodological_basis_failures` is removed because provenance is no longer model-authored.

This removal is not a favorable rescore. It deletes an obsolete instrumentation metric that no longer exists in the model result contract.

---

## 11. Provenance integrity is an execution invariant, not a recommendation score

Every planned output MUST satisfy deterministic provenance integrity before any scientific advancement classification is allowed:

```text
record generated before provider call
record derived from actual methodology payload
SHA-256 recomputes exactly
payload byte count recomputes exactly
GENERIC revision list empty
SELECTIVE revisions equal inherited exact selected revisions
FULL_HORIZON revision list contains all ten exact revisions
attempts/retries reuse the same frozen provenance record for the planned output
model result cannot mutate provenance
```

Any provenance mismatch means execution integrity fails.

When execution integrity fails:

```text
gate evaluation = not permitted
advancement outcome = none
```

It does not count as a model semantic error.

---

## 12. Blinded semantic judge

Every successful reasoner output receives exactly one judge call.

The judge receives only:

```text
opaque output ID
user task
project evidence
candidate action menu
blocked-scope menu
clarification menu
defer-trigger menu
frozen rubric
candidate model-owned recommendation result
score definitions
```

The judge MUST NOT receive:

```text
condition identity
methodological context
system provenance
context digest
selection metadata
provider usage or latency
paired outputs
expected deterministic labels outside the rubric
```

Each inherited obligation is scored:

```text
0 absent, materially wrong, or contradicted
1 partial or implicit without material contradiction
2 explicit and correct
```

Normalized score:

```text
sum(scores) / (2 * number_of_obligations)
```

The judge may not add obligations.

---

## 13. Frozen absolute SELECTIVE gates

SELECTIVE MUST satisfy all:

```text
SPRA-G01  critical_action_omissions == 0
SPRA-G02  blocking_scope_false_negatives == 0
SPRA-G03  defer_pointer_errors == 0
SPRA-G04  required_clarification_false_negatives == 0
SPRA-G05  aggregate exact disposition accuracy >= 0.90
SPRA-G06  every case exact disposition accuracy >= 0.85
SPRA-G07  aggregate semantic score >= 0.90
SPRA-G08  every case semantic score >= 0.85
```

The former Specification 017 unsupported-basis gate is not present because no model-authored basis field exists.

All provenance integrity invariants in Section 11 are prerequisites to evaluating these gates.

---

## 14. Frozen relative non-inferiority gates

Inherited unchanged:

```text
aggregate exact accuracy vs GENERIC       >= -0.05
per-case exact accuracy vs GENERIC        >= -0.10
aggregate exact accuracy vs FULL_HORIZON  >= -0.05
per-case exact accuracy vs FULL_HORIZON   >= -0.10

aggregate semantic score vs GENERIC       >= -0.05
per-case semantic score vs GENERIC        >= -0.10
aggregate semantic score vs FULL_HORIZON  >= -0.05
per-case semantic score vs FULL_HORIZON   >= -0.10

SELECTIVE critical omissions <= GENERIC
SELECTIVE blocking false negatives <= GENERIC
SELECTIVE under-recommendations <= GENERIC
SELECTIVE required-clarification false negatives <= GENERIC
SELECTIVE defer-pointer errors <= GENERIC
```

These remain bounded experiment gates, not formal statistical non-inferiority claims.

---

## 15. Frozen expansion gates

Inherited unchanged. SELECTIVE MUST be no worse than FULL_HORIZON on:

```text
unnecessary recommended cost
over-recommendations
blocking-scope false positives
required-clarification false positives
```

---

## 16. Frozen positive value signals

The ten Specification 017 signals are inherited without addition or threshold change:

```text
S1  SELECTIVE aggregate exact disposition accuracy >= GENERIC + 0.05
S2  SELECTIVE aggregate semantic score >= GENERIC + 0.05
S3  SELECTIVE total critical omissions < GENERIC
S4  SELECTIVE total blocking-scope false negatives < GENERIC
S5  SELECTIVE total under-recommendations < GENERIC
S6  SELECTIVE total required-clarification false negatives < GENERIC
S7  SELECTIVE total defer-pointer errors < GENERIC
S8  SELECTIVE unnecessary recommended cost < FULL_HORIZON
S9  SELECTIVE total over-recommendations < FULL_HORIZON
S10 SELECTIVE total blocking-scope false positives < FULL_HORIZON
```

Structured-output completion, retry reduction, and provenance conformance are descriptive instrumentation evidence only. They are not promotion signals.

---

## 17. Frozen complete-design outcomes

A scientific advancement outcome is allowed only if all 36 reasoner outputs and all 36 corresponding judge outputs are successfully scored and execution integrity passes.

### PROMOTE_SYSTEM_PROVENANCE_RECOMMENDATION_SEAM

Requires:

```text
all absolute gates pass
all relative gates pass
all expansion gates pass
at least one inherited positive value signal
```

### SAFE_BUT_NOT_DIFFERENTIATED

Requires:

```text
all absolute gates pass
all relative gates pass
all expansion gates pass
zero inherited positive value signals
```

### FAIL

Any frozen absolute, relative, or expansion gate fails after a complete scored design with execution integrity.

### Incomplete or integrity-failed execution

```text
advancement outcome = none
```

Do not force an incomplete execution into one of the three complete-design outcomes.

---

## 18. Frozen reasoner configuration

```text
provider                     OpenAI
runtime                      OpenAI Agents SDK behind ADS-owned ReasoningRuntime
runtime version              0.19.4
requested model              gpt-5.6-sol
reasoning effort             medium
text verbosity               low
max output tokens            4000
tools                        none
previous response state      none
fast/priority processing     not requested
store                        false where exposed
```

This is an experiment constant only.

---

## 19. Frozen judge configuration

```text
provider                     OpenAI
runtime                      OpenAI Agents SDK 0.19.4
requested model              gpt-5.6-sol
reasoning effort             high
text verbosity               low
max output tokens            4000
tools                        none
condition identity           hidden
one judge call               per successful reasoner output
```

---

## 20. Frozen repetitions, randomization, and provider budget

```text
4 cases
3 conditions
3 repetitions per condition
36 planned successful reasoner calls
36 planned successful judge calls
72 planned successful provider calls
randomization seed 2026082304
maximum total provider attempts 90
maximum retries per planned call 1
```

Retryable failure classes only:

```text
TRANSPORT_FAILURE
PROVIDER_FAILURE
INCOMPLETE_RESPONSE
INVALID_STRUCTURED_RESPONSE
```

Semantic disagreement is never a retry reason.

Every reasoner request receives a unique condition-neutral nonce. Judge order is independently deterministic and condition blinded. All failed attempts are preserved.

---

## 21. Frozen plan and trace artifacts

Before the first provider call, the runner MUST serialize and hash:

```text
reasoner plan
judge plan
accepted knowledge snapshot
system provenance plan
```

The system provenance plan MUST bind all 36 planned reasoner output IDs to:

```text
case_id
condition
repetition
nonce
supplied stable_key@revision_id pointers
methodology_payload_sha256
methodology_payload_bytes
```

The plan is immutable after the first provider attempt.

---

## 22. Provider-free technical invariants

Before any live provider call, ordinary CI MUST prove all overlay invariants, including:

```text
SPRA-INV-01 base fixture Git blob SHA matches exactly
SPRA-INV-02 effective four-case scientific truth equals frozen Specification 017 truth
SPRA-INV-03 exact 36-call reasoner plan deterministic under seed 2026082304
SPRA-INV-04 judge plan deterministic, independently shuffled, condition blinded
SPRA-INV-05 GENERIC supplies zero methodology revisions and records empty revision provenance
SPRA-INV-06 SELECTIVE stable-key sets match inherited exact sets
SPRA-INV-07 FULL_HORIZON supplies all ten exact accepted-current revisions
SPRA-INV-08 provenance generated before provider call from actual methodology payload
SPRA-INV-09 payload SHA-256 and byte count recompute exactly
SPRA-INV-10 model schema contains no methodological_basis field
SPRA-INV-11 model output cannot mutate system provenance
SPRA-INV-12 matched conditions share identical task/project/action/trigger evidence
SPRA-INV-13 action/menu/defer-pointer structured validation is exact
SPRA-INV-14 judge payload is condition/context/provenance/usage/paired-output blinded
SPRA-INV-15 retry accounting obeys 90-attempt ceiling; semantic disagreement non-retryable
SPRA-INV-16 complete fake-runtime design evaluates 36 reasoner and 36 judge outputs
SPRA-INV-17 ordinary CI contains no provider credential
SPRA-INV-18 application/domain layers remain free of provider SDK imports
SPRA-INV-19 authoritative project state is not mutated
SPRA-INV-20 live launch remains unauthorized until exact green source/CI evidence is checkpointed
```

The dedicated provider-free gate MUST run on Ubuntu and Windows.

---

## 23. Descriptive instrumentation

Record per condition and overall:

```text
successful structured outputs
invalid structured outputs
retry counts
input tokens
cached input tokens
output tokens
reasoning tokens
total tokens
latency
serialized methodology bytes
SELECTIVE/FULL context ratios
provider model/runtime identifiers
provider response/request IDs when exposed
```

These do not override recommendation/action gates.

---

## 24. Governed live launch boundary

No live provider call is authorized by this specification alone.

After implementation, a checkpoint MUST freeze:

```text
exact implementation source SHA
exact successful Ubuntu/Windows provider-free CI run IDs
exact target live workflow
exact confirmation token
exact required CI evidence for Specification 018 registry authorization
```

Only then may one enabled repository-controlled authorization be added to `.github/ads_live_experiments.json` on `main`.

The accepted Specification 018 launcher may then dispatch the target workflow from an owner-created governed issue.

The launcher itself MUST receive no provider credential. The target workflow MUST independently verify the exact source SHA and confirmation before provider execution.

---

## 25. Historical integrity requirements

Specification 019 implementation and interpretation MUST NOT:

```text
edit or rescore Specification 015
edit Specification 016 after its result
edit Specification 017 or its raw result
use partial Specification 017 scores to tune truth, thresholds, signals, or treatment
reinterpret reasoning-function labels as reusable-knowledge provenance
claim that removing methodological_basis retroactively makes Specification 017 complete
```

Specification 017 remains incomplete historical evidence permanently.

---

## 26. Explicit non-goals

This experiment does not establish or implement:

```text
model-authored methodological citation value
natural-language/project-state -> reasoning-function derivation
open-world action generation
production recommendation enum design
complete Foundation 018 dependency persistence
Proposal/Question/Investigation/Decision mutation
automatic project execution
human approval/escalation policy
final ranking/prioritization policy
risk/admissibility policy
multi-agent recommendation architecture
production semantic retrieval stack
frontend/Cockpit wiring
final provider/model selection
```

---

## 27. Exact implementation sequence

```text
1. freeze Research 026, Specification 019, overlay fixture, and Checkpoint 163
2. implement strict effective-fixture loading with base Git-blob verification
3. implement model-owned result without methodological_basis
4. implement system-owned provenance records and plan hashing
5. reuse the inherited context, action metric, judge, retry, and runner semantics without scientific-truth changes
6. implement complete fake-runtime and persistence-backed provider-free tests
7. add dedicated Ubuntu/Windows provider-free CI with no provider credential
8. freeze and checkpoint the exact green implementation head
9. add one exact Specification 018 launch authorization
10. dispatch one frozen live run through the governed launcher
11. preserve all raw evidence before interpreting any outcome
```

No Specification 019 live provider call is authorized before steps 1-8 are complete and green.
