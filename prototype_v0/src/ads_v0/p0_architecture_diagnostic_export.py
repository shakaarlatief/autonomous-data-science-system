"""Export post-unblinding P0 architecture diagnostics for Prototype V0.

This module is strictly downstream of the frozen and decoded held-out experiment.
It performs no model calls, does not alter treatment or semantic evidence, and
writes nothing inside retained attempt directories.

Its purpose is to collect the P0-internal evidence needed for the remaining
Foundation 012 architecture-specific clauses that cannot be inferred from the
condition-neutral S1-S10 judge scores:

* critical architecture-induced false blocking or over-invalidation;
* noncritical architecture-induced false blocking or unnecessary broad reopening;
* held-out-case-specific hard coding.

The export contains only retained P0 trajectories. It includes the P0 state,
state history, knowledge activations, common trace, conversation, milestones,
summary, deterministic evaluation, and executor provenance for each P0 run,
plus a compact deterministic structural summary and per-file SHA-256 hashes.
The semantic private decoder is never copied into this export.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


DEFAULT_DECODED_RESULT = Path(
    "results/held_out/semantic_judge_decoded/decoded_results.json"
)
DEFAULT_ATTEMPTS_ROOT = Path("results/held_out/attempts")
DEFAULT_EXPORT_ROOT = Path("results/held_out/p0_architecture_diagnostic_exports")
EXPORT_SCHEMA_VERSION = "p0_architecture_diagnostic_export_v0_1"

_REQUIRED_FILES = (
    "attempt_started.json",
    "attempt_record.json",
    "summary.json",
    "deterministic_evaluation.json",
    "milestones.json",
    "conversation.json",
    "trace.jsonl",
    "p0_state.json",
    "p0_state_history.json",
    "p0_knowledge_activations.json",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _timestamp_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _read_trace(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_number, raw in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not raw.strip():
            continue
        payload = json.loads(raw)
        if not isinstance(payload, dict):
            raise ValueError(f"Trace line {line_number} is not a JSON object: {path}")
        rows.append(payload)
    return rows


def _load_p0_rows(decoded_result_path: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    decoded = _read_json(decoded_result_path)
    if not isinstance(decoded, dict):
        raise ValueError("Decoded semantic result must be a JSON object.")
    if str(decoded.get("schema_version")) != "semantic_judge_decoded_v0_1":
        raise ValueError("Unexpected decoded semantic-result schema version.")
    if not bool(decoded.get("decoder_read_after_freeze_verification", False)):
        raise ValueError("Decoded result does not certify post-freeze decoding.")

    rows = decoded.get("run_rows")
    if not isinstance(rows, list) or len(rows) != 30:
        raise ValueError("Decoded semantic result must contain exactly 30 run rows.")
    p0_rows = [dict(row) for row in rows if isinstance(row, dict) and row.get("condition") == "P0"]
    if len(p0_rows) != 10:
        raise ValueError(f"Expected exactly 10 decoded P0 rows, found {len(p0_rows)}.")
    if {str(row.get("variant")) for row in p0_rows} != {"H1", "H2"}:
        raise ValueError("Decoded P0 rows do not cover both H1 and H2.")
    return decoded, sorted(p0_rows, key=lambda row: int(row["slot_index"]))


def _state_structural_summary(attempt_dir: Path) -> dict[str, Any]:
    state = _read_json(attempt_dir / "p0_state.json")
    history = _read_json(attempt_dir / "p0_state_history.json")
    activations = _read_json(attempt_dir / "p0_knowledge_activations.json")
    trace = _read_trace(attempt_dir / "trace.jsonl")

    if not isinstance(state, dict):
        raise ValueError(f"p0_state.json must contain an object: {attempt_dir}")
    objects = state.get("objects", [])
    relations = state.get("relations", [])
    if not isinstance(objects, list) or not isinstance(relations, list):
        raise ValueError(f"Malformed P0 state snapshot: {attempt_dir}")
    if not isinstance(history, list) or not isinstance(activations, list):
        raise ValueError(f"Malformed P0 state history/activation artifacts: {attempt_dir}")

    object_type_counts = Counter(
        str(obj.get("type")) for obj in objects if isinstance(obj, dict)
    )
    object_status_counts = Counter(
        f"{obj.get('type')}:{obj.get('status')}"
        for obj in objects
        if isinstance(obj, dict)
    )
    relation_counts = Counter(
        str(edge.get("relation")) for edge in relations if isinstance(edge, dict)
    )
    trace_event_counts = Counter(
        str(event.get("event_type")) for event in trace if isinstance(event, dict)
    )

    blocked_actions = [
        obj
        for obj in objects
        if isinstance(obj, dict)
        and obj.get("type") == "ACTION"
        and obj.get("status") == "BLOCKED"
    ]
    reopened_transitions = [
        item
        for item in history
        if isinstance(item, dict) and item.get("new_status_or_value") == "REOPENED"
    ]
    invalidated_transitions = [
        item
        for item in history
        if isinstance(item, dict) and item.get("new_status_or_value") == "INVALIDATED"
    ]
    repair_priority_objects = [
        obj
        for obj in objects
        if isinstance(obj, dict)
        and "priority:repair" in list(obj.get("tags", []))
    ]
    support_reassessment_objects = [
        obj
        for obj in objects
        if isinstance(obj, dict)
        and any(
            str(tag).startswith("support_reassessment:")
            for tag in list(obj.get("tags", []))
        )
    ]

    activation_components = [
        str(item.get("component_id"))
        for item in activations
        if isinstance(item, dict)
    ]
    activation_reopen_counts = {
        str(item.get("component_id")): int(item.get("reopen_count", 0))
        for item in activations
        if isinstance(item, dict)
    }

    return {
        "state_step": int(state.get("step", 0)),
        "state_object_count": len(objects),
        "state_relation_count": len(relations),
        "object_type_counts": dict(sorted(object_type_counts.items())),
        "object_status_counts": dict(sorted(object_status_counts.items())),
        "relation_counts": dict(sorted(relation_counts.items())),
        "trace_event_counts": dict(sorted(trace_event_counts.items())),
        "p0_state_control_error_events": int(trace_event_counts.get("P0_STATE_CONTROL_ERROR", 0)),
        "p0_python_budget_block_events": int(trace_event_counts.get("P0_PYTHON_BUDGET_BLOCK", 0)),
        "blocked_action_object_count": len(blocked_actions),
        "reopened_transition_count": len(reopened_transitions),
        "invalidated_transition_count": len(invalidated_transitions),
        "repair_priority_object_count": len(repair_priority_objects),
        "support_reassessment_object_count": len(support_reassessment_objects),
        "knowledge_components_activated": activation_components,
        "knowledge_activation_reopen_counts": activation_reopen_counts,
        "knowledge_reopen_total": sum(activation_reopen_counts.values()),
    }


def build_export_manifest(
    *,
    decoded_result_path: str | Path = DEFAULT_DECODED_RESULT,
    attempts_root: str | Path = DEFAULT_ATTEMPTS_ROOT,
) -> tuple[dict[str, Any], list[tuple[Path, str]]]:
    """Validate and describe the ten retained P0 diagnostic trajectories."""

    decoded_path = Path(decoded_result_path)
    attempts = Path(attempts_root)
    decoded, p0_rows = _load_p0_rows(decoded_path)

    archive_files: list[tuple[Path, str]] = []
    cases: list[dict[str, Any]] = []

    for row in p0_rows:
        attempt_id = str(row["attempt_id"])
        attempt_dir = attempts / attempt_id
        if not attempt_dir.is_dir():
            raise FileNotFoundError(f"Retained P0 attempt directory is missing: {attempt_dir}")

        file_rows: list[dict[str, Any]] = []
        for filename in _REQUIRED_FILES:
            source = attempt_dir / filename
            if not source.is_file():
                raise FileNotFoundError(f"Required P0 diagnostic artifact is missing: {source}")
            arcname = f"attempts/{attempt_id}/{filename}"
            digest = _sha256_file(source)
            file_rows.append(
                {
                    "path": arcname,
                    "sha256": digest,
                    "size_bytes": source.stat().st_size,
                }
            )
            archive_files.append((source, arcname))

        summary = _read_json(attempt_dir / "summary.json")
        if not isinstance(summary, dict) or summary.get("condition") != "P0":
            raise ValueError(f"Attempt is not a P0 retained trajectory: {attempt_id}")
        if str(summary.get("run_id")) != attempt_id:
            raise ValueError(f"P0 attempt summary identity mismatch: {attempt_id}")
        if not bool(summary.get("behavior_evaluable", False)):
            raise ValueError(f"P0 retained attempt is not behavior evaluable: {attempt_id}")

        cases.append(
            {
                "slot_index": int(row["slot_index"]),
                "variant": str(row["variant"]),
                "replicate": int(row["replicate"]),
                "attempt_id": attempt_id,
                "completed": bool(row["completed"]),
                "completed_within_budget": bool(row["completed_within_budget"]),
                "budget_exhausted": bool(row["budget_exhausted"]),
                "targeted_architecture_score": float(row["targeted_architecture_score"]),
                "critical_failure_events": int(row["critical_failure_events"]),
                "structural_diagnostics": _state_structural_summary(attempt_dir),
                "files": file_rows,
            }
        )

    manifest = {
        "schema_version": EXPORT_SCHEMA_VERSION,
        "created_at_utc": _utc_now(),
        "purpose": "post-unblinding P0 architecture-specific diagnostic review",
        "frozen_semantic_aggregate_sha256": str(
            decoded.get("frozen_semantic_aggregate_sha256", "")
        ),
        "decoded_result_schema_version": str(decoded.get("schema_version", "")),
        "p0_case_count": len(cases),
        "cases": cases,
        "boundary": {
            "launches_model_calls": False,
            "mutates_attempt_evidence": False,
            "includes_non_P0_treatment_trajectories": False,
            "includes_semantic_private_decoder": False,
            "performs_final_architecture_classification": False,
        },
    }
    return manifest, archive_files


def export_p0_architecture_diagnostics(
    *,
    decoded_result_path: str | Path = DEFAULT_DECODED_RESULT,
    attempts_root: str | Path = DEFAULT_ATTEMPTS_ROOT,
    export_root: str | Path = DEFAULT_EXPORT_ROOT,
) -> tuple[dict[str, Any], Path]:
    """Create a compact ZIP of the ten retained P0 diagnostic trajectories."""

    manifest, archive_files = build_export_manifest(
        decoded_result_path=decoded_result_path,
        attempts_root=attempts_root,
    )
    exports = Path(export_root)
    exports.mkdir(parents=True, exist_ok=True)
    archive_path = exports / f"p0_architecture_diagnostics_{_timestamp_id()}.zip"

    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(
            "p0_architecture_diagnostic_manifest.json",
            json.dumps(manifest, indent=2, sort_keys=True),
        )
        for source, arcname in archive_files:
            archive.write(source, arcname)

    return manifest, archive_path


def _print_summary(manifest: Mapping[str, Any]) -> None:
    print(f"P0 diagnostic cases: {manifest['p0_case_count']} / 10")
    total_control_errors = sum(
        int(case["structural_diagnostics"]["p0_state_control_error_events"])
        for case in manifest["cases"]
    )
    total_reopens = sum(
        int(case["structural_diagnostics"]["knowledge_reopen_total"])
        for case in manifest["cases"]
    )
    print(f"P0 state-control error events: {total_control_errors}")
    print(f"Knowledge reopen events: {total_reopens}")
    print("Model inference launched: 0")
    print("Attempt evidence mutated: no")
    print("Semantic private decoder included: no")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export retained P0 internal diagnostics after semantic unblinding."
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser(
        "verify",
        help="Validate and summarize P0 diagnostic artifacts without creating a ZIP.",
    )
    sub.add_parser(
        "export",
        help="Validate and export the ten retained P0 diagnostic trajectories.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    if args.command == "verify":
        manifest, _ = build_export_manifest()
        _print_summary(manifest)
        return
    if args.command == "export":
        manifest, archive = export_p0_architecture_diagnostics()
        _print_summary(manifest)
        print(f"P0 diagnostic export: {archive.resolve()}")
        return
    raise AssertionError(f"Unhandled P0 diagnostic-export command: {args.command}")


if __name__ == "__main__":
    main()
