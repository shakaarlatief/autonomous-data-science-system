from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HARNESS_PATHS = [
    "experiments/r8c_assurance_probe_v01/README.md",
    "experiments/r8c_assurance_probe_v01/p_d5_adapter_fidelity.py",
]


class ProbeFailure(RuntimeError):
    pass


def git_blob(commit: str, path: str) -> bytes:
    cp = subprocess.run(
        ["git", "show", f"{commit}:{path}"],
        cwd=ROOT,
        capture_output=True,
        check=False,
    )
    if cp.returncode:
        raise ProbeFailure(cp.stderr.decode("utf-8", errors="replace"))
    return cp.stdout


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def harness_binding(commit: str) -> dict[str, object]:
    return {
        "hash_basis": "GIT_BLOB_BYTES_AT_COMMIT",
        "commit": commit,
        "files": {path: sha256(git_blob(commit, path)) for path in HARNESS_PATHS},
    }


def run_pytest_case(case: str) -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix=f"p-d5-{case}-") as tmp:
        root = Path(tmp)
        xml_path = root / "result.xml"
        if case == "pass":
            (root / "test_case.py").write_text(
                "def test_ok():\n    assert 2 + 2 == 4\n", encoding="utf-8"
            )
        elif case == "fail":
            (root / "test_case.py").write_text(
                "def test_bad():\n    assert 2 + 2 == 5\n", encoding="utf-8"
            )
        elif case == "skipped":
            (root / "test_case.py").write_text(
                "import pytest\n@pytest.mark.skip(reason='fixture')\ndef test_skip():\n    pass\n",
                encoding="utf-8",
            )
        elif case == "collection_error":
            (root / "test_case.py").write_text(
                "def test_broken(:\n    pass\n", encoding="utf-8"
            )
        elif case == "zero":
            pass
        else:
            raise ValueError(case)

        cp = subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                "-q",
                str(root),
                f"--junitxml={xml_path}",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        xml_bytes = xml_path.read_bytes() if xml_path.exists() else b""
        return {
            "case": case,
            "returncode": cp.returncode,
            "stdout": cp.stdout,
            "stderr": cp.stderr,
            "xml": xml_bytes.decode("utf-8", errors="replace"),
        }


def aggregate_counts(root: ET.Element) -> tuple[int, int, int, int]:
    suites = [root] if root.tag == "testsuite" else list(root.findall(".//testsuite"))
    if not suites and root.tag == "testsuites":
        suites = list(root)
    tests = sum(int(s.attrib.get("tests", "0")) for s in suites)
    failures = sum(int(s.attrib.get("failures", "0")) for s in suites)
    errors = sum(int(s.attrib.get("errors", "0")) for s in suites)
    skipped = sum(int(s.attrib.get("skipped", "0")) for s in suites)
    return tests, failures, errors, skipped


def adapt_pytest_junit(xml_text: str, claim_name: str | None = None) -> str:
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return "HARNESS_INVALID"

    tests, failures, errors, skipped = aggregate_counts(root)
    if errors:
        return "HARNESS_INVALID"
    if tests == 0:
        return "INCOMPLETE"

    if claim_name is not None:
        matched = [
            node for node in root.findall(".//testcase")
            if node.attrib.get("name") == claim_name
        ]
        if not matched:
            return "UNVERIFIED"
        if any(node.find("failure") is not None for node in matched):
            return "FAIL"
        if all(node.find("skipped") is not None for node in matched):
            return "INCOMPLETE"
        return "PASS"

    if failures:
        return "FAIL"
    if skipped == tests:
        return "INCOMPLETE"
    return "PASS"


def faulty_pytest_adapter(xml_text: str) -> str:
    try:
        ET.fromstring(xml_text)
    except ET.ParseError:
        return "HARNESS_INVALID"
    return "PASS"


def adapt_jw1_json(text: str) -> str:
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        return "HARNESS_INVALID"
    if not isinstance(payload, dict) or type(payload.get("ok")) is not bool:
        return "HARNESS_INVALID"
    return "PASS" if payload["ok"] else "FAIL"


