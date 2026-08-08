"""Treatment-neutral runtime for Prototype V0 benchmark experiments.

The runtime provides the common experimental boundary that B0, B1, and P0
will eventually share. It is deliberately small. Its responsibilities are:

* expose only project artifacts that are available in the current phase;
* keep evaluator-only material outside the treatment-facing artifact registry;
* distinguish metadata-level and value-level data access;
* execute Python using only explicitly declared project artifacts;
* record a condition-neutral event trace;
* manage the Phase 1 -> Phase 2 -> final-evaluation transition; and
* optionally enforce the protected-final-test access rule for P0.

The implementation is an experimental harness, not a production sandbox. Python
is executed in a fresh temporary working directory containing copies of only the
declared project artifacts. This prevents accidental relative-path access to the
benchmark bundle and makes the declared-input contract observable. It is not an
OS-level security boundary against deliberately malicious code that searches the
host filesystem. Strong process/container isolation remains a future execution-
environment question outside Prototype V0.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import time
import uuid
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Iterable

import pandas as pd


class ProjectPhase(str, Enum):
    """Experiment phases visible to the treatment runtime."""

    PHASE_1 = "PHASE_1_PROVISIONAL_DEVELOPMENT"
    PHASE_2 = "PHASE_2_REVISED_DEVELOPMENT"
    FINAL_EVALUATION = "FINAL_EVALUATION"


class AccessLevel(str, Enum):
    """Information exposure level for project artifacts."""

    METADATA = "METADATA"
    VALUE = "VALUE"


class ActionCategory(str, Enum):
    """Condition-neutral purpose category used for trajectory evaluation."""

    INSPECTION = "INSPECTION"
    DEVELOPMENT = "DEVELOPMENT"
    FINAL_EVALUATION = "FINAL_EVALUATION"
    REPORTING = "REPORTING"
    PHASE_CONTROL = "PHASE_CONTROL"


@dataclass(frozen=True)
class ArtifactRecord:
    """Internal runtime registration for one project artifact."""

    artifact_id: str
    filename: str
    artifact_kind: str
    role: str
    source_path: Path
    available_from_phase: ProjectPhase


@dataclass(frozen=True)
class TraceEvent:
    """One condition-neutral observable event in an experiment trajectory."""

    sequence: int
    event_id: str
    run_id: str
    condition: str
    event_type: str
    phase: str
    category: str
    purpose: str
    artifacts_requested: tuple[str, ...]
    access_level: str | None
    allowed: bool
    blocked_reason: str | None
    duration_seconds: float | None
    details: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable event representation."""

        return asdict(self)


class ActionBlockedError(RuntimeError):
    """Raised when an enabled prospective runtime safeguard blocks an action."""


class TraceLog:
    """Append-only in-memory trace with optional JSONL persistence."""

    def __init__(self, run_id: str, condition: str, path: Path | None = None) -> None:
        self.run_id = run_id
        self.condition = condition
        self.path = path
        self._events: list[TraceEvent] = []
        if self.path is not None:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self.path.write_text("", encoding="utf-8")

    @property
    def events(self) -> tuple[TraceEvent, ...]:
        return tuple(self._events)

    def append(
        self,
        *,
        event_type: str,
        phase: ProjectPhase,
        category: ActionCategory,
        purpose: str,
        artifacts_requested: Iterable[str] = (),
        access_level: AccessLevel | None = None,
        allowed: bool = True,
        blocked_reason: str | None = None,
        duration_seconds: float | None = None,
        details: dict[str, Any] | None = None,
    ) -> TraceEvent:
        event = TraceEvent(
            sequence=len(self._events) + 1,
            event_id=f"EV-{len(self._events) + 1:05d}-{uuid.uuid4().hex[:8]}",
            run_id=self.run_id,
            condition=self.condition,
            event_type=event_type,
            phase=phase.value,
            category=category.value,
            purpose=purpose,
            artifacts_requested=tuple(artifacts_requested),
            access_level=access_level.value if access_level is not None else None,
            allowed=allowed,
            blocked_reason=blocked_reason,
            duration_seconds=duration_seconds,
            details=details or {},
        )
        self._events.append(event)

        if self.path is not None:
            with self.path.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(event.to_dict(), sort_keys=True) + "\n")

        return event


