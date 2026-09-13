# Research 138: Relation-Lifecycle Discriminator V0.2 H1/H2 Empirical Result

**Date:** 2026-09-13
**Status:** V0.2 RELATION-LIFECYCLE PROBE COMPLETE / BOTH CANDIDATES SEMANTICALLY PASS / FAMILY BOUNDARY AND ADMISSION-SELECTIVITY CLAIMS CORRECTED BY MC-0014 / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Execute the exact hash-frozen Relation-Lifecycle Discriminator V0.2 against the strongest allowed H1 source-local representation and a narrowed H2 first-class relation substrate; measure correctness, ownership naturalness, write coupling, stale-update safety, admission selectivity and derived-state rebuildability.
**Authority:** Supporting Research 124 empirical architecture evidence only. Requirements V0.2 remain the frozen candidate-acceptance authority. This result does not select a target architecture or authorize migration.
**Declared references:** `research:124`, `research:136`, `research:137`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`, `path:docs/research/project_knowledge_architecture_probe_v02/RELATION_LIFECYCLE_FIXTURE_V02.json`, `path:docs/research/project_knowledge_architecture_probe_v02/RESULTS_V02.json`, `checkpoint:480`

## 1. Probe integrity and implementation fairness

The exact V0.2 fixture was committed and pushed before any V0.2 candidate implementation existed:

```text
fixture_id: PKA-RL-V02
fixture SHA-256:
    ece094762e3fe4f064640004da3f2293aa39168268af183df6f1347ba7f4b4c0
fixture-freeze commit:
    5db6df2dd730d23ddfb11e6fd6a522e1a0755273
```

The runner refuses fixture drift through that exact SHA. H1 and H2 consume identical fixture bytes and identical temporal, lifecycle, concurrency, evidence and rebuild oracles.

Final implementation/evidence surfaces:

```text
scripts/research/project_knowledge_architecture_probe_v02.py
    SHA-256 12bb139baaec500d99d7e1e0f9fb2b781a381fa396cdb41dd2d916cb2f854fcc

tests/unit/test_project_knowledge_architecture_probe_v02.py
    SHA-256 ebe48955496ef7625ccbf4581635950f339ea863b62dcb044a399d2e6385a25a

docs/research/project_knowledge_architecture_probe_v02/RESULTS_V02.json
    SHA-256 75b3ff81370bee4acc7e2e932190b401f04dfd7dbefed1302650fc1ff65bdd53
```

A defect-first self-review strengthened, rather than weakened, H1 before final evidence was generated. The first implementation had placed the independent relation directly inside an endpoint document, which would overstate H1 carrier churn because Research 137 explicitly permits a tightly source-owned sidecar. The final H1 therefore uses a **source-owned relation sidecar** under one endpoint while keeping endpoint intrinsic documents unchanged. Likewise, the 10x/50x/100x ordinary-relation scale test materializes actual synthetic relations through each candidate's admission path rather than merely calculating expected counts.

No fixture bytes changed during those implementation refinements.

## 2. Final candidate representations

### 2.1 H1: strongest allowed source-local form

`R-ABC-1` and `R-ABC-2` remain source-local, but because the ternary relation is symmetric and the fixture declares no natural endpoint owner, H1 must choose one endpoint by a deterministic tie-break:

```text
owner-selection rule:
    lexicographically smallest symmetric member

chosen owner:
    S-A

authoritative location:
    sidecar:S-A:relations
