# Bound active-writer combined live test blocked by platform safety

**Date:** 2026-09-02
**Status:** `BLOCKED_BY_PLATFORM_SAFETY / COMBINED_LIVE_DISCRIMINANT_INCOMPLETE`
**Scope:** Preserve the final planned live discriminant for the durable thread-bind design, in which Codex Desktop deliberately retained writer ownership while ChatGPT attempted a non-owning bind followed by a conflicting send.
**Authority:** Negative platform-dispatch evidence only. This record is neither a PASS nor a FAIL of `codex.agent_bind` or the Codex active-writer contract because the Step 1 call did not reach Codexless.

## Planned discriminator

The intended sequence was:

```text
Desktop owns exact persisted thread
-> codex.agent_bind succeeds without taking writer ownership
-> codex.agent_send attempts thread/resume
-> App Server rejects with active-writer conflict
-> no turn/accepted or turn/started
-> Desktop-owned thread remains uninterrupted
```

This would have combined the already verified non-owning bind behavior with the already observed Codex active-writer rejection in one final real end-to-end test.

## Actual result

The platform safety layer blocked Step 1 before the Codexless bridge executed it. The returned result was:

```text
Deze toolaanroep is geblokkeerd door de veiligheidscontroles van OpenAI. Controleer nogmaals wat je verzendt.
```

Consequences:

```text
Step 1 bind result             none
fresh agentRef                 none
Codexless execution            none
thread resume                  not attempted
Call Codex card                none
Codex model turn               none
turn/accepted                  none from this attempt
turn/started                   none from this attempt
retry/workaround               deliberately not attempted
```

The experiment therefore failed closed at the outer platform layer.

## Related evidence that remains valid

This blocked combined test does not erase earlier evidence:

```text
live uncontested codex.agent_bind                         PASS
live restart/rebind with same durable threadId            PASS
live same-thread bound send after Desktop full quit       PASS
deterministic active-writer rejection/no-turn regression PASS
earlier real thread/resume while Desktop owned writer    rejected as already having an active writer
```

The only missing evidence is the new full live combination of Desktop ownership + new `codex.agent_bind` + conflicting bound send.

## Classification

```text
new combined live active-writer discriminant  INCOMPLETE
reason                                          BLOCKED_BY_PLATFORM_SAFETY
implementation failure                          NOT ESTABLISHED
Codexless failure                                NOT ESTABLISHED
Codex active-writer failure                      NOT ESTABLISHED
workaround/evasion                               NOT ATTEMPTED
```

The correct continuation is to preserve the block and move to supported cooperative-release investigation rather than rephrasing or wrapping the same blocked experiment.
