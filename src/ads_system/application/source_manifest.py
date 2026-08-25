"""Reviewable intake-manifest and comparison helpers for source-universe ingestion."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from ads_system.domain.source_universe import IntakeComparison


def load_intake_manifest(path: str | Path) -> dict[str, Any]:
    manifest = json.loads(Path(path).read_text(encoding="utf-8"))
    if (
        manifest.get("format") != "ADS_SOURCE_INTAKE_MANIFEST"
        or manifest.get("schema_version") != 1
    ):
        raise ValueError("unsupported intake manifest")
    names = [entry["observed_name"] for entry in manifest.get("entries", [])]
    if len(names) != len(set(names)):
        raise ValueError("intake manifest contains duplicate observed_name values")
    for entry in manifest.get("entries", []):
        for name in [entry["observed_name"], *entry.get("local_name_aliases", [])]:
            candidate = Path(name)
            if candidate.is_absolute() or candidate.name != name or name in {"", ".", ".."}:
                raise ValueError(
                    f"manifest filename must be a single relative basename: {name!r}"
                )
    return manifest


def compare_intake_manifest(
    manifest: dict[str, Any], local_root: str | Path
) -> tuple[IntakeComparison, ...]:
    root = Path(local_root)
    entries = list(manifest.get("entries", []))
    actual_names = {path.name for path in root.iterdir() if path.is_file()}
    matched_local_names: set[str] = set()
    results: list[IntakeComparison] = []
    for entry in sorted(entries, key=lambda item: item["observed_name"]):
        name = entry["observed_name"]
        expected_digest = entry.get("expected_sha256")
        expected_size = entry.get("expected_byte_size")
        candidates = [name, *entry.get("local_name_aliases", [])]
        local_name = next(
            (candidate for candidate in candidates if (root / candidate).is_file()), None
        )
        if local_name is None:
            results.append(
                IntakeComparison(
                    name,
                    "MISSING_LOCAL_SOURCE",
                    None,
                    expected_digest,
                    None,
                    expected_size,
                    None,
                )
            )
            continue
        matched_local_names.add(local_name)
        observed_digest, observed_size = _hash(root / local_name)
        status = (
            "MATCH"
            if observed_digest == expected_digest and observed_size == expected_size
            else "DIFFERENT_ARTIFACT"
        )
        results.append(
            IntakeComparison(
                name,
                status,
                local_name,
                expected_digest,
                observed_digest,
                expected_size,
                observed_size,
            )
        )
    for name in sorted(actual_names - matched_local_names):
        observed_digest, observed_size = _hash(root / name)
        results.append(
            IntakeComparison(
                name,
                "ADDITIONAL_LOCAL_SOURCE",
                name,
                None,
                observed_digest,
                None,
                observed_size,
            )
        )
    return tuple(results)


def _hash(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as handle:
        while block := handle.read(1024 * 1024):
            digest.update(block)
            size += len(block)
    return digest.hexdigest(), size


def manifest_ingest_requests(manifest: dict[str, Any], local_root: str | Path):
    """Yield explicit IngestRequest values for locally present manifest entries."""
    from ads_system.application.source_universe import IngestRequest

    root = Path(local_root)
    collection = manifest["collection"]
    for entry in manifest.get("entries", []):
        candidates = [entry["observed_name"], *entry.get("local_name_aliases", [])]
        local_name = next(
            (candidate for candidate in candidates if (root / candidate).is_file()), None
        )
        if local_name is None:
            continue
        path = root / local_name
        yield IngestRequest(
            input_path=path,
            stable_key=entry["stable_key"],
            title=entry["title"],
            source_type=entry["source_type"],
            canonical_locator=entry.get("canonical_locator"),
            external_identifier_type=entry.get("external_identifier_type"),
            external_identifier_value=entry.get("external_identifier_value"),
            access_class=entry.get("access_class", "PRIVATE_USER_SUPPLIED"),
            redistribution_status=entry.get("redistribution_status", "UNKNOWN"),
            rights_note=entry.get("rights_note"),
            metadata_visibility=entry.get("metadata_visibility", "PRIVATE"),
            media_type=entry.get("media_type", "application/pdf"),
            collection_stable_key=collection["stable_key"],
            collection_title=collection["title"],
            collection_type=collection.get("collection_type", "COURSE"),
            collection_canonical_locator=collection.get("canonical_locator"),
            collection_metadata=collection.get("metadata", {}),
            membership_role=entry.get("membership_role", "UNKNOWN"),
            association_status=entry.get("association_status", "UNVERIFIED"),
            membership_note=entry.get("membership_note"),
            observed_name=entry["observed_name"],
        )
