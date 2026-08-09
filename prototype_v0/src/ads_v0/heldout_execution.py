"""Deterministic held-out execution planning for Prototype V0.

This module sits between the preregistered protocol and paid held-out treatment
execution. Its purpose is to make the experimental schedule explicit and to
prevent accidental drift before any H1/H2 model call occurs.

The module deliberately performs no model inference. It provides three pieces of
condition-neutral infrastructure:

1. validate that local H1/H2 bundles are byte-identical to the identities frozen
   before P0 implementation;
2. materialize the exact 30-slot condition order registered in Foundation 012;
3. derive stable replacement-attempt identifiers without changing slot order.

The generated benchmark directories are intentionally git-ignored, so execution
must verify their aggregate SHA-256 fingerprints at runtime rather than assuming
that a directory named H1 or H2 is the frozen bundle. The committed fingerprint
record is therefore part of the execution contract.

Replacement attempts are represented as attempts *inside* one preregistered
slot. They do not create new slots and never alter the H1/H2 condition order.
The policy for deciding whether an attempt is replacement-eligible is implemented
by the later execution layer and remains the one frozen in Foundation 012:
provider/infrastructure generation termination may be replaced, while behavioral
failures such as poor methodology, Python errors, semantic mistakes, or resource
exhaustion may not be replaced.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping

from .prepare_heldout import fingerprint_bundle, load_protocol


DEFAULT_PROTOCOL_PATH = Path("configs/held_out_protocol_v0_1.json")
DEFAULT_FINGERPRINT_PATH = Path("configs/held_out_bundle_fingerprints_v0_1.json")
DEFAULT_BUNDLE_ROOT = Path("generated/held_out")
DEFAULT_PLAN_PATH = Path("results/held_out/run_plan.json")

_CONDITIONS = ("B0", "B1", "P0")
_EXPECTED_VARIANTS = ("H1", "H2")
_MAX_REPLACEMENT_ATTEMPTS = 2


@dataclass(frozen=True)
class HeldOutSlot:
    """One preregistered condition position in the 30-slot held-out schedule."""

    slot_index: int
    variant: str
    replicate: int
    position_in_replicate: int
    condition: str
    slot_id: str


@dataclass(frozen=True)
class FrozenBundleValidation:
    """Execution-time confirmation of one local held-out bundle identity."""

    variant: str
    bundle_path: str
    case_id: str
    surface_variant: str
    data_seed: int
    aggregate_sha256: str
    file_count: int
    passed_self_tests: bool


def load_frozen_bundle_record(path: str | Path) -> dict[str, Any]:
    """Load and validate the committed pre-P0 held-out identity record."""

    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Held-out fingerprint record must be a JSON object.")
    if "protocol_version" not in payload:
        raise ValueError("Held-out fingerprint record is missing protocol_version.")

    bundles = payload.get("bundles")
    if not isinstance(bundles, dict):
        raise ValueError("Held-out fingerprint record must contain a bundles object.")

    required = {
        "case_id",
        "selected_seed",
        "seed_start",
        "file_count",
        "aggregate_sha256",
    }
    for variant in _EXPECTED_VARIANTS:
        record = bundles.get(variant)
        if not isinstance(record, dict):
            raise ValueError(f"Missing frozen bundle identity for {variant}.")
        missing = required.difference(record)
        if missing:
            raise ValueError(
                f"Frozen bundle identity {variant} is missing fields: "
                + ", ".join(sorted(missing))
            )

    return payload


def validate_frozen_bundles(
    *,
    protocol_path: str | Path = DEFAULT_PROTOCOL_PATH,
    fingerprint_path: str | Path = DEFAULT_FINGERPRINT_PATH,
    bundle_root: str | Path = DEFAULT_BUNDLE_ROOT,
) -> dict[str, FrozenBundleValidation]:
    """Verify local H1/H2 directories against the identities frozen before P0.

    Validation is intentionally stronger than checking directory names. For each
    variant the function verifies protocol version, case identity, surface
    variant, selected seed, self-test status, file count, and the aggregate
    SHA-256 digest over the complete serialized bundle.

    Any mismatch aborts before treatment execution. A changed README, CSV,
    evaluator manifest, timing notice, or self-test report therefore changes the
    aggregate fingerprint and is detected.
    """

    protocol = load_protocol(protocol_path)
    frozen = load_frozen_bundle_record(fingerprint_path)
    if str(protocol["protocol_version"]) != str(frozen["protocol_version"]):
        raise ValueError(
            "Held-out protocol version does not match the frozen bundle record."
        )

    protocol_cases = protocol["held_out_cases"]
    frozen_bundles = frozen["bundles"]
    root = Path(bundle_root)
    validations: dict[str, FrozenBundleValidation] = {}

    if tuple(protocol_cases) != _EXPECTED_VARIANTS:
        raise ValueError(
            "Held-out protocol variants do not match the registered H1/H2 execution set."
        )

    for variant in _EXPECTED_VARIANTS:
        spec = protocol_cases[variant]
        expected = frozen_bundles[variant]
        bundle_dir = root / variant
        if not bundle_dir.is_dir():
            raise FileNotFoundError(f"Frozen held-out bundle is missing: {bundle_dir}")

        manifest_path = bundle_dir / "evaluator_only" / "manifest.json"
        self_test_path = bundle_dir / "evaluator_only" / "self_test_report.json"
        if not manifest_path.is_file() or not self_test_path.is_file():
            raise FileNotFoundError(
                f"Held-out bundle {variant} is missing evaluator identity files."
            )

        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        self_test = json.loads(self_test_path.read_text(encoding="utf-8"))
        passed_self_tests = bool(self_test.get("passed", False))
        if not passed_self_tests:
            raise ValueError(f"Held-out bundle {variant} does not pass self-tests.")

        case_id = str(manifest.get("case_id", ""))
        surface_variant = str(manifest.get("surface_variant", ""))
        data_seed = int(manifest.get("data_seed"))

        if case_id != str(spec["case_id"]) or case_id != str(expected["case_id"]):
            raise ValueError(f"Held-out bundle {variant} case_id does not match freeze.")
        if surface_variant != str(spec["surface_variant"]):
            raise ValueError(
                f"Held-out bundle {variant} surface_variant does not match protocol."
            )
        if data_seed != int(expected["selected_seed"]):
            raise ValueError(f"Held-out bundle {variant} seed does not match freeze.")
        if int(spec["seed_start"]) != int(expected["seed_start"]):
            raise ValueError(
                f"Held-out bundle {variant} seed-start record conflicts with protocol."
            )

        fingerprint = fingerprint_bundle(bundle_dir)
        if int(fingerprint["file_count"]) != int(expected["file_count"]):
            raise ValueError(f"Held-out bundle {variant} file count does not match freeze.")
        if fingerprint["aggregate_sha256"] != expected["aggregate_sha256"]:
            raise ValueError(
                f"Held-out bundle {variant} SHA-256 fingerprint does not match freeze."
            )

        validations[variant] = FrozenBundleValidation(
            variant=variant,
            bundle_path=bundle_dir.as_posix(),
            case_id=case_id,
            surface_variant=surface_variant,
            data_seed=data_seed,
            aggregate_sha256=str(fingerprint["aggregate_sha256"]),
            file_count=int(fingerprint["file_count"]),
            passed_self_tests=True,
        )

    return validations


def materialize_run_plan(protocol: Mapping[str, Any]) -> tuple[HeldOutSlot, ...]:
    """Convert the registered H1/H2 order into an immutable 30-slot plan."""

    run_order = protocol.get("run_order")
    if not isinstance(run_order, Mapping):
        raise ValueError("Held-out protocol is missing run_order.")

    expected_replicates = int(protocol.get("runs_per_condition_per_variant", 0))
    if expected_replicates != 5:
        raise ValueError("Prototype V0 held-out protocol must use five replicates.")

    slots: list[HeldOutSlot] = []
    slot_index = 0
    for variant in _EXPECTED_VARIANTS:
        replicates = run_order.get(variant)
        if not isinstance(replicates, list) or len(replicates) != expected_replicates:
            raise ValueError(
                f"Held-out run order for {variant} must contain five replicates."
            )

        for replicate_index, condition_order in enumerate(replicates, start=1):
            if not isinstance(condition_order, list):
                raise ValueError(
                    f"Held-out {variant} replicate {replicate_index} must be a list."
                )
            if tuple(sorted(condition_order)) != tuple(sorted(_CONDITIONS)):
                raise ValueError(
                    f"Held-out {variant} replicate {replicate_index} must contain "
                    "B0, B1, and P0 exactly once."
                )

            for position, condition in enumerate(condition_order, start=1):
                slot_index += 1
                slot_id = f"{variant.lower()}-r{replicate_index:02d}-{condition.lower()}"
                slots.append(
                    HeldOutSlot(
                        slot_index=slot_index,
                        variant=variant,
                        replicate=replicate_index,
                        position_in_replicate=position,
                        condition=str(condition),
                        slot_id=slot_id,
                    )
                )

    if len(slots) != 30:
        raise ValueError(f"Held-out plan must contain 30 slots, found {len(slots)}.")

    for condition in _CONDITIONS:
        count = sum(slot.condition == condition for slot in slots)
        if count != 10:
            raise ValueError(
                f"Held-out plan must contain 10 {condition} slots, found {count}."
            )

    return tuple(slots)


def attempt_id(slot: HeldOutSlot, attempt_number: int) -> str:
    """Return a stable identifier for an initial or replacement slot attempt."""

    maximum_attempt_number = _MAX_REPLACEMENT_ATTEMPTS + 1
    if attempt_number < 1 or attempt_number > maximum_attempt_number:
        raise ValueError(
            f"attempt_number must be between 1 and {maximum_attempt_number}."
        )
    return f"{slot.slot_id}-a{attempt_number:02d}"


def build_plan_document(
    *,
    protocol: Mapping[str, Any],
    validations: Mapping[str, FrozenBundleValidation],
) -> dict[str, Any]:
    """Build a deterministic JSON document linking schedule and bundle identities."""

    slots = materialize_run_plan(protocol)
    model = protocol.get("treatment_model")
    if not isinstance(model, Mapping):
        raise ValueError("Held-out protocol is missing treatment_model configuration.")

    return {
        "protocol_version": str(protocol["protocol_version"]),
        "bundle_validation": {
            variant: asdict(validations[variant]) for variant in _EXPECTED_VARIANTS
        },
        "treatment_model": dict(model),
        "replacement_policy": {
            "maximum_replacement_attempts_per_slot": _MAX_REPLACEMENT_ATTEMPTS,
            "maximum_total_attempts_per_slot": _MAX_REPLACEMENT_ATTEMPTS + 1,
            "replacement_preserves_slot_order": True,
        },
        "slot_count": len(slots),
        "slots": [
            {
                **asdict(slot),
                "initial_attempt_id": attempt_id(slot, 1),
            }
            for slot in slots
        ],
    }


def validate_and_write_plan(
    *,
    protocol_path: str | Path = DEFAULT_PROTOCOL_PATH,
    fingerprint_path: str | Path = DEFAULT_FINGERPRINT_PATH,
    bundle_root: str | Path = DEFAULT_BUNDLE_ROOT,
    output_path: str | Path = DEFAULT_PLAN_PATH,
    force: bool = False,
) -> dict[str, Any]:
    """Validate frozen inputs and persist the exact preregistered run plan.

    Existing plans are not overwritten by default. This protects a plan that may
    already have been used for held-out execution from accidental regeneration.
    """

    destination = Path(output_path)
    if destination.exists() and not force:
        raise FileExistsError(
            f"Held-out run plan already exists: {destination}. Refusing to overwrite."
        )

    protocol = load_protocol(protocol_path)
    validations = validate_frozen_bundles(
        protocol_path=protocol_path,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
    )
    document = build_plan_document(protocol=protocol, validations=validations)

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(document, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return document


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate frozen H1/H2 bundle identities and materialize the exact "
            "Prototype V0 held-out run plan. This command performs no model calls."
        )
    )
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL_PATH)
    parser.add_argument("--fingerprints", type=Path, default=DEFAULT_FINGERPRINT_PATH)
    parser.add_argument("--bundle-root", type=Path, default=DEFAULT_BUNDLE_ROOT)
    parser.add_argument("--output", type=Path, default=DEFAULT_PLAN_PATH)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing plan. Do not use after held-out execution begins.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    document = validate_and_write_plan(
        protocol_path=args.protocol,
        fingerprint_path=args.fingerprints,
        bundle_root=args.bundle_root,
        output_path=args.output,
        force=args.force,
    )

    print(f"Protocol: {document['protocol_version']}")
    print(f"Validated bundles: {', '.join(_EXPECTED_VARIANTS)}")
    for variant in _EXPECTED_VARIANTS:
        item = document["bundle_validation"][variant]
        print(
            f"{variant}: seed={item['data_seed']} files={item['file_count']} "
            f"sha256={item['aggregate_sha256']}"
        )
    print(f"Run slots: {document['slot_count']}")
    print(f"Output: {Path(args.output).resolve()}")


if __name__ == "__main__":
    main()
