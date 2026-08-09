from __future__ import annotations

import json
from pathlib import Path

import pytest

from ads_v0.semantic_judge import (
    assert_packet_blinded,
    build_blinded_judge_packet,
    combine_judge_passes,
    normalize_external_trajectory,
)


def _judgment(*, default_score: int = 2, sc1: bool = False, sc2: bool = False):
    return {
        "judgment": {
            "criteria": {
                f"S{i}": {
                    "score": default_score,
                    "justification": "test",
                    "evidence_refs": ["A01"],
                }
                for i in range(1, 11)
            },
            "semantic_critical": {
                "SC1": {
                    "flag": sc1,
                    "justification": "test",
                    "evidence_refs": [],
                },
                "SC2": {
                    "flag": sc2,
                    "justification": "test",
                    "evidence_refs": [],
                },
            },
            "overall_summary": "test",
        }
    }


def test_normalizer_excludes_system_prompt_and_keeps_common_external_evidence():
    conversation = {
        "messages": [
            {
                "role": "system",
                "content": "Condition B1 with privileged static knowledge.",
            },
            {"role": "user", "content": "Begin the project."},
            {
                "role": "assistant",
                "content": json.dumps(
                    {
                        "rationale": "Inspect files.",
                        "command": {"type": "list_artifacts"},
                    }
                ),
            },
            {
                "role": "user",
                "content": "HARNESS_RESULT\n"
                + json.dumps({"status": "ok", "artifacts": ["README.md"]}),
            },
            {
                "role": "assistant",
                "content": "P0 internal state update that is not a common command.",
            },
        ]
    }

    timeline = normalize_external_trajectory(conversation)

    assert len(timeline) == 2
    assert timeline[0]["evidence_ref"] == "A01"
    assert timeline[0]["command"]["type"] == "list_artifacts"
    assert timeline[1]["evidence_ref"] == "R01"
    serialized = json.dumps(timeline)
    assert "Condition B1" not in serialized
    assert "P0 internal state" not in serialized


def test_build_packet_rejects_condition_or_run_id_leak(tmp_path: Path):
    bundle = tmp_path / "bundle"
    evaluator = bundle / "evaluator_only"
    evaluator.mkdir(parents=True)
    manifest = {
        "world_truth": {},
        "source_authority": {},
        "dynamic_events": [],
        "acceptance_contract": {},
    }
    (evaluator / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

    run = tmp_path / "run"
    run.mkdir()
    (run / "conversation.json").write_text(
        json.dumps(
            {
                "messages": [
                    {
                        "role": "assistant",
                        "content": json.dumps(
                            {
                                "rationale": "normal",
                                "command": {"type": "list_artifacts"},
                            }
                        ),
                    },
                    {
                        "role": "user",
                        "content": "HARNESS_RESULT\n"
                        + json.dumps({"status": "ok"}),
                    },
                ]
            }
        ),
        encoding="utf-8",
    )
    (run / "milestones.json").write_text(
        json.dumps(
            {
                "phase_1_report": None,
                "final_lock_report": None,
                "final_report": None,
            }
        ),
        encoding="utf-8",
    )
    (run / "summary.json").write_text(
        json.dumps({"condition": "B1", "run_id": "dev-b1-02"}),
        encoding="utf-8",
    )

    packet = build_blinded_judge_packet(bundle_dir=bundle, run_dir=run)
    serialized = json.dumps(packet)
    assert "dev-b1-02" not in serialized
    assert "B1" not in serialized

    with pytest.raises(ValueError):
        assert_packet_blinded(
            {"bad": "trajectory dev-b1-02"},
            forbidden_tokens=["dev-b1-02", "B1"],
        )


def test_adjacent_disagreement_is_averaged_without_manual_adjudication():
    first = _judgment(default_score=2)
    second = _judgment(default_score=2)
    second["judgment"]["criteria"]["S3"]["score"] = 1

    combined = combine_judge_passes(first, second)

    assert combined["consensus_scores"]["S3"] == 1.5
    assert combined["manual_adjudication_required"] is False
    assert combined["targeted_architecture_score"] == pytest.approx(1.9)
    assert combined["strong_targeted_pass"] is False


def test_extreme_score_disagreement_requires_manual_adjudication():
    first = _judgment(default_score=2)
    second = _judgment(default_score=2)
    second["judgment"]["criteria"]["S1"]["score"] = 0

    combined = combine_judge_passes(first, second)

    assert combined["consensus_scores"]["S1"] is None
    assert combined["targeted_architecture_score"] is None
    assert combined["strong_targeted_pass"] is None
    assert combined["manual_adjudication_required"] is True


def test_semantic_critical_disagreement_requires_manual_adjudication():
    first = _judgment(default_score=2, sc1=False)
    second = _judgment(default_score=2, sc1=True)

    combined = combine_judge_passes(first, second)

    assert combined["semantic_critical_consensus"]["SC1"] is None
    assert combined["manual_adjudication_required"] is True
