"""Minimal structured P0 treatment for Prototype V0.

P0 is the first executable treatment that operationalizes the semantic spine
specified before held-out evaluation was frozen. It deliberately remains much
smaller than the eventual Autonomous Data Science System.

The treatment adds only the pre-registered Version 0 mechanisms:

* typed project-state objects with type-specific statuses;
* explicit DEPENDS_ON / SUPPORTS / CONTRADICTS / ANSWERS / GENERATED_BY
  relations;
* append-only state-change history;
* the same four methodological knowledge components supplied statically to B1,
  but activated as scoped state-driven instances rather than placed wholesale
  in the prompt;
* a prospective protected-final-evaluation gate already implemented by the
  common workspace;
* deterministic hard-dependency reopening and support-reassessment obligations;
* a small state-derived runnable frontier; and
* one model response per reasoning cycle containing both a state patch and the
  next common treatment command.

The implementation intentionally does not add another reviewer model, specialist
agent, retrieval system, new methodological checklist, or held-out-case-specific
rule. Every provider-backed P0 reasoning call counts against the same treatment
resource envelope registered for B0 and B1.

Primary semantic evaluation remains condition-neutral. P0 state, knowledge
activation, and dependency diagnostics are written separately and are excluded
from the blinded primary semantic packet.
"""

from __future__ import annotations

import copy
import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from .evaluator import evaluate_deterministic_behavior
from .model import (
    ModelClient,
    ModelGeneration,
    ModelGenerationError,
    ModelMessage,
    ModelUsage,
)
from .runtime import ActionBlockedError, ActionCategory, ExperimentWorkspace
from .treatments import (
    _COMMAND_CONTRACT,
    _GENERIC_METHODOLOGY,
    _required_report,
    _required_str,
    _validate_development_report,
)


STATE_TYPES = (
    "ARTIFACT",
    "FACT",
    "ASSUMPTION",
    "QUESTION",
    "EVIDENCE",
    "CLAIM",
    "DECISION",
    "OBLIGATION",
    "ACTION",
)

RELATION_TYPES = (
    "DEPENDS_ON",
    "SUPPORTS",
    "CONTRADICTS",
    "ANSWERS",
    "GENERATED_BY",
)

STATUS_BY_TYPE: dict[str, tuple[str, ...]] = {
    "ARTIFACT": ("AVAILABLE", "PROTECTED", "SUPERSEDED"),
    "FACT": ("ACTIVE", "DISPUTED", "SUPERSEDED"),
    "ASSUMPTION": ("PROVISIONAL", "SUPPORTED", "INVALIDATED"),
    "QUESTION": ("OPEN", "RESOLVED", "BLOCKED", "REOPENED"),
    "EVIDENCE": ("CURRENT", "INVALIDATED", "STALE"),
    "CLAIM": ("PROVISIONAL", "SUPPORTED", "WEAKENED", "INVALIDATED"),
    "DECISION": ("PROVISIONAL", "ACCEPTED", "REOPENED", "SUPERSEDED"),
    "OBLIGATION": ("OPEN", "SATISFIED", "BLOCKED"),
    "ACTION": ("PROPOSED", "ALLOWED", "BLOCKED", "EXECUTED", "FAILED"),
}

_ID_PREFIX = {
    "ARTIFACT": "AR",
    "FACT": "F",
    "ASSUMPTION": "A",
    "QUESTION": "Q",
    "EVIDENCE": "E",
    "CLAIM": "C",
    "DECISION": "D",
    "OBLIGATION": "O",
    "ACTION": "AC",
}

_ACTIVE_MOTIVATOR_STATUSES = {
    ("QUESTION", "OPEN"),
    ("QUESTION", "REOPENED"),
    ("OBLIGATION", "OPEN"),
    ("DECISION", "REOPENED"),
}

_INVALIDATING_STATUSES = {
    ("FACT", "SUPERSEDED"),
    ("ASSUMPTION", "INVALIDATED"),
    ("EVIDENCE", "INVALIDATED"),
    ("CLAIM", "INVALIDATED"),
    ("DECISION", "SUPERSEDED"),
}

_DEPENDENT_STATUS_AFTER_HARD_BREAK: dict[str, str] = {
    "FACT": "DISPUTED",
    "ASSUMPTION": "INVALIDATED",
    "QUESTION": "REOPENED",
    "EVIDENCE": "INVALIDATED",
    "CLAIM": "INVALIDATED",
    "DECISION": "REOPENED",
    "OBLIGATION": "OPEN",
    "ACTION": "FAILED",
}


@dataclass
class StateObject:
    """One typed current-state object.

    Content is immutable after creation in Version 0. Later semantic change is
    represented through status transitions, new objects, and explicit relations.
    This keeps audit history simple and avoids silently rewriting earlier claims.
    """

    id: str
    type: str
    status: str
    scope: str
    content: str
    source_refs: list[str]
    tags: list[str]
    created_step: int
    updated_step: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class StateRelation:
    source_id: str
    relation: str
    target_id: str
    created_step: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class StateChange:
    step: int
    object_id: str
    old_status_or_value: str | None
    new_status_or_value: str
    reason: str
    trigger_or_source: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class KnowledgeActivation:
    component_id: str
    scope: str
    activated_step: int
    instance_object_ids: list[str] = field(default_factory=list)
    reopen_count: int = 0

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


KNOWLEDGE_COMPONENTS: dict[str, dict[str, str]] = {
    "K-INFO-001": {
        "title": "Protected Final Evaluation",
        "role": "prospective safeguard",
        "content": (
            "Outcome information from an artifact designated as independent final "
            "evaluation must not influence development choices before development "
            "is locked. Use legitimate development evidence instead."
        ),
    },
    "K-INFO-002": {
        "title": "Learned Transformation Evaluation Boundary",
        "role": "methodological invariant",
        "content": (
            "A learned transformation participating in evaluation must be fitted "
            "only from information legitimate for the corresponding training "
            "portion. If inherited evaluation violates this boundary, that evidence "
            "is not clean comparative evidence and requires legitimate re-evaluation."
        ),
    },
    "K-INFO-003": {
        "title": "Prediction-Time Feature Eligibility",
        "role": "information-legitimacy question",
        "content": (
            "A predictive feature is legitimate only if the information it represents "
            "would actually exist at the represented prediction moment. Historical "
            "warehouse presence alone is insufficient."
        ),
    },
    "K-VAL-001": {
        "title": "Generalization-Regime Question",
        "role": "validation decision principle",
        "content": (
            "Validation should estimate the deployment quantity of interest. Repeated "
            "entities, timestamps, future prediction, and entity overlap require "
            "reasoning about future observations and known versus new entities; "
            "repeated IDs do not mechanically imply pure unseen-entity validation."
        ),
    },
}


