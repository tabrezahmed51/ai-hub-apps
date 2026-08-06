# ---------------------------------------------------------------------
# Copyright (c) 2025 Qualcomm Technologies, Inc. and/or its subsidiaries.
# SPDX-License-Identifier: BSD-3-Clause
# ---------------------------------------------------------------------
from __future__ import annotations

from pathlib import Path

from qai_hub_apps.configs.base_config import BaseConfig


class VersionsConfig(BaseConfig):
    python_version: str

    @classmethod
    def load(cls, path: Path) -> VersionsConfig:
        return cls.from_yaml(path)
