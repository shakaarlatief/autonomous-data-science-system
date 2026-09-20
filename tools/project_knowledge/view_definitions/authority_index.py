"""View definition: specification and view-private pure-unit declarations for `authority_index`."""

from ..model import RebuildabilityClass, ViewGenerator, ViewInputSelector, ViewSpecification
from .common import GENERATED_ROOT, SHARED_IMPLEMENTATION_FILES


# Data-only declarations read from this view's own committed blob; the bound worker never imports this module.
PURE_UNITS = (
    ('scope_token.v1', 'tools/project_knowledge/pure_authority_index.py', 'scope_token', (('normalize_scope', 'normalized_scope.v1'),), ('sorted_values', 'is_text')),
    ('normalized_relations.v1', 'tools/project_knowledge/pure_authority_index.py', 'normalized_relations', (('normalize_scope', 'normalized_scope.v1'), ('scope_key', 'scope_token.v1')), ('sorted_values',)),
    ('authority_candidate.v1', 'tools/project_knowledge/pure_authority_index.py', 'authority_candidate', (('normalize_scope', 'normalized_scope.v1'), ('normalize_relations', 'normalized_relations.v1'), ('unique', 'unique_values.v1')), ()),
    ('authority_index.v1', 'tools/project_knowledge/pure_authority_index.py', 'authority_index', (('authority_candidate', 'authority_candidate.v1'),), ()),
)


def authority_index_specification() -> ViewSpecification:
    """Persistent non-authoritative inputs for task-scoped G007 resolution."""
    files = SHARED_IMPLEMENTATION_FILES + (
        "tools/project_knowledge/view_definitions/authority_index.py",
        "tools/project_knowledge/view_definitions/units_normalized_scope.py",
        "tools/project_knowledge/view_definitions/units_unique_values.py",
        "tools/project_knowledge/pure_authority_index.py",
        "tools/project_knowledge/pure_normalized_scope.py",
        "tools/project_knowledge/pure_unique_values.py",
    )
    return ViewSpecification(
        "authority_index", GENERATED_ROOT + "authority_index.json",
        GENERATED_ROOT + "manifests/authority_index.json", "1", RebuildabilityClass.DETERMINISTIC_BYTE_REBUILD,
        ViewInputSelector(), ViewGenerator("project_knowledge_authority_index", "1", files),
        "authority_index.v1", "canonical_json.v1",
    )
