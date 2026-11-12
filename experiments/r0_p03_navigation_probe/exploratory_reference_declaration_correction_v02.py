"""Preserve V01 and execute a separately versioned exact-field correction.

The only modified evidence claim is PATH_SELECTOR adjacency and newly
distinguished author-declared reference metadata. This is not a governing
relationship adjudicator, an independent reference key, or a B2/J2 result.
"""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
from hashlib import sha256
import json
import re
from typing import Any

from experiments.r0_p03_navigation_probe.exploratory_legacy_b0_b1_live_comparison import source_at_revision
from experiments.r0_p03_navigation_probe.exploratory_reference_provenance_audit_v01 import (
    IDENTIFIER as V01_ID, PIN, PRIOR_RESULT_SHA256, RESULT as V01_RESULT,
    ROOT, SOURCE_SHA256, aggregate, run as run_v01,
)

IDENTIFIER = "R0_P03_EXPLORATORY_SOURCE_OWNED_REFERENCE_FIELD_CORRECTION_V02"
RESULT = ROOT / "experiments/r0_p03_navigation_probe/exploratory_reference_declaration_correction_result_v02.json"
CONTRACT = "EXPLORATORY_REFERENCE_DECLARATION_CORRECTION_CONTRACT_V02.md"
V01_SHA256 = "e935edf01c6298b2c55950236c18eab6a9d4f712cfeca1ce3c7c48f69376d299"
DECLARED_LINE = re.compile(r"\*\*Declared references:\*\*", re.I)


def is_adjacent_path_selector(line: str, at: int) -> bool:
    """The exact five characters preceding THIS occurrence must say path:."""
    return at >= 5 and line[at-5:at].casefold() == "path:"


def corrected_flags(entry: dict[str, Any]) -> list[str]:
    """A bounded mechanical correction, not a semantic source adjudication."""
    flags = set(entry["indicators"])
    flags.discard("PATH_SELECTOR")
    flags.discard("DECLARED_REFERENCES_FIELD")
    if is_adjacent_path_selector(entry["raw_original_line"], entry["char_start"]):
        flags.add("PATH_SELECTOR")
        if DECLARED_LINE.search(entry["raw_original_line"]):
            flags.add("DECLARED_REFERENCES_FIELD")
    return sorted(flags)


def independent_eligible_path_occurrences(
    sources: dict[str, bytes],
    eligible: set[str],
) -> Counter[tuple[str, str, int, int, int]]:
    """Enumerate independently using full known eligible path strings.

    Unlike the legacy source-path token regex, exact string matching accepts
    sentence-ending punctuation after a matched full path. Obvious continued
    file extensions or path suffixes are excluded. This is a bounded challenger,
    not exhaustive parser proof for all Markdown/URL syntax.
    """
    patterns = {
        target: re.compile(
            r"(?<![A-Za-z0-9_])" + re.escape(target) +
            r"(?![A-Za-z0-9_/-])"
        )
        for target in sorted(eligible)
    }
    result: Counter[tuple[str, str, int, int, int]] = Counter()
    for source in sorted(sources):
        for n, line in enumerate(sources[source].decode("utf-8").splitlines(), 1):
            for target, pattern in patterns.items():
                if target == source:
                    continue
                for match in pattern.finditer(line):
                    end = match.end()
                    if (end + 1 < len(line) and line[end] == "."
                            and line[end + 1].isalnum()):
                        continue
                    result[(source, target, n, match.start(), match.end())] += 1
    return result


