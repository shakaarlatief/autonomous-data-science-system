"""G009 pure complete-input view building and manifest freshness.

No discovery, clock, writes, semantic ID minting or authority resolution. Inputs
are supplied canonical Git materializations. Generated artifacts never enter the
input corpus. A smaller selection of view IDs uses this very same builder.
"""

import hashlib
import json
import re
from typing import Iterable, Mapping

from .model import (
    AuthorityClass, Diagnostic, DiagnosticSeverity, RawDeclaration, SnapshotMode,
    SubstrateError, ViewBuildResult, ViewFreshnessResult, ViewFreshnessStatus,
    ViewGenerator, ViewInput, ViewSpecification, thaw_json, validate_source_path,
)


FRESHNESS_BASIS = "G009_EXACT_INPUTS_AND_GENERATOR_V1"
GENERATED_ROOT = "docs/project_knowledge/generated/"


class ViewValidationError(SubstrateError):
    def __init__(self, diagnostics: Iterable[Diagnostic]):
        self.diagnostics = tuple(sorted(diagnostics, key=lambda d: (d.code, d.carrier_path, d.message, d.related_sources)))
        super().__init__("INVALID_VIEW_INPUT", "; ".join(d.message for d in self.diagnostics))


def finding(code, message, path=""):
    return Diagnostic(code, DiagnosticSeverity.ERROR, path, message)


def fail(code, message, path=""):
    raise ViewValidationError((finding(code, message, path),))