P0_ARCHITECTURE_INSTRUCTION = """
You are the reasoning engine for the structured P0 condition of a controlled
autonomous data-science experiment.

You have the same project capabilities and underlying methodological objective as
the simpler conditions, plus an explicit project-state controller. Do not rely on
conversation memory as the authoritative project state. Each turn includes a
compact P0_STATE_VIEW. Update that state with concise, evidence-grounded objects
before proposing the next action.

State object types:
ARTIFACT, FACT, ASSUMPTION, QUESTION, EVIDENCE, CLAIM, DECISION, OBLIGATION,
ACTION.

Allowed statuses by type:
ARTIFACT: AVAILABLE, PROTECTED, SUPERSEDED
FACT: ACTIVE, DISPUTED, SUPERSEDED
ASSUMPTION: PROVISIONAL, SUPPORTED, INVALIDATED
QUESTION: OPEN, RESOLVED, BLOCKED, REOPENED
EVIDENCE: CURRENT, INVALIDATED, STALE
CLAIM: PROVISIONAL, SUPPORTED, WEAKENED, INVALIDATED
DECISION: PROVISIONAL, ACCEPTED, REOPENED, SUPERSEDED
OBLIGATION: OPEN, SATISFIED, BLOCKED
ACTION: ACTION objects are maintained by the controller; do not create them.

Relations:
DEPENDS_ON, SUPPORTS, CONTRADICTS, ANSWERS, GENERATED_BY.
Use DEPENDS_ON only for a hard dependency whose failure should reopen or
invalidate the dependent object. Use SUPPORTS for non-exclusive evidential
support.

Each created object uses a temporary client_ref unique within the patch. The
controller assigns the canonical object ID. Relations may refer either to an
existing canonical ID from P0_STATE_VIEW or to a client_ref created in the same
patch.

Use semantic tags only when evidence supports them. Tags are small activation
signals, not conclusions by themselves. Useful Version 0 tags include:
future_prediction_objective, prediction_moment, repeated_entities,
temporal_structure, feature_eligibility, protected_final_evaluation,
validation_regime, inherited_evaluation, validation_evidence, model_selection.
Do not force a tag merely to activate knowledge.

The controller may instantiate a knowledge-derived QUESTION or OBLIGATION when
current state makes one of the four pre-specified knowledge components relevant.
Active knowledge appears in P0_STATE_VIEW. Resolve or update the instantiated
state object when evidence permits. Do not duplicate a scoped concern.

Every proposed command must cite at least one current motivator ID. The
controller's runnable frontier consists of open/reopened questions, open
obligations, reopened decisions, and the project deliverable obligation. When a
blocking or repair-priority concern exists, at least one such concern must
motivate the next action.

Milestone reports are common external project outputs. Important conclusions
that exist in structured state but matter to the project must also be expressed
clearly in the appropriate milestone report. Internal state alone receives no
primary semantic-evaluation credit.

Return exactly one structured object containing:
- a short rationale;
- a state_patch with creates, status_updates, relation additions/removals;
- motivator_ids for the proposed command; and
- exactly one common treatment command.

Do not expose private chain-of-thought. Keep state objects concise and
proposition-like.
""".strip()


