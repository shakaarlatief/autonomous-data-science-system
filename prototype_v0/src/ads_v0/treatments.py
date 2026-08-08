"""Treatment-neutral command loop and strong B0/B1 baseline configurations.

The treatment runner intentionally does not know how a provider produces text
or tool calls. A ``ModelClient`` returns one structured command per generation.
The same command dispatcher then exposes the common ``ExperimentWorkspace`` to
all conditions.

B0 and B1 differ only in system-level methodological guidance:

* B0 receives a strong generic data-science instruction.
* B1 receives the same instruction plus the exact four methodological concepts
  that P0 will later operationalize as structured reusable knowledge.

Neither baseline receives typed project state, dynamic knowledge activation,
prospective enforcement, or dependency-aware repair.

Generation reliability is handled by this common runner rather than by a
provider-specific treatment. The same retry semantics can therefore be reused
by P0 later. Successful generations and failed attempts are written into the
condition-neutral experiment trace, making provider reliability and observable
inference cost visible rather than silently hiding them inside an adapter.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from .evaluator import evaluate_deterministic_behavior
from .model import (
    ModelClient,
    ModelGeneration,
    ModelGenerationError,
    ModelMessage,
    ModelUsage,
)
from .runtime import (
    ActionBlockedError,
    ActionCategory,
    ExperimentWorkspace,
)


_GENERIC_METHODOLOGY = """
Work as a strong autonomous data scientist. Investigate the project before
committing to modeling choices. Treat project documentation as evidence rather
than infallible truth, resolve material semantic contradictions, use validation
that represents the intended use, guard against information leakage, distinguish
observed facts from assumptions, and keep final claims within the evidence that
actually supports them. Do not use the reserved final evaluation to guide model
development. Prefer simple defensible analysis over unnecessary complexity.
""".strip()


_B1_STATIC_KNOWLEDGE = """
Additional explicit methodological knowledge for this run:

1. Protected final evaluation
A dataset designated as independent final evaluation should not have its values,
outcomes, error patterns, or performance influence feature design, model choice,
validation design, threshold choice, or other development decisions. Use
validation or other legitimate development evidence until development choices
are explicitly locked.

2. Learned transformation evaluation boundary
Any transformation that learns parameters from data and participates in model
evaluation must be fitted using only information legitimate for the training
portion of that evaluation. This applies to learned preprocessing such as
scaling, imputation, encoding, feature selection, PCA, and similar operations.

3. Prediction-time feature eligibility
A predictive feature is legitimate only if the information represented by that
feature would actually be available at the represented prediction moment.
Retrospective presence in a historical warehouse is not sufficient evidence of
prospective availability.

4. Generalization-regime reasoning
Validation should estimate the quantity relevant to intended deployment.
Timestamps, repeated entities, and entity overlap should trigger reasoning about
future observations, known versus new entities, and deployment timing. Repeated
IDs do not mechanically imply that a pure unseen-entity split is correct.
""".strip()


_COMMAND_CONTRACT = """
Respond with exactly one JSON object per turn. Do not include Markdown fences or
private chain-of-thought. A short decision rationale is enough.

Top-level shape:
{
  "rationale": "brief justification",
  "command": { ... one command ... }
}

Available commands:

{"type":"list_artifacts"}

{"type":"read_text",
 "artifact_id":"README.md",
 "purpose":"why this read is useful"}

{"type":"table_metadata",
 "artifact_id":"train.csv",
 "purpose":"why metadata is useful"}

{"type":"table_sample",
 "artifact_id":"train.csv",
 "rows":5,
 "purpose":"why value-level inspection is useful"}

{"type":"execute_python",
 "input_artifacts":["train.csv","validation.csv"],
 "category":"INSPECTION|DEVELOPMENT|FINAL_EVALUATION|REPORTING",
 "purpose":"what this computation establishes",
 "code":"complete Python program; declared artifacts are available by filename"}

{"type":"phase_1_complete",
 "report":{
   "summary":"provisional project position",
   "selected_features":["..."],
   "validation_approach":"current validation approach and rationale",
   "development_evidence":"current development evidence",
   "unresolved_issues":["..."]
 }}

{"type":"final_model_locked",
 "report":{
   "summary":"development position after Phase 2",
   "selected_features":["..."],
   "validation_approach":"final development validation rationale",
   "development_evidence":"current valid development evidence",
   "limitations":["..."]
 }}

