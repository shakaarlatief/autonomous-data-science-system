"""Mechanically verify and cryptographically freeze completed blinded semantic evidence.

This module operates strictly after semantic-judge execution. It launches no model
calls, performs no new semantic scoring, and never reads the private condition
decoder. Its purpose is to establish a stable blinded boundary before any
B0/B1/P0 identity is revealed.

For the current Prototype V0 result no manual adjudication is required. The freeze
therefore requires every blinded case to contain two persisted judge passes and a
consensus whose registered mechanical combination is already final. If any case
still requires manual adjudication, freezing refuses to proceed until a separate
blinded adjudication artifact exists and the freeze contract is extended to cover
it explicitly.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

from .semantic_judge import combine_judge_passes, packet_fingerprint
from .semantic_judge_supervisor import (
    BATCH_DIR,
    BLINDED_DIR,
    DEFAULT_SEMANTIC_ROOT,
    PREPARED_MANIFEST_FILE,
    PROVIDER_ATTEMPTS_DIR,
)


FREEZE_SCHEMA_VERSION = "semantic_judge_blinded_freeze_v0_1"
FREEZE_FILE = "blinded_freeze.json"
DEFAULT_FREEZE_EXPORT_ROOT = Path("results/held_out/semantic_judge_freeze_exports")


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


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _aggregate_sha256(entries: list[dict[str, Any]]) -> str:
    canonical = json.dumps(
        [
            {"path": str(entry["path"]), "sha256": str(entry["sha256"])}
            for entry in sorted(entries, key=lambda item: str(item["path"]))
        ],
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _provider_attempt_files(case_dir: Path) -> list[Path]:
    provider_dir = case_dir / PROVIDER_ATTEMPTS_DIR
    if not provider_dir.exists():
        return []
    return sorted(path for path in provider_dir.glob("*.json") if path.is_file())


def verify_blinded_state(
    *,
    semantic_root: str | Path = DEFAULT_SEMANTIC_ROOT,
) -> dict[str, Any]:
    """Verify that the 30-case blinded consensus state is complete and immutable-ready."""

    root = Path(semantic_root)
    manifest_path = root / PREPARED_MANIFEST_FILE
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Missing prepared semantic manifest: {manifest_path}")

    manifest = _read_json(manifest_path)
    rows = manifest.get("cases")
    if not isinstance(rows, list) or len(rows) != 30:
        raise ValueError("Prepared semantic manifest must contain exactly 30 cases.")

    seen_blind_ids: set[str] = set()
    file_entries: list[dict[str, Any]] = []
    case_summaries: list[dict[str, Any]] = []
    logical_passes = 0
    completed_cases = 0
    manual_cases = 0
    provider_started = 0
    provider_success = 0
    provider_error = 0

    file_entries.append(
        {
            "path": PREPARED_MANIFEST_FILE,
            "sha256": _sha256_file(manifest_path),
        }
    )

    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Prepared semantic case entry must be a JSON object.")
        blind_id = str(row.get("blind_id", ""))
        expected_packet_sha = str(row.get("packet_sha256", ""))
        if not blind_id or blind_id in seen_blind_ids or not expected_packet_sha:
            raise ValueError("Prepared semantic manifest contains invalid case identity.")
        seen_blind_ids.add(blind_id)

        case_dir = root / BLINDED_DIR / blind_id
        packet_path = case_dir / "packet.json"
        first_path = case_dir / "pass_1.json"
        second_path = case_dir / "pass_2.json"
        consensus_path = case_dir / "consensus.json"
        required = [packet_path, first_path, second_path, consensus_path]
        missing = [path for path in required if not path.is_file()]
        if missing:
            raise FileNotFoundError(
                f"Blinded case {blind_id} is incomplete: "
                + ", ".join(path.name for path in missing)
            )

        packet = _read_json(packet_path)
        observed_packet_sha = packet_fingerprint(packet)
        if observed_packet_sha != expected_packet_sha:
            raise ValueError(f"Packet fingerprint mismatch for {blind_id}.")

        first = _read_json(first_path)
        second = _read_json(second_path)
        if int(first.get("pass_number", 0)) != 1:
            raise ValueError(f"Invalid pass_1 identity for {blind_id}.")
        if int(second.get("pass_number", 0)) != 2:
            raise ValueError(f"Invalid pass_2 identity for {blind_id}.")
        if str(first.get("packet_sha256", "")) != expected_packet_sha:
            raise ValueError(f"pass_1 packet fingerprint mismatch for {blind_id}.")
        if str(second.get("packet_sha256", "")) != expected_packet_sha:
            raise ValueError(f"pass_2 packet fingerprint mismatch for {blind_id}.")

        persisted_consensus = _read_json(consensus_path)
        consensus_payload = persisted_consensus.get("consensus")
        if not isinstance(consensus_payload, dict):
            raise ValueError(f"Consensus payload missing for {blind_id}.")
        recomputed = combine_judge_passes(first, second)
        if consensus_payload != recomputed:
            raise ValueError(f"Persisted consensus drift detected for {blind_id}.")

        manual_required = bool(recomputed.get("manual_adjudication_required", False))
        if manual_required:
            manual_cases += 1

        logical_passes += 2
        completed_cases += 1

        case_files = [packet_path, first_path, second_path, consensus_path]
        provider_files = _provider_attempt_files(case_dir)
        case_files.extend(provider_files)

        case_provider_started = 0
        case_provider_success = 0
        case_provider_error = 0
        for provider_path in provider_files:
            if provider_path.name.endswith("_started.json"):
                provider_started += 1
                case_provider_started += 1
            elif provider_path.name.endswith("_success.json"):
                provider_success += 1
                case_provider_success += 1
            elif provider_path.name.endswith("_error.json"):
                provider_error += 1
                case_provider_error += 1

        if case_provider_started != case_provider_success + case_provider_error:
            raise ValueError(
                f"Provider-attempt terminal-marker mismatch for {blind_id}: "
                f"started={case_provider_started}, success={case_provider_success}, "
                f"error={case_provider_error}."
            )

        for path in case_files:
            relative = path.relative_to(root).as_posix()
            file_entries.append({"path": relative, "sha256": _sha256_file(path)})

        case_summaries.append(
            {
                "blind_id": blind_id,
                "packet_sha256": expected_packet_sha,
                "manual_adjudication_required": manual_required,
                "provider_attempts_started": case_provider_started,
                "provider_attempts_succeeded": case_provider_success,
                "provider_attempts_failed": case_provider_error,
            }
        )

    batch_root = root / BATCH_DIR
    batch_files = sorted(batch_root.glob("*.json")) if batch_root.exists() else []
    for path in batch_files:
        file_entries.append(
            {
                "path": path.relative_to(root).as_posix(),
                "sha256": _sha256_file(path),
            }
        )

    if completed_cases != 30 or logical_passes != 60:
        raise ValueError(
            f"Blinded state is not complete: cases={completed_cases}, passes={logical_passes}."
        )
    if manual_cases:
        raise RuntimeError(
            "Blinded consensus cannot be frozen yet because manual adjudication is "
            f"required for {manual_cases} case(s)."
        )
    if provider_started != provider_success + provider_error:
        raise ValueError("Global provider-attempt accounting does not reconcile.")

    aggregate = _aggregate_sha256(file_entries)
    return {
        "schema_version": FREEZE_SCHEMA_VERSION,
        "verified_at_utc": _utc_now(),
        "prepared_cases": len(rows),
        "logical_passes": logical_passes,
        "completed_cases": completed_cases,
        "manual_adjudication_cases": manual_cases,
        "provider_attempts_started": provider_started,
        "provider_attempts_succeeded": provider_success,
        "provider_attempts_failed": provider_error,
        "batch_record_count": len(batch_files),
        "decoder_read": False,
        "file_count": len(file_entries),
        "aggregate_sha256": aggregate,
        "cases": sorted(case_summaries, key=lambda item: item["blind_id"]),
        "files": sorted(file_entries, key=lambda item: item["path"]),
    }


def freeze_blinded_state(
    *,
    semantic_root: str | Path = DEFAULT_SEMANTIC_ROOT,
    export_root: str | Path = DEFAULT_FREEZE_EXPORT_ROOT,
) -> tuple[dict[str, Any], Path]:
    """Persist a stable freeze manifest and export the exact blinded evidence."""

    root = Path(semantic_root)
    verification = verify_blinded_state(semantic_root=root)
    freeze_path = root / FREEZE_FILE

    payload = dict(verification)
    payload["frozen_at_utc"] = _utc_now()
    payload["status"] = "FROZEN_BLINDED_CONSENSUS"

    if freeze_path.exists():
        existing = _read_json(freeze_path)
        if str(existing.get("aggregate_sha256")) != str(payload["aggregate_sha256"]):
            raise ValueError(
                "Existing blinded freeze manifest disagrees with current evidence. "
                "Refusing to overwrite a prior freeze."
            )
        payload = existing
    else:
        _write_json(freeze_path, payload)

    exports = Path(export_root)
    exports.mkdir(parents=True, exist_ok=True)
    archive_path = exports / f"semantic_judge_frozen_blinded_{_timestamp_id()}.zip"

    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.write(freeze_path, FREEZE_FILE)
        for entry in payload["files"]:
            relative = Path(str(entry["path"]))
            source = root / relative
            if not source.is_file():
                raise FileNotFoundError(
                    f"Frozen source file disappeared before export: {source}"
                )
            if _sha256_file(source) != str(entry["sha256"]):
                raise ValueError(
                    f"Frozen source file changed before export: {relative.as_posix()}"
                )
            archive.write(source, relative.as_posix())

    return payload, archive_path


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify and freeze completed condition-blind semantic evidence."
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser(
        "verify",
        help="Mechanically verify completed blinded semantic evidence without writing a freeze.",
    )
    sub.add_parser(
        "freeze",
        help="Verify, persist the blinded freeze manifest, and create a decoder-free ZIP.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    if args.command == "verify":
        result = verify_blinded_state()
        print(f"Prepared cases verified: {result['prepared_cases']} / 30")
        print(f"Logical passes verified: {result['logical_passes']} / 60")
        print(f"Completed cases verified: {result['completed_cases']} / 30")
        print(f"Manual-adjudication cases: {result['manual_adjudication_cases']}")
        print(f"Provider attempts: {result['provider_attempts_started']}")
        print(f"Aggregate SHA-256: {result['aggregate_sha256']}")
        print("Private decoder read: no")
        return
    if args.command == "freeze":
        result, archive = freeze_blinded_state()
        print("Blinded consensus status: FROZEN")
        print(f"Prepared cases: {result['prepared_cases']} / 30")
        print(f"Logical passes: {result['logical_passes']} / 60")
        print(f"Completed cases: {result['completed_cases']} / 30")
        print(f"Manual-adjudication cases: {result['manual_adjudication_cases']}")
        print(f"Provider attempts: {result['provider_attempts_started']}")
        print(f"Aggregate SHA-256: {result['aggregate_sha256']}")
        print("Private decoder read: no")
        print(f"Frozen blinded export: {archive.resolve()}")
        return
    raise AssertionError(f"Unhandled command: {args.command}")


if __name__ == "__main__":
    main()
