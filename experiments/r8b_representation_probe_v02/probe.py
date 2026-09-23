from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import json
import re
import shutil
import sqlite3
import subprocess
import tempfile
import tomllib
from pathlib import Path
from typing import Any, Callable

from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent

REAL_WORKSTREAM = ROOT / "docs/source_universe/SOURCE_VAULT_BOOTSTRAP_WORKSTREAM.md"
REAL_SPEC = ROOT / "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md"

EXPECTED_SOURCE_SHA256 = {
    "docs/source_universe/SOURCE_VAULT_BOOTSTRAP_WORKSTREAM.md":
        "8af6602abbc25ff7eac8d8021239841231b32d28fe0880c859b3be2a7c30ea2a",
    "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md":
        "7651707b5d590efd7686a77dca20597dc731bfafa1fabc2358775bef7b9d2ffe",
}

HARNESS_PATHS = [
    "experiments/r8b_representation_probe_v02/README.md",
    "experiments/r8b_representation_probe_v02/probe.py",
    "experiments/r8b_representation_probe_v02/schemas/project_meta.schema.json",
    "experiments/r8b_representation_probe_v02/schemas/workstream_state.schema.json",
    "experiments/r8b_representation_probe_v02/schemas/receipt.schema.json",
    "experiments/r8b_representation_probe_v02/schemas/standalone_relation.schema.json",
]

META_FENCE = "\x60\x60\x60toml project-meta"
META_EXAMPLE_FENCE = "\x60\x60\x60toml project-meta-example"
FENCE_END = "\x60\x60\x60"
RC3_REVIEW_BOUND = 12


class ProbeFailure(RuntimeError):
    pass


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def canonical_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n"
    ).encode("utf-8")


def pretty_json(value: Any) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def normalize_newlines_bytes(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def normalize_blank_runs(text: str) -> str:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    out: list[str] = []
    blank = False
    for line in lines:
        if line.strip() == "":
            if not blank:
                out.append("")
            blank = True
        else:
            out.append(line.rstrip())
            blank = False
    return "\n".join(out).strip()


def load_schema(name: str) -> dict[str, Any]:
    return json.loads((HERE / "schemas" / name).read_text(encoding="utf-8"))


PROJECT_META_SCHEMA = load_schema("project_meta.schema.json")
WORKSTREAM_STATE_SCHEMA = load_schema("workstream_state.schema.json")
RECEIPT_SCHEMA = load_schema("receipt.schema.json")
RELATION_SCHEMA = load_schema("standalone_relation.schema.json")


def validate_schema(value: Any, schema: dict[str, Any]) -> None:
    Draft202012Validator(schema).validate(value)


def _reject_non_json_toml(value: Any, path: str = "$") -> None:
    if isinstance(value, (dt.datetime, dt.date, dt.time)):
        raise ProbeFailure(
            f"non-JSON TOML value at {path}: {type(value).__name__}"
        )
    if isinstance(value, dict):
        for key, item in value.items():
            _reject_non_json_toml(item, f"{path}.{key}")
    elif isinstance(value, list):
        for idx, item in enumerate(value):
            _reject_non_json_toml(item, f"{path}[{idx}]")


def _title_extent(lines: list[str], start: int) -> tuple[int, str] | None:
    if start >= len(lines):
        return None
    line = lines[start]
    if line.startswith("# ") and not line.startswith("## "):
        return start, line[2:].strip()
    if (
        line.strip()
        and start + 1 < len(lines)
        and re.fullmatch(r"=+\s*", lines[start + 1])
    ):
        return start + 1, line.strip()
    return None


def parse_governed_markdown(
    text: str,
    compat_checker: Callable[[Any], None] = _reject_non_json_toml,
) -> dict[str, Any]:
    if text.startswith("\ufeff"):
        text = text[1:]

    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    idx = 0
    while idx < len(lines) and lines[idx].strip() == "":
        idx += 1

    title = _title_extent(lines, idx)
    if title is None:
        if idx < len(lines) and lines[idx] == META_FENCE:
            return {
                "classification": "error",
                "error": "governed metadata fence appears without H1 title",
            }
        return {"classification": "plain", "metadata": None}

    title_end, title_text = title
    meta_idx = title_end + 1
    while meta_idx < len(lines) and lines[meta_idx].strip() == "":
        meta_idx += 1

    if meta_idx >= len(lines) or lines[meta_idx] != META_FENCE:
        return {
            "classification": "plain",
            "metadata": None,
            "title": title_text,
        }

    end = meta_idx + 1
    while end < len(lines) and lines[end] != FENCE_END:
        end += 1
    if end >= len(lines):
        return {
            "classification": "error",
            "error": "unterminated governed metadata fence",
        }

    block = "\n".join(lines[meta_idx + 1 : end])
    try:
        metadata = tomllib.loads(block)
        compat_checker(metadata)
        validate_schema(metadata, PROJECT_META_SCHEMA)
    except Exception as exc:
        return {"classification": "error", "error": str(exc)}

    if any(line == META_FENCE for line in lines[end + 1 :]):
        return {
            "classification": "error",
            "error": "duplicate governed metadata fence",
        }

    return {
        "classification": "governed",
        "metadata": metadata,
        "title": title_text,
        "metadata_start": meta_idx,
        "metadata_end": end,
        "normalized_text": "\n".join(lines),
    }


def _toml_scalar(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, int):
        return str(value)
    raise TypeError(f"unsupported TOML scalar: {type(value).__name__}")


def metadata_block(metadata: dict[str, Any]) -> str:
    scalar_keys = [
        "contract",
        "id",
        "kind",
        "authority",
        "lifecycle",
        "status",
    ]
    lines = [META_FENCE]
    for key in scalar_keys:
        if key in metadata:
            lines.append(f"{key} = {_toml_scalar(metadata[key])}")

    for key in ["subjects", "provenance", "declared_references"]:
        if key in metadata:
            values = ", ".join(_toml_scalar(x) for x in metadata[key])
            lines.append(f"{key} = [{values}]")

    if metadata.get("scope"):
        lines.append("")
        lines.append("[scope]")
        for key, value in metadata["scope"].items():
            lines.append(f"{key} = {_toml_scalar(value)}")

    if metadata.get("extensions"):
        lines.append("")
        lines.append("[extensions]")
        for key, value in metadata["extensions"].items():
            lines.append(f"{key} = {_toml_scalar(value)}")

    for relation in metadata.get("relations", []):
        lines.append("")
        lines.append("[[relations]]")
        lines.append(f"type = {_toml_scalar(relation['type'])}")
        lines.append(f"target = {_toml_scalar(relation['target'])}")

    lines.append(FENCE_END)
    return "\n".join(lines)


def strip_governed_metadata(text: str) -> str:
    parsed = parse_governed_markdown(text)
    if parsed["classification"] != "governed":
        raise ProbeFailure("carrier is not governed")
    lines = parsed["normalized_text"].split("\n")
    kept = (
        lines[: parsed["metadata_start"]]
        + lines[parsed["metadata_end"] + 1 :]
    )
    return "\n".join(kept)


def extract_legacy_json_declaration(
    text: str,
) -> tuple[dict[str, Any], str]:
    begin = "<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->"
    end = "<!-- PKA-STRUCTURED-DECLARATION-END -->"
    if begin not in text or end not in text:
        raise ProbeFailure("legacy declaration not found")
    start = text.index(begin)
    finish = text.index(end, start) + len(end)
    raw = text[start + len(begin) : text.index(end, start)].strip()
    return json.loads(raw), text[start:finish]


def verify_real_source_hashes() -> dict[str, str]:
    actual: dict[str, str] = {}
    for rel, expected in EXPECTED_SOURCE_SHA256.items():
        digest = sha256_file(ROOT / rel)
        if digest != expected:
            raise ProbeFailure(
                f"real-source drift for {rel}: {digest} != {expected}"
            )
        actual[rel] = digest
    return actual


def _parse_state_block(text: str) -> dict[str, str]:
    match = re.search(
        r"## Current qualified state\b.*?\n\x60\x60\x60text\s*\n"
        r"(.*?)\n\x60\x60\x60",
        text,
        flags=re.S,
    )
    if not match:
        raise ProbeFailure("real workstream state block not found")
    observations: dict[str, str] = {}
    for raw in match.group(1).splitlines():
        line = raw.strip()
        if not line:
            continue
        parts = re.split(r"\s{2,}", line, maxsplit=1)
        if len(parts) != 2:
            raise ProbeFailure(f"cannot parse state observation: {line}")
        observations[parts[0]] = parts[1]
    return observations


def convert_real_workstream(
    source_text: str,
) -> tuple[str, dict[str, Any], dict[str, Any], dict[str, Any]]:
    legacy, _legacy_block = extract_legacy_json_declaration(source_text)
    observations = _parse_state_block(source_text)

    metadata = {
        "contract": "project-knowledge-carrier/1",
        "id": legacy["semantic_id"],
        "kind": "workstream-definition",
        "authority": legacy["authority_class"],
        "lifecycle": "active",
        "subjects": sorted(set(legacy["scope"].values())),
        "scope": dict(legacy["scope"]),
        "provenance": list(legacy["provenance"]),
        "declared_references": list(legacy["references"]),
        "relations": [
            {
                "type": "governed-by",
                "target": legacy["governing_procedure"],
            }
        ],
    }

    milestone_map = {
        item["milestone_id"]: item["state"]
        for item in legacy["orientation_milestones"]
    }

    known_observation_labels = {
        "workstream state",
        "source ingestion",
        "Course 2",
        "resume target",
    }
    residual_observations = {
        key: value
        for key, value in observations.items()
        if key not in known_observation_labels
    }

    state = {
        "contract": "project-control-workstream-state/1",
        "workstream_id": legacy["semantic_id"],
        "revision": 1,
        "state": legacy["state"],
        "pause_reason": legacy["pause_reason"],
        "return_condition": legacy["return_condition"],
        "resume_target": legacy["resume_target"],
        "expected_to_resume": legacy["expected_to_resume"],
        "milestones": milestone_map,
        "observations": residual_observations,
    }
    validate_schema(state, WORKSTREAM_STATE_SCHEMA)

    public_boundary = ""
    for paragraph in re.split(r"\n\s*\n", source_text):
        if paragraph.strip().startswith(
            "The public source intentionally records only"
        ):
            public_boundary = paragraph.strip()
            break
    if not public_boundary:
        raise ProbeFailure("public/private boundary paragraph not found")

    risks = "\n".join(
        f"- {item}" for item in legacy["risk_or_reopen_triggers"]
    )
    definition = (
        "# Permanent Source Vault Bootstrap Workstream\n\n"
        + metadata_block(metadata)
        + "\n\n"
        + "## Objective\n\n"
        + legacy["objective"]
        + "\n\n"
        + "## Governing procedure\n\n"
        + legacy["governing_procedure"]
        + "\n\n"
        + "## Pause semantics\n\n"
        + "A PAUSED state is routing and does not by itself mean completion "
          "or supersession. Current pause/resume facts live in Project-system "
          "control state.\n\n"
        + "## Public/private boundary\n\n"
        + public_boundary
        + "\n\n"
        + "## Durable risk and reopen triggers\n\n"
        + risks
        + "\n"
    )

    declaration_disposition = {
        "schema_version": "replaced-by:metadata.contract",
        "profile": "mapped-to:metadata.kind",
        "kind": "mapped-to:metadata.kind",
        "authority_class": "mapped-to:metadata.authority",
        "semantic_id": "mapped-to:metadata.id",
        "state": "moved-to:state.state",
        "scope": "mapped-to:metadata.scope",
        "objective": "preserved-in:definition.objective",
        "expected_to_resume": "moved-to:state.expected_to_resume",
        "pause_reason": "moved-to:state.pause_reason",
        "return_condition": "moved-to:state.return_condition",
        "resume_target": "moved-to:state.resume_target",
        "governing_procedure": "preserved-in:definition-and-relation",
        "orientation_milestones": "moved-to:state.milestones",
        "provenance": "mapped-to:metadata.provenance",
        "references": "mapped-to:metadata.declared_references",
        "risk_or_reopen_triggers":
            "preserved-in:definition.risk_or_reopen_triggers",
    }
    if set(declaration_disposition) != set(legacy):
        missing = set(legacy) - set(declaration_disposition)
        extra = set(declaration_disposition) - set(legacy)
        raise ProbeFailure(
            f"workstream conversion manifest mismatch missing={missing} "
            f"extra={extra}"
        )

    loss_manifest = {
        "legacy_declaration_fields": declaration_disposition,
        "prose": {
            "current_qualified_state":
                "transition facts moved to state; residual observations retained",
            "pause_routing_paragraph":
                "durable pause semantics retained; current routing facts moved to state",
            "public_private_boundary":
                "preserved verbatim in definition",
        },
        "dropped_without_disposition": [],
    }
    return definition, state, loss_manifest, legacy


def _parse_header_value(source: str, label: str) -> str:
    pattern = rf"^\*\*{re.escape(label)}:\*\*\s*(.+)$"
    match = re.search(pattern, source, flags=re.M)
    if not match:
        raise ProbeFailure(f"header {label!r} not found")
    return match.group(1).strip()


def convert_real_specification(
    source_text: str,
) -> tuple[str, dict[str, Any], dict[str, Any], dict[str, Any]]:
    legacy, legacy_block = extract_legacy_json_declaration(source_text)
    status = _parse_header_value(source_text, "Status")
    authority_clause = _parse_header_value(source_text, "Authority")
    declared_line = _parse_header_value(source_text, "Declared references")
    declared_from_header = re.findall(r"\x60([^\x60]+)\x60", declared_line)
    all_references = sorted(
        set(declared_from_header) | set(legacy.get("references", []))
    )
    lifecycle = "frozen" if "FROZEN" in status.upper() else "active"

    metadata = {
        "contract": "project-knowledge-carrier/1",
        "id": legacy["semantic_id"],
        "kind": "specification",
        "authority": legacy["authority_class"],
        "lifecycle": lifecycle,
        "status": status,
        "subjects": sorted(set(legacy.get("scope", {}).values())),
        "scope": dict(legacy.get("scope", {})),
        "provenance": list(legacy.get("provenance", [])),
        "declared_references": all_references,
    }

    without_legacy = source_text.replace(legacy_block, "", 1)
    first_break = without_legacy.find("\n")
    if first_break < 0:
        raise ProbeFailure("specification title line missing newline")
    title = without_legacy[:first_break]
    rest = without_legacy[first_break + 1 :].lstrip("\r\n")
    candidate = title + "\n\n" + metadata_block(metadata) + "\n\n" + rest

    declaration_disposition = {
        "schema_version": "replaced-by:metadata.contract",
        "profile": "mapped-to:metadata.kind",
        "kind": "mapped-to:metadata.kind",
        "authority_class": "mapped-to:metadata.authority",
        "semantic_id": "mapped-to:metadata.id",
        "scope": "mapped-to:metadata.scope",
        "provenance": "mapped-to:metadata.provenance",
        "references": "merged-into:metadata.declared_references",
    }
    if set(declaration_disposition) != set(legacy):
        raise ProbeFailure(
            "spec conversion manifest does not cover every legacy field"
        )

    loss_manifest = {
        "legacy_declaration_fields": declaration_disposition,
        "header": {
            "status": "preserved-verbatim-and-mapped-to-metadata.status/lifecycle",
            "authority":
                "preserved-verbatim; metadata.authority reflects canonical carrier role",
            "declared_references":
                "preserved-verbatim-and-mapped-to-metadata.declared_references",
        },
        "authority_clause": authority_clause,
        "dropped_without_disposition": [],
    }
    return candidate, metadata, loss_manifest, legacy


def git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    cp = subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )
    if check and cp.returncode != 0:
        raise ProbeFailure(
            f"git {' '.join(args)} failed: {cp.stdout}\n{cp.stderr}"
        )
    return cp


