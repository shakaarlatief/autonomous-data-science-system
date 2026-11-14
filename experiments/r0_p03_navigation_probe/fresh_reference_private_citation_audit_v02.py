"""V02 correction to the source-nonrevealing R0-P03 citation audit.

The complete report is retained under ignored local storage. This verifier
reads it only within the local execution process and emits aggregate counts.
It checks exact original Git object identity, numerical line provenance and
literal excerpt matching. It cannot decide factual entailment, completeness,
owner authority, source truth, or eligibility for a scored R0-P03 trial.

V01 remains frozen as a separately preserved first audit. V02 corrects only
repository-prefix admission and incidental non-citation @ recognition. The
source-report hash, Git horizon, literal matching and output policy do not
change. This correction occurred after V01 results were observed.

The input hash and historical Git pin are fixed. Nothing is repaired after
observing a mismatch. A missing match is an unresolved attribution defect,
not proof that the underlying claim is false. Do not publish detailed findings
or case-to-source links. All exception types are sanitized before stdout.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

PIN = "47ed6344a9153dcf366769e95722840fbf1a8f8b"
REPORT = Path(".venv/r0_p03_fresh_reference_pilot_v01/PRIVATE_ORIGINAL_SOURCE_REFERENCE_REPORT.md")
EXPECTED_REPORT_BYTES = 84359
EXPECTED_REPORT_SHA256 = "cce0c99e2c6b019b3e8f67ea960e92c2108b8ff673b685b2865de6977d06dc0b"
PRIVATE_AUDIT = Path(".venv/r0_p03_fresh_reference_pilot_v01/PRIVATE_CITATION_AUDIT_V02.json")
PUBLIC_AGGREGATE = Path(
    "experiments/r0_p03_navigation_probe/fresh_reference_private_citation_audit_aggregate_v02.json"
)
SOURCE_RE = re.compile(
    r"([A-Za-z0-9_./-]+\.(?:md|py|json|toml|txt|yml|yaml))@([a-f0-9]{40})"
)
LINE_SPEC_RE = re.compile(r"\d+(?:-\d+)?(?:,\s*\d+(?:-\d+)?)*")
MAX_SOURCE_BYTES = 12_000_000
MAX_SOURCE_LINES = 200_000


@dataclass(frozen=True)
class Witness:
    private_report_line: int
    path: str
    blob_oid: str
    line_spec: str
    quoted_excerpt: str


def parse_line_spec(spec: str, total_lines: int) -> tuple[int, ...]:
    """Parse exact comma-separated 1-based inclusive ranges, rejecting reversal.

    Each number must reference an existing original Git source line.
    Numeric syntax alone is insufficient: out-of-bounds, descending ranges
    and empty selections are all rejected rather than silently clamped.
    """
    if LINE_SPEC_RE.fullmatch(spec) is None:
        raise ValueError("LINE_SPEC_SYNTAX")
    selected: list[int] = []
    for segment in spec.split(","):
        parts = [int(v) for v in segment.strip().split("-")]
        first, last = parts[0], parts[-1]
        if first < 1 or last > total_lines or last < first:
            raise ValueError("LINE_SPEC_BOUNDS")
        selected.extend(range(first, last + 1))
    if not selected:
        raise ValueError("LINE_SPEC_EMPTY")
    return tuple(sorted(set(selected)))


def validate_path(path: str) -> None:
    """Constrain a reported source to safe, repository-relative source paths."""
    if path.startswith("/") or "\\" in path or ":" in path:
        raise ValueError("SOURCE_PATH_UNSAFE")
    if ".." in path.split("/") or "." in path.split("/"):
        raise ValueError("SOURCE_PATH_UNSAFE")
    # V02: the pinned historical Git tree is the source-world admission gate.
    # V01 incorrectly excluded repository-root and other tracked sources.
    # No repository prefix may be excluded if Git itself resolves the exact blob.
    if not path or any(part == "" for part in path.split("/")):
        raise ValueError("SOURCE_PATH_UNSAFE")


def extract_witnesses(report: str) -> tuple[list[Witness], int]:
    """Read only explicit report-table source@blob witnesses.

    The report contains narrative, summary and table rows without actual
    source-line citations. Count citation-containing rows that fail the
    contract, rather than mistaking them for validated source observations.
    """
    result: list[Witness] = []
    unparsed = 0
    for line_number, line in enumerate(report.splitlines(), 1):
        if not line.startswith("|"):
            continue
        fields = [part.strip() for part in line.strip("|").split("|")]
        if len(fields) < 6 or "@" not in fields[3]:
            continue
        candidate = fields[3].strip(chr(96))
        # V01 counted an incidental @-bearing non-source cell as malformed.
        # Only file-extension@... citations are eligible for this parser.
        if re.search(r"\.[A-Za-z0-9]{1,8}@", candidate) is None:
            continue
        match = SOURCE_RE.fullmatch(candidate)
        if match is None:
            unparsed += 1
            continue
        result.append(Witness(
            private_report_line=line_number,
            path=match.group(1),
            blob_oid=match.group(2),
            line_spec=fields[4],
            quoted_excerpt=fields[5],
        ))
    return result, unparsed


def normalize_space(text: str) -> str:
    return " ".join(text.split())


def classify_literal_excerpt(quoted: str, selected_text: str, whole_text: str) -> str:
    """Conservatively classify a literal excerpt without fuzzy repair.

    Report quote columns may contain markdown backticks or ASCII double
    quotation marks around a cited phrase. Removing only those exterior
    delimiters avoids conflating a paraphrase with a verbatim source quote.
    """
    q = quoted.strip().strip(chr(96)).strip('"').strip()
    if not q:
        return "NO_LITERAL_MATCH"
    if q in selected_text:
        return "EXACT_CITED_LINE_MATCH"
    if normalize_space(q) in normalize_space(selected_text):
        return "WHITESPACE_ONLY_CITED_LINE_MATCH"
    if q in whole_text:
        return "LITERAL_MATCH_ELSEWHERE_IN_SAME_BLOB"
    return "NO_LITERAL_MATCH"


def git_bytes(*args: str) -> bytes:
    completed = subprocess.run(
        ["git", *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=False, timeout=20,
    )
    if completed.returncode:
        raise RuntimeError("HISTORICAL_GIT_SOURCE_UNAVAILABLE")
    if len(completed.stdout) > MAX_SOURCE_BYTES:
        raise RuntimeError("HISTORICAL_GIT_SOURCE_TOO_LARGE")
    return completed.stdout


def historical_source(path: str, cache: dict[str, tuple[str, list[str]]]) -> tuple[str, list[str]]:
    if path not in cache:
        validate_path(path)
        oid = git_bytes("rev-parse", PIN + ":" + path).decode("ascii").strip()
        if re.fullmatch(r"[0-9a-f]{40}", oid) is None:
            raise RuntimeError("INVALID_HISTORICAL_GIT_OID")
        blob = git_bytes("show", PIN + ":" + path)
        lines = blob.decode("utf-8").splitlines()
        if len(lines) > MAX_SOURCE_LINES:
            raise RuntimeError("HISTORICAL_GIT_SOURCE_TOO_MANY_LINES")
        cache[path] = oid, lines
    return cache[path]


def evaluate(
    witnesses: list[Witness],
) -> tuple[dict[str, int], list[dict[str, object]]]:
    """Return only counts to public callers, details to local ignored storage."""
    counts: Counter[str] = Counter()
    private_details: list[dict[str, object]] = []
    cache: dict[str, tuple[str, list[str]]] = {}
    for witness in witnesses:
        counts["citation_rows"] += 1
        status = ""
        try:
            actual_oid, lines = historical_source(witness.path, cache)
            if actual_oid != witness.blob_oid:
                status = "BLOB_ID_MISMATCH"
            else:
                counts["historical_blob_ids_verified"] += 1
                try:
                    positions = parse_line_spec(witness.line_spec, len(lines))
                except ValueError:
                    status = "LINE_RANGE_INVALID"
                else:
                    counts["historical_line_ranges_valid"] += 1
                    selected = "\n".join(lines[i-1] for i in positions)
                    full_text = "\n".join(lines)
                    status = classify_literal_excerpt(
                        witness.quoted_excerpt, selected, full_text
                    )
        except (RuntimeError, ValueError, UnicodeError, subprocess.TimeoutExpired):
            status = "HISTORICAL_SOURCE_READ_FAILURE"
        counts[status] += 1
        private_details.append({
            "report_line": witness.private_report_line,
            "reported_path": witness.path,
            "reported_blob_oid": witness.blob_oid,
            "reported_line_spec": witness.line_spec,
            "verification": status,
        })
    counts["distinct_historical_paths_opened"] = len(cache)
    return dict(counts), private_details


def build_results() -> tuple[dict[str, object], dict[str, object]]:
    raw = REPORT.read_bytes()
    if len(raw) != EXPECTED_REPORT_BYTES or sha256(raw).hexdigest() != EXPECTED_REPORT_SHA256:
        raise ValueError("PRIVATE_REPORT_IDENTITY_MISMATCH")
    report = raw.decode("utf-8")
    witnesses, unparsed = extract_witnesses(report)
    if not witnesses:
        raise ValueError("NO_EXPLICIT_CITATIONS")
    counts, detail = evaluate(witnesses)
    counts["unparsed_citation_cells"] = unparsed
    counts["original_git_pin_exists"] = int(git_bytes("cat-file", "-t", PIN).strip() == b"commit")
    if not counts["original_git_pin_exists"]:
        raise ValueError("ORIGINAL_PIN_INVALID")
    n = counts["citation_rows"]
    counts["all_blob_ids_verified"] = int(counts.get("historical_blob_ids_verified", 0) == n)
    counts["all_line_ranges_valid"] = int(counts.get("historical_line_ranges_valid", 0) == n)
    counts["all_literal_quotes_verified_on_cited_lines"] = int(
        counts.get("EXACT_CITED_LINE_MATCH", 0)
        + counts.get("WHITESPACE_ONLY_CITED_LINE_MATCH", 0) == n
    )
    public = {
        "audit_id": "R0_P03_FRESH_REFERENCE_CITATION_MECHANICAL_V02",
        "scientific_class": "UNSCORED_RETROSPECTIVE_PRIVATE_REPORT_CITATION_AUDIT",
        "original_source_git_pin": PIN,
        "private_report_bytes": EXPECTED_REPORT_BYTES,
        "private_report_sha256": EXPECTED_REPORT_SHA256,
        "verification_counts": dict(sorted(counts.items())),
        "detailed_source_paths_or_quotes_in_public_output": False,
        "original_case_answer_contents_released": False,
        "semantic_claim_entailment_checked": False,
        "independent_gold_or_scored_R0_P03_qualified": False,
        "limitations": [
            "Report-table explicit source witnesses only; narrative claims and uncited rows are not fully source-audited.",
            "Original Git path, blob and line bounds do not establish that source assertions are true or operative.",
            "Literal excerpts that do not match cited lines remain unresolved rather than silently repaired or falsified.",
            "Same-account local-only custody has no demonstrated separation from prospective scored arm authors.",
            "Retrospective mechanical audit follows the source-review result and cannot retroactively create blinded gold.",
        ],
    }
    private = {
        "audit_id": public["audit_id"],
        "private_report_sha256": EXPECTED_REPORT_SHA256,
        "details": detail,
    }
    return public, private


def main() -> int:
    try:
        public, private = build_results()
        public_bytes = (json.dumps(public, indent=2, sort_keys=True) + "\n").encode("utf-8")
        private_bytes = (json.dumps(private, indent=2, sort_keys=True) + "\n").encode("utf-8")
        # Exclusive creation: never overwrite original evidence or silently
        # rewrite a previous audit after inspecting the result.
        with PRIVATE_AUDIT.open("xb") as fp:
            fp.write(private_bytes)
        with PUBLIC_AGGREGATE.open("xb") as fp:
            fp.write(public_bytes)
        print(json.dumps({
            "audit_id": public["audit_id"],
            "verification_counts": public["verification_counts"],
            "public_bytes": len(public_bytes),
            "public_sha256": sha256(public_bytes).hexdigest(),
            "private_detail_bytes": len(private_bytes),
            "private_detail_sha256": sha256(private_bytes).hexdigest(),
            "private_report_text_disclosed": False,
        }, sort_keys=True))
        return 0
    except Exception:
        # Deliberately no raw exception details or traceback: Git and parsing
        # exceptions can contain private paths or source excerpts.
        print("AUDIT_FAILED_WITH_SANITIZED_ERROR; original input not modified")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
