"""Source-free independent adjudication V02 exact bytes and non-promotion gate.

This verifies only the publicly releasable aggregate and task-independent
historical Git tree identity. It never reads private question text, per-need
source mappings, actual answers or private owner-reviewed original capsule.
"""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
REPORT = (
    ROOT / "experiments/r0_p03_navigation_probe/"
    "NEED_SOURCE_ADJUDICATION_AGGREGATE_VERIFIED_V02.md"
)
OLD = ROOT / "experiments/r0_p03_navigation_probe/NEED_SOURCE_ADJUDICATION_AGGREGATE.md"
EXPECTED_V02_SHA = "29bda10bc26c19bdaa1328dc0e378a35f48cddaef7dc7595f254dd532057ffd0"
EXPECTED_OLD_SHA = "78f7d428372c9d51ea8c44fd63ff37740306d27de729642eca6daa5d751d09b7"
HISTORICAL_COMMIT = "c57556a8bf993a1d327e9197acb7b7c745071cd8"
HISTORICAL_TREE = "75a242cf74bf803bb1f7ee113ba08420cac34807"


def test_updated_independent_summary_exact_bytes_and_no_old_report_mutation() -> None:
    raw = REPORT.read_bytes()
    assert len(raw) == 6243
    assert sha256(raw).hexdigest() == EXPECTED_V02_SHA
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    old = OLD.read_bytes()
    assert len(old) == 6168
    assert sha256(old).hexdigest() == EXPECTED_OLD_SHA


def test_all_twelve_original_needs_unchanged_and_six_real_holds_persist() -> None:
    text = REPORT.read_text(encoding="utf-8")
    rows = (
        ("Orientation and situation reconstruction", 1, 2),
        ("Project/Product relationships", 3, 0),
        ("Impact and evolution", 1, 2),
        ("Exact evidence, authority and recovery", 1, 2),
    )
    for category, provisional, hold in rows:
        assert re.search(
            rf"^\| {re.escape(category)} \| 3 \| "
            rf"{provisional} \| {hold} \| 0 \| 0 \|$",
            text, re.MULTILINE,
        )
    assert "All six material HOLDs persist" in text
    assert "not" in text.lower() and "admitted/gold source rulings" in text
    assert "Three admitted/qualified needs" in text
    assert "**Total** | **12** | **6** | **6**" in text


def test_thirty_one_originals_byte_authenticated_but_not_operatively_qualified() -> None:
    text = REPORT.read_text(encoding="utf-8")
    for phrase in (
        "Distinct requested and previously inspected path identities matched | 31 / 31",
        "Independently calculated source byte counts matching both manifest and earlier index | 31 / 31",
        "Independently calculated source SHA-256 matching both manifest and earlier index | 31 / 31",
        "Independently calculated Git blob SHA-1 matching both manifest and earlier index | 31 / 31",
        "Total inspected original-file payload bytes | 439,974",
        "Independent external Git commit-tree/owner-provenance authentication | Not performed",
        "Test, CI, frontend browser, data-science workflow or real execution replay during this update | 0",
        "Original evidence sources admitted for experimental use | 0",
    ):
        assert phrase in text
    assert "31 of 31 supplied original payloads hash-identical" in text
    assert "owner-supplied custody chain" in text


def test_material_witness_families_remain_and_are_not_auto_summed() -> None:
    text = REPORT.read_text(encoding="utf-8")
    expected = {
        "Operative state and endpoint authority": 4,
        "Real integrated project start and execution": 5,
        "Cross-track chronological lineage and measured repeatability": 3,
        "Original analytical provenance, rollback and replay": 3,
        "Capability conflict/supersession reconciliation": 2,
    }
    for category, count in expected.items():
        assert re.search(
            rf"^\| {re.escape(category)} \| {count} \|",
            text, re.MULTILINE,
        )
    assert "Families overlap and must not be summed" in text
    assert "indexed corpus remains intentionally incomplete" in text


def test_uploaded_public_report_contains_no_explicit_per_case_or_source_paths() -> None:
    text = REPORT.read_text(encoding="utf-8")
    patterns = (
        r"(?:docs|src|frontend|experiments|tests|scripts)/[A-Za-z0-9_./-]+",
        r"(?i)\b(?:case|question|need)\s*(?:0?[1-9]|1[0-2])\s*:",
        r"(?i)\b(?:B[0-4])\s+(?:wins|outperforms|failed)",
    )
    assert not any(re.search(p, text) for p in patterns)
    assert "no candidate wording" in text


def test_pinned_local_git_tree_matches_independently_observed_public_tree_id() -> None:
    result = subprocess.run(
        ["git", "rev-parse", HISTORICAL_COMMIT + "^{tree}"],
        cwd=ROOT, check=True, capture_output=True, text=True, timeout=10,
    )
    assert result.stdout.strip() == HISTORICAL_TREE
    attributes = (ROOT / ".gitattributes").read_text(encoding="utf-8")
    assert (
        "experiments/r0_p03_navigation_probe/"
        "NEED_SOURCE_ADJUDICATION_AGGREGATE_VERIFIED_V02.md -text"
    ) in attributes
