from pathlib import Path
import re


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    Path(path).write_text(text.rstrip() + "\n", encoding="utf-8")


def replace_section(text: str, start: str, end: str, replacement: str) -> str:
    pattern = re.compile(rf"(?ms)^{re.escape(start)}\n.*?(?=^{re.escape(end)}\n)")
    if not pattern.search(text):
        raise RuntimeError(f"section not found: {start!r} -> {end!r}")
    return pattern.sub(replacement.rstrip() + "\n\n", text, count=1)


# CURRENT_STATE is a concise current routing artifact.
write(
    "docs/CURRENT_STATE.md",
    """# Current State

**Checkpoint:** 147  
**Date:** 2026-08-23  
**Active development branch:** `v1-recommendation-action-value`  
**Active promotion PR:** #13 into `v1-frontend-spike`  
**Promoted V1 integration branch:** `v1-frontend-spike` at PR #12 merge commit `bd7d1ec5cabc80d39e005d0a12c11295da32f4a6`  
**Development stage:** Prototype V0 complete; bounded V1 now connects governed methodological knowledge, an explained Horizon, selective exact-revision context, and an ADS-owned reasoning runtime to the first frozen recommendation/action-value experiment.  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** implement Specification 015 provider-free only, preserving the frozen GENERIC / SELECTIVE / FULL_HORIZON recommendation-action design, exact deterministic evaluator, bounded action menus, and no-authoritative-mutation boundary before any new live model call.

## Active ChatGPT development context

```text
Design session: 04
ChatGPT project: Autonomous Data Science System
Session title: 04 - Selective Context Promotion & Reasoning Vertical Slice
```

Repository artifacts remain authoritative across chats. The default `main` branch intentionally trails active V1 work.

---

## Durable post-V0 constraint

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Do not restore P0's large always-on context/frontier, narrow path-sensitive activation, generic recursive reopening, or full frontier machinery unchanged.

Current methodological path:

```text
large reusable knowledge universe
    -> retrieval
    -> bounded explained MethodologicalHorizon
    -> applicability / missing-context handling
    -> bounded task-specific relevance selection
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> reasoning evidence
    -> recommendation / REQUIRED-BLOCKING / action evidence [active]
```

---

## Accepted V1 boundaries already promoted

```text
D-028 + Specification 001
    SQLite-centered local-first operational architecture

D-029 + Specification 002 v1.1
    SQLAlchemy Core 2.0 + Alembic 1.x

D-030 + Specification 003
    pyproject.toml + uv + committed uv.lock + uv_build

D-031 + Specification 004
    deterministic governed reusable-knowledge interchange

Specification 008
    promoted Project Cockpit interaction architecture

D-032 / Checkpoint 133
    OpenAI Agents SDK behind an ADS-owned ReasoningRuntime port

Specification 012 v1.0 / Checkpoint 141
    first explained MethodologicalHorizon

Specification 013 v1.0 / Checkpoint 143
    first accepted selective exact-revision MethodologicalContextPack seam

Specification 014 v1.0 / Checkpoint 146
    first real-model selective-context value gate passed
```

Specification 014 observed equal frozen semantic quality (`1.000000` versus `1.000000`) while SELECTIVE used an aggregate provider input-token ratio of `0.334379`, a `66.56%` reduction, with no critical-obligation regression.

No final provider/model, multi-agent architecture, production semantic retrieval stack, final Horizon/context budget, task-profile derivation, or recommendation/REQUIRED-BLOCKING production policy is selected.

---

## Specification 015 recommendation/action contract is frozen

Research 022, Specification 015 v0.1, `recommendation_action_v1.json`, and Checkpoint 147 preregister the first downstream recommendation/action experiment before implementation or live calls.

Frozen question:

> Given the same project microstate, explicit task profile, candidate action menu, model/runtime configuration, and evaluation rubric, does the accepted ADS methodological path help a strong reasoner choose and calibrate the right methodological actions, preserve blocking dependencies, and avoid unnecessary work relative to strong simpler controls?

Frozen conditions:

```text
GENERIC
    same task/project/action envelope
    no reusable methodological assets

SELECTIVE
    accepted Specification 013 exact-revision context

FULL_HORIZON
    all ten exact current accepted Horizon revisions
    same compact reasoning projection
```

Benchmark-only dispositions:

```text
BLOCKING_REQUIRED
RECOMMENDED
DEFER
NOT_NOW
```

The distinction is explicit: `BLOCKING_REQUIRED` is tied to a named validity/dependency scope and is not merely a stronger recommendation.

Frozen cases:

```text
RA-01 VALIDITY_GATE
RA-02 MODEL_CHOICE
RA-03 EVIDENCE_PLAN
RA-04 MISSINGNESS_IMBALANCE
```

Frozen design:

```text
4 cases
3 conditions
3 repetitions
36 planned reasoner outputs
36 blinded judge outputs
72 planned successful provider calls
maximum 90 provider attempts
```

Primary evaluation is deterministic:

```text
exact disposition accuracy
critical action omissions
under-recommendations
over-recommendations
unnecessary recommended cost units
blocking-scope false negatives / positives
required-clarification false negatives
basis-provenance failures
```

The blinded semantic judge is secondary for rationale/dependency correctness.

Advancement is explicitly three-way:

```text
PROMOTE_BOUNDED_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
FAIL
```

A promotion claim requires all safety/non-regression/expansion gates plus at least one preregistered positive value signal. A three-way ceiling result must not be relabeled as added system value after the fact.

---

## Current non-selections

Still deliberately open:

```text
natural-language/project-state -> reasoning-function derivation
open-world proposal generation
final recommendation enum/ranking model
complete Foundation 018 production schema
mapping recommendations to authoritative Proposal/Question/Decision events
automatic execution
human approval/escalation policy
admissibility/risk-sensitive assurance policy
final provider/model and reasoning-effort policy
multi-agent/specialist recommendation architecture
production semantic retrieval/reranking/vector infrastructure
backend/API, artifact/job, cloud/deployment architecture
final frontend stack and Cockpit implementation details
```

Do not return to retrieval/relevance tuning merely because more tuning is possible. Add complexity only when downstream evidence exposes a concrete deficiency.

---

## Exact continuation

```text
1. implement ADS-owned RecommendationActionResult / disposition types provider-free
2. implement the exact deterministic evaluator
3. implement GENERIC / SELECTIVE / FULL_HORIZON condition construction
4. implement deterministic reasoner/judge plans and blinded semantic-judge contracts
5. add fake-runtime unit/integration coverage for the complete 36 + 36 observation shape
6. add ordinary Ubuntu/Windows provider-free workflow coverage with no live API key
7. validate the exact implementation head
8. only then establish the explicit secret-gated live boundary
9. preserve the live result before any treatment or threshold change
```

No live Specification 015 reasoner or judge call has occurred.

Primary active sources:

```text
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/recommendation_action_v1.json
docs/checkpoints/147_first_recommendation_action_value_contract_frozen.md
```
""",
)


