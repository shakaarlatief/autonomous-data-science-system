"""Operational P0 controller with prospective state and compact context semantics.

The controller resolves three timing and representation details that matter for
real-model P0 execution.

First, knowledge can become applicable because of facts created in the current
model patch. A newly instantiated blocking question cannot reasonably be cited
as the motivator for the same model response because its canonical ID did not
exist when that response was generated. The proposed action is therefore
validated against the runnable frontier visible before the patch. Newly
activated blockers still exist before command dispatch, so a phase transition
can be stopped prospectively.

Second, a model response may legitimately resolve or satisfy the very question
or obligation that motivated that response. Motivator validity must therefore
be checked against the pre-patch state rather than after status updates have
already closed the motivating object. ACTION audit records retain the original
canonical motivator IDs even when those objects become resolved in the same
accepted patch.

Third, the model-facing state view is a current-state interface, not the audit
log. Full ACTION objects can contain complete Python programs or milestone
reports, and retaining every historical ACTION in every subsequent state view
causes quadratic context growth when Responses API continuation also preserves
prior turns. The compact view therefore excludes ACTION history and closed
workflow-control objects while retaining current facts, assumptions, evidence,
claims, decisions, open concerns, artifacts, relevant relations, and a short
filtered change tail. The complete state snapshot and append-only history remain
available in P0 diagnostic artifacts for auditability.

A further repair subtlety is that a Phase 1 feature-eligibility question may
still be OPEN when authoritative Phase 2 information invalidates a feature
assumption. That is not a semantic no-op. The existing scoped question becomes
a repair priority even if its status does not need to transition from RESOLVED
to REOPENED.
"""

from __future__ import annotations

import copy
import json
from typing import Any, Mapping, Sequence

from .model import ModelMessage
from .p0 import (
    P0KnowledgeActivator,
    P0StateStore,
    P0TreatmentRunner as _BaseP0TreatmentRunner,
)
from .runtime import ActionCategory


_MODEL_VIEW_STATUSES: dict[str, set[str]] = {
    "ARTIFACT": {"AVAILABLE", "PROTECTED"},
    "FACT": {"ACTIVE", "DISPUTED"},
    "ASSUMPTION": {"PROVISIONAL", "SUPPORTED", "INVALIDATED"},
    "QUESTION": {"OPEN", "REOPENED", "BLOCKED"},
    "EVIDENCE": {"CURRENT", "INVALIDATED", "STALE"},
    "CLAIM": {"PROVISIONAL", "SUPPORTED", "WEAKENED", "INVALIDATED"},
    "DECISION": {"PROVISIONAL", "ACCEPTED", "REOPENED"},
    "OBLIGATION": {"OPEN", "BLOCKED"},
    "ACTION": set(),
}


