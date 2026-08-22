# V1 Selective Methodological Context Result

**Date:** 2026-08-22  
**Status:** Frozen RH-C result; Specification 013 v0.1 passed without threshold or target-set changes  
**Workflow:** `V1 selective methodological context`  
**Run:** `32563091893`  
**Validated implementation head:** `cdba8a11a108c52b8addf029d5612a83a8c20475`  
**PR merge-test commit:** `1af2117d44158ecab5b3995615841ac05ab73341`

## 1. Question tested

The first RH-C gate tested whether a simple deterministic task profile could reduce a deliberately wide ten-asset explained `MethodologicalHorizon` to a small exact-revision model-facing context pack while preserving required methodology and keeping omission evidence outside the pack.

Frozen policy:

```text
requested reasoning functions
    -> primary function matches
    -> REQUIRES_CONCEPT support from selected direct sources
    -> hard max_assets = 3
    -> exact accepted-current compact reasoning projection
    -> MethodologicalContextPack
```

No LLM relevance judge, embedding reranker, learned ranker, production semantic retriever, or model call participated.

---

## 2. Cross-platform gate

```text
Ubuntu   PASS
Windows  PASS
```

Dedicated RH-C/unit gate:

```text
3 passed
```

Full locked V1 regression suite:

```text
Ubuntu   42 passed, 2 skipped
Windows  42 passed, 2 skipped
```

The two skips are the existing PostgreSQL-dependent tests when `ADS_TEST_POSTGRES_URL` is not configured in this workflow.

All canonical selective-pack byte counts and SHA-256 digests were identical across Ubuntu and Windows.

---

## 3. Wide-Horizon stress setup

Direct seeds:

```text
class-imbalance
histogram
missing-data
prediction-time-feature-eligibility
random-forest
temporal-validation
```

Accepted one-hop expansion produced the remaining benchmark assets:

```text
bagging
ecdf
gradient-boosted-trees
prediction-moment
```

Observed:

```text
wide included Horizon = 10 assets
global accepted corpus = 10 assets
```

This intentionally creates a worst-case context-selection stress condition. It is not a production retrieval recommendation.

---

## 4. RH-C01 model-option reasoning

Request:

```text
MODEL_OPTION
max_assets = 3
```

Selected in model-pack order:

```text
1. random-forest
   revision fefb0b89-52b5-4353-9eb0-331670c9211c
   DIRECT
   PRIMARY_FUNCTION_MATCH

2. gradient-boosted-trees
   revision 1b9604fc-6cdb-4ff5-b4de-7aafaa157d89
   RELATION
   PRIMARY_FUNCTION_MATCH
```

Quality:

```text
required key coverage       1.00
required revision coverage  1.00
irrelevant selected         0
missing context             []
```

Size:

```text
full Horizon control        10,744 bytes
selective pack               2,151 bytes
selective/full ratio          0.20020477
reduction                    79.98%
SHA-256                      1945c55c99ee71fac289fd130c18c7cd9ba6ec1fcd8efb8186545e5785baa359
```

---

## 5. RH-C02 empirical-distribution evidence

Request:

```text
EVIDENCE_OPTION
max_assets = 3
```

Selected:

```text
1. histogram
   revision a5035424-0d67-4dfc-9491-dc73df2601ce
   DIRECT
   PRIMARY_FUNCTION_MATCH

2. ecdf
   revision 9b6b4a84-526f-4fba-9036-13ad3cc00896
   RELATION
   PRIMARY_FUNCTION_MATCH
```

Quality:

```text
required key coverage       1.00
required revision coverage  1.00
irrelevant selected         0
missing context             []
```

Size:

```text
full Horizon control        10,752 bytes
selective pack               1,770 bytes
selective/full ratio          0.16462054
reduction                    83.54%
SHA-256                      008f933b5fe5b7e98cf6b37e5dad4103ce329936f84dc9f9a7cab4577b69aad5
```

---

## 6. RH-C03 predictive-validity constraints

Request:

```text
VALIDITY_CONSTRAINT
max_assets = 3
```

Selected:

```text
1. prediction-time-feature-eligibility
   revision 8b63f2cd-a1b7-4b2c-939b-5b146c5d7477
   DIRECT
   PRIMARY_FUNCTION_MATCH
   MISSING_CONTEXT: prediction-moment

2. temporal-validation
   revision a952de3e-d761-4cab-9318-91b2f25f3231
   DIRECT
   PRIMARY_FUNCTION_MATCH
   MISSING_CONTEXT: prediction-moment

3. prediction-moment
   revision 4a3189bb-b007-4efd-a2bd-04a8cc6a4d5c
   RELATION
   REQUIRED_CONCEPT_SUPPORT
```

