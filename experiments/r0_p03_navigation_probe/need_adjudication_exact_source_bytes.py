"""Owner-side exact historical source capsule for an existing non-arm adjudicator.

A separate independent adjudicator identifies original pinned source paths
that were actually inspected in its owner-private assessment. The human owner
downloads that small private request JSON and runs the export under ordinary
Windows PowerShell. This module validates each requested path against the
unchanged task-neutral, risk-screened source index, reconstructs original
bytes directly from pinned local Git objects, authenticates length/SHA-256/
Git blob SHA-1, and packs the requested originals.

The exposed coordinating agent must NEVER pass a real question-specific
request through the Runtime Bridge, open the request, run this module against
it, or receive the original output capsule or source-specific receipt.
This creates NO answer key, task admission, source admission, or scored run.
"""
from __future__ import annotations

import argparse
from hashlib import sha1, sha256
from io import BytesIO
import json
from pathlib import Path
import re
import subprocess
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from experiments.r0_p03_navigation_probe import (
    primary_need_adjudication_discovery_packet as discovery,
    source_world_coverage_gate as world,
)

REQUEST_FORMAT = "ads-r0-p03-independent-reviewed-source-byte-request-v1"
CAPSULE_NAME = "NEED_SOURCE_EXACT_ORIGINAL_BYTES_RESTRICTED.zip"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)
MAX_REQUEST_BYTES = 28_000
MAX_SOURCES = 64
MAX_SINGLE_SOURCE_BYTES = 3_000_000
MAX_TOTAL_SOURCE_BYTES = 22_000_000
MAX_OUTPUT_ZIP_BYTES = 24_000_000
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
HEX40 = re.compile(r"[0-9a-f]{40}\Z")


def canonical(obj: object) -> bytes:
    return (json.dumps(obj, sort_keys=True, ensure_ascii=True,
                       separators=(",", ":"), allow_nan=False) + "\n").encode("ascii")


def unique_pairs(pairs: list[tuple[str, object]]) -> dict:
    output: dict = {}
    for key, value in pairs:
        if key in output:
            raise ValueError("DUPLICATE_REQUEST_KEY")
        output[key] = value
    return output


def parse_request(raw: bytes) -> tuple[str, ...]:
    if not isinstance(raw, bytes) or not 25 <= len(raw) <= MAX_REQUEST_BYTES:
        raise ValueError("REQUEST_BYTES_INVALID")
    try:
        request = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_pairs)
    except (ValueError, UnicodeError) as exc:
        raise ValueError("REQUEST_NOT_STRICT_JSON") from exc
    if (not isinstance(request, dict)
            or set(request) != {"format", "source_ref", "paths"}
            or request["format"] != REQUEST_FORMAT
            or request["source_ref"] != world.PIN
            or not isinstance(request["paths"], list)
            or not 1 <= len(request["paths"]) <= MAX_SOURCES):
        raise ValueError("REQUEST_FIELDS_OR_COUNT_INVALID")
    paths = request["paths"]
    if (any(not isinstance(p, str) or not world.safe_path(p) for p in paths)
            or len(set(paths)) != len(paths)
            or paths != sorted(paths)):
        raise ValueError("REQUEST_PATHS_NOT_SORTED_UNIQUE_SAFE")
    return tuple(paths)


def git_bytes(repo: Path, path: str) -> bytes:
    try:
        return subprocess.run(
            ["git", "--no-pager", "show", f"{world.PIN}:{path}"],
            cwd=repo, check=True, capture_output=True,
            timeout=20,
        ).stdout
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        raise ValueError("PINNED_GIT_OBJECT_UNAVAILABLE") from exc


def git_blob(raw: bytes) -> str:
    return sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()