def git_bytes(repo: Path, *args: str) -> bytes:
    cp = subprocess.run(
        ["git", *args],
        cwd=repo,
        capture_output=True,
        check=False,
    )
    if cp.returncode != 0:
        raise ProbeFailure(
            f"git {' '.join(args)} failed: "
            f"{cp.stderr.decode('utf-8', errors='replace')}"
        )
    return cp.stdout


def init_temp_repo(repo: Path) -> None:
    git(repo, "init")
    git(repo, "config", "user.email", "probe@example.invalid")
    git(repo, "config", "user.name", "P-R8B-01-R2 Probe")


def commit_all(repo: Path, message: str) -> str:
    git(repo, "add", "-A")
    git(repo, "commit", "-m", message)
    return git(repo, "rev-parse", "HEAD").stdout.strip()


def state_semantic_payload(record: dict[str, Any]) -> dict[str, Any]:
    payload = copy.deepcopy(record)
    payload.pop("revision", None)
    return payload


def validate_ordinary_transition(
    previous: dict[str, Any],
    new: dict[str, Any],
) -> None:
    validate_schema(previous, WORKSTREAM_STATE_SCHEMA)
    validate_schema(new, WORKSTREAM_STATE_SCHEMA)
    if state_semantic_payload(previous) == state_semantic_payload(new):
        raise ProbeFailure("revision-only mutation is invalid")
    if new["revision"] != previous["revision"] + 1:
        raise ProbeFailure(
            "ordinary semantic mutation must increment revision exactly once"
        )


def validate_merge_resolution(
    parents: list[dict[str, Any]],
    resolved: dict[str, Any],
) -> None:
    if len(parents) < 2:
        raise ProbeFailure("merge validation needs at least two parents")
    validate_schema(resolved, WORKSTREAM_STATE_SCHEMA)
    for parent in parents:
        validate_schema(parent, WORKSTREAM_STATE_SCHEMA)
    required = max(parent["revision"] for parent in parents) + 1
    if resolved["revision"] != required:
        raise ProbeFailure(
            f"merge resolution revision must be {required}"
        )
    if all(
        state_semantic_payload(resolved) == state_semantic_payload(parent)
        for parent in parents
    ):
        raise ProbeFailure("merge resolution must represent semantic result")


def expect_reject(call: Callable[[], Any], label: str) -> str:
    try:
        call()
    except Exception:
        return "rejected"
    raise ProbeFailure(f"{label} was accepted")


def exercise_transition_negative_checks(
    validator: Callable[[dict[str, Any], dict[str, Any]], None],
    base: dict[str, Any],
) -> dict[str, str]:
    revision_only = copy.deepcopy(base)
    revision_only["revision"] += 1

    decrement = copy.deepcopy(base)
    decrement["revision"] = max(1, base["revision"] - 1)
    decrement["state"] = "ACTIVE"

    same_revision = copy.deepcopy(base)
    same_revision["state"] = "ACTIVE"

    skipped = copy.deepcopy(base)
    skipped["revision"] += 2
    skipped["state"] = "ACTIVE"

    return {
        "revision_only": expect_reject(
            lambda: validator(base, revision_only),
            "revision-only mutation",
        ),
        "decrement": expect_reject(
            lambda: validator(base, decrement),
            "decrement",
        ),
        "same_revision": expect_reject(
            lambda: validator(base, same_revision),
            "same-revision semantic replacement",
        ),
        "skipped_revision": expect_reject(
            lambda: validator(base, skipped),
            "skipped ordinary revision",
        ),
    }


def transition_state_file(
    state_path: Path,
    mutator: Callable[[dict[str, Any]], None],
) -> dict[str, Any]:
    previous = json.loads(state_path.read_text(encoding="utf-8"))
    new = copy.deepcopy(previous)
    mutator(new)
    new["revision"] = previous["revision"] + 1
    validate_ordinary_transition(previous, new)
    state_path.write_text(pretty_json(new), encoding="utf-8")
    return new


def guarded_write(
    path: Path,
    expected_sha: str,
    new_record: dict[str, Any],
) -> str:
    if sha256_file(path) != expected_sha:
        raise ProbeFailure("stale write rejected")
    path.write_text(pretty_json(new_record), encoding="utf-8")
    return sha256_file(path)


