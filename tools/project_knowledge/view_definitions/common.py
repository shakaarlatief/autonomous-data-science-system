"""Implementation files that determine every persistent view.

This is the fixed generation TCB and the complete-admission schema closure. A
byte change here legitimately invalidates every view. View-specific files
(specification module, unit declarations, pure sources) are listed by each view
definition and must not be added here.
"""

# Must equal views.GENERATED_ROOT; validate_specifications rejects any output outside it.
GENERATED_ROOT = "docs/project_knowledge/generated/"

SHARED_IMPLEMENTATION_FILES = (
    "tools/project_knowledge/model.py", "tools/project_knowledge/views.py",
    "tools/project_knowledge/services/generation.py", "tools/project_knowledge/services/validation.py",
    "tools/project_knowledge/services/discovery.py", "tools/project_knowledge/adapters/gitio.py",
    "tools/project_knowledge/adapters/fsio.py", "tools/project_knowledge/adapters/schema.py",
    "tools/project_knowledge/declaration.py", "tools/project_knowledge/references.py",
    "schemas/project_knowledge/defs.v1.schema.json",
    "schemas/project_knowledge/semantic_source.v1.schema.json",
    "schemas/project_knowledge/workstream.v1.schema.json",
    "schemas/project_knowledge/governing_procedure.v1.schema.json",
    "schemas/project_knowledge/project_boundary.v1.schema.json",
    "schemas/project_knowledge/identity_transition.v1.schema.json",
    "schemas/project_knowledge/joint_authority.v1.schema.json",
    "schemas/project_knowledge/capture.v1.schema.json",
    "schemas/project_knowledge/derived_view_manifest.v1.schema.json",
    "tools/project_knowledge/__init__.py", "tools/project_knowledge/adapters/__init__.py",
    "tools/project_knowledge/services/__init__.py",
    "tools/project_knowledge/adapters/execution.py",
    "tools/project_knowledge/adapters/pure.py",
    "tools/project_knowledge/view_definitions/common.py",
)
