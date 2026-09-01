from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path, PurePosixPath


FIELD_RE = re.compile(r"^\*\*(?P<name>[^*]+):\*\*\s*(?P<value>.*?)(?:\s{2})?$")
NUMBERED_FILENAME_RE = re.compile(r"^(?P<number>\d{3})_.*\.md$")
EXPLICIT_H1_RE = re.compile(
    r"^#\s+(?P<family>Foundation|Specification|Research|Checkpoint)\s+(?P<number>\d+)\b"
)
TYPED_REFERENCE_RE = re.compile(
    r"^(?P<kind>foundation|specification|research|checkpoint):(?P<target>.+)$"
)
NUMBERED_LABEL_RE = re.compile(
    r"^(?P<family>Foundation|Specification|Research|Checkpoint)\s+(?P<number>\d+)$"
)
THREAD_RE = re.compile(r"^MC-\d{4}$")

HEADER_SCAN_LINES = 100
VALIDATION_LEGACY_SNAPSHOT = Path(
    "scripts/repository_integrity_legacy_validation_paths.json"
)
EXPECTED_VALIDATION_INVENTORY_COMMIT = "adce1b47011ec0cee98393c2b6ff8c5c753b0ba0"
EXPECTED_VALIDATION_INVENTORY_RUN = 33415541195
EXPECTED_VALIDATION_INVENTORY_JOB = 99565171066
EXPECTED_VALIDATION_LEGACY_COUNT = 15
EXPECTED_VALIDATION_LEGACY_DIGEST = (
    "57945715e63969b64cb3927922b79a0ea8c45b91c943e8fba13e79b7ae3a631b"
)


@dataclass(frozen=True)
class FamilyContract:
    key: str
    label: str
    directory: Path
    metadata_cutover: int | None


FAMILY_CONTRACTS: tuple[FamilyContract, ...] = (
    FamilyContract("foundation", "Foundation", Path("docs/foundations"), 25),
    FamilyContract("specification", "Specification", Path("docs/specifications"), 25),
    FamilyContract("research", "Research", Path("docs/research"), 106),
    FamilyContract("checkpoint", "Checkpoint", Path("docs/checkpoints"), None),
)
FAMILY_BY_KEY = {contract.key: contract for contract in FAMILY_CONTRACTS}
FAMILY_BY_LABEL = {contract.label: contract for contract in FAMILY_CONTRACTS}

RELATIONSHIP_FIELDS = {
    "Supersedes",
    "Superseded by",
    "Promoted to",
    "Promoted from",
    "Governed by",
    "Research",
    "Specification",
    "Companion collaboration thread",
    "Companion thread",
}


@dataclass(frozen=True)
class NumberedDocument:
    contract: FamilyContract
    number: int
    path: Path


class IntegrityConfigurationError(ValueError):
    pass