def faulty_jw1_adapter(text: str) -> str:
    try:
        json.loads(text)
    except json.JSONDecodeError:
        return "HARNESS_INVALID"
    return "PASS"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--harness-commit", required=True)
    ap.add_argument("--source-commit", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)

    product_cases = {
        name: run_pytest_case(name)
        for name in ("pass", "fail", "skipped", "collection_error", "zero")
    }

    expected_product = {
        "pass": "PASS",
        "fail": "FAIL",
        "skipped": "INCOMPLETE",
        "collection_error": "HARNESS_INVALID",
        "zero": "INCOMPLETE",
    }
    product_states = {
        name: adapt_pytest_junit(row["xml"])
        for name, row in product_cases.items()
    }
    if product_states != expected_product:
        raise ProbeFailure(
            f"Product adapter mismatch: expected={expected_product}, observed={product_states}"
        )

    pass_xml = product_cases["pass"]["xml"]
    truncated = pass_xml[: max(1, len(pass_xml) // 2)]
    truncated_state = adapt_pytest_junit(truncated)
    if truncated_state != "HARNESS_INVALID":
        raise ProbeFailure("truncated Product result was not HARNESS_INVALID")

    zero_match_state = adapt_pytest_junit(pass_xml, claim_name="missing_claim_case")
    if zero_match_state != "UNVERIFIED":
        raise ProbeFailure("zero claim match was not UNVERIFIED")

    bad_product = faulty_pytest_adapter(product_cases["fail"]["xml"])
    if bad_product == product_states["fail"]:
        raise ProbeFailure("faulty Product adapter witness did not discriminate")

    jw1_native = {
        "pass": json.dumps(
            {"command": "validate", "ok": True, "validated_sources": 3},
            sort_keys=True,
        ),
        "fail": json.dumps(
            {
                "command": "validate",
                "ok": False,
                "error": {"code": "INVALID_PROJECT_KNOWLEDGE", "message": "fixture"},
            },
            sort_keys=True,
        ),
        "truncated": '{"command":"validate","ok":',
    }
    jw1_states = {
        key: adapt_jw1_json(value) for key, value in jw1_native.items()
    }
    expected_jw1 = {
        "pass": "PASS",
        "fail": "FAIL",
        "truncated": "HARNESS_INVALID",
    }
    if jw1_states != expected_jw1:
        raise ProbeFailure(
            f"JW1 adapter mismatch: expected={expected_jw1}, observed={jw1_states}"
        )

    bad_jw1 = faulty_jw1_adapter(jw1_native["fail"])
    if bad_jw1 == jw1_states["fail"]:
        raise ProbeFailure("faulty JW1 adapter witness did not discriminate")

    cli_blob = git_blob(args.source_commit, "tools/project_knowledge/cli.py")
    cli_text = cli_blob.decode("utf-8")
    if '"ok": False' not in cli_text or 'return 0 if payload["ok"] else 1' not in cli_text:
        raise ProbeFailure("frozen JW1 CLI result contract evidence not found")

    payload = {
        "probe": "P-D5",
        "protocol": "Research 277",
        "candidate": "WARRANT-F V0.2",
        "result": "PASS",
        "harness_binding": harness_binding(args.harness_commit),
        "source_binding": {
            "commit": args.source_commit,
            "jw1_cli_path": "tools/project_knowledge/cli.py",
            "jw1_cli_sha256": sha256(cli_blob),
        },
        "product_native_path": {
            "format": "pytest-junit-xml",
            "states": product_states,
            "truncated_state": truncated_state,
            "zero_claim_match_state": zero_match_state,
            "faulty_adapter_fail_case": bad_product,
        },
        "jw1_native_path": {
            "format": "project_knowledge-cli-json",
            "states": jw1_states,
            "faulty_adapter_fail_case": bad_jw1,
        },
        "required_mapping": {
            "native_pass": "PASS",
            "native_fail": "FAIL",
            "crash_or_collection": "HARNESS_INVALID",
            "zero_collected": "INCOMPLETE",
            "skipped_only": "INCOMPLETE",
            "truncated_or_unparseable": "HARNESS_INVALID",
            "zero_claim_matches": "UNVERIFIED",
        },
        "assertions": {
            "product_adapter_mapping": "PASS",
            "jw1_adapter_mapping": "PASS",
            "product_faulty_adapter_detected": True,
            "jw1_faulty_adapter_detected": True,
            "owner_import_of_engineering_required": False,
        },
        "interpretation": {
            "target_architecture": "SUPPORTED",
            "engineering_consumer_side_adapter_viable": True,
            "physical_migration_authorized": False,
        },
    }
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"probe": "P-D5", "result": "PASS"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