def state_at_commit(
    repo: Path,
    commit: str,
    rel_path: str,
) -> dict[str, Any] | None:
    cp = subprocess.run(
        ["git", "show", f"{commit}:{rel_path}"],
        cwd=repo,
        capture_output=True,
        check=False,
    )
    if cp.returncode != 0:
        return None
    return json.loads(cp.stdout.decode("utf-8"))


def validate_committed_state_history(
    repo: Path,
    rel_path: str,
    head: str = "HEAD",
) -> dict[str, Any]:
    commits = git(
        repo,
        "rev-list",
        "--reverse",
        "--topo-order",
        head,
        "--",
        rel_path,
    ).stdout.splitlines()
    if not commits:
        raise ProbeFailure("no committed state history found")

    checked = 0
    for commit in commits:
        record = state_at_commit(repo, commit, rel_path)
        if record is None:
            continue
        validate_schema(record, WORKSTREAM_STATE_SCHEMA)
        parent_ids = git(
            repo,
            "show",
            "-s",
            "--format=%P",
            commit,
        ).stdout.strip().split()
        parent_records = [
            state_at_commit(repo, parent, rel_path)
            for parent in parent_ids
        ]
        parent_records = [p for p in parent_records if p is not None]
        if not parent_records:
            if record["revision"] < 1:
                raise ProbeFailure("root state revision must be positive")
            continue
        if len(parent_records) == 1:
            parent = parent_records[0]
            if state_semantic_payload(record) == state_semantic_payload(parent):
                if record["revision"] != parent["revision"]:
                    raise ProbeFailure(
                        "non-semantic commit changed revision"
                    )
            else:
                if record["revision"] != parent["revision"] + 1:
                    raise ProbeFailure(
                        "ordinary committed semantic mutation skipped or "
                        "failed to increment revision"
                    )
        else:
            validate_merge_resolution(parent_records, record)
        checked += 1

    return {"commits_checked": checked, "status": "valid"}


def make_receipt(
    event_type: str,
    result: str,
    source_revision: str = "rev-1",
) -> dict[str, Any]:
    provisional = {
        "receipt_id": "pending",
        "event_type": event_type,
        "source_revision": source_revision,
        "payload": {
            "result": result,
            "public_classification": "PUBLIC_SAFE",
        },
    }
    digest_source = copy.deepcopy(provisional)
    digest_source["receipt_id"] = ""
    digest = sha256_bytes(canonical_json_bytes(digest_source))
    provisional["receipt_id"] = f"receipt:{digest}"
    return provisional


def receipt_locator(
    receipt: dict[str, Any],
    month: str = "2026-09",
) -> str:
    digest = receipt["receipt_id"].split(":", 1)[1]
    return f"receipts/{month}/{digest}.json"


def contains_private_sentinel(value: Any) -> bool:
    if isinstance(value, str):
        return "PRIVATE_ONLY://" in value
    if isinstance(value, dict):
        return any(contains_private_sentinel(v) for v in value.values())
    if isinstance(value, list):
        return any(contains_private_sentinel(v) for v in value)
    return False


def validate_public_receipt(receipt: dict[str, Any]) -> None:
    validate_schema(receipt, RECEIPT_SCHEMA)
    if contains_private_sentinel(receipt):
        raise ProbeFailure("private-only sentinel rejected")


def relation_toml(
    relation_id: str,
    source: str,
    target: str,
    relation_type: str = "relates-to",
) -> str:
    return (
        'contract = "project-standalone-relation/1"\n'
        'kind = "standalone-relation"\n'
        f"relation_id = {json.dumps(relation_id)}\n"
        f"relation_type = {json.dumps(relation_type)}\n"
        f"source = {json.dumps(source)}\n"
        f"target = {json.dumps(target)}\n"
    )


def discover_relations(root: Path) -> list[dict[str, Any]]:
    found: list[dict[str, Any]] = []
    for path in root.rglob("*.toml"):
        raw = path.read_text(encoding="utf-8")
        try:
            value = tomllib.loads(raw)
        except Exception:
            if 'kind = "standalone-relation"' in raw:
                raise ProbeFailure(
                    f"malformed declared standalone relation: {path}"
                )
            continue
        if value.get("kind") == "standalone-relation":
            validate_schema(value, RELATION_SCHEMA)
            found.append(value)
    return sorted(found, key=lambda x: x["relation_id"])


def rc3_admission(discovered_count: int) -> str:
    return (
        "REVIEW_REQUIRED"
        if discovered_count >= RC3_REVIEW_BOUND
        else "ADMIT"
    )


def discover_pairing_violations(root: Path) -> dict[str, Any]:
    definitions: dict[str, int] = {}
    for path in root.rglob("*.md"):
        parsed = parse_governed_markdown(
            path.read_text(encoding="utf-8")
        )
        if (
            parsed["classification"] == "governed"
            and parsed["metadata"]["kind"] == "workstream-definition"
        ):
            semantic_id = parsed["metadata"]["id"]
            definitions[semantic_id] = definitions.get(semantic_id, 0) + 1

    states: list[tuple[Path, dict[str, Any]]] = []
    for path in root.rglob("*.json"):
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if value.get("contract") == "project-control-workstream-state/1":
            validate_schema(value, WORKSTREAM_STATE_SCHEMA)
            states.append((path, value))

    violations: list[str] = []
    for path, state in states:
        count = definitions.get(state["workstream_id"], 0)
        if count != 1:
            violations.append(
                f"{path.name}:{state['workstream_id']}:definition_count={count}"
            )

    for semantic_id, count in definitions.items():
        if count != 1:
            violations.append(
                f"definition:{semantic_id}:count={count}"
            )

    return {
        "definition_count": sum(definitions.values()),
        "state_count": len(states),
        "violations": violations,
        "pairing_violations": len(violations),
    }


def build_current_json(
    definition_path: Path,
    state_path: Path,
    state: dict[str, Any],
) -> dict[str, Any]:
    sources = [
        {
            "id": state["workstream_id"],
            "role": "definition",
            "path": definition_path.name,
            "revision": None,
            "sha256": sha256_file(definition_path),
        },
        {
            "id": state["workstream_id"],
            "role": "state",
            "path": state_path.name,
            "revision": state["revision"],
            "sha256": sha256_file(state_path),
        },
    ]
    boundary = sha256_bytes(canonical_json_bytes(sources))
    return {
        "contract": "project-orientation/1",
        "derived": True,
        "authoritative": False,
        "source_boundary_digest": boundary,
        "sources": sources,
        "workstreams": [
            {
                "id": state["workstream_id"],
                "state": state["state"],
                "revision": state["revision"],
            }
        ],
    }


def current_json_is_fresh(
    current: dict[str, Any],
    source_dir: Path,
) -> bool:
    for item in current["sources"]:
        path = source_dir / item["path"]
        if not path.exists():
            return False
        if sha256_file(path) != item["sha256"]:
            return False
        if item["revision"] is not None:
            value = json.loads(path.read_text(encoding="utf-8"))
            if value.get("revision") != item["revision"]:
                return False
    return (
        sha256_bytes(canonical_json_bytes(current["sources"]))
        == current["source_boundary_digest"]
    )


def build_sqlite_index_from_disk(
    db_path: Path,
    canonical_root: Path,
) -> dict[str, Any]:
    if db_path.exists():
        db_path.unlink()
    con = sqlite3.connect(db_path)
    try:
        con.executescript(
            """
            CREATE TABLE sources(
                id TEXT PRIMARY KEY,
                kind TEXT NOT NULL,
                state TEXT
            );
            CREATE TABLE relations(
                relation_id TEXT PRIMARY KEY,
                relation_type TEXT,
                source TEXT,
                target TEXT
            );
            CREATE VIRTUAL TABLE docs_fts USING fts5(id UNINDEXED, body);
            """
        )

        for path in canonical_root.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            parsed = parse_governed_markdown(text)
            if parsed["classification"] != "governed":
                continue
            semantic_id = parsed["metadata"]["id"]
            kind = parsed["metadata"]["kind"]
            con.execute(
                "INSERT OR REPLACE INTO sources(id, kind, state) "
                "VALUES (?, ?, NULL)",
                (semantic_id, kind),
            )
            con.execute(
                "INSERT INTO docs_fts(id, body) VALUES (?, ?)",
                (semantic_id, text),
            )

        for path in canonical_root.rglob("*.json"):
            try:
                value = json.loads(path.read_text(encoding="utf-8"))
            except Exception:
                continue
            if value.get("contract") == "project-control-workstream-state/1":
                validate_schema(value, WORKSTREAM_STATE_SCHEMA)
                con.execute(
                    "INSERT OR REPLACE INTO sources(id, kind, state) "
                    "VALUES (?, ?, ?)",
                    (
                        value["workstream_id"],
                        "workstream",
                        value["state"],
                    ),
                )

        for relation in discover_relations(canonical_root):
            con.execute(
                "INSERT INTO relations VALUES (?, ?, ?, ?)",
                (
                    relation["relation_id"],
                    relation["relation_type"],
                    relation["source"],
                    relation["target"],
                ),
            )

        con.commit()
        rows = con.execute(
            "SELECT id, kind, COALESCE(state, '') "
            "FROM sources ORDER BY id"
        ).fetchall()
        edges = con.execute(
            "SELECT relation_id, relation_type, source, target "
            "FROM relations ORDER BY relation_id"
        ).fetchall()
        fts = con.execute(
            "SELECT id FROM docs_fts "
            "WHERE docs_fts MATCH 'architecture' ORDER BY id"
        ).fetchall()
        return {
            "sources": [list(x) for x in rows],
            "relations": [list(x) for x in edges],
            "fts": [list(x) for x in fts],
        }
    finally:
        con.close()


