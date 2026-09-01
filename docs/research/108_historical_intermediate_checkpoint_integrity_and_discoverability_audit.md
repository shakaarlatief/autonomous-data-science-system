# Research 108 — Historical Intermediate Checkpoint Integrity and Discoverability Audit

**Date:** 2026-09-01  
**Status:** CLOSED / BOUNDED INTEGRITY GAP CONFIRMED / GOVERNANCE EXTENSION SELECTED  
**Scope:** Determine whether a preserved checkpoint artifact whose numeric identity was retired remains useful, whether it should remain in the repository, and how repository-integrity and Knowledge Map coverage should govern that non-numbered historical milestone without fabricating a replacement checkpoint number.  
**Authority:** Bounded architecture evidence for the historical-intermediate checkpoint class; Specification 027 governs implementation.  
**Declared references:** `research:091`, `research:107`, `specification:025`, `specification:026`, `checkpoint:252`, `path:docs/checkpoints/intermediate_2026-08-28_source_faithful_reintegration_interaction_integrity_gate.md`, `path:docs/checkpoints/252_advanced_integrated_cockpit_spatial_rail_study_opened.md`, `path:docs/checkpoints/README.md`, `path:docs/KNOWLEDGE_MAP.md`, `path:scripts/check_checkpoint_metadata.py`, `path:scripts/check_knowledge_map.py`

## 1. Question

The duplicate Checkpoint 252 repair correctly preserved one canonical numbered Checkpoint 252 and retired the earlier source-faithful reintegration milestone's numeric identity. That repair created a legitimate edge case:

```text
canonical numbered checkpoint
    docs/checkpoints/252_advanced_integrated_cockpit_spatial_rail_study_opened.md

preserved earlier milestone
    docs/checkpoints/intermediate_2026-08-28_source_faithful_reintegration_interaction_integrity_gate.md
```

The second file is intentionally not a numbered checkpoint. The question is whether that means it is merely inert residue, or whether it remains durable historical knowledge that should receive explicit integrity and discoverability protection.

## 2. The preserved intermediate milestone remains useful

The intermediate file is not redundant with Research 091.

Research 091 is the primary technical and execution-evidence record for the source-faithful reintegration gate. The preserved milestone additionally records the historical continuity interpretation at that boundary, including:

```text
PROVENANCE GATE
    PASS

FIRST CROSS-MECHANISM INTEGRATION GATE
    PASS for the mechanisms covered by deterministic tests

HOLISTIC INTEGRATED FIDELITY GATE
    OPEN
```

It also preserves the exact authority boundary, the unresolved human-review obligation, the accepted mechanisms that remained authoritative, the provisional shell quarantine, and the continuation protocol at that moment.

The repair wrapper further preserves why the original numeric identity was retired and why no replacement number was fabricated.

Deleting the file would therefore discard useful historical continuity and repair provenance. Renumbering it would fabricate chronology. Keeping it as an explicitly non-numbered historical intermediate milestone is the strongest option.

## 3. Confirmed integrity gap

The existing validators identify checkpoints by a three-digit filename prefix.

Consequences before this refinement:

```text
check_checkpoint_metadata.py
    validates numbered checkpoint files
    ignores the preserved intermediate file

check_knowledge_map.py
    requires semantic range coverage for every numbered checkpoint
    ignores the preserved intermediate file because it has no checkpoint number
```

Therefore both validators can report PASS even if a substantive `intermediate_...md` checkpoint milestone is missing required metadata or is absent from the Knowledge Map.

This is not evidence that the v0.8 integrity architecture failed its frozen contract. The exceptional artifact class arose from the later duplicate-identity repair and was outside the mechanically enumerated numbered-checkpoint surface. It is nevertheless a real discoverability and integrity gap once the intermediate artifact is accepted as durable knowledge.

## 4. Alternatives considered

### Delete the intermediate file

Rejected. It contains useful historical continuity and repair provenance not fully replaced by Research 091 or Git history.

