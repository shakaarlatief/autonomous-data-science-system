# Checkpoint 17: Duplicate Structured Output Normalization

**Date:** 2026-08-08  
**Stage:** Prototype V0 real-model calibration  
**Scope:** Second provider-interface diagnostic before any behavior-evaluable B0 run

## Why this checkpoint exists

The second attempted real B0 calibration, `dev-b0-02`, again terminated before one successful treatment command entered the common runtime. Unlike the first attempt, the provider response itself completed successfully and the improved accounting from Checkpoint 16 preserved enough information to diagnose the actual failure.

This checkpoint records that diagnosis, the condition-neutral adapter repair, and the experimental consequence: neither `dev-b0-01` nor `dev-b0-02` is evidence about B0's methodological behavior.

## Observed `dev-b0-02` result

The run summary was:

```text
condition: B0
completed: false
successful model calls: 0
generation attempts: 1
generation failures: 1
behavior_evaluable: false
input tokens: 1107
output tokens: 130
total tokens: 1237
terminal error: invalid_json
```

The provider metadata showed:

```text
response status: completed
reasoning effort: high
reasoning tokens: 41
max output tokens: 30000
```

This falsified the immediate hypothesis that the 30,000-token ceiling was still preventing the first structured command. The provider used only a small fraction of that ceiling and marked the response `completed`.

## Retrieval of the stored response

Because calibration uses `store=True`, the response could be retrieved by its recorded response ID without issuing another generation request.

The retrieved response contained two assistant message items. Each message contained the same independently valid strict-JSON command:

```json
{
  "rationale": "I need to identify the available documentation and data artifacts before assessing the task or modeling plan.",
  "command": {
    "type": "list_artifacts"
  }
}
```

The output sequence contained reasoning items around those two message items, but the two visible structured commands were semantically identical.

The OpenAI Python SDK `Response.output_text` convenience property aggregates every `output_text` block across message output items by concatenating their text. Therefore the property for this response became conceptually:

```text
{valid JSON object}{the same valid JSON object}
```

That concatenated string is not one valid JSON document, which is why the adapter's previous `json.loads(response.output_text)` call raised `JSONDecodeError` even though each individual structured-output block was valid.

The current SDK source documents `output` as a variable-length list whose contents depend on the model response, and its `output_text` property explicitly joins all message-level output-text blocks. Therefore assuming that the aggregate helper always represents exactly one JSON document is too strong for this experiment.

Relevant upstream references:

- OpenAI Python SDK `Response.output_text` implementation: https://github.com/openai/openai-python/blob/main/src/openai/types/responses/response.py
- OpenAI Python SDK structured-output parsing example: https://github.com/openai/openai-python/blob/main/examples/responses/structured_outputs.py

## Experimental interpretation

`dev-b0-02` is an infrastructure/provider-normalization diagnostic, not a B0 behavioral trajectory.

The model did produce a legitimate first action: `list_artifacts`. However, the experiment runner never accepted that action because the provider adapter incorrectly interpreted an aggregate convenience property as one JSON document.

Scoring this as a B0 methodological failure would therefore confound provider-response normalization with treatment behavior.

The run remains useful calibration evidence because it exposed a common-interface assumption before P0 exists.

## Condition-neutral normalization rule

The OpenAI adapter now normalizes completed structured responses conservatively:

```text
1. Extract non-empty output_text blocks from assistant message items.
2. If their aggregate is valid JSON, use that aggregate normally.
3. If the aggregate is invalid, parse message-level blocks independently.
4. Accept multiple blocks only when every block is valid JSON and all parsed payloads are semantically equal.
5. Collapse those duplicate-equal blocks into one provider-neutral ModelGeneration.
6. If multiple valid blocks encode different commands, reject the response as ambiguous.
7. If blocks are absent or malformed, preserve the existing empty/invalid-output failure semantics.
```

The adapter does not choose a first or last command when distinct commands are present. Doing so would introduce an arbitrary semantic decision into provider normalization.

This rule applies equally to B0, B1, and future P0 and therefore does not advantage one experimental condition.

## New observability

Provider metadata now records:

```text
output_text_block_count
distinct_output_text_block_count
duplicate_identical_output_blocks_collapsed
structured_output_source
```

If normalization cannot safely produce one command, the error metadata records the failure class, including `ambiguous_structured_output` for multiple distinct valid commands.

This lets later calibration distinguish ordinary one-block responses from provider responses that required a semantics-preserving normalization step.

## Regression tests

Two adapter tests were added:

1. two identical valid structured command blocks are collapsed into one command and explicitly marked in provider metadata;
2. two different valid structured command blocks are rejected as ambiguous rather than silently selecting one.

The full GitHub Actions suite after the repair passed:

```text
25 passed in 8.30s
```

The benchmark regenerated successfully with unchanged self-test metrics.

## What was deliberately not changed

The following experimental settings remain unchanged:

```text
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 20
max output tokens per call: 30000
max additional generation retries: 2
strict Structured Outputs
previous_response_id continuation
all-turn reasoning context
```

Changing model, reasoning effort, and provider normalization simultaneously would make the next result harder to interpret. The second diagnostic shows that the 30,000-token ceiling was not the cause of `dev-b0-02`, so there is no evidence-based reason to increase it again at this point.

## Experimental status after Checkpoint 17

The real-model calibration record is now:

```text
dev-b0-01
  provider response incomplete: max_output_tokens
  zero successful commands
  not behavior-evaluable

dev-b0-02
  provider response completed
  duplicate identical structured message blocks
  aggregate SDK output_text was invalid as one JSON document
  zero commands accepted by old adapter
  not behavior-evaluable
```

No genuine B0 methodological trajectory has yet been observed.

P0 therefore remains intentionally unimplemented.

## Next valid action

Pull the condition-neutral normalization repair, run the local test suite, and execute a fresh B0 calibration under the same common settings using a new run ID such as `dev-b0-03`.

If that run successfully enters the treatment command loop, it becomes the first candidate behavior-evaluable B0 trajectory. If another shared provider/interface defect appears, repair it condition-neutrally before running B1 or implementing P0.