def write_canonical_layout(
    root: Path,
    definition: str,
    state: dict[str, Any],
    spec_candidate: str,
) -> dict[str, Path]:
    knowledge = root / "project/knowledge"
    system = root / "project/system"
    governance = knowledge / "governance"
    evidence = knowledge / "evidence"
    instance = system / "instance"
    for directory in [governance, evidence, instance]:
        directory.mkdir(parents=True, exist_ok=True)

    definition_path = governance / "source_vault_workstream.md"
    state_path = instance / "source_vault_state.json"
    spec_path = governance / "specification_028.md"
    policy_path = instance / "policy.toml"
    relation_path = evidence / "relation.toml"

    definition_path.write_text(definition, encoding="utf-8")
    state_path.write_text(pretty_json(state), encoding="utf-8")
    spec_path.write_text(spec_candidate, encoding="utf-8")
    policy_path.write_text(
        'contract = "ads-instance-policy/1"\n'
        "contract_version = 1\n"
        'provider = "git"\n'
        'authority_mode = "current-continuity"\n',
        encoding="utf-8",
    )
    relation_path.write_text(
        relation_toml(
            "REL:SPEC-WORKSTREAM",
            "SPECIFICATION:028",
            state["workstream_id"],
            "informs",
        ),
        encoding="utf-8",
    )
    return {
        "definition": definition_path,
        "state": state_path,
        "spec": spec_path,
        "policy": policy_path,
        "relation": relation_path,
    }


def write_project_anchor(root: Path, paths: dict[str, Path]) -> Path:
    anchor = root / "project_anchor.json"
    locators = {
        key: str(path.relative_to(root)).replace("\\", "/")
        for key, path in paths.items()
        if key in {"definition", "state", "spec", "policy"}
    }
    anchor.write_text(
        pretty_json(
            {
                "contract": "project-anchor/1",
                "locators": locators,
            }
        ),
        encoding="utf-8",
    )
    return anchor


def recover_from_anchor(anchor_path: Path) -> dict[str, Any]:
    root = anchor_path.parent
    anchor = json.loads(anchor_path.read_text(encoding="utf-8"))
    required = {"definition", "state", "spec", "policy"}
    if set(anchor.get("locators", {})) != required:
        raise ProbeFailure("anchor locator set is incomplete")
    resolved = {
        key: root / rel
        for key, rel in anchor["locators"].items()
    }
    for key, path in resolved.items():
        if not path.exists():
            raise ProbeFailure(f"anchor locator unavailable: {key}:{path}")

    definition = parse_governed_markdown(
        resolved["definition"].read_text(encoding="utf-8")
    )
    specification = parse_governed_markdown(
        resolved["spec"].read_text(encoding="utf-8")
    )
    state = json.loads(resolved["state"].read_text(encoding="utf-8"))
    policy = tomllib.loads(
        resolved["policy"].read_text(encoding="utf-8")
    )
    if definition["classification"] != "governed":
        raise ProbeFailure("definition recovery failed")
    if specification["classification"] != "governed":
        raise ProbeFailure("specification recovery failed")
    validate_schema(state, WORKSTREAM_STATE_SCHEMA)
    return {
        "workstream_id": definition["metadata"]["id"],
        "state": state["state"],
        "specification": specification["metadata"]["id"],
        "authority_mode": policy["authority_mode"],
    }


def framework_schema(allowed_versions: list[int]) -> dict[str, Any]:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "required": [
            "contract",
            "contract_version",
            "provider",
            "authority_mode",
        ],
        "properties": {
            "contract": {"const": "ads-instance-policy/1"},
            "contract_version": {"enum": allowed_versions},
            "provider": {"type": "string"},
            "authority_mode": {"type": "string"},
        },
    }


def write_framework_source(
    root: Path,
    framework_version: int,
    allowed_versions: list[int],
) -> None:
    root.mkdir(parents=True, exist_ok=True)
    (root / "framework.json").write_text(
        pretty_json({"framework_version": framework_version}),
        encoding="utf-8",
    )
    (root / "policy.schema.json").write_text(
        pretty_json(framework_schema(allowed_versions)),
        encoding="utf-8",
    )
    (root / "parser_rules.json").write_text(
        pretty_json(
            {
                "format": "toml",
                "contract_field": "contract",
                "version_field": "contract_version",
            }
        ),
        encoding="utf-8",
    )


def refresh_framework(source: Path, live: Path) -> None:
    if live.exists():
        shutil.rmtree(live)
    shutil.copytree(source, live)


def validate_instance_with_framework(
    live_framework: Path,
    policy_path: Path,
) -> str:
    rules = json.loads(
        (live_framework / "parser_rules.json").read_text(encoding="utf-8")
    )
    if rules.get("format") != "toml":
        raise ProbeFailure("unsupported framework parser format")
    policy = tomllib.loads(policy_path.read_text(encoding="utf-8"))
    schema = json.loads(
        (live_framework / "policy.schema.json").read_text(encoding="utf-8")
    )
    try:
        Draft202012Validator(schema).validate(policy)
    except ValidationError:
        return "migration_required"
    return "valid"


def git_blob_sha256(commit: str, rel_path: str) -> str:
    data = git_bytes(ROOT, "show", f"{commit}:{rel_path}")
    return sha256_bytes(data)


def harness_binding(commit: str) -> dict[str, Any]:
    binding: dict[str, Any] = {
        "hash_basis": "GIT_BLOB_BYTES_AT_COMMIT",
        "commit": commit,
        "files": {},
    }
    for rel in HARNESS_PATHS:
        blob = git_bytes(ROOT, "show", f"{commit}:{rel}")
        working = (ROOT / rel).read_bytes()
        if normalize_newlines_bytes(working) != normalize_newlines_bytes(blob):
            raise ProbeFailure(
                f"working tree differs semantically from frozen blob: {rel}"
            )
        binding["files"][rel] = sha256_bytes(blob)
    return binding