def deterministic_json(value):
    """Object keys are unordered; each compute contract owns its array ordering."""
    return (json.dumps(thaw_json(value), ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n").encode("utf-8")


def deterministic_utf8(value):
    """Narrow text capability for qualified serializers, including Markdown."""
    if type(value) is not str:
        fail("INVALID_VIEW_SERIALIZATION", "Text serialization requires a plain string")
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    return (value if value.endswith("\n") else value + "\n").encode("utf-8")


def validate_specifications(specifications: Iterable[ViewSpecification]) -> tuple[ViewSpecification, ...]:
    specs = tuple(sorted(specifications, key=lambda s: (s.view_id, s.view_path, s.manifest_path)))
    ids, outputs = set(), set()
    for spec in specs:
        if (not re.fullmatch(r"[A-Za-z][A-Za-z0-9_.:-]*", spec.view_id)
                or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_.:-]*", spec.generator.generator_id)
                or not spec.view_schema_version.strip() or not spec.generator.generator_version.strip()
                or not (callable(spec.compute) or type(spec.compute) is str and spec.compute)
                or not (callable(spec.serialize) or type(spec.serialize) is str and spec.serialize)
                or not isinstance(spec.compute_identity, str) or not spec.compute_identity
                or not isinstance(spec.serialize_identity, str) or not spec.serialize_identity):
            fail("INVALID_VIEW_SPECIFICATION", "View/generator identities, versions and durable execution identities must be explicit")
        if spec.view_id in ids:
            fail("DUPLICATE_VIEW_ID", "View IDs must be unique")
        ids.add(spec.view_id)
        for path in (spec.view_path, spec.manifest_path):
            try:
                validate_source_path(path)
            except ValueError as error:
                fail("INVALID_VIEW_PATH", str(error))
            if not path.startswith(GENERATED_ROOT) or path in outputs:
                fail("INVALID_VIEW_PATH", "Outputs must have distinct generated-area paths", path)
            outputs.add(path)
        if not spec.manifest_path.startswith(GENERATED_ROOT + "manifests/"):
            fail("INVALID_VIEW_PATH", "JSON manifests belong in the designated manifest area", spec.manifest_path)
        for paths in (spec.generator.implementation_files, spec.selector.prefixes, spec.selector.ordered_paths or ()):
            if len(set(paths)) != len(paths):
                fail("DUPLICATE_VIEW_DEPENDENCY", "Declared path lists must not contain duplicates")
            for path in paths:
                try:
                    validate_source_path(path)
                except ValueError as error:
                    fail("INVALID_VIEW_DEPENDENCY", str(error))
        if not spec.generator.implementation_files:
            fail("MISSING_GENERATOR_IMPLEMENTATION", "Generator file list must be explicit and nonempty")
    for spec in specs:
        if (outputs.intersection((*spec.generator.implementation_files, *(spec.selector.ordered_paths or ())))
                or any(path.startswith(GENERATED_ROOT) for path in spec.generator.implementation_files)):
            fail("CIRCULAR_VIEW_BINDING", "Generated outputs/manifests cannot be inputs or generator implementation")
    return tuple(sorted(specs, key=lambda spec: spec.view_id))


def implementation_digest(generator: ViewGenerator, blobs: Mapping[str, bytes]) -> str:
    if not generator.implementation_files or len(set(generator.implementation_files)) != len(generator.implementation_files):
        fail("INVALID_GENERATOR_FILES", "Implementation paths must be explicit, ordered and unique")
    digest = hashlib.sha256()
    for path in generator.implementation_files:
        try:
            validate_source_path(path)
        except ValueError as error:
            fail("INVALID_GENERATOR_FILES", str(error))
        if path not in blobs or not isinstance(blobs[path], bytes):
            fail("MISSING_GENERATOR_IMPLEMENTATION", "Supply exact Git bytes for every declared implementation path", path)
        digest.update(path.encode("utf-8") + b"\0" + blobs[path] + b"\0")
    return digest.hexdigest()


def _complete_inputs(spec, corpus, outputs):
    selector = spec.selector
    allowed_classes = set(selector.authority_classes)
    seen, duplicates = set(), set()
    for item in corpus:
        if item.source.authority_class in allowed_classes:
            path = item.source.carrier_path
            if path in seen:
                duplicates.add(path)
            seen.add(path)
    if duplicates:
        fail("DUPLICATE_VIEW_INPUT", "Selected input paths must be unique", min(duplicates))
    selected, canonical_identities = {}, set()
    for item in sorted(corpus, key=lambda item: item.source.carrier_path):
        source = item.source
        if source.authority_class not in allowed_classes:
            continue
        path = source.carrier_path
        if path in outputs or path.startswith(GENERATED_ROOT):
            fail("CIRCULAR_VIEW_BINDING", "Generated content cannot enter governed view inputs", path)
        if path in selected:
            fail("DUPLICATE_VIEW_INPUT", "Selected input paths must be unique", path)
        if source.authority_class == AuthorityClass.CANONICAL and source.semantic_id is not None:
            if source.semantic_id in canonical_identities:
                fail("DUPLICATE_VIEW_INPUT_IDENTITY", "Canonical input identities must be unique")
            canonical_identities.add(source.semantic_id)
        revision = source.revision
        if source.snapshot_mode != SnapshotMode.COMMIT_SNAPSHOT or revision is None:
            fail("NON_COMMITTED_VIEW_INPUT", "Durable views require exact COMMIT_SNAPSHOT inputs", path)
        if revision.source_path != path or hashlib.sha256(item.content).hexdigest() != revision.content_digest:
            fail("VIEW_INPUT_DIGEST_MISMATCH", "Input must match its exact governed Git revision", path)
        selected[path] = item
    paths = selector.ordered_paths if selector.ordered_paths is not None else sorted(selected)
    return tuple(selected[path] for path in paths if path in selected
                 and (not selector.profiles or selected[path].source.profile in selector.profiles)
                 and (not selector.prefixes or any(path == p or path.startswith(p + "/") for p in selector.prefixes)))


def _manifest(spec, inputs, blobs):
    bindings = []
    for item in inputs:
        source = item.source
        binding = {"source_path": source.carrier_path, "hash_algorithm": "sha256",
                   "hash_basis": "GIT_BLOB_BYTES_AT_COMMIT", "content_digest": source.revision.content_digest}
        if source.semantic_id is not None:
            binding["semantic_id"] = source.semantic_id.value
        bindings.append(binding)
    data = {"schema_version": "1", "profile": "derived_view_manifest.v1", "kind": "derived_view_manifest",
            "authority_class": "derived", "view_id": spec.view_id, "view_path": spec.view_path,
            "view_schema_version": spec.view_schema_version, "input_bindings": bindings,
            "generator": {"generator_id": spec.generator.generator_id, "generator_version": spec.generator.generator_version,
                          "implementation_basis": "GIT_BLOB_BYTES_AT_COMMIT",
                          "implementation_files": list(spec.generator.implementation_files),
                          "implementation_digest": implementation_digest(spec.generator, blobs)},
            "rebuildability_class": spec.rebuildability_class,
            "freshness_basis": FRESHNESS_BASIS, "snapshot_mode": "COMMIT_SNAPSHOT", "snapshot_status": "COMMITTED"}
    # Content-derived boundary; no wall clock or final/output commit SHA. The
    # boundary is computed before inserting itself, avoiding digest circularity.
    # Bind the data-only executable choice independently of implementation bytes:
    # two qualified units may already coexist in the same exact Git closure.
    if not spec.compute_identity or not spec.serialize_identity:
        fail("UNBOUND_VIEW_EXECUTION_CONTRACT", "Durable manifests require explicit compute and serializer identities")
    boundary = {"manifest": data, "selection_contract": {
        "profiles": sorted(set(spec.selector.profiles)),
        "prefixes": sorted(set(spec.selector.prefixes)),
        "ordered_paths": spec.selector.ordered_paths,
        "authority_classes": sorted(set(spec.selector.authority_classes))}, "execution_contract": {
        "compute_unit": spec.compute_identity, "serializer": spec.serialize_identity}}
    data["created_or_refreshed_boundary"] = "sha256:" + hashlib.sha256(deterministic_json(boundary)).hexdigest()
    return RawDeclaration(data)


def bind_view_inputs(specifications, corpus: Iterable[ViewInput], implementation_blobs: Mapping[str, bytes], *,
                     snapshot_mode: SnapshotMode, selected_view_ids: Iterable[str] | None = None):
    """Shared complete-input selection and manifest binding, without compute.

    G013 compares these exact bindings, including the execution contract, rather
    than maintaining another selector/dependency interpretation or reading old
    generated artifacts. This is also the binding stage of every normal build.
    """
    if SnapshotMode(snapshot_mode) != SnapshotMode.COMMIT_SNAPSHOT:
        fail("NON_COMMITTED_VIEW_INPUT", "WORKTREE_SNAPSHOT is NON_COMMITTED; durable generation is unsupported")
    specs = validate_specifications(specifications)
    selected = {spec.view_id for spec in specs} if selected_view_ids is None else set(selected_view_ids)
    if selected - {spec.view_id for spec in specs}:
        fail("UNKNOWN_VIEW_SELECTION", "Selected view IDs must have explicit specifications")
    corpus = tuple(corpus)
    outputs = {path for spec in specs for path in (spec.view_path, spec.manifest_path)}
    results = []
    for spec in specs:
        if spec.view_id not in selected:
            continue
        inputs = _complete_inputs(spec, corpus, outputs)
        manifest = _manifest(spec, inputs, implementation_blobs)
        results.append((spec, inputs, manifest))
    return tuple(results)


def build_views(specifications, corpus: Iterable[ViewInput], implementation_blobs: Mapping[str, bytes], *,
                snapshot_mode: SnapshotMode, selected_view_ids: Iterable[str] | None = None) -> tuple[ViewBuildResult, ...]:
    """Full and selected operation share complete selection/compute/serialize.

    corpus is the complete current canonical corpus, never a changed-file delta.
    No persisted view state is accepted by this builder. The repository service
    obtains the corpus itself, so selecting view IDs cannot truncate its inputs.
    """
    results = []
    for spec, inputs, manifest in bind_view_inputs(
            specifications, corpus, implementation_blobs, snapshot_mode=snapshot_mode,
            selected_view_ids=selected_view_ids):
        if not callable(spec.compute) or not callable(spec.serialize):
            fail("UNRESOLVED_VIEW_UNIT", "Resolve declared units before entering the lower-level builder")
        # Only plain value projections reach compute; no enums, descriptors or
        # repository-domain objects are capabilities of a durable unit.
        projected = tuple({"source_path": item.source.carrier_path,
                           "semantic_id": item.source.semantic_id.value if item.source.semantic_id else None,
                           "profile": item.source.profile.value,
                           "authority_class": item.source.authority_class.value,
                           "state": item.source.state.value if item.source.state else None,
                           "content_digest": item.source.revision.content_digest,
                           "declaration": item.source.declaration.fields,
                           "content": item.content} for item in inputs)
        value = spec.compute(projected)
        content = spec.serialize(value)
        if not isinstance(content, bytes):
            fail("INVALID_VIEW_SERIALIZATION", "Serializer must return immutable bytes", spec.view_path)
        # JSON views must use the frozen encoding, not a competing JSON format.
        if spec.view_path.lower().endswith(".json"):
            try:
                valid = deterministic_json(json.loads(content)) == content
            except (ValueError, UnicodeError):
                valid = False
            if not valid:
                fail("INVALID_VIEW_SERIALIZATION", "JSON must be canonical UTF-8/LF, two-space indentation and final newline", spec.view_path)
        results.append(ViewBuildResult(spec.view_id, spec.view_path, spec.manifest_path, content,
                                       manifest, deterministic_json(manifest.fields)))
    return tuple(results)


def manifest_freshness(manifest: RawDeclaration, expected: ViewBuildResult, *,
                       existing_view_bytes: bytes | None = None) -> ViewFreshnessResult:
    """Compare a schema-validated manifest to a complete current rebuild.

    FRESH describes binding equality only, never governing authority. Supplying
    output bytes additionally checks the artifact itself against the rebuild.
    """
    actual, current = manifest.fields, expected.manifest.fields
    if actual.get("snapshot_mode") != "COMMIT_SNAPSHOT" or actual.get("snapshot_status") != "COMMITTED":
        return ViewFreshnessResult(ViewFreshnessStatus.UNSUPPORTED_SNAPSHOT,
                                   (finding("NON_COMMITTED_VIEW_MANIFEST", "Manifest cannot claim durable freshness", expected.manifest_path),))
    fixed = ("schema_version", "profile", "kind", "authority_class", "view_id", "view_path", "view_schema_version",
             "rebuildability_class", "freshness_basis")
    if set(actual) != set(current) or any(actual.get(key) != current[key] for key in fixed):
        return ViewFreshnessResult(ViewFreshnessStatus.INVALID,
                                   (finding("INCOMPATIBLE_VIEW_MANIFEST", "Manifest metadata does not match the current view contract", expected.manifest_path),))
    findings = []
    for key, code in (("input_bindings", "STALE_VIEW_INPUTS"), ("generator", "STALE_VIEW_GENERATOR"),
                      ("created_or_refreshed_boundary", "STALE_VIEW_BOUNDARY")):
        if actual.get(key) != current[key]:
            findings.append(finding(code, f"Manifest {key} differs from the complete current build", expected.manifest_path))
    if existing_view_bytes is not None and existing_view_bytes != expected.view_bytes:
        findings.append(finding("STALE_VIEW_CONTENT", "Artifact bytes differ from the complete current rebuild", expected.view_path))
    return ViewFreshnessResult(ViewFreshnessStatus.STALE if findings else ViewFreshnessStatus.FRESH, tuple(sorted(findings, key=lambda d: d.code)))