class ExperimentWorkspace:
    """Common treatment-facing workspace for one generated benchmark case.

    Parameters
    ----------
    bundle_dir:
        Generated case bundle containing ``visible``, ``phase_2``, and
        ``evaluator_only`` directories.
    run_id:
        Experiment-run identifier used in trace records.
    condition:
        Treatment label such as ``B0``, ``B1``, or ``P0``. The workspace does
        not change ordinary capabilities based on this label.
    enforce_protected_final_test:
        Enables the Version 0 prospective final-test safeguard. This should be
        false for B0/B1 and true for P0 when P0 is implemented.
    trace_path:
        Optional JSONL path for persistent condition-neutral trajectory logs.
    """

    def __init__(
        self,
        bundle_dir: str | Path,
        *,
        run_id: str,
        condition: str,
        enforce_protected_final_test: bool = False,
        trace_path: str | Path | None = None,
    ) -> None:
        self.bundle_dir = Path(bundle_dir).resolve()
        self.visible_dir = self.bundle_dir / "visible"
        self.phase_2_dir = self.bundle_dir / "phase_2"
        self.evaluator_dir = self.bundle_dir / "evaluator_only"

        self._manifest = json.loads(
            (self.evaluator_dir / "manifest.json").read_text(encoding="utf-8")
        )
        self._self_test_report = json.loads(
            (self.evaluator_dir / "self_test_report.json").read_text(
                encoding="utf-8"
            )
        )
        if not self._self_test_report.get("passed", False):
            raise ValueError("Benchmark bundle has not passed evaluator self-tests.")

        self.run_id = run_id
        self.condition = condition
        self.enforce_protected_final_test = enforce_protected_final_test
        self.phase = ProjectPhase.PHASE_1
        self.phase_1_report: dict[str, Any] | None = None
        self.final_lock_report: dict[str, Any] | None = None
        self.final_report: dict[str, Any] | None = None

        trace_file = Path(trace_path) if trace_path is not None else None
        self.trace = TraceLog(run_id=run_id, condition=condition, path=trace_file)

        self._artifacts = self._build_artifact_registry()
        self.trace.append(
            event_type="RUN_INITIALIZED",
            phase=self.phase,
            category=ActionCategory.PHASE_CONTROL,
            purpose="Initialize treatment workspace.",
            details={
                "case_id": self._manifest["case_id"],
                "enforce_protected_final_test": self.enforce_protected_final_test,
            },
        )

    def _build_artifact_registry(self) -> dict[str, ArtifactRecord]:
        roles = self._manifest["world_truth"]["artifact_roles"]
        records: dict[str, ArtifactRecord] = {}

        for path in sorted(self.visible_dir.iterdir()):
            if not path.is_file():
                continue
            records[path.name] = ArtifactRecord(
                artifact_id=path.name,
                filename=path.name,
                artifact_kind=_artifact_kind(path),
                role=roles.get(path.name, "project_artifact"),
                source_path=path,
                available_from_phase=ProjectPhase.PHASE_1,
            )

        for path in sorted(self.phase_2_dir.iterdir()):
            if not path.is_file():
                continue
            records[path.name] = ArtifactRecord(
                artifact_id=path.name,
                filename=path.name,
                artifact_kind=_artifact_kind(path),
                role=roles.get(path.name, "phase_2_artifact"),
                source_path=path,
                available_from_phase=ProjectPhase.PHASE_2,
            )

        return records

    @property
    def events(self) -> tuple[TraceEvent, ...]:
        return self.trace.events

    @property
    def case_id(self) -> str:
        return str(self._manifest["case_id"])

    def list_artifacts(self) -> list[dict[str, str]]:
        """List currently visible project artifacts without evaluator-only data."""

        visible = []
        for artifact in self._artifacts.values():
            if self._is_available(artifact):
                visible.append(
                    {
                        "artifact_id": artifact.artifact_id,
                        "filename": artifact.filename,
                        "kind": artifact.artifact_kind,
                    }
                )

        self.trace.append(
            event_type="LIST_ARTIFACTS",
            phase=self.phase,
            category=ActionCategory.INSPECTION,
            purpose="List project artifacts currently visible to the treatment.",
            details={"visible_count": len(visible)},
        )
        return sorted(visible, key=lambda item: item["artifact_id"])

    def read_text(
        self,
        artifact_id: str,
        *,
        purpose: str,
        category: ActionCategory = ActionCategory.INSPECTION,
    ) -> str:
        artifact = self._get_visible_artifact(artifact_id)
        if artifact.artifact_kind not in {"markdown", "python", "text"}:
            raise TypeError(f"{artifact_id} is not a text artifact.")

        self._enforce_or_log_access(
            artifact,
            AccessLevel.VALUE,
            event_type="READ_TEXT",
            category=category,
            purpose=purpose,
        )
        return artifact.source_path.read_text(encoding="utf-8")

    def table_metadata(self, artifact_id: str, *, purpose: str) -> dict[str, Any]:
        artifact = self._get_visible_artifact(artifact_id)
        if artifact.artifact_kind != "csv":
            raise TypeError(f"{artifact_id} is not a CSV artifact.")

        frame = pd.read_csv(artifact.source_path)
        metadata = {
            "rows": int(len(frame)),
            "columns": list(frame.columns),
            "dtypes": {name: str(dtype) for name, dtype in frame.dtypes.items()},
        }
        self._enforce_or_log_access(
            artifact,
            AccessLevel.METADATA,
            event_type="TABLE_METADATA",
            category=ActionCategory.INSPECTION,
            purpose=purpose,
            details=metadata,
        )
        return metadata

    def table_sample(
        self,
        artifact_id: str,
        *,
        purpose: str,
        rows: int = 5,
    ) -> list[dict[str, Any]]:
        artifact = self._get_visible_artifact(artifact_id)
        if artifact.artifact_kind != "csv":
            raise TypeError(f"{artifact_id} is not a CSV artifact.")
        if rows <= 0 or rows > 100:
            raise ValueError("rows must be between 1 and 100.")

        self._enforce_or_log_access(
            artifact,
            AccessLevel.VALUE,
            event_type="TABLE_SAMPLE",
            category=ActionCategory.INSPECTION,
            purpose=purpose,
            details={"rows_requested": rows},
        )
        return pd.read_csv(artifact.source_path, nrows=rows).to_dict(orient="records")

    def execute_python(
        self,
        code: str,
        *,
        input_artifacts: Iterable[str],
        purpose: str,
        category: ActionCategory,
        timeout_seconds: int = 60,
    ) -> dict[str, Any]:
        """Execute Python against only explicitly declared project artifacts."""

        artifact_ids = tuple(dict.fromkeys(input_artifacts))
        artifacts = [self._get_visible_artifact(item) for item in artifact_ids]

        blocked_reason = self._blocked_reason_for_accesses(
            artifacts,
            AccessLevel.VALUE,
        )
        if blocked_reason is not None and self.enforce_protected_final_test:
            self.trace.append(
                event_type="EXECUTE_PYTHON",
                phase=self.phase,
                category=category,
                purpose=purpose,
                artifacts_requested=artifact_ids,
                access_level=AccessLevel.VALUE,
                allowed=False,
                blocked_reason=blocked_reason,
            )
            raise ActionBlockedError(blocked_reason)

        started = time.perf_counter()
        with tempfile.TemporaryDirectory(prefix="ads-v0-run-") as temp_name:
            temp_dir = Path(temp_name)
            for artifact in artifacts:
                shutil.copy2(artifact.source_path, temp_dir / artifact.filename)

            script = temp_dir / "analysis.py"
            script.write_text(code, encoding="utf-8")

            try:
                completed = subprocess.run(
                    [sys.executable, script.name],
                    cwd=temp_dir,
                    capture_output=True,
                    text=True,
                    timeout=timeout_seconds,
                    check=False,
                )
                timed_out = False
                stdout = completed.stdout
                stderr = completed.stderr
                return_code = int(completed.returncode)
            except subprocess.TimeoutExpired as exc:
                timed_out = True
                stdout = exc.stdout or ""
                stderr = exc.stderr or ""
                return_code = -1

            generated_files = sorted(
                path.name
                for path in temp_dir.iterdir()
                if path.is_file()
                and path.name not in {artifact.filename for artifact in artifacts}
                and path.name != script.name
            )

        duration = time.perf_counter() - started
        details = {
            "stdout": stdout,
            "stderr": stderr,
            "return_code": return_code,
            "timed_out": timed_out,
            "generated_files": generated_files,
        }
        self.trace.append(
            event_type="EXECUTE_PYTHON",
            phase=self.phase,
            category=category,
            purpose=purpose,
            artifacts_requested=artifact_ids,
            access_level=AccessLevel.VALUE,
            allowed=True,
            blocked_reason=blocked_reason,
            duration_seconds=duration,
            details=details,
        )
        return details

    def signal_phase_1_complete(self, report: dict[str, Any]) -> None:
        if self.phase is not ProjectPhase.PHASE_1:
            raise RuntimeError("Phase 1 can only be completed once from Phase 1.")

        self.phase_1_report = dict(report)
        self.trace.append(
            event_type="PHASE_1_COMPLETE",
            phase=self.phase,
            category=ActionCategory.PHASE_CONTROL,
            purpose="Record provisional development position and release Phase 2 information.",
            details={"report": self.phase_1_report},
        )
        self.phase = ProjectPhase.PHASE_2
        self.trace.append(
            event_type="PHASE_2_STARTED",
            phase=self.phase,
            category=ActionCategory.PHASE_CONTROL,
            purpose="Expose the authoritative Phase 2 timing notice.",
            details={"released_artifacts": ["crm_field_timing_notice.md"]},
        )

    def signal_final_model_locked(self, report: dict[str, Any]) -> None:
        if self.phase is not ProjectPhase.PHASE_2:
            raise RuntimeError("Final model can only be locked after Phase 2.")

        self.final_lock_report = dict(report)
        self.trace.append(
            event_type="FINAL_MODEL_LOCKED",
            phase=self.phase,
            category=ActionCategory.PHASE_CONTROL,
            purpose="Freeze development choices before protected final evaluation.",
            details={"report": self.final_lock_report},
        )
        self.phase = ProjectPhase.FINAL_EVALUATION
        self.trace.append(
            event_type="FINAL_EVALUATION_STARTED",
            phase=self.phase,
            category=ActionCategory.PHASE_CONTROL,
            purpose="Permit protected final-evaluation access after development lock.",
        )

    def submit_final_report(self, report: dict[str, Any]) -> None:
        if self.phase is not ProjectPhase.FINAL_EVALUATION:
            raise RuntimeError("Final report requires the final-evaluation phase.")
        self.final_report = dict(report)
        self.trace.append(
            event_type="FINAL_REPORT_SUBMITTED",
            phase=self.phase,
            category=ActionCategory.REPORTING,
            purpose="Submit the condition-neutral final project report.",
            details={"report": self.final_report},
        )

    def _get_visible_artifact(self, artifact_id: str) -> ArtifactRecord:
        if artifact_id not in self._artifacts:
            raise KeyError(f"Unknown project artifact: {artifact_id}")
        artifact = self._artifacts[artifact_id]
        if not self._is_available(artifact):
            raise PermissionError(
                f"Artifact {artifact_id!r} is not available in phase {self.phase.value}."
            )
        return artifact

    def _is_available(self, artifact: ArtifactRecord) -> bool:
        if artifact.available_from_phase is ProjectPhase.PHASE_1:
            return True
        if artifact.available_from_phase is ProjectPhase.PHASE_2:
            return self.phase in {ProjectPhase.PHASE_2, ProjectPhase.FINAL_EVALUATION}
        return self.phase is ProjectPhase.FINAL_EVALUATION

    def _blocked_reason_for_accesses(
        self,
        artifacts: Iterable[ArtifactRecord],
        access_level: AccessLevel,
    ) -> str | None:
        if access_level is not AccessLevel.VALUE:
            return None
        if self.phase is ProjectPhase.FINAL_EVALUATION:
            return None

        protected = [
            artifact.filename
            for artifact in artifacts
            if artifact.role == "protected_final_evaluation"
        ]
        if protected:
            return (
                "Protected final-evaluation values are unavailable for development: "
                + ", ".join(protected)
            )
        return None

    def _enforce_or_log_access(
        self,
        artifact: ArtifactRecord,
        access_level: AccessLevel,
        *,
        event_type: str,
        category: ActionCategory,
        purpose: str,
        details: dict[str, Any] | None = None,
    ) -> None:
        blocked_reason = self._blocked_reason_for_accesses([artifact], access_level)
        if blocked_reason is not None and self.enforce_protected_final_test:
            self.trace.append(
                event_type=event_type,
                phase=self.phase,
                category=category,
                purpose=purpose,
                artifacts_requested=[artifact.artifact_id],
                access_level=access_level,
                allowed=False,
                blocked_reason=blocked_reason,
                details=details,
            )
            raise ActionBlockedError(blocked_reason)

        self.trace.append(
            event_type=event_type,
            phase=self.phase,
            category=category,
            purpose=purpose,
            artifacts_requested=[artifact.artifact_id],
            access_level=access_level,
            allowed=True,
            blocked_reason=blocked_reason,
            details=details,
        )


def _artifact_kind(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return "csv"
    if suffix == ".md":
        return "markdown"
    if suffix == ".py":
        return "python"
    return "text"
