"""Data-only pure-unit declarations shared by more than one view.

Read as a literal from a view's own committed implementation blobs; never imported by the bound worker.
"""

PURE_UNITS = (
    ('current_state_core.v1', 'tools/project_knowledge/pure_current_state_core.py', 'current_state_core', (('single', 'core_single.v1'), ('fields', 'core_fields.v1'), ('reference', 'core_reference.v1'), ('paused', 'core_paused.v1')), ('sorted_values',)),
    ('core_single.v1', 'tools/project_knowledge/pure_current_state_core.py', 'core_single', (), ('length', 'fail_view')),
    ('core_fields.v1', 'tools/project_knowledge/pure_current_state_core.py', 'core_fields', (), ('fail_view',)),
    ('core_reference.v1', 'tools/project_knowledge/pure_current_state_core.py', 'core_reference', (('single', 'core_single.v1'),), ()),
    ('core_procedure.v1', 'tools/project_knowledge/pure_current_state_core.py', 'core_procedure', (), ('length', 'fail_view')),
    ('core_paused.v1', 'tools/project_knowledge/pure_current_state_core.py', 'core_paused', (('fields', 'core_fields.v1'), ('reference', 'core_reference.v1'), ('procedure', 'core_procedure.v1')), ('sorted_values',)),
)