def exact_capsule(repo: Path, request_raw: bytes) -> tuple[bytes, dict]:
    """Never read questions or report paths to stdout; exact source bytes only."""
    repo = repo.resolve(strict=True)
    if not (repo / ".git").is_dir():
        raise ValueError("NOT_A_SOURCE_REPOSITORY")
    paths = parse_request(request_raw)
    ledger, _ = world.compute(repo)
    index = {r["path"]: r for r in discovery.indexed(ledger)}
    if any(path not in index for path in paths):
        raise ValueError("REQUESTED_SOURCE_NOT_IN_APPROVED_DISCOVERY_INDEX")
    items = []
    total = 0
    source_members: dict[str, bytes] = {}
    for path in paths:
        expected = index[path]
        raw = git_bytes(repo, path)
        if (len(raw) != expected["bytes"]
                or len(raw) > MAX_SINGLE_SOURCE_BYTES
                or sha256(raw).hexdigest() != expected["sha256"]
                or git_blob(raw) != expected["git_blob_oid"]
                or not HEX64.fullmatch(expected["sha256"])
                or not HEX40.fullmatch(expected["git_blob_oid"])):
            raise ValueError("PINNED_SOURCE_CONTENT_IDENTITY_FAILURE")
        try:
            raw.decode("utf-8")
        except UnicodeError as exc:
            raise ValueError("ORIGINAL_SOURCE_NOT_UTF8_TEXT") from exc
        total += len(raw)
        if total > MAX_TOTAL_SOURCE_BYTES:
            raise ValueError("TOTAL_ORIGINAL_SOURCE_BYTES_EXCEEDED")
        member = "originals/" + path
        source_members[member] = raw
        items.append({
            "archive_member": member,
            "historical_pin": world.PIN,
            "source_path": path,
            "sha256": expected["sha256"],
            "git_blob_oid": expected["git_blob_oid"],
            "bytes": expected["bytes"],
            "source_admission": "NO_NOT_ADMITTED_PRIVATE_REVIEW_EVIDENCE",
        })
    manifest = {
        "format": "ads-r0-p03-exact-reviewed-original-source-capsule-v1",
        "historical_pin": world.PIN,
        "original_file_count": len(items),
        "total_original_bytes": total,
        "requested_path_set_sha256": sha256(canonical(list(paths))).hexdigest(),
        "scope": "PRIVATE_INDEPENDENT_ADJUDICATOR_SOURCE_BYTE_VERIFICATION_ONLY",
        "source_admissions": 0,
        "answer_keys": "NONE",
        "scored_tasks": 0,
        "records": items,
    }
    members = {"SOURCE_MANIFEST.json": canonical(manifest), **source_members}
    output = BytesIO()
    with ZipFile(output, "w") as z:
        for member in sorted(members):
            raw = members[member]
            info = ZipInfo(member, date_time=FIXED_TIME)
            info.compress_type = ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            z.writestr(info, raw)
    capsule = output.getvalue()
    if len(capsule) > MAX_OUTPUT_ZIP_BYTES:
        raise ValueError("SOURCE_CAPSULE_TOO_LARGE")
    # Independently verify the bytes actually written into the ZIP, not just
    # the in-memory objects before compression.
    with ZipFile(BytesIO(capsule)) as z:
        if z.testzip() is not None or set(z.namelist()) != set(members):
            raise ValueError("SOURCE_CAPSULE_ARCHIVE_ROSTER_OR_CRC_FAILURE")
        for name, raw in members.items():
            if z.read(name) != raw:
                raise ValueError("SOURCE_CAPSULE_EXACT_MEMBER_READBACK_FAILED")
    safe_receipt = {
        "archive_filename": CAPSULE_NAME,
        "archive_bytes": len(capsule),
        "archive_sha256": sha256(capsule).hexdigest(),
        "original_file_count": len(items),
        "total_original_bytes": total,
        "reviewer_request_path_set_digest": manifest["requested_path_set_sha256"],
        "origin": world.PIN,
        "source_content_verified_locally": len(items),
        "source_admissions": 0,
        "protected_task_wording_accessed": False,
        "owner_transfer_to_independent_reviewer": "NOT_AUTOMATIC",
    }
    return capsule, safe_receipt


def safe_private_request_path(repo: Path, candidate: Path) -> Path:
    candidate = candidate.resolve(strict=True)
    if not candidate.is_file() or candidate.is_symlink():
        raise ValueError("REQUEST_MUST_BE_REGULAR_FILE")
    if candidate.is_relative_to(repo.resolve(strict=True)):
        raise ValueError("RESTRICTED_SOURCE_REQUEST_IN_PUBLIC_REPO")
    return candidate


def export_owner(repo: Path, request_file: Path, owner_folder: Path) -> dict:
    """Run ONLY from owner's ordinary PowerShell, not model/Bridge execution."""
    repo = repo.resolve(strict=True)
    source = safe_private_request_path(repo, request_file)
    destination = owner_folder.resolve(strict=True)
    if not destination.is_dir() or destination.is_symlink():
        raise ValueError("OWNER_DESTINATION_NOT_REGULAR_DIRECTORY")
    if destination.is_relative_to(repo):
        raise ValueError("PRIVATE_SOURCE_CAPSULE_DESTINATION_IN_PUBLIC_REPO")
    if not destination.name.startswith("ADS-P03-REVIEWED-SOURCE-BYTES-"):
        raise ValueError("UNEXPECTED_OWNER_PRIVATE_DESTINATION")
    archive, receipt = exact_capsule(repo, source.read_bytes())
    output = destination / CAPSULE_NAME
    if output.exists() or output.is_symlink():
        raise FileExistsError("EXACT_OWNER_SOURCE_CAPSULE_EXISTS")
    with output.open("xb") as file:
        file.write(archive)
        file.flush()
    if output.read_bytes() != archive:
        raise ValueError("OWNER_SOURCE_CAPSULE_READBACK_FAILURE")
    # The receipt includes no paths, questions or relevance labels.
    print("OWNER_SOURCE_EXACT_ORIGINAL_BYTES_EXPORT=PASS")
    print("OWNER_SOURCE_EXACT_ORIGINAL_BYTES_COUNT=" + str(receipt["original_file_count"]))
    print("OWNER_SOURCE_EXACT_ORIGINAL_BYTES_ZIP_BYTES=" + str(receipt["archive_bytes"]))
    print("OWNER_SOURCE_EXACT_ORIGINAL_BYTES_ZIP_SHA256=" + receipt["archive_sha256"])
    return receipt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path)
    parser.add_argument("--request", required=True, type=Path)
    parser.add_argument("--owner-destination", required=True, type=Path)
    args = parser.parse_args()
    export_owner(args.repo, args.request, args.owner_destination)