class P0StateStore:
    """Small audited typed-state store with deterministic dependency repair."""

    def __init__(self) -> None:
        self.objects: dict[str, StateObject] = {}
        self.relations: list[StateRelation] = []
        self.history: list[StateChange] = []
        self._counters = {state_type: 0 for state_type in STATE_TYPES}
        self.step = 0
        self.artifact_state_ids: dict[str, str] = {}

    def _next_step(self) -> int:
        self.step += 1
        return self.step

    def _next_id(self, state_type: str) -> str:
        self._counters[state_type] += 1
        return f"{_ID_PREFIX[state_type]}-{self._counters[state_type]:04d}"

    def _validate_type_status(self, state_type: str, status: str) -> None:
        if state_type not in STATUS_BY_TYPE:
            raise ValueError(f"Unknown state object type: {state_type!r}")
        if status not in STATUS_BY_TYPE[state_type]:
            raise ValueError(
                f"Invalid status {status!r} for state type {state_type!r}."
            )

    def create_object(
        self,
        *,
        state_type: str,
        status: str,
        scope: str,
        content: str,
        source_refs: Sequence[str] = (),
        tags: Sequence[str] = (),
        reason: str = "Create state object.",
        trigger: str = "controller",
    ) -> StateObject:
        state_type = str(state_type)
        status = str(status)
        self._validate_type_status(state_type, status)
        if state_type == "ACTION" and trigger == "model_patch":
            raise ValueError("ACTION objects are controller-maintained in P0.")
        if not str(scope).strip():
            raise ValueError("State object scope must be non-empty.")
        if not str(content).strip():
            raise ValueError("State object content must be non-empty.")

        step = self._next_step()
        object_id = self._next_id(state_type)
        obj = StateObject(
            id=object_id,
            type=state_type,
            status=status,
            scope=str(scope),
            content=str(content),
            source_refs=list(dict.fromkeys(str(x) for x in source_refs if str(x))),
            tags=list(dict.fromkeys(str(x) for x in tags if str(x))),
            created_step=step,
            updated_step=step,
        )
        self.objects[object_id] = obj
        self.history.append(
            StateChange(
                step=step,
                object_id=object_id,
                old_status_or_value=None,
                new_status_or_value=status,
                reason=reason,
                trigger_or_source=trigger,
            )
        )
        return obj

    def register_artifact(self, artifact_id: str, *, kind: str) -> StateObject:
        if artifact_id in self.artifact_state_ids:
            return self.objects[self.artifact_state_ids[artifact_id]]
        obj = self.create_object(
            state_type="ARTIFACT",
            status="AVAILABLE",
            scope="project",
            content=f"Project artifact {artifact_id} ({kind}).",
            source_refs=[artifact_id],
            tags=[f"artifact_kind:{kind}"],
            reason="Register currently visible project artifact.",
            trigger="workspace_visibility",
        )
        self.artifact_state_ids[artifact_id] = obj.id
        return obj

    def artifact_object(self, artifact_id: str) -> StateObject | None:
        object_id = self.artifact_state_ids.get(artifact_id)
        return self.objects.get(object_id) if object_id is not None else None

    def add_tags(
        self,
        object_id: str,
        tags: Iterable[str],
        *,
        reason: str,
        trigger: str,
    ) -> None:
        obj = self._require_object(object_id)
        new_tags = [str(tag) for tag in tags if str(tag) and str(tag) not in obj.tags]
        if not new_tags:
            return
        step = self._next_step()
        obj.tags.extend(new_tags)
        obj.updated_step = step
        self.history.append(
            StateChange(
                step=step,
                object_id=object_id,
                old_status_or_value="tags=" + ",".join(obj.tags[:-len(new_tags)]),
                new_status_or_value="tags=" + ",".join(obj.tags),
                reason=reason,
                trigger_or_source=trigger,
            )
        )

    def update_status(
        self,
        object_id: str,
        new_status: str,
        *,
        reason: str,
        trigger: str,
        source_refs: Sequence[str] = (),
        propagate: bool = True,
    ) -> list[str]:
        obj = self._require_object(object_id)
        self._validate_type_status(obj.type, new_status)
        if obj.status == new_status:
            for ref in source_refs:
                if ref not in obj.source_refs:
                    obj.source_refs.append(str(ref))
            return []

        old_status = obj.status
        step = self._next_step()
        obj.status = new_status
        obj.updated_step = step
        for ref in source_refs:
            ref_text = str(ref)
            if ref_text and ref_text not in obj.source_refs:
                obj.source_refs.append(ref_text)
        self.history.append(
            StateChange(
                step=step,
                object_id=object_id,
                old_status_or_value=old_status,
                new_status_or_value=new_status,
                reason=reason,
                trigger_or_source=trigger,
            )
        )

        changed = [object_id]
        if propagate and (obj.type, new_status) in _INVALIDATING_STATUSES:
            changed.extend(
                self._propagate_hard_dependency_break(
                    object_id,
                    trigger=f"dependency:{object_id}",
                )
            )
            self._create_support_reassessment_obligations(
                object_id,
                trigger=f"support_loss:{object_id}",
            )
        return list(dict.fromkeys(changed))

    def add_relation(
        self,
        source_id: str,
        relation: str,
        target_id: str,
    ) -> StateRelation:
        self._require_object(source_id)
        self._require_object(target_id)
        if relation not in RELATION_TYPES:
            raise ValueError(f"Unknown relation type: {relation!r}")
        for existing in self.relations:
            if (
                existing.source_id == source_id
                and existing.relation == relation
                and existing.target_id == target_id
            ):
                return existing
        step = self._next_step()
        edge = StateRelation(
            source_id=source_id,
            relation=relation,
            target_id=target_id,
            created_step=step,
        )
        self.relations.append(edge)
        return edge

    def remove_relation(self, source_id: str, relation: str, target_id: str) -> bool:
        for index, edge in enumerate(self.relations):
            if (
                edge.source_id == source_id
                and edge.relation == relation
                and edge.target_id == target_id
            ):
                del self.relations[index]
                self._next_step()
                return True
        return False

    def _propagate_hard_dependency_break(
        self,
        broken_id: str,
        *,
        trigger: str,
    ) -> list[str]:
        changed: list[str] = []
        queue = [broken_id]
        visited = {broken_id}

        while queue:
            current = queue.pop(0)
            dependents = [
                edge.source_id
                for edge in self.relations
                if edge.relation == "DEPENDS_ON" and edge.target_id == current
            ]
            for dependent_id in dependents:
                if dependent_id in visited:
                    continue
                visited.add(dependent_id)
                dependent = self._require_object(dependent_id)
                target_status = _DEPENDENT_STATUS_AFTER_HARD_BREAK.get(dependent.type)
                if target_status is None:
                    continue
                if target_status not in STATUS_BY_TYPE[dependent.type]:
                    continue
                if dependent.status != target_status:
                    changed.extend(
                        self.update_status(
                            dependent_id,
                            target_status,
                            reason=(
                                f"Hard dependency on {current} is no longer valid."
                            ),
                            trigger=trigger,
                            source_refs=[current],
                            propagate=False,
                        )
                    )
                if (dependent.type, dependent.status) in _INVALIDATING_STATUSES or dependent.status == "REOPENED":
                    queue.append(dependent_id)
        return changed

    def _create_support_reassessment_obligations(
        self,
        invalid_source_id: str,
        *,
        trigger: str,
    ) -> None:
        supported_targets = [
            edge.target_id
            for edge in self.relations
            if edge.relation == "SUPPORTS" and edge.source_id == invalid_source_id
        ]
        for target_id in supported_targets:
            marker = f"support_reassessment:{invalid_source_id}:{target_id}"
            if any(marker in obj.tags for obj in self.objects.values()):
                continue
            target = self._require_object(target_id)
            self.create_object(
                state_type="OBLIGATION",
                status="OPEN",
                scope=target.scope,
                content=(
                    f"Reassess {target_id} because supporting object "
                    f"{invalid_source_id} is no longer current."
                ),
                source_refs=[invalid_source_id, target_id],
                tags=[marker, "priority:repair"],
                reason="A supporting evidence path became invalid and sufficiency must be reassessed.",
                trigger=trigger,
            )

    def apply_model_patch(self, patch: Mapping[str, Any]) -> dict[str, Any]:
        creates = patch.get("creates", [])
        updates = patch.get("status_updates", [])
        additions = patch.get("add_relations", [])
        removals = patch.get("remove_relations", [])
        for name, value in (
            ("creates", creates),
            ("status_updates", updates),
            ("add_relations", additions),
            ("remove_relations", removals),
        ):
            if not isinstance(value, list):
                raise ValueError(f"state_patch.{name} must be a list.")

        client_map: dict[str, str] = {}
        changed_ids: list[str] = []

        for item in creates:
            if not isinstance(item, Mapping):
                raise ValueError("Each state create entry must be an object.")
            client_ref = str(item.get("client_ref", "")).strip()
            if not client_ref or client_ref in client_map or client_ref in self.objects:
                raise ValueError(f"Invalid or duplicate state client_ref: {client_ref!r}")
            obj = self.create_object(
                state_type=str(item.get("type", "")),
                status=str(item.get("status", "")),
                scope=str(item.get("scope", "")),
                content=str(item.get("content", "")),
                source_refs=_string_list(item.get("source_refs", []), "source_refs"),
                tags=_string_list(item.get("tags", []), "tags"),
                reason="Model-created state object.",
                trigger="model_patch",
            )
            client_map[client_ref] = obj.id
            changed_ids.append(obj.id)

        for item in updates:
            if not isinstance(item, Mapping):
                raise ValueError("Each state status update must be an object.")
            object_id = self._resolve_ref(str(item.get("object_id", "")), client_map)
            changed_ids.extend(
                self.update_status(
                    object_id,
                    str(item.get("new_status", "")),
                    reason=str(item.get("reason", "State status updated by model.")),
                    trigger="model_patch",
                    source_refs=_string_list(item.get("source_refs", []), "source_refs"),
                )
            )

        for item in removals:
            if not isinstance(item, Mapping):
                raise ValueError("Each relation removal must be an object.")
            self.remove_relation(
                self._resolve_ref(str(item.get("source_ref", "")), client_map),
                str(item.get("relation", "")),
                self._resolve_ref(str(item.get("target_ref", "")), client_map),
            )

        for item in additions:
            if not isinstance(item, Mapping):
                raise ValueError("Each relation addition must be an object.")
            self.add_relation(
                self._resolve_ref(str(item.get("source_ref", "")), client_map),
                str(item.get("relation", "")),
                self._resolve_ref(str(item.get("target_ref", "")), client_map),
            )

        return {
            "client_ref_map": client_map,
            "changed_object_ids": list(dict.fromkeys(changed_ids)),
        }

    def _resolve_ref(self, ref: str, client_map: Mapping[str, str]) -> str:
        if ref in client_map:
            return client_map[ref]
        self._require_object(ref)
        return ref

    def _require_object(self, object_id: str) -> StateObject:
        if object_id not in self.objects:
            raise ValueError(f"Unknown state object ID: {object_id!r}")
        return self.objects[object_id]

    def active_motivators(self) -> list[StateObject]:
        return [
            obj
            for obj in self.objects.values()
            if (obj.type, obj.status) in _ACTIVE_MOTIVATOR_STATUSES
        ]

    def frontier(self) -> dict[str, Any]:
        motivators = self.active_motivators()
        priorities = (
            "priority:hard_blocker",
            "priority:blocking",
            "priority:repair",
        )
        highest_ids: list[str] = []
        highest_priority: str | None = None
        for priority in priorities:
            ids = [obj.id for obj in motivators if priority in obj.tags]
            if ids:
                highest_priority = priority
                highest_ids = ids
                break
        if not highest_ids:
            highest_ids = [obj.id for obj in motivators]
        return {
            "highest_priority": highest_priority,
            "required_motivator_candidates": highest_ids,
            "all_motivator_ids": [obj.id for obj in motivators],
        }

    def validate_motivators(self, motivator_ids: Sequence[str]) -> None:
        requested = [str(item) for item in motivator_ids]
        if not requested:
            raise ValueError("Every P0 action must cite at least one current motivator ID.")
        active_ids = {obj.id for obj in self.active_motivators()}
        unknown = [item for item in requested if item not in active_ids]
        if unknown:
            raise ValueError(
                "Action cites non-current motivator IDs: " + ", ".join(unknown)
            )
        frontier = self.frontier()
        highest = set(frontier["required_motivator_candidates"])
        if frontier["highest_priority"] is not None and not highest.intersection(requested):
            raise ValueError(
                "A higher-priority blocking/repair concern exists; cite at least one "
                "frontier motivator: " + ", ".join(sorted(highest))
            )

    def create_action(
        self,
        *,
        command: Mapping[str, Any],
        motivator_ids: Sequence[str],
        status: str,
        rationale: str,
    ) -> StateObject:
        obj = self.create_object(
            state_type="ACTION",
            status=status,
            scope="project",
            content=json.dumps(dict(command), sort_keys=True, default=str),
            source_refs=list(motivator_ids),
            tags=["controller_action"],
            reason=rationale or "Record proposed treatment action.",
            trigger="controller",
        )
        for motivator_id in motivator_ids:
            if motivator_id in self.objects:
                self.add_relation(obj.id, "GENERATED_BY", motivator_id)
        return obj

    def snapshot(self) -> dict[str, Any]:
        return {
            "step": self.step,
            "objects": [obj.to_dict() for obj in self.objects.values()],
            "relations": [edge.to_dict() for edge in self.relations],
            "frontier": self.frontier(),
        }

    def compact_view(self, *, history_tail: int = 12) -> dict[str, Any]:
        return {
            "step": self.step,
            "objects": [obj.to_dict() for obj in self.objects.values()],
            "relations": [edge.to_dict() for edge in self.relations],
            "runnable_frontier": self.frontier(),
            "recent_changes": [
                change.to_dict() for change in self.history[-history_tail:]
            ],
        }