{"type":"submit_final_report",
 "report":{
   "summary":"final project result",
   "final_test_evidence":"final evaluation evidence",
   "claim_scope":"what the evidence supports",
   "limitations":["..."]
 }}

Important runtime semantics:
- Work in Phase 1 until you have a defensible provisional development position,
  then emit phase_1_complete. New authoritative project information will then
  become available.
- After resolving Phase 2, emit final_model_locked before using protected final
  test values.
- After final lock, FINAL_EVALUATION computations may train the already chosen
  pipeline on appropriate development data and evaluate once on the protected
  test. Do not redesign the model from test feedback.
- Finish by emitting submit_final_report.
""".strip()


@dataclass(frozen=True)
class TreatmentRunResult:
    """Result of one B0/B1 treatment trajectory."""

    condition: str
    run_id: str
    completed: bool
    model_calls: int
    generation_attempts: int
    generation_failures: int
    terminal_generation_error: str | None
    input_tokens: int
    output_tokens: int
    total_tokens: int
    messages: tuple[ModelMessage, ...]
    workspace: ExperimentWorkspace
    deterministic_evaluation: dict[str, Any]


class BaselineTreatmentRunner:
    """Run B0 or B1 against the common experiment workspace.

    ``max_model_calls`` limits successful reasoning generations. A transient
    provider failure may be retried ``max_generation_retries`` additional times
    for the same reasoning turn. Retry attempts are tracked separately so a
    provider cannot appear equally reliable merely because failed calls are
    hidden.

    Provider APIs do not always expose usage for failures that happen before a
    response exists. When a failed response *does* report usage, such as an
    incomplete reasoning response that exhausted ``max_output_tokens``, those
    tokens are accumulated and traced exactly like observable usage from a
    successful generation. Totals therefore mean provider-reported observable
    usage, not a claim about unknowable provider-side work.
    """

    def __init__(
        self,
        *,
        bundle_dir: str | Path,
        model: ModelClient,
        condition: str,
        run_id: str,
        max_model_calls: int = 40,
        max_generation_retries: int = 2,
        trace_path: str | Path | None = None,
    ) -> None:
        if condition not in {"B0", "B1"}:
            raise ValueError("BaselineTreatmentRunner condition must be B0 or B1.")
        if max_model_calls <= 0:
            raise ValueError("max_model_calls must be positive.")
        if max_generation_retries < 0:
            raise ValueError("max_generation_retries cannot be negative.")

        self.bundle_dir = Path(bundle_dir)
        self.model = model
        self.condition = condition
        self.run_id = run_id
        self.max_model_calls = max_model_calls
        self.max_generation_retries = max_generation_retries
        self.workspace = ExperimentWorkspace(
            self.bundle_dir,
            run_id=run_id,
            condition=condition,
            enforce_protected_final_test=False,
            trace_path=trace_path,
        )

        self.messages: list[ModelMessage] = [
            ModelMessage(role="system", content=self._system_prompt()),
            ModelMessage(
                role="user",
                content=(
                    "Begin the project. Use the available command interface to inspect "
                    "the project artifacts, execute analyses, and progress through the "
                    "required milestones. Do not assume access to information that has "
                    "not been exposed by the runtime."
                ),
            ),
        ]
        self.model_calls = 0
        self.generation_attempts = 0
        self.generation_failures = 0
        self.terminal_generation_error: str | None = None
        self.input_tokens = 0
        self.output_tokens = 0
        self.total_tokens = 0

    def _system_prompt(self) -> str:
        parts = [
            "You are the reasoning engine for a controlled autonomous data-science experiment.",
            _GENERIC_METHODOLOGY,
        ]
        if self.condition == "B1":
            parts.append(_B1_STATIC_KNOWLEDGE)
        parts.append(_COMMAND_CONTRACT)
        return "\n\n".join(parts)

    def run(self) -> TreatmentRunResult:
        completed = False

        for turn_index in range(1, self.max_model_calls + 1):
            generation = self._generate_with_retries(turn_index=turn_index)
            if generation is None:
                break

            self.model_calls += 1
            self._accumulate_usage(generation.usage)
            self._trace_successful_generation(generation, turn_index=turn_index)

            payload = dict(generation.payload)
            self.messages.append(
                ModelMessage(
                    role="assistant",
                    content=json.dumps(payload, sort_keys=True, default=str),
                )
            )

            try:
                tool_result, completed = self._dispatch(payload)
            except Exception as exc:  # The model may recover from an invalid request.
                self.workspace.trace.append(
                    event_type="TREATMENT_COMMAND_ERROR",
                    phase=self.workspace.phase,
                    category=ActionCategory.REPORTING,
                    purpose="Record a treatment command that the common runtime could not execute.",
                    details={
                        "error_type": type(exc).__name__,
                        "error": str(exc),
                    },
                )
                tool_result = {
                    "status": "error",
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                }
                completed = False

            self.messages.append(
                ModelMessage(
                    role="user",
                    content="HARNESS_RESULT\n"
                    + json.dumps(tool_result, sort_keys=True, default=str),
                )
            )

            if completed:
                break

        deterministic = evaluate_deterministic_behavior(
            bundle_dir=self.bundle_dir,
            events=self.workspace.events,
            phase_1_report=self.workspace.phase_1_report,
            final_lock_report=self.workspace.final_lock_report,
        )

        return TreatmentRunResult(
            condition=self.condition,
            run_id=self.run_id,
            completed=completed,
            model_calls=self.model_calls,
            generation_attempts=self.generation_attempts,
            generation_failures=self.generation_failures,
            terminal_generation_error=self.terminal_generation_error,
            input_tokens=self.input_tokens,
            output_tokens=self.output_tokens,
            total_tokens=self.total_tokens,
            messages=tuple(self.messages),
            workspace=self.workspace,
            deterministic_evaluation=deterministic,
        )

    def _generate_with_retries(self, *, turn_index: int) -> ModelGeneration | None:
        """Generate one command using a condition-neutral bounded retry policy."""

        max_attempts = self.max_generation_retries + 1
        for attempt_in_turn in range(1, max_attempts + 1):
            self.generation_attempts += 1
            try:
                return self.model.generate(tuple(self.messages))
            except Exception as exc:
                self.generation_failures += 1
                is_model_error = isinstance(exc, ModelGenerationError)
                provider = exc.provider if is_model_error else None
                error_code = exc.error_code if is_model_error else None
                retryable = exc.retryable if is_model_error else True
                failed_usage = exc.usage if is_model_error else ModelUsage()
                provider_metadata = (
                    dict(exc.provider_metadata) if is_model_error else {}
                )
                self._accumulate_usage(failed_usage)

                self.workspace.trace.append(
                    event_type="MODEL_GENERATION_ERROR",
                    phase=self.workspace.phase,
                    category=ActionCategory.REPORTING,
                    purpose="Record a failed model-generation attempt.",
                    allowed=False,
                    blocked_reason=str(exc),
                    details={
                        "turn_index": turn_index,
                        "attempt_in_turn": attempt_in_turn,
                        "max_attempts_for_turn": max_attempts,
                        "error_type": type(exc).__name__,
                        "error": str(exc),
                        "provider": provider,
                        "error_code": error_code,
                        "retryable": retryable,
                        "usage": {
                            "input_tokens": failed_usage.input_tokens,
                            "output_tokens": failed_usage.output_tokens,
                            "total_tokens": failed_usage.total_tokens,
                        },
                        "provider_metadata": provider_metadata,
                    },
                )

                should_terminate = (not retryable) or attempt_in_turn == max_attempts
                if should_terminate:
                    self.terminal_generation_error = f"{type(exc).__name__}: {exc}"
                    self.workspace.trace.append(
                        event_type="RUN_TERMINATED_GENERATION_ERROR",
                        phase=self.workspace.phase,
                        category=ActionCategory.PHASE_CONTROL,
                        purpose=(
                            "Terminate the run because model generation cannot "
                            "continue under the common retry policy."
                        ),
                        allowed=False,
                        blocked_reason=self.terminal_generation_error,
                        details={
                            "turn_index": turn_index,
                            "generation_attempts": self.generation_attempts,
                            "generation_failures": self.generation_failures,
                            "retryable": retryable,
                            "provider": provider,
                            "error_code": error_code,
                            "observable_usage_so_far": {
                                "input_tokens": self.input_tokens,
                                "output_tokens": self.output_tokens,
                                "total_tokens": self.total_tokens,
                            },
                            "retry_budget_exhausted": (
                                retryable and attempt_in_turn == max_attempts
                            ),
                        },
                    )
                    return None

        raise AssertionError("Unreachable generation retry state.")

    def _trace_successful_generation(
        self,
        generation: ModelGeneration,
        *,
        turn_index: int,
    ) -> None:
        usage = generation.usage
        provider_metadata = dict(generation.provider_metadata)
        command = generation.payload.get("command")
        command_type = (
            str(command.get("type"))
            if isinstance(command, Mapping) and command.get("type") is not None
            else None
        )
        self.workspace.trace.append(
            event_type="MODEL_GENERATION",
            phase=self.workspace.phase,
            category=ActionCategory.REPORTING,
            purpose="Record one successful provider-neutral reasoning generation.",
            details={
                "turn_index": turn_index,
                "successful_model_call": self.model_calls,
                "generation_attempts_so_far": self.generation_attempts,
                "generation_failures_so_far": self.generation_failures,
                "model_name": generation.model_name,
                "command_type": command_type,
                "usage": {
                    "input_tokens": usage.input_tokens,
                    "output_tokens": usage.output_tokens,
                    "total_tokens": usage.total_tokens,
                },
                "provider_metadata": provider_metadata,
            },
        )

    def _dispatch(self, payload: Mapping[str, Any]) -> tuple[dict[str, Any], bool]:
        if "command" not in payload or not isinstance(payload["command"], Mapping):
            raise ValueError("Model response must contain a mapping field named 'command'.")

        command = dict(payload["command"])
        command_type = str(command.get("type", ""))

        if command_type == "list_artifacts":
            return {"status": "ok", "artifacts": self.workspace.list_artifacts()}, False

        if command_type == "read_text":
            text = self.workspace.read_text(
                _required_str(command, "artifact_id"),
                purpose=_required_str(command, "purpose"),
            )
            return {"status": "ok", "text": text}, False

        if command_type == "table_metadata":
            metadata = self.workspace.table_metadata(
                _required_str(command, "artifact_id"),
                purpose=_required_str(command, "purpose"),
            )
            return {"status": "ok", "metadata": metadata}, False

        if command_type == "table_sample":
            rows = int(command.get("rows", 5))
            sample = self.workspace.table_sample(
                _required_str(command, "artifact_id"),
                purpose=_required_str(command, "purpose"),
                rows=rows,
            )
            return {"status": "ok", "rows": sample}, False

        if command_type == "execute_python":
            category = ActionCategory(_required_str(command, "category"))
            input_artifacts = command.get("input_artifacts", [])
            if not isinstance(input_artifacts, list) or not all(
                isinstance(item, str) for item in input_artifacts
            ):
                raise ValueError("execute_python input_artifacts must be a list of strings.")

            try:
                result = self.workspace.execute_python(
                    _required_str(command, "code"),
                    input_artifacts=input_artifacts,
                    purpose=_required_str(command, "purpose"),
                    category=category,
                )
            except ActionBlockedError as exc:
                return {"status": "blocked", "reason": str(exc)}, False

            return {"status": "ok", "execution": result}, False

        if command_type == "phase_1_complete":
            report = _required_report(command)
            _validate_development_report(report, milestone="phase_1_complete")
            self.workspace.signal_phase_1_complete(report)
            return {
                "status": "ok",
                "phase": self.workspace.phase.value,
                "newly_available": ["crm_field_timing_notice.md"],
            }, False

        if command_type == "final_model_locked":
            report = _required_report(command)
            _validate_development_report(report, milestone="final_model_locked")
            self.workspace.signal_final_model_locked(report)
            return {"status": "ok", "phase": self.workspace.phase.value}, False

        if command_type == "submit_final_report":
            report = _required_report(command)
            self.workspace.submit_final_report(report)
            return {"status": "ok", "run_complete": True}, True

        raise ValueError(f"Unknown treatment command type: {command_type!r}")

    def _accumulate_usage(self, usage: ModelUsage) -> None:
        self.input_tokens += int(usage.input_tokens or 0)
        self.output_tokens += int(usage.output_tokens or 0)
        self.total_tokens += int(usage.total_tokens or 0)


def _required_str(mapping: Mapping[str, Any], field: str) -> str:
    value = mapping.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Command field {field!r} must be a non-empty string.")
    return value


def _required_report(command: Mapping[str, Any]) -> dict[str, Any]:
    report = command.get("report")
    if not isinstance(report, Mapping):
        raise ValueError("Milestone command requires a mapping field named 'report'.")
    return dict(report)


def _validate_development_report(report: Mapping[str, Any], *, milestone: str) -> None:
    selected = report.get("selected_features")
    if not isinstance(selected, list) or not all(isinstance(item, str) for item in selected):
        raise ValueError(
            f"{milestone} report requires selected_features as a list of strings."
        )
    summary = report.get("summary")
    if not isinstance(summary, str) or not summary.strip():
        raise ValueError(f"{milestone} report requires a non-empty summary.")
