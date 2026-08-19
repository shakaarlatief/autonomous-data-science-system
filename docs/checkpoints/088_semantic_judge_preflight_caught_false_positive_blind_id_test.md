# Checkpoint 88: Semantic Judge Preflight Caught False-Positive Blind-ID Test

**Date:** 2026-08-19

## Purpose

Record the first local no-inference preflight of the new held-out semantic-judge supervisor, the single deterministic-test failure it exposed, and the condition-neutral correction made before any held-out semantic judge call was launched.

## User-run preflight

After pulling the semantic-judge supervisor implementation, the local preflight produced:

```text
pytest: 1 failed, 83 passed
heldout monitor: active=none, completed_attempts=34, verified=34, integrity_failures=none
semantic prepare: 30 / 30 blinded cases prepared
model inference launched during prepare: 0
semantic status: 0 / 60 logical passes, 0 / 30 completed cases, provider_calls=0
```

The first attempted `git pull` in the same session failed because the local machine could not resolve `github.com`; a later pull succeeded. This was a local network/DNS event and had no experiment effect.

## Failing test

The only failed assertion was in:

```text
prototype_v0/tests/test_semantic_judge_supervisor.py
```

The test required the opaque blind identifier string itself to contain none of the lexical substrings:

```text
b0
b1
p0
```

One synthetic packet deterministically produced:

```text
case-16f02ebb0b04904a
```

The random-looking hexadecimal digest happened to contain the two-character substring `b0`, causing the assertion to fail.

## Why this was a test false positive rather than a blinding defect

Production blind IDs are generated as:

```text
packet
  -> packet SHA-256
  -> SHA-256("prototype-v0-semantic-blind:" + packet_sha256)
  -> first 16 hexadecimal characters
  -> case-<hex>
```

The identifier derivation uses only the condition-neutral packet fingerprint. It does not use:

```text
condition label
slot ID
attempt ID
run order
variant/replicate identity
private decoder contents
```

A hexadecimal digest can naturally contain the character sequence `b0` or `b1` by coincidence. Lexical absence of those substrings is therefore not a valid invariant for condition blindness.

The real blinding invariants remain:

```text
1. common judge packets are checked for B0/B1/P0, slot IDs, and attempt IDs;
2. blind IDs are derived only from the packet fingerprint;
3. the treatment-to-blind-ID mapping is stored only in the private decoder;
4. the private decoder is excluded from blinded review exports;
5. semantic progress output exposes only opaque IDs before decoding.
```

## Correction

Only the test was changed. Production semantic-supervisor code was not modified.

The corrected test now verifies that each blind ID:

```text
exactly equals _opaque_blind_id(packet_sha256)
starts with case-
contains exactly 16 hexadecimal digest characters
has a corresponding persisted packet
```

This tests the intended invariant directly: blind identity is a deterministic function of packet fingerprint rather than execution identity.

## Existing local preparation

The user had already run `prepare` after the failing `pytest` command because the shell invocation continued after the test failure.

That preparation reported:

```text
Prepared blinded cases: 30 / 30
Model inference launched: 0
Private decoder created locally and excluded from blinded review exports.
```

The subsequent status was:

```text
prepared_cases=30
logical_passes=0/60
completed_cases=0/30
manual_cases=0
provider_calls=0
```

Because the production preparation implementation was not changed by this correction, those prepared packets are not invalidated. Preparation is idempotent and will revalidate them on the next invocation.

## Experimental integrity boundary

At this checkpoint:

```text
held-out treatment slots resolved: 30 / 30
held-out semantic judge provider calls launched: 0
held-out semantic logical passes persisted: 0 / 60
condition decoding performed: no
semantic condition comparison performed: no
```

Therefore the test correction occurred entirely before held-out semantic inference and cannot have been informed by semantic evaluation outcomes.

## Next action

Pull the corrected test and rerun the no-inference preflight:

```bash
git pull origin main
pytest
python -m ads_v0.heldout_monitor status
python -m ads_v0.semantic_judge_supervisor prepare
python -m ads_v0.semantic_judge_supervisor status
```

If the deterministic suite passes and the semantic status remains `0/60` with `provider_calls=0`, the blinded semantic-judge execution stage can be authorized.
