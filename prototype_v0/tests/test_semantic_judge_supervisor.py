from __future__ import annotations

import json
import zipfile
from dataclasses import asdict
from pathlib import Path
from types import SimpleNamespace

import pytest

from ads_v0.heldout_execution import HeldOutSlot
from ads_v0.model import ModelGenerationError
from ads_v0 import semantic_judge_supervisor as supervisor


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def _slot(index: int, condition: str) -> HeldOutSlot:
    return HeldOutSlot(
        slot_index=index,
        variant="H1",
        replicate=index,
        position_in_replicate=1,
        condition=condition,
        slot_id=f"h1-r{index:02d}-{condition.lower()}",
    )


def _record_retained_attempt(attempts_root: Path, slot: HeldOutSlot) -> Path:
    attempt_id = f"{slot.slot_id}-a01"
    run_dir = attempts_root / attempt_id
    _write_json(
        run_dir / "attempt_record.json",
        {
            "attempt_id": attempt_id,
            "slot": asdict(slot),
            "behavior_evaluable": True,
            "replacement_eligible": False,
            "slot_resolved": True,
            "classification": "BEHAVIOR_EVALUABLE",
        },
    )
    return run_dir


def _judgment(score: int = 2) -> dict:
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
                "SC1": {"flag": False, "justification": "test", "evidence_refs": []},
                "SC2": {"flag": False, "justification": "test", "evidence_refs": []},
            },
            "overall_summary": "test",
        },
        "usage": {
            "input_tokens": 10,
            "output_tokens": 5,
            "total_tokens": 15,
            "reasoning_tokens": 3,
        },
        "model": supervisor.JUDGE_MODEL,
        "response_id": "response-test",
        "output_metadata": {},
    }


def _make_prepared_root(root: Path, case_count: int = 2) -> list[str]:
    blind_ids = [f"case-{index:016x}" for index in range(1, case_count + 1)]
    rows = []
    for index, blind_id in enumerate(blind_ids, start=1):
        packet = {
            "evaluator_context": {"case": index},
            "external_trajectory": [{"evidence_ref": "A01", "kind": "treatment_action"}],
            "milestones": {},
        }
        packet_sha = supervisor.packet_fingerprint(packet)
        case_dir = root / supervisor.BLINDED_DIR / blind_id
        _write_json(case_dir / "packet.json", packet)
        rows.append({"blind_id": blind_id, "packet_sha256": packet_sha})

    _write_json(
        root / supervisor.PREPARED_MANIFEST_FILE,
        {
            "schema_version": "semantic_judge_supervisor_v0_1",
            "case_count": case_count,
            "cases": rows,
        },
    )
    _write_json(
        root / supervisor.PRIVATE_DECODER_FILE,
        {
            "warning": "PRIVATE",
            "cases": [{"blind_id": blind_ids[0], "condition": "P0"}],
        },
    )
    return blind_ids


