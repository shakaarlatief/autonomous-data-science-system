"""G009 read-only orchestration: committed corpus -> one pure view builder.

No publication/CLI, staged-byte relabeling or live compatibility output writes.
Existing generated artifacts are excluded from source validation so stale views
cannot prevent rebuilding their canonical inputs or become those inputs.
"""

from dataclasses import asdict
from pathlib import Path

from ..adapters.execution import TCB_FILES, execute_snapshot, verify_checkout_implementation
from ..adapters.pure import plain_text, resolve_unit
from ..adapters.gitio import read_blobs
from ..adapters.schema import SCHEMA_FILES, SchemaValidator
from ..model import (
    AuthorityClass, RepositorySnapshot, SnapshotMode, SubstrateError, ViewFreshnessResult,
    RawDeclaration, ViewBuildResult, ViewFreshnessStatus, ViewInput, thaw_json,
)
from ..views import (
    PURE_UNIT_REGISTRY, deterministic_json, deterministic_utf8, ViewValidationError, build_views, fail, finding,
    manifest_freshness, validate_specifications,
)
from .discovery import DiscoveryPolicy, PathRole
from .validation import validate_repository


class _GenerationDiscovery(DiscoveryPolicy):
    def classify(self, path):
        # W0 compatibility surfaces remain operational authority, never source
        # material for successor derived views (Research 185). Skip even reads.
        if path in {"docs/CURRENT_STATE.md", "docs/current_routing.json",
                    "docs/CONTINUITY.md", "docs/KNOWLEDGE_MAP.md"}:
            return PathRole.EVIDENCE_FIXTURE
        if self._under(path, self.generated_root):
            return PathRole.EVIDENCE_FIXTURE
        return super().classify(path)


def _capabilities():
    # This finite audited table is infrastructure. Pure source may only CALL
    # an explicitly declared entry; it cannot retrieve/inspect the callable.
    return {"canonical_json": deterministic_json, "utf8_text": deterministic_utf8, "length": len, "sorted_values": sorted,
            "as_text": plain_text, "as_integer": int, "as_tuple": tuple, "sequence_range": range,
            "minimum": min, "maximum": max, "total": sum, "fail_view": fail}


def _generate_verified(snapshot: RepositorySnapshot, specifications, *, selected_view_ids=None, schema_blobs):
    """Discover all current inputs even when only some view IDs are selected.

    The durable entry point has already resolved qualified restricted units
    from this view's explicit Git closure. Full and selected builds both use
    this complete corpus and the same domain builder.
    """
    if snapshot.mode != SnapshotMode.COMMIT_SNAPSHOT:
        fail("NON_COMMITTED_VIEW_INPUT", "WORKTREE_SNAPSHOT is NON_COMMITTED; use exact committed Git blobs")
    specs = validate_specifications(specifications)
    selected = {s.view_id for s in specs} if selected_view_ids is None else set(selected_view_ids)
    if selected - {s.view_id for s in specs}:
        fail("UNKNOWN_VIEW_SELECTION", "Selected views require explicit specifications")
    validator = SchemaValidator(schema_blobs=schema_blobs)
    validation = validate_repository(snapshot, validator=validator, policy=_GenerationDiscovery(), durable_evidence=True)
    if not validation.ok:
        raise ViewValidationError(validation.diagnostics)
    sources = tuple(source for source in validation.sources if source.authority_class == AuthorityClass.CANONICAL)
    paths = {source.carrier_path for source in sources}
    paths.update(path for spec in specs if spec.view_id in selected for path in spec.generator.implementation_files)
    entries = {entry.path: entry for entry in snapshot.entries}
    missing = paths - entries.keys()
    if missing:
        raise ViewValidationError(finding("MISSING_VIEW_DEPENDENCY", "Required committed source/implementation blob is absent", path)
                                  for path in sorted(missing))
    blobs = read_blobs(snapshot.root, tuple(entries[path] for path in sorted(paths)))
    content = {path: blobs[entries[path].blob_id] for path in paths}
    corpus = tuple(ViewInput(source, content[source.carrier_path]) for source in sources)
    results = build_views(specs, corpus, content, snapshot_mode=snapshot.mode, selected_view_ids=selected)
    for result in results:
        diagnostics = validator.validate(result.manifest, result.manifest_path)
        if diagnostics:
            raise ViewValidationError(diagnostics)
    return results


