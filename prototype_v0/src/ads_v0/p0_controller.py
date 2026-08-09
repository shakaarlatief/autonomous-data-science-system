"""Operational P0 controller with prospective state and compact context semantics.

The controller resolves several timing and representation details that matter for
real-model P0 execution.

First, knowledge can become applicable because of facts created in the current
model patch. A newly instantiated blocking question cannot reasonably be the
only valid motivator for the same model response because its canonical ID did
not exist when that response was generated. The proposed action is therefore
validated against the runnable frontier visible before the patch. Newly created
client references may be listed as supplemental motivators when at least one
valid pre-patch motivator still satisfies the frontier. Newly activated blockers
still exist before command dispatch, so a phase transition can be stopped
prospectively.

Second, a model response may legitimately resolve or satisfy the very question
or obligation that motivated that response. Motivator validity must therefore
be checked against the pre-patch state rather than after status updates have
already closed the motivating object. ACTION audit records retain the resolved
canonical motivator IDs even when those objects become resolved in the same
accepted patch.

Third, the model-facing state view is a current-state interface, not the audit
log. Full ACTION objects can contain complete Python programs or milestone
reports, and retaining every historical ACTION in every subsequent state view
causes quadratic context growth when provider continuation also preserves prior
turns. The current view therefore excludes ACTION history and closed workflow
controls. It also omits audit timestamps and repeated change-history records
that are already preserved in the full append-only diagnostic state. Current
semantic content, provenance, status, tags, relations, active knowledge, and the
runnable frontier remain available to the model.

Fourth, model-created client references are an interface alias for controller-
assigned canonical state IDs. The controller exposes the latest mapping and a
small persistent alias map in the private state view, and it also resolves those
aliases deterministically in later patches. This avoids forcing the reasoner to
manually translate every remembered temporary label back to a canonical ID.
Same-patch client references still resolve locally to the object created in that
patch.

Fifth, SUPPORTS is a non-exclusive evidential relation. Losing one support path
can require reassessment of a fact, assumption, evidence item, claim, or
decision, but an OBLIGATION is governed by its own lifecycle status rather than
by evidential support sufficiency. If generic support-loss propagation creates a
reassessment obligation whose target is itself an OBLIGATION, the controller
closes that redundant secondary obligation before phase-gate evaluation. The
full audit history still records that it was created and deterministically
reconciled.

A further repair subtlety is that a Phase 1 feature-eligibility question may
still be OPEN when authoritative Phase 2 information invalidates a feature
assumption. That is not a semantic no-op. The existing scoped question becomes
a repair priority even if its status does not need to transition from RESOLVED
to REOPENED.

Finally, provider usage is known only after a call returns. If a terminal call
completes the project but pushes cumulative usage above the registered ceiling,
the project is complete but it is still a budget-exceeded run. The subclass
normalizes that terminal accounting case after the common base loop returns.
"""

from __future__ import annotations

import copy
import json
from dataclasses import replace
from typing import Any, Mapping, Sequence

