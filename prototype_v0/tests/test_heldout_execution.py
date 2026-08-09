from __future__ import annotations

import json
from pathlib import Path

import pytest

from ads_v0.heldout_execution import (
    attempt_id,
    materialize_run_plan,
    validate_and_write_plan,
    validate_frozen_bundles,
)
from ads_v0.prepare_heldout import fingerprint_bundle, load_protocol


PROTOTYPE_ROOT = Path(__file__).resolve().parents[1]
PROTOCOL_PATH = PROTOTYPE_ROOT / "configs" / "held_out_protocol_v0_1.json"


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def _fake_frozen_bundles(tmp_path: Path) -> tuple[Path, Path]:
    protocol = load_protocol(PROTOCOL_PATH)
    bundle_root = tmp_path / "held_out"
    frozen_bundles: dict[str, dict] = {}

    for variant, spec in protocol["held_out_cases"].items():
        bundle = bundle_root / variant
        _write_json(
            bundle / "evaluator_only" / "manifest.json",
            {
                "case_id": spec["case_id"],
                "surface_variant": spec["surface_variant"],
                "data_seed": spec["seed_start"],
            },
        )
        _write_json(
            bundle / "evaluator_only" / "self_test_report.json",
            {"passed": True, "checks": []},
        )
        visible = bundle / "visible" / "project_brief.md"
        visible.parent.mkdir(parents=True, exist_ok=True)
        visible.write_text(f"synthetic frozen {variant} bundle\n", encoding="utf-8")

        fingerprint = fingerprint_bundle(bundle)
        frozen_bundles[variant] = {
            "case_id": spec["case_id"],
            "selected_seed": spec["seed_start"],
            "seed_start": spec["seed_start"],
            "first_candidate_passed": True,
            "file_count": fingerprint["file_count"],
            "aggregate_sha256": fingerprint["aggregate_sha256"],
        }

    fingerprint_path = tmp_path / "held_out_bundle_fingerprints.json"
    _write_json(
        fingerprint_path,
        {
            "protocol_version": protocol["protocol_version"],
            "bundles": frozen_bundles,
        },
    )
    return bundle_root, fingerprint_path


def test_materialized_plan_exactly_matches_registered_order_and_counts() -> None:
    protocol = load_protocol(PROTOCOL_PATH)
    slots = materialize_run_plan(protocol)

    assert len(slots) == 30
    assert [slot.slot_index for slot in slots] == list(range(1, 31))
    assert [slot.condition for slot in slots[:6]] == [
        "B0",
        "B1",
        "P0",
        "B1",
        "P0",
        "B0",
    ]
    assert [slot.condition for slot in slots[15:21]] == [
        "P0",
        "B0",
        "B1",
        "B0",
        "B1",
        "P0",
    ]
    assert sum(slot.condition == "B0" for slot in slots) == 10
    assert sum(slot.condition == "B1" for slot in slots) == 10
    assert sum(slot.condition == "P0" for slot in slots) == 10
    assert slots[0].slot_id == "h1-r01-b0"
    assert slots[-1].slot_id == "h2-r05-p0"


def test_attempt_identifier_keeps_replacements_inside_original_slot() -> None:
    protocol = load_protocol(PROTOCOL_PATH)
    slot = materialize_run_plan(protocol)[0]

    assert attempt_id(slot, 1) == "h1-r01-b0-a01"
    assert attempt_id(slot, 2) == "h1-r01-b0-a02"
    assert attempt_id(slot, 3) == "h1-r01-b0-a03"

    with pytest.raises(ValueError, match="between 1 and 3"):
        attempt_id(slot, 4)


def test_bundle_validation_accepts_exact_identity_and_rejects_tampering(
    tmp_path: Path,
) -> None:
    bundle_root, fingerprint_path = _fake_frozen_bundles(tmp_path)

    validation = validate_frozen_bundles(
        protocol_path=PROTOCOL_PATH,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
    )

    assert validation["H1"].passed_self_tests
    assert validation["H2"].passed_self_tests
    assert validation["H1"].data_seed == 811
    assert validation["H2"].data_seed == 1601

    tampered = bundle_root / "H1" / "visible" / "project_brief.md"
    tampered.write_text("tampered after freeze\n", encoding="utf-8")

    with pytest.raises(ValueError, match="SHA-256 fingerprint"):
        validate_frozen_bundles(
            protocol_path=PROTOCOL_PATH,
            fingerprint_path=fingerprint_path,
            bundle_root=bundle_root,
        )


def test_written_plan_carries_frozen_resource_config_and_is_not_overwritten(
    tmp_path: Path,
) -> None:
    bundle_root, fingerprint_path = _fake_frozen_bundles(tmp_path)
    output = tmp_path / "run_plan.json"

    document = validate_and_write_plan(
        protocol_path=PROTOCOL_PATH,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
        output_path=output,
    )

    assert document["slot_count"] == 30
    assert document["treatment_model"]["max_successful_model_calls"] == 24
    assert document["treatment_model"]["max_observed_total_tokens"] == 250000
    assert document["treatment_model"]["max_python_execution_attempts"] == 12
    assert document["replacement_policy"]["maximum_replacement_attempts_per_slot"] == 2
    assert output.is_file()

    with pytest.raises(FileExistsError, match="Refusing to overwrite"):
        validate_and_write_plan(
            protocol_path=PROTOCOL_PATH,
            fingerprint_path=fingerprint_path,
            bundle_root=bundle_root,
            output_path=output,
        )
