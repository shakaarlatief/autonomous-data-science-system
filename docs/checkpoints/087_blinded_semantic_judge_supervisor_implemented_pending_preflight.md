# Checkpoint 87: Blinded Semantic Judge Supervisor Implemented Pending Preflight

**Date:** 2026-08-19

## Purpose

Record the implementation boundary for the automated Prototype V0 held-out semantic-evaluation stage after all 30 treatment slots were complete and before any held-out semantic judge call was launched.

The treatment experiment remains frozen and complete. This checkpoint introduces evaluation orchestration only.

## Why another supervisor is needed

The preregistered semantic stage requires:

```text
30 retained behavior-evaluable treatment trajectories
x 2 fresh independent blinded judge passes
= 60 completed semantic judgments
```

Running those calls manually would recreate the same operational weakness previously observed during held-out treatment execution:

```text
manual path selection
manual condition-blindness bookkeeping
manual output naming
manual retry/recovery after provider errors
manual consensus assembly
manual export for adjudication
```

The evaluation should therefore automate mechanics while preserving the semantic protocol exactly.

## New implementation

Added:

```text
prototype_v0/src/ads_v0/semantic_judge_supervisor.py
prototype_v0/tests/test_semantic_judge_supervisor.py
```

The new supervisor wraps the already calibrated and preregistered semantic judge. It does not modify:

```text
semantic_judge.py rubric text
S1-S10 anchors
SC1/SC2 definitions
two-pass requirement
judge model
judge reasoning effort
judge blinding rules
consensus rules
manual adjudication triggers
continuation/falsification thresholds
any B0/B1/P0 trajectory
```

## Blinding architecture

Before inference, the supervisor reconstructs the frozen held-out plan and requires the treatment runner to report:

```text
EXPERIMENT_COMPLETE
```

For each of the 30 slots it then requires exactly one slot-resolving behavior-evaluable attempt.

Each retained trajectory is converted by the existing common external normalizer into a semantic judge packet. The packet is checked against all frozen execution identifiers, including:

```text
B0
B1
P0
all slot identifiers
all possible attempt identifiers
```

The packet receives an opaque case identifier derived only from its packet SHA-256 fingerprint:

```text
case-<opaque hash prefix>
```

Judge execution order is sorted by opaque case identity rather than treatment-slot order.

The treatment-to-blinded-case mapping is persisted separately as:

```text
results/held_out/semantic_judge/private_decoder.json
```

This file is local runtime state under the ignored `results/` tree. It must not be inspected or exported until all required blinded manual adjudications have been frozen.

## Resumability and provider recovery

Each logical pass is persisted independently:

```text
pass_1.json
pass_2.json
consensus.json
```

A completed valid pass is never rerun because of its score.

The semantic protocol specifies two completed independent judge judgments but does not define transport-level provider recovery. Before any held-out semantic judge call, this checkpoint therefore records a condition-neutral operational rule:

```text
maximum provider attempts per logical judge pass: 3
```

A new provider attempt is permitted only when the previous provider attempt did not produce a usable persisted semantic judgment. Provider failures and interrupted transport attempts are logged separately. Once a valid pass is persisted, that logical pass is immutable for ordinary execution.

This rule does not alter treatment resource accounting and cannot selectively improve a condition because case identity remains blinded during judge execution.

## Midstream information policy

The supervisor intentionally does not print score vectors or condition summaries while the batch is running.

Live terminal output may show only condition-blind mechanics such as:

```text
opaque case identifier
logical pass number
pass persisted
case complete
whether manual blinded adjudication is required
provider-call count
batch stop reason
```

Condition decoding and B0/B1/P0 aggregation remain forbidden until all ordinary two-pass consensus values and all required manual adjudications are frozen.

## Blinded review export

The supervisor can create one compact review ZIP containing an explicit allowlist of:

```text
prepared blinded manifest
packet.json
pass_1.json
pass_2.json
consensus.json
provider-attempt metadata
batch records
```

The export explicitly excludes:

```text
private_decoder.json
```

The implementation does not recursively ZIP the semantic root, specifically to prevent a future local file from accidentally leaking the decoder into a blinded review archive.

## Commands

No-inference preparation:

```bash
python -m ads_v0.semantic_judge_supervisor prepare
```

Condition-blind status:

```bash
python -m ads_v0.semantic_judge_supervisor status
```

Paid blinded judge batch:

```bash
python -m ads_v0.semantic_judge_supervisor run-batch --max-judge-calls <N>
```

Blinded export:

```bash
python -m ads_v0.semantic_judge_supervisor export
```

## Current validation status

At this checkpoint:

```text
implementation: complete
held-out treatment execution: complete 30 / 30
held-out semantic judge calls launched through this supervisor: 0
local deterministic test confirmation after implementation: pending
no-inference 30-case preparation confirmation: pending
```

No held-out semantic score has been generated or inspected as part of this implementation step.

## Next step

Pull the latest repository and run the complete deterministic suite.

If it passes, run only the no-inference preparation and status commands. Confirm:

```text
30 blinded cases prepared
0 model inference launched during preparation
0 logical judge passes persisted
next blinded work exists
```

Only after that preflight is reviewed should the first paid held-out semantic judge batch be authorized.