# README current route and active experiment.
path = "README.md"
text = read(path)
text = replace_section(
    text,
    "## Current development stage",
    "## Prototype V0 result and durable constraint",
    """## Current development stage

**Prototype V0 is complete. The project is in bounded V1 implementation and integration.**

Current execution state:

```text
checkpoint            147
active branch         v1-recommendation-action-value
active PR             #13 -> v1-frontend-spike
promoted V1 head      bd7d1ec5cabc80d39e005d0a12c11295da32f4a6
current boundary      Specification 015 frozen; provider-free recommendation/action implementation next
```

The first real-model selective-context value gate is promoted through Specification 014 v1.0 / Checkpoint 146. The next frozen question moves downstream from context economy to whether ADS can correctly calibrate `RECOMMENDED` versus `REQUIRED / BLOCKING`, avoid important omissions, and avoid unnecessary work.

Research 022, Specification 015 v0.1, the frozen recommendation/action fixture, and Checkpoint 147 now govern that implementation. No new live Specification 015 call has occurred.

For exact continuation, start with:

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
```
""",
)
text = text.replace(
    "This does not prove that reasoning functions solve general semantic relevance, that `max_assets = 3` is universal, or that selective context improves downstream reasoning.",
    "This does not prove that reasoning functions solve general semantic relevance or that `max_assets = 3` is universal. Specification 014 provides the first bounded downstream reasoning evidence; broader recommendation/action value and scaling remain separate questions.",
    1,
)
active = """## Active experiment: recommendation and action value

Specification 015 v0.1 / Checkpoint 147 freeze the first downstream test of:

```text
RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
    -> bounded project action
```

Three conditions hold the project microstate, explicit reasoning-function profile, candidate action menu, output schema, and concrete model/runtime configuration fixed:

```text
GENERIC
    no reusable methodological assets

SELECTIVE
    accepted exact-revision MethodologicalContextPack

FULL_HORIZON
    all ten exact Horizon revisions
```

The four frozen microstates test a future-prediction validity gate, compact nonlinear model choice, bounded distribution-evidence planning, and interacting missingness/class-imbalance decisions.

Every action must be classified exactly once as:

```text
BLOCKING_REQUIRED
RECOMMENDED
DEFER
NOT_NOW
```

Primary evaluation is deterministic, including exact disposition accuracy, critical omissions, under/over-recommendation, unnecessary action cost, and blocking-scope errors. A blinded semantic judge is secondary for rationale/dependency correctness.

The advancement rule deliberately distinguishes:

```text
PROMOTE_BOUNDED_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
FAIL
```

so a ceiling result against strong controls cannot be post-hoc reinterpreted as additional ADS value.

Primary active sources:

```text
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/recommendation_action_v1.json
docs/checkpoints/147_first_recommendation_action_value_contract_frozen.md
```

---

"""
marker = "## Exact continuation"
if "## Active experiment: recommendation and action value" not in text:
    if marker not in text:
        raise RuntimeError("README exact-continuation marker missing")
    text = text.replace(marker, active + marker, 1)