class P0KnowledgeActivator:
    """State-pattern activation for the four and only four V0 components."""

    def __init__(self) -> None:
        self.activations: dict[tuple[str, str], KnowledgeActivation] = {}

    def evaluate(self, state: P0StateStore, *, scope: str = "project") -> list[str]:
        activated: list[str] = []
        if self._protected_final_applicable(state):
            if self._activate("K-INFO-001", scope, state):
                activated.append("K-INFO-001")
        if self._learned_transformation_applicable(state):
            if self._activate("K-INFO-002", scope, state):
                activated.append("K-INFO-002")
        if self._feature_eligibility_applicable(state):
            if self._activate("K-INFO-003", scope, state):
                activated.append("K-INFO-003")
        if self._generalization_applicable(state):
            if self._activate("K-VAL-001", scope, state):
                activated.append("K-VAL-001")
        return activated

    def _protected_final_applicable(self, state: P0StateStore) -> bool:
        return any(
            obj.status == "PROTECTED" or "protected_final_evaluation" in obj.tags
            for obj in state.objects.values()
        )

    def _learned_transformation_applicable(self, state: P0StateStore) -> bool:
        return any(
            obj.type == "ARTIFACT"
            and "artifact_kind:python" in obj.tags
            and "inspected" in obj.tags
            for obj in state.objects.values()
        )

    def _feature_eligibility_applicable(self, state: P0StateStore) -> bool:
        prediction_known = any(
            "prediction_moment" in obj.tags for obj in state.objects.values()
        )
        schema_seen = any(
            obj.type == "ARTIFACT"
            and "artifact_kind:csv" in obj.tags
            and "metadata_inspected" in obj.tags
            for obj in state.objects.values()
        )
        return prediction_known and schema_seen

    def _generalization_applicable(self, state: P0StateStore) -> bool:
        tags = {tag for obj in state.objects.values() for tag in obj.tags}
        return {
            "future_prediction_objective",
            "repeated_entities",
            "temporal_structure",
        }.issubset(tags)

    def _activate(self, component_id: str, scope: str, state: P0StateStore) -> bool:
        key = (component_id, scope)
        if key in self.activations:
            return False

        activation = KnowledgeActivation(
            component_id=component_id,
            scope=scope,
            activated_step=state.step,
        )
        if component_id == "K-INFO-001":
            obj = state.create_object(
                state_type="OBLIGATION",
                status="OPEN",
                scope=scope,
                content=(
                    "Keep protected final-evaluation outcomes outside development "
                    "until development choices are explicitly locked."
                ),
                source_refs=[component_id],
                tags=["knowledge_instance:K-INFO-001"],
                reason="Protected-final-evaluation safeguard became applicable.",
                trigger=component_id,
            )
            activation.instance_object_ids.append(obj.id)
        elif component_id == "K-INFO-002":
            q = state.create_object(
                state_type="QUESTION",
                status="OPEN",
                scope=scope,
                content=(
                    "Does the inherited/evaluated workflow fit any learned transformation "
                    "using information outside the legitimate training portion?"
                ),
                source_refs=[component_id],
                tags=[
                    "knowledge_instance:K-INFO-002",
                    "priority:blocking",
                    "inherited_evaluation",
                ],
                reason="Inspected inherited code activates learned-transformation boundary review.",
                trigger=component_id,
            )
            o = state.create_object(
                state_type="OBLIGATION",
                status="OPEN",
                scope=scope,
                content=(
                    "Before relying on inherited validation evidence, resolve whether its "
                    "learned preprocessing respected the evaluation training boundary."
                ),
                source_refs=[component_id, q.id],
                tags=["knowledge_instance:K-INFO-002", "priority:blocking"],
                reason="Create repair/verification obligation for inherited evaluation integrity.",
                trigger=component_id,
            )
            activation.instance_object_ids.extend([q.id, o.id])
        elif component_id == "K-INFO-003":
            q = state.create_object(
                state_type="QUESTION",
                status="OPEN",
                scope=scope,
                content=(
                    "Which proposed predictor features are actually available at the "
                    "represented prediction moment, and which timing claims remain provisional?"
                ),
                source_refs=[component_id],
                tags=["knowledge_instance:K-INFO-003", "feature_eligibility"],
                reason="Prediction moment plus observed feature schema activates eligibility review.",
                trigger=component_id,
            )
            activation.instance_object_ids.append(q.id)
        elif component_id == "K-VAL-001":
            q = state.create_object(
                state_type="QUESTION",
                status="OPEN",
                scope=scope,
                content=(
                    "What generalization regime must validation estimate given future "
                    "prediction, repeated entities, temporal structure, and possible new entities?"
                ),
                source_refs=[component_id],
                tags=[
                    "knowledge_instance:K-VAL-001",
                    "priority:blocking",
                    "validation_regime",
                ],
                reason="Repeated entities plus temporal future prediction activate validation-regime question.",
                trigger=component_id,
            )
            activation.instance_object_ids.append(q.id)
        else:  # pragma: no cover - guarded by fixed component library
            raise ValueError(f"Unknown knowledge component {component_id!r}")

        self.activations[key] = activation
        return True

    def reopen(
        self,
        component_id: str,
        state: P0StateStore,
        *,
        repair_priority: bool = False,
        reason: str,
        source_ref: str,
    ) -> bool:
        key = (component_id, "project")
        activation = self.activations.get(key)
        if activation is None:
            return False
        reopened = False
        for object_id in activation.instance_object_ids:
            obj = state.objects.get(object_id)
            if obj is None:
                continue
            if obj.type == "QUESTION" and obj.status in {"RESOLVED", "BLOCKED"}:
                state.update_status(
                    object_id,
                    "REOPENED",
                    reason=reason,
                    trigger=component_id,
                    source_refs=[source_ref],
                )
                if repair_priority:
                    state.add_tags(
                        object_id,
                        ["priority:repair"],
                        reason="Reopened knowledge question is now a repair concern.",
                        trigger=component_id,
                    )
                reopened = True
            elif obj.type == "OBLIGATION" and obj.status == "SATISFIED":
                state.update_status(
                    object_id,
                    "OPEN",
                    reason=reason,
                    trigger=component_id,
                    source_refs=[source_ref],
                )
                if repair_priority:
                    state.add_tags(
                        object_id,
                        ["priority:repair"],
                        reason="Reopened knowledge obligation is now a repair concern.",
                        trigger=component_id,
                    )
                reopened = True
        if reopened:
            activation.reopen_count += 1
        return reopened

    def active_component_payload(self) -> list[dict[str, Any]]:
        payload = []
        for (component_id, scope), activation in sorted(self.activations.items()):
            component = KNOWLEDGE_COMPONENTS[component_id]
            payload.append(
                {
                    "component_id": component_id,
                    "scope": scope,
                    "title": component["title"],
                    "role": component["role"],
                    "content": component["content"],
                    "instance_object_ids": list(activation.instance_object_ids),
                    "reopen_count": activation.reopen_count,
                }
            )
        return payload


