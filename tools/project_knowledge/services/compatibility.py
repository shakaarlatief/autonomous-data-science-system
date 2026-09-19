"""W3 deterministic compatibility-shadow generation and comparison.

Candidate generation is independent of live compatibility content. The still-live
routing/current-state/Knowledge-Map files are read only during comparison.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
import hashlib
import json
from pathlib import Path

from ..adapters.generated_io import write_generated_bytes
from ..adapters.gitio import read_blobs
from ..model import AuthorityClass, LifecycleState, SnapshotMode, SubstrateError
from .semantic_validation import validate_project_knowledge
from .validation import validate_public_projection


SHADOW_ROOT = "docs/project_knowledge/generated/compatibility_shadow"
ROUTING_PATH = SHADOW_ROOT + "/current_routing.json"
CURRENT_STATE_PATH = SHADOW_ROOT + "/CURRENT_STATE.md"
KNOWLEDGE_MAP_PATH = SHADOW_ROOT + "/KNOWLEDGE_MAP.md"
ARTIFACT_INVENTORY_PATH = SHADOW_ROOT + "/artifact_inventory.json"
COMPARISON_REPORT_PATH = SHADOW_ROOT + "/comparison_report.json"

LIVE_ROUTING = "docs/current_routing.json"
LIVE_CURRENT_STATE = "docs/CURRENT_STATE.md"
LIVE_KNOWLEDGE_MAP = "docs/KNOWLEDGE_MAP.md"

GENERATOR_ID = "compatibility_shadow.w3"
GENERATOR_VERSION = "1"


class DifferenceClass(StrEnum):
    EXPECTED_SEMANTIC_IMPROVEMENT = "EXPECTED_SEMANTIC_IMPROVEMENT"
    EQUIVALENT_REPRESENTATION = "EQUIVALENT_REPRESENTATION"
    MIGRATION_GAP = "MIGRATION_GAP"
    LEGACY_DRIFT = "LEGACY_DRIFT"
    UNRESOLVED = "UNRESOLVED"


BLOCKING_CLASSES = frozenset(
    {DifferenceClass.MIGRATION_GAP, DifferenceClass.UNRESOLVED}
)


@dataclass(frozen=True)
class CompatibilityArtifact:
    role: str
    path: str
    content: bytes

    @property
    def digest(self) -> str:
        return hashlib.sha256(self.content).hexdigest()


@dataclass(frozen=True)
class CompatibilityDifference:
    difference_id: str
    role: str
    classification: DifferenceClass
    rationale: str

    @property
    def blocking(self) -> bool:
        return self.classification in BLOCKING_CLASSES


@dataclass(frozen=True)
class CompatibilityShadow:
    source_commit: str
    source_boundary: str
    artifacts: tuple[CompatibilityArtifact, ...]
    differences: tuple[CompatibilityDifference, ...]

    @property
    def blocking(self) -> bool:
        return any(item.blocking for item in self.differences)

    def artifact(self, role: str) -> CompatibilityArtifact:
        matches = tuple(item for item in self.artifacts if item.role == role)
        if len(matches) != 1:
            raise SubstrateError(
                "COMPATIBILITY_SHADOW_ROLE_CARDINALITY",
                f"Expected exactly one compatibility artifact for role: {role}",
            )
        return matches[0]


def _json_bytes(value) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")


def _require_commit(snapshot) -> None:
    if snapshot.mode != SnapshotMode.COMMIT_SNAPSHOT or snapshot.source_commit is None:
        raise SubstrateError(
            "NON_COMMITTED_COMPATIBILITY_SHADOW",
            "W3 compatibility candidates require one exact committed repository snapshot.",
        )


def _canonical_sources(snapshot):
    validation = validate_project_knowledge(snapshot, durable_evidence=True)
    if not validation.ok:
        details = "; ".join(
            f"{item.code}:{item.carrier_path}"
            for item in validation.diagnostics
        )
        raise SubstrateError(
            "INVALID_COMPATIBILITY_SOURCE_STATE",
            "Successor semantic owners must validate before W3 generation. " + details,
        )
    return tuple(
        source
        for source in validation.repository.sources
        if source.authority_class == AuthorityClass.CANONICAL
        and source.state != LifecycleState.SUPERSEDED
    )


def _one_source(sources, semantic_id: str):
    matches = tuple(
        source
        for source in sources
        if source.semantic_id is not None
        and source.semantic_id.value == semantic_id
    )
    if len(matches) != 1:
        raise SubstrateError(
            "COMPATIBILITY_SOURCE_CARDINALITY",
            f"Expected exactly one canonical source for {semantic_id}.",
        )
    return matches[0]


def _one_kind(sources, kind: str):
    matches = tuple(
        source
        for source in sources
        if source.declaration.fields.get("kind") == kind
    )
    if len(matches) != 1:
        raise SubstrateError(
            "COMPATIBILITY_SOURCE_CARDINALITY",
            f"Expected exactly one canonical source for kind {kind}.",
        )
    return matches[0]


def _successor_model(sources):
    active = _one_source(sources, "WS-PKA-CURRENT")
    boundary = _one_source(sources, "PROJECT-INTEGRATION-BOUNDARY")
    specification = _one_kind(sources, "SPECIFICATION")
    experiment = _one_kind(sources, "EXPERIMENT_RESULT")

    active_fields = active.declaration.fields
    anchor = active_fields["execution_anchor"]
    stage = active_fields["stage"]
    specification_id = specification.semantic_id.value
    if not specification_id.startswith("SPECIFICATION:"):
        raise SubstrateError(
            "INVALID_COMPATIBILITY_SPECIFICATION_ID",
            "Current specification identity must use SPECIFICATION:<number>.",
        )

    paused = []
    for source in sorted(
        (
            item
            for item in sources
            if item.declaration.fields.get("profile") == "workstream.v1"
            and item.state == LifecycleState.PAUSED
            and item.declaration.fields.get("expected_to_resume") is True
        ),
        key=lambda item: item.semantic_id.value,
    ):
        fields = source.declaration.fields
        row = {
            "semantic_id": source.semantic_id.value,
            "state": source.state.value,
            "resume_target": fields["resume_target"],
            "return_condition": fields["return_condition"],
            "source_path": source.carrier_path,
        }
        if "governing_procedure" in fields:
            row["governing_procedure"] = fields["governing_procedure"]
        if "orientation_milestones" in fields:
            row["orientation_milestones"] = sorted(
                fields["orientation_milestones"],
                key=lambda item: item["milestone_id"],
            )
        paused.append(row)

    routing = {
        "schema_version": 1,
        "current_checkpoint": anchor["checkpoint"],
        "active_development_branch": anchor["development_branch"],
        "active_pr": anchor["pull_request"],
        "promoted_integration_branch": boundary.declaration.fields["promoted_branch"],
        "promoted_integration_sha": boundary.declaration.fields["promoted_commit"],
        "latest_specification": specification_id.split(":", 1)[1],
        "latest_experiment_outcome": experiment.declaration.fields["outcome"],
        "current_boundary": anchor["current_boundary"],
    }
    return {
        "routing": routing,
        "active": {
            "semantic_id": active.semantic_id.value,
            "state": active.state.value,
            "objective": active_fields["objective"],
            "stage_id": stage["stage_id"],
            "stage_state": stage["stage_state"],
            "source_path": active.carrier_path,
        },
        "boundary": {
            "semantic_id": boundary.semantic_id.value,
            "source_path": boundary.carrier_path,
        },
        "specification": {
            "semantic_id": specification_id,
            "source_path": specification.carrier_path,
        },
        "experiment": {
            "semantic_id": experiment.semantic_id.value,
            "outcome": experiment.declaration.fields["outcome"],
            "source_path": experiment.carrier_path,
        },
        "paused": paused,
    }


def _artifact_inventory(snapshot, sources):
    semantic_by_path = {
        source.carrier_path: source.semantic_id.value
        for source in sources
        if source.semantic_id is not None
    }
    artifacts = []
    group_counts = {}
    for entry in sorted(snapshot.entries, key=lambda item: item.path):
        path = entry.path
        if not path.startswith("docs/"):
            continue
        if path.startswith("docs/project_knowledge/generated/"):
            continue
        if entry.git_mode not in {"100644", "100755"}:
            continue
        parts = path.split("/")
        group = parts[1] if len(parts) > 2 else "<docs-root>"
        group_counts[group] = group_counts.get(group, 0) + 1
        row = {
            "path": path,
            "group": group,
            "suffix": Path(path).suffix.lower() or "<none>",
        }
        if path in semantic_by_path:
            row["semantic_id"] = semantic_by_path[path]
        artifacts.append(row)

    tree_material = "\n".join(
        item["path"] + "\0" + item["group"] + "\0" + item["suffix"]
        for item in artifacts
    ).encode("utf-8")
    return {
        "schema_version": "1",
        "authority_class": "derived",
        "artifact_count": len(artifacts),
        "artifact_tree_digest": hashlib.sha256(tree_material).hexdigest(),
        "groups": [
            {"group": group, "artifact_count": count}
            for group, count in sorted(group_counts.items())
        ],
        "artifacts": artifacts,
    }


def _source_boundary(sources, inventory) -> str:
    records = []
    for source in sorted(sources, key=lambda item: item.carrier_path):
        if source.revision is None:
            raise SubstrateError(
                "MISSING_COMPATIBILITY_SOURCE_REVISION",
                "Committed compatibility inputs require exact source revisions.",
            )
        records.append(
            source.carrier_path + "\0" + source.revision.content_digest
        )
    records.append("artifact-tree\0" + inventory["artifact_tree_digest"])
    material = "\n".join(records).encode("utf-8")
    return "sha256:" + hashlib.sha256(material).hexdigest()


def _subject_rows(sources):
    rows = []
    for source in sorted(
        (item for item in sources if item.semantic_id is not None),
        key=lambda item: (item.semantic_id.value, item.carrier_path),
    ):
        fields = source.declaration.fields
        rows.append(
            {
                "axis": "kind",
                "value": fields["kind"],
                "semantic_id": source.semantic_id.value,
                "source_path": source.carrier_path,
            }
        )
        rows.append(
            {
                "axis": "profile",
                "value": fields["profile"],
                "semantic_id": source.semantic_id.value,
                "source_path": source.carrier_path,
            }
        )
        for key in sorted(fields.get("scope", {})):
            value = fields["scope"][key]
            values = (value,) if isinstance(value, str) else tuple(sorted(value))
            for scoped in values:
                rows.append(
                    {
                        "axis": "scope:" + key,
                        "value": scoped,
                        "semantic_id": source.semantic_id.value,
                        "source_path": source.carrier_path,
                    }
                )
    return tuple(
        sorted(
            rows,
            key=lambda item: (
                item["axis"],
                item["value"],
                item["semantic_id"],
                item["source_path"],
            ),
        )
    )


def _current_state_markdown(model) -> bytes:
    routing = model["routing"]
    active = model["active"]
    lines = [
        "# Current State",
        "",
        f"Checkpoint: {routing['current_checkpoint']}",
        f"Active development branch: {routing['active_development_branch']}",
        f"Active PR: {'none' if routing['active_pr'] is None else routing['active_pr']}",
        (
            "Promoted integration boundary: "
            + routing["promoted_integration_branch"]
            + " at "
            + routing["promoted_integration_sha"]
        ),
        "Latest specification: Specification " + routing["latest_specification"],
        "Latest scientific experiment outcome: " + routing["latest_experiment_outcome"],
        "",
        "## Active migration workstream",
        "",
        "- Semantic ID: " + active["semantic_id"],
        "- State: " + active["state"],
        "- Stage: " + active["stage_id"] + " / " + active["stage_state"],
        "- Boundary: " + routing["current_boundary"],
        "- Canonical owner: " + active["source_path"],
        "- Objective: " + active["objective"],
        "",
        "## Operational authority",
        "",
        "- Current operational authority remains the current continuity architecture.",
        "- AUTHORITY_SWITCH_ALLOWED=false until the separately qualified W8 decision.",
        "- This compatibility candidate is derived and non-authoritative.",
        "",
        "## Paused resumable workstreams",
        "",
    ]
    for item in model["paused"]:
        lines.extend(
            [
                "### " + item["semantic_id"],
                "",
                "- State: " + item["state"],
                "- Resume target: " + item["resume_target"],
                "- Return condition: " + item["return_condition"],
                "- Canonical owner: " + item["source_path"],
            ]
        )
        if "governing_procedure" in item:
            lines.append("- Governing procedure: " + item["governing_procedure"])
        for milestone in item.get("orientation_milestones", []):
            lines.append(
                "- Milestone "
                + milestone["milestone_id"]
                + ": "
                + milestone["state"]
            )
        lines.append("")

    lines.extend(
        [
            "## Canonical current controls",
            "",
            (
                "- Project Integration Boundary: "
                + model["boundary"]["semantic_id"]
                + " in "
                + model["boundary"]["source_path"]
            ),
            (
                "- Current specification: "
                + model["specification"]["semantic_id"]
                + " in "
                + model["specification"]["source_path"]
            ),
            (
                "- Current experiment result: "
                + model["experiment"]["semantic_id"]
                + " / "
                + model["experiment"]["outcome"]
                + " in "
                + model["experiment"]["source_path"]
            ),
            "",
            "## Navigation",
            "",
            "- Structural views: docs/project_knowledge/generated/",
            "- Compatibility artifact inventory: "
            + ARTIFACT_INVENTORY_PATH,
            "- Compatibility Knowledge Map candidate: " + KNOWLEDGE_MAP_PATH,
            "",
            (
                "Historical checkpoints, research evidence and deep project history remain "
                "reachable through repository history and the artifact inventory rather than "
                "being copied into this current-orientation view."
            ),
            "",
        ]
    )
    return "\n".join(lines).encode("utf-8")


def _knowledge_map_markdown(sources, inventory) -> bytes:
    grouped = {}
    for row in _subject_rows(sources):
        grouped.setdefault((row["axis"], row["value"]), []).append(row)

    lines = [
        "# Knowledge Map",
        "",
        "Status: Derived W3 compatibility-shadow candidate / non-authoritative",
        "",
        "## Purpose",
        "",
        (
            "Provide semantic navigation for governed successor knowledge while preserving "
            "complete repository-document reachability through a deterministic artifact inventory."
        ),
        "",
        "## Governed semantic navigation",
        "",
    ]
    for (axis, value), memberships in sorted(grouped.items()):
        lines.extend(["### " + axis + " = " + value, ""])
        for item in memberships:
            lines.append(
                "- " + item["semantic_id"] + " -> " + item["source_path"]
            )
        lines.append("")

    lines.extend(
        [
            "## Repository artifact inventory",
            "",
            (
                "The exact committed documentation inventory contains "
                + str(inventory["artifact_count"])
                + " non-generated artifacts."
            ),
            "",
            "Machine-readable inventory: " + ARTIFACT_INVENTORY_PATH,
            "",
            "Top-level documentation groups:",
            "",
        ]
    )
    for item in inventory["groups"]:
        lines.append(
            "- " + item["group"] + ": " + str(item["artifact_count"])
        )
    lines.extend(
        [
            "",
            "## Navigation contract",
            "",
            (
                "Semantic subjects are multi-axis and non-exclusive. The artifact inventory is "
                "the high-recall fallback for knowledge not yet migrated into explicit semantic "
                "subject declarations."
            ),
            (
                "Appearance in this view does not establish authority. Task-scoped authority "
                "resolution remains separate from retrieval/navigation."
            ),
            "",
        ]
    )
    return "\n".join(lines).encode("utf-8")


def build_shadow_candidates(snapshot):
    """Build W3 candidates without reading live compatibility content."""
    _require_commit(snapshot)
    sources = _canonical_sources(snapshot)
    model = _successor_model(sources)
    inventory = _artifact_inventory(snapshot, sources)
    source_boundary = _source_boundary(sources, inventory)
    inventory["source_boundary"] = source_boundary
    artifacts = (
        CompatibilityArtifact("routing", ROUTING_PATH, _json_bytes(model["routing"])),
        CompatibilityArtifact(
            "current_state",
            CURRENT_STATE_PATH,
            _current_state_markdown(model),
        ),
        CompatibilityArtifact(
            "knowledge_map",
            KNOWLEDGE_MAP_PATH,
            _knowledge_map_markdown(sources, inventory),
        ),
        CompatibilityArtifact(
            "artifact_inventory",
            ARTIFACT_INVENTORY_PATH,
            _json_bytes(inventory),
        ),
    )
    diagnostics = []
    for artifact in artifacts:
        diagnostics.extend(validate_public_projection(artifact.content, artifact.path))
    if diagnostics:
        raise SubstrateError(
            "UNSAFE_COMPATIBILITY_SHADOW",
            "; ".join(
                item.code + ":" + item.carrier_path for item in diagnostics
            ),
        )
    return snapshot.source_commit, source_boundary, sources, model, inventory, artifacts


def _read_committed_paths(snapshot, paths):
    entries = {entry.path: entry for entry in snapshot.entries}
    missing = tuple(sorted(set(paths) - entries.keys()))
    if missing:
        raise SubstrateError(
            "MISSING_COMPATIBILITY_SURFACE",
            "Missing live compatibility surface(s): " + ", ".join(missing),
        )
    selected = tuple(entries[path] for path in sorted(paths))
    raw = read_blobs(snapshot.root, selected)
    return {entry.path: raw[entry.blob_id] for entry in selected}


def _knowledge_map_references(text: str):
    references = []
    for raw in text.splitlines():
        line = raw.strip().replace(chr(96), "")
        if not line.startswith("docs/"):
            continue
        token = line.split()[0]
        references.append(token)
    return tuple(sorted(set(references)))


def _difference(difference_id, role, classification, rationale):
    return CompatibilityDifference(
        difference_id,
        role,
        DifferenceClass(classification),
        rationale,
    )


def compare_shadow_to_live(snapshot, model, inventory, artifacts):
    """Compare candidates to live surfaces without making those surfaces inputs."""
    _require_commit(snapshot)
    live = _read_committed_paths(
        snapshot,
        (LIVE_ROUTING, LIVE_CURRENT_STATE, LIVE_KNOWLEDGE_MAP),
    )
    routing_candidate = json.loads(
        next(item.content for item in artifacts if item.role == "routing").decode("utf-8")
    )
    live_routing = json.loads(live[LIVE_ROUTING].decode("utf-8"))
    differences = []

    if routing_candidate == live_routing:
        differences.append(
            _difference(
                "routing.semantic-parity",
                "routing",
                DifferenceClass.EQUIVALENT_REPRESENTATION,
                "Successor routing reproduces the exact live routing schema and values.",
            )
        )
    else:
        differences.append(
            _difference(
                "routing.semantic-parity",
                "routing",
                DifferenceClass.MIGRATION_GAP,
                "Successor routing does not reproduce the live routing contract.",
            )
        )

    current_text = live[LIVE_CURRENT_STATE].decode("utf-8")
    routing = model["routing"]
    current_markers = (
        "**Checkpoint:** " + str(routing["current_checkpoint"]),
        "**Active development branch:** " + chr(96)
        + routing["active_development_branch"] + chr(96),
        routing["promoted_integration_branch"],
        routing["promoted_integration_sha"],
        "Specification " + routing["latest_specification"],
        routing["latest_experiment_outcome"],
        routing["current_boundary"],
        "authority_switch_allowed=false",
    )
    missing_markers = tuple(
        marker for marker in current_markers if marker not in current_text
    )
    if missing_markers:
        differences.append(
            _difference(
                "current-state.control-parity",
                "current_state",
                DifferenceClass.MIGRATION_GAP,
                "Live current-state control facts disagree or are absent: "
                + ", ".join(missing_markers),
            )
        )
    else:
        differences.append(
            _difference(
                "current-state.control-parity",
                "current_state",
                DifferenceClass.EQUIVALENT_REPRESENTATION,
                "Successor orientation preserves the live high-consequence current controls.",
            )
        )

    differences.append(
        _difference(
            "current-state.history-compaction",
            "current_state",
            DifferenceClass.EXPECTED_SEMANTIC_IMPROVEMENT,
            "Successor current state points to canonical owners instead of replaying accumulated checkpoint and research history.",
        )
    )
    stale_phrase = (
        "while Research 124 project-knowledge architecture qualification "
        "has routing priority"
    )
    if stale_phrase in current_text:
        differences.append(
            _difference(
                "current-state.legacy-source-vault-route",
                "current_state",
                DifferenceClass.LEGACY_DRIFT,
                "The live surface retains an older Research 124 Source Vault route sentence; successor continuation uses durable return semantics.",
            )
        )

    map_text = live[LIVE_KNOWLEDGE_MAP].decode("utf-8")
    references = _knowledge_map_references(map_text)
    inventory_paths = {item["path"] for item in inventory["artifacts"]}
    missing_references = []
    for reference in references:
        if reference.endswith("/"):
            if not any(path.startswith(reference) for path in inventory_paths):
                missing_references.append(reference)
        elif reference not in inventory_paths:
            missing_references.append(reference)
    if missing_references:
        differences.append(
            _difference(
                "knowledge-map.artifact-reachability",
                "knowledge_map",
                DifferenceClass.MIGRATION_GAP,
                "Legacy Knowledge Map references missing from successor inventory: "
                + ", ".join(sorted(missing_references)),
            )
        )
    else:
        differences.append(
            _difference(
                "knowledge-map.artifact-reachability",
                "knowledge_map",
                DifferenceClass.EQUIVALENT_REPRESENTATION,
                "All "
                + str(len(references))
                + " unique legacy path/directory references remain reachable.",
            )
        )

    differences.append(
        _difference(
            "knowledge-map.organization",
            "knowledge_map",
            DifferenceClass.EXPECTED_SEMANTIC_IMPROVEMENT,
            "Successor navigation separates multi-axis semantic membership from complete artifact inventory instead of indefinite manual path enumeration.",
        )
    )
    return tuple(sorted(differences, key=lambda item: item.difference_id))


def build_compatibility_shadow(snapshot) -> CompatibilityShadow:
    source_commit, source_boundary, sources, model, inventory, artifacts = build_shadow_candidates(snapshot)
    differences = compare_shadow_to_live(snapshot, model, inventory, artifacts)
    provisional = CompatibilityShadow(source_commit, source_boundary, artifacts, differences)
    report = {
        "schema_version": "1",
        "authority_class": "derived",
        "generator": {
            "generator_id": GENERATOR_ID,
            "generator_version": GENERATOR_VERSION,
        },
        "source_boundary": source_boundary,
        "blocking": provisional.blocking,
        "candidates": [
            {
                "role": item.role,
                "path": item.path,
                "sha256": item.digest,
                "byte_length": len(item.content),
            }
            for item in artifacts
        ],
        "differences": [
            {
                "difference_id": item.difference_id,
                "role": item.role,
                "classification": item.classification.value,
                "blocking": item.blocking,
                "rationale": item.rationale,
            }
            for item in differences
        ],
    }
    report_artifact = CompatibilityArtifact(
        "comparison_report",
        COMPARISON_REPORT_PATH,
        _json_bytes(report),
    )
    diagnostics = validate_public_projection(
        report_artifact.content,
        report_artifact.path,
    )
    if diagnostics:
        raise SubstrateError(
            "UNSAFE_COMPATIBILITY_SHADOW",
            "; ".join(
                item.code + ":" + item.carrier_path for item in diagnostics
            ),
        )
    return CompatibilityShadow(
        source_commit,
        source_boundary,
        (*artifacts, report_artifact),
        differences,
    )


def materialize_compatibility_shadow(root: Path, shadow: CompatibilityShadow) -> None:
    if shadow.blocking:
        raise SubstrateError(
            "BLOCKING_COMPATIBILITY_DIFFERENCE",
            "W3 materialization is blocked by MIGRATION_GAP or UNRESOLVED differences.",
        )
    for artifact in shadow.artifacts:
        write_generated_bytes(root, artifact.path, artifact.content)
