"""Standalone TEMPORARY-CHAT sender for one fictional-only R0-P03 handoff.

This file contains NO real source questions, answer keys, owner secrets, private
key, experiment conditions, Git paths, or hidden-gold operations. It may be
given to a new Temporary Chat together with only a public PEM certificate.

Requires local Python 3.10+ and an existing OpenSSL executable supporting
CMS AES-256-GCM. If unavailable, fail closed; never substitute cleartext,
password-in-chat, public Git, or an unauthenticated envelope format.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

MARKER = "SYNTHETIC_R0P03_DEMONSTRATION_ONLY"
FILENAME = "R0_P03_FAKE_AUTHOR_PACKET.cms"
CATEGORIES = (
    "cold_start_current_orientation",
    "cross_plane_discovery",
    "impact_analysis_evolution",
    "exact_source_authority_recovery",
)


def fictional_payload() -> bytes:
    """Construct exactly 21 overtly fabricated fixed references in memory."""
    packet = {
        "marker": MARKER,
        "synthetic_only": True,
        "legacy": [
            {"id": f"legacy-{i:02}", "claim": f"FAKE_LEGACY_{i:02}",
             "source": "SYNTHETIC_SOURCE_ONLY"}
            for i in range(1, 10)
        ],
        "primary": [
            {"id": f"primary-{i:02}", "category": CATEGORIES[(i - 1) // 3],
             "claim": f"FAKE_PRIMARY_{i:02}",
             "source": "SYNTHETIC_SOURCE_ONLY"}
            for i in range(1, 13)
        ],
    }
    return (json.dumps(packet, separators=(",", ":"), sort_keys=True) + "\n").encode("utf-8")


def sender(cert: Path, output: Path) -> dict[str, object]:
    """Validate a public certificate; seal in memory and emit only ciphertext.

    Do not serialize the invented plaintext, re-read private keys or transmit
    any model transcript. Refuse existing output and any different filename.
    """
    if output.name != FILENAME or not output.parent.is_dir():
        raise ValueError("Expected exact CMS output filename in an existing directory")
    if not cert.is_file() or cert.is_symlink() or not 0 < cert.stat().st_size < 65536:
        raise ValueError("Public certificate file absent or invalid")
    pem = cert.read_bytes()
    if b"BEGIN CERTIFICATE" not in pem or b"PRIVATE KEY" in pem:
        raise ValueError("Only a public PEM certificate is allowed")
    executable = shutil.which("openssl")
    if executable is None:
        raise RuntimeError("OpenSSL unavailable: stop rather than changing encryption format")
    checked = subprocess.run(
        [executable, "x509", "-in", str(cert), "-noout", "-fingerprint", "-sha256"],
        capture_output=True, timeout=20, check=False,
    )
    if checked.returncode != 0:
        raise RuntimeError("Public certificate parse failed")
    fake = fictional_payload()
    encrypted = subprocess.run(
        [executable, "cms", "-encrypt", "-binary", "-outform", "DER",
         "-aes-256-gcm", "-recip", str(cert)],
        input=fake, capture_output=True, timeout=25, check=False,
    )
    if encrypted.returncode != 0 or len(encrypted.stdout) < 100:
        raise RuntimeError("CMS authenticated encryption failed")
    if fake in encrypted.stdout:
        raise RuntimeError("Cleartext visible in ciphertext output")
    with output.open("xb") as handle:
        handle.write(encrypted.stdout)
        handle.flush()
    return {
        "synthetic_only": True,
        "real_reference_answers": False,
        "ciphertext_file": output.name,
        "ciphertext_sha256": hashlib.sha256(encrypted.stdout).hexdigest(),
        "ciphertext_bytes": len(encrypted.stdout),
        "fake_legacy_slots": 9,
        "fake_primary_slots": 12,
        "plaintext_packet_file_written": False,
        "private_key_available_to_sender": False,
        "custody_qualified": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cert", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(sender(args.cert, args.output), sort_keys=True))