def relative_posix(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def read_header_fields(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines()[:HEADER_SCAN_LINES]:
        if line.startswith("## "):
            break
        match = FIELD_RE.match(line.strip())
        if match:
            fields[match.group("name").strip()] = match.group("value").strip()
    return fields


def read_first_h1(path: Path) -> str | None:
    for line in path.read_text(encoding="utf-8").splitlines()[:HEADER_SCAN_LINES]:
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped
    return None


def collect_numbered_documents(root: Path) -> dict[str, list[NumberedDocument]]:
    result: dict[str, list[NumberedDocument]] = {}
    for contract in FAMILY_CONTRACTS:
        documents: list[NumberedDocument] = []
        directory = root / contract.directory
        if directory.is_dir():
            for path in sorted(directory.iterdir()):
                if not path.is_file():
                    continue
                match = NUMBERED_FILENAME_RE.match(path.name)
                if match:
                    documents.append(
                        NumberedDocument(contract, int(match.group("number")), path)
                    )
        result[contract.key] = documents
    return result


def validate_numbered_documents(root: Path) -> list[str]:
    errors: list[str] = []
    documents_by_family = collect_numbered_documents(root)

    for contract in FAMILY_CONTRACTS:
        documents = documents_by_family[contract.key]
        by_number: dict[int, list[NumberedDocument]] = {}
        for document in documents:
            by_number.setdefault(document.number, []).append(document)

        for number, matches in sorted(by_number.items()):
            if len(matches) > 1:
                paths = ", ".join(
                    relative_posix(document.path, root) for document in matches
                )
                errors.append(
                    f"{contract.label} {number:03d}: duplicate family identity: {paths}"
                )

        for document in documents:
            h1 = read_first_h1(document.path)
            if h1:
                h1_match = EXPLICIT_H1_RE.match(h1)
                if h1_match:
                    declared_family = h1_match.group("family")
                    declared_number = int(h1_match.group("number"))
                    if (
                        declared_family != contract.label
                        or declared_number != document.number
                    ):
                        errors.append(
                            f"{relative_posix(document.path, root)}: explicit H1 identity "
                            f"{declared_family} {declared_number:03d} disagrees with "
                            f"filename identity {contract.label} {document.number:03d}"
                        )

            if (
                contract.metadata_cutover is not None
                and document.number >= contract.metadata_cutover
            ):
                fields = read_header_fields(document.path)
                for required in ("Date", "Status", "Scope"):
                    if required not in fields or not fields[required].strip():
                        errors.append(
                            f"{relative_posix(document.path, root)}: post-cutover "
                            f"{contract.label} requires non-empty {required} metadata"
                        )

    return errors


def validation_evidence_paths(root: Path) -> list[Path]:
    docs = root / "docs"
    if not docs.is_dir():
        return []
    return sorted(
        path
        for path in docs.rglob("*.md")
        if path.is_file() and "validation" in path.relative_to(root).parts
    )


def _legacy_path_digest(paths: list[str]) -> str:
    payload = ("\n".join(paths) + "\n").encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def load_validation_legacy_snapshot(
    root: Path, snapshot_path: Path | None = None
) -> set[str]:
    relative = snapshot_path or VALIDATION_LEGACY_SNAPSHOT
    path = relative if relative.is_absolute() else root / relative
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise IntegrityConfigurationError(
            f"validation/evidence legacy compatibility snapshot missing: {path}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise IntegrityConfigurationError(
            f"validation/evidence legacy compatibility snapshot invalid JSON: {exc}"
        ) from exc

    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise IntegrityConfigurationError(
            "validation/evidence legacy compatibility snapshot requires schema_version=1"
        )
    if data.get("inventory_commit") != EXPECTED_VALIDATION_INVENTORY_COMMIT:
        raise IntegrityConfigurationError(
            "validation/evidence legacy snapshot inventory_commit is not the frozen MC-0008 inventory commit"
        )
    if data.get("inventory_workflow_run") != EXPECTED_VALIDATION_INVENTORY_RUN:
        raise IntegrityConfigurationError(
            "validation/evidence legacy snapshot workflow run is not the frozen MC-0008 inventory run"
        )
    if data.get("inventory_job") != EXPECTED_VALIDATION_INVENTORY_JOB:
        raise IntegrityConfigurationError(
            "validation/evidence legacy snapshot job is not the frozen MC-0008 inventory job"
        )

    paths = data.get("legacy_paths")
    if not isinstance(paths, list) or not paths:
        raise IntegrityConfigurationError(
            "validation/evidence legacy compatibility snapshot requires legacy_paths"
        )
    if any(not isinstance(item, str) or not item for item in paths):
        raise IntegrityConfigurationError(
            "validation/evidence legacy compatibility paths must be non-empty strings"
        )
    if len(paths) != len(set(paths)):
        raise IntegrityConfigurationError(
            "validation/evidence legacy compatibility snapshot contains duplicate paths"
        )
    if paths != sorted(paths):
        raise IntegrityConfigurationError(
            "validation/evidence legacy compatibility snapshot paths must remain sorted"
        )
    if len(paths) != EXPECTED_VALIDATION_LEGACY_COUNT:
        raise IntegrityConfigurationError(
            "validation/evidence legacy compatibility snapshot path count changed from the frozen inventory"
        )
    if _legacy_path_digest(paths) != EXPECTED_VALIDATION_LEGACY_DIGEST:
        raise IntegrityConfigurationError(
            "validation/evidence legacy compatibility snapshot path set changed from the frozen inventory"
        )
    return set(paths)


def validate_validation_evidence(
    root: Path, snapshot_path: Path | None = None
) -> list[str]:
    errors: list[str] = []
    try:
        legacy_paths = load_validation_legacy_snapshot(root, snapshot_path)
    except IntegrityConfigurationError as exc:
        return [str(exc)]

    current_paths = {relative_posix(path, root) for path in validation_evidence_paths(root)}
    missing_legacy = sorted(legacy_paths - current_paths)
    for path in missing_legacy:
        errors.append(
            f"{path}: frozen validation/evidence legacy path is missing from repository"
        )

    for path in validation_evidence_paths(root):
        relative = relative_posix(path, root)
        if relative in legacy_paths:
            continue
        fields = read_header_fields(path)
        if not fields.get("Date", "").strip():
            errors.append(f"{relative}: new validation/evidence artifact requires Date")
        if not (
            fields.get("Status", "").strip()
            or fields.get("Classification", "").strip()
        ):
            errors.append(
                f"{relative}: new validation/evidence artifact requires Status or Classification"
            )
        if not any(
            fields.get(name, "").strip()
            for name in ("Research", "Specification", "Scope")
        ):
            errors.append(
                f"{relative}: new validation/evidence artifact requires Research, "
                "Specification, or Scope"
            )
    return errors


def safe_repository_relative_path(value: str) -> PurePosixPath | None:
    if not value or "\\" in value or "\x00" in value:
        return None
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or "." in path.parts:
        return None
    if not path.parts or path.parts[0].startswith("~"):
        return None
    if any(":" in part for part in path.parts):
        return None
    return path


def numbered_target_exists(
    documents_by_family: dict[str, list[NumberedDocument]], kind: str, number: int
) -> bool:
    return any(
        document.number == number for document in documents_by_family.get(kind, [])
    )


def validate_reference_token(
    root: Path,
    token: str,
    documents_by_family: dict[str, list[NumberedDocument]] | None = None,
) -> str | None:
    documents = documents_by_family or collect_numbered_documents(root)
    token = token.strip()

    if token.startswith("path:"):
        raw_path = token[len("path:") :]
        safe_path = safe_repository_relative_path(raw_path)
        if safe_path is None:
            return f"unsafe or malformed repository path reference: {token!r}"
        if not (root / Path(*safe_path.parts)).exists():
            return f"missing repository path reference target: {token!r}"
        return None

    match = TYPED_REFERENCE_RE.fullmatch(token)
    if not match:
        return f"malformed or unknown declared reference: {token!r}"
    kind = match.group("kind")
    target = match.group("target")
    if kind not in FAMILY_BY_KEY or not target.isdigit() or int(target) <= 0:
        return f"malformed or unknown declared reference: {token!r}"
    number = int(target)
    if not numbered_target_exists(documents, kind, number):
        return f"missing {kind} reference target: {token!r}"
    return None


def parse_declared_reference_field(value: str) -> tuple[list[str], str | None]:
    stripped = value.strip()
    if not stripped:
        return [], "Declared references must contain one or more backticked references"
    parts = [part.strip() for part in stripped.split(",")]
    if any(not re.fullmatch(r"`[^`]+`", part) for part in parts):
        return [], (
            "Declared references must be a comma-separated list of backticked references"
        )
    return [part[1:-1].strip() for part in parts], None


def _looks_like_explicit_path(candidate: str) -> bool:
    return "/" in candidate or candidate.lower().endswith(".md")


def existing_relationship_reference(value: str) -> tuple[str, str] | None:
    stripped = value.strip()
    if re.fullmatch(r"`[^`]+`", stripped):
        candidate = stripped[1:-1].strip()
        if THREAD_RE.fullmatch(candidate):
            return ("thread", candidate)
        if NUMBERED_LABEL_RE.fullmatch(candidate):
            return ("numbered", candidate)
        if (
            _looks_like_explicit_path(candidate)
            and safe_repository_relative_path(candidate) is not None
        ):
            return ("path", candidate)
        return None

    if THREAD_RE.fullmatch(stripped):
        return ("thread", stripped)
    if NUMBERED_LABEL_RE.fullmatch(stripped):
        return ("numbered", stripped)
    return None


def validate_existing_relationship_target(
    root: Path,
    reference: tuple[str, str],
    documents_by_family: dict[str, list[NumberedDocument]],
) -> str | None:
    kind, target = reference
    if kind == "path":
        safe_path = safe_repository_relative_path(target)
        if safe_path is None:
            return f"unsafe repository path relationship target: {target!r}"
        if not (root / Path(*safe_path.parts)).exists():
            return f"missing repository path relationship target: {target!r}"
        return None
    if kind == "thread":
        if not (root / "docs" / "model_collaboration" / "threads" / target).is_dir():
            return f"missing collaboration thread relationship target: {target!r}"
        return None
    if kind == "numbered":
        match = NUMBERED_LABEL_RE.fullmatch(target)
        if not match:
            return f"malformed numbered relationship target: {target!r}"
        contract = FAMILY_BY_LABEL[match.group("family")]
        number = int(match.group("number"))
        if number <= 0 or not numbered_target_exists(
            documents_by_family, contract.key, number
        ):
            return f"missing numbered relationship target: {target!r}"
        return None
    return f"unsupported relationship target kind: {kind!r}"


def validate_declared_relationships(root: Path) -> list[str]:
    errors: list[str] = []
    documents_by_family = collect_numbered_documents(root)
    docs = root / "docs"
    if not docs.is_dir():
        return ["docs directory missing"]

    for path in sorted(docs.rglob("*.md")):
        if not path.is_file():
            continue
        fields = read_header_fields(path)
        relative = relative_posix(path, root)

        if "Declared references" in fields:
            tokens, parse_error = parse_declared_reference_field(
                fields["Declared references"]
            )
            if parse_error:
                errors.append(f"{relative}: {parse_error}")
            else:
                for token in tokens:
                    error = validate_reference_token(root, token, documents_by_family)
                    if error:
                        errors.append(f"{relative}: {error}")

        for field_name in sorted(RELATIONSHIP_FIELDS):
            if field_name not in fields:
                continue
            reference = existing_relationship_reference(fields[field_name])
            if reference is None:
                continue
            error = validate_existing_relationship_target(
                root, reference, documents_by_family
            )
            if error:
                errors.append(f"{relative}: {field_name}: {error}")

    return errors


def validate_repository_contracts(root: Path) -> list[str]:
    errors: list[str] = []
    errors.extend(validate_numbered_documents(root))
    errors.extend(validate_validation_evidence(root))
    errors.extend(validate_declared_relationships(root))
    return errors
