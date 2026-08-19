from __future__ import annotations

import csv
import json
import zipfile
from pathlib import Path

import pytest

from ads_v0 import semantic_judge_decode as decode


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def _consensus(targeted: float = 1.6) -> dict:
    scores = {
        "S1": 1.0,
        "S2": 2.0,
        "S3": 2.0,
        "S4": 1.0,
        "S5": 2.0,
        "S6": 2.0,
        "S7": 2.0,
        "S8": 2.0,
        "S9": 2.0,
        "S10": 2.0,
    }
    return {
        "consensus": {
            "consensus_scores": scores,
            "semantic_critical_consensus": {"SC1": False, "SC2": False},
            "targeted_architecture_score": targeted,
            "strong_targeted_pass": False,
            "manual_adjudication_required": False,
            "disagreements": [],
        }
    }


def _make_decodable_root(tmp_path: Path) -> tuple[Path, dict, dict]:
    semantic_root = tmp_path / "semantic"
    attempts_root = tmp_path / "attempts"
    cases = []
    decoder_rows = []

    slot_index = 0
    for variant in ("H1", "H2"):
        for replicate in range(1, 6):
            for position, condition in enumerate(("B0", "B1", "P0"), start=1):
                slot_index += 1
                blind_id = f"case-{slot_index:016x}"
                packet_sha = f"{slot_index:064x}"
                attempt_id = f"{variant.lower()}-r{replicate:02d}-{condition.lower()}-a01"
                run_dir = attempts_root / attempt_id
                target = 1.5 if condition == "B0" else 1.6 if condition == "B1" else 1.7

                _write_json(
                    semantic_root / decode.BLINDED_DIR / blind_id / "consensus.json",
                    _consensus(target),
                )
                _write_json(
                    run_dir / "summary.json",
                    {
                        "run_id": attempt_id,
                        "condition": condition,
                        "behavior_evaluable": True,
                        "critical_failures": [],
                        "completed": True,
                        "completed_within_budget": condition != "P0",
                        "budget_exhausted": condition == "P0",
                        "model_calls": 10 if condition != "P0" else 12,
                        "generation_attempts": 10 if condition != "P0" else 12,
                        "generation_failures": 0,
                        "python_execution_attempts": 4 if condition != "P0" else 5,
                        "total_tokens": 100_000 if condition != "P0" else 200_000,
                    },
                )
                _write_json(run_dir / "milestones.json", {"final_report": {"ok": True}})

                slot = {
                    "slot_index": slot_index,
                    "variant": variant,
                    "replicate": replicate,
                    "position_in_replicate": position,
                    "condition": condition,
                    "slot_id": f"{variant.lower()}-r{replicate:02d}-{condition.lower()}",
                }
                cases.append(
                    {
                        "blind_id": blind_id,
                        "packet_sha256": packet_sha,
                        "manual_adjudication_required": False,
                    }
                )
                decoder_rows.append(
                    {
                        "blind_id": blind_id,
                        "packet_sha256": packet_sha,
                        "slot": slot,
                        "attempt_number": 1,
                        "attempt_id": attempt_id,
                        "run_dir": str(run_dir),
                        "bundle_dir": str(tmp_path / "bundles" / variant),
                    }
                )

    frozen = {
        "status": "FROZEN_BLINDED_CONSENSUS",
        "decoder_read": False,
        "manual_adjudication_cases": 0,
        "aggregate_sha256": "a" * 64,
        "cases": cases,
    }
    verification = {
        "aggregate_sha256": "a" * 64,
        "prepared_cases": 30,
        "logical_passes": 60,
        "completed_cases": 30,
        "manual_adjudication_cases": 0,
        "provider_attempts_started": 60,
    }
    _write_json(
        semantic_root / decode.PRIVATE_DECODER_FILE,
        {"schema_version": "test", "cases": decoder_rows},
    )
    return semantic_root, frozen, verification


