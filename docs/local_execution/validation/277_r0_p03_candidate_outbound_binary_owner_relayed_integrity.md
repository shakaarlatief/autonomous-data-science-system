# Validation 277: User-relayed candidate outbound binary and direct attachment equality

**Date:** 2026-10-28
**Status:** INDEPENDENT_UPLOADED_ARTIFACT_BYTE_COMPARISON_PASS / PRIVATE_CUSTODY_HOLD
**Scope:** Verify the actual file uploaded back from the prospective candidate session is exactly the source-free prescribed 1,063-byte payload, not merely a pasted length/hash claim. Preserve the boundary between actual artifact inspection and unverified candidate tool telemetry.
**Basis:** Research 611, Validation 275–276, S1 A2 actor-gate candidate; unchanged Checkpoint 898 and Specification 028.

## Evidence directly observed

The user posted a source-free report returning `OUTPUT_FILE_CREATED_AND_READBACK_VERIFIED` and separately attached `a2_candidate_outbound_v1.bin`. The coordinator directly read that mounted attachment using Python:

```python
from pathlib import Path
import hashlib

uploaded = Path("/mnt/data/a2_candidate_outbound_v1.bin").read_bytes()
expected = (
    b"ADS-S1-A2-OUTBOUND-FIDELITY-V1\n"
    + bytes(range(256)) * 4
    + b"\x00\xff\r\nEND\x00"
)
assert len(uploaded) == len(expected) == 1063
assert uploaded == expected
assert hashlib.sha256(uploaded).hexdigest() == (
    "36ef80e20ed23c52b4e83b0599ba4ca3cc2229fcc2e104e4b0eb4a01b386c33d"
)
```

Actual result:

```text
UPLOADED_FILE_EXISTS=TRUE
UPLOADED_BINARY_BYTES=1063
EXPECTED_BYTES=1063
UPLOADED_SHA256=36ef80e20ed23c52b4e83b0599ba4ca3cc2229fcc2e104e4b0eb4a01b386c33d
EXPECTED_SHA256=36ef80e20ed23c52b4e83b0599ba4ca3cc2229fcc2e104e4b0eb4a01b386c33d
COMPLETE_BYTE_EQUALITY=TRUE
```

The exact `/mnt/data` attachment was available in the coordinator's current sandbox; the Windows Runtime Bridge repository is **a separate filesystem and authority surface**. This validation record keeps the observable bytes/digest and exact construction algorithm, but does not claim that the actual uploaded binary has been automatically published or copied into Git.

## What this test cannot qualify

The original candidate Temporary Chat's claimed `Path.write_bytes()`, `Path.read_bytes()` and `hashlib.sha256()` invocations are reported, not independently observed by the coordinator. The successful user-mediated transfer demonstrates an intact **public** outbound artifact, not restricted reviewer-only output, recipient authorization, confidentiality, revocation, owner-only recovery or denial from an actual primary-author session.

The previous CMS trial did not use this exact route or an owner-approved actual recipient and must not be combined transitively into an A2-R05 confidential-custody PASS. No real historical source was sent, no reviewer/challenger assigned, and no source-specific rationale or hidden gold was disclosed.

```text
VALIDATION_277=SOURCE_FREE_OUTBOUND_USER_ATTACHED_FILE_BYTE_MATCH_PASS
RECEIVED_ARTIFACT_SHA256=36ef80e20ed23c52b4e83b0599ba4ca3cc2229fcc2e104e4b0eb4a01b386c33d
CANDIDATE_TOOL_EXECUTION=SELF_REPORTED
REAL_PRIVATE_CUSTODY=NOT_QUALIFIED
ACTUAL_AUTHOR_ACCESS_DENIAL=NOT_TESTED
REAL_REVIEWER_AND_CHALLENGER=NOT_ADMITTED
REAL_SOURCE_RECORDS_DELIVERED=ZERO
AUTHOR_WORLD=WORLD_UNFROZEN
GOLD_AND_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