def _freshness_verified(snapshot: RepositorySnapshot, specifications, view_id: str, manifest, *, existing_view_bytes=None, schema_blobs):
    """Schema validation plus the same complete-input builder, never old-state patching."""
    if snapshot.mode != SnapshotMode.COMMIT_SNAPSHOT:
        return ViewFreshnessResult(ViewFreshnessStatus.UNSUPPORTED_SNAPSHOT,
                                   (finding("NON_COMMITTED_VIEW_INPUT", "WORKTREE_SNAPSHOT cannot verify durable freshness"),))
    diagnostics = SchemaValidator(schema_blobs=schema_blobs).validate(manifest)
    if diagnostics:
        return ViewFreshnessResult(ViewFreshnessStatus.INVALID, diagnostics)
    try:
        result, = _generate_verified(snapshot, specifications, selected_view_ids=(view_id,), schema_blobs=schema_blobs)
        return manifest_freshness(manifest, result, existing_view_bytes=existing_view_bytes)
    except ViewValidationError as error:
        return ViewFreshnessResult(ViewFreshnessStatus.INVALID, error.diagnostics)
    except SubstrateError as error:
        return ViewFreshnessResult(ViewFreshnessStatus.INVALID, (finding(error.code, str(error)),))



def _execute_bound(snapshot, specifications, selected, operation, **extra):
    if snapshot.mode != SnapshotMode.COMMIT_SNAPSHOT:
        fail("NON_COMMITTED_VIEW_INPUT", "WORKTREE_SNAPSHOT cannot produce durable evidence")
    specs = validate_specifications(specifications)
    selected = {s.view_id for s in specs} if selected is None else set(selected)
    if selected - {s.view_id for s in specs}:
        fail("UNKNOWN_VIEW_SELECTION", "Selected views require explicit specifications")
    specs = tuple(s for s in specs if s.view_id in selected)
    if any(type(spec.compute) is not str or type(spec.serialize) is not str for spec in specs):
        fail("UNQUALIFIED_DURABLE_CALLBACK", "Durable definitions contain unit identities, never caller-provided callables")
    required = set(TCB_FILES) | set(SCHEMA_FILES)
    for spec in specs:
        if not required <= set(spec.generator.implementation_files):
            fail("INCOMPLETE_EXECUTION_BINDING", "Each durable view must declare the complete generation/schema execution closure")
    entries = {entry.path: entry for entry in snapshot.entries}
    builds = []
    for spec in specs:
        # A new interpreter and this view's own explicit files prevent another
        # selected view from supplying imports, schemas or cached module state.
        # Keep whole-set specification validation above, and recompute complete
        # current inputs through the same pure builder inside every worker.
        paths = set(spec.generator.implementation_files)
        missing = paths - entries.keys()
        if missing:
            raise ViewValidationError(finding("MISSING_VIEW_DEPENDENCY", "Required implementation blob is absent", p) for p in sorted(missing))
        raw = read_blobs(snapshot.root, tuple(entries[p] for p in sorted(paths)))
        blobs = {p: raw[entries[p].blob_id] for p in paths}
        verify_checkout_implementation(blobs)
        encoded = {"view_id": spec.view_id, "view_path": spec.view_path, "manifest_path": spec.manifest_path,
                   "view_schema_version": spec.view_schema_version, "rebuildability_class": spec.rebuildability_class,
                   "selector": asdict(spec.selector), "generator": asdict(spec.generator),
                   "compute": spec.compute, "serialize": spec.serialize}
        result = execute_snapshot({"operation": operation, "root": str(snapshot.root), "snapshot_mode": snapshot.mode,
                                   "source_commit": snapshot.source_commit, "entries": [asdict(e) for e in snapshot.entries],
                                   "repository_roots": sorted({str(snapshot.root.resolve()), str(Path(__file__).resolve().parents[3])}),
                                   "specifications": [encoded], "selected": [spec.view_id], **extra}, blobs)
        if result.get("error"):
            raise ViewValidationError(finding(d["code"], d["message"], d["carrier_path"]) for d in result["diagnostics"])
        if operation == "freshness":
            return result
        builds.extend(result["builds"])
    # No partial generated evidence escapes if any selected view fails.
    return {"builds": builds}


