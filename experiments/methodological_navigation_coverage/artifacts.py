"""Attempt accounting and raw-before-interpretation safeguards for Specification 022."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
from typing import Mapping

from experiments.methodological_navigation_coverage.contract import (
    MAX_RETRIES_PER_OBSERVATION,
    MAX_TOTAL_PROVIDER_ATTEMPTS,
    canonical_json_bytes,
)

_ALLOWED_RETRY_REASONS = {"TRANSIENT_PROVIDER_FAILURE", "INVALID_STRUCTURED_OUTPUT"}
_RAW_STREAMS = {
    "requests",
    "navigation",
    "reasoner_attempts",
    "judge_attempts",
    "usage",
}


@dataclass(frozen=True, slots=True)
class AttemptRecord:
    role: str
    observation_id: str
    attempt_number: int
    retry_reason: str | None


class AttemptBudget:
    """Fail closed on the frozen global and per-observation attempt ceilings."""

    def __init__(self) -> None:
        self._records: list[AttemptRecord] = []
        self._counts: dict[tuple[str, str], int] = {}

    @property
    def records(self) -> tuple[AttemptRecord, ...]:
        return tuple(self._records)

    @property
    def total_attempts(self) -> int:
        return len(self._records)

    def record_attempt(
        self,
        *,
        role: str,
        observation_id: str,
        retry_reason: str | None = None,
    ) -> AttemptRecord:
        if role not in {"reasoner", "judge"}:
            raise ValueError("role must be reasoner or judge")
        if not observation_id.strip():
            raise ValueError("observation_id must be non-empty")
        key = (role, observation_id)
        previous = self._counts.get(key, 0)
        attempt_number = previous + 1
        if attempt_number > 1 + MAX_RETRIES_PER_OBSERVATION:
            raise RuntimeError(
                f"{role} {observation_id} exceeded the frozen retry ceiling"
            )
        if attempt_number == 1 and retry_reason is not None:
            raise ValueError("first attempt must not have a retry reason")
        if attempt_number > 1 and retry_reason not in _ALLOWED_RETRY_REASONS:
            raise ValueError(
                "retry reason must be transient provider failure or invalid structured output"
            )
        if self.total_attempts + 1 > MAX_TOTAL_PROVIDER_ATTEMPTS:
            raise RuntimeError("Specification 022 global provider-attempt ceiling exceeded")
        record = AttemptRecord(
            role=role,
            observation_id=observation_id,
            attempt_number=attempt_number,
            retry_reason=retry_reason,
        )
        self._counts[key] = attempt_number
        self._records.append(record)
        return record


class RawEvidenceWriter:
    """Write append-only raw streams and require sealing before interpretation."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self.raw_dir = root / "raw"
        self.interpretation_dir = root / "interpretation"
        self.manifest_path = root / "raw_manifest.json"
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self._sealed = self.manifest_path.exists()

    @property
    def sealed(self) -> bool:
        return self._sealed

    def append(self, stream: str, payload: Mapping[str, object]) -> None:
        if self._sealed:
            raise RuntimeError("raw evidence is sealed and cannot be modified")
        if stream not in _RAW_STREAMS:
            raise ValueError(f"unsupported raw evidence stream: {stream}")
        path = self.raw_dir / f"{stream}.jsonl"
        line = canonical_json_bytes(dict(payload)).decode("utf-8")
        with path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(line + "\n")

    def seal(self) -> dict[str, object]:
        if self._sealed:
            return json.loads(self.manifest_path.read_text(encoding="utf-8"))
        files: dict[str, dict[str, object]] = {}
        for path in sorted(self.raw_dir.glob("*.jsonl"), key=lambda item: item.name):
            payload = path.read_bytes()
            files[path.name] = {
                "bytes": len(payload),
                "sha256": hashlib.sha256(payload).hexdigest(),
            }
        manifest = {
            "schema_version": 1,
            "raw_evidence_sealed": True,
            "files": files,
        }
        self.manifest_path.write_bytes(canonical_json_bytes(manifest) + b"\n")
        self._sealed = True
        return manifest

    def write_interpretation(
        self,
        name: str,
        payload: Mapping[str, object],
    ) -> Path:
        if not self._sealed:
            raise RuntimeError(
                "raw evidence must be sealed before interpretation is written"
            )
        if not name.strip() or "/" in name or "\\" in name:
            raise ValueError("interpretation name must be a simple non-empty filename")
        self.interpretation_dir.mkdir(parents=True, exist_ok=True)
        path = self.interpretation_dir / name
        path.write_bytes(canonical_json_bytes(dict(payload)) + b"\n")
        return path