```

The sidecar is source-owned rather than an independently authoritative relation registry. Relation lifecycle updates therefore do not modify `S-A`'s intrinsic semantic document or semantic revision. They do, however, repeatedly mutate an authoritative surface whose ownership is justified only by a tie-break rather than relation meaning.

### 2.2 H2: minimal first-class relation substrate

H2 applies the frozen four-part admission rule:

```text
stable relation identity required
AND independent lifecycle
AND relation-specific provenance
AND no natural endpoint owner
```

Only `R-ABC-1` and `R-ABC-2` qualify. The ordinary directional `S-D depends_on S-A` control remains source-local. The same is true for every added ordinary relation in the 10/50/100 scale condition.

This is intentionally much narrower than the V0.1 H2 prototype. It tests **selective semantic promotion**, not a general-purpose central control registry.

## 3. Semantic correctness: both candidates pass

Both H1 and H2 pass every frozen V0.2 semantic/failure oracle:

```text
H1 semantic correctness: PASS
H2 semantic correctness: PASS
```

Both correctly reconstruct:

```text
proposed relation state
later disputed state
accepted but not yet effective state
accepted and effective state
accepted pending future supersession
superseded predecessor after successor effectiveness
current successor relation
relation-specific evidence lineage
recording time versus authority-transition time versus effective time
```

Both also:

```text
reject the stale revision-3 update after relation revision reaches 4
perform zero authoritative mutation on that stale attempt
surface missing E3 as unresolved_missing_relation_evidence
preserve endpoint semantic revision 1 throughout the relation lifecycle
delete and deterministically rebuild all declared derived relation views
bind each rebuilt view to authoritative-source digest/freshness
```

So V0.2 does **not** show that H1 is incapable of representing a first-class relation lifecycle correctly. A source-local sidecar plus explicit relation identity/state can do so.

## 4. The discriminator moved from correctness to semantic ownership

The central empirical difference is not whether the lifecycle can be encoded. It is whether the authoritative home has a semantic reason to be where it is.

Observed owner classification:

```text
H1
    R-ABC-1 owner       sidecar:S-A:relations
    R-ABC-2 owner       sidecar:S-A:relations
    owner basis         lexicographic tie-break
    natural owner?      no
    arbitrary owners    2

H2
    R-ABC-1 owner       spine:R-ABC-1
    R-ABC-2 owner       spine:R-ABC-2
    owner basis         relation owns independent lifecycle
    natural owner?      yes under frozen admission semantics
    arbitrary owners    0
```

This is stronger evidence than the V0.1 generic-cross-object argument because the fixture deliberately removes directional ownership. `S-A`, `S-B` and `S-C` are symmetric members; none changes intrinsically while the relation is proposed, disputed, accepted, verified and superseded.

The valid conclusion is therefore:

> **When a relation has stable identity, materially independent lifecycle/state, relation-specific provenance, and no natural source owner, separate first-class relation ownership removes an otherwise arbitrary placement decision.**

That is empirical support for a **selective relation-object mechanism**, not for a broad semantic/control spine.

## 5. Strongest-H1 correction removes an overclaim about endpoint churn

The final strong H1 representation matters to interpretation.

Endpoint intrinsic carrier revisions remain unchanged in **both** candidates:

```text
                       H1   H2
S-A endpoint carrier    1    1
S-B endpoint carrier    1    1
S-C endpoint carrier    1    1
S-D endpoint carrier    1    1
```

H1's source-owned sidecar instead evolves:

```text
S-A relation sidecar write revision: 1 -> 5
```

This means the V0.2 evidence does **not** support a claim that H1 inherently rewrites endpoint intrinsic knowledge whenever an independent relation changes. The architecture can isolate that churn in a sidecar while still keeping source-local ownership.

The remaining H1 cost is more precise:

```text
relation lifecycle is physically isolated
BUT
its authoritative namespace/owner is semantically arbitrary
```

That is a real architectural distinction, but a smaller one than “H1 corrupts or churns endpoint documents.”

## 6. Physical write/fan-out comparison is mixed

The probe also prevents a false claim that H2 is automatically cheaper to maintain.

Successful relation-lifecycle transitions produce:

```text
                                      H1   H2