def record_gate(
    results: list[dict[str, Any]],
    gate: str,
    fn: Callable[[], Any],
) -> None:
    try:
        details = fn()
        results.append(
            {"gate": gate, "status": "PASS", "details": details}
        )
    except Exception as exc:
        results.append(
            {
                "gate": gate,
                "status": "FAIL",
                "details": {
                    "error": f"{type(exc).__name__}: {exc}"
                },
            }
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--harness-commit", required=True)
    args = parser.parse_args()

    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    source_hashes = verify_real_source_hashes()
    binding = harness_binding(args.harness_commit)

    real_workstream_text = REAL_WORKSTREAM.read_text(encoding="utf-8")
    real_spec_text = REAL_SPEC.read_text(encoding="utf-8")
    definition, state, workstream_manifest, legacy_workstream = (
        convert_real_workstream(real_workstream_text)
    )
    spec_candidate, spec_meta, spec_manifest, legacy_spec = (
        convert_real_specification(real_spec_text)
    )

    artifacts = output / "artifacts"
    artifacts.mkdir()
    (artifacts / "source_vault_definition.md").write_text(
        definition, encoding="utf-8"
    )
    (artifacts / "source_vault_state.json").write_text(
        pretty_json(state), encoding="utf-8"
    )
    (artifacts / "source_vault_conversion_manifest.json").write_text(
        pretty_json(workstream_manifest), encoding="utf-8"
    )
    (artifacts / "specification_028_candidate.md").write_text(
        spec_candidate, encoding="utf-8"
    )
    (artifacts / "specification_028_conversion_manifest.json").write_text(
        pretty_json(spec_manifest), encoding="utf-8"
    )

    results: list[dict[str, Any]] = []
    amendment_results: list[dict[str, Any]] = []

    def g01():
        valid_meta = {
            "contract": "project-knowledge-carrier/1",
            "id": "TEST:1",
            "kind": "test",
            "authority": "canonical",
            "lifecycle": "active",
        }
        valid = (
            "# Test\n\n" + metadata_block(valid_meta) + "\n\nBody\n"
        )
        plain = "# Plain\n\nBody only.\n"
        about = (
            "# Metadata Format Guide\n\n"
            "This document explains the format.\n\n"
            + META_FENCE
            + '\ncontract = "project-knowledge-carrier/1"\n'
              'id = "EXAMPLE"\nkind = "example"\n'
              'authority = "canonical"\nlifecycle = "active"\n'
            + FENCE_END
            + "\n"
        )
        example = (
            "# Example Guide\n\nExample follows.\n\n"
            + META_EXAMPLE_FENCE
            + '\nid = "EXAMPLE"\n'
            + FENCE_END
            + "\n"
        )
        malformed = (
            "# Broken\n\n" + META_FENCE + "\nid = [\n"
            + FENCE_END + "\n"
        )
        wrong_position = (
            "# Wrong Place\n\nProse first.\n\n"
            + metadata_block(valid_meta)
            + "\n"
        )
        duplicate = (
            "# Duplicate\n\n"
            + metadata_block(valid_meta)
            + "\n\n"
            + metadata_block(valid_meta)
            + "\n"
        )
        non_h1 = "Title\n\n" + metadata_block(valid_meta) + "\n"

        cases = [
            ("valid", valid, "governed"),
            ("plain", plain, "plain"),
            ("about", about, "plain"),
            ("example", example, "plain"),
            ("malformed", malformed, "error"),
            ("wrong_position", wrong_position, "plain"),
            ("duplicate", duplicate, "error"),
            ("non_h1", non_h1, "plain"),
        ]
        observed: dict[str, str] = {}
        for name, text, expected in cases:
            got = parse_governed_markdown(text)["classification"]
            observed[name] = got
            if got != expected:
                raise ProbeFailure(
                    f"{name}: expected {expected}, got {got}"
                )
        return {"cases": observed, "count": len(cases)}

    record_gate(results, "G01", g01)

    def g02():
        base = {
            "contract": "project-knowledge-carrier/1",
            "id": "TIME:1",
            "kind": "test",
            "authority": "canonical",
            "lifecycle": "active",
        }
        native_values = {
            "date": "2026-09-23",
            "time": "12:30:00",
            "local_datetime": "2026-09-23T12:30:00",
            "offset_datetime": "2026-09-23T12:30:00+02:00",
        }
        observed: dict[str, str] = {}
        for name, literal in native_values.items():
            block = metadata_block(base)
            block = block[:-len(FENCE_END)]
            block += (
                "\n[extensions]\n"
                f"when = {literal}\n"
                + FENCE_END
            )
            text = "# Time\n\n" + block + "\n"
            actual = parse_governed_markdown(text)
            if actual["classification"] != "error":
                raise ProbeFailure(
                    f"native TOML {name} was not rejected"
                )
            observed[name] = "rejected"

            no_op = parse_governed_markdown(
                text,
                compat_checker=lambda _value: None,
            )
            if no_op["classification"] != "governed":
                raise ProbeFailure(
                    f"G02 is confounded for {name}; no-op compatibility "
                    "checker did not make carrier valid"
                )

        string_meta = copy.deepcopy(base)
        string_meta["extensions"] = {
            "when": "2026-09-23T12:30:00+02:00"
        }
        string_text = (
            "# Time\n\n" + metadata_block(string_meta) + "\n"
        )
        if (
            parse_governed_markdown(string_text)["classification"]
            != "governed"
        ):
            raise ProbeFailure("formatted timestamp string rejected")
        return {
            "native_types": observed,
            "string_equivalent": "accepted",
            "isolated_compatibility_checker": True,
        }

    record_gate(results, "G02", g02)

    def g03():
        parsed = parse_governed_markdown(
            "# Ordinary Note\n\nNo governed metadata is needed here.\n"
        )
        if parsed["classification"] != "plain":
            raise ProbeFailure(
                "plain Markdown was not accepted as non-governed"
            )
        return {"classification": "plain"}

    record_gate(results, "G03", g03)

    def g04():
        parsed = parse_governed_markdown(definition)
        if parsed["classification"] != "governed":
            raise ProbeFailure(
                "real workstream definition metadata did not parse"
            )
        if parsed["metadata"]["id"] != legacy_workstream["semantic_id"]:
            raise ProbeFailure("workstream identity changed")

        transition_values = [
            legacy_workstream["state"],
            legacy_workstream["pause_reason"],
            legacy_workstream["return_condition"],
            legacy_workstream["resume_target"],
            legacy_workstream["orientation_milestones"][0]["state"],
            legacy_workstream["orientation_milestones"][1]["state"],
        ]
        for value in transition_values:
            if value and value in definition:
                raise ProbeFailure(
                    f"transition-owned current fact leaked into definition: "
                    f"{value!r}"
                )

        with tempfile.TemporaryDirectory(
            prefix="pr8b01r2-g04-"
        ) as td:
            root = Path(td)
            canonical = root / "canonical"
            canonical.mkdir()
            (canonical / "definition.md").write_text(
                definition, encoding="utf-8"
            )
            (canonical / "state.json").write_text(
                pretty_json(state), encoding="utf-8"
            )
            pairing = discover_pairing_violations(canonical)

        if pairing["pairing_violations"] != 0:
            raise ProbeFailure(
                f"pairing violations: {pairing['violations']}"
            )
        if workstream_manifest["dropped_without_disposition"]:
            raise ProbeFailure(
                "workstream conversion dropped material without disposition"
            )
        if set(workstream_manifest["legacy_declaration_fields"]) != set(
            legacy_workstream
        ):
            raise ProbeFailure(
                "workstream declaration loss manifest is incomplete"
            )
        if len(parsed["metadata"].get("provenance", [])) != len(
            legacy_workstream["provenance"]
        ):
            raise ProbeFailure("workstream provenance was lost")
        if len(parsed["metadata"].get("declared_references", [])) != len(
            legacy_workstream["references"]
        ):
            raise ProbeFailure("workstream references were lost")
        if (
            state["expected_to_resume"]
            != legacy_workstream["expected_to_resume"]
        ):
            raise ProbeFailure("expected_to_resume meaning was lost")

        return {
            "removed_transition_facts": len(transition_values),
            "pairing_violations": pairing["pairing_violations"],
            "loss_manifest_complete": True,
            "provenance_preserved": len(
                legacy_workstream["provenance"]
            ),
            "references_preserved": len(
                legacy_workstream["references"]
            ),
        }

    record_gate(results, "G04", g04)

    def g05():
        with tempfile.TemporaryDirectory(
            prefix="pr8b01r2-g05-split-"
        ) as td:
            repo = Path(td)
            init_temp_repo(repo)
            definition_path = repo / "definition.md"
            state_path = repo / "state.json"
            definition_path.write_text(
                definition, encoding="utf-8"
            )
            state_path.write_text(
                pretty_json(state), encoding="utf-8"
            )
            commit_all(repo, "base")

            transition_state_file(
                state_path,
                lambda record: record.update(
                    {
                        "state": "ACTIVE",
                        "pause_reason": None,
                        "return_condition": None,
                    }
                ),
            )
            definition_diff = git(
                repo,
                "diff",
                "--",
                "definition.md",
            ).stdout
            state_diff = git(
                repo,
                "diff",
                "--",
                "state.json",
            ).stdout
            if definition_diff:
                raise ProbeFailure(
                    "routine split-state transition changed definition"
                )
            if not state_diff:
                raise ProbeFailure(
                    "routine split-state transition did not change state"
                )

        with tempfile.TemporaryDirectory(
            prefix="pr8b01r2-g05-colocated-"
        ) as td:
            repo = Path(td)
            init_temp_repo(repo)
            colocated_path = repo / "definition.md"
            colocated = (
                definition
                + "\n## Current control state\n\n"
                + FENCE_END
                + "json\n"
                + pretty_json(state)
                + FENCE_END
                + "\n"
            )
            colocated_path.write_text(
                colocated, encoding="utf-8"
            )
            commit_all(repo, "base")
            changed = colocated_path.read_text(encoding="utf-8")
            changed = changed.replace(
                '"revision": 1',
                '"revision": 2',
                1,
            ).replace(
                '"state": "PAUSED"',
                '"state": "ACTIVE"',
                1,
            )
            colocated_path.write_text(
                changed, encoding="utf-8"
            )
            negative_diff = git(
                repo,
                "diff",
                "--",
                "definition.md",
            ).stdout
            if not negative_diff:
                raise ProbeFailure(
                    "co-located negative control did not change definition"
                )

        return {
            "definition_bytes_modified": 0,
            "state_file_changed": True,
            "colocated_negative_control": "nonzero-definition-diff",
        }

    record_gate(results, "G05", g05)

    def g06():
        with tempfile.TemporaryDirectory(
            prefix="pr8b01r2-g06-"
        ) as td:
            path = Path(td) / "state.json"
            path.write_text(pretty_json(state), encoding="utf-8")
            base_sha = sha256_file(path)

            writer_a = copy.deepcopy(state)
            writer_a["revision"] += 1
            writer_a["state"] = "ACTIVE"
            writer_a["pause_reason"] = None
            writer_a["return_condition"] = None
            validate_ordinary_transition(state, writer_a)
            guarded_write(path, base_sha, writer_a)

            writer_b = copy.deepcopy(state)
            writer_b["revision"] += 1
            writer_b["resume_target"] = "SOURCE-VAULT:OTHER"
            validate_ordinary_transition(state, writer_b)
            rejected = expect_reject(
                lambda: guarded_write(path, base_sha, writer_b),
                "stale writer",
            )
            return {
                "stale_writer": rejected,
                "base_sha": base_sha,
            }

    record_gate(results, "G06", g06)

    def _branch_merge_experiment(
        include_revision_bump: bool,
    ) -> dict[str, Any]:
        with tempfile.TemporaryDirectory(
            prefix="pr8b01r2-g07-"
        ) as td:
            repo = Path(td)
            init_temp_repo(repo)
            path = repo / "state.json"
            path.write_text(pretty_json(state), encoding="utf-8")
            commit_all(repo, "base")
            base_branch = (
                git(repo, "branch", "--show-current").stdout.strip()
                or "master"
            )

            git(repo, "checkout", "-b", "branch-a")
            a = copy.deepcopy(state)
            if include_revision_bump:
                a["revision"] += 1
            a["state"] = "ACTIVE"
            path.write_text(pretty_json(a), encoding="utf-8")
            commit_all(repo, "branch a")

            git(repo, "checkout", base_branch)
            git(repo, "checkout", "-b", "branch-b")
            b = copy.deepcopy(state)
            if include_revision_bump:
                b["revision"] += 1
            b["milestones"]["SOURCE-VAULT:INGESTION"] = "IN_PROGRESS"
            path.write_text(pretty_json(b), encoding="utf-8")
            commit_all(repo, "branch b")

            merge = git(
                repo,
                "merge",
                "branch-a",
                check=False,
            )
            result: dict[str, Any] = {
                "merge_returncode": merge.returncode,
                "status": git(repo, "status", "--porcelain").stdout,
            }
            if merge.returncode == 0:
                result["merged_record"] = json.loads(
                    path.read_text(encoding="utf-8")
                )
            else:
                git(repo, "merge", "--abort")
            return result

    def g07():
        protected = _branch_merge_experiment(True)
        if protected["merge_returncode"] == 0:
            raise ProbeFailure(
                "revision-bumped branches merged cleanly"
            )
        if "UU state.json" not in protected["status"]:
            raise ProbeFailure(
                "expected state.json conflict was not surfaced"
            )

        control = _branch_merge_experiment(False)
        if control["merge_returncode"] != 0:
            raise ProbeFailure(
                "no-revision control did not merge cleanly"
            )
        merged = control["merged_record"]
        if (
            merged["state"] != "ACTIVE"
            or merged["pause_reason"] is None
        ):
            raise ProbeFailure(
                "control arm did not demonstrate inconsistent clean merge"
            )
        return {
            "revision_bump": "conflict",
            "no_revision_control": "clean-merge",
            "control_hazard": {
                "state": merged["state"],
                "pause_reason_present": merged["pause_reason"] is not None,
                "ingestion": merged["milestones"][
                    "SOURCE-VAULT:INGESTION"
                ],
            },
        }

    record_gate(results, "G07", g07)

    def _build_valid_merge_history() -> dict[str, Any]:
        td = tempfile.TemporaryDirectory(
            prefix="pr8b01r2-g08-valid-"
        )
        repo = Path(td.name)
        init_temp_repo(repo)
        path = repo / "state.json"
        path.write_text(pretty_json(state), encoding="utf-8")
        base = commit_all(repo, "rev1")
        base_branch = (
            git(repo, "branch", "--show-current").stdout.strip()
            or "master"
        )

        git(repo, "checkout", "-b", "branch-a")
        a = copy.deepcopy(state)
        a["revision"] = 2
        a["state"] = "ACTIVE"
        a["pause_reason"] = None
        a["return_condition"] = None
        validate_ordinary_transition(state, a)
        path.write_text(pretty_json(a), encoding="utf-8")
        a_commit = commit_all(repo, "branch a rev2")

        git(repo, "checkout", base_branch)
        git(repo, "checkout", "-b", "branch-b")
        b = copy.deepcopy(state)
        b["revision"] = 2
        b["milestones"]["SOURCE-VAULT:INGESTION"] = "IN_PROGRESS"
        validate_ordinary_transition(state, b)
        path.write_text(pretty_json(b), encoding="utf-8")
        b_commit = commit_all(repo, "branch b rev2")

        merge = git(repo, "merge", "branch-a", check=False)
        if merge.returncode == 0:
            td.cleanup()
            raise ProbeFailure("expected merge conflict not produced")

        resolved = copy.deepcopy(a)
        resolved["revision"] = 3
        resolved["milestones"]["SOURCE-VAULT:INGESTION"] = "IN_PROGRESS"
        validate_merge_resolution([a, b], resolved)
        path.write_text(pretty_json(resolved), encoding="utf-8")
        git(repo, "add", "state.json")
        git(repo, "commit", "-m", "merge resolution rev3")
        merge_commit = git(repo, "rev-parse", "HEAD").stdout.strip()

        validation = validate_committed_state_history(
            repo, "state.json"
        )
        return {
            "tempdir": td,
            "repo": repo,
            "base": base,
            "a_commit": a_commit,
            "b_commit": b_commit,
            "merge_commit": merge_commit,
            "validation": validation,
        }

    def g08():
        negative_base = copy.deepcopy(state)
        negative_base["revision"] = 2
        negatives = exercise_transition_negative_checks(
            validate_ordinary_transition,
            negative_base,
        )

        no_op_detected = False
        try:
            exercise_transition_negative_checks(
                lambda _previous, _new: None,
                negative_base,
            )
        except ProbeFailure:
            no_op_detected = True
        if not no_op_detected:
            raise ProbeFailure(
                "no-op transition validator escaped negative controls"
            )

        parent_a = copy.deepcopy(state)
        parent_a["revision"] = 2
        parent_a["state"] = "ACTIVE"
        parent_a["pause_reason"] = None
        parent_a["return_condition"] = None
        parent_b = copy.deepcopy(state)
        parent_b["revision"] = 2
        parent_b["milestones"]["SOURCE-VAULT:INGESTION"] = "IN_PROGRESS"
        invalid_merge = copy.deepcopy(parent_a)
        invalid_merge["revision"] = 2
        merge_negative = expect_reject(
            lambda: validate_merge_resolution(
                [parent_a, parent_b],
                invalid_merge,
            ),
            "invalid merge revision",
        )

        no_op_merge_detected = False
        try:
            expect_reject(
                lambda: (lambda _parents, _resolved: None)(
                    [parent_a, parent_b],
                    invalid_merge,
                ),
                "no-op merge validator",
            )
        except ProbeFailure:
            no_op_merge_detected = True
        if not no_op_merge_detected:
            raise ProbeFailure(
                "no-op merge validator escaped negative control"
            )

        valid_history = _build_valid_merge_history()
        try:
            valid_history_result = valid_history["validation"]
        finally:
            valid_history["tempdir"].cleanup()

        with tempfile.TemporaryDirectory(
            prefix="pr8b01r2-g08-corrupt-"
        ) as td:
            repo = Path(td)
            init_temp_repo(repo)
            path = repo / "state.json"
            path.write_text(pretty_json(state), encoding="utf-8")
            commit_all(repo, "rev1")
            corrupted = copy.deepcopy(state)
            corrupted["state"] = "ACTIVE"
            corrupted["pause_reason"] = None
            corrupted["return_condition"] = None
            path.write_text(pretty_json(corrupted), encoding="utf-8")
            commit_all(repo, "semantic change without revision bump")
            corrupt_rejected = expect_reject(
                lambda: validate_committed_state_history(
                    repo, "state.json"
                ),
                "corrupted committed history",
            )

        return {
            "negative_checks": negatives,
            "invalid_merge": merge_negative,
            "no_op_transition_validator_detected": no_op_detected,
            "no_op_merge_validator_detected": no_op_merge_detected,
            "valid_committed_history": valid_history_result,
            "corrupted_history": corrupt_rejected,
        }

    record_gate(results, "G08", g08)

    def g09():
        with tempfile.TemporaryDirectory(
            prefix="pr8b01r2-g09-"
        ) as td:
            root = Path(td)
            homes = [
                root / "knowledge/governance",
                root / "system/instance",
                root / "knowledge/evidence",
            ]
            for idx in range(12):
                home = homes[idx % len(homes)]
                home.mkdir(parents=True, exist_ok=True)
                (home / f"relation_{idx + 1}.toml").write_text(
                    relation_toml(
                        f"REL:{idx + 1}",
                        f"S:{idx + 1}",
                        f"T:{idx + 1}",
                    ),
                    encoding="utf-8",
                )

            found = discover_relations(root)
            if len(found) != 12:
                raise ProbeFailure(
                    f"expected 12 discovered relations, got {len(found)}"
                )
            if rc3_admission(len(found) - 1) != "ADMIT":
                raise ProbeFailure(
                    "12th record should be admitted before bound is reached"
                )
            if rc3_admission(len(found)) != "REVIEW_REQUIRED":
                raise ProbeFailure(
                    "attempted 13th record did not trigger review"
                )

            malformed = homes[0] / "malformed.toml"
            malformed.write_text(
                'kind = "standalone-relation"\nrelation_id = [\n',
                encoding="utf-8",
            )
            malformed_rejected = expect_reject(
                lambda: discover_relations(root),
                "malformed standalone relation",
            )
            return {
                "discovered_repository_wide": len(found),
                "review_bound": RC3_REVIEW_BOUND,
                "attempted_13th": "REVIEW_REQUIRED",
                "malformed_relation": malformed_rejected,
            }

    record_gate(results, "G09", g09)


    def review_capture(
        capture_path: Path,
        review_path: Path,
    ) -> None:
        capture = json.loads(capture_path.read_text(encoding="utf-8"))
        if capture.get("authority") != "candidate":
            raise ProbeFailure("capture is unexpectedly authoritative")
        review_path.write_text(
            "# Capture Review\n\n"
            f"Capture: {capture['capture_id']}\n\n"
            f"Receipt: {capture['receipt_id']}\n\n"
            f"Interpretation: {capture['interpretation']}\n",
            encoding="utf-8",
        )

    def promote_capture(
        capture_path: Path,
        review_path: Path,
        target_path: Path,
    ) -> None:
        capture = json.loads(capture_path.read_text(encoding="utf-8"))
        review = review_path.read_text(encoding="utf-8")
        if capture["capture_id"] not in review:
            raise ProbeFailure("review does not bind capture")
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(
            "# Trigger Vocabulary\n\n"
            f"Source capture: {capture['capture_id']}\n\n"
            f"Source receipt: {capture['receipt_id']}\n\n"
            f"Accepted interpretation: {capture['interpretation']}\n",
            encoding="utf-8",
        )

    def g10():
        with tempfile.TemporaryDirectory(
            prefix="pr8b01r2-g10-"
        ) as td:
            root = Path(td)
            receipt = make_receipt("activation-miss", "surfaced")
            validate_public_receipt(receipt)
            receipt_path = root / receipt_locator(receipt)
            receipt_path.parent.mkdir(parents=True, exist_ok=True)
            receipt_path.write_text(
                pretty_json(receipt), encoding="utf-8"
            )

            capture = {
                "capture_id": "CAPTURE:MACHINE:1",
                "kind": "machine-capture",
                "authority": "candidate",
                "receipt_id": receipt["receipt_id"],
                "interpretation": "Potential trigger-vocabulary gap.",
            }
            capture_path = root / "captures/capture.json"
            capture_path.parent.mkdir(parents=True, exist_ok=True)
            capture_path.write_text(
                pretty_json(capture), encoding="utf-8"
            )
            capture_before = capture_path.read_bytes()
            receipt_before = receipt_path.read_bytes()

            review_path = root / "reviews/capture.md"
            review_path.parent.mkdir(parents=True, exist_ok=True)
            review_capture(capture_path, review_path)

            target_path = root / "knowledge/governance/trigger_vocabulary.md"
            promote_capture(capture_path, review_path, target_path)

            if capture_path.read_bytes() != capture_before:
                raise ProbeFailure(
                    "machine capture changed during review/promotion"
                )
            if receipt_path.read_bytes() != receipt_before:
                raise ProbeFailure(
                    "receipt changed during review/promotion"
                )
            target_text = target_path.read_text(encoding="utf-8")
            if receipt["payload"]["result"] in target_text:
                raise ProbeFailure(
                    "receipt event payload duplicated into canonical target"
                )
            persisted_capture = json.loads(
                capture_path.read_text(encoding="utf-8")
            )
            if persisted_capture["authority"] != "candidate":
                raise ProbeFailure(
                    "capture authority was flipped in place"
                )
            return {
                "capture_bytes_unchanged": True,
                "receipt_bytes_unchanged": True,
                "human_review_separate": review_path.exists(),
                "canonical_target_written": target_path.exists(),
                "capture_authority": persisted_capture["authority"],
            }

    record_gate(results, "G10", g10)

    def g11():
        receipt_a = make_receipt("transition", "A")
        receipt_b = make_receipt("transition", "B")
        locator_a = receipt_locator(receipt_a)
        locator_a2 = receipt_locator(copy.deepcopy(receipt_a))
        locator_b = receipt_locator(receipt_b)
        if locator_a != locator_a2:
            raise ProbeFailure(
                "identical receipt did not produce identical locator"
            )
        if locator_a == locator_b:
            raise ProbeFailure("distinct receipt contents collided")

        with tempfile.TemporaryDirectory(
            prefix="pr8b01r2-g11-"
        ) as td:
            repo = Path(td)
            init_temp_repo(repo)
            (repo / ".keep").write_text("base\n", encoding="utf-8")
            commit_all(repo, "base")
            base_branch = (
                git(repo, "branch", "--show-current").stdout.strip()
                or "master"
            )

            git(repo, "checkout", "-b", "receipt-a")
            pa = repo / locator_a
            pa.parent.mkdir(parents=True, exist_ok=True)
            pa.write_text(pretty_json(receipt_a), encoding="utf-8")
            commit_all(repo, "receipt a")

            git(repo, "checkout", base_branch)
            git(repo, "checkout", "-b", "receipt-b")
            pb = repo / locator_b
            pb.parent.mkdir(parents=True, exist_ok=True)
            pb.write_text(pretty_json(receipt_b), encoding="utf-8")
            commit_all(repo, "receipt b")

            merge = git(repo, "merge", "receipt-a", check=False)
            if merge.returncode != 0:
                raise ProbeFailure(
                    "distinct receipt files did not merge cleanly"
                )
            other_before = pb.read_bytes()
            pa.unlink()
            if pb.read_bytes() != other_before:
                raise ProbeFailure(
                    "deleting one receipt rewrote another"
                )
        return {
            "locator_a": locator_a,
            "locator_b": locator_b,
            "parallel_merge": "clean",
            "retention_isolated": True,
            "claim_scope":
                "individual-content-addressed-JSON-behaves-as-designed",
        }

    record_gate(results, "G11", g11)

    def g12():
        public_receipt = make_receipt("qualification", "PASS")
        validate_public_receipt(public_receipt)

        private_field = copy.deepcopy(public_receipt)
        private_field["payload"]["private_locator"] = (
            "PRIVATE_ONLY://synthetic-secret"
        )
        private_field_result = expect_reject(
            lambda: validate_public_receipt(private_field),
            "private-only field",
        )

        private_sentinel = copy.deepcopy(public_receipt)
        private_sentinel["payload"]["summary"] = (
            "PRIVATE_ONLY://synthetic-secret"
        )
        private_sentinel_result = expect_reject(
            lambda: validate_public_receipt(private_sentinel),
            "private-only sentinel",
        )
        return {
            "public_safe": "accepted",
            "private_field": private_field_result,
            "private_sentinel": private_sentinel_result,
        }

    record_gate(results, "G12", g12)

    def g13():
        parsed = parse_governed_markdown(spec_candidate)
        if parsed["classification"] != "governed":
            raise ProbeFailure(
                "converted Specification 028 did not parse as governed"
            )
        if parsed["metadata"]["id"] != legacy_spec["semantic_id"]:
            raise ProbeFailure("Specification identity changed")
        if parsed["metadata"]["authority"] != legacy_spec["authority_class"]:
            raise ProbeFailure("Specification authority role changed")

        _, legacy_block = extract_legacy_json_declaration(real_spec_text)
        original_non_metadata = real_spec_text.replace(
            legacy_block, "", 1
        )
        converted_non_metadata = strip_governed_metadata(
            spec_candidate
        )
        if normalize_blank_runs(original_non_metadata) != normalize_blank_runs(
            converted_non_metadata
        ):
            raise ProbeFailure(
                "non-metadata Specification 028 content changed"
            )

        status = _parse_header_value(real_spec_text, "Status")
        authority_clause = _parse_header_value(
            real_spec_text, "Authority"
        )
        declared_line = _parse_header_value(
            real_spec_text, "Declared references"
        )
        header_refs = set(
            re.findall(r"\x60([^\x60]+)\x60", declared_line)
        )
        expected_refs = header_refs | set(legacy_spec["references"])
        actual_refs = set(
            parsed["metadata"].get("declared_references", [])
        )
        if actual_refs != expected_refs:
            raise ProbeFailure(
                "Specification declared references were not fully mapped"
            )
        if parsed["metadata"].get("provenance") != legacy_spec["provenance"]:
            raise ProbeFailure("Specification provenance changed")
        if status not in spec_candidate:
            raise ProbeFailure("Specification status header was lost")
        if authority_clause not in spec_candidate:
            raise ProbeFailure(
                "Specification governing authority clause was lost"
            )
        if parsed["metadata"]["lifecycle"] != "frozen":
            raise ProbeFailure(
                "FROZEN status was not explicitly mapped to frozen lifecycle"
            )
        if spec_manifest["dropped_without_disposition"]:
            raise ProbeFailure(
                "Specification conversion dropped material silently"
            )
        if set(spec_manifest["legacy_declaration_fields"]) != set(
            legacy_spec
        ):
            raise ProbeFailure(
                "Specification loss manifest is incomplete"
            )
        return {
            "id": parsed["metadata"]["id"],
            "authority": parsed["metadata"]["authority"],
            "lifecycle": parsed["metadata"]["lifecycle"],
            "non_metadata_content_preserved": True,
            "declared_reference_count": len(actual_refs),
            "provenance_count": len(
                parsed["metadata"].get("provenance", [])
            ),
            "loss_manifest_complete": True,
        }

    record_gate(results, "G13", g13)

    def g14():
        with tempfile.TemporaryDirectory(
            prefix="pr8b01r2-g14-"
        ) as td:
            root = Path(td)
            definition_path = root / "definition.md"
            state_path = root / "state.json"
            definition_path.write_text(
                definition, encoding="utf-8"
            )
            state_path.write_text(
                pretty_json(state), encoding="utf-8"
            )

            current = build_current_json(
                definition_path, state_path, state
            )
            first = pretty_json(current)
            second = pretty_json(
                build_current_json(
                    definition_path, state_path, state
                )
            )
            if first != second:
                raise ProbeFailure(
                    "unchanged sources did not reproduce current.json"
                )
            if not current.get("derived") or current.get("authoritative"):
                raise ProbeFailure(
                    "current.json role is not derived/non-authoritative"
                )
            if not current_json_is_fresh(current, root):
                raise ProbeFailure("fresh current.json failed")

            changed = copy.deepcopy(state)
            changed["revision"] += 1
            changed["state"] = "ACTIVE"
            changed["pause_reason"] = None
            changed["return_condition"] = None
            validate_ordinary_transition(state, changed)
            state_path.write_text(
                pretty_json(changed), encoding="utf-8"
            )
            if current_json_is_fresh(current, root):
                raise ProbeFailure(
                    "stale state did not invalidate current.json"
                )
            listed_revision = [
                x["revision"]
                for x in current["sources"]
                if x["role"] == "state"
            ][0]
            if listed_revision == changed["revision"]:
                raise ProbeFailure(
                    "revision-level stale comparison did not differ"
                )

            state_path.write_text(
                pretty_json(state), encoding="utf-8"
            )
            current = build_current_json(
                definition_path, state_path, state
            )
            definition_path.write_text(
                definition + "\nAdditional durable note.\n",
                encoding="utf-8",
            )
            if current_json_is_fresh(current, root):
                raise ProbeFailure(
                    "revisionless definition hash drift was not detected"
                )

            (artifacts / "current.json").write_text(
                pretty_json(current), encoding="utf-8"
            )
            return {
                "deterministic": True,
                "state_staleness_detected": True,
                "definition_hash_staleness_detected": True,
                "tool_less_revision_comparison_scope": "revisioned-state-only",
                "cold_start_usefulness": "not-a-blocking-claim",
            }

    record_gate(results, "G14", g14)

    def g15():
        with tempfile.TemporaryDirectory(
            prefix="pr8b01r2-g15-"
        ) as td:
            root = Path(td)
            canonical = root / "canonical"
            paths = write_canonical_layout(
                canonical,
                definition,
                state,
                spec_candidate,
            )
            db_path = root / "index.sqlite"
            first = build_sqlite_index_from_disk(
                db_path, canonical
            )
            if not db_path.exists():
                raise ProbeFailure("SQLite index was not created")
            db_path.unlink()
            second = build_sqlite_index_from_disk(
                db_path, canonical
            )
            if first != second:
                raise ProbeFailure(
                    "disk-driven SQLite rebuild changed semantic rows"
                )
            fts_ids = {row[0] for row in first["fts"]}
            if "SPECIFICATION:028" not in fts_ids:
                raise ProbeFailure(
                    "FTS did not return real Specification 028"
                )
            if not first["relations"]:
                raise ProbeFailure(
                    "disk-discovered relation did not reach SQLite"
                )
            (artifacts / "sqlite_semantic_rows.json").write_text(
                pretty_json(first), encoding="utf-8"
            )
            return {
                "rebuild_equivalent": True,
                "canonical_files_reread": True,
                "fts_ids": sorted(fts_ids),
                "edge_count": len(first["relations"]),
                "relation_path": str(paths["relation"].name),
            }

    record_gate(results, "G15", g15)

    def g16():
        with tempfile.TemporaryDirectory(
            prefix="pr8b01r2-g16-"
        ) as td:
            root = Path(td)
            paths = write_canonical_layout(
                root,
                definition,
                state,
                spec_candidate,
            )
            anchor = write_project_anchor(root, paths)

            generated = root / "project/system/generated"
            generated.mkdir(parents=True, exist_ok=True)
            current_path = generated / "current.json"
            current_path.write_text(
                pretty_json(
                    build_current_json(
                        paths["definition"],
                        paths["state"],
                        state,
                    )
                ),
                encoding="utf-8",
            )
            db_path = generated / "query.sqlite"
            build_sqlite_index_from_disk(
                db_path, root / "project"
            )
            if not current_path.exists() or not db_path.exists():
                raise ProbeFailure("derivatives were not materialized")

            shutil.rmtree(generated)
            recovered = recover_from_anchor(anchor)
            expected = {
                "workstream_id": "WS-SOURCE-VAULT-BOOTSTRAP",
                "state": "PAUSED",
                "specification": "SPECIFICATION:028",
                "authority_mode": "current-continuity",
            }
            if recovered != expected:
                raise ProbeFailure(
                    f"break-glass recovery mismatch: {recovered}"
                )

            broken_anchor = root / "broken_anchor.json"
            broken = json.loads(anchor.read_text(encoding="utf-8"))
            broken["locators"]["definition"] = (
                "project/system/generated/current.json"
            )
            broken_anchor.write_text(
                pretty_json(broken), encoding="utf-8"
            )
            failure = expect_reject(
                lambda: recover_from_anchor(broken_anchor),
                "generated-only anchor recovery",
            )
            return {
                "derivatives_materialized_then_deleted": True,
                "recovered": recovered,
                "generated_only_negative_control": failure,
            }

    record_gate(results, "G16", g16)

    def g17():
        with tempfile.TemporaryDirectory(
            prefix="pr8b01r2-g17-"
        ) as td:
            root = Path(td)
            framework_v2 = root / "framework_v2"
            framework_v3 = root / "framework_v3"
            live = root / "framework_live"
            instance = root / "instance"
            instance.mkdir()
            policy_path = instance / "policy.toml"
            state_path = instance / "state.json"
            policy_path.write_text(
                'contract = "ads-instance-policy/1"\n'
                "contract_version = 1\n"
                'provider = "git"\n'
                'authority_mode = "current-continuity"\n',
                encoding="utf-8",
            )
            state_path.write_text(
                pretty_json(state), encoding="utf-8"
            )
            policy_before = policy_path.read_bytes()
            state_before = state_path.read_bytes()

            write_framework_source(
                framework_v2,
                framework_version=2,
                allowed_versions=[1, 2],
            )
            write_framework_source(
                framework_v3,
                framework_version=3,
                allowed_versions=[2],
            )

            refresh_framework(framework_v2, live)
            compatible = validate_instance_with_framework(
                live, policy_path
            )
            if compatible != "valid":
                raise ProbeFailure(
                    "compatible framework refresh did not validate"
                )
            if (
                policy_path.read_bytes() != policy_before
                or state_path.read_bytes() != state_before
            ):
                raise ProbeFailure(
                    "compatible framework refresh overwrote instance"
                )

            refresh_framework(framework_v3, live)
            incompatible = validate_instance_with_framework(
                live, policy_path
            )
            if incompatible != "migration_required":
                raise ProbeFailure(
                    "incompatible refresh did not produce migration_required"
                )
            if (
                policy_path.read_bytes() != policy_before
                or state_path.read_bytes() != state_before
            ):
                raise ProbeFailure(
                    "incompatible framework refresh overwrote instance"
                )
            return {
                "framework_files_replaced": [
                    "framework.json",
                    "policy.schema.json",
                    "parser_rules.json",
                ],
                "compatible_refresh": compatible,
                "incompatible_refresh": incompatible,
                "instance_bytes_unchanged": True,
            }

    record_gate(results, "G17", g17)

    def g18():
        with tempfile.TemporaryDirectory(
            prefix="pr8b01r2-g18-transition-"
        ) as td:
            repo = Path(td)
            init_temp_repo(repo)
            definition_path = repo / "definition.md"
            state_path = repo / "state.json"
            definition_path.write_text(
                definition, encoding="utf-8"
            )
            state_path.write_text(
                pretty_json(state), encoding="utf-8"
            )
            commit_all(repo, "base")
            transition_state_file(
                state_path,
                lambda record: record.update(
                    {
                        "state": "ACTIVE",
                        "pause_reason": None,
                        "return_condition": None,
                    }
                ),
            )
            human_diff = git(
                repo, "diff", "--", "definition.md"
            ).stdout
            if human_diff:
                raise ProbeFailure(
                    "routine transition produced human-definition diff"
                )

        with tempfile.TemporaryDirectory(
            prefix="pr8b01r2-g18-meta-"
        ) as td:
            repo = Path(td)
            init_temp_repo(repo)
            path = repo / "definition.md"
            path.write_text(definition, encoding="utf-8")
            commit_all(repo, "base")
            parsed = parse_governed_markdown(definition)
            changed_meta = copy.deepcopy(parsed["metadata"])
            changed_meta["lifecycle"] = "superseded"
            lines = parsed["normalized_text"].split("\n")
            changed_lines = (
                lines[: parsed["metadata_start"]]
                + metadata_block(changed_meta).splitlines()
                + lines[parsed["metadata_end"] + 1 :]
            )
            changed_definition = "\n".join(changed_lines)
            path.write_text(
                changed_definition, encoding="utf-8"
            )
            diff = git(repo, "diff", "--", "definition.md").stdout
            if not diff:
                raise ProbeFailure("metadata-only change produced no diff")
            if normalize_blank_runs(
                strip_governed_metadata(definition)
            ) != normalize_blank_runs(
                strip_governed_metadata(changed_definition)
            ):
                raise ProbeFailure(
                    "metadata-only change modified human body"
                )

        with tempfile.TemporaryDirectory(
            prefix="pr8b01r2-g18-receipt-"
        ) as td:
            repo = Path(td)
            init_temp_repo(repo)
            (repo / ".keep").write_text("base\n", encoding="utf-8")
            commit_all(repo, "base")
            receipt = make_receipt("review-quality", "PASS")
            locator = receipt_locator(receipt)
            receipt_path = repo / locator
            receipt_path.parent.mkdir(parents=True, exist_ok=True)
            receipt_path.write_text(
                pretty_json(receipt), encoding="utf-8"
            )
            git(repo, "add", "-N", locator)
            name_status = git(
                repo, "diff", "--name-status"
            ).stdout.strip().splitlines()
            if name_status != [f"A\t{locator}"]:
                raise ProbeFailure(
                    f"receipt Git diff shape unexpected: {name_status}"
                )

        with tempfile.TemporaryDirectory(
            prefix="pr8b01r2-g18-spec-"
        ) as td:
            repo = Path(td)
            init_temp_repo(repo)
            spec_path = repo / "spec.md"
            spec_path.write_text(
                real_spec_text, encoding="utf-8"
            )
            commit_all(repo, "legacy")
            spec_path.write_text(
                spec_candidate, encoding="utf-8"
            )
            spec_diff = git(
                repo, "diff", "--", "spec.md"
            ).stdout
            if META_FENCE not in spec_diff:
                raise ProbeFailure(
                    "visible metadata did not appear in Git diff"
                )

        return {
            "routine_human_definition_diff_bytes": 0,
            "metadata_change": "git-diffed-body-preserved",
            "receipt_change": "one-new-json-file",
            "spec_metadata": "visible-in-git-diff",
        }

    record_gate(results, "G18", g18)

    def am1_g1():
        meta = {
            "contract": "project-knowledge-carrier/1",
            "id": "AM1:1",
            "kind": "test",
            "authority": "canonical",
            "lifecycle": "active",
        }
        block = metadata_block(meta)
        cases = {
            "bom": "\ufeff# Governed\n\n" + block + "\n",
            "leading_blank": "\n# Governed\n\n" + block + "\n",
            "setext": "Governed\n========\n\n" + block + "\n",
        }
        observed: dict[str, str] = {}
        for name, text in cases.items():
            classification = parse_governed_markdown(text)[
                "classification"
            ]
            observed[name] = classification
            if classification == "plain":
                raise ProbeFailure(
                    f"{name} silently became plain"
                )

        indented = (
            "# Indented\n\n    " + META_FENCE
            + '\n    id = "NOT-METADATA"\n    '
            + FENCE_END
            + "\n"
        )
        if (
            parse_governed_markdown(indented)["classification"]
            != "plain"
        ):
            raise ProbeFailure(
                "indented pseudo-fence became governing metadata"
            )

        body_example = (
            "# Guide\n\nProse first.\n\n"
            + META_EXAMPLE_FENCE
            + '\nid = "EXAMPLE"\n'
            + FENCE_END
            + "\n"
        )
        if (
            parse_governed_markdown(body_example)["classification"]
            != "plain"
        ):
            raise ProbeFailure(
                "body example became governing metadata"
            )
        return {
            "intended_governed_cases": observed,
            "indented_pseudo_fence": "plain",
            "body_example": "plain",
        }

    record_gate(amendment_results, "AM1-G1", am1_g1)

    def am2_g1():
        history = _build_valid_merge_history()
        try:
            valid = history["validation"]
        finally:
            history["tempdir"].cleanup()

        with tempfile.TemporaryDirectory(
            prefix="pr8b01r2-am2-corrupt-"
        ) as td:
            repo = Path(td)
            init_temp_repo(repo)
            path = repo / "state.json"
            path.write_text(pretty_json(state), encoding="utf-8")
            commit_all(repo, "rev1")
            skipped = copy.deepcopy(state)
            skipped["revision"] = 3
            skipped["state"] = "ACTIVE"
            skipped["pause_reason"] = None
            skipped["return_condition"] = None
            path.write_text(
                pretty_json(skipped), encoding="utf-8"
            )
            commit_all(repo, "skipped revision")
            rejected = expect_reject(
                lambda: validate_committed_state_history(
                    repo, "state.json"
                ),
                "skipped committed revision",
            )
        return {
            "valid_merge_history": valid,
            "skipped_history": rejected,
            "history_validation_required": True,
        }

    record_gate(amendment_results, "AM2-G1", am2_g1)

    blocking_pass = (
        len(results) == 18
        and all(item["status"] == "PASS" for item in results)
    )
    amendments_pass = (
        len(amendment_results) == 2
        and all(
            item["status"] == "PASS"
            for item in amendment_results
        )
    )
    overall = (
        "PASS"
        if blocking_pass and amendments_pass
        else "AMEND_REQUIRED"
    )

    payload = {
        "probe": "P-R8B-01-R2",
        "protocol": "Research 266",
        "original_threshold_basis": "Research 263",
        "candidate": "WMR-H V0.3",
        "harness_binding": binding,
        "source_hashes": source_hashes,
        "blocking_gate_count": 18,
        "amendment_gate_count": 2,
        "overall": overall,
        "blocking_gates": results,
        "amendment_gates": amendment_results,
    }
    (output / "result.json").write_text(
        pretty_json(payload), encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "probe": payload["probe"],
                "overall": overall,
                "blocking_passed": sum(
                    x["status"] == "PASS" for x in results
                ),
                "blocking_total": len(results),
                "amendment_passed": sum(
                    x["status"] == "PASS"
                    for x in amendment_results
                ),
                "amendment_total": len(amendment_results),
            },
            indent=2,
        )
    )
    return 0 if overall == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
