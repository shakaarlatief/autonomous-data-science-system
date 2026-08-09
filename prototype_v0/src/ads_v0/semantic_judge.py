"""Condition-blinded semantic evaluation for Prototype V0 trajectories.

This module implements the primary semantic-judge procedure preregistered in
Foundation 012. The judge receives only condition-neutral external evidence:

* hidden evaluator truth and acceptance-contract material;
* the treatment's externally visible command/rationale trajectory;
* visible harness results returned for those commands; and
* common milestone reports.

Treatment system prompts, condition labels, run identifiers, provider metadata,
and future P0-only internal state are intentionally excluded from the primary
semantic packet. P0 architecture diagnostics can be evaluated separately, but
cannot improve the common semantic score merely by existing.

Each behavior-evaluable trajectory receives two fresh independent judge calls.
The two passes are combined mechanically according to the registered rules:
exact agreement is retained, adjacent score disagreement is averaged, and an
extreme 0-versus-2 disagreement or semantic-critical-flag disagreement requires
manual condition-blinded adjudication.

The semantic judge is deliberately separate from the treatment-model adapter.
It uses the same registered model family and reasoning effort, but does not use
``previous_response_id`` or share judge-call state across passes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Mapping, Sequence

from .model import ModelGenerationError, ModelUsage
from .openai_model import (
    _classify_openai_exception,
    _parse_structured_response_payload,
    _safe_openai_error_message,
    _usage_from_response,
)


CRITERION_IDS = tuple(f"S{i}" for i in range(1, 11))
TARGETED_CRITERIA = ("S1", "S2", "S3", "S6", "S7")
SEMANTIC_CRITICAL_IDS = ("SC1", "SC2")

RUBRIC_TEXT = r"""
Use the following anchored 0/1/2 rubric exactly.

S1 Row-unit correction
0: stale one-row-per-entity interpretation remains consequentially accepted,
   or row semantics are used incorrectly downstream.
1: repeated entity-period snapshots are operationally inferred and used
   correctly, but the contradiction is not explicitly resolved as a durable
   project conclusion.
2: stale documentation is explicitly resolved, the actual entity-period
   observation unit is stated, and that interpretation is used consistently.

S2 Validation/generalization reasoning
0: validation is incompatible with the future-facing deployment regime, or
   repeated entities trigger an unjustified mechanical split rule.
1: defensible temporal evaluation is used, but deployment/entity reasoning is
   partial or implicit.
2: validation is explicitly related to future deployment, timestamps, repeated
   entities, and the mixture of continuing and newly observed entities.

S3 Inherited preprocessing contamination
0: contaminated inherited validation evidence is treated as clean comparative
   evidence, or the learned-transformation violation is reproduced.
1: the treatment avoids relying on contaminated inherited evidence and uses
   legitimate preprocessing, but does not explicitly diagnose the inherited
   evidence-boundary violation.
2: the treatment explicitly identifies the learned-transformation boundary
   violation and retires or repairs the inherited evidence accordingly.

S4 Prediction-time feature eligibility before Phase 2
0: an unjustified timing claim is made, the feature is accepted/rejected for the
   wrong reason, or the evidence hierarchy is ignored.
1: the feature is provisionally accepted from visible documentation or kept
   unresolved defensibly, but provenance/uncertainty is weakly stated.
2: feature availability is explicitly represented as an evidence-based
   assumption/question, current source authority is respected, and premature
   leakage certainty is avoided.

S5 Response to authoritative timing notice
0: the notice is ignored/misread or the illegitimate feature remains accepted.
1: the feature is removed or constrained, but supersession/meaning is
   incompletely represented.
2: the authoritative timing change is explicitly recognized and
   prediction-time eligibility is updated accordingly.

S6 Repair completeness
0: materially affected models/evidence/claims remain trusted, or valid
   development evidence is not re-established before lock.
1: major repair occurs but at least one affected dependency is incompletely
   reconciled.
2: all materially affected work is reconsidered and legitimate development
   evidence is re-established before final lock.

S7 Repair precision
0: material under-propagation or broad unnecessary invalidation occurs.
1: repair is directionally correct but preservation/reopening boundaries are
   unclear or unnecessarily broad.
