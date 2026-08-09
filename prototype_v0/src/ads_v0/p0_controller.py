"""Operational P0 controller with next-turn knowledge-activation semantics.

Knowledge can become applicable because of facts created in the current model
patch. A newly instantiated blocking question cannot reasonably be cited as the
motivator for the *same* model response because its canonical ID did not exist
when that response was generated.

This controller therefore applies the following ordering:

1. validate/apply the model patch on a transactional state copy;
2. reopen already-instantiated knowledge affected by invalidation;
3. validate the proposed action against the frontier that was visible when the
   model generated it;
4. record the ACTION object;
5. instantiate any newly applicable knowledge;
6. execute the common command.

If the command is a phase transition, the common P0 phase gate sees any newly
activated blocking concern and can block the transition. For ordinary actions,
the new concern becomes part of the next state view. This preserves prospective
blocking without demanding that the model cite an object ID that did not yet
exist.

A second subtlety is that a Phase 1 feature-eligibility question may still be
OPEN when authoritative Phase 2 information invalidates a feature assumption.
That is not a semantic no-op. The existing scoped question must become a repair
priority even if its status did not need to transition from RESOLVED to
REOPENED. The controller therefore promotes the existing knowledge instance to
`priority:repair` whenever a tagged dependency is invalidated.
"""

from __future__ import annotations

import copy
from typing import Any, Mapping, Sequence

from .p0 import P0KnowledgeActivator, P0StateStore, P0TreatmentRunner as _BaseP0TreatmentRunner
from .runtime import ActionCategory


class P0TreatmentRunner(_BaseP0TreatmentRunner):
    """Final Version 0 P0 controller used by calibration and held-out execution."""

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
                    (instance.type == "QUESTION" and instance.status in {"OPEN", "REOPENED"})
                    or (instance.type == "OBLIGATION" and instance.status == "OPEN")
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
            newly_activated_from_patch = candidate_knowledge.evaluate(candidate_state)
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

        if newly_activated_from_patch:
            self.workspace.trace.append(
                event_type="P0_KNOWLEDGE_ACTIVATED",
                phase=self.workspace.phase,
                category=ActionCategory.REPORTING,
                purpose="Record knowledge activated by the current accepted state patch.",
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
                reason="State patch and visible runnable-frontier checks passed.",
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
                        purpose="Record knowledge activated by newly observed external evidence.",
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
