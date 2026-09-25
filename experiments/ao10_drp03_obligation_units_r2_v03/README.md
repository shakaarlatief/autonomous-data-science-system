# AO10 DRP-03 R2 V0.3 Public Protocol Assets

This directory is the public, pre-key freeze surface for the second DRP-03 qualification attempt.

It contains no hidden evaluator key, no hidden semantic labels, no expected STATE outputs, and no scoring harness.

## Core protocol

- `public_protocol.json`: frozen component semantics, thresholds, floors, reviewer-independence rules, and attempt policy.
- `event_universe_frozen.json`: frozen BIRTH event membership and proposal-source-cluster split.
- `REVIEWER_INSTRUCTIONS.md`: packet-only decision-reviewer contract.
- `reviewer_annotation_schema.json`: reviewer output contract.
- `KEY_AUTHOR_INSTRUCTIONS.md`: independent key-author contract.
- `key_author_schema.json`: private key output contract.
- `delivery_plan.json`: exposure order and reviewer/non-reviewer file boundary.

## Deterministic generation

- `splitter.py`: mechanical Markdown segmentation.
- `generate_packets.py`: deterministic reviewer packet and attention-session generator.
- `generate_key_author_packets.py`: bounded key-author packet generator.
- `public_fixtures/sentence_splitter_test_vectors.json`: frozen splitter tests.
- `freeze_public_assets.py`: hashes every public asset and external binding.

The packet generator is reproducible at the public freeze: regenerating all packets and the freeze manifest yields the same public-freeze digest.

## Reviewer delivery

Classification is batch-first.

For BIRTH and LEGACY, each classification batch is frozen before the next batch is exposed. The unique semantic grouping catalog is exposed only after all classification batches for that component are frozen.

Files containing provenance or attention-check mappings are never reviewer deliverables.

The STATE packet contains no expected outputs.

## Hidden-key stage

Two independent key authors are required. At least one must be fresh to MC-0029/R1. Full private key bytes are kept outside reviewer-accessible storage. Only canonical-byte commitments are public until both fresh blind reviewer annotations are frozen.

## Freeze binding

See:

- `public_freeze_manifest.json`
- `public_freeze_commitment.json`

The commitment digest is the source for deterministic cluster-bootstrap seeding in the later scoring harness.

## Authority boundary

This protocol freeze qualifies only the experimental contract. It does not accept V0.7 architecture, authorize production AO-10, authorize migration, retire current oracles, or switch authority.
