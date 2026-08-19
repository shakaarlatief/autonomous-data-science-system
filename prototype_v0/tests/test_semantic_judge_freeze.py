from __future__ import annotations

import json
import zipfile
from pathlib import Path

import pytest

from ads_v0 import semantic_judge_freeze as freeze
from ads_v0.semantic_judge import combine_judge_passes, packet_fingerprint


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def _judgment(*, pass_number: int, score: int = 2, manual_sc1: bool = False) -> dict:
    return {
        "judgment": {
            "criteria": {
                f"S{i}": {
                    "score": score,
                    "justification": "test",
                    "evidence_refs": ["A01"],
                }
                for i in range(1, 11)
            },
            "semantic_critical": {
                "SC1": {
                    "flag": manual_sc1,
                    "justification": "test",
                    "evidence_refs": [],
                },
                "SC2": {
                    "flag": False,
                    "justification": "test",
                    "evidence_refs": [],
                },
            },
            "overall_summary": "test",
        },
        "usage": {
            "input_tokens": 10,
            "output_tokens": 5,
            "total_tokens": 15,
            "reasoning_tokens": 2,
        },
        "model": "test-model",
        "response_id": f"response-{pass_number}",
        "output_metadata": {},
        "pass_number": pass_number,
        "provider_attempt": 1,
    }


def _make_complete_blinded_root(root: Path, *, manual_case: int | None = None) -> None:
    rows = []
    for index in range(1, 31):
        blind_id = f"case-{index:016x}"
        packet = {
            "evaluator_context": {"case": index},
            "external_trajectory": [
                {"evidence_ref": "A01", "kind": "treatment_action"}
            ],
            "milestones": {},
        }
        packet_sha = packet_fingerprint(packet)
        rows.append({"blind_id": blind_id, "packet_sha256": packet_sha})

        case_dir = root / freeze.BLINDED_DIR / blind_id
        _write_json(case_dir / "packet.json", packet)

        first = _judgment(pass_number=1, manual_sc1=False)
        second = _judgment(
            pass_number=2,
            manual_sc1=(manual_case == index),
        )
        first["packet_sha256"] = packet_sha
        second["packet_sha256"] = packet_sha
        _write_json(case_dir / "pass_1.json", first)
        _write_json(case_dir / "pass_2.json", second)

        consensus = combine_judge_passes(first, second)
        _write_json(case_dir / "consensus.json", {"consensus": consensus})

        provider_dir = case_dir / freeze.PROVIDER_ATTEMPTS_DIR
        _write_json(
            provider_dir / "pass_1_attempt_01_started.json",
            {"logical_pass": 1, "provider_attempt": 1},
        )
        _write_json(
            provider_dir / "pass_1_attempt_01_success.json",
            {"logical_pass": 1, "provider_attempt": 1},
        )
        _write_json(
            provider_dir / "pass_2_attempt_01_started.json",
            {"logical_pass": 2, "provider_attempt": 1},
        )
        _write_json(
            provider_dir / "pass_2_attempt_01_success.json",
            {"logical_pass": 2, "provider_attempt": 1},
        )

    _write_json(
        root / freeze.PREPARED_MANIFEST_FILE,
        {
            "schema_version": "semantic_judge_supervisor_v0_1",
            "case_count": 30,
            "cases": rows,
        },
    )
    _write_json(
        root / freeze.BATCH_DIR / "semantic-batch-test.json",
        {"stop_reason": "JUDGE_COMPLETE"},
    )


def test_verify_complete_blinded_state_recomputes_consensus_and_accounting(
    tmp_path: Path,
) -> None:
    root = tmp_path / "semantic"
    _make_complete_blinded_root(root)

    result = freeze.verify_blinded_state(semantic_root=root)

    assert result["prepared_cases"] == 30
    assert result["logical_passes"] == 60
    assert result["completed_cases"] == 30
    assert result["manual_adjudication_cases"] == 0
    assert result["provider_attempts_started"] == 60
    assert result["provider_attempts_succeeded"] == 60
    assert result["provider_attempts_failed"] == 0
    assert result["decoder_read"] is False
    assert len(result["aggregate_sha256"]) == 64


def test_verify_refuses_case_requiring_manual_adjudication(tmp_path: Path) -> None:
    root = tmp_path / "semantic"
    _make_complete_blinded_root(root, manual_case=1)

    with pytest.raises(RuntimeError, match="manual adjudication"):
        freeze.verify_blinded_state(semantic_root=root)


def test_verify_detects_consensus_drift(tmp_path: Path) -> None:
    root = tmp_path / "semantic"
    _make_complete_blinded_root(root)
    target = root / freeze.BLINDED_DIR / "case-0000000000000001" / "consensus.json"
    payload = json.loads(target.read_text(encoding="utf-8"))
    payload["consensus"]["consensus_scores"]["S1"] = 0.0
    _write_json(target, payload)

    with pytest.raises(ValueError, match="consensus drift"):
        freeze.verify_blinded_state(semantic_root=root)


def test_freeze_is_idempotent_and_export_excludes_private_decoder(tmp_path: Path) -> None:
    root = tmp_path / "semantic"
    exports = tmp_path / "exports"
    _make_complete_blinded_root(root)

    # This file is deliberately present but must never be read or exported.
    (root / "private_decoder.json").write_text(
        '{"condition":"P0","secret":"do not inspect"}',
        encoding="utf-8",
    )

    first, archive = freeze.freeze_blinded_state(
        semantic_root=root,
        export_root=exports,
    )
    second, second_archive = freeze.freeze_blinded_state(
        semantic_root=root,
        export_root=exports,
    )

    assert first["aggregate_sha256"] == second["aggregate_sha256"]
    assert first["status"] == "FROZEN_BLINDED_CONSENSUS"
    assert second_archive.is_file()

    with zipfile.ZipFile(archive) as zipped:
        names = zipped.namelist()
        assert freeze.FREEZE_FILE in names
        assert all("private_decoder" not in name for name in names)
        frozen = json.loads(zipped.read(freeze.FREEZE_FILE))
        assert frozen["aggregate_sha256"] == first["aggregate_sha256"]
        assert frozen["decoder_read"] is False


def test_freeze_refuses_to_overwrite_changed_frozen_evidence(tmp_path: Path) -> None:
    root = tmp_path / "semantic"
    exports = tmp_path / "exports"
    _make_complete_blinded_root(root)
    freeze.freeze_blinded_state(semantic_root=root, export_root=exports)

    target = root / freeze.BLINDED_DIR / "case-0000000000000001" / "packet.json"
    payload = json.loads(target.read_text(encoding="utf-8"))
    payload["milestones"] = {"changed": True}
    _write_json(target, payload)

    # Packet fingerprint verification fails before any prior freeze can be replaced.
    with pytest.raises(ValueError):
        freeze.freeze_blinded_state(semantic_root=root, export_root=exports)