Quality:

```text
required key coverage       1.00
required revision coverage  1.00
irrelevant selected         0
aggregate missing context   [prediction-moment]
```

Size:

```text
full Horizon control        10,752 bytes
selective pack               3,724 bytes
selective/full ratio          0.34635417
reduction                    65.36%
SHA-256                      18f7fe20a5ecb219e1c1ce47b5ebc7a99b8caf8a4d01280567d8d21e9eab7010
```

This case demonstrates that required conceptual knowledge can be added without erasing the unresolved project-context signal. The concept `prediction-moment` is present as methodological support while the project still lacks an actual represented prediction moment.

---

## 7. RH-C04 data-quality decision frameworks

Request:

```text
DECISION_FRAMEWORK
max_assets = 3
```

Selected:

```text
1. class-imbalance
   revision f30b1304-f5c0-4070-9f21-dc27945d866f
   DIRECT
   PRIMARY_FUNCTION_MATCH
   MISSING_CONTEXT: class-prevalence

2. missing-data
   revision cfefb760-e70a-4b1a-bb6a-3393334b70fa
   DIRECT
   PRIMARY_FUNCTION_MATCH
   MISSING_CONTEXT: production-missingness
```

Quality:

```text
required key coverage       1.00
required revision coverage  1.00
irrelevant selected         0
aggregate missing context   [class-prevalence, production-missingness]
```

Size:

```text
full Horizon control        10,754 bytes
selective pack               3,035 bytes
selective/full ratio          0.28222057
reduction                    71.78%
SHA-256                      2ac2f6e69b13488b2816ebf0dc0940069ca14532d49c2ed669701fedf7826930
```

---

## 8. Frozen acceptance-gate outcome

Specification 013 required:

```text
exact required stable-key coverage          = 1.00
exact required revision coverage            = 1.00
irrelevant selected assets                  = 0
selected asset count                        <= 3
omitted candidates without system reason    = 0
selective/full-Horizon byte ratio            <= 0.65 per case
```

Observed:

```text
RH-C01 PASS  ratio 0.20020477
RH-C02 PASS  ratio 0.16462054
RH-C03 PASS  ratio 0.34635417
RH-C04 PASS  ratio 0.28222057
```

All four cases passed without changing the preregistered targets, max-assets limit, byte threshold, reasoning-function profile, or support rule.

---

## 9. Invariants demonstrated

The executable gate also demonstrated:

```text
exact accepted-current revision reads
stale revision lookup fails closed
full reasoning content materialized only after budget selection
omitted candidates receive explicit system-facing reasons
omission decisions absent from model-facing pack
MISSING_CONTEXT retained for selected unresolved knowledge
REQUIRES_CONCEPT support remains one-hop and Horizon-bounded
retrieval aliases/terms/cues/scores absent from model-facing projection
accepted components, narrative facets, and rules survive selective projection
canonical serialization deterministic
cross-platform pack digests identical
authoritative reusable knowledge unchanged
application/storage boundary preserved
budget overflow reported explicitly as BUDGET_LIMIT
```

---

## 10. Interpretation

The first deterministic relevance/context policy **earns continuation on the frozen corpus**.

The result is stronger than merely reducing asset count. It preserves exact methodological revision coverage while reducing canonical context bytes by approximately:

```text
65% to 84%
```

across four heterogeneous task profiles.

The most important architectural evidence is the separation:

```text
SYSTEM
    retains the ten-asset Horizon
    retains eight omission decisions when two assets are selected

MODEL-FACING PACK
    receives only the two selected exact revisions
```

This is direct executable support for the post-V0 scaling direction.

---

## 11. What this result does not prove

Do not infer that:

```text
reasoning_functions alone solve general semantic relevance
max_assets = 3 is the final context budget
all future Horizons can be compressed this strongly
UTF-8 bytes equal model tokens
an LLM relevance judge will never be useful
selected knowledge improves downstream model reasoning
all required concerns can be represented by existing reasoning functions
recommendation / REQUIRED-BLOCKING policy is solved
```

The benchmark intentionally isolates task-profile selection and context assembly.

---

## 12. Next evidence boundary

The next justified experiment is a real reasoning vertical slice:

```text
same project/task evidence
    -> selective MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> one concrete model configuration
```

Compare selective context against a strong simple control while measuring:

```text
reasoning-output quality on frozen task obligations
exact knowledge revisions actually supplied
provider/model token counts
latency/cost where observable
whether omitted methodology causes a real quality loss
whether full-Horizon context causes distraction or unnecessary cost
```

The real reasoning experiment should be preregistered before model calls.