def run() -> dict[str, Any]:
    original_bytes = V01_RESULT.read_bytes()
    if sha256(original_bytes).hexdigest() != V01_SHA256:
        raise ValueError("Published V01 result identity has changed")
    original = json.loads(original_bytes)
    rebuilt = run_v01()
    if rebuilt != original or original["identifier"] != V01_ID:
        raise ValueError("Original full V01 run is not reproducible")
    if original["historical_source_fingerprint_sha256"] != SOURCE_SHA256:
        raise ValueError("Pinned source-body fingerprint changed")
    if original["prior_checkpoint_910_result_sha256"] != PRIOR_RESULT_SHA256:
        raise ValueError("Checkpoint 910 preservation failed")

    corrected = deepcopy(original["occurrences"])
    changed = 0
    for entry in corrected:
        flags = corrected_flags(entry)
        if entry["indicators"] != flags:
            changed += 1
        entry["indicators"] = flags
    old_identity = [
        (e["source"], e["target"], e["line_number"], e["char_start"], e["char_end"],
         e["source_sha256"], e["source_blob_sha1"], e["source_line_sha256"],
         e["syntax_context"], e["raw_original_line"])
        for e in original["occurrences"]
    ]
    new_identity = [
        (e["source"], e["target"], e["line_number"], e["char_start"], e["char_end"],
         e["source_sha256"], e["source_blob_sha1"], e["source_line_sha256"],
         e["syntax_context"], e["raw_original_line"])
        for e in corrected
    ]
    if old_identity != new_identity:
        raise ValueError("V02 must preserve every exact original occurrence")
    eligible = set(original["eligible_sources"])
    edges = {
        (entry["source"], entry["target"])
        for entry in corrected
    }
    independently_scanned = independent_eligible_path_occurrences(
        {p: source_at_revision(PIN, p) for p in sorted(eligible)},
        eligible,
    )
    recorded = Counter(
        (e["source"], e["target"], e["line_number"], e["char_start"], e["char_end"])
        for e in corrected
    )
    if recorded != independently_scanned:
        raise ValueError("Alternate exact-target occurrence scanner disagrees with 65-source historical corpus")
    stats = aggregate(corrected, eligible, edges)
    path_selectors = [
        e for e in corrected if "PATH_SELECTOR" in e["indicators"]
    ]
    declared = [
        e for e in corrected if "DECLARED_REFERENCES_FIELD" in e["indicators"]
    ]
    if not set(map(id, declared)) <= set(map(id, path_selectors)):
        raise AssertionError("Declared field must be an adjacent selector")
    if stats["occurrences_total"] != 146 or stats["directed_pairs_total"] != 110:
        raise ValueError("Original source pairs changed")
    metadata = {}
    for key, rows in (
        ("adjacent_path_selector", path_selectors),
        ("source_declared_references_field", declared),
    ):
        metadata[key] = {
            "occurrence_count": len(rows),
            "distinct_directed_pairs": len({(r["source"], r["target"]) for r in rows}),
            "source_count": len({r["source"] for r in rows}),
            "target_count": len({r["target"] for r in rows}),
            "occurrence_indices": [i for i, e in enumerate(corrected) if e in rows],
            "semantic_authority_accepted": False,
        }
    return {
        "identifier": IDENTIFIER,
        "contract": CONTRACT,
        "classification": "VERSIONED_CORRECTION_AND_SOURCE_OWNED_REFERENCE_DECLARATION_SYNTAX",
        "historical_git_pin": PIN,
        "source_fingerprint_sha256": SOURCE_SHA256,
        "v01_exact_sha256": V01_SHA256,
        "v01_exact_bytes": len(original_bytes),
        "change_scope": "PATH_SELECTOR adjacency and DECLARED_REFERENCES_FIELD only",
        "changed_occurrence_flag_records": changed,
        "source_line_identity_unchanged": True,
        "alternate_exact_path_enumeration": {
            "matching_original_occurrences": sum(independently_scanned.values()),
            "matching_original_directed_pairs": len({(k[0], k[1]) for k in independently_scanned}),
            "new_occurrences_in_this_pinned_corpus": 0,
            "known_legacy_regex_terminal_period_blind_spot": True,
        },
        "occurrences": corrected,
        "metadata": metadata,
        "summary": stats,
        "limitations": [
            "Declared references are source-authored references, NOT governing/editorial J2/B2 authoritative relations.",
            "Some explicit normative prose uses inline-code paths but no declared path: metadata; no syntax filter determines its authority.",
            "Original corpus has identical 146 literal occurrences under challenger match, not proof of no legacy parser blind spot in new corpora.",
            "V01 is immutable; previous 909/910 source reference self-consistency claims remain only structural.",
            "No new independently adjudicated reference gold, B3/B4 method, scored R0-P03 or physical architecture selection.",
        ],
        "formal_r0_p03_scored": False,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", action="store_true")
    args = parser.parse_args()
    data = run()
    raw = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=True) + "\n"
    if args.output:
        with RESULT.open("x", encoding="utf-8", newline="\n") as f:
            f.write(raw)
    print(json.dumps({
        "id": data["identifier"],
        "changed_flagged_occurrences": data["changed_occurrence_flag_records"],
        "metadata": data["metadata"],
        "alternate_scan": data["alternate_exact_path_enumeration"],
        "written": bool(args.output),
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
