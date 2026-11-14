"""Transparent V02 correction of two incorrectly omitted excerpt clipping flags.

V01 selected original source paths, source lines, question text and excerpt
contents remain frozen. V02 changes only boolean line_clipped annotations,
using exact full historical Git source lines. Every other serialized field
is asserted equal. V02 is a post-V01 observation correction, not a result
selection, ranking modification, source repair or scoring operation.
"""
from __future__ import annotations
from collections import Counter
from copy import deepcopy
from hashlib import sha256, sha1
import json
import subprocess

from experiments.r0_p03_navigation_probe import four_need_gold_free_original_source_navigation_v01 as nav

V01_SHA = {
    "A": "0c7b39ecba5524c96d96426303e29c362b09c070fa24c14aa2d6c8b4a080be10",
    "B": "60bcdf530b98377f2faa7749ac904f0f1a0f9d00590f32cd1b38a03af0375ac5",
}
V01_AGG_SHA = "6f35585e5b2ba71e6b20c72f6932ac2291c2365b51c3820b9ea1cc74bbae56bb"
OUTPUT_A = nav.BASE / "four_need_gold_free_source_packet_A_v02.json"
OUTPUT_B = nav.BASE / "four_need_gold_free_source_packet_B_v02.json"
AGGREGATE = nav.BASE / "four_need_gold_free_navigation_aggregate_v02.json"


def pinned_lines(path: str, oid: str, cache: dict[str, list[str]]) -> list[str]:
    if path not in cache:
        ref = subprocess.check_output(
            ["git", "rev-parse", nav.SOURCE_PIN + ":" + path],
            cwd=nav.ROOT, timeout=12,
        ).decode("ascii").strip()
        if ref != oid:
            raise ValueError("Original Git source path/blob identity drift")
        data = subprocess.check_output(
            ["git", "cat-file", "blob", oid], cwd=nav.ROOT, timeout=12,
        )
        if sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest() != oid:
            raise ValueError("Original Git blob data identity mismatch")
        cache[path] = data.decode("utf8").splitlines()
    return cache[path]


def corrected_packet(old: dict, cache: dict[str, list[str]]) -> tuple[dict, int]:
    candidate = deepcopy(old)
    fixes = 0
    for case in candidate["cases"]:
        for item in case["source_excerpts"]:
            lines = pinned_lines(item["original_git_path"], item["original_git_blob_sha1"], cache)
            for excerpt in item["excerpts"]:
                for report_line in excerpt["lines"]:
                    original = lines[report_line["original_line"] - 1]
                    displayed = report_line["text"]
                    if not original.startswith(displayed):
                        raise ValueError("Source excerpt text not present at asserted original line")
                    expected = len(displayed) < len(original)
                    if report_line["line_clipped"] != expected:
                        report_line["line_clipped"] = expected
                        fixes += 1
    # A structural audit independent of hand-selected citations: after
    # deleting line_clipped flags, every part of V01 and V02 is unchanged.
    def strip_flags(value):
        if isinstance(value, dict):
            return {k: strip_flags(v) for k, v in value.items() if k != "line_clipped"}
        if isinstance(value, list):
            return [strip_flags(v) for v in value]
        return value
    if strip_flags(old) != strip_flags(candidate):
        raise ValueError("V02 illegally changed original question, ranking or source text")
    return candidate, fixes


def run() -> tuple[dict, bytes, bytes]:
    if sha256(nav.NEEDS.read_bytes()).hexdigest() != nav.NEEDS_SHA256:
        raise ValueError("Frozen original question identity drift")
    if sha256(nav.CONTRACT.read_bytes()).hexdigest() != nav.CONTRACT_SHA256:
        raise ValueError("Frozen original protocol identity drift")
    for target in (OUTPUT_A, OUTPUT_B, AGGREGATE):
        if target.exists():
            raise FileExistsError("V02 output already exists; no replacement allowed")
    original = {}
    for key, path in (("A", nav.PACKET_A), ("B", nav.PACKET_B)):
        raw = path.read_bytes()
        if sha256(raw).hexdigest() != V01_SHA[key]:
            raise ValueError("Frozen V01 packet differs")
        original[key] = json.loads(raw)
    if sha256(nav.AGGREGATE.read_bytes()).hexdigest() != V01_AGG_SHA:
        raise ValueError("Frozen V01 aggregate differs")
    cache: dict[str, list[str]] = {}
    first, fixes_a = corrected_packet(original["A"], cache)
    second, fixes_b = corrected_packet(original["B"], cache)
    out_a, out_b = nav.canonical(first), nav.canonical(second)
    summary = {
        "id": "R0_P03_FOUR_NEED_GOLD_FREE_PACKET_CLIP_FLAG_CORRECTION_V02",
        "original_git_pin": nav.SOURCE_PIN,
        "original_frozen_questions_sha256": nav.NEEDS_SHA256,
        "original_v01_aggregate_sha256": V01_AGG_SHA,
        "original_v01_packet_A_sha256": V01_SHA["A"],
        "original_v01_packet_B_sha256": V01_SHA["B"],
        "v02_packet_A_sha256": sha256(out_a).hexdigest(),
        "v02_packet_B_sha256": sha256(out_b).hexdigest(),
        "v02_packet_A_bytes": len(out_a),
        "v02_packet_B_bytes": len(out_b),
        "candidate_sources_reordered": False,
        "question_text_changed": False,
        "retrieved_source_content_changed": False,
        "original_source_line_numbers_changed": False,
        "v01_still_preserved": True,
        "only_boolean_line_clipped_flags_changed": True,
        "corrected_clipping_flags_A": fixes_a,
        "corrected_clipping_flags_B": fixes_b,
        "original_source_files_checked": len(cache),
        "private_reference_report_read": False,
        "formal_scoring": False,
    }
    if fixes_a + fixes_b != 2:
        raise ValueError("Unexpected number of original clipping defects")
    return summary, out_a, out_b


def main() -> None:
    summary, a, b = run()
    files = (
        (OUTPUT_A, a),
        (OUTPUT_B, b),
        (AGGREGATE, nav.canonical(summary)),
    )
    for target, data in files:
        with target.open("xb") as f:
            f.write(data)
    print(json.dumps({
        "status": "V02_METADATA_ONLY_CORRECTION",
        "original_v01_preserved": True,
        "clipping_flags_corrected_A": summary["corrected_clipping_flags_A"],
        "clipping_flags_corrected_B": summary["corrected_clipping_flags_B"],
        "source_text_or_rankings_changed": False,
        "v02_packet_A_bytes": len(a),
        "v02_packet_A_sha256": sha256(a).hexdigest(),
        "v02_packet_B_bytes": len(b),
        "v02_packet_B_sha256": sha256(b).hexdigest(),
        "v02_aggregate_sha256": sha256(files[-1][1]).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
