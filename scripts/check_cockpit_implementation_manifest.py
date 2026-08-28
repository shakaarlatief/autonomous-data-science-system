"""Validate the Project Cockpit implementation-provenance manifest.

The validator is intentionally deterministic. It does not judge visual quality.
Its job is to prevent a future integrator from silently dropping required
Phase-C mechanisms, promoting provisional/deferred work, using malformed source
identities, or treating the failed holistic browser as an accepted source.

Run from the repository root:

    python scripts/check_cockpit_implementation_manifest.py

For a repository checkout that contains the relevant historical Git objects,
add exact historical source verification:

    python scripts/check_cockpit_implementation_manifest.py --verify-git-history

The historical mode checks that every declared source file exists at the exact
integration source commit. It also reports whether the current branch copy of
each source path is byte-identical to the declared historical source. Current
branch divergence is reported rather than rejected because a later compatible
refinement may legitimately exist; the report tells an integrator which files
may be imported directly from HEAD and which require deliberate historical
porting or a separately justified newer source binding.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "docs" / "cockpit" / "accepted_implementation_manifest.json"
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
ENTRY_ID_RE = re.compile(r"^M\d{2}$")

REQUIRED_IDS = {f"M{index:02d}" for index in range(1, 24)}
ALLOWED_MATURITIES = {
    "MUST_PRESERVE",
    "MUST_PORT",
    "PROVISIONAL_ONLY",
    "DO_NOT_SELECT_DURING_INTEGRATION",
    "EXCLUDED_SOURCE",
}
REQUIRED_MATURITIES = {"MUST_PRESERVE", "MUST_PORT"}
NON_PROMOTABLE_MATURITIES = {
    "PROVISIONAL_ONLY",
    "DO_NOT_SELECT_DURING_INTEGRATION",
    "EXCLUDED_SOURCE",
}
FAILED_INTEGRATION_SHA = "8e554d847bb3b6318db432abcb5dff742f0fa523"
FAILED_SOURCE_PREFIX = "frontend/design-lab/cockpit-integrated-baseline"


class ManifestError(Exception):
    """Raised when a deterministic manifest invariant is violated."""


def load_manifest() -> dict[str, Any]:
    try:
        data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ManifestError(f"Manifest missing: {MANIFEST_PATH}") from exc
    except json.JSONDecodeError as exc:
        raise ManifestError(f"Manifest is not valid JSON: {exc}") from exc

    if not isinstance(data, dict):
        raise ManifestError("Manifest root must be a JSON object")
    return data


def require_non_empty_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ManifestError(f"{label} must be a non-empty string")
    return value


def require_string_list(value: Any, label: str, *, allow_empty: bool = False) -> list[str]:
    if not isinstance(value, list):
        raise ManifestError(f"{label} must be a list")
    if not allow_empty and not value:
        raise ManifestError(f"{label} must not be empty")
    if any(not isinstance(item, str) or not item.strip() for item in value):
        raise ManifestError(f"{label} must contain only non-empty strings")
    return value


def validate_sha(value: Any, label: str, *, allow_null: bool = False) -> str | None:
    if value is None and allow_null:
        return None
    if not isinstance(value, str) or not SHA_RE.fullmatch(value):
        raise ManifestError(f"{label} must be a lowercase 40-character Git SHA")
    return value


def validate_manifest(data: dict[str, Any]) -> list[dict[str, Any]]:
    if data.get("schema_version") != 1:
        raise ManifestError("schema_version must equal 1")

    if data.get("failed_integration_sha") != FAILED_INTEGRATION_SHA:
        raise ManifestError("failed_integration_sha must remain the frozen failed target")

    declared_required = set(require_string_list(data.get("required_maturities"), "required_maturities"))
    if declared_required != REQUIRED_MATURITIES:
        raise ManifestError(
            f"required_maturities must be exactly {sorted(REQUIRED_MATURITIES)}"
        )

    declared_non_promotable = set(
        require_string_list(data.get("non_promotable_maturities"), "non_promotable_maturities")
    )
    if declared_non_promotable != NON_PROMOTABLE_MATURITIES:
        raise ManifestError(
            "non_promotable_maturities must preserve the provisional/deferred/excluded boundary"
        )

    entries = data.get("entries")
    if not isinstance(entries, list):
        raise ManifestError("entries must be a list")

    ids: list[str] = []
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            raise ManifestError(f"entries[{index}] must be an object")

        entry_id = require_non_empty_string(entry.get("id"), f"entries[{index}].id")
        if not ENTRY_ID_RE.fullmatch(entry_id):
            raise ManifestError(f"{entry_id}: id must match MNN")
        ids.append(entry_id)

        require_non_empty_string(entry.get("name"), f"{entry_id}.name")
        maturity = require_non_empty_string(entry.get("maturity"), f"{entry_id}.maturity")
        if maturity not in ALLOWED_MATURITIES:
            raise ManifestError(f"{entry_id}: unsupported maturity {maturity!r}")

        require_string_list(entry.get("decision_sources"), f"{entry_id}.decision_sources")
        validate_sha(
            entry.get("decision_target_sha"),
            f"{entry_id}.decision_target_sha",
            allow_null=(entry_id == "M02"),
        )

        integration_sha = validate_sha(
            entry.get("integration_source_sha"),
            f"{entry_id}.integration_source_sha",
            allow_null=(maturity == "EXCLUDED_SOURCE"),
        )
        source_files = require_string_list(entry.get("source_files"), f"{entry_id}.source_files")
        require_string_list(entry.get("invariants"), f"{entry_id}.invariants")
        require_string_list(
            entry.get("allowed_adaptations"),
            f"{entry_id}.allowed_adaptations",
            allow_empty=True,
        )
        require_string_list(entry.get("fixture_caveats"), f"{entry_id}.fixture_caveats")
        require_string_list(entry.get("verification"), f"{entry_id}.verification")

        for source_file in source_files:
            if source_file.startswith("/") or ".." in Path(source_file).parts:
                raise ManifestError(f"{entry_id}: unsafe/non-repository source path {source_file!r}")

        if maturity in REQUIRED_MATURITIES:
            if integration_sha is None:
                raise ManifestError(f"{entry_id}: required item has no integration source SHA")
            if any(path.startswith(FAILED_SOURCE_PREFIX) for path in source_files):
                raise ManifestError(f"{entry_id}: required item references failed integration source")
            if integration_sha == FAILED_INTEGRATION_SHA:
                raise ManifestError(f"{entry_id}: required item uses failed integration SHA")

        if maturity == "EXCLUDED_SOURCE":
            if entry_id != "M23":
                raise ManifestError(f"{entry_id}: only M23 may be the frozen excluded-source guard")
            if integration_sha is not None:
                raise ManifestError("M23: excluded source must not have an integration_source_sha")
            if entry.get("decision_target_sha") != FAILED_INTEGRATION_SHA:
                raise ManifestError("M23: excluded source must point to the failed target SHA")
            if not all(path.startswith(FAILED_SOURCE_PREFIX) for path in source_files):
                raise ManifestError("M23: excluded source paths must be the failed baseline family")

    if len(ids) != len(set(ids)):
        duplicates = sorted({entry_id for entry_id in ids if ids.count(entry_id) > 1})
        raise ManifestError(f"duplicate manifest ids: {duplicates}")

    missing = sorted(REQUIRED_IDS - set(ids))
    extra = sorted(set(ids) - REQUIRED_IDS)
    if missing or extra:
        raise ManifestError(f"manifest id coverage mismatch; missing={missing}, extra={extra}")

    return entries


def verify_current_paths(entries: list[dict[str, Any]]) -> list[str]:
    """Return warnings for historical source paths absent from the current checkout.

    Historical exact-target verification is authoritative when requested. Current
    path presence is reported as a warning because an accepted historical source
    may legitimately no longer exist at HEAD.
    """

    warnings: list[str] = []
    for entry in entries:
        if entry["maturity"] == "EXCLUDED_SOURCE":
            continue
        for relative in entry["source_files"]:
            if not (ROOT / relative).exists():
                warnings.append(f"{entry['id']}: current checkout does not contain {relative}")
    return warnings


def run_git(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        check=False,
    )


def git_object_exists(spec: str) -> bool:
    result = subprocess.run(
        ["git", "cat-file", "-e", spec],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0


def git_object_sha(spec: str) -> str | None:
    result = run_git("rev-parse", "--verify", spec)
    if result.returncode != 0:
        return None
    value = result.stdout.strip()
    return value if SHA_RE.fullmatch(value) else None


def verify_git_history(entries: list[dict[str, Any]]) -> None:
    for entry in entries:
        integration_sha = entry["integration_source_sha"]
        if integration_sha is None:
            continue

        if not git_object_exists(f"{integration_sha}^{{commit}}"):
            raise ManifestError(
                f"{entry['id']}: historical commit {integration_sha} is unavailable. "
                "Fetch repository history or omit --verify-git-history in a shallow checkout."
            )

        for source_file in entry["source_files"]:
            if not git_object_exists(f"{integration_sha}:{source_file}"):
                raise ManifestError(
                    f"{entry['id']}: {source_file} does not exist at exact source {integration_sha}"
                )


def compare_current_source_blobs(entries: list[dict[str, Any]]) -> dict[str, list[str]]:
    """Classify current branch source paths against each exact historical binding.

    The comparison is informational. A current path that differs from the
    historical source is not automatically wrong because later compatible
    refinements may exist. It does mean the integrator must not assume that
    importing the current path is equivalent to porting the manifest source.
    """

    result: dict[str, list[str]] = {
        "exact_current": [],
        "diverged_current": [],
        "absent_current": [],
    }

    for entry in entries:
        integration_sha = entry["integration_source_sha"]
        if integration_sha is None:
            continue

        for source_file in entry["source_files"]:
            historical_blob = git_object_sha(f"{integration_sha}:{source_file}")
            current_blob = git_object_sha(f"HEAD:{source_file}")
            label = f"{entry['id']} {source_file}"

            if current_blob is None:
                result["absent_current"].append(label)
            elif current_blob == historical_blob:
                result["exact_current"].append(label)
            else:
                result["diverged_current"].append(
                    f"{label} historical={historical_blob} current={current_blob}"
                )

    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--verify-git-history",
        action="store_true",
        help="verify every declared source path at its exact historical integration source SHA",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        data = load_manifest()
        entries = validate_manifest(data)
        current_path_warnings = verify_current_paths(entries)
        current_compatibility: dict[str, list[str]] | None = None
        if args.verify_git_history:
            verify_git_history(entries)
            current_compatibility = compare_current_source_blobs(entries)
    except ManifestError as exc:
        print(f"Cockpit implementation manifest: FAIL\n{exc}", file=sys.stderr)
        return 1

    print(
        "Cockpit implementation manifest: PASS\n"
        f"entries={len(entries)} required={sum(e['maturity'] in REQUIRED_MATURITIES for e in entries)} "
        f"non_promotable={sum(e['maturity'] in NON_PROMOTABLE_MATURITIES for e in entries)}"
    )
    if args.verify_git_history:
        print("exact historical source verification: PASS")
    if current_compatibility is not None:
        print(
            "current-source compatibility: "
            f"exact={len(current_compatibility['exact_current'])} "
            f"diverged={len(current_compatibility['diverged_current'])} "
            f"absent={len(current_compatibility['absent_current'])}"
        )
        if current_compatibility["diverged_current"]:
            print("current-source divergences requiring deliberate port/rebinding:")
            for item in current_compatibility["diverged_current"]:
                print(f"  - {item}")
        if current_compatibility["absent_current"]:
            print("historical sources absent from current branch:")
            for item in current_compatibility["absent_current"]:
                print(f"  - {item}")
    if current_path_warnings:
        print("current-checkout path warnings:")
        for warning in current_path_warnings:
            print(f"  - {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