@dataclass(frozen=True)
class P0TreatmentRunResult:
    condition: str
    run_id: str
    completed: bool
    completed_within_budget: bool
    budget_exhausted: bool
    model_calls: int
    generation_attempts: int
    generation_failures: int
    terminal_generation_error: str | None
    input_tokens: int
    output_tokens: int
    total_tokens: int
    python_execution_attempts: int
    messages: tuple[ModelMessage, ...]
    workspace: ExperimentWorkspace
    deterministic_evaluation: dict[str, Any]
    state_snapshot: dict[str, Any]
    state_history: tuple[dict[str, Any], ...]
    knowledge_activations: tuple[dict[str, Any], ...]


class P0TreatmentRunner:
    """Execute P0 with one structured state patch plus one common action per turn."""

    def __init__(
        self,
        *,
        bundle_dir: str | Path,
        model: ModelClient,
        run_id: str,
        max_model_calls: int = 24,
        max_total_tokens: int = 250_000,
        max_python_execution_attempts: int = 12,
        max_generation_retries: int = 2,
        trace_path: str | Path | None = None,
    ) -> None:
        if max_model_calls <= 0:
            raise ValueError("max_model_calls must be positive.")
        if max_total_tokens <= 0:
            raise ValueError("max_total_tokens must be positive.")
        if max_python_execution_attempts <= 0:
            raise ValueError("max_python_execution_attempts must be positive.")
        if max_generation_retries < 0:
            raise ValueError("max_generation_retries cannot be negative.")

        self.bundle_dir = Path(bundle_dir)
        self.model = model
        self.run_id = run_id
        self.condition = "P0"
        self.max_model_calls = max_model_calls
        self.max_total_tokens = max_total_tokens
        self.max_python_execution_attempts = max_python_execution_attempts
        self.max_generation_retries = max_generation_retries

        self.workspace = ExperimentWorkspace(
            self.bundle_dir,
            run_id=run_id,
            condition="P0",
            enforce_protected_final_test=True,
            trace_path=trace_path,
        )
        self.state = P0StateStore()
        self.knowledge = P0KnowledgeActivator()
        self._initialize_state()

        self.model_calls = 0
        self.generation_attempts = 0
        self.generation_failures = 0
        self.terminal_generation_error: str | None = None
        self.input_tokens = 0
        self.output_tokens = 0
        self.total_tokens = 0
        self.python_execution_attempts = 0
        self.budget_exhausted = False

        self.messages: list[ModelMessage] = [
            ModelMessage(
                role="system",
                content="\n\n".join(
                    [
                        "You are the reasoning engine for a controlled autonomous data-science experiment.",
                        _GENERIC_METHODOLOGY,
                        P0_ARCHITECTURE_INSTRUCTION,
                        _COMMAND_CONTRACT,
                    ]
                ),
            ),
            ModelMessage(
                role="user",
                content=(
                    "Begin the project. Use the common command interface and maintain "
                    "the explicit project state supplied separately. Do not assume "
                    "access to information not exposed by the runtime."
                ),
            ),
            self._state_view_message(),
        ]

    def _initialize_state(self) -> None:
        for path in sorted((self.bundle_dir / "visible").iterdir()):
            if path.is_file():
                self.state.register_artifact(path.name, kind=_artifact_kind_from_name(path.name))
        self.state.create_object(
            state_type="OBLIGATION",
            status="OPEN",
            scope="project",
            content=(
                "Produce a defensible predictive model, validation rationale, and final "
                "performance report while preserving methodological integrity."
            ),
            source_refs=["project_request"],
            tags=["deliverable", "priority:deliverable"],
            reason="Initialize the common project deliverable need.",
            trigger="project_request",
        )

    def _state_view_message(self) -> ModelMessage:
        payload = {
            "state": self.state.compact_view(),
            "active_knowledge": self.knowledge.active_component_payload(),
            "resource_status": {
                "successful_model_calls": self.model_calls,
                "max_successful_model_calls": self.max_model_calls,
                "observed_total_tokens": self.total_tokens,
                "max_observed_total_tokens": self.max_total_tokens,
                "python_execution_attempts": self.python_execution_attempts,
                "max_python_execution_attempts": self.max_python_execution_attempts,
            },
        }
        return ModelMessage(
            role="user",
            content="P0_STATE_VIEW\n" + json.dumps(payload, sort_keys=True, default=str),
        )

    def run(self) -> P0TreatmentRunResult:
        completed = False

        for turn_index in range(1, self.max_model_calls + 1):
            if self.total_tokens >= self.max_total_tokens:
                self._record_budget_exhaustion("total_token_budget_before_model_call")
                break

            generation = self._generate_with_retries(turn_index=turn_index)
            if generation is None:
                break

            self.model_calls += 1
            self._accumulate_usage(generation.usage)
            self._trace_successful_generation(generation, turn_index=turn_index)

            payload = dict(generation.payload)
            self.messages.append(
                ModelMessage(
                    role="assistant",
                    content=json.dumps(payload, sort_keys=True, default=str),
                )
            )

            tool_result, completed = self._process_payload(payload)
            self.messages.append(
                ModelMessage(
                    role="user",
                    content="HARNESS_RESULT\n"
                    + json.dumps(tool_result, sort_keys=True, default=str),
                )
            )

            if completed:
                break

            if self.total_tokens > self.max_total_tokens:
                self._record_budget_exhaustion("total_token_budget_crossed_by_completed_call")
                break

            self.messages.append(self._state_view_message())

        if not completed and self.model_calls >= self.max_model_calls:
            self._record_budget_exhaustion("successful_model_call_budget_exhausted")

        deterministic = evaluate_deterministic_behavior(
            bundle_dir=self.bundle_dir,
            events=self.workspace.events,
            phase_1_report=self.workspace.phase_1_report,
            final_lock_report=self.workspace.final_lock_report,
        )

        completed_within_budget = completed and not self.budget_exhausted
        return P0TreatmentRunResult(
            condition="P0",
            run_id=self.run_id,
            completed=completed,
            completed_within_budget=completed_within_budget,
            budget_exhausted=self.budget_exhausted,
            model_calls=self.model_calls,
            generation_attempts=self.generation_attempts,
            generation_failures=self.generation_failures,
            terminal_generation_error=self.terminal_generation_error,
            input_tokens=self.input_tokens,
            output_tokens=self.output_tokens,
            total_tokens=self.total_tokens,
            python_execution_attempts=self.python_execution_attempts,
            messages=tuple(self.messages),
            workspace=self.workspace,
            deterministic_evaluation=deterministic,
            state_snapshot=self.state.snapshot(),
            state_history=tuple(change.to_dict() for change in self.state.history),
            knowledge_activations=tuple(
                activation.to_dict()
                for _, activation in sorted(self.knowledge.activations.items())
            ),
        )

    def _process_payload(self, payload: Mapping[str, Any]) -> tuple[dict[str, Any], bool]:
        rationale = str(payload.get("rationale", ""))
        command = payload.get("command")
        patch = payload.get("state_patch")
        motivators = payload.get("motivator_ids")
        if not isinstance(command, Mapping):
            return self._state_control_error("Model response requires a command mapping."), False
        if not isinstance(patch, Mapping):
            return self._state_control_error("Model response requires a state_patch mapping."), False
        if not isinstance(motivators, list) or not all(isinstance(x, str) for x in motivators):
            return self._state_control_error("motivator_ids must be a list of state IDs."), False

        candidate_state = copy.deepcopy(self.state)
        candidate_knowledge = copy.deepcopy(self.knowledge)
        try:
            patch_result = candidate_state.apply_model_patch(patch)
            self._reopen_knowledge_after_patch(
                candidate_state,
                candidate_knowledge,
                patch_result["changed_object_ids"],
            )
            candidate_knowledge.evaluate(candidate_state)
            resolved_motivators = [
                patch_result["client_ref_map"].get(item, item) for item in motivators
            ]
            candidate_state.validate_motivators(resolved_motivators)
            action = candidate_state.create_action(
                command=command,
                motivator_ids=resolved_motivators,
                status="PROPOSED",
                rationale=rationale,
            )
        except Exception as exc:
            blocked_action = self.state.create_action(
                command=command,
                motivator_ids=[m for m in motivators if m in self.state.objects],
                status="BLOCKED",
                rationale=f"State/controller rejected proposal: {exc}",
            )
            self.workspace.trace.append(
                event_type="P0_STATE_CONTROL_ERROR",
                phase=self.workspace.phase,
                category=ActionCategory.REPORTING,
                purpose="Reject an invalid P0 state patch or runnable-frontier proposal.",
                allowed=False,
                blocked_reason=str(exc),
                details={"action_state_id": blocked_action.id},
            )
            return {
                "status": "error",
                "error_type": type(exc).__name__,
                "error": str(exc),
            }, False

        self.state = candidate_state
        self.knowledge = candidate_knowledge

        if (
            str(command.get("type", "")) == "execute_python"
            and self.python_execution_attempts >= self.max_python_execution_attempts
        ):
            self.budget_exhausted = True
            self.state.update_status(
                action.id,
                "BLOCKED",
                reason="Python execution-attempt budget is exhausted.",
                trigger="resource_budget",
                propagate=False,
            )
            self.workspace.trace.append(
                event_type="P0_PYTHON_BUDGET_BLOCK",
                phase=self.workspace.phase,
                category=ActionCategory.REPORTING,
                purpose="Prevent a Python execution beyond the common registered limit.",
                allowed=False,
                blocked_reason="Python execution-attempt budget exhausted.",
                details={
                    "attempts": self.python_execution_attempts,
                    "limit": self.max_python_execution_attempts,
                    "action_state_id": action.id,
                },
            )
            return {
                "status": "blocked",
                "reason": "Python execution-attempt budget exhausted.",
            }, False

        before_events = len(self.workspace.events)
        try:
            self.state.update_status(
                action.id,
                "ALLOWED",
                reason="State patch and runnable-frontier checks passed.",
                trigger="controller",
                propagate=False,
            )
            result, completed = self._dispatch_common_command(command)
            new_events = self.workspace.events[before_events:]
            if any(event.event_type == "EXECUTE_PYTHON" and event.allowed for event in new_events):
                self.python_execution_attempts += 1

            if result.get("status") == "blocked":
                self.state.update_status(
                    action.id,
                    "BLOCKED",
                    reason=str(result.get("reason", "Common runtime blocked action.")),
                    trigger="workspace_gate",
                    propagate=False,
                )
            else:
                self.state.update_status(
                    action.id,
                    "EXECUTED",
                    reason="Common runtime executed the proposed action.",
                    trigger="workspace",
                    propagate=False,
                )
                self._synchronize_state_after_common_result(command, result)
                newly_activated = self.knowledge.evaluate(self.state)
                if newly_activated:
                    self.workspace.trace.append(
                        event_type="P0_KNOWLEDGE_ACTIVATED",
                        phase=self.workspace.phase,
                        category=ActionCategory.REPORTING,
                        purpose="Record newly applicable structured knowledge components.",
                        details={"components": newly_activated},
                    )
            return result, completed
        except Exception as exc:
            self.state.update_status(
                action.id,
                "FAILED",
                reason=str(exc),
                trigger="command_error",
                propagate=False,
            )
            self.workspace.trace.append(
                event_type="TREATMENT_COMMAND_ERROR",
                phase=self.workspace.phase,
                category=ActionCategory.REPORTING,
                purpose="Record a P0 command that the common runtime could not execute.",
                details={
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                    "action_state_id": action.id,
                },
            )
            return {
                "status": "error",
                "error_type": type(exc).__name__,
                "error": str(exc),
            }, False

    def _reopen_knowledge_after_patch(
        self,
        state: P0StateStore,
        knowledge: P0KnowledgeActivator,
        changed_ids: Sequence[str],
    ) -> None:
        for object_id in changed_ids:
            obj = state.objects.get(object_id)
            if obj is None or obj.status != "INVALIDATED":
                continue
            if "feature_eligibility" in obj.tags:
                knowledge.reopen(
                    "K-INFO-003",
                    state,
                    repair_priority=True,
                    reason="A feature-eligibility dependency was invalidated by new evidence.",
                    source_ref=object_id,
                )
            if "validation_regime" in obj.tags:
                knowledge.reopen(
                    "K-VAL-001",
                    state,
                    repair_priority=True,
                    reason="A validation-regime dependency was invalidated by new evidence.",
                    source_ref=object_id,
                )

    def _synchronize_state_after_common_result(
        self,
        command: Mapping[str, Any],
        result: Mapping[str, Any],
    ) -> None:
        command_type = str(command.get("type", ""))
        artifact_id = command.get("artifact_id")
        if isinstance(artifact_id, str):
            artifact_obj = self.state.artifact_object(artifact_id)
            if artifact_obj is not None:
                if command_type == "read_text":
                    self.state.add_tags(
                        artifact_obj.id,
                        ["inspected"],
                        reason="Artifact text was inspected successfully.",
                        trigger=artifact_id,
                    )
                elif command_type == "table_metadata":
                    self.state.add_tags(
                        artifact_obj.id,
                        ["metadata_inspected"],
                        reason="Table metadata was inspected successfully.",
                        trigger=artifact_id,
                    )
                elif command_type == "table_sample":
                    self.state.add_tags(
                        artifact_obj.id,
                        ["values_inspected"],
                        reason="Table values were sampled successfully.",
                        trigger=artifact_id,
                    )

        if command_type == "execute_python":
            for item in command.get("input_artifacts", []):
                if isinstance(item, str):
                    artifact_obj = self.state.artifact_object(item)
                    if artifact_obj is not None:
                        self.state.add_tags(
                            artifact_obj.id,
                            ["values_inspected"],
                            reason="Artifact values participated in Python execution.",
                            trigger=item,
                        )

        if command_type == "phase_1_complete" and result.get("status") == "ok":
            phase2_path = self.bundle_dir / "phase_2" / "crm_field_timing_notice.md"
            if phase2_path.exists():
                self.state.register_artifact(
                    "crm_field_timing_notice.md",
                    kind=_artifact_kind_from_name("crm_field_timing_notice.md"),
                )

        if command_type == "final_model_locked" and result.get("status") == "ok":
            for activation in self.knowledge.activations.values():
                if activation.component_id == "K-INFO-001":
                    for object_id in activation.instance_object_ids:
                        obj = self.state.objects.get(object_id)
                        if obj is not None and obj.type == "OBLIGATION" and obj.status == "OPEN":
                            self.state.update_status(
                                object_id,
                                "SATISFIED",
                                reason="Development is now explicitly locked before final evaluation.",
                                trigger="final_model_locked",
                                propagate=False,
                            )

        if command_type == "submit_final_report" and result.get("status") == "ok":
            for obj in self.state.objects.values():
                if obj.type == "OBLIGATION" and "deliverable" in obj.tags and obj.status == "OPEN":
                    self.state.update_status(
                        obj.id,
                        "SATISFIED",
                        reason="Final project report submitted.",
                        trigger="submit_final_report",
                        propagate=False,
                    )

    def _dispatch_common_command(
        self,
        command: Mapping[str, Any],
    ) -> tuple[dict[str, Any], bool]:
        command_type = str(command.get("type", ""))

        if command_type == "list_artifacts":
            return {"status": "ok", "artifacts": self.workspace.list_artifacts()}, False

        if command_type == "read_text":
            try:
                text = self.workspace.read_text(
                    _required_str(command, "artifact_id"),
                    purpose=_required_str(command, "purpose"),
                )
            except ActionBlockedError as exc:
                return {"status": "blocked", "reason": str(exc)}, False
            return {"status": "ok", "text": text}, False

        if command_type == "table_metadata":
            try:
                metadata = self.workspace.table_metadata(
                    _required_str(command, "artifact_id"),
                    purpose=_required_str(command, "purpose"),
                )
            except ActionBlockedError as exc:
                return {"status": "blocked", "reason": str(exc)}, False
            return {"status": "ok", "metadata": metadata}, False

        if command_type == "table_sample":
            rows = int(command.get("rows", 5))
            try:
                sample = self.workspace.table_sample(
                    _required_str(command, "artifact_id"),
                    purpose=_required_str(command, "purpose"),
                    rows=rows,
                )
            except ActionBlockedError as exc:
                return {"status": "blocked", "reason": str(exc)}, False
            return {"status": "ok", "rows": sample}, False

        if command_type == "execute_python":
            category = ActionCategory(_required_str(command, "category"))
            input_artifacts = command.get("input_artifacts", [])
            if not isinstance(input_artifacts, list) or not all(
                isinstance(item, str) for item in input_artifacts
            ):
                raise ValueError("execute_python input_artifacts must be a list of strings.")
            try:
                execution = self.workspace.execute_python(
                    _required_str(command, "code"),
                    input_artifacts=input_artifacts,
                    purpose=_required_str(command, "purpose"),
                    category=category,
                )
            except ActionBlockedError as exc:
                return {"status": "blocked", "reason": str(exc)}, False
            return {"status": "ok", "execution": execution}, False

        if command_type == "phase_1_complete":
            report = _required_report(command)
            _validate_development_report(report, milestone="phase_1_complete")
            blocking = [
                obj.id
                for obj in self.state.active_motivators()
                if "priority:blocking" in obj.tags
            ]
            if blocking:
                return {
                    "status": "blocked",
                    "reason": (
                        "Phase 1 cannot close while blocking methodological concerns remain open: "
                        + ", ".join(blocking)
                    ),
                }, False
            self.workspace.signal_phase_1_complete(report)
            return {
                "status": "ok",
                "phase": self.workspace.phase.value,
                "newly_available": ["crm_field_timing_notice.md"],
            }, False

        if command_type == "final_model_locked":
            report = _required_report(command)
            _validate_development_report(report, milestone="final_model_locked")
            repair = [
                obj.id
                for obj in self.state.active_motivators()
                if "priority:repair" in obj.tags
            ]
            if repair:
                return {
                    "status": "blocked",
                    "reason": (
                        "Final model cannot lock while repair concerns remain open: "
                        + ", ".join(repair)
                    ),
                }, False
            self.workspace.signal_final_model_locked(report)
            return {"status": "ok", "phase": self.workspace.phase.value}, False

        if command_type == "submit_final_report":
            report = _required_report(command)
            self.workspace.submit_final_report(report)
            return {"status": "ok", "run_complete": True}, True

        raise ValueError(f"Unknown treatment command type: {command_type!r}")

    def _state_control_error(self, message: str) -> dict[str, Any]:
        self.workspace.trace.append(
            event_type="P0_STATE_CONTROL_ERROR",
            phase=self.workspace.phase,
            category=ActionCategory.REPORTING,
            purpose="Reject malformed structured P0 response.",
            allowed=False,
            blocked_reason=message,
        )
        return {"status": "error", "error_type": "ValueError", "error": message}

    def _generate_with_retries(self, *, turn_index: int) -> ModelGeneration | None:
        max_attempts = self.max_generation_retries + 1
        for attempt_in_turn in range(1, max_attempts + 1):
            if self.total_tokens >= self.max_total_tokens:
                self._record_budget_exhaustion("total_token_budget_before_generation_attempt")
                return None
            self.generation_attempts += 1
            try:
                return self.model.generate(tuple(self.messages))
            except Exception as exc:
                self.generation_failures += 1
                is_model_error = isinstance(exc, ModelGenerationError)
                provider = exc.provider if is_model_error else None
                error_code = exc.error_code if is_model_error else None
                retryable = exc.retryable if is_model_error else True
                failed_usage = exc.usage if is_model_error else ModelUsage()
                provider_metadata = (
                    dict(exc.provider_metadata) if is_model_error else {}
                )
                self._accumulate_usage(failed_usage)
                self.workspace.trace.append(
                    event_type="MODEL_GENERATION_ERROR",
                    phase=self.workspace.phase,
                    category=ActionCategory.REPORTING,
                    purpose="Record a failed P0 model-generation attempt.",
                    allowed=False,
                    blocked_reason=str(exc),
                    details={
                        "turn_index": turn_index,
                        "attempt_in_turn": attempt_in_turn,
                        "max_attempts_for_turn": max_attempts,
                        "error_type": type(exc).__name__,
                        "error": str(exc),
                        "provider": provider,
                        "error_code": error_code,
                        "retryable": retryable,
                        "usage": {
                            "input_tokens": failed_usage.input_tokens,
                            "output_tokens": failed_usage.output_tokens,
                            "total_tokens": failed_usage.total_tokens,
                        },
                        "provider_metadata": provider_metadata,
                    },
                )
                if self.total_tokens >= self.max_total_tokens:
                    self._record_budget_exhaustion("total_token_budget_crossed_by_failed_attempt")
                    return None
                if (not retryable) or attempt_in_turn == max_attempts:
                    self.terminal_generation_error = f"{type(exc).__name__}: {exc}"
                    self.workspace.trace.append(
                        event_type="RUN_TERMINATED_GENERATION_ERROR",
                        phase=self.workspace.phase,
                        category=ActionCategory.PHASE_CONTROL,
                        purpose="Terminate P0 because generation cannot continue under retry policy.",
                        allowed=False,
                        blocked_reason=self.terminal_generation_error,
                        details={
                            "turn_index": turn_index,
                            "generation_attempts": self.generation_attempts,
                            "generation_failures": self.generation_failures,
                            "retryable": retryable,
                            "provider": provider,
                            "error_code": error_code,
                        },
                    )
                    return None
        raise AssertionError("Unreachable generation retry state.")

    def _trace_successful_generation(
        self,
        generation: ModelGeneration,
        *,
        turn_index: int,
    ) -> None:
        usage = generation.usage
        command = generation.payload.get("command")
        command_type = (
            str(command.get("type"))
            if isinstance(command, Mapping) and command.get("type") is not None
            else None
        )
        self.workspace.trace.append(
            event_type="MODEL_GENERATION",
            phase=self.workspace.phase,
            category=ActionCategory.REPORTING,
            purpose="Record one successful P0 provider-neutral reasoning generation.",
            details={
                "turn_index": turn_index,
                "successful_model_call": self.model_calls,
                "generation_attempts_so_far": self.generation_attempts,
                "generation_failures_so_far": self.generation_failures,
                "model_name": generation.model_name,
                "command_type": command_type,
                "usage": {
                    "input_tokens": usage.input_tokens,
                    "output_tokens": usage.output_tokens,
                    "total_tokens": usage.total_tokens,
                },
                "provider_metadata": dict(generation.provider_metadata),
            },
        )

    def _accumulate_usage(self, usage: ModelUsage) -> None:
        self.input_tokens += int(usage.input_tokens or 0)
        self.output_tokens += int(usage.output_tokens or 0)
        self.total_tokens += int(usage.total_tokens or 0)

    def _record_budget_exhaustion(self, reason: str) -> None:
        if self.budget_exhausted:
            return
        self.budget_exhausted = True
        self.workspace.trace.append(
            event_type="RESOURCE_BUDGET_EXHAUSTED",
            phase=self.workspace.phase,
            category=ActionCategory.PHASE_CONTROL,
            purpose="Record exhaustion of the registered P0 treatment resource envelope.",
            allowed=False,
            blocked_reason=reason,
            details={
                "model_calls": self.model_calls,
                "max_model_calls": self.max_model_calls,
                "total_tokens": self.total_tokens,
                "max_total_tokens": self.max_total_tokens,
                "python_execution_attempts": self.python_execution_attempts,
                "max_python_execution_attempts": self.max_python_execution_attempts,
            },
        )


def _string_list(value: Any, field_name: str) -> list[str]:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"{field_name} must be a list of strings.")
    return list(value)


def _artifact_kind_from_name(name: str) -> str:
    suffix = Path(name).suffix.lower()
    if suffix == ".csv":
        return "csv"
    if suffix == ".md":
        return "markdown"
    if suffix == ".py":
        return "python"
    return "text"