def generate_views(snapshot: RepositorySnapshot, specifications, *, selected_view_ids=None):
    """Durable entry point: verify execution identity, then use the same builder.

    Data-only definitions resolve committed restricted units and serializer
    capabilities. Each view gets a fresh worker and its own explicit Git closure;
    general repository imports cannot become pure view authority.
    """
    try:
        result = _execute_bound(snapshot, specifications, selected_view_ids, "build")
    except ViewValidationError:
        raise
    except SubstrateError as error:
        raise ViewValidationError((finding(error.code, str(error)),)) from error
    return tuple(ViewBuildResult(r["view_id"], r["view_path"], r["manifest_path"], bytes.fromhex(r["view_bytes"]),
                                 RawDeclaration(r["manifest"]), bytes.fromhex(r["manifest_bytes"])) for r in result["builds"])


def check_view_freshness(snapshot: RepositorySnapshot, specifications, view_id: str, manifest, *, existing_view_bytes=None):
    """Freshness cannot accept evidence using unbound Python or checkout schemas."""
    if snapshot.mode != SnapshotMode.COMMIT_SNAPSHOT:
        return ViewFreshnessResult(ViewFreshnessStatus.UNSUPPORTED_SNAPSHOT,
                                   (finding("NON_COMMITTED_VIEW_INPUT", "WORKTREE_SNAPSHOT cannot verify durable freshness"),))
    try:
        result = _execute_bound(snapshot, specifications, (view_id,), "freshness", view_id=view_id,
                                manifest=thaw_json(manifest.fields), existing_view_bytes=existing_view_bytes.hex() if existing_view_bytes is not None else None)
        return ViewFreshnessResult(result["status"], tuple(finding(d["code"], d["message"], d["carrier_path"]) for d in result["diagnostics"]))
    except ViewValidationError as error:
        return ViewFreshnessResult(ViewFreshnessStatus.INVALID, error.diagnostics)
    except SubstrateError as error:
        return ViewFreshnessResult(ViewFreshnessStatus.INVALID, (finding(error.code, str(error)),))


def _worker_dispatch(request, blobs):
    """Bound-process transport only; generation still uses the one pure builder."""
    try:
        from tools.project_knowledge.model import (
            RepositorySnapshot, SnapshotEntry, ViewSpecification, ViewGenerator,
            ViewInputSelector, RawDeclaration, thaw_json,
        )
        from tools.project_knowledge.services.generation import _generate_verified, _freshness_verified
        specs = []
        for s in request["specifications"]:
            capabilities = _capabilities()
            compute = resolve_unit(s["compute"], PURE_UNIT_REGISTRY, blobs, capabilities)
            serialize = deterministic_json if s["serialize"] == "canonical_json.v1" else resolve_unit(
                s["serialize"], PURE_UNIT_REGISTRY, blobs, capabilities)
            specs.append(ViewSpecification(s["view_id"], s["view_path"], s["manifest_path"], s["view_schema_version"],
                s["rebuildability_class"], ViewInputSelector(**s["selector"]), ViewGenerator(**s["generator"]), compute, serialize,
                compute_identity=s["compute"], serialize_identity=s["serialize"]))
        snapshot = RepositorySnapshot(Path(request["root"]), request["snapshot_mode"],
                                      tuple(SnapshotEntry(**e) for e in request["entries"]), request["source_commit"])
        schemas = {p: b for p, b in blobs.items() if p.startswith("schemas/project_knowledge/") and p.endswith(".schema.json")}
        if request["operation"] == "build":
            results = _generate_verified(snapshot, specs, selected_view_ids=request["selected"], schema_blobs=schemas)
            output = {"builds": [{"view_id": r.view_id, "view_path": r.view_path, "manifest_path": r.manifest_path,
                                 "view_bytes": r.view_bytes.hex(), "manifest": thaw_json(r.manifest.fields),
                                 "manifest_bytes": r.manifest_bytes.hex()} for r in results]}
        else:
            content = request["existing_view_bytes"]
            result = _freshness_verified(snapshot, specs, request["view_id"], RawDeclaration(request["manifest"]),
                                        existing_view_bytes=bytes.fromhex(content) if content is not None else None, schema_blobs=schemas)
            output = {"status": result.status, "diagnostics": [_diagnostic_data(d) for d in result.diagnostics]}
    except Exception as error:
        output = {"error": True, "diagnostics": [_diagnostic_data(d) for d in getattr(error, "diagnostics", ())]}
        if not output["diagnostics"]:
            output["diagnostics"] = [{"code": getattr(error, "code", "BOUND_EXECUTION_FAILED"),
                                      "message": str(error), "carrier_path": ""}]
    return output


def _diagnostic_data(d):
    return {"code": d.code, "message": d.message, "carrier_path": d.carrier_path}
