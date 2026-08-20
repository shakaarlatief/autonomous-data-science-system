# Checkpoint 94: Post-Freeze Condition Decoder Implemented Pending Validation

**Date:** 2026-08-19  
**Status:** Deterministic decoder implemented; local validation and first decode pending  
**Checkpoint class:** EXPERIMENT_VERIFICATION  
**Project stage:** Prototype V0 post-freeze decoding  
**Scope:** Records the historical milestone described by this checkpoint: Post-Freeze Condition Decoder Implemented Pending Validation.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Record the implementation boundary for condition decoding after the complete semantic evidence set was frozen and independently verified.

The decoder is implemented in:

```text
prototype_v0/src/ads_v0/semantic_judge_decode.py
prototype_v0/tests/test_semantic_judge_decode.py
```

No decoder execution has yet been reported locally at this checkpoint.

## Why decoding is a separate stage

The semantic experiment deliberately separated:

```text
condition-blind scoring
    from
condition-level comparison
```

The blind is no longer scientifically required after the frozen aggregate was independently verified, but decoding should still be deterministic and auditable rather than performed by manually opening `private_decoder.json` and copying identities into an ad hoc table.

The decoder therefore turns unblinding into a reproducible transformation over already-fixed evidence.

## Ordering invariant

The decoder enforces this exact order:

```text
1. require blinded_freeze.json;
2. require status FROZEN_BLINDED_CONSENSUS;
3. recompute the full blinded semantic verification without reading the decoder;
4. require the recomputed aggregate SHA-256 to equal the frozen aggregate;
5. require 30 cases, 60 logical passes, 30 completed cases, and zero unresolved manual adjudications;
6. only then read private_decoder.json;
7. validate 10 B0, 10 B1, 10 P0 and 5 per condition within both H1 and H2;
8. map each opaque semantic consensus to exactly one retained treatment attempt;
9. combine semantic and mechanical outcomes;
10. write decoded outputs outside the frozen evidence tree.
```

The frozen semantic evidence is never mutated.

## Decoded outputs

The run-level table contains:

```text
variant
replicate
condition
slot and attempt identity
blind identity
S1-S10 consensus scores
SC1/SC2
pooled targeted architecture score
strong-targeted-pass indicator
deterministic + semantic critical-failure count
completion / completion-within-budget / budget exhaustion
model calls
generation attempts and failures
Python attempts
total treatment tokens
final-report presence
```

Aggregates are produced:

```text
pooled by condition
by H1/H2 and condition
paired by H1/H2 replicate for P0-B1 and B1-B0 targeted-score differences
```

## Registered comparison facts

The decoder mechanically evaluates only clauses that have explicit frozen definitions in the common evidence:

```text
P0 versus B1 critical-failure counts
material reliability branch A
material reliability branch B
cross-variant targeted-score robustness
completion requirement
median token/call/Python resource ratios
budget-exhaustion requirement
```

Because every continuation clause is mandatory, the decoder may state whether already-resolved common/mechanical components make the continuation signal impossible.

It does not silently reinterpret ambiguous or P0-internal clauses.

## Deliberately unresolved architecture diagnostics

The decoder explicitly leaves these separate:

```text
critical architecture-induced false block or over-invalidation
noncritical architecture-induced false blocking or unnecessary broad reopening
held-out-case-specific hard coding
```

Those properties require P0-specific internal diagnostics after unblinding and cannot be inferred merely from the condition-neutral S1-S10 score vector.

Similarly, Foundation 012's final strong-falsification clause uses the phrase:

```text
B1 matches or exceeds P0's reliability
```

The decoder reports all underlying critical-failure, targeted-score, strong-pass, and resource facts but does not invent an unstated scalar definition of `reliability` merely to force a classification.

That interpretation will be made explicitly after seeing the decoded result and architecture diagnostics.

## Export boundary

The decoder produces:

```text
results/held_out/semantic_judge_decoded/decoded_results.json
results/held_out/semantic_judge_decoded/decoded_run_table.csv
results/held_out/semantic_judge_decoded_exports/semantic_judge_decoded_<timestamp>.zip
```

The compact export includes the decoded result and run table but does not copy the raw `private_decoder.json` file.

At this stage unblinding itself is authorized, so the output necessarily contains decoded condition identity. Excluding the raw decoder simply keeps the export limited to information needed for analysis.

## Test coverage added

The new tests cover:

```text
predecode freeze re-verification;
refusal on aggregate drift;
30-case condition mapping and balance;
registered comparison facts without fabricated P0 diagnostics;
decoded export contents and exclusion of raw private decoder.
```

The local full-suite result remains pending and must be observed before relying on the decoder output.

## Promotion audit

No new general architecture principle is introduced here. The general principles already governing this stage are:

```text
P-004 evidence over unsupported LLM judgment
P-014 reproducibility and provenance
P-019 complexity must earn its cost
P-022 execution and observability separation
```

The decoder is experiment-specific evaluation tooling. It belongs in the Prototype V0 implementation and experiment history rather than a new system foundation.

## Next step

Pull the decoder, run the full deterministic suite, re-verify the freeze through the decoder's own predecode command, then perform the deterministic decode:

```bash
pytest
python -m ads_v0.semantic_judge_decode verify-freeze
python -m ads_v0.semantic_judge_decode decode
```

Upload the resulting `semantic_judge_decoded_<timestamp>.zip` for independent analysis.

After decoded common outcomes are reviewed, perform the separate P0 architecture-diagnostic pass needed for the remaining strong-falsification clauses.