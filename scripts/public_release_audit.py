"""Audit the repository and reachable Git history before public release.

The audit is intentionally conservative and uses only the Python standard
library plus the local Git executable. It checks both the current tracked tree
and all reachable historical blobs so deleting a sensitive file from the latest
commit cannot accidentally make a release appear clean.

The script never prints matched secret values. Findings identify only a rule,
scope, path, and (for historical findings) a short object identifier.

Exit status:
    0: no blocking findings; warnings may still require human review.
    1: at least one blocking finding was detected.
"""

from __future__ import annotations

import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
MAX_SCANNED_BLOB_BYTES = 5 * 1024 * 1024
LARGE_BLOB_WARNING_BYTES = 10 * 1024 * 1024


@dataclass(frozen=True)
class Finding:
    severity: str
    rule: str
    scope: str
    path: str
    detail: str


SECRET_PATTERNS: tuple[tuple[str, re.Pattern[bytes]], ...] = (
    (
        "openai_or_generic_sk_token",
        re.compile(rb"(?<![A-Za-z0-9])sk-(?:proj-|ant-)?[A-Za-z0-9_-]{20,}"),
    ),
    (
        "github_classic_token",
        re.compile(rb"(?<![A-Za-z0-9])gh[pousr]_[A-Za-z0-9]{20,}"),
    ),
    (
        "github_fine_grained_token",
        re.compile(rb"(?<![A-Za-z0-9])github_pat_[A-Za-z0-9_]{20,}"),
    ),
    (
        "aws_access_key_id",
        re.compile(rb"(?<![A-Z0-9])(?:AKIA|ASIA)[A-Z0-9]{16}(?![A-Z0-9])"),
    ),
    (
        "google_api_key",
        re.compile(rb"(?<![A-Za-z0-9])AIza[0-9A-Za-z_-]{35}(?![A-Za-z0-9])"),
    ),
    (
        "slack_token",
        re.compile(rb"(?<![A-Za-z0-9])xox[baprs]-[A-Za-z0-9-]{20,}"),
    ),
    (
        "huggingface_token",
        re.compile(rb"(?<![A-Za-z0-9])hf_[A-Za-z0-9]{30,}"),
    ),
    (
        "stripe_live_secret",
        re.compile(rb"(?<![A-Za-z0-9])sk_live_[A-Za-z0-9]{16,}"),
    ),
    (
        "private_key_material",
        re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ),
)

NAMED_SECRET_ASSIGNMENT = re.compile(
    rb"(?i)\b(?:OPENAI_API_KEY|ANTHROPIC_API_KEY|AZURE_OPENAI_API_KEY|"
    rb"AWS_SECRET_ACCESS_KEY|GITHUB_TOKEN|GITHUB_PAT)\b\s*[:=]\s*"
    rb"[\"']?([A-Za-z0-9_./+=:-]{16,})"
)

PLACEHOLDER_MARKERS = (
    b"example",
    b"placeholder",
    b"dummy",
    b"fake",
    b"test",
    b"your_",
    b"your-",
    b"replace",
    b"changeme",
    b"redacted",
)

LOCAL_PATH_PATTERNS: tuple[tuple[str, re.Pattern[bytes]], ...] = (
    (
        "windows_user_home",
        re.compile(rb"(?i)[A-Z]:\\Users\\[^\\\r\n\"']+"),
    ),
    (
        "unix_user_home",
        re.compile(rb"/(?:Users|home)/[^/\s\"']+"),
    ),
    (
        "projects_data_absolute_path",
        re.compile(rb"(?i)(?:[A-Z]:\\|/[a-z]/)Projects_Data(?:\\|/)"),
    ),
)

SENSITIVE_BASENAMES = {
    ".env",
    "id_rsa",
    "id_dsa",
    "id_ecdsa",
    "id_ed25519",
    "credentials.json",
    "service-account.json",
    "service_account.json",
}

SENSITIVE_SUFFIXES = {".pem", ".p12", ".pfx"}
RUNTIME_SEGMENTS = {"generated", "results"}


def _git_bytes(args: list[str], *, check: bool = True) -> bytes:
    completed = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and completed.returncode != 0:
        stderr = completed.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"git {' '.join(args)} failed: {stderr}")
    return completed.stdout


def _git_text(args: list[str], *, check: bool = True) -> str:
    return _git_bytes(args, check=check).decode("utf-8", errors="replace")


def _normalize_git_path(path: str) -> str:
    return path.replace("\\", "/").strip("/")


