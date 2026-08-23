# Checkpoint 163: System-Owned Provenance Recommendation and Action Contract Frozen

**Date:** 2026-08-23  
**Status:** FROZEN EXPERIMENT CONTRACT  
**Checkpoint class:** EXPERIMENT CONTRACT / PRE-IMPLEMENTATION BOUNDARY  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Freezes the prospective Specification 019 recommendation/action-value experiment that preserves Specification 017 scientific truth while moving exact supplied-context provenance to system ownership.  
**Authority:** Historical contract-freeze boundary. Research 026, Specification 019 v0.1, and the frozen overlay fixture govern this experiment until a result is preserved.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Development branch:** `v1-recommendation-action-value-system-provenance`  
**Starting integration head:** `ecf37585f576a3c4fd84a884dee4650b52ab1519`  
**Specification 018 promotion merge:** `9fd2243c38a8f0f010396847f519e115d30b8f58`

## 1. Why this checkpoint exists

Specification 017 remains an incomplete live execution rather than a recommendation/action PASS or FAIL.

Its failure boundary was mechanical and treatment-specific:

```text
GENERIC supplied reusable revisions     0
GENERIC successful outputs              5 / 12
GENERIC failed reasoner attempts        19
failure class                           INVALID_STRUCTURED_RESPONSE
repeated invalid values                 requested reasoning-function labels
invalid target field                    methodological_basis
```

The stable lesson was:

```text
reasoning function / task profile
    !=
reusable knowledge stable-key provenance
```

The system already knows exactly what methodological context it supplies. Specification 019 therefore prospectively moves authoritative supplied-context provenance into a deterministic system trace and removes `methodological_basis` from the model-owned result.

This checkpoint freezes that correction before implementation.

---

## 2. Frozen source artifacts

```text
Research 026
    docs/research/026_system_owned_provenance_recommendation_action_value_design.md
    Git blob SHA e1af0113814b63f0deefaf271e51b881497fd150

Specification 019 v0.1
    docs/specifications/019_v1_system_owned_provenance_recommendation_action_value_vertical_slice.md
    Git blob SHA 535a01c9067cfc1ca2aa9abafa8e453c6ede2f8b

Specification 019 overlay fixture
    tests/fixtures/reasoning/system_owned_provenance_recommendation_action_v1.json
    Git blob SHA 1544b804d175efd89cb99a28f6e4576478d286af

Immutable Specification 017 base fixture
    tests/fixtures/reasoning/relation_backed_recommendation_action_v1.json
    Git blob SHA eac949c47a01878dcc47dcca1116493a02ba9805
```

Contract source head immediately before this checkpoint:

```text
6c76509c2614aca9aba3418f998f549a0e704fc3
```

---

## 3. Frozen scientific continuity rule

The experiment inherits Specification 017 benchmark truth rather than rebuilding it.

Frozen rule:

```text
Specification 017 scientific benchmark truth is inherited unchanged.
Only provenance ownership and model-output schema dependence are changed.
```

Inherited without change:

```text
RB-01 through RB-04 project microstates
candidate action menus
costs
expected dispositions
expected DEFER pointers
blocked-scope truth
clarification truth
judge obligations
three conditions
SELECTIVE exact stable-key sets
FULL_HORIZON construction
relative non-inferiority margins
expansion gates
positive value signals
reasoner and judge treatment
repetitions and provider-attempt budget
```

Specification 017 partial outputs and partial scores are prohibited inputs to benchmark tuning.

---

## 4. Frozen model/system ownership split

### System-owned provenance

Before each reasoner call, the harness freezes:

```text
SystemContextProvenance
    condition
    supplied stable_key@revision_id pointers
    methodology_payload_sha256
    methodology_payload_bytes
```

The record is derived from the exact methodology payload actually supplied.

GENERIC has an empty revision list.

SELECTIVE has the exact inherited selected revision set.

FULL_HORIZON has all ten exact accepted-current revisions.

### Model-owned recommendation content

The model returns only:

```text
summary
action decisions
    action_id
    disposition
    defer_until_id
    rationale
blocked_scopes
required_clarification_ids
warnings
```

`methodological_basis` is forbidden.

The model cannot mutate, substitute, or author the system provenance record.

---

## 5. Frozen evaluation

Recommendation metrics remain the Specification 017 deterministic metrics except the obsolete unsupported-basis metric:

```text
exact disposition accuracy
critical action omissions
under-recommendations
over-recommendations
unnecessary recommended cost
blocking-scope false negatives
blocking-scope false positives
required-clarification false negatives
required-clarification false positives
defer-pointer errors
```

SELECTIVE absolute gates:

