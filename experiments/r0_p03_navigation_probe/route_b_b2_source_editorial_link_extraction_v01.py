"""Freeze original source-authored candidate editorial path links, not authority.

Typed/declared and explicit Authority/Parent headers are excluded because
they belong to the common native relation substrate. The remainder is a
source-written editorial/path mention only, never a governing acceptance.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re

from experiments.r0_p03_navigation_probe.route_b_primary_b0_baseline_execution_v01 import (
    original_contents, ROOT, PIN,
)

BASELINE = ROOT / "experiments/r0_p03_navigation_probe/route_b_primary_b0_baseline_result_v01.json"
RESULT = ROOT / "experiments/r0_p03_navigation_probe/route_b_primary_b2_source_editorial_link_witnesses_v01.json"
PATH = re.compile(r"(?<![\w/])docs/[A-Za-z0-9_./-]+\.(?:md|json|py)\b")
EXCLUDED_NATIVE_HEADERS = (
    "**Declared references:**", "**Authority:**", "**Parent:**",
)


def original_edges() -> dict:
    result = json.loads(BASELINE.read_text(encoding="utf8"))
    build = result["build_sources"]
    if len(build) != 60 or result["source_git_pin"] != PIN:
        raise ValueError("B0 original source boundary drift")
    original = original_contents(build)
    available = set(build)
    edges = []
    excluded_natives = 0
    excluded_outside = 0
    excluded_fenced = 0
    seen = set()
    for p in build:
        lines = original[p].decode("utf-8").splitlines()
        fence = False
        for number, line in enumerate(lines, 1):
            if line.lstrip().startswith((chr(96) * 3, "~~~")):
                fence = not fence
                continue
            found = list(PATH.finditer(line))
            if fence:
                excluded_fenced += len(found)
                continue
            if line.strip().startswith(EXCLUDED_NATIVE_HEADERS):
                excluded_natives += len(found)
                continue
            for m in found:
                target = m.group(0)
                if target not in available or target == p:
                    excluded_outside += 1
                    continue
                dedup = (p, target, number)
                if dedup in seen:
                    continue
                seen.add(dedup)
                edges.append({
                    "source_path": p,
                    "source_sha256": sha256(original[p]).hexdigest(),
                    "target_path": target,
                    "target_sha256": sha256(original[target]).hexdigest(),
                    "source_line": number,
                    "verbatim_original_source_line": line,
                    "source_line_sha256": sha256(line.encode("utf8")).hexdigest(),
                    "source_evidence": "literal_source_written_path_reference_outside_fence",
                    "relationship": "CANDIDATE_EDITORIAL_NAVIGATION_NOT_GOVERNING",
                    "owner_governing_effect_asserted": False,
                })
    return {
        "id": "R0_P03_ROUTE_B_B2_SOURCE_WRITTEN_EDITORIAL_LINK_CANDIDATES_V01",
        "source_git_pin": PIN,
        "build_paths": build,
        "source_policy": "Original nonfenced direct build-to-build docs/path literal; exclude native Declared references, Authority and Parent headings",
        "native_header_matches_not_in_B2": excluded_natives,
        "fenced_source_mentions_not_in_B2": excluded_fenced,
        "nonbuild_or_self_mentions_not_in_B2": excluded_outside,
        "observed_editorial_candidate_link_count": len(edges),
        "observed_unique_directed_candidate_pairs": len(set(
            (x["source_path"], x["target_path"]) for x in edges
        )),
        "original_source_written_candidate_edges": sorted(
            edges, key=lambda x: (x["source_path"], x["target_path"], x["source_line"])
        ),
        "source_owned_assertion_class": "EDITORIAL_PATH_MENTION_ONLY",
        "none_of_these_edges_proves_operative_authority": True,
        "limitations": [
            "A literal reference is not proof of a specially authored carrier-to-governing semantic relation.",
            "Native relation/authority declarations excluded because they are not a B2-only addition.",
            "Source text is inspected beyond the common 12000-character retrieval cap for candidate editorial references; all additional source inspection/metadata cost must be reported.",
            "The graph is sparse and all non-build references are excluded. No task source IDs or gold are consulted.",
            "Historical Git original source bytes are read, but no original carriers are modified and no governing or source-accepted relation is generated.",
        ],
    }


def main() -> None:
    import argparse
    arg = argparse.ArgumentParser(description=__doc__)
    arg.add_argument("--output", action="store_true")
    arg.add_argument("--verify", action="store_true")
    args = arg.parse_args()
    data = original_edges()
    raw = (json.dumps(data, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if args.output:
        with RESULT.open("xb") as f:
            f.write(raw)
    if args.verify and RESULT.read_bytes() != raw:
        raise ValueError("Original source editorial link result not replayable byte-for-byte")
    print(json.dumps({
        "links": data["observed_editorial_candidate_link_count"],
        "pairs": data["observed_unique_directed_candidate_pairs"],
        "native_excluded": data["native_header_matches_not_in_B2"],
        "fenced_excluded": data["fenced_source_mentions_not_in_B2"],
        "outside_excluded": data["nonbuild_or_self_mentions_not_in_B2"],
        "bytes": len(raw),
        "sha256": sha256(raw).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
