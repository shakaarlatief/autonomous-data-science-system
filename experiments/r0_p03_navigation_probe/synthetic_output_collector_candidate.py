"""Synthetic-only Claude stream-to-encrypted-archive output-path feasibility.

This candidate is NOT a production gold collector or a secure secret-entry path.
It accepts only a mechanically fixed fake packet schema and a disposable
SYNTHETIC_ONLY password. Actual passwords must never enter process argv.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
SCRATCH_ROOT = ROOT / ".venv"
SEVEN_ZIP = Path(r"C:\Program Files\7-Zip\7z.exe")
MARKER = "SYNTHETIC_R0P03_DEMONSTRATION_ONLY"
PASSWORD_PREFIX = "SYNTHETIC_ONLY_"
ARCHIVE_NAME = "synthetic-packet.7z"
MEMBER_NAME = "synthetic-reference.json"
MAX_STREAM_BYTES = 512 * 1024
MAX_PACKET_BYTES = 128 * 1024
CATEGORIES = (
    "cold_start_current_orientation",
    "cross_plane_discovery",
    "impact_analysis_evolution",
    "exact_source_authority_recovery",
)


class SyntheticOutputError(ValueError):
    """Reject invalid or ambiguous synthetic-only stream/packet evidence."""


def fake_packet() -> dict:
    """Construct imaginary case slots, never ADS sources or benchmark answers."""
    return {
        "marker": MARKER,
        "synthetic_only": True,
        "legacy": [
            {"id": f"legacy-{i:02}", "claim": f"FAKE_LEGACY_{i:02}",
             "source": "SYNTHETIC_SOURCE_ONLY"}
            for i in range(1, 10)
        ],
        "primary": [
            {"id": f"primary-{i:02}", "category": CATEGORIES[(i - 1) // 3],
             "claim": f"FAKE_PRIMARY_{i:02}", "source": "SYNTHETIC_SOURCE_ONLY"}
            for i in range(1, 13)
        ],
    }


def fake_stream() -> bytes:
    """Simulated provider stream; this function never invokes Claude."""
    packet = json.dumps(fake_packet(), separators=(",", ":"), sort_keys=True)
    events = [
        {"type": "system", "subtype": "init", "message": "synthetic startup"},
        {"type": "assistant", "message": {"content": [
            {"type": "text", "text": "SYNTHETIC_NON_FINAL_IGNORED"}]}},
        {"type": "result", "subtype": "success", "is_error": False, "result": packet},
    ]
    return ("\n".join(json.dumps(e, separators=(",", ":")) for e in events)
            + "\n").encode("utf-8")


def _packet_bytes(packet: object) -> bytes:
    if not isinstance(packet, dict) or set(packet) != {
        "marker", "synthetic_only", "legacy", "primary"
    }:
        raise SyntheticOutputError("invalid synthetic packet shape")
    if packet["marker"] != MARKER or packet["synthetic_only"] is not True:
        raise SyntheticOutputError("real/non-synthetic packet is forbidden")
    legacy = packet["legacy"]
    primary = packet["primary"]
    if not isinstance(legacy, list) or len(legacy) != 9:
        raise SyntheticOutputError("nine fake legacy slots required")
    if not isinstance(primary, list) or len(primary) != 12:
        raise SyntheticOutputError("twelve fake primary slots required")
    for i, record in enumerate(legacy, 1):
        expected = {"id": f"legacy-{i:02}", "claim": f"FAKE_LEGACY_{i:02}",
                    "source": "SYNTHETIC_SOURCE_ONLY"}
        if record != expected:
            raise SyntheticOutputError("non-synthetic legacy content refused")
    for i, record in enumerate(primary, 1):
        expected = {"id": f"primary-{i:02}", "category": CATEGORIES[(i - 1) // 3],
                    "claim": f"FAKE_PRIMARY_{i:02}",
                    "source": "SYNTHETIC_SOURCE_ONLY"}
        if record != expected:
            raise SyntheticOutputError("non-synthetic primary content refused")
    data = (json.dumps(packet, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if len(data) > MAX_PACKET_BYTES:
        raise SyntheticOutputError("synthetic packet too large")
    return data


def extract_synthetic_final(stream: bytes) -> bytes:
    """Fail closed on any duplicate, failed, missing or malformed final event.

    A single final result is used. Assistant text/tool results must never be
    promoted to a gold answer. Unknown event types are not reference content.
    """
    if not isinstance(stream, bytes) or len(stream) > MAX_STREAM_BYTES:
        raise SyntheticOutputError("invalid or oversized stream")
    try:
        text = stream.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise SyntheticOutputError("invalid stream encoding") from exc
    results = []
    for line in text.splitlines():
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SyntheticOutputError("malformed stream event") from exc
        if not isinstance(event, dict) or not isinstance(event.get("type"), str):
            raise SyntheticOutputError("malformed stream event structure")
        if event["type"] == "result":
            results.append(event)
    if len(results) != 1:
        raise SyntheticOutputError("exactly one final result event required")
    result = results[0]
    if result.get("is_error") is not False or result.get("subtype") != "success":
        raise SyntheticOutputError("non-successful final result")
    raw = result.get("result")
    if not isinstance(raw, str):
        raise SyntheticOutputError("nontext final result")
    try:
        return _packet_bytes(json.loads(raw))
    except json.JSONDecodeError as exc:
        raise SyntheticOutputError("invalid final packet JSON") from exc


def _scratch_path(archive: Path) -> None:
    """Constrain synthetic output to disposable scratch, never a real gold path."""
    scratch = SCRATCH_ROOT.resolve(strict=True)
    if (not archive.is_absolute() or archive.name != ARCHIVE_NAME
            or not archive.parent.name.startswith(".r0p03-")):
        raise SyntheticOutputError("non-scratch synthetic archive path")
    if (not archive.parent.resolve(strict=True).is_relative_to(scratch)
            or archive.parent.is_symlink()):
        raise SyntheticOutputError("archive outside local synthetic scratch")
    if archive.exists() or archive.is_symlink():
        raise SyntheticOutputError("refuse to overwrite existing archive")


def seal_synthetic_final(stream: bytes, archive: Path, password: str) -> dict:
    """Encrypt in-memory fake final bytes directly via 7z stdin, no plaintext file.

    The disposable password is deliberately a subprocess argument for this
    synthetic-only mechanism check. This MUST NOT handle real secrets/answers.
    """
    payload = extract_synthetic_final(stream)
    if not isinstance(password, str) or not re.fullmatch(
        r"SYNTHETIC_ONLY_[0-9a-f]{32,64}", password
    ):
        raise SyntheticOutputError("real passwords not accepted")
    _scratch_path(archive)
    if not SEVEN_ZIP.is_file():
        raise SyntheticOutputError("installed 7-Zip not available")
    args = [str(SEVEN_ZIP), "a", "-t7z", "-mhe=on", "-mx=0",
            "-p" + password, str(archive), "-si" + MEMBER_NAME]
    result = subprocess.run(args, input=payload, capture_output=True, timeout=25)
    if result.returncode != 0 or not archive.is_file():
        archive.unlink(missing_ok=True)
        raise SyntheticOutputError("synthetic 7z seal failed")
    ciphertext = archive.read_bytes()
    if payload in ciphertext:
        archive.unlink(missing_ok=True)
        raise SyntheticOutputError("plaintext visible in archive bytes")
    return {
        "synthetic_only": True,
        "case_slots": {"legacy": 9, "primary": 12},
        "source_sha256": hashlib.sha256(payload).hexdigest(),
        "archive_sha256": hashlib.sha256(ciphertext).hexdigest(),
        "archive_bytes": len(ciphertext),
        "plaintext_file_written_by_collector": False,
        "real_output_custody_qualified": False,
    }


def verify_synthetic_seal(archive: Path, password: str, expected_sha256: str) -> bool:
    """Mechanical synthetic recovery check; never prints decrypted packet bytes."""
    if not re.fullmatch(r"SYNTHETIC_ONLY_[0-9a-f]{32,64}", password):
        raise SyntheticOutputError("real passwords not accepted")
    recovery = subprocess.run(
        [str(SEVEN_ZIP), "e", "-so", "-p" + password, str(archive), MEMBER_NAME],
        capture_output=True, timeout=25,
    )
    return (recovery.returncode == 0
            and hashlib.sha256(recovery.stdout).hexdigest() == expected_sha256)


def run_demo() -> dict:
    """No networking, Claude call, real answers, persistent archive or key."""
    import secrets
    with tempfile.TemporaryDirectory(prefix=".r0p03-collector-", dir=SCRATCH_ROOT) as d:
        archive = Path(d) / ARCHIVE_NAME
        password = PASSWORD_PREFIX + secrets.token_hex(20)
        receipt = seal_synthetic_final(fake_stream(), archive, password)
        receipt["exact_recovery_after_subprocess"] = verify_synthetic_seal(
            archive, password, receipt["source_sha256"]
        )
        bad = PASSWORD_PREFIX + ("0" * 40)
        if bad == password:
            bad = PASSWORD_PREFIX + ("f" * 40)
        receipt["wrong_password_rejected"] = not verify_synthetic_seal(
            archive, bad, receipt["source_sha256"]
        )
        receipt["not_for_real_gold"] = True
        return receipt


if __name__ == "__main__":
    print(json.dumps(run_demo(), sort_keys=True))
