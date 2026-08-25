# Checkpoint 190: Specification 022 Live-Capable Source Frozen

**Date:** 2026-08-25  
**Status:** LIVE-CAPABLE SOURCE FROZEN; NO PROVIDER CALL AUTHORIZED  
**Checkpoint class:** IMPLEMENTATION / LIVE-SOURCE FREEZE  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Preserves the exact live-capable source, target workflow, provider-free executable validation, and immutable source ref for the already-frozen Specification 022 methodological-navigation coverage diagnostic.  
**Authority:** Engineering/instrumentation and source-freeze checkpoint only. It does not assign a Specification 022 scientific outcome, create a live-experiment registry authorization, authorize provider execution, change the frozen scientific contract or fixtures, promote benchmark knowledge into accepted methodological authority, modify Specifications 015-021, or select a final production navigation policy.  
**Design session:** 05  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 05 - Selective Context Promotion & Reasoning Vertical Slice  
**Branch:** `v1-methodological-navigation-coverage-diagnostic`  
**PR:** #68, draft  
**Starting promoted integration head:** `0b8ad9cdc3fbd4dab7fcc53dec596ba78946831e`

## Boundary

Specification 022 remains scientifically unexecuted. Checkpoint 188 froze the prospective scientific contract and fixtures. Checkpoint 189 closed the provider-free implementation boundary. This checkpoint closes the subsequent live-capable engineering boundary without changing the frozen scientific question, treatment, oracle, representation map, seed, thresholds, gates, or model/runtime treatment.

No provider execution is authorized by this checkpoint.

## Frozen live-capable source

Exact executable source SHA:

```text
cf5893d74fefa699296842b0a48326a9cb50161c
```

Dedicated immutable source ref:

```text
v1-spec022-methodological-navigation-coverage-live-source
```

The ref was created directly from the exact already-green source SHA and must not be moved for this experiment.

## Live-capable additions since Checkpoint 189

The frozen source adds only machinery required to execute the already-frozen Specification 022 design:

```text
experiments/methodological_navigation_coverage/dense_fastembed.py
experiments/methodological_navigation_coverage/adjudication.py
experiments/methodological_navigation_coverage/diagnostics.py
experiments/methodological_navigation_coverage/runner.py
experiments/methodological_navigation_coverage/live_runner.py

tests/unit/test_methodological_navigation_coverage_dense_fastembed.py
tests/unit/test_methodological_navigation_coverage_runner.py
tests/unit/test_methodological_navigation_coverage_live_runner.py
tests/unit/test_methodological_navigation_coverage_live_workflow.py

.github/workflows/v1-methodological-navigation-coverage-live.yml
```

The ordinary cross-platform Specification 022 workflow was expanded to cover the new provider-free/live-capable surfaces.

## Dense retrieval treatment preserved exactly

The live-capable dense adapter preserves the frozen Specification 022 treatment:

```text
fastembed                0.8.0
model                    BAAI/bge-small-en-v1.5
embedding dimension      384
provider                 CPUExecutionProvider
threads                  1
query method             query_embed
passage method           passage_embed
similarity               exact normalized cosine
tie break                stable_key ascending
channel depth            6
```

The semantic passage projection remains the already established Specification 010 projection. `fastembed` remains experiment-local and lazily imported; it is not promoted into the production dependency set by this checkpoint.

## Blinded adjudication tightening

The executable path now makes the frozen two-stage evaluator explicit:

```text
Stage 1
    deterministic normalized exact / acceptable-alias prematching

Stage 2
    one blinded semantic judge call
    fixed Stage-1 pairs cannot be remapped
    semantic matching operates only on remaining unmatched pairs
    fixed pairs receive only state/question-equivalence adjudication
```

Explicit inactive controls are supplied to the judge using opaque evaluator-local control IDs. Their methodological stable keys remain system-owned and are not exposed in the judge prompt.

The judge input still excludes:

```text
condition identity
Horizon source
retrieval trace
methodological payload
representation map
provider-usage differences
advancement thresholds
methodological stable keys for explicit inactive controls
```

## Failure attribution and descriptive diagnostics

The live-capable path preserves the frozen distinction between:

