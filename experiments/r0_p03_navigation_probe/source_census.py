"""Read-only R0-P03 candidate source-pool census over one immutable Git commit.

This tool evaluates the feasibility and provenance of a proposed stratified corpus
frame. It deliberately does not choose the experiment's build carriers, held-out
carriers, task prompts, gold answers, semantic subject memberships, or governing
authority. In particular, no selection seed or held-out path list is published.

A source appearing in a Git tree establishes its existence as a historical
carrier at a specified repository revision. It does not establish that its
statements are currently authoritative under the selected future V03 semantics.

The pool definitions are proposal-stage sampling strata, not ontological
types, authority classes, navigation labels, or a proposed final directory tree.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from typing import Callable


# A separate, independent fixture-freeze step must select the actual source
# cohort and keep held-out paths inaccessible to the authors of comparison arms.
# Each stratum is proposed to contribute six build and two held-out carriers.
SPLIT_TARGET = {"build": 60, "heldout": 20}
PER_STRATUM_TARGET = {"build": 6, "heldout": 2}
STRATUM_ORDER = (
    "current_orientation",
    "foundations",
    "governing_specifications",
    "semantic_prior_research",
    "ao_assurance_research",
    "v03_r0_physical_research",
    "engineering_collaboration",
    "product_source_context",
    "historical_checkpoints",
    "other_research_evidence",
)

# These explicit anchors are prospective BUILD candidates. They ensure that
# known cross-plane, temporal and evidence responsibilities are represented,
# without exposing or preselecting the held-out sample. They may be challenged
# or replaced before any exact corpus freeze. Selection is never driven by the
# historical Research 217 annotation labels.
BUILD_ANCHORS = {
    "current_orientation": (
        "docs/ARCHITECTURE_PROGRAM_OVERVIEW.md",
        "docs/DECISIONS.md",
    ),
    "foundations": (
        "docs/foundations/014_knowledge_preservation_architecture_and_evolution.md",
        "docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md",
    ),
    "governing_specifications": (
        "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md",
        "docs/specifications/021_v1_dependency_backed_recommendation_action_value_vertical_slice.md",
    ),
    "semantic_prior_research": (
        "docs/research/217_w5_t1_v02_controlled_subject_architecture_acceptance.md",
        "docs/research/254_r7b_target_project_information_hierarchy_and_research218_supersession_candidate.md",
    ),
    "ao_assurance_research": (
        "docs/research/219_activation_orchestration_self_hosting_bootstrap_program.md",
        "docs/research/293_p_d1_warrant_proportionality_result.md",
    ),
    "v03_r0_physical_research": (
        "docs/research/507_r0_semantic_organization_and_external_execution_amendment.md",
        "docs/research/512_mc0030_claude_critique_reconciliation_governed_ledger_kernel_v02.md",
        "docs/research/555_r0_owner_authentication_direction_and_probe_gate_amendment.md",
    ),
    "engineering_collaboration": (
        "docs/local_execution/OPERATIONS.md",
        "docs/model_collaboration/README.md",
    ),
    "product_source_context": (
        "docs/cockpit/README.md",
        "docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md",
    ),
    "historical_checkpoints": (
        "docs/checkpoints/891_r0_owner_authentication_deferral_and_p03_resume.md",
        "docs/checkpoints/892_r0_p03_source_reconciliation_and_prefreeze_next.md",
    ),
    "other_research_evidence": (
        "docs/research/002_primary_project_cockpit_interface_concept.md",
        "docs/research/035_multi_model_development_collaboration_architecture.md",
    ),
}

REF_PATTERN = re.compile(r"[0-9a-f]{40}\Z")
NUMBERED_NAME = re.compile(r"(\d{3})_")


def numbered_id(path: str) -> int | None:
    match = NUMBERED_NAME.match(Path(path).name)
    return int(match.group(1)) if match else None


def belongs_to_stratum(name: str, path: str) -> bool:
    """Select by reproducible *source-frame* rules, never by presumed authority."""
    if not path.endswith(".md"):
        return False
    number = numbered_id(path)
    if name == "current_orientation":
        return path.startswith("docs/") and path.count("/") == 1
    if name == "foundations":
        return path.startswith("docs/foundations/")
    if name == "governing_specifications":
        return path.startswith("docs/specifications/")
    if name == "semantic_prior_research":
        return path.startswith("docs/research/") and number is not None and (
            124 <= number <= 218 or 240 <= number <= 263
        )
    if name == "ao_assurance_research":
        return path.startswith("docs/research/") and number is not None and (
            219 <= number <= 239 or 280 <= number <= 314
        )
    if name == "v03_r0_physical_research":
        return path.startswith("docs/research/") and number is not None and (
            437 <= number <= 556
        )
    if name == "engineering_collaboration":
        if path.startswith("docs/local_execution/"):
            return "/validation/" not in path or (
                number is not None and 200 <= number <= 249
            )
        if path.startswith("docs/model_collaboration/"):
            return "/messages/" not in path or "/MC-0030/" in path
        return False
    if name == "product_source_context":
        return path.startswith((
            "docs/cockpit/",
            "docs/source_universe/",
            "docs/methodological_knowledge/",
        ))
    if name == "historical_checkpoints":
        return path.startswith("docs/checkpoints/") and number is not None and (
            200 <= number <= 892
        )
    if name == "other_research_evidence":
        return path.startswith("docs/research/") and number is not None and (
            1 <= number <= 123 or 264 <= number <= 279
            or 315 <= number <= 436
        )
    raise ValueError(f"Unknown sampling stratum: {name}")


def committed_markdown_sources(repository: Path, source_ref: str) -> dict[str, str]:
    """Read path and blob identity from Git, never mutable working-tree content.

    Git object IDs bind actual source bytes at the chosen immutable public
    commit. They are provenance evidence, not semantic identity or assertions
    of source authority. The full revision must be provided explicitly so
    regenerating a source frame does not silently move it to the latest HEAD.
    """
    if not REF_PATTERN.fullmatch(source_ref):
        raise ValueError("source_ref must be a full 40-character lowercase commit SHA")

    proc = subprocess.run(
        ["git", "ls-tree", "-r", "-z", source_ref, "--", "docs"],
        cwd=repository, capture_output=True, check=True,
    )
    result: dict[str, str] = {}
    for entry in proc.stdout.split(b"\0"):
        if not entry:
            continue
        metadata, raw_path = entry.split(b"\t", 1)
        mode, kind, object_id = metadata.decode("ascii").split(" ")
        path = raw_path.decode("utf-8")
        if kind == "blob" and mode in {"100644", "100755"} and path.endswith(".md"):
            result[path] = object_id
    if not result:
        raise ValueError("No source files found at the specified revision")
    return result


def build_census(repository: Path, source_ref: str) -> dict[str, object]:
    """Prove each candidate pool exists and can support the proposed quotas.

    Pool entries and their hashes are reproducible from a frozen Git commit.
    The returned public summary intentionally omits non-anchor path lists,
    scenario keys, random seeds, exact sample choices and held-out membership.
    Independently separated fixture custodians must freeze those later.
    """
    sources = committed_markdown_sources(repository, source_ref)
    memberships: Counter[str] = Counter()
    strata: list[dict[str, object]] = []
    for name in STRATUM_ORDER:
        pool = sorted(
            (path, object_id)
            for path, object_id in sources.items()
            if belongs_to_stratum(name, path)
        )
        if len(pool) < sum(PER_STRATUM_TARGET.values()):
            raise ValueError(f"Stratum {name} has fewer than eight eligible path candidates")
        anchors = BUILD_ANCHORS[name]
        if len(set(anchors)) != len(anchors) or len(anchors) > PER_STRATUM_TARGET["build"]:
            raise ValueError(f"Invalid unique BUILD-anchor count in {name}")
        for path in anchors:
            if path not in dict(pool):
                raise ValueError(f"Build anchor absent from frozen source pool: {path}")
        for path, _ in pool:
            memberships[path] += 1
        packed = "".join(
            f"{path}\0{object_id}\n" for path, object_id in pool
        ).encode("utf-8")
        strata.append({
            "name": name,
            "candidate_source_count": len(pool),
            "candidate_pool_digest_sha256": hashlib.sha256(packed).hexdigest(),
            "prospective_build_anchors": list(anchors),
            "target_build": PER_STRATUM_TARGET["build"],
            "target_heldout": PER_STRATUM_TARGET["heldout"],
        })
    overlapping = [name for name, count in memberships.items() if count > 1]
    if overlapping:
        raise ValueError(f"Source candidates assigned to multiple strata: {overlapping[:5]}")
    if len(set(sum((list(items) for items in BUILD_ANCHORS.values()), []))) != sum(
        len(items) for items in BUILD_ANCHORS.values()
    ):
        raise ValueError("The same build anchor belongs to multiple strata")
    return {
        "schema_version": 1,
        "classification": "UNFROZEN_SOURCE_FRAME_FEASIBILITY_ONLY",
        "source_ref": source_ref,
        "sample_plan": {
            "total": sum(SPLIT_TARGET.values()),
            **SPLIT_TARGET,
            "stratum_count": len(STRATUM_ORDER),
            "per_stratum": PER_STRATUM_TARGET,
        },
        "source_pool_size_unique_paths": len(memberships),
        "strata": strata,
        "limitations": [
            "Tracked Markdown path and Git blob identity do not establish current authority or qualifying semantic relevance.",
            "No selected build sample or held-out paths, salt, task keys, answer oracles, navigation arm outputs or evaluation scores are published.",
            "The 60/20 split must be selected and committed prospectively by a separated fixture custodian after semantic eligibility review.",
            "Build anchors are proposals only and cannot be credited as experimental results.",
            "All navigation arms must receive the same source provenance, semantic substrate, lexical search and derived orientation.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-ref", required=True, help="Full immutable Git commit SHA")
    parser.add_argument("--repository", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    print(json.dumps(build_census(args.repository.resolve(), args.source_ref), indent=2))


if __name__ == "__main__":
    main()
