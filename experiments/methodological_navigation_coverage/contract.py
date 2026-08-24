"""Provider-free contract machinery for Specification 022.

This module owns the frozen fixture integrity checks, deterministic project-state
projection, randomized request plan, experiment-owned structured result types,
reasoner request construction, deterministic exact/alias prematching, and
blinded semantic-judge request construction. It imports no provider SDK and
performs no authoritative project mutation.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import StrEnum
import hashlib
import inspect
import json
from pathlib import Path
import random
import re
from typing import Any, Mapping, Sequence

from ads_system.application.reasoning import (
    KnowledgeRevisionPointer,
    ReasoningModelConfiguration,
    ReasoningRequest,
)

ROOT = Path(__file__).resolve().parents[2]
FIXTURE_DIR = ROOT / "tests" / "fixtures" / "methodological_navigation"
UNIVERSE_PATH = FIXTURE_DIR / "spec022_methodological_universe_v1.json"
EPISODES_PATH = FIXTURE_DIR / "spec022_project_state_episodes_v1.json"
ORACLE_PATH = FIXTURE_DIR / "spec022_coverage_oracle_v1.json"
REPRESENTATION_MAP_PATH = FIXTURE_DIR / "spec022_oracle_representation_map_v1.json"
MANIFEST_PATH = FIXTURE_DIR / "spec022_contract_fixture_manifest_v1.json"

EXPECTED_CANONICAL_SHA256 = {
    "spec022_coverage_oracle_v1.json": "e6774d8caed623d913a44a2bca1e6ed4861aa2e2b13a72f44f3df85f834b9eec",
    "spec022_methodological_universe_v1.json": "2e907c0de7dc5bfb01fbf4fef61de18f96ff6000b4a034aded7fb17ff1ff231e",
    "spec022_oracle_representation_map_v1.json": "186b554abbb5814333dc9b80611f3524ae5580242708b7add65897bb51374e49",
    "spec022_project_state_episodes_v1.json": "8650dac2f3332b29553cc8d076c40067361c51bdb489220f6e9101e11b09cc45",
}

CONDITIONS = ("ADS_HORIZON", "GENERIC", "ORACLE_HORIZON")
REPETITIONS = 3
RANDOMIZATION_SEED = 2026082403
PLANNED_REASONER_OBSERVATIONS = 108
PLANNED_JUDGE_OBSERVATIONS = 108
PLANNED_SUCCESSFUL_PROVIDER_CALLS = 216
MAX_TOTAL_PROVIDER_ATTEMPTS = 270
MAX_RETRIES_PER_OBSERVATION = 1
MAX_CONCERNS = 12

COMMON_INSTRUCTION = (
    "Review the current project state as a rigorous data-science methodologist. "
    "Surface the most important methodological concerns that currently deserve "
    "attention, including concerns that require missing information before they "
    "can be resolved. Do not assume a supplied list is exhaustive. Do not invent "
    "project facts. Focus on concerns that materially affect validity, evaluation, "
    "modelling choices, data quality, or defensibility now. Avoid repeating "
    "concerns that the project state shows are already resolved. Return at most "
    "twelve distinct concerns and ground each one in supplied project-object IDs."
)
USER_TASK = (
    "Identify the methodological concerns that deserve attention in the current "
    "project state."
)

REASONER_MODEL = ReasoningModelConfiguration(
    requested_model="gpt-5.6-sol",
    reasoning_effort="medium",
    verbosity="low",
    max_output_tokens=5000,
    store=False,
)
JUDGE_MODEL = ReasoningModelConfiguration(
    requested_model="gpt-5.6-sol",
    reasoning_effort="high",
    verbosity="low",
    max_output_tokens=4000,
    store=False,
)

JUDGE_INSTRUCTION = (
    "Act only as a blinded semantic adjudicator for methodological-coverage scoring. "
    "Match reasoner concern records to evaluator concern descriptions when they are "
    "semantically equivalent and project-state grounded. For matched concerns, judge "
    "whether CURRENT versus MISSING_CONTEXT is equivalent to the evaluator state and, "
    "when missing context is expected, whether the clarification question requests the "
    "missing prerequisite without inventing a project fact. Mark unsupported output "
    "records and semantic duplicates. Do not score prose style or infer a condition."
)


class CoverageCondition(StrEnum):
    ADS_HORIZON = "ADS_HORIZON"
    GENERIC = "GENERIC"
    ORACLE_HORIZON = "ORACLE_HORIZON"


class ConcernState(StrEnum):
    CURRENT = "CURRENT"
    MISSING_CONTEXT = "MISSING_CONTEXT"


class EvaluatorState(StrEnum):
    ACTIVE = "ACTIVE"
    MISSING_CONTEXT = "MISSING_CONTEXT"
    INACTIVE = "INACTIVE"
    RESOLVED = "RESOLVED"


@dataclass(frozen=True, slots=True)
class MethodologicalConcern:
    local_concern_id: str
    title: str
    explanation: str
    state: str
    grounding_project_object_ids: tuple[str, ...]
    missing_context_question: str | None

    def __post_init__(self) -> None:
        if not self.local_concern_id.strip():
            raise ValueError("local_concern_id must be non-empty")
        if not self.title.strip() or not self.explanation.strip():
            raise ValueError("concern title and explanation must be non-empty")
        try:
            normalized = ConcernState(self.state)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"unsupported concern state: {self.state!r}") from exc
        object.__setattr__(self, "state", normalized.value)
        if not 1 <= len(self.grounding_project_object_ids) <= 6:
            raise ValueError("grounding_project_object_ids must contain 1..6 IDs")
        if any(not item.strip() for item in self.grounding_project_object_ids):
            raise ValueError("grounding_project_object_ids cannot contain empty IDs")
        if len(self.grounding_project_object_ids) != len(
            set(self.grounding_project_object_ids)
        ):
            raise ValueError("grounding_project_object_ids must be unique")
        if normalized is ConcernState.CURRENT:
            if self.missing_context_question is not None:
                raise ValueError(
                    "CURRENT concern requires null missing_context_question"
                )
        elif (
            self.missing_context_question is None
            or not self.missing_context_question.strip()
        ):
            raise ValueError(
                "MISSING_CONTEXT concern requires a concrete clarification question"
            )

    def to_payload(self) -> dict[str, object]:
        return {
            "local_concern_id": self.local_concern_id,
            "title": self.title,
            "explanation": self.explanation,
            "state": self.state,
            "grounding_project_object_ids": list(
                self.grounding_project_object_ids
            ),
            "missing_context_question": self.missing_context_question,
        }


@dataclass(frozen=True, slots=True)
class MethodologicalCoverageResult:
    summary: str
    concerns: tuple[MethodologicalConcern, ...]
    warnings: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.summary.strip():
            raise ValueError("summary must be non-empty")
        if not 1 <= len(self.concerns) <= MAX_CONCERNS:
            raise ValueError(f"concerns must contain 1..{MAX_CONCERNS} records")
        ids = [item.local_concern_id for item in self.concerns]
        if len(ids) != len(set(ids)):
            raise ValueError(
                "local_concern_id values must be unique inside one result"
            )
        if any(not item.strip() for item in self.warnings):
            raise ValueError("warnings cannot contain empty strings")
        if len(self.warnings) != len(set(self.warnings)):
            raise ValueError("warnings must not contain duplicates")

    def to_payload(self) -> dict[str, object]:
        return {
            "summary": self.summary,
            "concerns": [item.to_payload() for item in self.concerns],
            "warnings": list(self.warnings),
        }


@dataclass(frozen=True, slots=True)
class SemanticMatch:
    local_concern_id: str
    oracle_id: str
    state_equivalent: bool
    missing_context_question_equivalent: bool | None


@dataclass(frozen=True, slots=True)
class SemanticAdjudicationResult:
    matches: tuple[SemanticMatch, ...]
    unsupported_local_concern_ids: tuple[str, ...]
    duplicate_local_concern_ids: tuple[str, ...]

    def to_payload(self) -> dict[str, object]:
        return {
            "matches": [asdict(item) for item in self.matches],
            "unsupported_local_concern_ids": list(
                self.unsupported_local_concern_ids
            ),
            "duplicate_local_concern_ids": list(
                self.duplicate_local_concern_ids
            ),
        }


@dataclass(frozen=True, slots=True)
class FrozenContract:
    universe: Mapping[str, Any]
    episodes: Mapping[str, Any]
    oracle: Mapping[str, Any]
    representation_map: Mapping[str, Any]
    manifest: Mapping[str, Any]


@dataclass(frozen=True, slots=True)
class ReasonerPlanEntry:
    observation_id: str
    run_id: str
    run_nonce: str
    episode_id: str
    snapshot_id: str
    repetition: int
    condition: str


@dataclass(frozen=True, slots=True)
class Prematch:
    local_concern_id: str
    oracle_id: str
    matched_text: str


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def canonical_sha256(value: Any) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def _load_json(path: Path) -> dict[str, Any]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError(f"{path.name} must contain a JSON object")
    return raw


def load_frozen_contract() -> FrozenContract:
    contract = FrozenContract(
        universe=_load_json(UNIVERSE_PATH),
        episodes=_load_json(EPISODES_PATH),
        oracle=_load_json(ORACLE_PATH),
        representation_map=_load_json(REPRESENTATION_MAP_PATH),
        manifest=_load_json(MANIFEST_PATH),
    )
    validate_frozen_contract(contract)
    return contract


def validate_frozen_contract(contract: FrozenContract) -> None:
    files = {
        "spec022_coverage_oracle_v1.json": contract.oracle,
        "spec022_methodological_universe_v1.json": contract.universe,
        "spec022_oracle_representation_map_v1.json": contract.representation_map,
        "spec022_project_state_episodes_v1.json": contract.episodes,
    }
    manifest_files = contract.manifest.get("files")
    if not isinstance(manifest_files, dict):
        raise ValueError("fixture manifest files must be an object")
    for filename, value in files.items():
        observed = canonical_sha256(value)
        expected = EXPECTED_CANONICAL_SHA256[filename]
        if observed != expected:
            raise ValueError(
                f"{filename} canonical SHA-256 drifted: expected {expected}, "
                f"observed {observed}"
            )
        entry = manifest_files.get(filename)
        if not isinstance(entry, dict):
            raise ValueError(f"manifest is missing {filename}")
        if entry.get("canonical_sha256") != expected:
            raise ValueError(f"manifest SHA-256 drifted for {filename}")
        if int(entry.get("canonical_bytes", -1)) != len(
            canonical_json_bytes(value)
        ):
            raise ValueError(
                f"manifest canonical byte count drifted for {filename}"
            )

    assets = contract.universe.get("assets")
    relations = contract.universe.get("relations")
    if not isinstance(assets, list) or len(assets) != 28:
        raise ValueError(
            "Specification 022 requires exactly 28 methodological assets"
        )
    if not isinstance(relations, list) or len(relations) != 15:
        raise ValueError(
            "Specification 022 requires exactly 15 methodological relations"
        )
    stable_keys = [str(item["stable_key"]) for item in assets]
    if len(stable_keys) != len(set(stable_keys)):
        raise ValueError("methodological asset stable keys must be unique")
    if contract.universe.get("bundle_kind") != "BENCHMARK_FIXTURE":
        raise ValueError(
            "Specification 022 universe must remain BENCHMARK_FIXTURE"
        )

    episodes = contract.episodes.get("episodes")
    if not isinstance(episodes, list) or len(episodes) != 4:
        raise ValueError("Specification 022 requires exactly four episodes")
    snapshots: dict[str, Mapping[str, Any]] = {}
    episode_ids: list[str] = []
    for episode in episodes:
        episode_id = str(episode["episode_id"])
        episode_ids.append(episode_id)
        episode_snapshots = episode.get("snapshots")
        if not isinstance(episode_snapshots, list) or len(episode_snapshots) != 3:
            raise ValueError(f"{episode_id} must contain exactly three snapshots")
        for snapshot in episode_snapshots:
            snapshot_id = str(snapshot["snapshot_id"])
            if snapshot_id in snapshots:
                raise ValueError(f"duplicate snapshot_id: {snapshot_id}")
            snapshots[snapshot_id] = snapshot
            _validate_snapshot_grounding_shape(episode_id, snapshot)
    if len(episode_ids) != len(set(episode_ids)) or len(snapshots) != 12:
        raise ValueError(
            "episode/snapshot identities must be unique and total 4/12"
        )

    oracle_items = contract.oracle.get("items")
    if not isinstance(oracle_items, list) or len(oracle_items) != 33:
        raise ValueError("Specification 022 requires exactly 33 oracle items")
    oracle_ids = [str(item["oracle_id"]) for item in oracle_items]
    if len(oracle_ids) != len(set(oracle_ids)):
        raise ValueError("oracle IDs must be unique")
    if contract.oracle.get("importance_weights") != {
        "CRITICAL_VALIDITY": 4,
        "HIGH_VALUE": 2,
        "OPTIONAL": 0,
        "USEFUL": 1,
    }:
        raise ValueError("oracle importance weights drifted")

    mappings = contract.representation_map.get("mappings")
    if not isinstance(mappings, list) or len(mappings) != len(oracle_items):
        raise ValueError(
            "representation map must contain one entry per oracle item"
        )
    mapping_ids = [str(item["oracle_id"]) for item in mappings]
    if (
        set(mapping_ids) != set(oracle_ids)
        or len(mapping_ids) != len(set(mapping_ids))
    ):
        raise ValueError(
            "representation-map oracle identities must match exactly"
        )
    empty_mappings = 0
    for mapping in mappings:
        keys = mapping.get("stable_keys")
        if not isinstance(keys, list):
            raise ValueError("representation stable_keys must be an array")
        if not keys:
            empty_mappings += 1
        unknown = set(map(str, keys)).difference(stable_keys)
        if unknown:
            raise ValueError(
                "representation map contains unknown stable keys: "
                f"{sorted(unknown)}"
            )
    if empty_mappings != 2:
        raise ValueError(
            "Specification 022 requires exactly two intentional catalog gaps"
        )

    for item in oracle_items:
        episode_id = str(item["episode_id"])
        if episode_id not in episode_ids:
            raise ValueError(
                f"oracle item references unknown episode: {episode_id}"
            )
        state_by_snapshot = item.get("state_by_snapshot")
        grounding = item.get("grounding_project_object_ids_by_snapshot")
        if not isinstance(state_by_snapshot, dict) or not isinstance(
            grounding, dict
        ):
            raise ValueError("oracle state and grounding maps must be objects")
        for snapshot_id, state in state_by_snapshot.items():
            if snapshot_id not in snapshots:
                raise ValueError(
                    f"oracle item references unknown snapshot: {snapshot_id}"
                )
            EvaluatorState(str(state))
            valid_objects = {
                str(obj["object_id"])
                for obj in snapshots[snapshot_id].get("objects", [])
            }
            for object_id in grounding.get(snapshot_id, []):
                if str(object_id) not in valid_objects:
                    raise ValueError(
                        f"{item['oracle_id']} grounding references unknown object "
                        f"{object_id}"
                    )

    inactive_controls = contract.oracle.get("inactive_controls_by_snapshot")
    if not isinstance(inactive_controls, dict):
        raise ValueError("inactive_controls_by_snapshot must be an object")
    for snapshot_id, keys in inactive_controls.items():
        if snapshot_id not in snapshots:
            raise ValueError(
                f"inactive control references unknown snapshot {snapshot_id}"
            )
        unknown = set(map(str, keys)).difference(stable_keys)
        if unknown:
            raise ValueError(
                f"inactive controls contain unknown stable keys: {sorted(unknown)}"
            )


def _validate_snapshot_grounding_shape(
    episode_id: str,
    snapshot: Mapping[str, Any],
) -> None:
    snapshot_id = str(snapshot["snapshot_id"])
    if not snapshot_id.startswith(episode_id + "-"):
        raise ValueError(f"{snapshot_id} does not belong to {episode_id}")
    objects = snapshot.get("objects")
    relations = snapshot.get("relations")
    project_facts = snapshot.get("project_facts")
    if not isinstance(objects, list) or not isinstance(relations, list):
        raise ValueError(f"{snapshot_id} objects/relations must be arrays")
    if not isinstance(project_facts, dict):
        raise ValueError(f"{snapshot_id} project_facts must be an object")
    object_ids = [str(item["object_id"]) for item in objects]
    if len(object_ids) != len(set(object_ids)):
        raise ValueError(f"{snapshot_id} object IDs must be unique")
    valid = set(object_ids)
    relation_ids: list[str] = []
    for relation in relations:
        relation_ids.append(str(relation["relation_id"]))
        if (
            str(relation["source_id"]) not in valid
            or str(relation["target_id"]) not in valid
        ):
            raise ValueError(
                f"{snapshot_id} relation endpoint is not a supplied object"
            )
    if len(relation_ids) != len(set(relation_ids)):
        raise ValueError(f"{snapshot_id} relation IDs must be unique")


def episode_by_id(
    contract: FrozenContract,
    episode_id: str,
) -> Mapping[str, Any]:
    matches = [
        item
        for item in contract.episodes["episodes"]
        if item["episode_id"] == episode_id
    ]
    if len(matches) != 1:
        raise KeyError(f"unknown episode_id: {episode_id}")
    return matches[0]


def snapshot_by_id(
    contract: FrozenContract,
    episode_id: str,
    snapshot_id: str,
) -> Mapping[str, Any]:
    episode = episode_by_id(contract, episode_id)
    matches = [
        item
        for item in episode["snapshots"]
        if item["snapshot_id"] == snapshot_id
    ]
    if len(matches) != 1:
        raise KeyError(f"unknown snapshot_id {snapshot_id} in {episode_id}")
    return matches[0]


def canonical_project_state(
    episode_id: str,
    snapshot: Mapping[str, Any],
) -> dict[str, Any]:
    value = {
        "episode_id": episode_id,
        "snapshot_id": str(snapshot["snapshot_id"]),
        "transition_summary": str(snapshot["transition_summary"]),
        "project_facts": dict(snapshot["project_facts"]),
        "objects": list(snapshot["objects"]),
        "relations": list(snapshot["relations"]),
    }
    return json.loads(canonical_json_bytes(value).decode("utf-8"))


def canonical_project_state_bytes(
    episode_id: str,
    snapshot: Mapping[str, Any],
) -> bytes:
    return canonical_json_bytes(canonical_project_state(episode_id, snapshot))


def _canonical_scalar(value: Any) -> str:
    if isinstance(value, (dict, list)):
        raise ValueError(
            "project-state projector accepts scalar fact values only"
        )
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )


def project_state_to_retrieval_text(
    episode_id: str,
    snapshot: Mapping[str, Any],
) -> str:
    lines = [
        f"EPISODE: {episode_id}",
        f"SNAPSHOT: {snapshot['snapshot_id']}",
        f"TRANSITION: {snapshot['transition_summary']}",
    ]
    project_facts = snapshot.get("project_facts", {})
    for key in sorted(project_facts):
        lines.append(
            f"FACT: {key}={_canonical_scalar(project_facts[key])}"
        )

    for obj in sorted(
        snapshot.get("objects", []),
        key=lambda item: str(item["object_id"]),
    ):
        object_id = str(obj["object_id"])
        lines.append(
            "OBJECT: "
            f"{object_id} | {obj['object_type']} | {obj['title']} | "
            f"{obj['description']}"
        )
        facts = obj.get("facts", {})
        for key in sorted(facts):
            lines.append(
                f"OBJECT_FACT: {object_id} | "
                f"{key}={_canonical_scalar(facts[key])}"
            )

    for relation in sorted(
        snapshot.get("relations", []),
        key=lambda item: str(item["relation_id"]),
    ):
        lines.append(
            "RELATION: "
            f"{relation['relation_id']} | {relation['type']} | "
            f"{relation['source_id']} | {relation['target_id']}"
        )
    return "\n".join(lines)


def build_reasoner_plan(
    contract: FrozenContract,
) -> tuple[ReasonerPlanEntry, ...]:
    raw: list[tuple[str, str, int, str]] = []
    for episode in sorted(
        contract.episodes["episodes"],
        key=lambda item: item["episode_id"],
    ):
        for snapshot in sorted(
            episode["snapshots"],
            key=lambda item: item["snapshot_id"],
        ):
            for repetition in range(1, REPETITIONS + 1):
                for condition in CONDITIONS:
                    raw.append(
                        (
                            str(episode["episode_id"]),
                            str(snapshot["snapshot_id"]),
                            repetition,
                            condition,
                        )
                    )
    if len(raw) != PLANNED_REASONER_OBSERVATIONS:
        raise AssertionError(
            f"reasoner plan drifted: observed {len(raw)} entries"
        )

    rng = random.Random(RANDOMIZATION_SEED)
    rng.shuffle(raw)
    result: list[ReasonerPlanEntry] = []
    for ordinal, (
        episode_id,
        snapshot_id,
        repetition,
        condition,
    ) in enumerate(raw, start=1):
        digest = hashlib.sha256(
            (
                f"spec022|{RANDOMIZATION_SEED}|{ordinal}|{episode_id}|"
                f"{snapshot_id}|{repetition}|{condition}"
            ).encode("utf-8")
        ).hexdigest()
        result.append(
            ReasonerPlanEntry(
                observation_id=f"mn-{digest[:20]}",
                run_id=f"reasoner-{digest[20:40]}",
                run_nonce=f"nonce-{digest[40:64]}",
                episode_id=episode_id,
                snapshot_id=snapshot_id,
                repetition=repetition,
                condition=condition,
            )
        )
    return tuple(result)


def serialize_reasoner_plan(
    plan: Sequence[ReasonerPlanEntry],
) -> tuple[str, str]:
    text = json.dumps(
        [asdict(item) for item in plan],
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )
    return text, hashlib.sha256(text.encode("utf-8")).hexdigest()


def methodology_payload_sha256(
    payload: Mapping[str, object],
) -> str:
    return hashlib.sha256(canonical_json_bytes(dict(payload))).hexdigest()


def validate_result_grounding(
    result: MethodologicalCoverageResult,
    snapshot: Mapping[str, Any],
) -> None:
    valid_ids = {str(item["object_id"]) for item in snapshot["objects"]}
    for concern in result.concerns:
        unknown = set(concern.grounding_project_object_ids).difference(
            valid_ids
        )
        if unknown:
            raise ValueError(
                f"{concern.local_concern_id} references unknown project-object "
                f"IDs: {sorted(unknown)}"
            )


def build_reasoner_request(
    *,
    entry: ReasonerPlanEntry,
    snapshot: Mapping[str, Any],
    methodological_context_payload: Mapping[str, object],
    knowledge_revisions: Sequence[KnowledgeRevisionPointer],
) -> ReasoningRequest:
    condition = CoverageCondition(entry.condition)
    if condition is CoverageCondition.GENERIC:
        if methodological_context_payload or knowledge_revisions:
            raise ValueError(
                "GENERIC must not receive reusable methodological context"
            )
    elif not methodological_context_payload or not knowledge_revisions:
        raise ValueError(
            f"{condition.value} requires a non-empty methodological context"
        )

    project_state = canonical_project_state(entry.episode_id, snapshot)
    context_payload = json.loads(
        canonical_json_bytes(dict(methodological_context_payload)).decode(
            "utf-8"
        )
    )
    return ReasoningRequest(
        run_id=entry.run_id,
        run_nonce=entry.run_nonce,
        system_instruction=COMMON_INSTRUCTION,
        user_task=USER_TASK,
        project_evidence=project_state,
        methodological_context_payload=context_payload,
        methodological_context_sha256=methodology_payload_sha256(
            context_payload
        ),
        knowledge_revisions=tuple(knowledge_revisions),
        model_configuration=REASONER_MODEL,
        structured_output_type=MethodologicalCoverageResult,
    )


_NORMALIZE_RE = re.compile(r"[^\w\s]+", flags=re.UNICODE)


def normalize_concern_text(value: str) -> str:
    normalized = _NORMALIZE_RE.sub(" ", value.casefold())
    return " ".join(normalized.split())


def oracle_items_for_snapshot(
    contract: FrozenContract,
    episode_id: str,
    snapshot_id: str,
) -> tuple[Mapping[str, Any], ...]:
    default_state = str(contract.oracle["default_unspecified_state"])
    result: list[Mapping[str, Any]] = []
    for item in contract.oracle["items"]:
        if item["episode_id"] != episode_id:
            continue
        copied = dict(item)
        copied["expected_state"] = str(
            item.get("state_by_snapshot", {}).get(
                snapshot_id,
                default_state,
            )
        )
        result.append(copied)
    return tuple(result)


def deterministic_prematch(
    result: MethodologicalCoverageResult,
    oracle_items: Sequence[Mapping[str, Any]],
) -> tuple[Prematch, ...]:
    lookup: dict[str, list[str]] = {}
    for item in oracle_items:
        oracle_id = str(item["oracle_id"])
        values = [
            str(item["canonical_concern"]),
            *map(str, item["acceptable_aliases"]),
        ]
        for value in values:
            lookup.setdefault(
                normalize_concern_text(value),
                [],
            ).append(oracle_id)

    prematches: list[Prematch] = []
    used_oracle_ids: set[str] = set()
    for concern in result.concerns:
        normalized = normalize_concern_text(concern.title)
        candidates = lookup.get(normalized, [])
        available = [
            item for item in candidates if item not in used_oracle_ids
        ]
        if len(available) == 1:
            oracle_id = available[0]
            used_oracle_ids.add(oracle_id)
            prematches.append(
                Prematch(
                    local_concern_id=concern.local_concern_id,
                    oracle_id=oracle_id,
                    matched_text=normalized,
                )
            )
    return tuple(prematches)


def _judge_oracle_projection(
    oracle_items: Sequence[Mapping[str, Any]],
    snapshot_id: str,
) -> list[dict[str, object]]:
    return [
        {
            "oracle_id": str(item["oracle_id"]),
            "canonical_concern": str(item["canonical_concern"]),
            "acceptable_aliases": list(item["acceptable_aliases"]),
            "expected_state": str(item["expected_state"]),
            "missing_context_question_semantics": item.get(
                "missing_context_question_semantics"
            ),
            "grounding_project_object_ids": list(
                item.get(
                    "grounding_project_object_ids_by_snapshot",
                    {},
                ).get(snapshot_id, [])
            ),
        }
        for item in oracle_items
    ]


def build_blinded_judge_request(
    *,
    entry: ReasonerPlanEntry,
    snapshot: Mapping[str, Any],
    result: MethodologicalCoverageResult,
    oracle_items: Sequence[Mapping[str, Any]],
    prematches: Sequence[Prematch],
) -> ReasoningRequest:
    validate_result_grounding(result, snapshot)
    anonymous_digest = hashlib.sha256(
        f"spec022-judge|{entry.observation_id}".encode("utf-8")
    ).hexdigest()
    judge_evidence = {
        "project_state": canonical_project_state(
            entry.episode_id,
            snapshot,
        ),
        "reasoner_concerns": [
            item.to_payload() for item in result.concerns
        ],
        "oracle_concerns": _judge_oracle_projection(
            oracle_items,
            entry.snapshot_id,
        ),
        "deterministic_prematches": [
            asdict(item) for item in prematches
        ],
    }
    return ReasoningRequest(
        run_id=f"judge-{anonymous_digest[:20]}",
        run_nonce=f"judge-nonce-{anonymous_digest[20:44]}",
        system_instruction=JUDGE_INSTRUCTION,
        user_task=(
            "Return semantic matches, state/question equivalence, unsupported "
            "records, and duplicate records for this anonymized "
            "methodological-coverage observation."
        ),
        project_evidence=judge_evidence,
        methodological_context_payload={},
        methodological_context_sha256=methodology_payload_sha256({}),
        knowledge_revisions=(),
        model_configuration=JUDGE_MODEL,
        structured_output_type=SemanticAdjudicationResult,
    )


def validate_semantic_adjudication(
    adjudication: SemanticAdjudicationResult,
    result: MethodologicalCoverageResult,
    oracle_items: Sequence[Mapping[str, Any]],
) -> None:
    valid_local_ids = {
        item.local_concern_id for item in result.concerns
    }
    valid_oracle_ids = {
        str(item["oracle_id"]) for item in oracle_items
    }
    matched_local: list[str] = []
    matched_oracle: list[str] = []
    for match in adjudication.matches:
        if match.local_concern_id not in valid_local_ids:
            raise ValueError(
                f"judge matched unknown local concern "
                f"{match.local_concern_id}"
            )
        if match.oracle_id not in valid_oracle_ids:
            raise ValueError(
                f"judge matched unknown oracle item {match.oracle_id}"
            )
        matched_local.append(match.local_concern_id)
        matched_oracle.append(match.oracle_id)
    if len(matched_local) != len(set(matched_local)):
        raise ValueError("judge may match a local concern at most once")
    if len(matched_oracle) != len(set(matched_oracle)):
        raise ValueError("judge may match an oracle item at most once")

    unsupported = set(adjudication.unsupported_local_concern_ids)
    duplicates = set(adjudication.duplicate_local_concern_ids)
    if not unsupported.issubset(valid_local_ids) or not duplicates.issubset(
        valid_local_ids
    ):
        raise ValueError(
            "judge unsupported/duplicate IDs must reference supplied concerns"
        )
    if unsupported & duplicates:
        raise ValueError(
            "one concern cannot be both unsupported and duplicate"
        )
    if (unsupported | duplicates) & set(matched_local):
        raise ValueError(
            "matched concerns cannot also be unsupported or duplicate"
        )


def public_reasoner_builder_parameters() -> tuple[str, ...]:
    """Expose the treatment-builder signature for leakage regression tests."""

    return tuple(inspect.signature(build_reasoner_request).parameters)