```text
METHODOLOGICAL_UNIVERSE_GAP
NAVIGATION_GAP
REASONING_USE_GAP
```

It also derives, after raw evidence is sealed:

```text
catalog-gap recovery
navigation-gap counts
reasoning-use-gap counts
semantic inactive-control matches
surface-latency records
premature surfacing indicators
never-surfaced-after-activation indicators
```

These are descriptive/diagnostic outputs only and do not alter the frozen advancement gates.

## Raw-before-interpretation boundary

The executable runner writes append-only raw streams for:

```text
requests
navigation
reasoner_attempts
judge_attempts
usage
```

The raw streams are SHA-256 manifested and sealed before any condition metrics, gate evaluation, diagnostics, or advancement outcome are written under the interpretation directory.

A complete scientific classification requires:

```text
108 valid reasoner observations
108 valid blinded judge observations
216 planned successful calls
<= 270 provider attempts
exact frozen fixture identities
all technical preflight invariants
unchanged experiment-local accepted knowledge
sealed raw evidence
```

If the complete integrity-valid matrix is not produced, the runner writes no scientific advancement outcome.

## Provider-free executable validation

The full 108-reasoner + 108-judge orchestration is exercised in ordinary CI with an explicitly evaluator-informed fake runtime. That fake exists only to test execution plumbing and does not constitute scientific evidence.

The test covers:

```text
complete 216-call orchestration
one frozen allowed retry
live-shaped raw_provider_usage serialization
condition-blind judge inputs
opaque inactive-control identities
raw evidence sealing before interpretation
full scoring/gate code path
```

## Live target workflow

The frozen source contains:

```text
.github/workflows/v1-methodological-navigation-coverage-live.yml
```

It is `workflow_dispatch` only and hardcodes:

```text
launch_id     spec022-methodological-navigation-coverage-001
confirmation  RUN_SPEC_022_FROZEN
```

The workflow requires an exact repository-authorized source SHA and `OPENAI_API_KEY`, blanks the provider credential during provider-free preflight, verifies exact live dependency versions, and only then invokes the frozen live runner.

The workflow is present only as an executable target at this boundary. No registry authorization has been created and no owner launch request has been made.

## Exact source validation

The exact frozen source SHA passed all applicable checks:

```text
V1 methodological navigation coverage     32813574558  success
  ubuntu-latest                            97697436258  success
  windows-latest                           97697436153  success
Checkpoint metadata                       32813574617  success
Current routing consistency               32813574588  success
V1 disposition semantics diagnostic       32813574578  success
V1 autonomous live experiment launcher CI 32813574629  success
V1 reasoning context value                32813574553  success
V1 blocking calibration diagnostic        32813574555  success
```

The dedicated Specification 022 workflow also verified `fastembed==0.8.0` on both Ubuntu and Windows without initializing the embedding model or making a provider call.

## Scientific integrity

No Specification 022 scientific fixture or prospectively frozen rule changed during this implementation step.

In particular, unchanged:

```text
28-asset methodological universe
15 methodological relations
4 episodes / 12 snapshots
33 oracle items
2 intentional catalog gaps
GENERIC / ADS_HORIZON / ORACLE_HORIZON conditions
project-state projector
lexical top 6
dense top 6
equal-weight RRF
top 8 direct seeds
one-hop relation expansion
Specification-012 applicability semantics
12-asset Horizon cap
reasoner and judge model treatment
3 repetitions
seed 2026082403
270-attempt ceiling
MN-G01 through MN-G15
MN-P01 through MN-P05
advancement outcome taxonomy
```

Specifications 015-021 remain immutable.

## Exact continuation

```text
1. reconcile README, CURRENT_STATE, KNOWLEDGE_MAP, and current_routing.json to Checkpoint 190
2. validate one clean post-reconciliation Checkpoint 190 head
3. keep v1-spec022-methodological-navigation-coverage-live-source fixed at cf5893d74fefa699296842b0a48326a9cb50161c
4. do not create a registry authorization merely because the source is frozen
5. any provider-backed run still requires a separate one-shot Specification-018 authorization and owner launch request
6. preserve raw artifact bytes before any live scientific interpretation
7. do not modify or rescore Specifications 015-021
```