def test_prepare_creates_opaque_packets_and_private_decoder(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    semantic_root = tmp_path / "semantic"
    attempts_root = tmp_path / "attempts"
    bundle_root = tmp_path / "bundles"

    # Production preparation always contains 30 slots. Construct a synthetic
    # complete plan with unique slot identities so the test exercises the same
    # cardinality and uniqueness invariants without requiring generated bundles.
    conditions = ["B0", "B1", "P0"] * 10
    slots = tuple(
        HeldOutSlot(
            slot_index=index,
            variant="H1" if index <= 15 else "H2",
            replicate=((index - 1) // 3) % 5 + 1,
            position_in_replicate=((index - 1) % 3) + 1,
            condition=condition,
            slot_id=f"slot-{index:02d}-{condition.lower()}",
        )
        for index, condition in enumerate(conditions, start=1)
    )
    for slot in slots:
        _record_retained_attempt(attempts_root, slot)

    monkeypatch.setattr(
        supervisor,
        "_validate_experiment_complete",
        lambda *, attempts_root: ({}, slots),
    )

    packet_counter = {slot.slot_id: slot.slot_index for slot in slots}

    def fake_packet_builder(*, bundle_dir: Path, run_dir: Path) -> dict:
        record = json.loads((run_dir / "attempt_record.json").read_text(encoding="utf-8"))
        slot_id = record["slot"]["slot_id"]
        return {
            "evaluator_context": {"synthetic_case": packet_counter[slot_id]},
            "external_trajectory": [{"evidence_ref": "A01", "kind": "treatment_action"}],
            "milestones": {},
        }

    monkeypatch.setattr(supervisor, "build_blinded_judge_packet", fake_packet_builder)
    checked_tokens: list[str] = []

    def fake_blind_check(packet: dict, *, forbidden_tokens: list[str]) -> None:
        checked_tokens.extend(forbidden_tokens)

    monkeypatch.setattr(supervisor, "assert_packet_blinded", fake_blind_check)

    manifest = supervisor.prepare_blinded_cases(
        semantic_root=semantic_root,
        attempts_root=attempts_root,
        bundle_root=bundle_root,
    )

    assert manifest["case_count"] == 30
    assert len({row["blind_id"] for row in manifest["cases"]}) == 30
    assert "B0" in checked_tokens and "B1" in checked_tokens and "P0" in checked_tokens

    decoder = json.loads(
        (semantic_root / supervisor.PRIVATE_DECODER_FILE).read_text(encoding="utf-8")
    )
    assert len(decoder["cases"]) == 30
    assert all("condition" in row["slot"] for row in decoder["cases"])

    for row in manifest["cases"]:
        blind_id = row["blind_id"]
        assert blind_id.startswith("case-")
        assert "b0" not in blind_id.lower()
        assert "b1" not in blind_id.lower()
        assert "p0" not in blind_id.lower()
        assert (semantic_root / supervisor.BLINDED_DIR / blind_id / "packet.json").is_file()


def test_run_batch_persists_two_passes_and_resumes_without_rerunning(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    semantic_root = tmp_path / "semantic"
    export_root = tmp_path / "exports"
    blind_ids = _make_prepared_root(semantic_root, case_count=2)

    # The production loader requires 30 cases. Expand the synthetic manifest to
    # 30 while only the first two need real work by pre-populating the remaining
    # 28 cases with completed pass/consensus files.
    rows = json.loads(
        (semantic_root / supervisor.PREPARED_MANIFEST_FILE).read_text(encoding="utf-8")
    )["cases"]
    for index in range(3, 31):
        blind_id = f"case-{index:016x}"
        packet = {
            "evaluator_context": {"case": index},
            "external_trajectory": [{"evidence_ref": "A01", "kind": "treatment_action"}],
            "milestones": {},
        }
        packet_sha = supervisor.packet_fingerprint(packet)
        case_dir = semantic_root / supervisor.BLINDED_DIR / blind_id
        _write_json(case_dir / "packet.json", packet)
        first = _judgment()
        first["pass_number"] = 1
        second = _judgment()
        second["pass_number"] = 2
        _write_json(case_dir / "pass_1.json", first)
        _write_json(case_dir / "pass_2.json", second)
        supervisor._persist_consensus_if_ready(case_dir)
        rows.append({"blind_id": blind_id, "packet_sha256": packet_sha})
    _write_json(
        semantic_root / supervisor.PREPARED_MANIFEST_FILE,
        {"schema_version": "semantic_judge_supervisor_v0_1", "case_count": 30, "cases": rows},
    )

    monkeypatch.setattr(
        supervisor,
        "prepare_blinded_cases",
        lambda **kwargs: json.loads(
            (semantic_root / supervisor.PREPARED_MANIFEST_FILE).read_text(encoding="utf-8")
        ),
    )

    calls: list[int] = []

    class FakeJudge:
        def evaluate(self, packet: dict) -> dict:
            calls.append(packet["evaluator_context"]["case"])
            return _judgment()

    result = supervisor.run_judge_batch(
        max_judge_calls=4,
        semantic_root=semantic_root,
        export_root=export_root,
        judge_factory=FakeJudge,
    )

    assert result.stop_reason == "JUDGE_COMPLETE"
    assert result.provider_calls_launched == 4
    assert result.logical_passes_persisted == 60
    assert result.completed_cases == 30
    assert calls == [1, 1, 2, 2]

    for blind_id in blind_ids:
        case_dir = semantic_root / supervisor.BLINDED_DIR / blind_id
        assert (case_dir / "pass_1.json").is_file()
        assert (case_dir / "pass_2.json").is_file()
        assert (case_dir / "consensus.json").is_file()

    calls.clear()
    resumed = supervisor.run_judge_batch(
        max_judge_calls=4,
        semantic_root=semantic_root,
        export_root=export_root,
        judge_factory=FakeJudge,
    )
    assert resumed.provider_calls_launched == 0
    assert resumed.stop_reason == "JUDGE_COMPLETE"
    assert calls == []


def test_provider_failure_is_logged_and_retried_only_before_usable_pass(
    tmp_path: Path,
) -> None:
    semantic_root = tmp_path / "semantic"
    export_root = tmp_path / "exports"
    _make_prepared_root(semantic_root, case_count=1)

    # Expand to 30 prepared cases, with 29 already complete, so only one blinded
    # case exercises the provider-recovery path.
    manifest = json.loads(
        (semantic_root / supervisor.PREPARED_MANIFEST_FILE).read_text(encoding="utf-8")
    )
    for index in range(2, 31):
        blind_id = f"case-{index:016x}"
        packet = {
            "evaluator_context": {"case": index},
            "external_trajectory": [{"evidence_ref": "A01", "kind": "treatment_action"}],
            "milestones": {},
        }
        packet_sha = supervisor.packet_fingerprint(packet)
        case_dir = semantic_root / supervisor.BLINDED_DIR / blind_id
        _write_json(case_dir / "packet.json", packet)
        first = _judgment()
        first["pass_number"] = 1
        second = _judgment()
        second["pass_number"] = 2
        _write_json(case_dir / "pass_1.json", first)
        _write_json(case_dir / "pass_2.json", second)
        supervisor._persist_consensus_if_ready(case_dir)
        manifest["cases"].append({"blind_id": blind_id, "packet_sha256": packet_sha})
    manifest["case_count"] = 30
    _write_json(semantic_root / supervisor.PREPARED_MANIFEST_FILE, manifest)

    # run_judge_batch would call production preparation, which depends on the
    # real held-out ledger. The recovery behavior itself is isolated by calling
    # the logical-pass primitive directly.
    _, cases = supervisor._load_prepared_cases(semantic_root)
    target = cases[0]
    sequence = ["fail", "success", "success"]

    class FakeJudge:
        def evaluate(self, packet: dict) -> dict:
            outcome = sequence.pop(0)
            if outcome == "fail":
                raise ModelGenerationError(
                    "temporary provider failure",
                    retryable=True,
                    provider="test",
                    error_code="temporary",
                )
            return _judgment()

    status, used = supervisor._run_one_logical_pass(
        case=target,
        pass_number=1,
        semantic_root=semantic_root,
        judge_factory=FakeJudge,
        remaining_call_budget=3,
    )
    assert status == "PASS_PERSISTED"
    assert used == 2

    case_dir = semantic_root / supervisor.BLINDED_DIR / target.blind_id
    attempts_dir = case_dir / supervisor.PROVIDER_ATTEMPTS_DIR
    assert (attempts_dir / "pass_1_attempt_01_error.json").is_file()
    assert (attempts_dir / "pass_1_attempt_02_success.json").is_file()
    assert (case_dir / "pass_1.json").is_file()

    # Once the usable pass exists, the same logical pass is never judged again.
    status_again, used_again = supervisor._run_one_logical_pass(
        case=target,
        pass_number=1,
        semantic_root=semantic_root,
        judge_factory=FakeJudge,
        remaining_call_budget=3,
    )
    assert status_again == "PASS_PERSISTED"
    assert used_again == 0


def test_blinded_export_explicitly_excludes_private_decoder(tmp_path: Path) -> None:
    semantic_root = tmp_path / "semantic"
    export_root = tmp_path / "exports"
    _make_prepared_root(semantic_root, case_count=30)

    archive = supervisor.export_blinded_review(
        semantic_root=semantic_root,
        export_root=export_root,
    )

    with zipfile.ZipFile(archive) as zipped:
        names = zipped.namelist()
        assert supervisor.PRIVATE_DECODER_FILE not in names
        assert all("private_decoder" not in name for name in names)
        summary = json.loads(zipped.read("blinded_export_summary.json"))
        assert summary["decoder_included"] is False
