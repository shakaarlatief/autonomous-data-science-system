# P-R8B-01 Representation Probe

This is a temporary architecture-qualification harness for Research 263.

It is not the future ADS assurance/test/CI architecture and must not be treated as target repository structure.

The probe reads two real canonical sources without modifying them:

- `docs/source_universe/SOURCE_VAULT_BOOTSTRAP_WORKSTREAM.md`
- `docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md`

Run from repository root with:

```powershell
.\.venv\Scripts\python.exe experiments\r8b_representation_probe_v01\probe.py --output experiments\r8b_representation_probe_v01\results\run_001
```

The blocking gates and thresholds are preregistered in Research 263. The harness may not weaken them after seeing results.
