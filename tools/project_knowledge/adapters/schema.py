"""Offline Draft 2020-12 validation with an explicit local resource registry."""

import json
from datetime import datetime
from pathlib import Path
import re

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

from ..model import Diagnostic, DiagnosticSeverity, Profile, RawDeclaration, SemanticId, thaw_json


# Durable validation requires this explicit schema closure. The ordinary
# directory-based validator keeps its existing WORKTREE/G001-G008 behavior.
SCHEMA_FILES = (
    "schemas/project_knowledge/defs.v1.schema.json",
    "schemas/project_knowledge/semantic_source.v1.schema.json",
    "schemas/project_knowledge/workstream.v1.schema.json",
    "schemas/project_knowledge/governing_procedure.v1.schema.json",
    "schemas/project_knowledge/project_boundary.v1.schema.json",
    "schemas/project_knowledge/identity_transition.v1.schema.json",
    "schemas/project_knowledge/joint_authority.v1.schema.json",
    "schemas/project_knowledge/capture.v1.schema.json",
    "schemas/project_knowledge/derived_view_manifest.v1.schema.json",
)


class SchemaValidator:
    def __init__(self, schema_root: Path | None = None, *, schema_blobs=None):
        if schema_blobs is not None:
            if schema_root is not None:
                raise ValueError("Choose explicit schema blobs or a schema directory")
            schemas = [json.loads(schema_blobs[path].decode("utf-8")) for path in sorted(schema_blobs)]
        else:
            root = schema_root or Path(__file__).resolve().parents[3] / "schemas" / "project_knowledge"
            schemas = [json.loads(path.read_text(encoding="utf-8")) for path in sorted(root.glob("*.schema.json"))]
        registry = Registry().with_resources((schema["$id"], Resource.from_contents(schema)) for schema in schemas)
        formats = FormatChecker()

        @formats.checks("date-time", raises=ValueError)
        def date_time(value):
            # jsonschema's optional RFC3339 dependency is not installed in all
            # repository environments. Always enforce timezone-bearing dates.
            if not isinstance(value, str):
                return True
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:[Zz]|[+-]\d{2}:\d{2})", value):
                return False
            datetime.fromisoformat(value.upper().replace("Z", "+00:00"))
            return True

        self.validators = {}
        for schema in schemas:
            Draft202012Validator.check_schema(schema)
            if "properties" in schema:
                profile = Profile(schema["properties"]["profile"]["const"])
                self.validators[profile] = Draft202012Validator(schema, registry=registry, format_checker=formats)
        if set(self.validators) != set(Profile):
            raise ValueError("All eight V1 profile schemas must be available")

    def validate(self, declaration: RawDeclaration, carrier_path: str = "") -> tuple[Diagnostic, ...]:
        value = thaw_json(declaration.fields)
        try:
            profile = Profile(value.get("profile"))
        except (ValueError, TypeError):
            return (Diagnostic("UNKNOWN_PROFILE", DiagnosticSeverity.ERROR, carrier_path, "Unsupported or missing profile"),)
        try:
            semantic_id = SemanticId(value["semantic_id"]) if "semantic_id" in value else None
        except ValueError:
            semantic_id = None
        errors = sorted(self.validators[profile].iter_errors(value), key=lambda e: (tuple(map(str, e.absolute_path)), e.message))
        return tuple(Diagnostic(
            "PROFILE_SCHEMA_VIOLATION", DiagnosticSeverity.ERROR, carrier_path,
            f"/{'/'.join(map(str, error.absolute_path))}: {error.message}", semantic_id,
        ) for error in errors)
