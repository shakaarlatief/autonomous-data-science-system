from __future__ import annotations

import json
import re
import statistics
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CATALOG = HERE / "subject_catalog_candidate.json"
ANNOTATIONS = HERE / "corpus_annotations.json"
SCENARIOS = HERE / "navigation_scenarios.json"
RESULT_JSON = HERE / "result.json"
PROJECTION_JSON = HERE / "candidate_projection.json"
RESULT_MD = HERE / "RESULT.md"

def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def git_show(ref: str, path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{ref}:{path}"],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
    )

def git_path_exists(ref: str, path: str) -> bool:
    proc = subprocess.run(
        ["git", "cat-file", "-e", f"{ref}:{path}"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return proc.returncode == 0

def parse_legacy_memberships(text: str):
    by_path = defaultdict(set)
    current_topic = None
    in_fence = False
    for raw in text.splitlines():
        line = raw.strip()
        if raw.startswith("### "):
            current_topic = None
            in_fence = False
            continue
        m = re.fullmatch(r"<!--\s*KM-TOPIC:\s*([^\s]+)\s*-->", line)
        if m:
            current_topic = m.group(1)
            continue
        if line == "~~~text":
            in_fence = True
            continue
        if line == "~~~":
            in_fence = False
            continue
        if current_topic and in_fence and line.startswith("docs/"):
            by_path[line].add(current_topic)
    return {k: sorted(v) for k, v in by_path.items()}

def ancestors(subject_id: str, subjects_by_id: dict[str, dict]):
    out = set()
    stack = list(subjects_by_id[subject_id]["broader"])
    while stack:
        parent = stack.pop()
        if parent in out:
            continue
        out.add(parent)
        stack.extend(subjects_by_id[parent]["broader"])
    return out

def score(result_set: set[str], scenario: dict):
    must = set(scenario["must_retrieve"])
    must_not = set(scenario["must_not_retrieve"])
    return {
        "result_count": len(result_set),
        "must_recall": len(must & result_set) / len(must),
        "must_not_rejection": len(must_not - result_set) / len(must_not),
        "missing_must": sorted(must - result_set),
        "returned_distractors": sorted(must_not & result_set),
    }

def main():
    catalog = load(CATALOG)
    annotations_doc = load(ANNOTATIONS)
    scenarios_doc = load(SCENARIOS)

    boundaries = {
        catalog["source_boundary"],
        annotations_doc["source_boundary"],
        scenarios_doc["source_boundary"],
    }
    assert len(boundaries) == 1, boundaries
    source_boundary = next(iter(boundaries))

    subjects = catalog["subjects"]
    by_id = {s["id"]: s for s in subjects}
    assert len(by_id) == len(subjects)
    assignable = {s["id"] for s in subjects if s["assignable"]}

    forbidden_membership_keys = {"members", "member_paths", "memberships", "sources", "source_paths"}
    for subject in subjects:
        assert not forbidden_membership_keys.intersection(subject), subject["id"]
        for parent in subject["broader"]:
            assert parent in by_id, (subject["id"], parent)
        preferred_parent = subject["preferred_parent"]
        if preferred_parent is not None:
            assert preferred_parent in subject["broader"], subject["id"]

    for sid in by_id:
        assert sid not in ancestors(sid, by_id), f"cycle at {sid}"

    annotations = annotations_doc["annotations"]
    paths = [a["path"] for a in annotations]
    assert len(paths) == len(set(paths))
    for a in annotations:
        assert git_path_exists(source_boundary, a["path"]), a["path"]
        assert a["subjects"], a["path"]
        assert len(a["subjects"]) == len(set(a["subjects"])), a["path"]
        assert set(a["subjects"]) <= assignable, a["path"]
        preferred = a["preferred_subject"]
        assert preferred is None or preferred in a["subjects"], a["path"]

    fence = chr(96) * 3
    legacy_text = git_show(source_boundary, "docs/KNOWLEDGE_MAP.md").replace(fence + "text", "~~~text").replace(fence, "~~~")
    legacy = parse_legacy_memberships(legacy_text)

    candidate_members = defaultdict(list)
    preferred_members = defaultdict(list)
    parent_rollup = defaultdict(set)
    for a in annotations:
        for sid in a["subjects"]:
            candidate_members[sid].append(a["path"])
            for parent in ancestors(sid, by_id):
                parent_rollup[parent].add(a["path"])
        if a["preferred_subject"] is not None:
            preferred_members[a["preferred_subject"]].append(a["path"])

    counts = {sid: len(candidate_members[sid]) for sid in sorted(assignable)}
    membership_lengths = [len(a["subjects"]) for a in annotations]
    zero_member = sorted(sid for sid, count in counts.items() if count == 0)
    singleton = sorted(sid for sid, count in counts.items() if count == 1)

    legacy_covered = [a for a in annotations if legacy.get(a["path"])]
    aligned = 0
    evaluable = 0
    alignment_rows = []
    for a in annotations:
        preferred = a["preferred_subject"]
        legacy_topics = set(legacy.get(a["path"], []))
        if preferred is None or not legacy_topics:
            continue
        equivalents = set(by_id[preferred]["legacy_topics"])
        if not equivalents:
            continue
        evaluable += 1
        ok = bool(equivalents & legacy_topics)
        aligned += int(ok)
        alignment_rows.append({
            "path": a["path"],
            "preferred_subject": preferred,
            "legacy_topics": sorted(legacy_topics),
            "legacy_equivalents": sorted(equivalents),
            "aligned": ok,
        })

    scenario_rows = []
    candidate_passes = 0
    legacy_passes = 0
    corpus_set = set(paths)
    for scenario in scenarios_doc["scenarios"]:
        assert set(scenario["must_retrieve"]) <= corpus_set
        assert set(scenario["must_not_retrieve"]) <= corpus_set

        candidate_result = {
            a["path"]
            for a in annotations
            if set(a["subjects"]) & set(scenario["candidate_subjects"])
        }
        legacy_result = {
            path
            for path in corpus_set
            if set(legacy.get(path, [])) & set(scenario["legacy_topics"])
        }
        candidate_score = score(candidate_result, scenario)
        legacy_score = score(legacy_result, scenario)
        candidate_pass = (
            candidate_score["must_recall"] == 1.0
            and candidate_score["must_not_rejection"] == 1.0
        )
        legacy_pass = (
            legacy_score["must_recall"] == 1.0
            and legacy_score["must_not_rejection"] == 1.0
        )
        candidate_passes += int(candidate_pass)
        legacy_passes += int(legacy_pass)
        scenario_rows.append({
            "id": scenario["id"],
            "candidate_subjects": scenario["candidate_subjects"],
            "legacy_topics": scenario["legacy_topics"],
            "candidate": candidate_score | {"pass": candidate_pass},
            "legacy": legacy_score | {"pass": legacy_pass},
        })

    projection = {
        "schema_version": 1,
        "experiment": "W5-T1",
        "authority_class": "research_output",
        "source_boundary": source_boundary,
        "subjects": [
            {
                "id": s["id"],
                "label": s["label"],
                "assignable": s["assignable"],
                "broader": s["broader"],
                "preferred_parent": s["preferred_parent"],
                "members": sorted(candidate_members.get(s["id"], [])),
                "preferred_members": sorted(preferred_members.get(s["id"], [])),
                "rolled_up_members": sorted(parent_rollup.get(s["id"], set())),
            }
            for s in subjects
        ],
    }

    metrics = {
        "schema_version": 1,
        "experiment": "W5-T1",
        "authority_class": "research_output",
        "source_boundary": source_boundary,
        "corpus_count": len(annotations),
        "catalog_subject_count": len(subjects),
        "assignable_subject_count": len(assignable),
        "membership_count": sum(membership_lengths),
        "memberships_per_artifact_mean": sum(membership_lengths) / len(membership_lengths),
        "memberships_per_artifact_median": statistics.median(membership_lengths),
        "multi_subject_artifact_count": sum(1 for n in membership_lengths if n > 1),
        "multi_subject_artifact_fraction": sum(1 for n in membership_lengths if n > 1) / len(membership_lengths),
        "no_unique_preferred_route_count": sum(1 for a in annotations if a["preferred_subject"] is None),
        "per_subject_member_count": counts,
        "zero_member_subjects": zero_member,
        "singleton_subjects": singleton,
        "legacy_covered_artifact_count": len(legacy_covered),
        "legacy_coverage_fraction": len(legacy_covered) / len(annotations),
        "preferred_route_legacy_alignment": {
            "evaluable": evaluable,
            "aligned": aligned,
            "fraction": (aligned / evaluable) if evaluable else None,
            "rows": alignment_rows,
        },
        "scenario_summary": {
            "scenario_count": len(scenario_rows),
            "candidate_pass_count": candidate_passes,
            "legacy_pass_count": legacy_passes,
        },
        "scenarios": scenario_rows,
    }

    PROJECTION_JSON.write_text(json.dumps(projection, indent=2) + "\n", encoding="utf-8")
    RESULT_JSON.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")

    tick = chr(96)
    lines = [
        "# W5 T1 Controlled Subject Vocabulary Result",
        "",
        f"**Source boundary:** {tick}{source_boundary}{tick}",
        "**Authority:** Non-authoritative research output.",
        "",
        "## Corpus and grouping",
        "",
        "~~~text",
        f"corpus artifacts                 {metrics['corpus_count']}",
        f"assignable subjects              {metrics['assignable_subject_count']}",
        f"total memberships                {metrics['membership_count']}",
        f"mean memberships/artifact        {metrics['memberships_per_artifact_mean']:.3f}",
        f"median memberships/artifact      {metrics['memberships_per_artifact_median']}",
        f"multi-subject artifacts          {metrics['multi_subject_artifact_count']} ({metrics['multi_subject_artifact_fraction']:.1%})",
        f"no unique preferred route        {metrics['no_unique_preferred_route_count']}",
        f"zero-member subjects             {len(zero_member)}",
        f"singleton subjects               {len(singleton)}",
        "~~~",
        "",
        "## Subject sizes",
        "",
        "~~~text",
    ]
    for sid, count in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"{sid:32s} {count}")
    lines += [
        "~~~",
        "",
        "## Legacy continuity",
        "",
        "~~~text",
        f"legacy Knowledge Map coverage    {metrics['legacy_covered_artifact_count']} / {metrics['corpus_count']} ({metrics['legacy_coverage_fraction']:.1%})",
        f"preferred-route legacy alignment {aligned} / {evaluable}" + (f" ({aligned/evaluable:.1%})" if evaluable else ""),
        "~~~",
        "",
        "## Navigation scenarios",
        "",
        "| Scenario | Candidate pass | Candidate results | Legacy pass | Legacy results |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for row in scenario_rows:
        lines.append(
            f"| {row['id']} | {str(row['candidate']['pass']).lower()} | {row['candidate']['result_count']} | "
            f"{str(row['legacy']['pass']).lower()} | {row['legacy']['result_count']} |"
        )
    lines += [
        "",
        "A scenario passes only when every must-retrieve artifact is present and every explicit distractor is rejected.",
        "",
        "## Mechanical verdict",
        "",
        "~~~text",
        f"candidate scenario passes        {candidate_passes} / {len(scenario_rows)}",
        f"legacy scenario passes           {legacy_passes} / {len(scenario_rows)}",
        "~~~",
        "",
        "No architectural acceptance is inferred mechanically. Research interpretation must consider vocabulary quality, subject overfitting, corpus representativeness, authoring burden and whether the controlled vocabulary remains distinct from resolver/structural facets.",
        "",
    ]
    RESULT_MD.write_text("\n".join(lines).replace("~~~", fence), encoding="utf-8")

    print(json.dumps({
        "source_boundary": source_boundary,
        "corpus_count": len(annotations),
        "assignable_subject_count": len(assignable),
        "zero_member_subjects": zero_member,
        "singleton_subjects": singleton,
        "candidate_scenario_passes": candidate_passes,
        "legacy_scenario_passes": legacy_passes,
        "legacy_alignment": {"aligned": aligned, "evaluable": evaluable},
    }, indent=2))

if __name__ == "__main__":
    main()