### Give it a replacement checkpoint number

Rejected. That would manufacture a chronology that did not occur and would force unnecessary renumbering or retrospective identity invention.

### Leave it preserved but informally exempt

Rejected. A durable artifact that matters to reconstruction should not depend on human memory to remain discoverable.

### Treat every non-numbered Markdown file in `docs/checkpoints/` as a checkpoint

Rejected. `README.md` and future support/index files are not historical checkpoint records. A generic rule would blur family roles.

### Introduce an explicit historical-intermediate checkpoint class

Selected. The class is narrow, machine-recognizable, preserves the absence of a current checkpoint number, and can receive its own integrity contract without changing numbered chronology.

## 5. Selected class

A retained historical intermediate checkpoint milestone uses:

```text
docs/checkpoints/intermediate_YYYY-MM-DD_<descriptive-slug>.md
```

The `intermediate_` prefix is a governed signal. It is not a substitute checkpoint number.

The file must remain visibly classified as a historical intermediate milestone and must preserve:

```text
Date
Status
Checkpoint class
Project stage
Scope
Authority
interaction provenance appropriate to the originally recorded checkpoint era
Original recorded identity
Identity disposition
```

`Original recorded identity` records history. It does not reactivate that number.

The substantive body should remain historical evidence. A repair wrapper may explain the identity disposition without rewriting what was known at the original milestone.

## 6. Knowledge Map rule

Checkpoint range records remain the correct compact mechanism for numbered checkpoints.

A non-numbered historical intermediate cannot truthfully participate in a numeric range. It must instead be directly routed as a repository path under at least one semantically appropriate Knowledge Map topic.

For the existing source-faithful milestone, the natural route is:

```text
cockpit-provenance
```

This gives the artifact direct semantic discoverability while preserving the single canonical meaning of Checkpoint 252.

## 7. Mechanical enforcement

The bounded implementation should extend the existing focused validators rather than create a parallel truth system.

`check_checkpoint_metadata.py` should:

```text
detect every docs/checkpoints/intermediate_*.md file
reject malformed intermediate filenames
require an explicit Historical Intermediate Milestone H1
require Original recorded identity = Checkpoint NNN
apply the existing checkpoint metadata/provenance era contract using that original NNN
require non-empty Identity disposition
fail, rather than warn, when a governed intermediate wrapper is defective
continue to ignore non-checkpoint support files such as README.md
```

`check_knowledge_map.py` should:

```text
detect every docs/checkpoints/intermediate_*.md file
reject malformed intermediate filenames
require each recognized intermediate path to appear directly in the Knowledge Map routing set
continue using semantic ranges for numbered checkpoints
```

The aggregate public integrity gate already invokes both focused validators, so no second aggregate mechanism is needed.

## 8. Verification requirements

Regression coverage must prove at least:

```text
valid historical intermediate metadata -> PASS
missing Identity disposition -> FAIL
malformed intermediate filename -> FAIL
historical intermediate absent from routed paths -> FAIL
directly routed historical intermediate -> PASS
ordinary support file in docs/checkpoints -> not misclassified
```

The exact branch target must then pass the existing Repository Integrity workflow on both operating systems before the refinement is accepted.

## 9. Collaboration disposition

No additional Claude round is required for this change.

The current Development Method makes SOLO the default for routine bounded work and uses collaboration when independent counter-design or audit value justifies the coordination cost. This edge case has one narrow observed failure mode, a small option set, an existing accepted integrity architecture to extend, and no competing product/scientific interpretation. The coordination cost of opening another collaboration thread would exceed the expected independent-review value.

This does not weaken the prior MC-0008 multi-model architecture. It applies that architecture's proportionality rule.

## 10. Boundary

This audit does not:

```text
renumber any checkpoint
change canonical Checkpoint 252
rewrite Research 091
resume Source Vault ingestion
complete Research 105 local write validation
create a new checkpoint merely for the repair
```

The selected next action is the narrow contract and validator extension frozen in Specification 027.
