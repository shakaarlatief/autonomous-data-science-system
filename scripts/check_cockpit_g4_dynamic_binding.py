#!/usr/bin/env python3
"""Validate the supplemental exact-source binding for the accepted G4 scheduler.

The primary Cockpit implementation manifest currently models one integration
SHA per manifest entry. M02 requires both a later SEL2-compatible WorkUnit
substrate and an earlier, independently refined stochastic G4 scheduler.
Until the primary manifest schema supports multiple ordered source groups, the
scheduler is represented by a machine-readable supplement and verified here.

This validator deliberately checks both repository history and the active
working-tree copy. A future integrator therefore cannot silently replace the
accepted stochastic scheduler with a fixed authored ambient fixture while the
provenance gate remains green.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUPPLEMENT = ROOT / "docs" / "cockpit" / "g4_dynamic_source_binding_supplement.json"


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT)


def git_object_exists(spec: str) -> bool:
    completed = subprocess.run(
        ["git", "cat-file", "-e", spec],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return completed.returncode == 0


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def fail(message: str) -> None:
    print(f"G4 dynamic source binding: FAIL\n{message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    payload = json.loads(SUPPLEMENT.read_text(encoding="utf-8"))

    if payload.get("supplements_entry") != "M02":
        fail("supplement must extend M02")
    if payload.get("maturity") != "MUST_PORT":
        fail("supplemented G4 scheduler must remain MUST_PORT")

    integration_sha = payload.get("integration_source_sha")
    if not isinstance(integration_sha, str) or len(integration_sha) != 40:
        fail("integration_source_sha must be a full 40-character commit SHA")
    if not git_object_exists(f"{integration_sha}^{{commit}}"):
        fail(f"historical commit does not resolve: {integration_sha}")

    files = payload.get("source_files")
    if not isinstance(files, list) or len(files) < 3:
        fail("expected the exact combined HTML/CSS/JS source group")

    expected_paths = {
        "frontend/design-lab/grid-dynamics-combined.html",
        "frontend/design-lab/grid-dynamics-combined.css",
        "frontend/design-lab/grid-dynamics-combined.js",
    }
    actual_paths = {item.get("path") for item in files if isinstance(item, dict)}
    if actual_paths != expected_paths:
        fail(f"unexpected G4 source path set: {sorted(actual_paths)}")

    verified = 0
    for item in files:
        path = item["path"]
        expected_blob = item.get("blob_sha")
        if not isinstance(expected_blob, str) or len(expected_blob) != 40:
            fail(f"invalid blob SHA for {path}")

        historical_spec = f"{integration_sha}:{path}"
        if not git_object_exists(historical_spec):
            fail(f"historical source does not resolve: {historical_spec}")

        historical = git("show", historical_spec)
        historical_blob = git_blob_sha(historical)
        if historical_blob != expected_blob:
            fail(
                f"historical blob mismatch for {path}: "
                f"expected {expected_blob}, observed {historical_blob}"
            )

        current_path = ROOT / path
        if not current_path.is_file():
            fail(f"current branch source is absent: {path}")
        current_blob = git_blob_sha(current_path.read_bytes())
        if current_blob != expected_blob:
            fail(
                f"current branch diverges from accepted G4 source for {path}: "
                f"expected {expected_blob}, observed {current_blob}"
            )

        verified += 1

    invariant_text = "\n".join(payload.get("invariants", []))
    required_terms = (
        "Lively",
        "20px",
        "100px",
        "independent quiet scheduler",
        "at most two glints",
        "ambient drift",
        "localized semantic activity",
        "reduced motion",
    )
    missing = [term for term in required_terms if term not in invariant_text]
    if missing:
        fail(f"supplement is missing required invariant terms: {missing}")

    print(
        "G4 dynamic source binding: PASS\n"
        f"entry=M02 source_group={integration_sha} files={verified} "
        "current_branch_exact=true"
    )


if __name__ == "__main__":
    main()
