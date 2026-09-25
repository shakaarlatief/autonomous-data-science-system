# MC-0028 Provenance Correction: Claude Interaction Session

**Date corrected:** 2026-09-25
**Correction class:** FACTUAL / CLERICAL INTERACTION-PROVENANCE REPAIR
**Substantive findings changed:** no
**Independence boundary changed:** no
**Architecture result changed:** no

## Correct provenance

The Claude work for MC-0028 was performed in the newly opened persistent Claude conversation:

    interaction session   claude-04
    conversation title    04 - Assurance and Delivery Architecture Design

The original MC-0028 coordination files incorrectly carried forward claude-03 and the prior conversation title when the thread was opened.

MC-0028 Message 001 then correctly stated that it had been produced in a new Claude chat with no carried conversation context and that the visible title had changed from 03 to 04. However, because the thread STATE file already said claude-03 and Claude's write scope excluded STATE, Message 001 preserved claude-03 as a supposed thread participant slot.

That participant-slot distinction was not part of the accepted interaction-provenance convention. It was a workaround around the already-wrong coordination metadata.

The governing convention in docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md says that a newly opened persistent conversation is a new provider-local interaction session and must not reuse the prior session ID. Therefore the correct MC-0028 Claude interaction session is claude-04.

The original Claude-authored Message 001 and Message 003 remain unchanged as historical collaborator evidence. Their claude-03 (thread participant slot) provenance line is superseded by this correction for provenance interpretation only. Their substantive reasoning, evidence, independence claims and conclusions are unchanged.

Git history preserves the original mistaken coordination metadata and the original collaborator messages.

## Downstream consequence

MC-0029 continues in the same Claude conversation, so its correct Claude interaction provenance is also:

    interaction session   claude-04
    conversation title    04 - Assurance and Delivery Architecture Design
