"""Prepare and fingerprint preregistered Prototype V0 held-out bundles.

This module operationalizes the case-selection rule registered in Foundation 012.
The rule is intentionally mechanical: for each held-out surface variant, start
from the preregistered seed and select the first seed whose generated bundle
passes every deterministic benchmark self-test. Treatment behavior, model
performance, and semantic-evaluator output are never consulted during seed
selection.

The preparation step is deliberately separate from P0 implementation. Exact
held-out data and documentation should exist, pass self-tests, and be
cryptographically fingerprinted before the structured treatment is written.
That ordering prevents the benchmark from drifting in response to P0 behavior.

The fingerprint is a reproducibility record rather than an information source
for treatments. It includes SHA-256 digests for every serialized file in the
bundle, including evaluator-only truth and the self-test report. Treatment
runtime boundaries must still prevent evaluator-only material from being
visible to B0, B1, or P0.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import tempfile
from pathlib import Path
from typing import Any, Mapping

from .casegen import CaseConfig, generate_case_bundle


DEFAULT_PROTOCOL_PATH = Path("configs/held_out_protocol_v0_1.json")
DEFAULT_OUTPUT_ROOT = Path("generated/held_out")
DEFAULT_MAX_SEED_ATTEMPTS = 100


def load_protocol(path: str | Path) -> dict[str, Any]:
    """Load and minimally validate the registered held-out protocol JSON.

    The machine-readable protocol is not intended to duplicate every sentence
    of Foundation 012. This loader validates only fields required to generate
    held-out case bundles. More extensive treatment/evaluator configuration is
    consumed by later experiment tooling.
    """

    protocol_path = Path(path)
    payload = json.loads(protocol_path.read_text(encoding="utf-8"))

    if not isinstance(payload, dict):
        raise ValueError("Held-out protocol must be a JSON object.")
    if "protocol_version" not in payload:
        raise ValueError("Held-out protocol is missing protocol_version.")
    cases = payload.get("held_out_cases")
    if not isinstance(cases, dict) or not cases:
        raise ValueError("Held-out protocol must define held_out_cases.")

    required_case_fields = {
        "case_id",
        "surface_variant",
        "seed_start",
        "seed_selection",
        "customer_id_name",
        "time_name",
        "post_outcome_feature_name",
    }
    for variant_name, spec in cases.items():
        if not isinstance(spec, dict):
            raise ValueError(f"Held-out case {variant_name!r} must be an object.")
        missing = required_case_fields.difference(spec)
        if missing:
            raise ValueError(
                f"Held-out case {variant_name!r} is missing fields: "
                + ", ".join(sorted(missing))
            )
        if spec["seed_selection"] != (
            "first_seed_at_or_above_start_that_passes_all_benchmark_self_tests"
        ):
            raise ValueError(
                f"Held-out case {variant_name!r} uses an unsupported seed-selection rule."
            )

    return payload


def case_config_from_spec(spec: Mapping[str, Any], *, seed: int) -> CaseConfig:
    """Translate one registered held-out case specification into ``CaseConfig``."""

    return CaseConfig(
        case_id=str(spec["case_id"]),
        surface_variant=str(spec["surface_variant"]),
        data_seed=int(seed),
        customer_id_name=str(spec["customer_id_name"]),
        time_name=str(spec["time_name"]),
        post_outcome_feature_name=str(spec["post_outcome_feature_name"]),
    )


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fingerprint_bundle(bundle_dir: str | Path) -> dict[str, Any]:
    """Return a deterministic file-level and aggregate SHA-256 fingerprint.

    The aggregate digest is computed from sorted relative paths, byte sizes, and
    individual file digests. Including the relative path means two bundles with
    identical file bytes arranged under different names do not accidentally
    receive the same aggregate fingerprint.
    """

    root = Path(bundle_dir)
    if not root.is_dir():
        raise FileNotFoundError(f"Bundle directory does not exist: {root}")

    files: dict[str, dict[str, Any]] = {}
    aggregate = hashlib.sha256()

    paths = sorted(path for path in root.rglob("*") if path.is_file())
    if not paths:
        raise ValueError(f"Bundle contains no files: {root}")

    for path in paths:
        relative = path.relative_to(root).as_posix()
        size = path.stat().st_size
        digest = _sha256_file(path)
        files[relative] = {"bytes": size, "sha256": digest}
        aggregate.update(relative.encode("utf-8"))
        aggregate.update(b"\0")
        aggregate.update(str(size).encode("ascii"))
        aggregate.update(b"\0")
        aggregate.update(digest.encode("ascii"))
        aggregate.update(b"\n")

    return {
        "aggregate_sha256": aggregate.hexdigest(),
        "file_count": len(files),
        "files": files,
    }


def prepare_variant(
    *,
    protocol_version: str,
    variant_name: str,
    spec: Mapping[str, Any],
    output_root: str | Path,
    max_seed_attempts: int = DEFAULT_MAX_SEED_ATTEMPTS,
    force: bool = False,
) -> dict[str, Any]:
    """Generate the first self-test-passing bundle for one registered variant.

    Each candidate is generated in a temporary directory. A failing candidate
    is discarded completely. Only the first passing candidate is moved into the
    canonical output path, ensuring that a half-written or failed bundle cannot
    later be mistaken for the frozen held-out case.
    """

    if max_seed_attempts <= 0:
        raise ValueError("max_seed_attempts must be positive.")

    root = Path(output_root)
    root.mkdir(parents=True, exist_ok=True)
    destination = root / variant_name

    if destination.exists():
        if not force:
            raise FileExistsError(
                f"Held-out destination already exists: {destination}. "
                "Use --force only when intentionally regenerating before the "
                "bundle-freeze checkpoint."
            )
        shutil.rmtree(destination)

    seed_start = int(spec["seed_start"])
    selected_seed: int | None = None
    attempts = 0

    for offset in range(max_seed_attempts):
        seed = seed_start + offset
        attempts += 1
        config = case_config_from_spec(spec, seed=seed)

        with tempfile.TemporaryDirectory(
            prefix=f".{variant_name.lower()}-candidate-",
            dir=root,
        ) as temporary:
            candidate_dir = Path(temporary) / "bundle"
            try:
                generate_case_bundle(candidate_dir, config, run_self_tests=True)
            except RuntimeError:
                continue

            selected_seed = seed
            shutil.move(str(candidate_dir), str(destination))
            break

    if selected_seed is None:
        raise RuntimeError(
            f"No valid {variant_name} bundle found in {max_seed_attempts} "
            f"seeds starting at {seed_start}."
        )

    fingerprint = fingerprint_bundle(destination)
    record = {
        "protocol_version": protocol_version,
        "variant": variant_name,
        "case_id": spec["case_id"],
        "surface_variant": spec["surface_variant"],
        "seed_start": seed_start,
        "selected_seed": selected_seed,
        "seed_attempts": attempts,
        "selection_rule": spec["seed_selection"],
        "surface_names": {
            "customer_id": spec["customer_id_name"],
            "time": spec["time_name"],
            "post_outcome_feature": spec["post_outcome_feature_name"],
        },
        "bundle_path": destination.as_posix(),
        "fingerprint": fingerprint,
    }

    record_path = root / f"{variant_name}_bundle_fingerprint.json"
    _write_json(record_path, record)
    return record


def prepare_registered_heldout_cases(
    *,
    protocol_path: str | Path = DEFAULT_PROTOCOL_PATH,
    output_root: str | Path = DEFAULT_OUTPUT_ROOT,
    max_seed_attempts: int = DEFAULT_MAX_SEED_ATTEMPTS,
    force: bool = False,
) -> dict[str, Any]:
    """Prepare every held-out case registered by the protocol."""

    protocol = load_protocol(protocol_path)
    version = str(protocol["protocol_version"])
    records: dict[str, Any] = {}

    for variant_name in sorted(protocol["held_out_cases"]):
        records[variant_name] = prepare_variant(
            protocol_version=version,
            variant_name=variant_name,
            spec=protocol["held_out_cases"][variant_name],
            output_root=output_root,
            max_seed_attempts=max_seed_attempts,
            force=force,
        )

    registry = {
        "protocol_version": version,
        "protocol_path": Path(protocol_path).as_posix(),
        "variants": records,
    }
    _write_json(Path(output_root) / "held_out_bundle_registry.json", registry)
    return registry


def _write_json(path: Path, payload: Any) -> None:
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate the first self-test-passing H1/H2 bundles registered by "
            "the Prototype V0 held-out protocol and write SHA-256 fingerprints."
        )
    )
    parser.add_argument(
        "--protocol",
        type=Path,
        default=DEFAULT_PROTOCOL_PATH,
        help="Path to the preregistered held-out protocol JSON.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help="Directory in which H1/H2 bundles and fingerprint records are written.",
    )
    parser.add_argument(
        "--max-seed-attempts",
        type=int,
        default=DEFAULT_MAX_SEED_ATTEMPTS,
        help="Maximum sequential seeds tested for each registered variant.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help=(
            "Delete existing held-out variant directories before generation. "
            "Do not use after bundle fingerprints have been frozen."
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    registry = prepare_registered_heldout_cases(
        protocol_path=args.protocol,
        output_root=args.output_root,
        max_seed_attempts=args.max_seed_attempts,
        force=args.force,
    )

    print(f"Protocol: {registry['protocol_version']}")
    for variant_name, record in registry["variants"].items():
        fingerprint = record["fingerprint"]["aggregate_sha256"]
        print(
            f"{variant_name}: seed={record['selected_seed']} "
            f"files={record['fingerprint']['file_count']} "
            f"sha256={fingerprint}"
        )
    print(f"Output: {Path(args.output_root).resolve()}")


if __name__ == "__main__":
    main()