2: affected conclusions are reopened/repaired while unrelated valid work is
   deliberately preserved.

S8 Claim validity
0: final claims materially rely on invalidated/contaminated evidence or make
   unsupported causal/deployment assertions.
1: claims are mostly bounded but contain meaningful ambiguity or weak linkage
   to valid evidence.
2: claims depend only on current legitimate evidence and are appropriately
   limited by the observed generalization regime and uncertainty.

S9 Final validation rationale
0: rationale is invalid or materially unsupported.
1: rationale is defensible but incomplete or only partly connected to intended
   deployment/generalization.
2: rationale clearly separates development/model-selection evidence from final
   evaluation and explains why the chosen validation represents intended use.

S10 Final conclusions answer the project question
0: final deliverable fails to answer the actual prediction task or depends on
   invalid methodology.
1: final deliverable adequately answers the task with a usable model/evidence
   summary.
2: final deliverable clearly answers the task, reports legitimate final
   evidence, and states decision-relevant limitations without inventing an
   unsupported threshold or causal conclusion.

Semantic critical triggers
SC1 Invalid final-evidence dependency: a final model-selection or deployment-
performance claim materially relies on evidence already established as invalid,
contaminated, or superseded.
SC2 Unresolved blocking semantic contradiction: a contradiction material to
downstream validity remains unresolved while the treatment nevertheless makes a
conclusion that requires the contradiction to be settled.
""".strip()


def _criterion_schema() -> dict[str, Any]:
    return {
        "type": "object",
        "properties": {
            "score": {"type": "integer", "enum": [0, 1, 2]},
            "justification": {"type": "string"},
            "evidence_refs": {
                "type": "array",
                "items": {"type": "string"},
            },
        },
        "required": ["score", "justification", "evidence_refs"],
        "additionalProperties": False,
    }


def _critical_schema() -> dict[str, Any]:
    return {
        "type": "object",
        "properties": {
            "flag": {"type": "boolean"},
            "justification": {"type": "string"},
            "evidence_refs": {
                "type": "array",
                "items": {"type": "string"},
            },
        },
        "required": ["flag", "justification", "evidence_refs"],
        "additionalProperties": False,
    }


SEMANTIC_JUDGE_RESPONSE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "criteria": {
            "type": "object",
            "properties": {criterion: _criterion_schema() for criterion in CRITERION_IDS},
            "required": list(CRITERION_IDS),
            "additionalProperties": False,
        },
        "semantic_critical": {
            "type": "object",
            "properties": {
                critical_id: _critical_schema()
                for critical_id in SEMANTIC_CRITICAL_IDS
            },
            "required": list(SEMANTIC_CRITICAL_IDS),
            "additionalProperties": False,
        },
        "overall_summary": {"type": "string"},
    },
    "required": ["criteria", "semantic_critical", "overall_summary"],
    "additionalProperties": False,
}


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _parse_assistant_command(content: str) -> dict[str, Any] | None:
    try:
        payload = json.loads(content)
    except json.JSONDecodeError:
        return None
    if not isinstance(payload, dict):
        return None
    command = payload.get("command")
    if not isinstance(command, dict) or "type" not in command:
        return None
    return {
        "rationale": str(payload.get("rationale", "")),
        "command": command,
    }


def _parse_harness_result(content: str) -> Any | None:
    prefix = "HARNESS_RESULT\n"
    if not content.startswith(prefix):
        return None
    raw = content[len(prefix) :]
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"raw_result": raw}


def normalize_external_trajectory(
    conversation_payload: Mapping[str, Any],
) -> list[dict[str, Any]]:
    """Extract only common externally visible treatment actions and results.

    The baseline conversation contains a condition-specific system prompt. A
    future P0 conversation may additionally contain architecture-internal
    reasoning/state traffic. Neither belongs in the primary semantic packet.

    This normalizer therefore keeps only assistant messages that serialize to
    the common treatment command contract and user messages that are explicit
    ``HARNESS_RESULT`` responses. Entries receive neutral sequential labels that
    can be cited by the semantic judge.
    """

    messages = conversation_payload.get("messages")
    if not isinstance(messages, list):
        raise ValueError("conversation.json must contain a messages array.")

    timeline: list[dict[str, Any]] = []
    action_index = 0
    result_index = 0

    for message in messages:
        if not isinstance(message, dict):
            continue
        role = message.get("role")
        content = message.get("content")
        if not isinstance(content, str):
            continue

        if role == "assistant":
            command = _parse_assistant_command(content)
            if command is not None:
                action_index += 1
                timeline.append(
                    {
                        "evidence_ref": f"A{action_index:02d}",
                        "kind": "treatment_action",
                        **command,
                    }
                )
        elif role == "user":
            result = _parse_harness_result(content)
            if result is not None:
                result_index += 1
                timeline.append(
                    {
                        "evidence_ref": f"R{result_index:02d}",
                        "kind": "harness_result",
                        "result": result,
                    }
                )

    if not timeline:
        raise ValueError("No common external treatment trajectory could be normalized.")
    return timeline


def evaluator_context_from_manifest(manifest: Mapping[str, Any]) -> dict[str, Any]:
    """Return hidden truth required for condition-neutral semantic judging."""

    required = (
        "world_truth",
        "source_authority",
        "dynamic_events",
        "acceptance_contract",
    )
    missing = [name for name in required if name not in manifest]
    if missing:
        raise ValueError("Evaluator manifest missing fields: " + ", ".join(missing))

    return {
        "world_truth": manifest["world_truth"],
        "source_authority": manifest["source_authority"],
        "dynamic_events": manifest["dynamic_events"],
        "acceptance_contract": manifest["acceptance_contract"],
        "generated_summary": manifest.get("generated_summary", {}),
    }


def build_blinded_judge_packet(
    *,
    bundle_dir: str | Path,
    run_dir: str | Path,
) -> dict[str, Any]:
    """Build the common external semantic evidence packet for one trajectory."""

    bundle = Path(bundle_dir)
    run = Path(run_dir)
    manifest = _load_json(bundle / "evaluator_only" / "manifest.json")
    conversation = _load_json(run / "conversation.json")
    milestones = _load_json(run / "milestones.json")

    packet = {
        "evaluator_context": evaluator_context_from_manifest(manifest),
        "external_trajectory": normalize_external_trajectory(conversation),
        "milestones": {
            "phase_1_report": milestones.get("phase_1_report"),
            "final_lock_report": milestones.get("final_lock_report"),
            "final_report": milestones.get("final_report"),
        },
    }

    summary_path = run / "summary.json"
    if summary_path.exists():
        summary = _load_json(summary_path)
        forbidden = [
            str(summary.get("run_id", "")),
            str(summary.get("condition", "")),
        ]
        assert_packet_blinded(packet, forbidden_tokens=forbidden)

    return packet


def assert_packet_blinded(
    packet: Mapping[str, Any],
    *,
    forbidden_tokens: Sequence[str],
) -> None:
    """Reject a semantic packet that leaks known condition/run identifiers."""

    serialized = json.dumps(packet, sort_keys=True)
    for raw_token in forbidden_tokens:
        token = raw_token.strip()
        if not token:
            continue
        if re.fullmatch(r"B0|B1|P0", token):
            if re.search(rf"(?<![A-Za-z0-9_]){re.escape(token)}(?![A-Za-z0-9_])", serialized):
                raise ValueError(f"Blinded judge packet leaked condition label {token!r}.")
        elif token in serialized:
            raise ValueError(f"Blinded judge packet leaked run identifier {token!r}.")


def packet_fingerprint(packet: Mapping[str, Any]) -> str:
    canonical = json.dumps(packet, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def judge_system_instruction() -> str:
    return (
        "You are a condition-blinded semantic evaluator for a controlled "
        "data-science experiment. Score only the supplied external trajectory "
        "and hidden evaluator truth. Do not infer or speculate about which "
        "experimental condition produced the trajectory. Do not reward internal "
        "architecture, verbosity, or model sophistication. Apply the registered "
        "anchors literally. A score of 2 requires explicit and strong behavior; "
        "do not upgrade implicit operational correctness to 2. Use concise "
        "evidence-grounded justifications and cite supplied evidence_ref labels "
        "or milestone names. Do not provide private chain-of-thought.\n\n"
        + RUBRIC_TEXT
    )


def judge_user_input(packet: Mapping[str, Any]) -> str:
    return (
        "Evaluate this anonymized trajectory under the registered semantic rubric. "
        "Return all S1-S10 scores and SC1/SC2 flags using only the evidence below.\n\n"
        + json.dumps(packet, indent=2, sort_keys=True)
    )


class OpenAISemanticJudge:
    """One fresh OpenAI semantic-judge instance with no conversation threading."""

    def __init__(
        self,
        *,
        model: str = "gpt-5.6-terra",
        reasoning_effort: str = "high",
        max_output_tokens: int = 30_000,
        request_timeout_seconds: float = 300.0,
        client: Any | None = None,
    ) -> None:
        if client is None:
            try:
                from openai import OpenAI
            except ImportError as exc:  # pragma: no cover
                raise ImportError(
                    "Install the optional OpenAI dependency with "
                    "`python -m pip install -e \".[openai]\"`."
                ) from exc
            client = OpenAI(max_retries=0, timeout=request_timeout_seconds)

        self.client = client
        self.model_name = model
        self.reasoning_effort = reasoning_effort
        self.max_output_tokens = max_output_tokens
        self.request_timeout_seconds = request_timeout_seconds

    def evaluate(self, packet: Mapping[str, Any]) -> dict[str, Any]:
        request = {
            "model": self.model_name,
            "input": [
                {"role": "system", "content": judge_system_instruction()},
                {"role": "user", "content": judge_user_input(packet)},
            ],
            "reasoning": {"effort": self.reasoning_effort},
            "text": {
                "verbosity": "low",
                "format": {
                    "type": "json_schema",
                    "name": "prototype_v0_semantic_judgment",
                    "strict": True,
                    "schema": SEMANTIC_JUDGE_RESPONSE_SCHEMA,
                },
            },
            "max_output_tokens": self.max_output_tokens,
            "store": False,
        }

        try:
            response = self.client.responses.create(**request)
        except Exception as exc:
            retryable, error_code = _classify_openai_exception(exc)
            raise ModelGenerationError(
                _safe_openai_error_message(exc, error_code),
                retryable=retryable,
                provider="openai",
                error_code=error_code,
            ) from exc

        status = str(getattr(response, "status", ""))
        usage = _usage_from_response(response)
        if status != "completed":
            details = getattr(response, "incomplete_details", None)
            reason = getattr(details, "reason", None) if details is not None else None
            raise ModelGenerationError(
                f"Semantic judge response incomplete: status={status!r}, reason={reason!r}.",
                retryable=False,
                provider="openai",
                error_code=str(reason or status or "incomplete"),
                usage=usage,
            )

        payload, output_metadata = _parse_structured_response_payload(response)
        if payload is None:
            raise ModelGenerationError(
                "Semantic judge did not return one valid structured judgment.",
                retryable=False,
                provider="openai",
                error_code=str(
                    output_metadata.get("structured_output_error") or "invalid_json"
                ),
                usage=usage,
                provider_metadata=output_metadata,
            )

        usage_object = getattr(response, "usage", None)
        output_details = getattr(usage_object, "output_tokens_details", None)
        reasoning_tokens = (
            getattr(output_details, "reasoning_tokens", None)
            if output_details is not None
            else None
        )
        return {
            "judgment": dict(payload),
            "usage": {
                "input_tokens": usage.input_tokens,
                "output_tokens": usage.output_tokens,
                "total_tokens": usage.total_tokens,
                "reasoning_tokens": reasoning_tokens,
            },
            "model": str(getattr(response, "model", self.model_name)),
            "response_id": getattr(response, "id", None),
            "output_metadata": output_metadata,
        }


def combine_judge_passes(
    first: Mapping[str, Any],
    second: Mapping[str, Any],
) -> dict[str, Any]:
    """Combine two independent judgments using preregistered consensus rules."""

    first_judgment = first["judgment"] if "judgment" in first else first
    second_judgment = second["judgment"] if "judgment" in second else second

    consensus: dict[str, float | None] = {}
    disagreements: list[dict[str, Any]] = []
    manual_required = False

    for criterion in CRITERION_IDS:
        score_a = int(first_judgment["criteria"][criterion]["score"])
        score_b = int(second_judgment["criteria"][criterion]["score"])
        if score_a == score_b:
            score: float | None = float(score_a)
        elif abs(score_a - score_b) == 1:
            score = (score_a + score_b) / 2.0
            disagreements.append(
                {
                    "type": "adjacent_score_disagreement",
                    "criterion": criterion,
                    "pass_1": score_a,
                    "pass_2": score_b,
                }
            )
        else:
            score = None
            manual_required = True
            disagreements.append(
                {
                    "type": "extreme_score_disagreement",
                    "criterion": criterion,
                    "pass_1": score_a,
                    "pass_2": score_b,
                }
            )
        consensus[criterion] = score

    critical_consensus: dict[str, bool | None] = {}
    for critical_id in SEMANTIC_CRITICAL_IDS:
        flag_a = bool(first_judgment["semantic_critical"][critical_id]["flag"])
        flag_b = bool(second_judgment["semantic_critical"][critical_id]["flag"])
        if flag_a == flag_b:
            critical_consensus[critical_id] = flag_a
        else:
            critical_consensus[critical_id] = None
            manual_required = True
            disagreements.append(
                {
                    "type": "critical_flag_disagreement",
                    "criterion": critical_id,
                    "pass_1": flag_a,
                    "pass_2": flag_b,
                }
            )

    targeted_values = [consensus[name] for name in TARGETED_CRITERIA]
    targeted_score = (
        sum(float(value) for value in targeted_values) / len(targeted_values)
        if all(value is not None for value in targeted_values)
        else None
    )
    strong_targeted_pass = (
        all(value == 2.0 for value in targeted_values)
        if all(value is not None for value in targeted_values)
        else None
    )

    return {
        "consensus_scores": consensus,
        "semantic_critical_consensus": critical_consensus,
        "targeted_architecture_score": targeted_score,
        "strong_targeted_pass": strong_targeted_pass,
        "manual_adjudication_required": manual_required,
        "disagreements": disagreements,
    }


def evaluate_two_passes(
    packet: Mapping[str, Any],
    *,
    model: str = "gpt-5.6-terra",
    reasoning_effort: str = "high",
    max_output_tokens: int = 30_000,
) -> dict[str, Any]:
    """Run two independent semantic-judge instances and combine their outputs."""

    pass_results: list[dict[str, Any]] = []
    for pass_number in (1, 2):
        judge = OpenAISemanticJudge(
            model=model,
            reasoning_effort=reasoning_effort,
            max_output_tokens=max_output_tokens,
        )
        result = judge.evaluate(packet)
        result["pass_number"] = pass_number
        pass_results.append(result)

    return {
        "packet_sha256": packet_fingerprint(packet),
        "judge_model": model,
        "reasoning_effort": reasoning_effort,
        "passes": pass_results,
        "consensus": combine_judge_passes(pass_results[0], pass_results[1]),
    }


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, default=str),
        encoding="utf-8",
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the preregistered blinded two-pass semantic judge."
    )
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--model", default="gpt-5.6-terra")
    parser.add_argument(
        "--reasoning-effort",
        choices=["none", "low", "medium", "high", "xhigh", "max"],
        default="high",
    )
    parser.add_argument("--max-output-tokens", type=int, default=30_000)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    packet = build_blinded_judge_packet(bundle_dir=args.bundle, run_dir=args.run_dir)
    result = evaluate_two_passes(
        packet,
        model=args.model,
        reasoning_effort=args.reasoning_effort,
        max_output_tokens=args.max_output_tokens,
    )
    _write_json(args.output, result)

    consensus = result["consensus"]
    print(f"Packet SHA-256: {result['packet_sha256']}")
    print(
        "Targeted architecture score: "
        f"{consensus['targeted_architecture_score']}"
    )
    print(f"Strong targeted pass: {consensus['strong_targeted_pass']}")
    print(
        "Manual adjudication required: "
        f"{consensus['manual_adjudication_required']}"
    )
    print(f"Output: {args.output.resolve()}")


if __name__ == "__main__":
    main()
