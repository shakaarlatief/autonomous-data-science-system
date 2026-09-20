"""View definition: specification and view-private pure-unit declarations for `identity_index`."""

from ..model import AuthorityClass, RebuildabilityClass, ViewGenerator, ViewInputSelector, ViewSpecification
from .common import GENERATED_ROOT, SHARED_IMPLEMENTATION_FILES


# Data-only declarations read from this view's own committed blob; the bound worker never imports this module.
PURE_UNITS = (
    ('identity_transition_record.v1', 'tools/project_knowledge/pure_identity_index.py', 'identity_transition_record', (('unique', 'unique_values.v1'), ('temporal', 'has_temporal_control.v1')), ()),
    ('identity_source_record.v1', 'tools/project_knowledge/pure_identity_index.py', 'identity_source_record', (('temporal', 'has_temporal_control.v1'),), ()),
    ('any_temporal.v1', 'tools/project_knowledge/pure_identity_index.py', 'any_temporal', (('temporal', 'has_temporal_control.v1'),), ()),
    ('identity_static_resolution.v1', 'tools/project_knowledge/pure_identity_index.py', 'identity_static_resolution', (('unique', 'unique_values.v1'), ('any_temporal', 'any_temporal.v1'), ('temporal', 'has_temporal_control.v1')), ('length', 'any_true', 'fail_view')),
    ('identity_index.v1', 'tools/project_knowledge/pure_identity_index.py', 'identity_index', (('transition_record', 'identity_transition_record.v1'), ('unique', 'unique_values.v1'), ('resolve_identity_row', 'identity_static_resolution.v1'), ('identity_source', 'identity_source_record.v1')), ()),
)


def identity_index_specification() -> ViewSpecification:
    """Persistent identity/history lookup over canonical plus accepted historical sources."""
    files = SHARED_IMPLEMENTATION_FILES + (
        "tools/project_knowledge/view_definitions/identity_index.py",
        "tools/project_knowledge/view_definitions/units_temporal.py",
        "tools/project_knowledge/view_definitions/units_unique_values.py",
        "tools/project_knowledge/pure_identity_index.py",
        "tools/project_knowledge/pure_temporal.py",
        "tools/project_knowledge/pure_unique_values.py",
    )
    selector = ViewInputSelector(
        authority_classes=(AuthorityClass.CANONICAL, AuthorityClass.HISTORICAL)
    )
    return ViewSpecification(
        "identity_index", GENERATED_ROOT + "identity_index.json",
        GENERATED_ROOT + "manifests/identity_index.json", "1", RebuildabilityClass.DETERMINISTIC_BYTE_REBUILD,
        selector, ViewGenerator("project_knowledge_identity_index", "1", files),
        "identity_index.v1", "canonical_json.v1",
    )