text = replace_section(
    text,
    "## Exact continuation",
    "## Repository role",
    """## Exact continuation

```text
1. implement Specification 015 provider-free only
2. establish ADS-owned recommendation result/disposition types and exact evaluator
3. build GENERIC / SELECTIVE / FULL_HORIZON condition construction and deterministic plans
4. validate the full fake-runtime 36 reasoner + 36 judge shape
5. prove no authoritative project mutation and no live-key leakage into ordinary CI
6. validate Ubuntu + Windows on the exact implementation head
7. only then establish the explicit secret-gated live boundary
```

Do not make a live Specification 015 model call before the provider-free implementation boundary is validated. Do not promote the benchmark disposition labels or bounded candidate menu into final product semantics from the freeze alone.
""",
)
write(path, text)


# KNOWLEDGE_MAP routing.
path = "docs/KNOWLEDGE_MAP.md"
text = read(path)
text = text.replace("**Current checkpoint:** 146", "**Current checkpoint:** 147", 1)
text = text.replace("**Active development branch:** `v1-reasoning-context-value`", "**Active development branch:** `v1-recommendation-action-value`", 1)
text = text.replace("**Active promotion PR:** #12 into `v1-frontend-spike`", "**Active promotion PR:** #13 into `v1-frontend-spike`", 1)
text = text.replace(
    "**Promoted V1 integration branch:** `v1-frontend-spike` at PR #11 merge commit `fd33184fbff588c6737d77af751bc5def0e31954`",
    "**Promoted V1 integration branch:** `v1-frontend-spike` at PR #12 merge commit `bd7d1ec5cabc80d39e005d0a12c11295da32f4a6`",
    1,
)
text = text.replace(
    "active experiment branch  v1-reasoning-context-value\nactive PR                  #12 -> v1-frontend-spike\npromoted integration head  fd33184fbff588c6737d77af751bc5def0e31954",
    "active experiment branch  v1-recommendation-action-value\nactive PR                  #13 -> v1-frontend-spike\npromoted integration head  bd7d1ec5cabc80d39e005d0a12c11295da32f4a6",
    1,
)
text = text.replace(
    "Specification 014 v1.0 / Checkpoint 146\n    first real-model selective-context value gate PASS\n    quality 1.000000 vs 1.000000\n    aggregate provider input-token ratio 0.334379\n    66.56% input-token reduction",
    "Specification 014 v1.0 / Checkpoint 146\n    first real-model selective-context value gate PASS\n    quality 1.000000 vs 1.000000\n    aggregate provider input-token ratio 0.334379\n    66.56% input-token reduction\n\nSpecification 015 v0.1 / Checkpoint 147\n    first recommendation/action-value contract frozen\n    GENERIC vs SELECTIVE vs FULL_HORIZON\n    provider-free implementation is the active next boundary",
    1,
)
text = text.replace(
    "    -> harder recommendation/action evidence [next]",
    "    -> recommendation / REQUIRED-BLOCKING / action evidence [active frozen slice]",
    1,
)
insert = """## Active recommendation/action-value route

Frozen design sources:

```text
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/recommendation_action_v1.json
docs/checkpoints/147_first_recommendation_action_value_contract_frozen.md
```

Frozen conditions:

```text
GENERIC
    same project/task/action envelope, no reusable methodological assets

SELECTIVE
    accepted Specification 013 exact-revision context

FULL_HORIZON
    all ten exact current accepted Horizon revisions
```

Frozen benchmark dispositions:

```text
BLOCKING_REQUIRED
RECOMMENDED
DEFER
NOT_NOW
```

Frozen cases:

```text
RA-01 VALIDITY_GATE
RA-02 MODEL_CHOICE
RA-03 EVIDENCE_PLAN
RA-04 MISSINGNESS_IMBALANCE
```

Frozen plan:

```text
4 cases x 3 conditions x 3 repetitions
36 reasoner outputs
36 condition-blinded judge outputs
72 planned successful provider calls
maximum 90 attempts
```

Primary metrics are deterministic recommendation/action metrics; semantic judging is secondary. Promotion additionally requires at least one preregistered positive value signal. Otherwise a fully safe ceiling result is classified `SAFE_BUT_NOT_DIFFERENTIATED` rather than being overclaimed.

No provider-free implementation result or live result exists yet.

---

"""
marker = "## Current exact continuation"
if "## Active recommendation/action-value route" not in text:
    if marker not in text:
        raise RuntimeError("KNOWLEDGE_MAP continuation marker missing")
    text = text.replace(marker, insert + marker, 1)
