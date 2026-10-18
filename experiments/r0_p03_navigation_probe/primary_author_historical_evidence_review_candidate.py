"""Exact-Git, non-scored inventory of missing R0-P03 author source evidence.

The 406-file source-window remains untouched. All records here are REVIEW_ONLY
or NON_TEXT_UNSUPPORTED, never author-admitted merely due to a clean lexical
screen. No records' content is packaged for authoring, and no tasks or gold
are generated. This prevents a repository-scale omission from being 'fixed'
by simply attaching prior scoring and comparator-design source material.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys

from experiments.r0_p03_navigation_probe import (
    primary_author_frontend_expansion_candidate as expanded,
)

ID = "R0_P03_HISTORICAL_EVIDENCE_ADMISSION_REVIEW_V1"
ROOTS = (
    "docs/checkpoints",
    "docs/research",
    "docs/local_execution/validation",
    "scripts",
    "tests",
    "schemas",
)
TEXT_SUFFIXES = frozenset({
    ".md", ".json", ".jsonl", ".py", ".ts", ".tsx", ".js", ".jsx",
    ".sql", ".toml", ".yaml", ".yml", ".txt", ".html", ".css",
    ".mako", ".ps1", ".sh",
})
FLAGS = {
    "R0_P03_DESIGN": re.compile(
        r"R0[-_ ]?P0?3|(?:research\s+513|research\s+55[6-9])\b", re.I,
    ),
    "LEGACY_W5_REFERENCE": re.compile(
        r"(?:research\s+217|navigation_scenarios_v02|"
        r"must[_ -]?retrieve|must[_ -]?not[_ -]?retrieve)\b", re.I,
    ),
    "EXPLICIT_ARM_COMPARISON": re.compile(
        r"(?:\bB[0-4]\s*[-\u2013]\s*B[0-4]\b|"
        r"\bB0[ -]?(?:B1|B4)\b|"
        r"gold[_ -]?(?:answer|label|key))", re.I,
    ),
}
DIRECT_PATH = re.compile(
    r"(?:^|[/_])(?:r0[_-]?p0?3|navigation_scenarios_v02|"
    r"corpus_annotations_v02)(?:[_./-]|$)", re.I,
)
OUTPUT = Path(".venv") / ".r0_p03_historical_evidence_review"
FILENAME = "R0_P03_HISTORICAL_EVIDENCE_REVIEW.json"


def _role(path: str) -> str:
    if path.startswith("docs/checkpoints/"):
        return "historical_checkpoint_evidence"
    if path.startswith("docs/research/"):
        return "historical_research_and_decision_basis"
    if path.startswith("docs/local_execution/validation/"):
        return "execution_validation_evidence"
    if path.startswith("scripts/"):
        return "execution_or_build_tool"
    if path.startswith("tests/"):
        return "test_source_or_fixture"
    if path.startswith("schemas/"):
        return "machine_schema"
    raise ValueError("Unknown evidence family")


def audit(repo: Path, *, pin: str = expanded.prior.base.PIN) -> dict:
    repo = repo.resolve()
    if not (repo / ".git").is_dir():
        raise ValueError("Expected trusted Git repository")
    if (expanded.prior.base.git(
        repo, "rev-parse", "--verify", pin + "^{commit}"
    ).strip().decode("ascii") != pin):
        raise ValueError("Historical source ref not pinned")
    selected = set(expanded.prior.source_window(repo, pin=pin))
    frontend, _ = expanded._frontend(repo, pin)
    selected.update(frontend)
    tree = expanded.prior.base.git(repo, "ls-tree", "-rz", pin, "--", *ROOTS)
    candidates = {}
    for entry in tree.split(b"\0"):
        if not entry:
            continue
        meta, rawpath = entry.split(b"\t", 1)
        mode, typ, oid = meta.decode("ascii").split()
        path = rawpath.decode("utf-8")
        parts = PurePosixPath(path)
        if path.startswith("/") or ".." in parts.parts or "\\" in path:
            raise ValueError("Unsafe source path")
        if path in selected:
            continue
        if mode not in {"100644", "100755"} or typ != "blob":
            raise ValueError("Unexpected Git object type")
        role = _role(path)
        candidates[path] = (oid, role, parts.suffix.lower())
    eligible_for_text_audit = {
        p: oid for p, (oid, _, suffix) in candidates.items()
        if suffix in TEXT_SUFFIXES
    }
    oids = sorted(set(eligible_for_text_audit.values()))
    batch = expanded.prior.base.git(
        repo, "cat-file", "--batch",
        input_bytes=("\n".join(oids) + "\n").encode("ascii") if oids else b"",
    ) if oids else b""
    pos = 0
    blobs = {}
    for expected in oids:
        end = batch.index(b"\n", pos)
        header = batch[pos:end].decode("ascii").split()
        if len(header) != 3:
            raise ValueError("Malformed Git batch response")
        actual, typ, size_text = header
        size = int(size_text)
        start, stop = end + 1, end + 1 + size
        raw = batch[start:stop]
        if (actual != expected or typ != "blob" or len(raw) != size
                or batch[stop:stop + 1] != b"\n"
                or hashlib.sha1(
                    b"blob " + str(size).encode("ascii") + b"\0" + raw
                ).hexdigest() != expected):
            raise ValueError("Git source evidence blob identity mismatch")
        blobs[expected] = raw
        pos = stop + 1
    if pos != len(batch):
        raise ValueError("Unconsumed Git batch content")
    lines = []
    counts = Counter()
    for path, (oid, role, suffix) in sorted(candidates.items()):
        if suffix not in TEXT_SUFFIXES:
            record = {
                "path": path, "git_blob_oid": oid, "role_hint": role,
                "status": "NON_TEXT_UNSUPPORTED_NOT_ADMITTED",
                "review_flags": ["UNSUPPORTED_MEDIA"],
            }
        else:
            raw = blobs[oid]
            if b"\0" in raw:
                record = {
                    "path": path, "git_blob_oid": oid, "role_hint": role,
                    "status": "NON_TEXT_UNSUPPORTED_NOT_ADMITTED",
                    "review_flags": ["BINARY_BYTES"],
                }
            else:
                try:
                    content = raw.decode("utf-8")
                except UnicodeDecodeError:
                    record = {
                        "path": path, "git_blob_oid": oid, "role_hint": role,
                        "status": "NON_TEXT_UNSUPPORTED_NOT_ADMITTED",
                        "review_flags": ["NON_UTF8_ENCODING"],
                    }
                else:
                    flags = [
                        flag for flag, pattern in FLAGS.items()
                        if pattern.search(content)
                    ]
                    if DIRECT_PATH.search(path):
                        flags.append("PATH_INDICATES_DESIGN_OR_LEGACY")
                    record = {
                        "path": path,
                        "git_blob_oid": oid,
                        "sha256": hashlib.sha256(raw).hexdigest(),
                        "bytes": len(raw),
                        "role_hint": role,
                        "status": "REVIEW_ONLY_NOT_ADMITTED",
                        "review_flags": sorted(flags),
                    }
                    counts[(role, "flagged" if flags else "no_lexical_flag")] += 1
        counts[(role, "total")] += 1
        if record["status"].startswith("NON_TEXT"):
            counts[(role, "unsupported")] += 1
        lines.append(record)
    summary = {
        role: {
            "tracked": counts[(role, "total")],
            "flagged_text": counts[(role, "flagged")],
            "unflagged_text_requires_review": counts[(role, "no_lexical_flag")],
            "unsupported": counts[(role, "unsupported")],
        }
        for role in sorted(set(r["role_hint"] for r in lines))
    }
    return {
        "schema_version": 1,
        "identifier": ID,
        "source_ref": pin,
        "classification": "NONSCORING_HISTORICAL_EVIDENCE_REVIEW_MANIFEST",
        "excluded_already_present_in_406_source_candidate": len(selected),
        "review_record_count": len(lines),
        "summary": summary,
        "review_records": lines,
        "admission_decision": "NONE_ADMITTED_BY_LEXICAL_OR_PATH_CENSUS",
        "required_next_action": (
            "Prospective independent source-status and contamination adjudication "
            "before any task-author source-world freeze; missing necessary evidence "
            "must trigger source-review and cannot be handpicked per known task"
        ),
    }


def emit(repo: Path, *, pin: str = expanded.prior.base.PIN,
         verify_only: bool = False, root_override: Path | None = None) -> dict:
    result = audit(repo, pin=pin)
    data = (json.dumps(result, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    digest = hashlib.sha256(data).hexdigest()
    receipt = {
        "identifier": ID,
        "source_ref": pin,
        "manifest_bytes": len(data),
        "manifest_sha256": digest,
        "review_record_count": result["review_record_count"],
        "status": result["admission_decision"],
    }
    out = (root_override or (repo / OUTPUT)).resolve()
    if root_override is not None and (out == repo or out.is_relative_to(repo)):
        raise ValueError("Output override cannot point into repo")
    manifest = out / FILENAME
    receipt_path = out / "R0_P03_HISTORICAL_EVIDENCE_REVIEW.receipt.json"
    if verify_only:
        if not manifest.is_file() or manifest.read_bytes() != data:
            raise ValueError("Historical evidence audit reproducibility failure")
        if not receipt_path.is_file() or json.loads(receipt_path.read_text("utf-8")) != receipt:
            raise ValueError("Historical evidence receipt mismatch")
        print("HISTORICAL_EVIDENCE_REPRODUCIBILITY=PASS")
    else:
        if manifest.exists() or receipt_path.exists():
            raise FileExistsError("Refusing to overwrite historical evidence review")
        out.mkdir(parents=True, exist_ok=True)
        manifest.write_bytes(data)
        receipt_path.write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8", newline="\n")
    print(json.dumps({"receipt":receipt,"summary":result["summary"]}, sort_keys=True))
    return receipt


if __name__ == "__main__":
    if len(sys.argv) not in {2, 3} or (len(sys.argv) == 3 and sys.argv[2] != "--verify-only"):
        raise SystemExit("usage: python -m experiments.r0_p03_navigation_probe.primary_author_historical_evidence_review_candidate REPO [--verify-only]")
    emit(Path(sys.argv[1]), verify_only=len(sys.argv) == 3)
