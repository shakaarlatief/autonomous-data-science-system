# MC-0019 Thread: W5 T1 Blind Subject-Placement Calibration

**Thread:** MC-0019
**Status:** OPEN / CLAUDE MESSAGE 001 NEXT
**Review mode:** INDEPENDENT / BLIND PLACEMENT CALIBRATION
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Exact reviewer-fixture target:** `dcd01d865340c0d562c07f68307ef0a2c7ee2d75`
**Exact source-corpus boundary:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`
**Task owner:** ChatGPT / `chatgpt-27`

## Purpose

Measure whether a second capable model can apply the frozen W5 T1 semantic-subject vocabulary consistently to a representative blind subset before the project freezes any production subject schema.

## Independence contract

Claude receives the candidate vocabulary, the reviewer subset and the exact source carriers. It must not read ChatGPT's candidate annotations, scenarios, generated T1 outputs, legacy Knowledge Map routing or later interpretation before freezing Message 001.

This is independence with respect to placement labels, not independence from the broader ADS architecture context.

## Expected sequence

```text
001  Claude blind subject placement
002  ChatGPT comparison, construct-validity interpretation and T1 disposition
```

## Write ownership

Claude may write only under `docs/model_collaboration/threads/MC-0019/messages/**`. ChatGPT remains task owner/integrator.

```text
MC0019=OPEN
NEXT=CLAUDE_MESSAGE_001
```