source-owned relation touch events      4    0
independent relation authority sites    1    2
total authoritative location touches    4    5
```

H1 stores predecessor and successor relation declarations in one source-owned sidecar, so scheduling supersession can update one physical authoritative location. H2 gives predecessor and successor independent first-class records, so that transition touches two relation records.

Therefore:

> **H2 improves semantic ownership clarity in V0.2, but it does not win the physical-write-cost dimension.**

This is exactly the kind of trade-off the architecture comparison needed to expose. First-class identity and lifecycle isolation can increase explicit object count or transition fan-out.

## 7. Minimal H2 admission rule passes its first selectivity test

The strongest concern after V0.1 was that “bounded spine” could become semantically central despite staying physically small. V0.2 therefore narrows H2 and adds a negative control.

Observed admission result:

```text
qualifying independent relations
    expected  R-ABC-1, R-ABC-2
    admitted  R-ABC-1, R-ABC-2

ordinary directional control
    SR-D-A admitted?  no

false-positive admissions  0
false-negative admissions  0
```

When additional ordinary relations are materialized:

```text
ordinary source-local relations added   10    50    100
H2 first-class relation-spine records    2     2      2
false-positive spine admissions          0     0      0
```

This is materially different from V0.1's broad H2 prototype. It supports the narrower hypothesis:

> **A first-class relation substrate can stay selective if admission is based on relation identity/lifecycle/provenance/ownership semantics rather than mere cross-objectness.**

The result is synthetic and rule-shaped, so it does not yet prove that humans/models will classify ambiguous real ADS relationships correctly. Classification ergonomics and borderline cases remain open.

## 8. Semantic-fact share must be interpreted in fixture context

V0.2 normalizes 15 propositions:

```text
H1
    source-local 15
    relation spine 0

H2
    source-local 5
    relation spine 10