from .model import ModelMessage
from .p0 import (
    P0KnowledgeActivator,
    P0StateStore,
    P0TreatmentRunResult,
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

    def run(self) -> P0TreatmentRunResult:
        """Run P0 and enforce the registered token rule on terminal calls too.

        The common base loop already stops after any nonterminal call that
        crosses the token ceiling. A terminal ``submit_final_report`` response
        returns immediately because the project is complete. Usage accounting
        still has to classify that trajectory as budget-exceeded when the
        terminal completed provider call moved cumulative usage above the hard
        envelope.
        """

        result = super().run()
        if result.total_tokens > self.max_total_tokens and not result.budget_exhausted:
            self._record_budget_exhaustion(
                "total_token_budget_crossed_by_completed_terminal_call"
            )
            return replace(
                result,
                completed_within_budget=False,
                budget_exhausted=True,
            )
        return result

    def _state_view_message(self) -> ModelMessage:
        """Return the authoritative current-state view used for the next model turn.

        The full state store remains append-only for diagnostics. The model view
        intentionally contains only current semantic fields required for the
        next reasoning step. Creation/update timestamps and recent change-history
        entries remain available in ``p0_state.json`` and
        ``p0_state_history.json`` and are not resent every turn.
        """

        visible_objects = [
            obj
            for obj in self.state.objects.values()
            if obj.status in _MODEL_VIEW_STATUSES[obj.type]
        ]
        visible_ids = {obj.id for obj in visible_objects}

        object_payloads = [
            {
                "id": obj.id,
                "type": obj.type,
                "status": obj.status,
                "scope": obj.scope,
                "content": obj.content,
                "source_refs": list(obj.source_refs),
                "tags": list(obj.tags),
            }
            for obj in visible_objects
        ]
        relations = [
            {
                "source_id": edge.source_id,
                "relation": edge.relation,
                "target_id": edge.target_id,
            }
            for edge in self.state.relations
            if edge.source_id in visible_ids and edge.target_id in visible_ids
        ]

        active_knowledge = []
        for component in self.knowledge.active_component_payload():
            if any(
                instance_id in visible_ids
                for instance_id in component["instance_object_ids"]
            ):
                active_knowledge.append(
                    {
                        "component_id": component["component_id"],
                        "title": component["title"],
                        "role": component["role"],
                        "content": component["content"],
                        "instance_object_ids": list(component["instance_object_ids"]),
                    }
                )

        payload = {
            "state": {
                "step": self.state.step,
                "objects": object_payloads,
                "relations": relations,
                "runnable_frontier": self.state.frontier(),
            },
            "active_knowledge": active_knowledge,
            "last_patch_client_ref_map": dict(
                getattr(self, "_last_patch_client_ref_map", {})
            ),
            "client_ref_aliases": dict(getattr(self, "_client_ref_aliases", {})),
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

    def _canonicalize_persistent_ref(
        self,
        ref: str,
        *,
        same_patch_client_refs: set[str],
    ) -> str:
        """Resolve an earlier model client-ref alias without shadowing local refs."""

        if ref in same_patch_client_refs:
            return ref
        return str(getattr(self, "_client_ref_aliases", {}).get(ref, ref))

    def _normalize_patch_references(
        self,
        patch: Mapping[str, Any],
    ) -> tuple[dict[str, Any], set[str]]:
        """Normalize persistent aliases in state-reference fields of one patch."""

        normalized = copy.deepcopy(dict(patch))
        creates = normalized.get("creates", [])
        same_patch_client_refs = {
            str(item.get("client_ref", ""))
            for item in creates
            if isinstance(item, Mapping) and str(item.get("client_ref", ""))
        }

        for item in normalized.get("status_updates", []):
            if isinstance(item, dict):
                ref = str(item.get("object_id", ""))
                item["object_id"] = self._canonicalize_persistent_ref(
                    ref,
                    same_patch_client_refs=same_patch_client_refs,
                )

        for field_name in ("add_relations", "remove_relations"):
            for item in normalized.get(field_name, []):
                if not isinstance(item, dict):
                    continue
                for ref_field in ("source_ref", "target_ref"):
                    ref = str(item.get(ref_field, ""))
                    item[ref_field] = self._canonicalize_persistent_ref(
                        ref,
                        same_patch_client_refs=same_patch_client_refs,
                    )

        return normalized, same_patch_client_refs

    def _resolve_action_motivators(
        self,
        requested: Sequence[str],
        *,
        same_patch_client_refs: set[str],
        patch_client_map: Mapping[str, str],
    ) -> tuple[list[str], list[str]]:
        """Return pre-patch motivators for validation and final canonical IDs.

        At least one motivator must exist in the pre-patch frontier. A client ref
        created by the current patch can be supplemental, but it cannot create
        the justification for an otherwise unmotivated action retroactively.
        """

        prepatch: list[str] = []
        supplemental_local: list[str] = []
        unknown: list[str] = []

        for raw in requested:
            ref = str(raw)
            if ref in same_patch_client_refs:
                supplemental_local.append(ref)
                continue
            canonical = self._canonicalize_persistent_ref(
                ref,
                same_patch_client_refs=same_patch_client_refs,
            )
            if canonical in self.state.objects:
                prepatch.append(canonical)
            else:
                unknown.append(ref)

        if unknown:
            raise ValueError(
                "Action cites unknown motivator IDs or aliases: " + ", ".join(unknown)
            )

        self.state.validate_motivators(list(dict.fromkeys(prepatch)))

        final_ids = list(dict.fromkeys(prepatch))
        for local_ref in supplemental_local:
            canonical = patch_client_map.get(local_ref)
            if canonical is not None and canonical not in final_ids:
                final_ids.append(canonical)
        return list(dict.fromkeys(prepatch)), final_ids

    def _reconcile_obligation_support_reassessments(self, state: P0StateStore) -> None:
        """Close redundant support-loss reassessments whose target is an obligation.

        ``SUPPORTS`` is evidential. An obligation's current force is represented
        by OPEN/SATISFIED/BLOCKED status, so losing one object that happened to
        support the deliverable does not create a second repair obligation about
        whether the original obligation still exists.
        """

        for obj in list(state.objects.values()):
            if obj.type != "OBLIGATION" or obj.status != "OPEN":
                continue
            markers = [
                tag for tag in obj.tags if tag.startswith("support_reassessment:")
            ]
            for marker in markers:
                parts = marker.split(":", 2)
                if len(parts) != 3:
                    continue
                target_id = parts[2]
                target = state.objects.get(target_id)
                if target is None or target.type != "OBLIGATION":
                    continue
                state.update_status(
                    obj.id,
                    "SATISFIED",
                    reason=(
                        "Support-loss reassessment is not applicable to an obligation "
                        "target; obligation lifecycle is represented directly by status."
                    ),
                    trigger="controller_support_semantics",
                    propagate=False,
                )
                break

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

        candidate_state = copy.deepcopy(self.state)
        candidate_knowledge = copy.deepcopy(self.knowledge)
        prepatch_motivators: list[str] = []
        try:
            normalized_patch, same_patch_client_refs = self._normalize_patch_references(
                patch
            )

            # Validate only motivators that existed in the state view that
            # preceded this response. Same-patch client refs may be supplemental,
            # but cannot retroactively satisfy the runnable-frontier requirement.
            provisional_prepatch: list[str] = []
            unknown_motivators: list[str] = []
            supplemental_local: list[str] = []
            for raw in motivators:
                if raw in same_patch_client_refs:
                    supplemental_local.append(raw)
                    continue
                canonical = self._canonicalize_persistent_ref(
                    raw,
                    same_patch_client_refs=same_patch_client_refs,
                )
                if canonical in self.state.objects:
                    provisional_prepatch.append(canonical)
                else:
                    unknown_motivators.append(raw)
            if unknown_motivators:
                raise ValueError(
                    "Action cites unknown motivator IDs or aliases: "
                    + ", ".join(unknown_motivators)
                )
            prepatch_motivators = list(dict.fromkeys(provisional_prepatch))
            self.state.validate_motivators(prepatch_motivators)

            patch_result = candidate_state.apply_model_patch(normalized_patch)
            self._reopen_knowledge_after_patch(
                candidate_state,
                candidate_knowledge,
                patch_result["changed_object_ids"],
            )
            self._reconcile_obligation_support_reassessments(candidate_state)

            canonical_motivators = list(prepatch_motivators)
            for local_ref in supplemental_local:
                canonical = patch_result["client_ref_map"].get(local_ref)
                if canonical is not None and canonical not in canonical_motivators:
                    canonical_motivators.append(canonical)

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
                    item for item in prepatch_motivators if item in self.state.objects
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
        self._last_patch_client_ref_map = dict(patch_result["client_ref_map"])
        aliases = dict(getattr(self, "_client_ref_aliases", {}))
        aliases.update(patch_result["client_ref_map"])
        self._client_ref_aliases = aliases

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