class P0TreatmentRunner(_BaseP0TreatmentRunner):
    """Final Version 0 P0 controller used by calibration and held-out execution."""

    def _state_view_message(self) -> ModelMessage:
        """Return the authoritative current-state view used for the next model turn.

        The full state store remains append-only for diagnostics, but historical
        ACTION objects and already-closed control concerns are intentionally not
        repeated to the model. Their durable semantic consequences should be
        represented by current FACT, EVIDENCE, CLAIM, DECISION, ASSUMPTION, or
        reopened repair objects rather than by replaying prior commands.
        """

        visible_objects = [
            obj
            for obj in self.state.objects.values()
            if obj.status in _MODEL_VIEW_STATUSES[obj.type]
        ]
        visible_ids = {obj.id for obj in visible_objects}

        relations = [
            edge.to_dict()
            for edge in self.state.relations
            if edge.source_id in visible_ids and edge.target_id in visible_ids
        ]
        recent_changes = [
            change.to_dict()
            for change in self.state.history
            if change.object_id in visible_ids
        ][-12:]

        active_knowledge = []
        for component in self.knowledge.active_component_payload():
            if any(
                instance_id in visible_ids
                for instance_id in component["instance_object_ids"]
            ):
                active_knowledge.append(component)

        payload = {
            "state": {
                "step": self.state.step,
                "objects": [obj.to_dict() for obj in visible_objects],
                "relations": relations,
                "runnable_frontier": self.state.frontier(),
                "recent_changes": recent_changes,
            },
            "active_knowledge": active_knowledge,
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
            content="P0_STATE_VIEW\n"
            + json.dumps(payload, sort_keys=True, default=str),
        )

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

            component_id: str | None = None
            if "feature_eligibility" in obj.tags:
                component_id = "K-INFO-003"
            elif "validation_regime" in obj.tags:
                component_id = "K-VAL-001"

            if component_id is None:
                continue

            # If applicability already exists, keep the same scoped instance.
            # Calling evaluate is idempotent and can instantiate the component
            # here if its state pattern is already satisfied but it had not yet
            # been materialized for some earlier reason.
            knowledge.evaluate(state)
            knowledge.reopen(
                component_id,
                state,
                repair_priority=True,
                reason=(
                    "A previously accepted dependency covered by this knowledge "
                    "component was invalidated by newer project evidence."
                ),
                source_ref=object_id,
            )

            activation = knowledge.activations.get((component_id, "project"))
            if activation is None:
                continue
            for instance_id in activation.instance_object_ids:
                instance = state.objects.get(instance_id)
                if instance is None:
                    continue
                if (
                    (
                        instance.type == "QUESTION"
                        and instance.status in {"OPEN", "REOPENED"}
                    )
                    or (
                        instance.type == "OBLIGATION"
                        and instance.status == "OPEN"
                    )
                ):
                    state.add_tags(
                        instance_id,
                        ["priority:repair"],
                        reason=(
                            "An already-open scoped knowledge concern became a "
                            "material repair obligation after dependency invalidation."
                        ),
                        trigger=component_id,
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
        if not isinstance(motivators, list) or not all(
            isinstance(item, str) for item in motivators
        ):
            return self._state_control_error(
                "motivator_ids must be a list of state IDs."
            ), False

        canonical_motivators = [str(item) for item in motivators]
        candidate_state = copy.deepcopy(self.state)
        candidate_knowledge = copy.deepcopy(self.knowledge)
        try:
            # The model generated this action from the frontier in the state view
            # that preceded the response. Validate against exactly that frontier.
            # A patch may then resolve the motivating question/obligation without
            # retroactively making the action invalid.
            self.state.validate_motivators(canonical_motivators)

            patch_result = candidate_state.apply_model_patch(patch)
            self._reopen_knowledge_after_patch(
                candidate_state,
                candidate_knowledge,
                patch_result["changed_object_ids"],
            )
            action = candidate_state.create_action(
                command=command,
                motivator_ids=canonical_motivators,
                status="PROPOSED",
                rationale=rationale,
            )
            newly_activated_from_patch = candidate_knowledge.evaluate(candidate_state)
        except Exception as exc:
            blocked_action = self.state.create_action(
                command=command,
                motivator_ids=[
                    item for item in canonical_motivators if item in self.state.objects
                ],
                status="BLOCKED",
                rationale=f"State/controller rejected proposal: {exc}",
            )
            self.workspace.trace.append(
                event_type="P0_STATE_CONTROL_ERROR",
                phase=self.workspace.phase,
                category=ActionCategory.REPORTING,
                purpose=(
                    "Reject an invalid P0 state patch or runnable-frontier proposal."
                ),
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

        if newly_activated_from_patch:
            self.workspace.trace.append(
                event_type="P0_KNOWLEDGE_ACTIVATED",
                phase=self.workspace.phase,
                category=ActionCategory.REPORTING,
                purpose=(
                    "Record knowledge activated by the current accepted state patch."
                ),
                details={"components": newly_activated_from_patch},
            )

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
                purpose=(
                    "Prevent a Python execution beyond the common registered limit."
                ),
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
                reason=(
                    "State patch and visible runnable-frontier checks passed."
                ),
                trigger="controller",
                propagate=False,
            )
            result, completed = self._dispatch_common_command(command)
            new_events = self.workspace.events[before_events:]
            if any(
                event.event_type == "EXECUTE_PYTHON" and event.allowed
                for event in new_events
            ):
                self.python_execution_attempts += 1

            if result.get("status") == "blocked":
                self.state.update_status(
                    action.id,
                    "BLOCKED",
                    reason=str(
                        result.get("reason", "Common runtime blocked action.")
                    ),
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
                        purpose=(
                            "Record knowledge activated by newly observed external evidence."
                        ),
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
                purpose=(
                    "Record a P0 command that the common runtime could not execute."
                ),
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