def test_validate_frozen_boundary_recomputes_before_decode(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    semantic_root = tmp_path / "semantic"
    frozen = {
        "status": "FROZEN_BLINDED_CONSENSUS",
        "decoder_read": False,
        "manual_adjudication_cases": 0,
        "aggregate_sha256": "b" * 64,
    }
    _write_json(semantic_root / decode.FREEZE_FILE, frozen)

    calls = []

    def fake_verify(*, semantic_root: Path) -> dict:
        calls.append(semantic_root)
        return {
            "aggregate_sha256": "b" * 64,
            "prepared_cases": 30,
            "logical_passes": 60,
            "completed_cases": 30,
            "manual_adjudication_cases": 0,
            "provider_attempts_started": 60,
        }

    monkeypatch.setattr(decode, "verify_blinded_state", fake_verify)
    observed_frozen, verification = decode._validate_frozen_boundary(semantic_root)

    assert calls == [semantic_root]
    assert observed_frozen["aggregate_sha256"] == "b" * 64
    assert verification["logical_passes"] == 60


def test_validate_frozen_boundary_rejects_aggregate_drift(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    semantic_root = tmp_path / "semantic"
    _write_json(
        semantic_root / decode.FREEZE_FILE,
        {
            "status": "FROZEN_BLINDED_CONSENSUS",
            "decoder_read": False,
            "manual_adjudication_cases": 0,
            "aggregate_sha256": "c" * 64,
        },
    )
    monkeypatch.setattr(
        decode,
        "verify_blinded_state",
        lambda *, semantic_root: {
            "aggregate_sha256": "d" * 64,
            "prepared_cases": 30,
            "logical_passes": 60,
            "completed_cases": 30,
            "manual_adjudication_cases": 0,
            "provider_attempts_started": 60,
        },
    )

    with pytest.raises(ValueError, match="no longer matches"):
        decode._validate_frozen_boundary(semantic_root)


def test_build_decoded_result_maps_all_conditions_after_freeze(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    semantic_root, frozen, verification = _make_decodable_root(tmp_path)
    monkeypatch.setattr(
        decode,
        "_validate_frozen_boundary",
        lambda root: (frozen, verification),
    )

    result = decode.build_decoded_result(semantic_root=semantic_root)

    assert len(result["run_rows"]) == 30
    assert {row["condition"] for row in result["run_rows"]} == {"B0", "B1", "P0"}
    assert result["decoder_read_after_freeze_verification"] is True
    pooled = result["summaries"]["pooled"]
    assert pooled["B0"]["n"] == 10
    assert pooled["B1"]["n"] == 10
    assert pooled["P0"]["n"] == 10
    assert pooled["B0"]["targeted_architecture_mean"] == pytest.approx(1.5)
    assert pooled["B1"]["targeted_architecture_mean"] == pytest.approx(1.6)
    assert pooled["P0"]["targeted_architecture_mean"] == pytest.approx(1.7)


def test_registered_comparison_reports_failure_without_inventing_architecture_diagnostics(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    semantic_root, frozen, verification = _make_decodable_root(tmp_path)
    monkeypatch.setattr(
        decode,
        "_validate_frozen_boundary",
        lambda root: (frozen, verification),
    )

    result = decode.build_decoded_result(semantic_root=semantic_root)
    comparison = result["registered_comparison_facts"]

    assert comparison["pooled_targeted_mean_difference_P0_minus_B1"] == pytest.approx(0.1)
    assert comparison["resource_median_ratios_P0_over_B1"]["total_tokens"] == pytest.approx(2.0)
    assert comparison["continuation_signal_already_impossible_from_resolved_components"] is True
    assert len(comparison["architecture_specific_clauses_not_scored_here"]) == 3
    assert result["interpretation_boundary"]["architecture_specific_P0_diagnostics_inferred"] is False


def test_decode_export_contains_decoded_outputs_but_not_raw_private_decoder(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    semantic_root, frozen, verification = _make_decodable_root(tmp_path)
    output_root = tmp_path / "decoded"
    export_root = tmp_path / "exports"
    monkeypatch.setattr(
        decode,
        "_validate_frozen_boundary",
        lambda root: (frozen, verification),
    )

    result, archive = decode.decode_and_export(
        semantic_root=semantic_root,
        output_root=output_root,
        export_root=export_root,
    )

    assert result["frozen_semantic_aggregate_sha256"] == "a" * 64
    with zipfile.ZipFile(archive) as zipped:
        names = set(zipped.namelist())
        assert names == {decode.DECODED_RESULT_FILE, decode.RUN_TABLE_FILE}
        assert decode.PRIVATE_DECODER_FILE not in names
        decoded_payload = json.loads(zipped.read(decode.DECODED_RESULT_FILE))
        assert len(decoded_payload["run_rows"]) == 30
        csv_rows = list(
            csv.DictReader(
                zipped.read(decode.RUN_TABLE_FILE).decode("utf-8").splitlines()
            )
        )
        assert len(csv_rows) == 30
