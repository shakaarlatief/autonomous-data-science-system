"""Strict Structured Outputs schema for the P0 treatment response.

The common treatment command schema is reused verbatim. P0 adds only the
architecture-specific state patch and motivator references around that common
external action, so the observable project capability remains comparable with
B0/B1.
"""

from __future__ import annotations

from typing import Any

from .openai_model import TREATMENT_RESPONSE_SCHEMA
from .p0 import RELATION_TYPES, STATE_TYPES, STATUS_BY_TYPE


_MODEL_CREATABLE_TYPES = [state_type for state_type in STATE_TYPES if state_type != "ACTION"]
_ALL_STATUSES = sorted({status for values in STATUS_BY_TYPE.values() for status in values})


def _strict_object(properties: dict[str, Any]) -> dict[str, Any]:
    return {
        "type": "object",
        "properties": properties,
        "required": list(properties),
        "additionalProperties": False,
    }


_STATE_CREATE_SCHEMA = _strict_object(
    {
        "client_ref": {"type": "string"},
        "type": {"type": "string", "enum": _MODEL_CREATABLE_TYPES},
        "status": {"type": "string", "enum": _ALL_STATUSES},
        "scope": {"type": "string"},
        "content": {"type": "string"},
        "source_refs": {"type": "array", "items": {"type": "string"}},
        "tags": {"type": "array", "items": {"type": "string"}},
    }
)

_STATUS_UPDATE_SCHEMA = _strict_object(
    {
        "object_id": {"type": "string"},
        "new_status": {"type": "string", "enum": _ALL_STATUSES},
        "reason": {"type": "string"},
        "source_refs": {"type": "array", "items": {"type": "string"}},
    }
)

_RELATION_SCHEMA = _strict_object(
    {
        "source_ref": {"type": "string"},
        "relation": {"type": "string", "enum": list(RELATION_TYPES)},
        "target_ref": {"type": "string"},
    }
)

_STATE_PATCH_SCHEMA = _strict_object(
    {
        "creates": {"type": "array", "items": _STATE_CREATE_SCHEMA},
        "status_updates": {"type": "array", "items": _STATUS_UPDATE_SCHEMA},
        "add_relations": {"type": "array", "items": _RELATION_SCHEMA},
        "remove_relations": {"type": "array", "items": _RELATION_SCHEMA},
    }
)


P0_RESPONSE_SCHEMA: dict[str, Any] = _strict_object(
    {
        "rationale": {
            "type": "string",
            "description": "Brief decision rationale without private chain-of-thought.",
        },
        "state_patch": _STATE_PATCH_SCHEMA,
        "motivator_ids": {"type": "array", "items": {"type": "string"}},
        "command": TREATMENT_RESPONSE_SCHEMA["properties"]["command"],
    }
)
