# Validation 306: Owner-verified real restricted Wave0 semantic adjudication packet

**Date:** 2026-11-09
**Status:** OWNER_REPORTED_REAL_SEMANTIC_VERIFYEXPORT_PASS / NEW_ADJUDICATOR_DELIVERY_PENDING
**Research:** 623 and 622; **Prior validation:** 304–305.
**Specification:** 028 unchanged. **Checkpoint:** 898 unchanged.
**Scope:** Preserve source-free owner-local readback of the restricted ten-source semantic adjudication packet without transferring the protected ZIP or source-specific findings to the public engineering coordinator.

## 1. Exact owner-returned observation

The owner pasted this output from their local Windows PowerShell:

```text
S1_WAVE0_OWNER_SEMANTIC_PACKET_VERIFYEXPORT=PASS
S1_WAVE0_OWNER_SEMANTIC_EXPORT_RECHECK=PASS
PS C:\Projects_Data\autonomous-data-science-system>
```

These are two markers **from the same `-Action VerifyExport` invocation**: one emitted by the Python verifier and one by the PowerShell wrapper, not two separate verification attempts. This message did not include a separate `SelfTest` or `Export` marker, a packet SHA-256 or its byte size. Those details are not fabricated.

The source-free qualified implementation (Validation 305) only emits the `VerifyExport` PASS marker after reauthenticating and binding the two complete first-pass CMS reports, paired comparison CMS, original ten source bytes and the authenticated substantive adversarial challenge CMS; reconstructing the seven-member adjudication packet from those authenticated inputs; and finding a byte-for-byte match with the existing owner-protected restricted ZIP.

The file `R0_P03_S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION_INPUT.zip` therefore exists in the owner's existing ACL-protected recipient folder and was independently recomputed from the intended evidence. It is a **restricted plaintext** ZIP, not a CMS, and upload to a chosen adjudicator explicitly exposes its contents to that provider. No real owner-private data was read through the public Codexless Runtime Bridge and no source-specific result has been imported into the repository.

## 2. Scientific and workflow limits

This verifies **adjudication input custody**, not that a new adjudicator has inspected the packet, chosen ten dispositions, tested missing context or returned any new encrypted decision report. The record does not imply ten source admissions, a final semantic consensus, or a frozen source world.

The owner's explicit separate disclosure authorization (Research 623) remains narrowly limited to **one new non-arm semantic adjudicator** with the same ten original sources, both complete first-pass rationales, paired evidence and the authenticated adversarial challenge. The first-pass and challenge evidence remains immutable. The selected adjudicator is distinct from the earlier adversarial challenger, primary/gold/arm/scoring actors and public coordinator. A fresh Temporary Chat without connected apps is a pragmatic independence measure, not cryptographic proof of provider memory isolation.

The new adjudicator must issue one evidence-grounded **proposed** decision or a justified HOLD for every source, including claim and disclosure materiality, contrary interpretations, historical/version authority, missing evidence, and a specific falsification or follow-up condition. Its report stays `PROPOSED_DECISIONS_REQUIRE_OWNER_QUALIFICATION`, `author_release=NONE`, `WORLD_UNFROZEN`, even after transport and eventual owner authentication.

## 3. Next action

Do **not rerun `Export`**. The owner now selects `R0_P03_S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION_INPUT.zip` from the protected local owner folder and personally uploads exactly that file to one separate new **Temporary Chat outside the ADS Project with no connected apps**. Use the read-only role/scoping prompt in `experiments/r0_p03_navigation_probe/S1_WAVE0_SEMANTIC_ADJUDICATION_HANDOFF_V01.md`.

After actual source-grounded adjudication, the new actor returns a distinct `R0_P03_S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION.cms` binary and only a safe size/SHA-256/schema-completion receipt. The owner then downloads the CMS and runs the existing owner-only `Receive` once, followed by a **separate** `Verify`; do not expose the CMS or decrypted contents to the public coordinator. Further owner acceptance of source decisions and wider risk-based source-world closure remain after genuine readback, with the 12-primary/9-legacy task generation and B0–B4 experiment still ahead.

```text
VALIDATION_306=OWNER_REPORTED_REAL_SEMANTIC_ADJUDICATION_PACKET_VERIFYEXPORT_PASS
SEMANTIC_PACKET_VERIFYEXPORT=PASS
SEMANTIC_PACKET_POWERSHELL_RECHECK=PASS
VERIFY_MARKERS_SAME_INVOCATION=YES
SEMANTIC_PACKET_SOURCE_BYTES=OWNER_PROTECTED_NOT_READ_BY_PUBLIC_COORDINATOR
SEMANTIC_PACKET_SHA256_BYTES=NOT_SUPPLIED
EXTERNAL_SEPARATE_ADJUDICATOR_RUN=NOT_YET_REPORTED
NEW_ADJUDICATION_CMS=NOT_YET_REPORTED
SEMANTIC_SOURCE_DECISIONS=NOT_YET_OWNER_QUALIFIED
SOURCE_AUTHOR_ADMISSIONS=ZERO
S3_WORLD=WORLD_UNFROZEN
S4_B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