```

Unlike V0.1, this fixture intentionally concentrates most tested semantics **inside the two qualifying relations**. The 10/15 H2 share is therefore not evidence that a future ADS relation substrate would own two thirds of project semantics.

The relevant boundedness observation is instead:

```text
ordinary non-qualifying relation growth  -> remains source-local
qualifying independent relation count    -> determines relation-spine growth
```

Future real-corpus qualification must measure the empirical frequency of qualifying relations rather than extrapolate this synthetic ratio.

## 9. What V0.1 + V0.2 jointly establish

The two probes together sharpen the candidate boundary substantially.

V0.1 established:

```text
cross-objectness alone does not justify separate authority
directional relations can remain source-local
multi-source closure may safely be derived
broad H2 semantic centralization is not automatically earned
```

V0.2 adds:

```text
some relations can have their own material identity/lifecycle/provenance/time
source-local representation remains semantically possible
but no natural endpoint owner may exist
first-class relation ownership removes arbitrary placement
narrow admission can reject ordinary relations and stay physically bounded
first-class objects may cost more physical locations/touches
```

The strongest integrated architecture hypothesis is therefore narrower than both original H1 and original H2:

> **Source-local by default, with separately authoritative first-class semantic/control objects only when the thing itself earns independent identity/lifecycle/provenance and cannot be naturally owned by one source; all broader navigation, closure, search and context views remain derived/rebuildable.**

This remains a **working hypothesis**, not a selected target.

## 10. Relationship to Requirements V0.2

No requirement defect was exposed. V0.2 already permits exactly this selective interpretation.

The result particularly operationalizes:

```text
KA-R15  first-class relation semantics only where the relation carries material state/time/provenance/authority
KA-R16  current/history and selective temporal semantics
KA-R18  relation-specific provenance/auditability
KA-R21  derived-view rebuildability
KA-R29  stale/concurrent update detection
KA-R33  dependency-local maintenance
KA-R43  preservation through representation/identity change
KA-R46  representation-independent identity when continuity is intentional
KA-R47  multi-axis organization without duplicated truth
KA-R49  selective temporal/supersession semantics
```

Requirements V0.2 therefore remain unchanged.

## 11. What remains unproven

V0.2 does not answer several important target-selection questions:

```text
how often real ADS relations satisfy the first-class admission rule
whether borderline cases are classified consistently by humans and models
whether first-class workstream/control objects should use the same admission principle
how first-class relation identity should be physically represented
whether typed files, structured text, relational rows, a static graph, or another substrate is best
how source-local -> first-class promotion works during a real relation's evolution
how merge/split of relation identities behaves under real migration
whether independent relation objects materially improve fresh-model discovery/authority activation
how public/private relation boundaries behave in realistic mixed-authority cases
```

The probe also does not convert the synthetic admission rule into permanent architecture policy merely because it passed its own fixture.

## 12. Multi-model gate is now valuable again

Research 134 explicitly deferred another Claude turn until probe evidence existed, preferably as adversarial interpretation of the same raw results. That condition is now satisfied with **two** empirical probe rounds.

The next high-value step is not a third internally designed synthetic fixture immediately. It is a bounded adversarial review that gives Claude:

```text
frozen Requirements V0.2
Research 134 protocol
V0.1 fixture + raw results + Research 136 interpretation
V0.2 fixture + raw results + this Research 138 interpretation
```

and asks it specifically to search for:

```text
fixture bias toward H1 or H2
invalid ownership assumptions
whether H1 source-owned sidecars secretly cross into H2
whether H2's admission rule is circular or self-fulfilling
measurement artifacts
missing stronger H1/H2 representations
unjustified extrapolation from synthetic to real ADS
whether H3 or another family should reopen
what minimum real-repository evidence is needed before target narrowing
```

This should be an **ADVERSARIAL_REVIEW**, not another independent architecture design. Independence from candidate families is no longer the point; critical interpretation of shared evidence is.

## 13. Verification

Final V0.2 verification:

```text
fixture hash guard                    PASS
probe no-write execution              PASS
H1 semantic checks                    PASS
H2 semantic checks                    PASS
focused V0.2 unit tests               11 passed
full tests/unit suite                 187 passed
Python compile check                  PASS
```

Repository-wide structural integrity is evaluated after this result is reconciled into routing/checkpoint state; only that later aggregate can establish `PUBLIC_REPOSITORY_INTEGRITY=PASS` for the full transition.

## 14. Current disposition

```text
RELATION_LIFECYCLE_FIXTURE_V02=COMPLETE
H1_V02_SEMANTIC_CORRECTNESS=PASS
H2_V02_SEMANTIC_CORRECTNESS=PASS
H1_ARBITRARY_RELATION_OWNER=OBSERVED
H1_ENDPOINT_INTRINSIC_CHURN=NOT_OBSERVED_WITH_ALLOWED_SIDECAR
H2_FIRST_CLASS_RELATION_OWNERSHIP=SUPPORTED_FOR_QUALIFYING_CASE
H2_ADMISSION_SELECTIVITY=SUPPORTED_IN_V02
H2_PHYSICAL_WRITE_COST_DOMINANCE=NOT_ESTABLISHED
REQUIREMENTS_V02=UNCHANGED_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=BOUNDED_ADVERSARIAL_CROSS_MODEL_INTERPRETATION
```

## 15. MC-0014 adversarial correction

MC-0014 materially narrows two claims made above.

First, the final strong-H1 sidecar already stores the same lifecycle-bearing first-class relation object shape as H2. V0.2 therefore does not cleanly discriminate non-reified H1 from reified H2; it mainly compares endpoint-namespaced versus relation-addressed ownership of the same broad mechanism. The placement distinction remains real, but the family distinction was overstated.

Second, the V0.2 admission/selectivity result is self-confirming as a classification test. The fixture supplies the same four semantic flags that `H2Probe.qualifies_for_spine()` reads directly. Zero false positives/negatives therefore establishes rule implementation correctness on hand-labeled inputs, not reliable classification of real unlabeled ADS relationships. The lifecycle, temporal, stale-update, missing-evidence and derived-rebuild results remain valid.

Accordingly `H2_ADMISSION_SELECTIVITY=SUPPORTED_IN_V02` is withdrawn as a real-world classification claim. Research 139 replaces `bounded spine` with the representation-neutral working concept `selective semantic reification` and freezes the real-corpus independent-judgment protocol required to test the admission boundary properly.
