"""Prospective two-file neutral independent-need input invariants.

The tests do not invent or grade the twelve primary tasks, read hidden gold,
admit original source files, or certify an independent future actor.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
from zipfile import ZipFile
import pytest

from experiments.r0_p03_navigation_probe import neutral_need_origination_packet as m

ROOT = Path(__file__).resolve().parents[2]
LOCAL = ROOT / m.LOCAL_FOLDER
ARCHIVE = LOCAL / m.ARCHIVE_NAME
RECEIPT = LOCAL / m.RECEIPT_NAME
PRIVATE_COORDINATOR_MANIFEST = (
    LOCAL / "R0_P03_FRESH_NEED_ORIGINATION.coordinator_provenance.json"
)


def test_real_historical_supporting_origins_are_exact_and_not_copied() -> None:
    evidence = m.verify_originals(ROOT)
    assert len(evidence) == 5
    assert set(evidence) == set(m.SOURCE_PROVENANCE)
    for path, item in evidence.items():
        assert item["sha256"] == m.SOURCE_PROVENANCE[path]["sha256"]
        assert item["git_blob"] == m.SOURCE_PROVENANCE[path]["git_blob"]
        assert item["source_witness_type"] == (
            "DECLARATION_ONLY_NOT_IMPLEMENTATION_PROOF"
        )


def test_exact_real_artifact_has_two_neutral_files_and_no_original_sources() -> None:
    with ZipFile(ARCHIVE) as z:
        assert z.namelist() == sorted(m.AUTHOR_FILES)
        assert z.testzip() is None
        author_inputs = {name: z.read(name) for name in z.namelist()}
    assert sum(map(len, author_inputs.values())) < 12000
    assert all(b"R0_P03" not in raw for raw in author_inputs.values())
    m.check_author_texts(author_inputs)
    assert set(author_inputs) == {"AUTHOR_BRIEF.md", "NEUTRAL_CONTEXT.md"}
    assert sha256(m.zip_data(author_inputs)).digest() == sha256(ARCHIVE.read_bytes()).digest()


def test_author_brief_is_need_origin_only_and_has_no_answer_key() -> None:
    with ZipFile(ARCHIVE) as z:
        author = z.read("AUTHOR_BRIEF.md").decode()
        context = z.read("NEUTRAL_CONTEXT.md").decode()
    assert "up to **twelve distinct" in author
    assert "NOT_YET_ADJUDICATED" in author
    assert "Do not" in author
    assert "NEED_PROPOSALS_RESTRICTED.md" in author
    assert "NEED_ORIGINATION_SAFE_RECEIPT.md" in author
    assert "source-specific" not in context.lower()
    assert "not a statement that any architecture" in context
    assert "not by itself prove a production deployment" in context
    assert "complete current state" in context


@pytest.mark.parametrize("leak", [
    "\nResearch 217: old comparator expected sources\n",
    "\nR0-P03: test outcome\n",
    "\nB2 wins the benchmark\n",
    "\ndocs/research/513_scoring_answer.md\n",
    "\nhttps://example.org/hidden/gold\n",
    "\n" + "b" * 40 + "\n",
    "\n" + "c" * 64 + "\n",
])
def test_leakage_guard_rejects_direct_known_forbidden_tokens(leak: str) -> None:
    source = (ROOT / "experiments/r0_p03_navigation_probe/"
              "NEED_ORIGINATION_NEUTRAL_CONTEXT_V01.md").read_bytes()
    mutated = {
        "NEUTRAL_CONTEXT.md": source + leak.encode(),
        "AUTHOR_BRIEF.md": (
            ROOT / "experiments/r0_p03_navigation_probe/"
            "NEED_ORIGINATION_INDEPENDENT_AUTHOR_BRIEF_V01.md"
        ).read_bytes(),
    }
    with pytest.raises(ValueError, match="Recognized"):
        m.check_author_texts(mutated)


def test_historical_input_and_deterministic_local_receipt_reproducible() -> None:
    receipt = m.build(ROOT, verify_only=True)
    assert receipt["archive_bytes"] == 3158
    assert receipt["archive_sha256"] == (
        "56c3c6fe3955ff8746bedb426df23e953555a6a67dce16d6b04d63a4ea4c25be"
    )
    assert sha256(ARCHIVE.read_bytes()).hexdigest() == receipt["archive_sha256"]
    assert m.stable_json(receipt) == RECEIPT.read_bytes()
    provenance = json.loads(PRIVATE_COORDINATOR_MANIFEST.read_text())
    assert provenance["source_admissions"] == 0
    assert provenance["author_visible_original_source_files"] == 0
    assert provenance["owner_transfer_authorization"] == "NOT_YET_AUTHORIZED"
    assert provenance["task_proposals_created"] == 0
    assert provenance["answer_key"] == "NONE"
    assert provenance["semantic_disclosure_clearance"] == (
        "CANDIDATE_PENDING_ACTUAL_AUTHOR_ROLE_EXPOSURE"
    )


def test_corrupt_historical_bytes_fail_without_fabricating_evidence(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    original = m.git

    def corrupt(repo: Path, *args: str) -> bytes:
        raw = original(repo, *args)
        if args[:1] == ("show",):
            return raw + b"tamper"
        return raw

    monkeypatch.setattr(m, "git", corrupt)
    with pytest.raises(ValueError, match="Source provenance drift"):
        m.verify_originals(ROOT)


def test_original_copy_and_author_packet_remain_separate() -> None:
    path = ROOT / "experiments/r0_p03_navigation_probe"
    assert (path / "NEED_ORIGINATION_NEUTRAL_CONTEXT_V01.md").is_file()
    assert (path / "NEED_ORIGINATION_INDEPENDENT_AUTHOR_BRIEF_V01.md").is_file()
    assert PRIVATE_COORDINATOR_MANIFEST.parent == ARCHIVE.parent
    attributes = (ROOT / ".gitattributes").read_text(encoding="utf-8")
    for tracked in (
        "NEED_ORIGINATION_NEUTRAL_CONTEXT_V01.md",
        "NEED_ORIGINATION_INDEPENDENT_AUTHOR_BRIEF_V01.md",
    ):
        assert (
            "experiments/r0_p03_navigation_probe/" + tracked + " -text"
        ) in attributes
    with ZipFile(ARCHIVE) as z:
        assert not any(name.endswith("provenance.json") for name in z.namelist())
        assert not any(name.startswith("sources/") for name in z.namelist())