```text
critical action omissions == 0
blocking-scope false negatives == 0
defer-pointer errors == 0
required-clarification false negatives == 0
aggregate exact disposition accuracy >= 0.90
every case exact disposition accuracy >= 0.85
aggregate semantic score >= 0.90
every case semantic score >= 0.85
```

Relative and expansion gates are inherited unchanged from Specification 017.

All ten positive value signals are inherited unchanged.

System provenance integrity is a technical execution prerequisite, not a semantic recommendation score.

---

## 6. Frozen complete-design outcomes

Exactly these complete-design advancement classes are allowed:

```text
PROMOTE_SYSTEM_PROVENANCE_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
FAIL
```

A complete design requires:

```text
36 / 36 successful reasoner outputs
36 / 36 successful judge outputs
execution integrity passed
```

If the scored design is incomplete or provenance integrity fails:

```text
gate evaluation     not permitted
advancement outcome none
```

---

## 7. Frozen runtime and call plan

Reasoner:

```text
OpenAI
OpenAI Agents SDK 0.19.4 behind ADS-owned ReasoningRuntime
gpt-5.6-sol
reasoning effort medium
verbosity low
max output tokens 4000
no tools
no previous response state
```

Judge:

```text
same provider/runtime/model
reasoning effort high
verbosity low
max output tokens 4000
no tools
condition blinded
```

Call plan:

```text
4 cases
3 conditions
3 repetitions
36 planned successful reasoner calls
36 planned successful judge calls
72 planned successful provider calls
randomization seed 2026082304
maximum provider attempts 90
maximum retries per planned call 1
```

Retryable classes remain:

```text
TRANSPORT_FAILURE
PROVIDER_FAILURE
INCOMPLETE_RESPONSE
INVALID_STRUCTURED_RESPONSE
```

Semantic disagreement is never retryable.

---

## 8. Provider-free implementation gate

No provider call is authorized until ordinary Ubuntu and Windows CI prove at least SPRA-INV-01 through SPRA-INV-20 from the frozen overlay/specification.

Particularly important invariants are:

```text
base fixture blob identity exact
scientific truth inheritance exact
36-call plan deterministic
judge independently shuffled and blinded
GENERIC provenance deterministically empty
SELECTIVE provenance exact
FULL_HORIZON provenance exact
SHA-256 and payload byte counts exact
provenance frozen before provider calls
model schema has no methodological_basis
model output cannot mutate provenance
complete fake-runtime 36+36 design passes
normal CI has no provider credential
project state is not mutated
```

The exact green implementation head and exact required CI run IDs must be checkpointed before live authorization.

---

## 9. Specification 018 launch boundary

Specification 018 is now the accepted launch transport for this future live experiment.

After the exact provider-free implementation head is green, a separate checkpoint may authorize one registry entry containing:

```text
exact launch_id
exact live workflow file
exact source branch
exact source SHA
exact confirmation token
exact required successful CI run IDs
```

Only then may an owner-created governed issue select that authorization.

The launcher itself must receive no provider credential. The target live workflow must independently validate the exact source SHA and confirmation before provider execution.

---

## 10. Promotion audit

### Promoted now

Only the following are frozen as experiment authority:

- Research 026 design rationale;
- Specification 019 v0.1;
- the overlay fixture and its exact immutable-base identity;
- the system-owned provenance/model-owned recommendation split;
- unchanged inherited Specification 017 scientific truth;
- the new randomization seed and prospective call plan;
- provider-free invariants and live-authorization boundary.

### Not promoted now

The following remain unselected:

```text
whether SELECTIVE adds recommendation/action value
production recommendation result schema
production DEFER/NOT_NOW enums
model-authored knowledge citations
final provider/model
human approval/escalation policy
automatic project mutation or execution
multi-agent recommendation architecture
final Cockpit wiring
```

No recommendation/action scientific claim is promoted at this checkpoint.

---

## 11. Exact continuation

```text
1. implement the Specification 019 effective-fixture overlay loader
2. verify the locked Specification 017 base Git blob identity
3. implement recommendation result without methodological_basis
4. implement system-owned provenance records and immutable provenance plan
5. reuse inherited context construction, metrics, judge, retry, and evaluation truth
6. implement provider-free unit/integration tests including a complete fake 36+36 design
7. add dedicated Ubuntu/Windows CI with no provider credential
8. freeze the exact green implementation head in a new checkpoint
9. add one exact Specification 018 launch authorization
10. launch one frozen run through the governed launcher
11. preserve raw evidence before interpreting any complete-design outcome
```

No Specification 019 live provider call is authorized at Checkpoint 163.