text = replace_section(
    text,
    "## Current exact continuation",
    "## Recent continuity checkpoints",
    """## Current exact continuation

```text
A. implement ADS-owned recommendation result/disposition types provider-free
B. implement exact deterministic evaluator
C. implement GENERIC / SELECTIVE / FULL_HORIZON condition construction
D. add deterministic reasoner/judge plans and fake-runtime coverage
E. add ordinary Ubuntu/Windows provider-free workflow coverage
F. validate the exact implementation head
G. only then establish the explicit secret-gated live execution boundary
```

Do not make a live Specification 015 call before the frozen provider-free implementation is validated. Do not return to retrieval/reranking/vector work without a measured downstream reason.
""",
)
text = text.replace(
    "146  first real reasoning-context-value gate passed and promotion authorized",
    "146  first real reasoning-context-value gate passed and promotion authorized\n147  first recommendation/action-value contract frozen",
    1,
)
write(path, text)


# OPEN_QUESTIONS: route active uncertainty to Specification 015 without pretending the result exists.
path = "docs/OPEN_QUESTIONS.md"
text = read(path)
text = re.sub(
    r"(?m)^\*\*Reconciliation context:\*\*.*$",
    "**Reconciliation context:** Prototype V0 is complete; the post-V0 V1 object/methodological foundations, Project Cockpit interaction architecture, governed reusable-knowledge persistence/interchange, initial runtime selection, retrieval/Horizon chain, deterministic selective-context seam, and first real-model context-value result are established through Specification 014 v1.0 / Checkpoint 146. Specification 015 v0.1 / Checkpoint 147 now freeze the first downstream recommendation/action-value test across GENERIC, SELECTIVE, and FULL_HORIZON conditions. The immediate unresolved boundary is whether the accepted ADS methodological path improves recommendation calibration, blocking behavior, and unnecessary-action control beyond strong simpler controls; task-profile derivation, open-world proposal generation, project-state mutation, human approval, and broader scaling remain separate questions.",
    text,
    count=1,
)
text = text.replace(
    "This supports selective methodological context as a real-reasoning V1 seam. Still open are natural-language/project-state task interpretation, behavior on harder and heterogeneous project tasks, when richer semantic/LLM relevance becomes necessary, open-world discovery of concerns absent from explicit knowledge, final budget policy, and how reasoning should become recommendation/action.",
    "This supports selective methodological context as a real-reasoning V1 seam. Specification 015 / Checkpoint 147 now freeze the first direct downstream recommendation/action test while deliberately holding task-profile derivation fixed. Still open are its result, natural-language/project-state task interpretation, behavior on harder and heterogeneous project tasks, when richer semantic/LLM relevance becomes necessary, open-world discovery of concerns absent from explicit knowledge, final budget policy, and later authoritative project mutation.",
    1,
)
text = replace_section(
    text,
    "### Q-006. How should relevant investigations be activated?",
    "### Q-007. What should a reusable decision or knowledge unit contain?",
    """### Q-006. How should relevant investigations be activated?

**Status:** Retrieval/Horizon/selective-context mechanics validated; first recommendation/action calibration experiment frozen

P0's path-sensitive tag-trigger activation should not scale unchanged. Foundation 019 instead uses staged retrieval, applicability/context checks, bounded relevance selection, recommendation reasoning, and selective reasoning context.

Specification 015 / Checkpoint 147 now isolate the next step after relevance by supplying the same bounded candidate action menu to three conditions and measuring whether actions are calibrated as:

```text
BLOCKING_REQUIRED
RECOMMENDED
DEFER
NOT_NOW
```

The experiment holds action discovery and task-profile derivation constant so recommendation strength and blocking behavior can be attributed cleanly.

Still open:

```text
project state -> current task/reasoning-function profile
open-world concern/action discovery
accepted recommendation -> durable Question / Proposal / Investigation
human approval / automatic-action policy
production REQUIRED/BLOCKING semantics and scope
```
""",
)
text = text.replace(
    "how reasoning becomes recommendation, required concern, proposal, investigation, or action\nhow activation behaves on harder and open-world project states",
    "whether the frozen Specification 015 recommendation/action seam adds value over strong controls\nhow a future accepted recommendation becomes Proposal / Question / Investigation / Decision state\nhow activation behaves on harder and open-world project states",
    1,
)
text = replace_section(
    text,
    "### Q-045. How should recommendation and reasoning quality be evaluated separately from knowledge coverage?",
    "## Agent/runtime, execution, and interoperability",
    """### Q-045. How should recommendation and reasoning quality be evaluated separately from knowledge coverage?

**Status:** First reasoning-quality separation validated; first recommendation/action-value contract now frozen

The executable failure decomposition can already distinguish catalog, retrieval, applicability, relation-expansion, relevance/budget, context-selection, and reasoner-obligation failures.

Specification 014 established the first downstream reasoning evidence:

```text
SELECTIVE quality       1.000000
FULL_HORIZON quality    1.000000
critical regressions    none
aggregate input ratio   0.334379
```

Specification 015 / Checkpoint 147 now preregister the next layer with exact deterministic recommendation metrics:

```text
exact disposition accuracy
critical action omissions
under-recommendations
over-recommendations
unnecessary recommended cost
blocking-scope false negatives / positives
basis-provenance failures
```

and three conditions:

```text
GENERIC
SELECTIVE
FULL_HORIZON
```

The frozen advancement rule distinguishes `PROMOTE_BOUNDED_RECOMMENDATION_SEAM`, `SAFE_BUT_NOT_DIFFERENTIATED`, and `FAIL`, so equal ceiling performance cannot be claimed as added ADS value without a preregistered positive signal.

Still open after this gate will be open-world proposal generation, final recommendation strength/ranking semantics, production REQUIRED/BLOCKING policy, human/system follow-through, authoritative project-object mutation, and downstream execution outcome quality.
""",
)
text = text.replace(
    "**Status:** Open; runtime boundary selected, one bounded model treatment frozen for Specification 014",
    "**Status:** Open; runtime boundary selected, the same bounded model treatment is held fixed through Specification 015 for attribution",
    1,
)
text = text.replace(
    "D-032 selects runtime infrastructure, not the final LLM provider/model. Specification 014 deliberately freezes `gpt-5.6-sol` under one model configuration only to make the selective/full-context comparison interpretable. That treatment must not be promoted into a permanent model choice merely because the experiment uses it.",
    "D-032 selects runtime infrastructure, not the final LLM provider/model. Specification 014 froze `gpt-5.6-sol` for the selective/full-context comparison; Specification 015 deliberately holds the same concrete treatment fixed while changing the recommendation/action task. This preserves attribution and still must not be promoted into a permanent model choice merely because the experiments use it.",
    1,
)
write(path, text)
