"""Restricted current-state Markdown serializer: declarations only."""


def current_state_core_markdown(value):
    active = value["active_workstream"]
    boundary = value["integration_boundary"]
    experiment = value["current_experiment"]
    text = "# Current State Core\n\n"
    text = text + "## Active workstream\n\n"
    text = text + "- Semantic ID: " + active["semantic_id"] + "\n"
    text = text + "- State: " + active["state"] + "\n"
    text = text + "- Objective: " + active["objective"] + "\n"
    text = text + "- Stage: " + active["stage"]["stage_id"] + "\n"
    text = text + "- Checkpoint: " + as_text(active["execution_anchor"]["checkpoint"]) + "\n\n"
    text = text + "## Integration boundary\n\n"
    text = text + "- Semantic ID: " + boundary["semantic_id"] + "\n"
    text = text + "- Promoted branch: " + boundary["promoted_branch"] + "\n"
    text = text + "- Promoted commit: " + boundary["promoted_commit"] + "\n\n"
    text = text + "## Current specification and experiment\n\n"
    text = text + "- Specification: " + value["current_specification"]["semantic_id"] + "\n"
    text = text + "- Experiment: " + experiment["semantic_id"] + "\n"
    text = text + "- Outcome: " + experiment["outcome"] + "\n\n"
    text = text + "## Paused resumable workstreams\n\n"
    if length(value["paused_workstreams"]) == 0:
        text = text + "None.\n"
    else:
        for workstream in value["paused_workstreams"]:
            text = text + "- " + workstream["semantic_id"] + " -> " + workstream["resume_target"] + "\n"
    return utf8_text(text)
