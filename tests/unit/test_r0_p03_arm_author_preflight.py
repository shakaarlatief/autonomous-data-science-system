"""Receipt classification only; no model, ACL changes or host launch."""
import errno
import os
from pathlib import Path

import pytest

from experiments.r0_p03_navigation_probe.arm_author_synthetic_preflight import (
    fixture_bytes, qualification, read_observation,
)


def test_exact_native_fixture_bytes(tmp_path):
    target = tmp_path / "fake.txt"
    target.write_text("SYNTHETIC_ONLY\n", encoding="utf-8")
    assert fixture_bytes("SYNTHETIC_ONLY") == ("SYNTHETIC_ONLY" + os.linesep).encode()
    result = read_observation(target, fixture_bytes("SYNTHETIC_ONLY"))
    assert result["status"] == "ACCESS_SUCCEEDED" and result["exact_bytes"]


def test_missing_target_is_never_denial(tmp_path):
    assert read_observation(tmp_path / "missing", b"fake") == {"status": "MISSING_TARGET"}


@pytest.mark.parametrize("exception,status", [
    (PermissionError(errno.EACCES, "fake denied"), "OS_DENIED"),
    (OSError(errno.EIO, "fake I/O failure"), "EXECUTION_UNAVAILABLE"),
])
def test_actual_io_error_classes(monkeypatch, exception, status):
    def fail(self):
        raise exception
    monkeypatch.setattr(Path, "read_bytes", fail)
    assert read_observation(Path("synthetic"), b"fake")["status"] == status


def test_mismatched_success_still_proves_access(tmp_path):
    target = tmp_path / "fake"
    target.write_bytes(b"different fake")
    result = read_observation(target, b"expected fake")
    assert result["status"] == "ACCESS_SUCCEEDED" and not result["exact_bytes"]


@pytest.mark.parametrize("observations", [{}, {"build": True}, {"all_files": "OS_DENIED"}])
def test_command_observations_never_qualify_model_host(observations):
    assert qualification(observations) == "NOT_QUALIFIED"
