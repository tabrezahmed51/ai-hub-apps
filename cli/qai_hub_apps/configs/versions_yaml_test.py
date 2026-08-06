# ---------------------------------------------------------------------
# Copyright (c) 2025 Qualcomm Technologies, Inc. and/or its subsidiaries.
# SPDX-License-Identifier: BSD-3-Clause
# ---------------------------------------------------------------------
from __future__ import annotations

from pathlib import Path

import pytest
from pydantic import ValidationError

from qai_hub_apps.configs.versions_yaml import VersionsConfig


def test_load_valid_versions_yaml(tmp_path: Path):
    p = tmp_path / "versions.yaml"
    p.write_text("python_version: '3.10'\n")
    config = VersionsConfig.load(p)
    assert config.python_version == "3.10"


def test_load_missing_required_field_raises(tmp_path: Path):
    p = tmp_path / "versions.yaml"
    p.write_text("other_field: value\n")
    with pytest.raises(ValidationError):
        VersionsConfig.load(p)


def test_load_extra_fields_ignored(tmp_path: Path):
    p = tmp_path / "versions.yaml"
    p.write_text("python_version: '3.11'\nextra_key: ignored\n")
    config = VersionsConfig.load(p)
    assert config.python_version == "3.11"


def test_load_missing_file_raises(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        VersionsConfig.load(tmp_path / "nonexistent.yaml")
