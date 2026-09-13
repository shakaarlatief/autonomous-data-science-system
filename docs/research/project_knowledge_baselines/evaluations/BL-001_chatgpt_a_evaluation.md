# BL-001 ChatGPT A Evaluation

**Date evaluated:** 2026-09-13
**Scenario:** BL-001
**Environment:** ChatGPT
**Result commit:** `edc4cbf211f61b68cce2952c0902b178fa8864cc`
**Frozen evidence snapshot:** `a570f0d87b77960ae0715b291de0d5f6e884e4d0`
**Result artifact:** `docs/research/project_knowledge_baselines/results/BL-001_chatgpt_a.md`
**Historical parent:** `KF-SD-01`
**Evaluation status:** USABLE WITH RESULT-RECEIPT DEFECT

## 1. Protocol integrity

The result commit changed exactly one allowed result path. The project owner separately reported that the factual evidence boundary remained the frozen snapshot and that forbidden evaluator/current-Research-124 material was not read.

The result artifact itself does **not** contain the required structured receipt fields for:

```text
snapshot access method
sources materially consulted
read/access failures
uncertainty / areas not checked
approximate tool/read effort
```

Therefore source-use and effort claims cannot be fully reconstructed from the result artifact alone. This is a protocol defect, but it does not invalidate the substantive answer because the commit/write isolation is clean and the answer itself contains snapshot-specific evidence that permits bounded evaluation.

Do not amend the trial result after evaluation. The missing receipt remains part of the baseline evidence.

## 2. Core scenario finding

The original historical failure was:

```text
correct OPERATIONS authority existed
    +
restart task required exact ordered guidance
    ->
governing procedure was not consumed before advice
```

BL-001 does **not** reproduce that exact dispatch failure.

The fresh ChatGPT answer explicitly identifies:

```text
docs/local_execution/OPERATIONS.md
```

as the restart authority, says not to reconstruct startup from chat memory, and includes several details that are specific to the frozen runbook, including port `7690`, preservation of the tunnel Git Bash shell, local/private tunnel variables, health/readiness checks and downstream developer-MCP refresh behavior. This is strong evidence that the governing operational source was discovered and materially consumed.

However, the user task asked for the **exact order** to execute the controlled restart/reconnect. The answer never actually reproduces the frozen runbook's governing full sequence:

```text
1. stop tunnel-client, keep its Git Bash shell open
2. stop Codexless HTTP
3. restart Codexless
4. verify Codexless /healthz + expected toolCount
5. confirm tunnel variables are SET without printing values
6. optionally run tunnel doctor when reconfirmation is needed
7. start tunnel-client
8. verify tunnel /healthz = 200
9. verify tunnel /readyz = 200
10. only then refresh ChatGPT developer MCP if the tool surface changed
11. perform fresh read-only discovery before invoking a newly added mutation tool
```

Instead, it gives a broad eight-point project reconstruction/continuation answer and refers generically to `restart/reconnect through the controlled runbook`.

So the observed mechanism is different from KF-SD-01:

```text
situation recognition             succeeded
source discovery                  succeeded
source consumption                materially succeeded
exact task-output fidelity         failed / incomplete
context narrowing                 weak
```

This is important: merely activating the right source does not guarantee that the final answer faithfully emits the exact action contract requested by the user.

## 3. Frozen qualitative scoring

### S1 — task/situation recognition: PASS

The answer correctly recognizes this as a project-governed operational restart/reconnect task rather than answering from generic service-restart knowledge.

### S2 — governing-source discovery: PASS

`docs/local_execution/OPERATIONS.md` is explicitly identified as the relevant operational authority.

### S3 — governing-source consumption: PASS WITH EVIDENCE LIMIT

The answer contains multiple details strongly indicating material consumption of the runbook rather than filename-only discovery. The missing source receipt prevents independent reconstruction of the exact read path, so this PASS carries an observability limitation.

### S4 — authority/source-strength selection: PASS

The answer treats the evergreen operations runbook and frozen current-state/checkpoint boundary as stronger than chat memory and historical superseded instructions.

### S5 — final task correctness / fidelity: FAIL

The user explicitly requested the exact order to follow. The response does not provide the governing full controlled restart sequence and therefore does not satisfy the central output requirement despite finding the right source.

The failure is primarily an **answer-extraction / task-fidelity failure after source activation**, not the original governing-authority activation failure.

### S6 — uncertainty calibration: PARTIAL

The answer distinguishes current versus superseded guidance and correctly conditions some refresh steps. But it does not acknowledge that it has omitted the exact ordered restart sequence while still presenting itself as the requested execution guidance.

### S7 — broad-vs-narrow context appropriateness: PARTIAL

The answer reconstructs substantial unrelated project context, including Research 117 continuation, Source Vault status, semantic-Git authority and secret-storage semantics. Some context is relevant to the frozen boundary, but much of it is not necessary to answer the narrow restart-order task.

### S8 — read/tool cost and irrelevant-context burden: PARTIAL

The required effort receipt is missing, so direct tool/read cost is not observable. The final answer nevertheless shows a broad reconstruction burden substantially larger than the narrow operational task required.

## 4. Failure attribution

```text
snapshot/source absence             NO
navigation/discoverability failure  NO
task/situation dispatch failure     NO
authority-resolution failure        NO
source-consumed reasoning failure   YES, specifically exact task-output fidelity
uncertainty/calibration failure      PARTIAL
context-allocation inefficiency      YES / MATERIAL
protocol receipt defect              YES
```

## 5. Research 124 implication

BL-001 weakens the simple hypothesis that the historical restart problem is purely an inability to route to governing authority under the frozen architecture. A fresh ChatGPT can discover and materially consume the correct runbook when explicitly asked for exact project-governed restart guidance.

But BL-001 simultaneously exposes a different weakness:

> **Governing-source activation is necessary but not sufficient. The reasoning/output path must preserve the exact task-relevant contract from the source instead of broadening into project reconstruction and then gesturing back to the runbook.**

This suggests future qualification needs to distinguish at least:

```text
source activation
contract extraction
answer/task fidelity
context discipline
```

rather than treating `right file was read` as complete success.

## 6. Replicate decision

No immediate repeat is required. The core result is not borderline:

```text
right governing source activated        clear
exact ordered answer omitted             clear
```

A targeted second replicate may still be justified later if the four-scenario pilot shows that answer-fidelity behavior is unstable across otherwise similar cases, but BL-001 does not currently block progression to BL-002.

```text
BL001_CHATGPT_A=USABLE_WITH_RECEIPT_DEFECT
S1=PASS
S2=PASS
S3=PASS_WITH_OBSERVABILITY_LIMIT
S4=PASS
S5=FAIL
S6=PARTIAL
S7=PARTIAL
S8=PARTIAL
HISTORICAL_DISPATCH_FAILURE_REPRODUCED=false
NEW_POST_ACTIVATION_TASK_FIDELITY_FAILURE=observed
IMMEDIATE_REPLICATE=NO
NEXT=BL-002_CHATGPT_A
```