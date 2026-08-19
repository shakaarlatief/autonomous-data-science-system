"""Resumable blinded semantic-evaluation orchestration for Prototype V0.

This module automates the held-out semantic-judge stage without changing the
frozen treatment trajectories or the preregistered semantic rubric. It sits
outside treatment execution and uses the already-calibrated judge implementation
in :mod:`ads_v0.semantic_judge`.

The supervisor has five design goals.

1. **Preserve condition blindness.** Exactly one behavior-evaluable retained
   trajectory is discovered for each of the 30 frozen treatment slots. Each
   trajectory is converted to the common external judge packet and assigned an
   opaque identifier derived only from the packet fingerprint. The mapping back
   to slot/condition identity is written to a separate private decoder file that
   is never included in blinded review exports.
2. **Make paid judge work resumable.** Each logical judge pass is persisted as
   soon as it completes. A later invocation never reruns an already persisted
   valid pass.
3. **Separate provider transport attempts from logical judge passes.** The
   preregistered outcome requires two completed independent judgments per
   trajectory. If a provider call fails before producing a usable judgment, the
   supervisor may make another fresh provider attempt for that same logical pass,
   up to a fixed condition-neutral limit. Failed transport calls are logged but
   never interpreted as semantic evidence.
4. **Avoid midstream unblinding.** Batch progress reports expose opaque case
   identifiers and completion/adjudication status only. They do not print
   condition labels, treatment run identifiers, score vectors, or aggregate
   condition comparisons.
5. **Keep manual adjudication blind.** The export command packages packets,
   judge-pass outputs, consensus files, and provider-attempt metadata under
   opaque case identifiers while explicitly excluding the private decoder.

The provider-recovery rule in this module is operational rather than semantic:
there may be at most three provider attempts to obtain one usable logical judge
pass. A completed judgment is never rerun merely because its score is surprising
or inconvenient. This rule is established before any held-out semantic-judge
call is launched and is applied identically to every blinded case.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Mapping

from .heldout_execution import DEFAULT_BUNDLE_ROOT, HeldOutSlot, attempt_id
from .heldout_runner import (
    DEFAULT_ATTEMPTS_ROOT,
    determine_next_status,
    load_and_validate_materialized_plan,
)
from .model import ModelGenerationError
from .semantic_judge import (
    OpenAISemanticJudge,
    assert_packet_blinded,
    build_blinded_judge_packet,
    combine_judge_passes,
    packet_fingerprint,
)


DEFAULT_SEMANTIC_ROOT = Path("results/held_out/semantic_judge")
DEFAULT_EXPORT_ROOT = Path("results/held_out/semantic_judge_exports")
PREPARED_MANIFEST_FILE = "prepared_manifest.json"
PRIVATE_DECODER_FILE = "private_decoder.json"
BLINDED_DIR = "blinded"
BATCH_DIR = "batches"
PROVIDER_ATTEMPTS_DIR = "provider_attempts"

JUDGE_MODEL = "gpt-5.6-terra"
JUDGE_REASONING_EFFORT = "high"
JUDGE_MAX_OUTPUT_TOKENS = 30_000
MAX_PROVIDER_ATTEMPTS_PER_LOGICAL_PASS = 3
LOGICAL_PASSES = (1, 2)
MAX_TREATMENT_ATTEMPTS_PER_SLOT = 3


@dataclass(frozen=True)
class RetainedTrajectory:
    """Private mapping from one frozen slot to its retained treatment attempt."""

    slot: HeldOutSlot
    attempt_number: int
    attempt_id: str
    run_dir: Path
    bundle_dir: Path


@dataclass(frozen=True)
class BlindedCase:
    """Condition-neutral identity for one semantic-evaluation case."""

    blind_id: str
    packet_sha256: str
    packet_path: Path


@dataclass(frozen=True)
class JudgeBatchResult:
    """Mechanical result of one resumable semantic-judge batch invocation."""

    batch_id: str
    provider_calls_launched: int
    logical_passes_persisted: int
    completed_cases: int
    manual_adjudication_cases: int
    stop_reason: str
    next_blind_id: str | None
    next_logical_pass: int | None
    export_path: str


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


def _canonical_json(payload: Mapping[str, Any]) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)


def _opaque_blind_id(packet_sha256: str) -> str:
    """Derive a stable opaque identifier without using slot or condition identity."""

    digest = hashlib.sha256(
        f"prototype-v0-semantic-blind:{packet_sha256}".encode("utf-8")
    ).hexdigest()
    return f"case-{digest[:16]}"


def _all_forbidden_execution_tokens(slots: tuple[HeldOutSlot, ...]) -> list[str]:
    """Return identifiers that must never appear in a common judge packet."""

    tokens = ["B0", "B1", "P0"]
    for slot in slots:
        tokens.append(slot.slot_id)
        for number in range(1, MAX_TREATMENT_ATTEMPTS_PER_SLOT + 1):
            tokens.append(attempt_id(slot, number))
    return tokens


def _discover_retained_trajectory(
    *,
    slot: HeldOutSlot,
    attempts_root: Path,
    bundle_root: Path,
) -> RetainedTrajectory:
    """Find exactly one behavior-evaluable slot-resolving attempt.

    The held-out runner has already enforced replacement semantics. This function
    nevertheless rechecks the persisted attempt records because semantic judging
    must never accidentally select a provider-failure attempt or more than one
    trajectory from the same preregistered slot.
    """

    retained: list[RetainedTrajectory] = []
    saw_resolved = False

    for number in range(1, MAX_TREATMENT_ATTEMPTS_PER_SLOT + 1):
        current_id = attempt_id(slot, number)
        run_dir = attempts_root / current_id
        record_path = run_dir / "attempt_record.json"
        if not record_path.is_file():
            continue

        record = _read_json(record_path)
        record_slot = record.get("slot")
        if not isinstance(record_slot, Mapping):
            raise ValueError(f"Attempt record lacks slot metadata: {record_path}")
        if str(record_slot.get("slot_id")) != slot.slot_id:
            raise ValueError(f"Attempt record slot mismatch: {record_path}")
        if str(record.get("attempt_id")) != current_id:
            raise ValueError(f"Attempt record identity mismatch: {record_path}")

        slot_resolved = bool(record.get("slot_resolved", False))
        behavior_evaluable = bool(record.get("behavior_evaluable", False))

        if slot_resolved:
            if saw_resolved:
                raise ValueError(
                    f"Multiple slot-resolving attempts found for {slot.slot_id}."
                )
            saw_resolved = True
            if not behavior_evaluable:
                raise ValueError(
                    f"Resolved attempt is unexpectedly non-behavior-evaluable: {current_id}."
                )
            if str(record.get("classification")) != "BEHAVIOR_EVALUABLE":
                raise ValueError(
                    f"Resolved attempt classification mismatch: {current_id}."
                )
            retained.append(
                RetainedTrajectory(
                    slot=slot,
                    attempt_number=number,
                    attempt_id=current_id,
                    run_dir=run_dir,
                    bundle_dir=bundle_root / slot.variant,
                )
            )

    if len(retained) != 1:
        raise ValueError(
            f"Expected exactly one retained behavior-evaluable trajectory for "
            f"{slot.slot_id}, found {len(retained)}."
        )
    return retained[0]


def _validate_experiment_complete(
    *,
    attempts_root: Path,
) -> tuple[dict[str, Any], tuple[HeldOutSlot, ...]]:
    """Require the frozen 30-slot treatment experiment to be fully resolved."""

    plan, slots, _ = load_and_validate_materialized_plan()
    status = determine_next_status(slots=slots, attempts_root=attempts_root)
    if status.status != "EXPERIMENT_COMPLETE":
        raise RuntimeError(
            "Semantic judging is forbidden until held-out treatment execution is "
            f"complete. Current runner status: {status.status}."
        )
    if len(slots) != 30:
        raise ValueError(f"Expected 30 frozen held-out slots, found {len(slots)}.")
    return plan, slots


def prepare_blinded_cases(
    *,
    semantic_root: str | Path = DEFAULT_SEMANTIC_ROOT,
    attempts_root: str | Path = DEFAULT_ATTEMPTS_ROOT,
    bundle_root: str | Path = DEFAULT_BUNDLE_ROOT,
) -> dict[str, Any]:
    """Build and persist all 30 blinded judge packets without model inference.

    Preparation is idempotent. If a prior private decoder or packet exists, its
    contents must exactly match the freshly reconstructed frozen evidence. This
    prevents accidental remapping or silent packet drift between invocations.
    """

    root = Path(semantic_root)
    attempts = Path(attempts_root)
    bundles = Path(bundle_root)
    _, slots = _validate_experiment_complete(attempts_root=attempts)

    forbidden_tokens = _all_forbidden_execution_tokens(slots)
    blinded_root = root / BLINDED_DIR
    blinded_root.mkdir(parents=True, exist_ok=True)

    decoder_rows: list[dict[str, Any]] = []
    manifest_rows: list[dict[str, Any]] = []
    seen_blind_ids: set[str] = set()
    seen_packet_hashes: set[str] = set()

    for slot in slots:
        retained = _discover_retained_trajectory(
            slot=slot,
            attempts_root=attempts,
            bundle_root=bundles,
        )
        packet = build_blinded_judge_packet(
            bundle_dir=retained.bundle_dir,
            run_dir=retained.run_dir,
        )

        # The packet builder already rejects the current run/condition identity.
        # A global second pass protects against leakage of any other frozen
        # execution identifier and makes the invariant explicit at orchestration
        # level rather than relying only on one run's summary metadata.
        assert_packet_blinded(packet, forbidden_tokens=forbidden_tokens)

        packet_sha = packet_fingerprint(packet)
        blind_id = _opaque_blind_id(packet_sha)
        if blind_id in seen_blind_ids or packet_sha in seen_packet_hashes:
            raise ValueError(
                "Blinded semantic cases are not uniquely identifiable by packet fingerprint."
            )
        seen_blind_ids.add(blind_id)
        seen_packet_hashes.add(packet_sha)

        case_dir = blinded_root / blind_id
        packet_path = case_dir / "packet.json"
        case_dir.mkdir(parents=True, exist_ok=True)
        if packet_path.exists():
            existing = _read_json(packet_path)
            if _canonical_json(existing) != _canonical_json(packet):
                raise ValueError(f"Existing blinded packet drift detected: {packet_path}")
        else:
            _write_json(packet_path, packet)

        manifest_rows.append(
            {
                "blind_id": blind_id,
                "packet_sha256": packet_sha,
            }
        )
        decoder_rows.append(
            {
                "blind_id": blind_id,
                "packet_sha256": packet_sha,
                "slot": asdict(slot),
                "attempt_number": retained.attempt_number,
                "attempt_id": retained.attempt_id,
                "run_dir": retained.run_dir.as_posix(),
                "bundle_dir": retained.bundle_dir.as_posix(),
            }
        )

    # Judge execution order is based on the opaque identifier, not on frozen
    # treatment order. This avoids making the evaluation sequence a trivial
    # encoding of B0/B1/P0 order for a later human blinded adjudicator.
    manifest_rows.sort(key=lambda row: str(row["blind_id"]))
    decoder_rows.sort(key=lambda row: str(row["blind_id"]))

    manifest = {
        "schema_version": "semantic_judge_supervisor_v0_1",
        "prepared_at_utc": _utc_now(),
        "case_count": len(manifest_rows),
        "judge_model": JUDGE_MODEL,
        "reasoning_effort": JUDGE_REASONING_EFFORT,
        "max_output_tokens": JUDGE_MAX_OUTPUT_TOKENS,
        "logical_passes_per_case": len(LOGICAL_PASSES),
        "max_provider_attempts_per_logical_pass": MAX_PROVIDER_ATTEMPTS_PER_LOGICAL_PASS,
        "cases": manifest_rows,
    }
    decoder = {
        "schema_version": "semantic_judge_private_decoder_v0_1",
        "warning": (
            "PRIVATE DECODER. Do not inspect or export until all required blinded "
            "manual adjudications are frozen."
        ),
        "case_count": len(decoder_rows),
        "cases": decoder_rows,
    }

    if len(manifest_rows) != 30 or len(decoder_rows) != 30:
        raise ValueError("Semantic preparation must produce exactly 30 blinded cases.")

    manifest_path = root / PREPARED_MANIFEST_FILE
    decoder_path = root / PRIVATE_DECODER_FILE

    if manifest_path.exists():
        previous = _read_json(manifest_path)
        comparable_previous = dict(previous)
        comparable_previous.pop("prepared_at_utc", None)
        comparable_current = dict(manifest)
        comparable_current.pop("prepared_at_utc", None)
        if comparable_previous != comparable_current:
            raise ValueError("Prepared semantic manifest drift detected.")
        # Preserve the original preparation timestamp for stable provenance.
        manifest = previous
    else:
        _write_json(manifest_path, manifest)

    if decoder_path.exists():
        previous_decoder = _read_json(decoder_path)
        if previous_decoder != decoder:
            raise ValueError("Private semantic decoder drift detected.")
    else:
        _write_json(decoder_path, decoder)

    return manifest


def _load_prepared_cases(semantic_root: Path) -> tuple[dict[str, Any], list[BlindedCase]]:
    manifest_path = semantic_root / PREPARED_MANIFEST_FILE
    if not manifest_path.is_file():
        raise FileNotFoundError(
            "Blinded semantic cases have not been prepared. Run the prepare command first."
        )
    manifest = _read_json(manifest_path)
    rows = manifest.get("cases")
    if not isinstance(rows, list) or len(rows) != 30:
        raise ValueError("Prepared semantic manifest must contain exactly 30 cases.")

    cases: list[BlindedCase] = []
    seen: set[str] = set()
    for row in rows:
        if not isinstance(row, Mapping):
            raise ValueError("Prepared semantic case entry must be an object.")
        blind_id = str(row.get("blind_id", ""))
        packet_sha = str(row.get("packet_sha256", ""))
        if not blind_id or not packet_sha or blind_id in seen:
            raise ValueError("Prepared semantic manifest contains invalid case identity.")
        seen.add(blind_id)
        packet_path = semantic_root / BLINDED_DIR / blind_id / "packet.json"
        if not packet_path.is_file():
            raise FileNotFoundError(f"Missing blinded packet: {packet_path}")
        packet = _read_json(packet_path)
        if packet_fingerprint(packet) != packet_sha:
            raise ValueError(f"Blinded packet fingerprint mismatch: {packet_path}")
        cases.append(
            BlindedCase(
                blind_id=blind_id,
                packet_sha256=packet_sha,
                packet_path=packet_path,
            )
        )

    cases.sort(key=lambda case: case.blind_id)
    return manifest, cases


def _pass_path(case_dir: Path, pass_number: int) -> Path:
    return case_dir / f"pass_{pass_number}.json"


def _consensus_path(case_dir: Path) -> Path:
    return case_dir / "consensus.json"


def _provider_attempt_prefix(case_dir: Path, pass_number: int, attempt_number: int) -> Path:
    attempts_dir = case_dir / PROVIDER_ATTEMPTS_DIR
    attempts_dir.mkdir(parents=True, exist_ok=True)
    return attempts_dir / f"pass_{pass_number}_attempt_{attempt_number:02d}"


def _next_provider_attempt_number(case_dir: Path, pass_number: int) -> int:
    attempts_dir = case_dir / PROVIDER_ATTEMPTS_DIR
    if not attempts_dir.exists():
        return 1
    prefixes: set[int] = set()
    marker = f"pass_{pass_number}_attempt_"
    for path in attempts_dir.glob(f"{marker}*.json"):
        stem = path.stem
        if not stem.startswith(marker):
            continue
        remainder = stem[len(marker) :]
        number_text = remainder.split("_", 1)[0]
        if number_text.isdigit():
            prefixes.add(int(number_text))
    return (max(prefixes) + 1) if prefixes else 1


def _persist_consensus_if_ready(case_dir: Path) -> bool:
    first_path = _pass_path(case_dir, 1)
    second_path = _pass_path(case_dir, 2)
    if not first_path.is_file() or not second_path.is_file():
        return False

    first = _read_json(first_path)
    second = _read_json(second_path)
    consensus = combine_judge_passes(first, second)
    output_path = _consensus_path(case_dir)
    payload = {
        "created_at_utc": _utc_now(),
        "consensus": consensus,
    }
    if output_path.exists():
        existing = _read_json(output_path)
        if existing.get("consensus") != consensus:
            raise ValueError(f"Persisted semantic consensus drift detected: {output_path}")
    else:
        _write_json(output_path, payload)
    return True


def _count_provider_calls(case_dir: Path) -> int:
    attempts_dir = case_dir / PROVIDER_ATTEMPTS_DIR
    if not attempts_dir.exists():
        return 0
    return len(list(attempts_dir.glob("*_started.json")))


def semantic_status(
    *,
    semantic_root: str | Path = DEFAULT_SEMANTIC_ROOT,
) -> dict[str, Any]:
    """Return a condition-blind mechanical progress summary with no inference."""

    root = Path(semantic_root)
    _, cases = _load_prepared_cases(root)
    logical_passes = 0
    completed_cases = 0
    manual_cases = 0
    provider_calls = 0
    next_blind_id: str | None = None
    next_logical_pass: int | None = None

    for case in cases:
        case_dir = root / BLINDED_DIR / case.blind_id
        provider_calls += _count_provider_calls(case_dir)
        for pass_number in LOGICAL_PASSES:
            if _pass_path(case_dir, pass_number).is_file():
                logical_passes += 1
            elif next_blind_id is None:
                next_blind_id = case.blind_id
                next_logical_pass = pass_number
                break

        if _persist_consensus_if_ready(case_dir):
            completed_cases += 1
            consensus = _read_json(_consensus_path(case_dir))["consensus"]
            if bool(consensus.get("manual_adjudication_required", False)):
                manual_cases += 1

    return {
        "prepared_cases": len(cases),
        "logical_passes_persisted": logical_passes,
        "logical_passes_required": len(cases) * len(LOGICAL_PASSES),
        "provider_calls_recorded": provider_calls,
        "completed_cases": completed_cases,
        "manual_adjudication_cases": manual_cases,
        "next_blind_id": next_blind_id,
        "next_logical_pass": next_logical_pass,
        "judge_complete": completed_cases == len(cases),
    }


JudgeFactory = Callable[[], OpenAISemanticJudge]


def _default_judge_factory() -> OpenAISemanticJudge:
    return OpenAISemanticJudge(
        model=JUDGE_MODEL,
        reasoning_effort=JUDGE_REASONING_EFFORT,
        max_output_tokens=JUDGE_MAX_OUTPUT_TOKENS,
    )


def _run_one_logical_pass(
    *,
    case: BlindedCase,
    pass_number: int,
    semantic_root: Path,
    judge_factory: JudgeFactory,
    remaining_call_budget: int,
) -> tuple[str, int]:
    """Obtain one completed logical judge pass using bounded provider recovery.

    Returns ``(status, calls_launched)`` where status is ``PASS_PERSISTED``,
    ``CALL_BUDGET_EXHAUSTED``, or ``PROVIDER_ATTEMPTS_EXHAUSTED``.
    """

    case_dir = semantic_root / BLINDED_DIR / case.blind_id
    output_path = _pass_path(case_dir, pass_number)
    if output_path.is_file():
        return "PASS_PERSISTED", 0

    packet = _read_json(case.packet_path)
    calls_launched = 0

    while True:
        if calls_launched >= remaining_call_budget:
            return "CALL_BUDGET_EXHAUSTED", calls_launched

        provider_attempt = _next_provider_attempt_number(case_dir, pass_number)
        if provider_attempt > MAX_PROVIDER_ATTEMPTS_PER_LOGICAL_PASS:
            return "PROVIDER_ATTEMPTS_EXHAUSTED", calls_launched

        prefix = _provider_attempt_prefix(case_dir, pass_number, provider_attempt)
        started_path = Path(str(prefix) + "_started.json")
        _write_json(
            started_path,
            {
                "blind_id": case.blind_id,
                "logical_pass": pass_number,
                "provider_attempt": provider_attempt,
                "started_at_utc": _utc_now(),
                "packet_sha256": case.packet_sha256,
                "judge_model": JUDGE_MODEL,
                "reasoning_effort": JUDGE_REASONING_EFFORT,
            },
        )
        calls_launched += 1

        try:
            judge = judge_factory()
            result = judge.evaluate(packet)
        except ModelGenerationError as exc:
            error_path = Path(str(prefix) + "_error.json")
            _write_json(
                error_path,
                {
                    "blind_id": case.blind_id,
                    "logical_pass": pass_number,
                    "provider_attempt": provider_attempt,
                    "failed_at_utc": _utc_now(),
                    "error_type": type(exc).__name__,
                    "error_code": getattr(exc, "error_code", None),
                    "retryable": bool(getattr(exc, "retryable", False)),
                    "usage": (
                        asdict(exc.usage)
                        if getattr(exc, "usage", None) is not None
                        else None
                    ),
                    "message": str(exc),
                },
            )
            # A failed provider call contains no usable semantic judgment. The
            # next fresh attempt, if any, therefore does not replace or cherry-pick
            # a score; it only tries to obtain the preregistered logical pass.
            continue

        result = dict(result)
        result["pass_number"] = pass_number
        result["provider_attempt"] = provider_attempt
        result["packet_sha256"] = case.packet_sha256
        _write_json(output_path, result)
        success_path = Path(str(prefix) + "_success.json")
        _write_json(
            success_path,
            {
                "blind_id": case.blind_id,
                "logical_pass": pass_number,
                "provider_attempt": provider_attempt,
                "completed_at_utc": _utc_now(),
                "packet_sha256": case.packet_sha256,
                "usage": result.get("usage"),
                "response_id": result.get("response_id"),
            },
        )
        return "PASS_PERSISTED", calls_launched


def export_blinded_review(
    *,
    semantic_root: str | Path = DEFAULT_SEMANTIC_ROOT,
    export_root: str | Path = DEFAULT_EXPORT_ROOT,
) -> Path:
    """Create one compact condition-blind review ZIP.

    The export uses an explicit allowlist and never traverses the semantic root
    recursively. Therefore ``private_decoder.json`` cannot enter the archive by
    accident when new local files are added later.
    """

    root = Path(semantic_root)
    exports = Path(export_root)
    manifest, cases = _load_prepared_cases(root)
    exports.mkdir(parents=True, exist_ok=True)

    status = semantic_status(semantic_root=root)
    summary = {
        "exported_at_utc": _utc_now(),
        "schema_version": "semantic_judge_blinded_export_v0_1",
        "prepared_case_count": status["prepared_cases"],
        "logical_passes_persisted": status["logical_passes_persisted"],
        "logical_passes_required": status["logical_passes_required"],
        "provider_calls_recorded": status["provider_calls_recorded"],
        "completed_cases": status["completed_cases"],
        "manual_adjudication_cases": status["manual_adjudication_cases"],
        "judge_complete": status["judge_complete"],
        "decoder_included": False,
    }

    archive_path = exports / f"semantic_judge_blinded_{_timestamp_id()}.zip"
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(
            "blinded_export_summary.json",
            json.dumps(summary, indent=2, sort_keys=True),
        )
        archive.writestr(
            PREPARED_MANIFEST_FILE,
            json.dumps(manifest, indent=2, sort_keys=True),
        )

        for case in cases:
            case_dir = root / BLINDED_DIR / case.blind_id
            allowed_files = [
                case_dir / "packet.json",
                case_dir / "pass_1.json",
                case_dir / "pass_2.json",
                case_dir / "consensus.json",
            ]
            provider_dir = case_dir / PROVIDER_ATTEMPTS_DIR
            if provider_dir.exists():
                allowed_files.extend(sorted(provider_dir.glob("*.json")))

            for path in allowed_files:
                if not path.is_file():
                    continue
                relative = Path(BLINDED_DIR) / case.blind_id / path.relative_to(case_dir)
                archive.write(path, relative.as_posix())

        batch_root = root / BATCH_DIR
        if batch_root.exists():
            for path in sorted(batch_root.glob("*.json")):
                archive.write(path, (Path(BATCH_DIR) / path.name).as_posix())

    return archive_path


def run_judge_batch(
    *,
    max_judge_calls: int,
    semantic_root: str | Path = DEFAULT_SEMANTIC_ROOT,
    export_root: str | Path = DEFAULT_EXPORT_ROOT,
    judge_factory: JudgeFactory = _default_judge_factory,
) -> JudgeBatchResult:
    """Run a bounded number of blinded judge provider calls sequentially."""

    if max_judge_calls <= 0:
        raise ValueError("max_judge_calls must be positive.")

    root = Path(semantic_root)
    prepare_blinded_cases(semantic_root=root)
    _, cases = _load_prepared_cases(root)

    batch_id = f"semantic-batch-{_timestamp_id()}"
    calls_launched = 0
    newly_persisted_passes = 0
    stop_reason = "JUDGE_COMPLETE"
    next_blind_id: str | None = None
    next_logical_pass: int | None = None

    print(
        f"Blinded semantic batch started: {batch_id} | cases=30 | "
        f"max_provider_calls={max_judge_calls}",
        flush=True,
    )

    for case in cases:
        case_dir = root / BLINDED_DIR / case.blind_id
        for pass_number in LOGICAL_PASSES:
            pass_path = _pass_path(case_dir, pass_number)
            if pass_path.is_file():
                continue

            if calls_launched >= max_judge_calls:
                stop_reason = "MAX_JUDGE_CALLS_REACHED"
                next_blind_id = case.blind_id
                next_logical_pass = pass_number
                break

            remaining = max_judge_calls - calls_launched
            print(
                f"{case.blind_id}: logical pass {pass_number} starting",
                flush=True,
            )
            status, used = _run_one_logical_pass(
                case=case,
                pass_number=pass_number,
                semantic_root=root,
                judge_factory=judge_factory,
                remaining_call_budget=remaining,
            )
            calls_launched += used

            if status == "PASS_PERSISTED":
                newly_persisted_passes += 1
                print(
                    f"{case.blind_id}: logical pass {pass_number} persisted",
                    flush=True,
                )
                continue

            stop_reason = status
            next_blind_id = case.blind_id
            next_logical_pass = pass_number
            break

        _persist_consensus_if_ready(case_dir)
        if _consensus_path(case_dir).is_file():
            consensus = _read_json(_consensus_path(case_dir))["consensus"]
            print(
                f"{case.blind_id}: case complete | "
                f"manual_adjudication_required="
                f"{bool(consensus.get('manual_adjudication_required', False))}",
                flush=True,
            )

        if stop_reason != "JUDGE_COMPLETE":
            break

    status = semantic_status(semantic_root=root)
    if status["judge_complete"]:
        stop_reason = "JUDGE_COMPLETE"
        next_blind_id = None
        next_logical_pass = None
    elif stop_reason == "JUDGE_COMPLETE":
        stop_reason = "INCOMPLETE_WITHOUT_EXPLICIT_STOP"
        next_blind_id = status["next_blind_id"]
        next_logical_pass = status["next_logical_pass"]

    batch_record = {
        "batch_id": batch_id,
        "started_or_recorded_at_utc": _utc_now(),
        "provider_calls_launched": calls_launched,
        "new_logical_passes_persisted": newly_persisted_passes,
        "stop_reason": stop_reason,
        "post_batch_status": status,
    }
    _write_json(root / BATCH_DIR / f"{batch_id}.json", batch_record)
    export_path = export_blinded_review(semantic_root=root, export_root=export_root)

    result = JudgeBatchResult(
        batch_id=batch_id,
        provider_calls_launched=calls_launched,
        logical_passes_persisted=int(status["logical_passes_persisted"]),
        completed_cases=int(status["completed_cases"]),
        manual_adjudication_cases=int(status["manual_adjudication_cases"]),
        stop_reason=stop_reason,
        next_blind_id=(
            str(status["next_blind_id"])
            if status["next_blind_id"] is not None
            else None
        ),
        next_logical_pass=(
            int(status["next_logical_pass"])
            if status["next_logical_pass"] is not None
            else None
        ),
        export_path=str(export_path.resolve()),
    )

    print(f"Provider calls launched: {result.provider_calls_launched}", flush=True)
    print(
        f"Logical passes persisted: {result.logical_passes_persisted} / 60",
        flush=True,
    )
    print(f"Completed blinded cases: {result.completed_cases} / 30", flush=True)
    print(
        f"Manual-adjudication cases: {result.manual_adjudication_cases}",
        flush=True,
    )
    print(f"Stop reason: {result.stop_reason}", flush=True)
    if result.next_blind_id is not None:
        print(
            f"Next blinded work: {result.next_blind_id} pass {result.next_logical_pass}",
            flush=True,
        )
    print(f"Blinded review export: {result.export_path}", flush=True)
    return result


def _format_status(status: Mapping[str, Any]) -> str:
    next_text = (
        "none"
        if status.get("next_blind_id") is None
        else f"{status['next_blind_id']} pass {status['next_logical_pass']}"
    )
    return (
        f"prepared_cases={status['prepared_cases']} "
        f"logical_passes={status['logical_passes_persisted']}/"
        f"{status['logical_passes_required']} "
        f"completed_cases={status['completed_cases']}/30 "
        f"manual_cases={status['manual_adjudication_cases']} "
        f"provider_calls={status['provider_calls_recorded']} "
        f"next={next_text}"
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Resumable condition-blind semantic judge supervisor for Prototype V0."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser(
        "prepare",
        help="Build and verify all blinded judge packets without model inference.",
    )
    sub.add_parser(
        "status",
        help="Show condition-blind semantic-judge progress without inference.",
    )
    run_parser = sub.add_parser(
        "run-batch",
        help="Run a bounded sequential batch of blinded semantic judge calls.",
    )
    run_parser.add_argument("--max-judge-calls", type=int, required=True)
    sub.add_parser(
        "export",
        help="Create a blinded review ZIP that explicitly excludes the private decoder.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    if args.command == "prepare":
        manifest = prepare_blinded_cases()
        print(f"Prepared blinded cases: {manifest['case_count']} / 30")
        print("Model inference launched: 0")
        print(
            "Private decoder created locally and excluded from blinded review exports."
        )
        return
    if args.command == "status":
        print(_format_status(semantic_status()))
        return
    if args.command == "run-batch":
        run_judge_batch(max_judge_calls=args.max_judge_calls)
        return
    if args.command == "export":
        path = export_blinded_review()
        print(f"Blinded review export: {path.resolve()}")
        return
    raise AssertionError(f"Unhandled semantic judge supervisor command: {args.command}")


if __name__ == "__main__":
    main()
