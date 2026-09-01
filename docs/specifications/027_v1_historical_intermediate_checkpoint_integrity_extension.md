# Specification 027 — V1 Historical Intermediate Checkpoint Integrity Extension

**Date:** 2026-09-01  
**Status:** FROZEN / IMPLEMENTATION CONTRACT  
**Scope:** Extend the governed repository-integrity architecture so preserved non-numbered historical intermediate checkpoint milestones receive explicit metadata and Knowledge Map protection without re-entering the numbered checkpoint sequence.  
**Authority:** Narrow extension to Specifications 025 and 026 for the historical-intermediate checkpoint class. All unaffected clauses of Specifications 025 and 026 remain in force.  
**Declared references:** `research:108`, `research:107`, `specification:025`, `specification:026`, `checkpoint:252`, `path:docs/checkpoints/intermediate_2026-08-28_source_faithful_reintegration_interaction_integrity_gate.md`, `path:docs/checkpoints/252_advanced_integrated_cockpit_spatial_rail_study_opened.md`, `path:docs/checkpoints/README.md`, `path:docs/KNOWLEDGE_MAP.md`, `path:scripts/check_checkpoint_metadata.py`, `path:scripts/check_knowledge_map.py`

## 1. Relationship to the existing integrity architecture

Specifications 025 and 026 remain the base repository-integrity and recovery contracts.

This specification adds one narrowly observed artifact class created by legitimate checkpoint-identity repair:

```text
historical intermediate checkpoint milestone
```

The extension MUST reuse the existing checkpoint metadata validator, Knowledge Map validator and aggregate public repository-integrity gate. It MUST NOT create a parallel checkpoint registry or a second semantic map.

## 2. Recognized historical-intermediate filename contract

A governed historical intermediate checkpoint milestone MUST use:

```text
intermediate_YYYY-MM-DD_<descriptive-slug>.md
```

under:

```text
docs/checkpoints/
```

The exact machine-recognized shape is:

```text
^intermediate_\d{4}-\d{2}-\d{2}_[a-z0-9][a-z0-9_-]*\.md$
```

Any file in `docs/checkpoints/` whose basename begins with `intermediate_` but does not satisfy that shape MUST fail integrity validation.

Other non-numbered support files such as `docs/checkpoints/README.md` remain outside this class.

## 3. Identity semantics

A historical intermediate milestone has no current checkpoint number.

It MUST contain:

```text
**Original recorded identity:** `Checkpoint NNN`
**Identity disposition:** <non-empty explanation>
```

`Original recorded identity` is provenance only. It MUST NOT:

```text
reactivate the retired number
create a second canonical checkpoint with that number
change current_checkpoint
participate in maximum-number freshness
force renumbering of later checkpoints
```

The filename remains non-numbered and is the current repository identity of the preserved artifact.

## 4. H1 and metadata contract

The H1 MUST begin with:

```text
# Historical Intermediate Milestone:
```

The wrapper MUST satisfy the existing checkpoint historical/authority core:

```text
Date
Status
Checkpoint class
Project stage
Scope
Authority
```

Interaction provenance MUST use the existing checkpoint-era contract determined by the numeric value in `Original recorded identity`:

```text
original checkpoint <= 203
    historical ChatGPT provenance fields

original checkpoint >= 204
    provider-neutral interaction provenance fields
```

This preserves the provenance era of the represented historical checkpoint rather than rewriting old context into a newer schema.

Unlike ordinary numbered checkpoints 000-099, an explicitly governed `intermediate_...` wrapper receives no legacy-warning exemption. Once retained as this class, missing required metadata is a repository-integrity error.

## 5. Knowledge Map contract

Numbered checkpoint semantic coverage remains range-based.

Historical intermediate milestones MUST NOT be inserted into `KM-CHECKPOINT-RANGE` records because they have no active numeric checkpoint identity.

Instead:

```text
every recognized docs/checkpoints/intermediate_*.md artifact
    MUST appear as an exact repository path in docs/KNOWLEDGE_MAP.md
    under at least one KM-TOPIC subject
```

The existing source-faithful reintegration intermediate milestone MUST be routed under `cockpit-provenance`.

Direct routing is required because the artifact contains durable historical knowledge and repair provenance that should not depend on filename browsing or chat memory.

## 6. Validator behavior

### `scripts/check_checkpoint_metadata.py`

MUST:

```text
discover all files beginning intermediate_ in docs/checkpoints
reject malformed intermediate filenames
validate the Historical Intermediate Milestone H1
parse Original recorded identity as exactly Checkpoint NNN
apply the corresponding existing checkpoint metadata/provenance era contract
require Identity disposition
report intermediate defects as errors
leave ordinary non-numbered support files unclassified
```

### `scripts/check_knowledge_map.py`

MUST:

```text
discover all files beginning intermediate_ in docs/checkpoints
reject malformed intermediate filenames
require every valid intermediate path in the map's routed path set
keep numbered checkpoint range coverage unchanged
include the intermediate count in the successful summary
```

### Aggregate gate

No new aggregate component is required because `scripts/check_repository_integrity.py` already invokes both focused validators.

A defect in either focused contract therefore MUST cause:

```text
PUBLIC_REPOSITORY_INTEGRITY=FAIL
```

## 7. Regression tests

The implementation MUST add deterministic regression coverage for:

```text
valid provider-neutral intermediate metadata
missing Identity disposition
malformed intermediate filename
missing direct Knowledge Map route
direct Knowledge Map route present
README/support file not misclassified as an intermediate milestone
```

Tests MUST execute inside the existing Repository Integrity workflow on both Ubuntu and Windows.

## 8. Current Checkpoint 252 repair

The accepted repair remains unchanged:

```text
canonical numbered Checkpoint 252
    docs/checkpoints/252_advanced_integrated_cockpit_spatial_rail_study_opened.md

historical intermediate milestone
    docs/checkpoints/intermediate_2026-08-28_source_faithful_reintegration_interaction_integrity_gate.md
```

The intermediate artifact MUST retain its historical substance and identity-repair provenance.

No new checkpoint number is assigned to it.

## 9. Canonical method promotion

The operational Development Method and checkpoint-family contract MUST be updated to state the distinction:

```text
numbered checkpoints
    semantic range coverage + numbered checkpoint metadata contract

historical intermediate checkpoint milestones
    non-numbered identity + explicit retired-identity provenance
    + checkpoint metadata validation
    + direct Knowledge Map routing
```

The current routing manifest MUST identify Specification 027 as the latest specification once this extension is promoted.

## 10. Verification and acceptance

The extension is accepted only when the exact public branch target passes:

```text
focused checkpoint metadata validation
focused Knowledge Map validation
repository-integrity regression tests
aggregate PUBLIC_REPOSITORY_INTEGRITY gate
Ubuntu workflow job
Windows workflow job
```

The validator MUST NOT be weakened to obtain a green result.

After any resulting public commit, private continuity remains a separate claim and its public-safe anchor must be reconciled independently if private PASS is required.

## 11. Non-goals

This specification does not authorize:

```text
renumbering checkpoints
creating a general unnumbered-checkpoint family
turning every docs/checkpoints Markdown support file into a checkpoint
rewriting historical milestone bodies
resuming Source Vault ingestion
completing Research 105 local write validation
creating a new checkpoint merely because this integrity refinement exists
```

A later checkpoint after 269 remains subject to the normal meaningful-verified-boundary rule.
