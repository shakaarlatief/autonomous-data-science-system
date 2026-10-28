"""Deterministic source-free comparison of A2 candidate-reported file properties.

These tests compare the current, owner-relayed transcription of a separate
session's report against exact independently produced local fixture bytes.
Neither these assertions nor an exact SHA-256 match constitute an audit of
the candidate's tool execution or a real reviewer/challenger qualification.
"""
from __future__ import annotations

import hashlib
import struct
import zlib
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "experiments" / "r0_p03_navigation_probe"
REPORT = BASE / "reviewer_intake_evidence" / "20261028_a2_candidate_fidelity_owner_relayed_report.md"
BRIEF = BASE / "S1_A2_CANDIDATE_FIDELITY_PROBE_V01.md"
TEXT = BASE / "a2_source_free_fidelity_unicode_crlf.txt"
PNG = BASE / "a2_source_free_fidelity_pattern.png"

EXPECTED = {
    BRIEF.name: (5392, "c00df15f79b1b734a40efa34b5fe14aed536fdedafb4acba49a77114974e384c"),
    TEXT.name: (193, "8af9f2f5ea35071e1e8db50e0f467188a63b0a2ad390e5a3eba3853b109603fb"),
    PNG.name: (291, "fb598054eef1c3200b13967887f225d41acfd88059c6a335f9cb4655fa3cb05f"),
}


def test_all_three_reported_hashes_match_original_files() -> None:
    report = REPORT.read_text(encoding="utf-8")
    for path in (BRIEF, TEXT, PNG):
        raw = path.read_bytes()
        count, sha = EXPECTED[path.name]
        assert len(raw) == count
        assert hashlib.sha256(raw).hexdigest() == sha
        assert path.name in report
        assert sha in report
        assert f"{count:,}" in report


def test_text_content_and_line_endings_match_reported_values() -> None:
    report = REPORT.read_text(encoding="utf-8")
    assert "50" in report and "Standalone LF" in report
    assert BRIEF.read_bytes().count(b"\n") == 50
    assert BRIEF.read_bytes().count(b"\r") == 0
    assert BRIEF.read_bytes().endswith(b"\n")
    raw = TEXT.read_bytes()
    assert raw.count(b"\r\n") == 5
    assert raw.count(b"\n") == 5
    assert raw.count(b"\t") == 1
    assert not raw.endswith(b"\n")
    for fragment in ("café", "naïve", "Δ", "雪", "مرحبا"):
        assert fragment in raw.decode("utf-8")
    assert "preserved raw CRLF sequences" in report


def _parsed_rgb_pixels(raw_png: bytes) -> tuple[int, int, Counter[tuple[int, int, int]], bytes]:
    assert raw_png[:8] == b"\x89PNG\r\n\x1a\n"
    chunks: dict[bytes, bytes] = {}
    pos = 8
    while pos < len(raw_png):
        length = struct.unpack("!I", raw_png[pos:pos + 4])[0]
        kind = raw_png[pos + 4:pos + 8]
        data = raw_png[pos + 8:pos + 8 + length]
        crc = struct.unpack("!I", raw_png[pos + 8 + length:pos + 12 + length])[0]
        assert zlib.crc32(kind + data) & 0xffffffff == crc
        chunks[kind] = data
        pos += length + 12
    assert list(chunks) == [b"IHDR", b"tEXt", b"IDAT", b"IEND"]
    assert pos == len(raw_png)
    width, height = struct.unpack("!II", chunks[b"IHDR"][:8])
    assert chunks[b"IHDR"][8:] == bytes((8, 2, 0, 0, 0))
    filtered_pixels = zlib.decompress(chunks[b"IDAT"])
    row_length = 1 + width * 3
    assert len(filtered_pixels) == height * row_length
    assert all(filtered_pixels[y * row_length] == 0 for y in range(height))
    colors = Counter(
        tuple(filtered_pixels[y * row_length + 1 + 3 * x:y * row_length + 4 + 3 * x])
        for y in range(height)
        for x in range(width)
    )
    return width, height, colors, chunks[b"tEXt"]


def test_original_png_pixels_and_metadata_match_report() -> None:
    width, height, counts, metadata = _parsed_rgb_pixels(PNG.read_bytes())
    assert (width, height) == (48, 32)
    assert counts == {
        (219, 61, 47): 651,
        (45, 96, 207): 641,
        (42, 178, 86): 212,
        (248, 234, 202): 32,
    }
    assert sum(counts.values()) == 1536
    assert metadata == b"Comment\x00S1 A2 source-free integrity probe"
    report = REPORT.read_text(encoding="utf-8")
    for color, count in counts.items():
        assert f"`{color}`" in report
        assert f"{count:,}" in report
    assert "1,536" in report and "Comment" in report


def test_transcription_is_not_claimed_as_verbatim_upstream_bytes() -> None:
    report = REPORT.read_text(encoding="utf-8")
    assert "original-byte export of the Temporary Chat response" in report
    assert "user-relayed" not in report or "transcribed" in report
    assert "independently audited tool-call telemetry" in report
    assert "pre-upload file identity `NOT_VERIFIED`" not in report or "NOT_VERIFIED" in report


def test_report_does_not_advance_review_or_source_admission() -> None:
    report = REPORT.read_text(encoding="utf-8")
    for item in (
        "TEXT_AND_PNG_BYTES_AND_RENDER_VERIFIED",
        "REAL_REVIEWER_ROLE=PENDING",
        "REAL_CHALLENGER_ROLE=PENDING",
        "RESTRICTED_REPORT_ROUTE=NOT_TESTED_IN_THIS_PROBE",
        "AUTHOR_VIEW_DENIAL=NOT_TESTED_IN_THIS_PROBE",
        "HISTORICAL_SOURCES_DELIVERED=ZERO",
        "GOLD=NONE",
        "SCORING=NOT_STARTED",
    ):
        assert item in report
