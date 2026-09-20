# MC-0020 Thread: W5 T1 V0.2 Blind Subject-Placement Calibration

**Thread:** MC-0020
**Status:** RESOLVED / T1 ACCEPTED / FULL W5 RECONCILIATION NEXT
**Review mode:** INDEPENDENT / BLIND PLACEMENT CALIBRATION
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Exact reviewer-fixture target:** `f4308cc74b6d44640f399b6e9c102473382232df`
**Exact source-corpus boundary:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`
**Task owner:** ChatGPT / `chatgpt-27`
**Reviewer control:** fresh Claude Opus conversation

## Purpose

Repeat the same 24-carrier blind calibration used by MC-0019 against the refined V0.2 subject vocabulary so the project can measure whether definitions, membership admission rules and the new admissibility-authority subject improve inter-reviewer consistency.

## Independence contract

Claude receives only the blind reviewer catalog projection, the reviewer subset and the exact source carriers. It must not read V0.2 ChatGPT annotations/results, V0.1 calibration material, prior MC-0019 messages, legacy Knowledge Map routing or later interpretation before freezing Message 001.

## Expected sequence

```text
001  Claude Opus V0.2 blind subject placement
002  ChatGPT controlled V0.1/V0.2 comparison and final T1 disposition
```

## Write ownership

Claude may write only under `docs/model_collaboration/threads/MC-0020/messages/**`. ChatGPT remains task owner/integrator.

```text
MC0020=RESOLVED
MESSAGE_001=CLAUDE_COMPLETE
MESSAGE_002=CHATGPT_COMPLETE
T1=ACCEPTED
NEXT=FINAL_W5_INFORMATION_ARCHITECTURE_RECONCILIATION
```