def _is_sensitive_path(path: str) -> bool:
    normalized = _normalize_git_path(path)
    name = Path(normalized).name.lower()
    suffix = Path(normalized).suffix.lower()
    if name == ".env.example":
        return False
    if name in SENSITIVE_BASENAMES:
        return True
    if name.startswith(".env."):
        return True
    if suffix in SENSITIVE_SUFFIXES:
        return True
    if suffix == ".key" and "test" not in name and "example" not in name:
        return True
    return False


def _contains_runtime_segment(path: str) -> bool:
    parts = {part.lower() for part in _normalize_git_path(path).split("/")}
    return bool(parts.intersection(RUNTIME_SEGMENTS))


def _current_index() -> tuple[dict[str, str], set[str]]:
    """Return current blob SHA -> path and the set of tracked paths."""

    output = _git_text(["ls-files", "-s"])
    by_sha: dict[str, str] = {}
    paths: set[str] = set()
    for line in output.splitlines():
        if not line.strip():
            continue
        metadata, path = line.split("\t", 1)
        fields = metadata.split()
        if len(fields) < 3:
            continue
        sha = fields[1]
        normalized = _normalize_git_path(path)
        by_sha.setdefault(sha, normalized)
        paths.add(normalized)
    return by_sha, paths


def _historical_object_paths() -> dict[str, set[str]]:
    """Map every reachable object SHA with a named path to all observed paths."""

    mapping: dict[str, set[str]] = {}
    output = _git_text(["rev-list", "--objects", "--all"])
    for line in output.splitlines():
        if not line.strip():
            continue
        sha, separator, path = line.partition(" ")
        if not separator or not path:
            continue
        mapping.setdefault(sha, set()).add(_normalize_git_path(path))
    return mapping


def _all_historical_paths() -> set[str]:
    output = _git_text(["log", "--all", "--name-only", "--pretty=format:"])
    return {
        _normalize_git_path(line)
        for line in output.splitlines()
        if line.strip()
    }


def _object_type(sha: str) -> str:
    return _git_text(["cat-file", "-t", sha]).strip()


def _object_size(sha: str) -> int:
    return int(_git_text(["cat-file", "-s", sha]).strip())


def _blob_bytes(sha: str) -> bytes:
    return _git_bytes(["cat-file", "blob", sha])


def _secret_assignment_is_placeholder(match: re.Match[bytes]) -> bool:
    value = match.group(1).lower()
    return any(marker in value for marker in PLACEHOLDER_MARKERS)


def _scan_blob(
    *,
    sha: str,
    data: bytes,
    paths: Iterable[str],
    current_shas: set[str],
) -> list[Finding]:
    findings: list[Finding] = []
    scope = "current" if sha in current_shas else "history"
    path_list = sorted(set(paths))
    path_label = ", ".join(path_list[:3])
    if len(path_list) > 3:
        path_label += f" (+{len(path_list) - 3} more paths)"

    if b"\x00" in data:
        return findings

    for rule, pattern in SECRET_PATTERNS:
        if pattern.search(data):
            findings.append(
                Finding(
                    severity="FAIL",
                    rule=rule,
                    scope=scope,
                    path=path_label,
                    detail=f"secret-like material found in blob {sha[:12]}",
                )
            )

    for match in NAMED_SECRET_ASSIGNMENT.finditer(data):
        if _secret_assignment_is_placeholder(match):
            continue
        findings.append(
            Finding(
                severity="FAIL",
                rule="named_secret_assignment",
                scope=scope,
                path=path_label,
                detail=f"credential-like assignment found in blob {sha[:12]}",
            )
        )
        break

    for rule, pattern in LOCAL_PATH_PATTERNS:
        if pattern.search(data):
            findings.append(
                Finding(
                    severity="WARN",
                    rule=rule,
                    scope=scope,
                    path=path_label,
                    detail=f"absolute local path found in blob {sha[:12]}",
                )
            )

    return findings


def _mask_email(email: str) -> str:
    local, separator, domain = email.partition("@")
    if not separator:
        return "<invalid-email>"
    visible = local[:1] if local else "?"
    return f"{visible}***@{domain}"


def _commit_email_warnings() -> list[Finding]:
    output = _git_text(["log", "--all", "--format=%ae%n%ce"])
    emails = {
        line.strip()
        for line in output.splitlines()
        if line.strip()
    }
    findings: list[Finding] = []
    for email in sorted(emails):
        lower = email.lower()
        if lower.endswith("@users.noreply.github.com"):
            continue
        findings.append(
            Finding(
                severity="WARN",
                rule="commit_email_visibility",
                scope="history",
                path="Git commit metadata",
                detail=(
                    "non-noreply commit email will become public: "
                    + _mask_email(email)
                ),
            )
        )
    return findings


