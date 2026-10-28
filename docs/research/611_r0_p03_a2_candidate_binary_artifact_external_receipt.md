# Research 611: Candidate outbound binary artifact delivery verified independently

**Date:** 2026-10-28
**Status:** SOURCE_FREE_CANDIDATE_OUTBOUND_BINARY_INDEPENDENTLY_VERIFIED / RESTRICTED_CUSTODY_AND_AUTHOR_ACCESS_DENIAL_NOT_QUALIFIED
**Scope:** Reconcile the separate candidate-session's outbound binary-file creation and readback report with the actual user-uploaded output attachment, reconstruct the deterministic expected bytes independently, and identify the distinct remaining A2-R05/R07 qualification requirements.
**Basis:** Research 600/603/606–610 and Validation 270/274–276; R0-P03 S1 A2 actor admission gate candidate; Checkpoint 898, Specification 028 and historic source pin remain unchanged.
**Provenance:** The owner posted the prospective candidate Temporary Chat's source-free response and uploaded the exact named binary artifact `a2_candidate_outbound_v1.bin` to the coordinator conversation. The coordinator directly read the **actual uploaded bytes** from the current conversation's mounted attachment at `/mnt/data/a2_candidate_outbound_v1.bin` using Python and independently reconstructed the prescribed payload. That transient attachment path belongs to the ChatGPT analysis environment, **not** the Windows project workspace or protected owner custody; the binary is not silently imported into Git or a real reviewer store.
**Authority:** Source-free outbound artifact and user-relayed transport-fidelity observation only; no independent candidate session tool telemetry, confidential reviewer custody, real challenger identity, historical-source inspection or primary author-world admission.

## 1. Directly verified evidence

The prospective candidate reported `OUTPUT_FILE_CREATED_AND_READBACK_VERIFIED` using local `Path.write_bytes()`, `Path.read_bytes()`, `hashlib.sha256()` and a full byte equality check on `a2_candidate_outbound_v1.bin`. Its reported output path was `/mnt/data/a2_candidate_outbound_v1.bin`. These **tool actions are candidate self-reported**, but their artifact was actually attached by the owner.

The coordinator directly read the uploaded file and separately reconstructed exactly:

```python
expected = (
    b"ADS-S1-A2-OUTBOUND-FIDELITY-V1\n"
    + bytes(range(256)) * 4
    + b"\x00\xff\r\nEND\x00"
)
```

```text
ATTACHMENT_PRESENT=TRUE
ATTACHMENT_READ_SUCCESS=TRUE
ATTACHMENT_BYTES=1063
EXPECTED_BYTES=1063
ATTACHMENT_SHA256=36ef80e20ed23c52b4e83b0599ba4ca3cc2229fcc2e104e4b0eb4a01b386c33d
EXPECTED_SHA256=36ef80e20ed23c52b4e83b0599ba4ca3cc2229fcc2e104e4b0eb4a01b386c33d
COMPLETE_BYTE_BY_BYTE_EQUALITY=TRUE
CANDIDATE_REPORTED_SHA256=36ef80e20ed23c52b4e83b0599ba4ca3cc2229fcc2e104e4b0eb4a01b386c33d
```

The independently compared **actual user-supplied binary** matches all 1,063 expected bytes, not only its length or a pasted string. The candidate accurately distinguished local readback from independent owner/recipient retrieval; this coordinator's inspection closes that particular external artifact-transfer observation in bounded scope.

## 2. Qualification implications

**Observed improvement:** In addition to R609/R610's source-free text/PNG inbound receipt, the candidate-session route can reportedly construct and read back a binary file, and an actual complete artifact was delivered through the user to this coordinator with exact byte equality. This is a directly observed **end-to-end source-free artifact integrity witness**, bounded to one manually transferred file and one deterministic payload.

**Not established:** The candidate's tool invocation trace remains self-reported; the artifact was carried through a public/exposed coordinator channel, **not** an owner-restricted reviewer-only channel. Therefore this does **not** qualify A2-R05 complete confidential/private output custody, authenticated owner recipient, owner-only recovery, output version/manifest binding, resumption after interruptions, or genuine author-access denial under A2-R07. It does not establish past-exposure independence or authorize the eventual reviewer or challenger. **Do not treat the current public attachment as an example of an acceptable transport for real private findings.**

The existing Research 603 fictional CMS test remains a separate owner-reported protected-handoff precedent. Combining an unrelated CMS demonstration with this unencrypted binary delivery does **not** prove that the exact selected candidate session can send protected, versioned, private review records to an owner-only recipient. Neither the old hardcoded fake schema nor its dummy public certificate is silently promoted.

## 3. Next purposeful qualification, not a repeat of fabricated tests

The next relevant A2-R05/R07 qualification requires **choosing an actual owner-approved protected recipient or storage path and a prospective future author-facing route** with meaningful independent access boundaries. Only then can the exact candidate's protected dummy output be delivered and recovered, followed by a negative access test from that exact author-facing interface. Avoid generating real private keys in public chat, invoking arbitrary cross-workspace paths, or broadening ACLs to make a test appear to pass. If the owner chooses a different architecture, compare its actual isolation properties rather than inheriting the current Windows, branch or CMS assumptions.

A2-R01/R06 distinct actual reviewer and challenger role admission remain separate prerequisites before historical source delivery. No owner approval has yet selected the required restricted route; no actual historical source body, source-status rationale, source admission, task-author packet or hidden gold was exposed by this test.

## 4. Scientific state

```text
RESEARCH_611=SOURCE_FREE_CANDIDATE_OUTBOUND_BINARY_EXTERNAL_ARTIFACT_VERIFIED
A2_CANDIDATE_OUTBOUND_FILE_BYTES=1063
A2_CANDIDATE_OUTBOUND_FILE_SHA256=36ef80e20ed23c52b4e83b0599ba4ca3cc2229fcc2e104e4b0eb4a01b386c33d
A2_PUBLIC_ARTIFACT_TRANSFER_BYTE_EQUALITY=PASS
A2_R05_CONFIDENTIAL_REVIEWER_OUTPUT=NOT_QUALIFIED
A2_R07_ACTUAL_PRIMARY_AUTHOR_ACCESS_DENIAL=NOT_TESTED
A2_R01_ACTUAL_REVIEWER=NOT_ADMITTED
A2_R06_ACTUAL_CHALLENGER=NOT_ADMITTED
REAL_HISTORICAL_SOURCE_DELIVERY=ZERO
S3_AUTHOR_WORLD=WORLD_UNFROZEN
S4_GOLD_AND_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
