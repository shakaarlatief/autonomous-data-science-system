"""Source-free evidence and file-fidelity fixture contracts for R0-P03 S1 A2.

These tests are intentionally mechanical. They verify local fixture bytes,
decoding and nontext PNG structure, and the complete owner-relayed candidate
session intake report. They do not assert model-session independence,
source-adjudication reliability, protected report custody or author access
denial. They must not be used as a reason to deliver real historical sources.
"""
from __future__ import annotations

import hashlib
import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "experiments" / "r0_p03_navigation_probe"
REPORT = BASE / "reviewer_intake_evidence" / "20261028_a2_candidate_reviewer_environment_intake_report.txt"
TEXT = BASE / "a2_source_free_fidelity_unicode_crlf.txt"
PNG = BASE / "a2_source_free_fidelity_pattern.png"
BRIEF = BASE / "S1_A2_CANDIDATE_FIDELITY_PROBE_V01.md"


def _assert_exact(path: Path, size: int, digest: str) -> bytes:
    content = path.read_bytes()
    assert len(content) == size
    assert hashlib.sha256(content).hexdigest() == digest
    return content


def _png_chunks(raw: bytes) -> list[tuple[bytes, bytes]]:
    assert raw.startswith(b"\x89PNG\r\n\x1a\n")
    chunks: list[tuple[bytes, bytes]] = []
    offset = 8
    while offset < len(raw):
        assert len(raw) - offset >= 12
        length = struct.unpack("!I", raw[offset:offset + 4])[0]
        kind = raw[offset + 4:offset + 8]
        payload = raw[offset + 8:offset + 8 + length]
        checksum = raw[offset + 8 + length:offset + 12 + length]
        assert len(payload) == length and len(checksum) == 4
        assert struct.unpack("!I", checksum)[0] == zlib.crc32(kind + payload) & 0xffffffff
        chunks.append((kind, payload))
        offset += 12 + length
    assert offset == len(raw)
    assert chunks[-1] == (b"IEND", b"")
    return chunks


def test_owner_uploaded_intake_report_preserved_with_lf_only_normalization() -> None:
    raw = _assert_exact(
        REPORT,
        16334,
        "610dd4025dbb5bc129e12ed1670dcae7efc0d9d66460893f9f4d9d9e466146dc",
    )
    assert b"\r" not in raw and not raw.endswith(b"\n")
    assert len(raw.splitlines()) == 237
    for item in (
        b"INTAKE_LIMITED",
        b"VISIBLE_UNTESTED",
        b"UNKNOWN",
        b"Actual reviewer admission remains `PENDING`",
        b"Actual challenger admission remains `PENDING`",
        b"no broad host-level access-denial claim",
    ):
        assert item.lower() in raw.lower()


def test_unicode_text_fixture_exact_binary_fidelity() -> None:
    raw = _assert_exact(
        TEXT, 193,
        "8af9f2f5ea35071e1e8db50e0f467188a63b0a2ad390e5a3eba3853b109603fb",
    )
    decoded = raw.decode("utf-8")
    assert raw.count(b"\r\n") == 5
    assert raw.count(b"\n") == 5
    assert not raw.endswith(b"\n")
    assert raw.count(b"\t") == 1
    for token in ("café", "naïve", "Δ", "雪", "مرحبا", "END-SOURCE-FREE-A2-FIXTURE"):
        assert token in decoded


def test_png_fixture_exact_binary_identity_and_consistent_chunks() -> None:
    raw = _assert_exact(
        PNG, 291,
        "fb598054eef1c3200b13967887f225d41acfd88059c6a335f9cb4655fa3cb05f",
    )
    chunks = _png_chunks(raw)
    assert [kind for kind, _ in chunks] == [
        b"IHDR", b"tEXt", b"IDAT", b"IEND"
    ]
    assert struct.unpack("!II", chunks[0][1][:8]) == (48, 32)
    assert chunks[0][1][8:] == bytes((8, 2, 0, 0, 0))
    assert chunks[1][1] == b"Comment\x00S1 A2 source-free integrity probe"


def test_png_fixture_pixel_decode_and_representation_are_not_hash_only() -> None:
    chunks = _png_chunks(PNG.read_bytes())
    image = zlib.decompress(chunks[2][1])
    width, height = 48, 32
    row_len = 1 + width * 3
    assert len(image) == height * row_len
    assert all(image[y * row_len] == 0 for y in range(height))

    def rgb(x: int, y: int) -> tuple[int, int, int]:
        offset = y * row_len + 1 + 3 * x
        return tuple(image[offset:offset + 3])

    assert rgb(4, 28) == (219, 61, 47)
    assert rgb(40, 28) == (45, 96, 207)
    assert rgb(20, 12) == (42, 178, 86)
    assert rgb(5, 0) == (248, 234, 202)


def test_review_brief_requires_only_attachment_scoped_access() -> None:
    b = BRIEF.read_bytes()
    assert b.endswith(b"\n") and b"\r" not in b
    text = b.decode("utf-8")
    for marker in (
        "RAW_BYTES_UNVERIFIED", "TEXT_AND_PNG_BYTES_AND_RENDER_VERIFIED",
        "PARTIAL_CAPABILITY_OBSERVED", "INPUT_HOLD",
        "does *not* prove raw-byte parity",
        "No source admission",
        "HISTORICAL_SOURCES_DELIVERED=ZERO",
    ):
        assert marker.lower() in text.lower()


def test_mixed_file_test_is_not_private_report_transport_or_source_admission() -> None:
    text = BRIEF.read_text(encoding="utf-8")
    assert "RESTRICTED_REPORT_ROUTE=NOT_TESTED_IN_THIS_PROBE" in text
    assert "AUTHOR_VIEW_DENIAL=NOT_TESTED_IN_THIS_PROBE" in text
    assert "REAL_REVIEWER_ROLE=PENDING" in text
    assert "REAL_CHALLENGER_ROLE=PENDING" in text
    assert "GOLD=NONE" in text
    assert "SCORING=NOT_STARTED" in text


def test_scoped_git_attributes_preserve_cross_platform_fixture_bytes() -> None:
    attributes = (ROOT / ".gitattributes").read_text(encoding="utf-8")
    assert "experiments/r0_p03_navigation_probe/a2_source_free_fidelity_unicode_crlf.txt -text whitespace=cr-at-eol" in attributes
    assert "experiments/r0_p03_navigation_probe/a2_source_free_fidelity_pattern.png binary" in attributes