def _repository_shape_warnings(current_paths: set[str]) -> list[Finding]:
    findings: list[Finding] = []
    if not any(
        path.lower() in {"license", "license.md", "license.txt"}
        for path in current_paths
    ):
        findings.append(
            Finding(
                severity="WARN",
                rule="missing_license",
                scope="current",
                path="repository root",
                detail="no LICENSE file is tracked; choose a license before public release",
            )
        )
    return findings


def run_audit() -> tuple[list[Finding], dict[str, int]]:
    findings: list[Finding] = []
    current_by_sha, current_paths = _current_index()
    current_shas = set(current_by_sha)
    history_paths = _all_historical_paths()

    for path in sorted(current_paths):
        if _is_sensitive_path(path):
            findings.append(
                Finding(
                    severity="FAIL",
                    rule="sensitive_path_tracked",
                    scope="current",
                    path=path,
                    detail="sensitive credential/key filename is tracked",
                )
            )
        if _contains_runtime_segment(path):
            findings.append(
                Finding(
                    severity="FAIL",
                    rule="runtime_artifact_tracked",
                    scope="current",
                    path=path,
                    detail="generated/results runtime material is tracked",
                )
            )

    for path in sorted(history_paths):
        if path in current_paths:
            continue
        if _is_sensitive_path(path):
            findings.append(
                Finding(
                    severity="FAIL",
                    rule="sensitive_path_in_history",
                    scope="history",
                    path=path,
                    detail="sensitive credential/key filename exists in reachable history",
                )
            )
        if _contains_runtime_segment(path):
            findings.append(
                Finding(
                    severity="FAIL",
                    rule="runtime_artifact_in_history",
                    scope="history",
                    path=path,
                    detail="generated/results runtime material exists in reachable history",
                )
            )

    object_paths = _historical_object_paths()
    blobs_scanned = 0
    blobs_skipped_large = 0
    large_blobs = 0
    for sha, paths in sorted(object_paths.items()):
        if _object_type(sha) != "blob":
            continue
        size = _object_size(sha)
        if size >= LARGE_BLOB_WARNING_BYTES:
            large_blobs += 1
            findings.append(
                Finding(
                    severity="WARN",
                    rule="large_history_blob",
                    scope="current" if sha in current_shas else "history",
                    path=", ".join(sorted(paths)[:3]),
                    detail=f"blob {sha[:12]} is {size / (1024 * 1024):.1f} MiB",
                )
            )
        if size > MAX_SCANNED_BLOB_BYTES:
            blobs_skipped_large += 1
            continue
        data = _blob_bytes(sha)
        blobs_scanned += 1
        findings.extend(
            _scan_blob(
                sha=sha,
                data=data,
                paths=paths,
                current_shas=current_shas,
            )
        )

    findings.extend(_commit_email_warnings())
    findings.extend(_repository_shape_warnings(current_paths))

    # Deduplicate identical findings that can arise when historical objects are
    # reachable through more than one ref.
    findings = sorted(
        set(findings),
        key=lambda item: (item.severity, item.rule, item.scope, item.path, item.detail),
    )
    stats = {
        "current_tracked_files": len(current_paths),
        "historical_paths": len(history_paths),
        "history_blobs_scanned": blobs_scanned,
        "history_blobs_skipped_large": blobs_skipped_large,
        "large_history_blobs": large_blobs,
    }
    return findings, stats


def main() -> int:
    try:
        findings, stats = run_audit()
    except Exception as exc:
        print(f"PUBLIC_RELEASE_AUDIT ERROR: {type(exc).__name__}: {exc}")
        return 1

    print("PUBLIC RELEASE AUDIT")
    print("====================")
    for key, value in stats.items():
        print(f"{key}: {value}")

    failures = [item for item in findings if item.severity == "FAIL"]
    warnings = [item for item in findings if item.severity == "WARN"]
    print(f"blocking_findings: {len(failures)}")
    print(f"warnings: {len(warnings)}")

    if findings:
        print("\nFindings:")
        for item in findings:
            print(
                f"[{item.severity}] {item.rule} | scope={item.scope} | "
                f"path={item.path} | {item.detail}"
            )

    if failures:
        print("\nRESULT: FAIL - repository is not ready to make public.")
        return 1

    if warnings:
        print("\nRESULT: PASS WITH WARNINGS - review warnings before public release.")
        return 0

    print("\nRESULT: PASS - no blocking public-release findings detected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
