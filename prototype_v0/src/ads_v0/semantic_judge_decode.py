"""Deterministically decode frozen Prototype V0 semantic results after blinding.

This module is deliberately downstream of the blinded semantic freeze. It never
calls a model provider and never changes treatment, judge, or frozen semantic
evidence. Its job is to turn the already-frozen opaque case identities into the
registered H1/H2 and B0/B1/P0 comparison structure.

The order of operations is important:

1. re-verify the complete blinded semantic state without reading the decoder;
2. require exact agreement with the persisted blinded freeze aggregate;
3. only then read ``private_decoder.json``;
4. map every opaque case to exactly one frozen treatment slot;
5. combine frozen semantic consensus with the retained treatment's mechanical
   summary;
6. emit run-level, variant-level, pooled, and paired comparison data;
7. package a compact decoded export outside the frozen evidence tree.

The decoder intentionally does not infer architecture-induced false blocking,
unnecessary reopening, over-invalidation, or held-out-specific hard coding from
the common semantic score. Those are P0-internal architecture diagnostics and
must be evaluated explicitly after unblinding rather than silently conflated
with condition-neutral semantic criteria.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping

from .semantic_judge_freeze import FREEZE_FILE, verify_blinded_state
from .semantic_judge_supervisor import (
    BLINDED_DIR,
    DEFAULT_SEMANTIC_ROOT,
    PRIVATE_DECODER_FILE,
)


DECODE_SCHEMA_VERSION = "semantic_judge_decoded_v0_1"
DEFAULT_DECODE_ROOT = Path("results/held_out/semantic_judge_decoded")
DEFAULT_DECODE_EXPORT_ROOT = Path("results/held_out/semantic_judge_decoded_exports")
RUN_TABLE_FILE = "decoded_run_table.csv"
DECODED_RESULT_FILE = "decoded_results.json"

CRITERIA = tuple(f"S{i}" for i in range(1, 11))
CONDITIONS = ("B0", "B1", "P0")
VARIANTS = ("H1", "H2")


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _timestamp_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _read_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Expected JSON object in {path}.")
    return payload


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(dict(payload), indent=2, sort_keys=True, default=str),
        encoding="utf-8",
    )


def _safe_ratio(numerator: float, denominator: float) -> float | None:
    if denominator == 0:
        return None
    return float(numerator) / float(denominator)


def _mean(values: Iterable[float]) -> float:
    materialized = [float(value) for value in values]
    if not materialized:
        raise ValueError("Cannot compute mean of an empty collection.")
    return float(statistics.mean(materialized))


def _median(values: Iterable[float]) -> float:
    materialized = [float(value) for value in values]
    if not materialized:
        raise ValueError("Cannot compute median of an empty collection.")
    return float(statistics.median(materialized))


def _validate_frozen_boundary(semantic_root: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    """Re-verify blinded evidence before any private decoder is read."""

    freeze_path = semantic_root / FREEZE_FILE
    if not freeze_path.is_file():
        raise FileNotFoundError(
            f"Blinded semantic freeze does not exist: {freeze_path}. Refusing decode."
        )

    frozen = _read_json(freeze_path)
    if frozen.get("status") != "FROZEN_BLINDED_CONSENSUS":
        raise ValueError("Semantic evidence is not marked FROZEN_BLINDED_CONSENSUS.")
    if bool(frozen.get("decoder_read", True)):
        raise ValueError("Frozen manifest does not certify a decoder-free freeze boundary.")
    if int(frozen.get("manual_adjudication_cases", -1)) != 0:
        raise ValueError("Cannot decode while frozen manual adjudication remains unresolved.")

    # This call is decoder-free by construction. It recomputes packet identities,
    # pass/consensus consistency, provider accounting, file hashes, and aggregate.
    verification = verify_blinded_state(semantic_root=semantic_root)
    if verification["aggregate_sha256"] != frozen.get("aggregate_sha256"):
        raise ValueError(
            "Current blinded evidence no longer matches the frozen aggregate. "
            "Refusing to reveal condition identities."
        )
    if int(verification["prepared_cases"]) != 30:
        raise ValueError("Frozen semantic decode requires exactly 30 prepared cases.")
    if int(verification["logical_passes"]) != 60:
        raise ValueError("Frozen semantic decode requires exactly 60 logical judge passes.")
    if int(verification["completed_cases"]) != 30:
        raise ValueError("Frozen semantic decode requires exactly 30 completed cases.")
    if int(verification["manual_adjudication_cases"]) != 0:
        raise ValueError("Frozen semantic state unexpectedly requires manual adjudication.")

    return frozen, verification


def _load_decoder_after_freeze(
    *,
    semantic_root: Path,
    frozen: Mapping[str, Any],
) -> list[dict[str, Any]]:
    """Read and validate the private mapping only after the freeze is established."""

    decoder_path = semantic_root / PRIVATE_DECODER_FILE
    if not decoder_path.is_file():
        raise FileNotFoundError(f"Private semantic decoder is missing: {decoder_path}")
    decoder = _read_json(decoder_path)
    rows = decoder.get("cases")
    if not isinstance(rows, list) or len(rows) != 30:
        raise ValueError("Private decoder must contain exactly 30 cases.")

    frozen_cases = frozen.get("cases")
    if not isinstance(frozen_cases, list) or len(frozen_cases) != 30:
        raise ValueError("Frozen manifest must contain exactly 30 case summaries.")
    frozen_by_id = {
        str(row["blind_id"]): str(row["packet_sha256"])
        for row in frozen_cases
        if isinstance(row, dict)
    }
    if len(frozen_by_id) != 30:
        raise ValueError("Frozen manifest contains duplicate or malformed blind identities.")

    seen_blind_ids: set[str] = set()
    seen_slot_ids: set[str] = set()
    validated: list[dict[str, Any]] = []

    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Private decoder case entry must be an object.")
        blind_id = str(row.get("blind_id", ""))
        packet_sha = str(row.get("packet_sha256", ""))
        slot = row.get("slot")
        if not blind_id or blind_id in seen_blind_ids:
            raise ValueError("Private decoder contains duplicate/empty blind identity.")
        if not isinstance(slot, dict):
            raise ValueError(f"Private decoder slot is malformed for {blind_id}.")

        slot_id = str(slot.get("slot_id", ""))
        condition = str(slot.get("condition", ""))
        variant = str(slot.get("variant", ""))
        if not slot_id or slot_id in seen_slot_ids:
            raise ValueError("Private decoder contains duplicate/empty slot identity.")
        if condition not in CONDITIONS or variant not in VARIANTS:
            raise ValueError(f"Invalid decoded condition/variant for {blind_id}.")
        if frozen_by_id.get(blind_id) != packet_sha:
            raise ValueError(
                f"Private decoder packet identity disagrees with frozen evidence: {blind_id}."
            )

        seen_blind_ids.add(blind_id)
        seen_slot_ids.add(slot_id)
        validated.append(dict(row))

    condition_counts = {
        condition: sum(
            str(row["slot"]["condition"]) == condition for row in validated
        )
        for condition in CONDITIONS
    }
    variant_condition_counts = {
        variant: {
            condition: sum(
                str(row["slot"]["variant"]) == variant
                and str(row["slot"]["condition"]) == condition
                for row in validated
            )
            for condition in CONDITIONS
        }
        for variant in VARIANTS
    }
    if condition_counts != {"B0": 10, "B1": 10, "P0": 10}:
        raise ValueError(f"Decoded condition counts are invalid: {condition_counts}")
    expected_variant_counts = {
        "H1": {"B0": 5, "B1": 5, "P0": 5},
        "H2": {"B0": 5, "B1": 5, "P0": 5},
    }
    if variant_condition_counts != expected_variant_counts:
        raise ValueError(
            "Decoded H1/H2 condition balance is invalid: "
            f"{variant_condition_counts}"
        )

    return validated


def _semantic_row(semantic_root: Path, blind_id: str) -> dict[str, Any]:
    consensus_path = semantic_root / BLINDED_DIR / blind_id / "consensus.json"
    payload = _read_json(consensus_path)
    consensus = payload.get("consensus")
    if not isinstance(consensus, dict):
        raise ValueError(f"Missing semantic consensus for {blind_id}.")
    scores = consensus.get("consensus_scores")
    critical = consensus.get("semantic_critical_consensus")
    if not isinstance(scores, dict) or not isinstance(critical, dict):
        raise ValueError(f"Malformed semantic consensus for {blind_id}.")
    if any(scores.get(name) is None for name in CRITERIA):
        raise ValueError(f"Unresolved ordinary semantic score for {blind_id}.")
    if critical.get("SC1") is None or critical.get("SC2") is None:
        raise ValueError(f"Unresolved semantic critical flag for {blind_id}.")

    return {
        **{name: float(scores[name]) for name in CRITERIA},
        "SC1": bool(critical["SC1"]),
        "SC2": bool(critical["SC2"]),
        "targeted_architecture_score": float(consensus["targeted_architecture_score"]),
        "strong_targeted_pass": bool(consensus["strong_targeted_pass"]),
    }


def _load_treatment_summary(run_dir: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    summary_path = run_dir / "summary.json"
    milestones_path = run_dir / "milestones.json"
    if not summary_path.is_file() or not milestones_path.is_file():
        raise FileNotFoundError(f"Retained trajectory artifacts are incomplete: {run_dir}")
    return _read_json(summary_path), _read_json(milestones_path)


def _decode_run_rows(
    *,
    semantic_root: Path,
    decoder_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    for mapping in decoder_rows:
        blind_id = str(mapping["blind_id"])
        slot = mapping["slot"]
        attempt_id = str(mapping["attempt_id"])
        run_dir = Path(str(mapping["run_dir"]))
        summary, milestones = _load_treatment_summary(run_dir)
        semantic = _semantic_row(semantic_root, blind_id)

        if str(summary.get("run_id")) != attempt_id:
            raise ValueError(f"Decoded attempt identity mismatch for {blind_id}.")
        if str(summary.get("condition")) != str(slot["condition"]):
            raise ValueError(f"Decoded condition disagrees with summary for {blind_id}.")
        if not bool(summary.get("behavior_evaluable", False)):
            raise ValueError(f"Decoded retained trajectory is not behavior evaluable: {attempt_id}.")

        deterministic_critical = summary.get("critical_failures", [])
        if not isinstance(deterministic_critical, list):
            raise ValueError(f"critical_failures is malformed for {attempt_id}.")
        semantic_critical_count = int(semantic["SC1"]) + int(semantic["SC2"])
        total_critical_events = len(deterministic_critical) + semantic_critical_count

        rows.append(
            {
                "slot_index": int(slot["slot_index"]),
                "variant": str(slot["variant"]),
                "replicate": int(slot["replicate"]),
                "position_in_replicate": int(slot["position_in_replicate"]),
                "condition": str(slot["condition"]),
                "slot_id": str(slot["slot_id"]),
                "blind_id": blind_id,
                "attempt_id": attempt_id,
                "attempt_number": int(mapping["attempt_number"]),
                **semantic,
                "deterministic_critical_failures": list(deterministic_critical),
                "critical_failure_events": total_critical_events,
                "critical_failure_run": total_critical_events > 0,
                "completed": bool(summary.get("completed", False)),
                "completed_within_budget": bool(
                    summary.get("completed_within_budget", False)
                ),
                "budget_exhausted": bool(summary.get("budget_exhausted", False)),
                "model_calls": int(summary.get("model_calls", 0)),
                "generation_attempts": int(summary.get("generation_attempts", 0)),
                "generation_failures": int(summary.get("generation_failures", 0)),
                "python_execution_attempts": int(
                    summary.get("python_execution_attempts", 0)
                ),
                "total_tokens": int(summary.get("total_tokens", 0)),
                "final_report_present": milestones.get("final_report") is not None,
            }
        )

    rows.sort(key=lambda row: int(row["slot_index"]))
    if len(rows) != 30:
        raise ValueError(f"Decoded run table must contain 30 rows, found {len(rows)}.")
    return rows


def _group_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    if not rows:
        raise ValueError("Cannot summarize an empty decoded group.")
    return {
        "n": len(rows),
        "semantic_mean": {
            criterion: _mean(row[criterion] for row in rows)
            for criterion in CRITERIA
        },
        "targeted_architecture_mean": _mean(
            row["targeted_architecture_score"] for row in rows
        ),
        "strong_targeted_pass_count": sum(
            bool(row["strong_targeted_pass"]) for row in rows
        ),
        "semantic_critical_SC1_count": sum(bool(row["SC1"]) for row in rows),
        "semantic_critical_SC2_count": sum(bool(row["SC2"]) for row in rows),
        "critical_failure_runs": sum(bool(row["critical_failure_run"]) for row in rows),
        "critical_failure_events": sum(int(row["critical_failure_events"]) for row in rows),
        "completed_count": sum(bool(row["completed"]) for row in rows),
        "completed_within_budget_count": sum(
            bool(row["completed_within_budget"]) for row in rows
        ),
        "budget_exhausted_count": sum(bool(row["budget_exhausted"]) for row in rows),
        "final_report_count": sum(bool(row["final_report_present"]) for row in rows),
        "resource_medians": {
            "total_tokens": _median(row["total_tokens"] for row in rows),
            "model_calls": _median(row["model_calls"] for row in rows),
            "python_execution_attempts": _median(
                row["python_execution_attempts"] for row in rows
            ),
        },
        "resource_means": {
            "total_tokens": _mean(row["total_tokens"] for row in rows),
            "model_calls": _mean(row["model_calls"] for row in rows),
            "python_execution_attempts": _mean(
                row["python_execution_attempts"] for row in rows
            ),
        },
    }


def _condition_summaries(rows: list[dict[str, Any]]) -> dict[str, Any]:
    pooled = {
        condition: _group_summary(
            [row for row in rows if row["condition"] == condition]
        )
        for condition in CONDITIONS
    }
    by_variant = {
        variant: {
            condition: _group_summary(
                [
                    row
                    for row in rows
                    if row["variant"] == variant and row["condition"] == condition
                ]
            )
            for condition in CONDITIONS
        }
        for variant in VARIANTS
    }
    return {"pooled": pooled, "by_variant": by_variant}


def _paired_targeted_differences(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    pairs: list[dict[str, Any]] = []
    for variant in VARIANTS:
        for replicate in range(1, 6):
            block = [
                row
                for row in rows
                if row["variant"] == variant and int(row["replicate"]) == replicate
            ]
            by_condition = {str(row["condition"]): row for row in block}
            if set(by_condition) != set(CONDITIONS):
                raise ValueError(
                    f"Decoded replicate {variant} R{replicate} lacks one condition."
                )
            p0 = float(by_condition["P0"]["targeted_architecture_score"])
            b1 = float(by_condition["B1"]["targeted_architecture_score"])
            b0 = float(by_condition["B0"]["targeted_architecture_score"])
            pairs.append(
                {
                    "variant": variant,
                    "replicate": replicate,
                    "B0": b0,
                    "B1": b1,
                    "P0": p0,
                    "P0_minus_B1": p0 - b1,
                    "B1_minus_B0": b1 - b0,
                }
            )
    return pairs


def _registered_comparison_facts(summaries: Mapping[str, Any]) -> dict[str, Any]:
    pooled = summaries["pooled"]
    variants = summaries["by_variant"]
    b1 = pooled["B1"]
    p0 = pooled["P0"]

    targeted_diff = (
        float(p0["targeted_architecture_mean"])
        - float(b1["targeted_architecture_mean"])
    )
    strong_diff = int(p0["strong_targeted_pass_count"]) - int(
        b1["strong_targeted_pass_count"]
    )
    critical_event_diff = int(p0["critical_failure_events"]) - int(
        b1["critical_failure_events"]
    )
    variant_diffs = {
        variant: (
            float(variants[variant]["P0"]["targeted_architecture_mean"])
            - float(variants[variant]["B1"]["targeted_architecture_mean"])
        )
        for variant in VARIANTS
    }

    p0_medians = p0["resource_medians"]
    b1_medians = b1["resource_medians"]
    ratios = {
        "total_tokens": _safe_ratio(
            float(p0_medians["total_tokens"]), float(b1_medians["total_tokens"])
        ),
        "model_calls": _safe_ratio(
            float(p0_medians["model_calls"]), float(b1_medians["model_calls"])
        ),
        "python_execution_attempts": _safe_ratio(
            float(p0_medians["python_execution_attempts"]),
            float(b1_medians["python_execution_attempts"]),
        ),
    }

    reliability_a = critical_event_diff <= -2
    reliability_b = targeted_diff >= 0.30 and strong_diff >= 2
    cross_variant = all(diff >= -0.10 for diff in variant_diffs.values())
    completion = (
        int(p0["completed_within_budget_count"]) >= 9
        and int(p0["completed_within_budget_count"])
        >= int(b1["completed_within_budget_count"]) - 1
    )
    resource_cost = (
        all(value is not None and value <= 1.50 for value in ratios.values())
        and int(p0["budget_exhausted_count"]) <= 1
    )

    # Architecture-specific P0 diagnostic clauses are intentionally unresolved
    # here. The continuation criterion already fails if any mechanically resolved
    # mandatory component is false, but final strong-falsification classification
    # must also consider the separate architecture-diagnostic clauses.
    continuation_mechanical_components = {
        "critical_failures_not_worse_than_B1": (
            int(p0["critical_failure_events"])
            <= int(b1["critical_failure_events"])
        ),
        "material_reliability_A": reliability_a,
        "material_reliability_B": reliability_b,
        "material_reliability_A_or_B": reliability_a or reliability_b,
        "cross_variant_robustness": cross_variant,
        "completion": completion,
        "acceptable_resource_cost": resource_cost,
    }
    continuation_already_impossible = any(
        not value for value in continuation_mechanical_components.values()
    )

    return {
        "primary_comparison": "P0_vs_B1",
        "pooled_targeted_mean_difference_P0_minus_B1": targeted_diff,
        "strong_targeted_pass_count_difference_P0_minus_B1": strong_diff,
        "critical_failure_event_difference_P0_minus_B1": critical_event_diff,
        "variant_targeted_mean_differences_P0_minus_B1": variant_diffs,
        "resource_median_ratios_P0_over_B1": ratios,
        "completion_counts": {
            "B1_completed_within_budget": int(b1["completed_within_budget_count"]),
            "P0_completed_within_budget": int(p0["completed_within_budget_count"]),
            "B1_budget_exhausted": int(b1["budget_exhausted_count"]),
            "P0_budget_exhausted": int(p0["budget_exhausted_count"]),
        },
        "continuation_components_resolved_from_common_evidence": (
            continuation_mechanical_components
        ),
        "continuation_signal_already_impossible_from_resolved_components": (
            continuation_already_impossible
        ),
        "architecture_specific_clauses_not_scored_here": [
            "critical architecture-induced false block or over-invalidation",
            "noncritical architecture-induced false blocking/unnecessary broad reopening",
            "held-out-case-specific hard coding",
        ],
        "strong_falsification_resource_trigger": {
            "P0_tokens_at_least_1_25x_B1": (
                ratios["total_tokens"] is not None and ratios["total_tokens"] >= 1.25
            ),
            "P0_calls_at_least_1_25x_B1": (
                ratios["model_calls"] is not None and ratios["model_calls"] >= 1.25
            ),
            "registered_reliability_match_or_exceed_clause": (
                "requires final interpretation of the decoded reliability outcomes; "
                "not silently defined by this decoder"
            ),
        },
    }


def build_decoded_result(
    *,
    semantic_root: str | Path = DEFAULT_SEMANTIC_ROOT,
) -> dict[str, Any]:
    """Verify frozen state, reveal the private mapping, and compute comparisons."""

    root = Path(semantic_root)
    frozen, verification = _validate_frozen_boundary(root)
    decoder_rows = _load_decoder_after_freeze(semantic_root=root, frozen=frozen)
    run_rows = _decode_run_rows(semantic_root=root, decoder_rows=decoder_rows)
    summaries = _condition_summaries(run_rows)
    paired = _paired_targeted_differences(run_rows)
    comparison = _registered_comparison_facts(summaries)

    return {
        "schema_version": DECODE_SCHEMA_VERSION,
        "decoded_at_utc": _utc_now(),
        "frozen_semantic_aggregate_sha256": str(frozen["aggregate_sha256"]),
        "predecode_verification": {
            "prepared_cases": int(verification["prepared_cases"]),
            "logical_passes": int(verification["logical_passes"]),
            "completed_cases": int(verification["completed_cases"]),
            "manual_adjudication_cases": int(
                verification["manual_adjudication_cases"]
            ),
            "provider_attempts_started": int(
                verification["provider_attempts_started"]
            ),
            "decoder_read_during_verification": False,
        },
        "decoder_read_after_freeze_verification": True,
        "run_rows": run_rows,
        "summaries": summaries,
        "paired_targeted_differences": paired,
        "registered_comparison_facts": comparison,
        "interpretation_boundary": {
            "launches_model_calls": False,
            "mutates_frozen_semantic_evidence": False,
            "changes_semantic_scores": False,
            "architecture_specific_P0_diagnostics_inferred": False,
        },
    }


def _write_run_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "slot_index",
        "variant",
        "replicate",
        "position_in_replicate",
        "condition",
        "slot_id",
        "blind_id",
        "attempt_id",
        "attempt_number",
        *CRITERIA,
        "SC1",
        "SC2",
        "targeted_architecture_score",
        "strong_targeted_pass",
        "critical_failure_events",
        "critical_failure_run",
        "completed",
        "completed_within_budget",
        "budget_exhausted",
        "model_calls",
        "generation_attempts",
        "generation_failures",
        "python_execution_attempts",
        "total_tokens",
        "final_report_present",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def decode_and_export(
    *,
    semantic_root: str | Path = DEFAULT_SEMANTIC_ROOT,
    output_root: str | Path = DEFAULT_DECODE_ROOT,
    export_root: str | Path = DEFAULT_DECODE_EXPORT_ROOT,
) -> tuple[dict[str, Any], Path]:
    """Create compact decoded artifacts without copying the raw private decoder."""

    result = build_decoded_result(semantic_root=semantic_root)
    output = Path(output_root)
    exports = Path(export_root)
    output.mkdir(parents=True, exist_ok=True)
    exports.mkdir(parents=True, exist_ok=True)

    result_path = output / DECODED_RESULT_FILE
    csv_path = output / RUN_TABLE_FILE
    _write_json(result_path, result)
    _write_run_csv(csv_path, result["run_rows"])

    archive = exports / f"semantic_judge_decoded_{_timestamp_id()}.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zipped:
        zipped.write(result_path, DECODED_RESULT_FILE)
        zipped.write(csv_path, RUN_TABLE_FILE)

    return result, archive


def _print_summary(result: Mapping[str, Any]) -> None:
    pooled = result["summaries"]["pooled"]
    comparison = result["registered_comparison_facts"]
    print(
        "Frozen aggregate verified before decode: "
        f"{result['frozen_semantic_aggregate_sha256']}"
    )
    print("Private decoder read only after freeze verification: yes")
    for condition in CONDITIONS:
        summary = pooled[condition]
        print(
            f"{condition}: targeted_mean="
            f"{summary['targeted_architecture_mean']:.3f} "
            f"strong={summary['strong_targeted_pass_count']}/10 "
            f"critical_failure_runs={summary['critical_failure_runs']}/10 "
            f"completed_within_budget={summary['completed_within_budget_count']}/10 "
            f"budget_exhausted={summary['budget_exhausted_count']}/10"
        )
    print(
        "P0-B1 pooled targeted mean difference: "
        f"{comparison['pooled_targeted_mean_difference_P0_minus_B1']:.3f}"
    )
    print(
        "P0/B1 median resource ratios: "
        + ", ".join(
            f"{name}={value:.3f}" if value is not None else f"{name}=undefined"
            for name, value in comparison["resource_median_ratios_P0_over_B1"].items()
        )
    )
    print(
        "Continuation signal already impossible from resolved common/mechanical "
        "components: "
        f"{comparison['continuation_signal_already_impossible_from_resolved_components']}"
    )
    print(
        "Architecture-specific friction/hard-coding clauses remain a separate "
        "post-unblinding diagnostic step."
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Decode frozen Prototype V0 semantic results after blinding."
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser(
        "verify-freeze",
        help="Re-verify the frozen semantic aggregate without reading the decoder.",
    )
    sub.add_parser(
        "decode",
        help="Verify the freeze, decode conditions, compute comparisons, and export.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    if args.command == "verify-freeze":
        frozen, verification = _validate_frozen_boundary(Path(DEFAULT_SEMANTIC_ROOT))
        print(f"Frozen aggregate: {frozen['aggregate_sha256']}")
        print(f"Prepared cases: {verification['prepared_cases']} / 30")
        print(f"Logical passes: {verification['logical_passes']} / 60")
        print(f"Completed cases: {verification['completed_cases']} / 30")
        print("Private decoder read: no")
        return
    if args.command == "decode":
        result, archive = decode_and_export()
        _print_summary(result)
        print(f"Decoded export: {archive.resolve()}")
        return
    raise AssertionError(f"Unhandled semantic decode command: {args.command}")


if __name__ == "__main__":
    main()
