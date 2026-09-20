from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CANDIDATE = HERE / "historical_navigation_candidate.json"
QUERIES = HERE / "cold_queries.json"
RESULT = HERE / "result.json"
RESULT_MD = HERE / "RESULT.md"

def git_bytes(ref: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{ref}:{path}"], cwd=ROOT)

def parse_legacy(raw: bytes):
    text = raw.decode("utf-8")
    lines = text.splitlines()
    subjects = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("### "):
            label = lines[i][4:].strip()
            topic = None
            description = None
            paths = []
            j = i + 1
            while j < len(lines) and not lines[j].startswith("### ") and not lines[j].startswith("## "):
                match = re.fullmatch(r"<!--\s*KM-TOPIC:\s*([^\s]+)\s*-->", lines[j].strip())
                if match:
                    topic = match.group(1)
                if topic and description is None and lines[j].strip().startswith("Use for "):
                    description = lines[j].strip()
                if topic and lines[j].strip().startswith("docs/"):
                    paths.append(lines[j].strip())
                j += 1
            if topic:
                subjects.append(
                    {
                        "topic_id": topic,
                        "label": label,
                        "description": description or "",
                        "explicit_paths": paths,
                    }
                )
            i = j
            continue
        i += 1

    ranges = []
    for line in lines:
        match = re.fullmatch(
            r"<!--\s*KM-CHECKPOINT-RANGE:\s*(\d+)-(\d+)\s+(.+?)\s*-->",
            line.strip(),
        )
        if match:
            ranges.append(
                {
                    "start": int(match.group(1)),
                    "end": int(match.group(2)),
                    "topics": match.group(3).split(),
                }
            )

    specialized = []
    try:
        start = lines.index("## Specialized library indexes")
    except ValueError:
        start = -1
    if start >= 0:
        for line in lines[start + 1 :]:
            if line.startswith("## "):
                break
            stripped = line.strip()
            if stripped.startswith("docs/"):
                specialized.append(stripped)
    return subjects, ranges, specialized

def subject_route(subjects, topic_id: str):
    for subject in subjects:
        if subject["topic_id"] == topic_id:
            return {
                "topic_id": topic_id,
                "label": subject["label"],
                "description": subject["description"],
                "explicit_paths": subject["explicit_paths"],
            }
    raise KeyError(topic_id)

def checkpoint_route(ranges, number: int):
    matches = [entry for entry in ranges if entry["start"] <= number <= entry["end"]]
    if len(matches) != 1:
        raise AssertionError(f"checkpoint {number}: expected exactly one range, got {matches}")
    return matches[0]["topics"]

def main():
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    queries = json.loads(QUERIES.read_text(encoding="utf-8"))
    assert candidate["source_boundary"] == queries["source_boundary"]

    raw = git_bytes(candidate["source_boundary"], candidate["source_path"])
    source_sha256 = hashlib.sha256(raw).hexdigest()
    assert source_sha256 == candidate["source_sha256"]

    source_subjects, source_ranges, source_specialized = parse_legacy(raw)

    exact_structure_parity = (
        candidate["subjects"] == source_subjects
        and candidate["checkpoint_ranges"] == source_ranges
        and candidate["specialized_indexes"] == source_specialized
    )

    subject_rows = []
    for topic in queries["subject_queries"]:
        source_route = subject_route(source_subjects, topic)
        cold_route = subject_route(candidate["subjects"], topic)
        subject_rows.append(
            {
                "topic_id": topic,
                "exact_match": cold_route == source_route,
                "explicit_path_count": len(cold_route["explicit_paths"]),
            }
        )

    checkpoint_rows = []
    for number in queries["checkpoint_queries"]:
        source_topics = checkpoint_route(source_ranges, number)
        cold_topics = checkpoint_route(candidate["checkpoint_ranges"], number)
        checkpoint_rows.append(
            {
                "checkpoint": number,
                "exact_match": cold_topics == source_topics,
                "topics": cold_topics,
            }
        )

    specialized_exact = candidate["specialized_indexes"] == source_specialized

    flat_inventory = sorted(
        {
            path
            for subject in candidate["subjects"]
            for path in subject["explicit_paths"]
        }
        | set(candidate["specialized_indexes"])
    )

    cold_subject_pass = all(row["exact_match"] for row in subject_rows)
    cold_checkpoint_pass = all(row["exact_match"] for row in checkpoint_rows)
    candidate_bytes = CANDIDATE.read_bytes()
    result = {
        "schema_version": 1,
        "experiment": "W5-T4",
        "authority_class": "research_output",
        "source_boundary": candidate["source_boundary"],
        "source_sha256": source_sha256,
        "source_map_bytes": len(raw),
        "candidate_evidence_bytes": len(candidate_bytes),
        "candidate_to_source_size_ratio": len(candidate_bytes) / len(raw),
        "subject_count": len(candidate["subjects"]),
        "checkpoint_range_count": len(candidate["checkpoint_ranges"]),
        "specialized_index_count": len(candidate["specialized_indexes"]),
        "flat_inventory_path_count": len(flat_inventory),
        "flat_inventory_has_subject_mapping": False,
        "flat_inventory_has_checkpoint_subject_ranges": False,
        "exact_structure_parity": exact_structure_parity,
        "cold_subject_queries": subject_rows,
        "cold_checkpoint_queries": checkpoint_rows,
        "specialized_indexes_exact": specialized_exact,
        "mechanical_verdict": {
            "compact_evidence_preserves_full_legacy_routing_structure": exact_structure_parity,
            "cold_subject_queries_pass_without_live_map": cold_subject_pass,
            "cold_checkpoint_queries_pass_without_live_map": cold_checkpoint_pass,
            "specialized_index_routes_pass_without_live_map": specialized_exact,
            "flat_inventory_is_insufficient_for_deterministic_subject_routing": True,
        },
    }
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    fence = chr(96) * 3
    tick = chr(96)
    lines = [
        "# W5 T4 Historical Navigation Result",
        "",
        f"**Source boundary:** {tick}{candidate['source_boundary']}{tick}",
        "**Authority:** Non-authoritative research output.",
        "",
        "## Representation",
        "",
        "~~~text",
        f"legacy Knowledge Map bytes        {len(raw)}",
        f"compact evidence bytes            {len(candidate_bytes)}",
        f"size ratio                        {len(candidate_bytes) / len(raw):.3f}",
        f"subjects                          {len(candidate['subjects'])}",
        f"checkpoint ranges                 {len(candidate['checkpoint_ranges'])}",
        f"specialized indexes               {len(candidate['specialized_indexes'])}",
        f"flat inventory paths              {len(flat_inventory)}",
        "~~~",
        "",
        "## Cold-query parity with live Knowledge Map withheld",
        "",
        "~~~text",
        f"exact structure parity            {str(exact_structure_parity).lower()}",
        f"subject queries                    {sum(r['exact_match'] for r in subject_rows)} / {len(subject_rows)}",
        f"checkpoint queries                 {sum(r['exact_match'] for r in checkpoint_rows)} / {len(checkpoint_rows)}",
        f"specialized indexes                {str(specialized_exact).lower()}",
        "~~~",
        "",
        "The cold retrieval functions above operate only on the compact evidence after source parity is established. A flat path inventory has no deterministic subject-membership or checkpoint-topic relation and therefore cannot satisfy the same contract.",
        "",
    ]
    RESULT_MD.write_text("\n".join(lines).replace("~~~", fence), encoding="utf-8")
    print(json.dumps(result["mechanical_verdict"], indent=2))

if __name__ == "__main__":
    main()
