from __future__ import annotations

import json
from pathlib import Path

import pytest

from ads_v0 import prepare_heldout


def _case_spec(seed_start: int = 811) -> dict[str, object]:
    return {
        "case_id": "churn_v0_h1",
        "surface_variant": "held_out_h1",
        "seed_start": seed_start,
        "seed_selection": (
            "first_seed_at_or_above_start_that_passes_all_benchmark_self_tests"
        ),
        "customer_id_name": "member_key",
        "time_name": "scoring_period",
        "post_outcome_feature_name": "lifecycle_flag",
    }


def test_fingerprint_bundle_is_deterministic(tmp_path: Path) -> None:
    bundle = tmp_path / "bundle"
    (bundle / "visible").mkdir(parents=True)
    (bundle / "evaluator_only").mkdir(parents=True)
    (bundle / "visible" / "README.md").write_text("alpha\n", encoding="utf-8")
    (bundle / "evaluator_only" / "manifest.json").write_text(
        '{"value": 1}\n', encoding="utf-8"
    )

    first = prepare_heldout.fingerprint_bundle(bundle)
    second = prepare_heldout.fingerprint_bundle(bundle)

    assert first == second
    assert first["file_count"] == 2
    assert set(first["files"]) == {
        "evaluator_only/manifest.json",
        "visible/README.md",
    }
    assert len(first["aggregate_sha256"]) == 64


def test_prepare_variant_selects_first_passing_seed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    observed_seeds: list[int] = []

    def fake_generate_case_bundle(
        output_dir: str | Path,
        config: object,
        *,
        run_self_tests: bool = True,
    ) -> dict[str, object]:
        assert run_self_tests is True
        seed = int(getattr(config, "data_seed"))
        observed_seeds.append(seed)
        output = Path(output_dir)
        output.mkdir(parents=True, exist_ok=True)

        if seed == 811:
            raise RuntimeError("synthetic self-test failure")

        (output / "visible").mkdir()
        (output / "evaluator_only").mkdir()
        (output / "visible" / "project_brief.md").write_text(
            f"seed={seed}\n", encoding="utf-8"
        )
        (output / "evaluator_only" / "self_test_report.json").write_text(
            json.dumps({"passed": True}), encoding="utf-8"
        )
        return {"case_id": "churn_v0_h1"}

    monkeypatch.setattr(
        prepare_heldout,
        "generate_case_bundle",
        fake_generate_case_bundle,
    )

    record = prepare_heldout.prepare_variant(
        protocol_version="v0.1.0",
        variant_name="H1",
        spec=_case_spec(),
        output_root=tmp_path,
        max_seed_attempts=5,
    )

    assert observed_seeds == [811, 812]
    assert record["selected_seed"] == 812
    assert record["seed_attempts"] == 2
    assert (tmp_path / "H1" / "visible" / "project_brief.md").exists()
    assert (tmp_path / "H1_bundle_fingerprint.json").exists()


def test_prepare_variant_refuses_to_overwrite_frozen_destination(
    tmp_path: Path,
) -> None:
    (tmp_path / "H1").mkdir()

    with pytest.raises(FileExistsError):
        prepare_heldout.prepare_variant(
            protocol_version="v0.1.0",
            variant_name="H1",
            spec=_case_spec(),
            output_root=tmp_path,
        )


def test_load_protocol_rejects_unregistered_seed_rule(tmp_path: Path) -> None:
    payload = {
        "protocol_version": "v0.1.0",
        "held_out_cases": {
            "H1": {
                **_case_spec(),
                "seed_selection": "pick_best_model_performance",
            }
        },
    }
    path = tmp_path / "protocol.json"
    path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match="unsupported seed-selection rule"):
        prepare_heldout.load_protocol(path)
