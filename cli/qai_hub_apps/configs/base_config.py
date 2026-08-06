# ---------------------------------------------------------------------
# Copyright (c) 2025 Qualcomm Technologies, Inc. and/or its subsidiaries.
# SPDX-License-Identifier: BSD-3-Clause
# ---------------------------------------------------------------------
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, ConfigDict
from typing_extensions import Self


class BaseConfig(BaseModel):
    """Lightweight config base: Pydantic v2 model with YAML deserialization."""

    model_config = ConfigDict(extra="ignore")

    @classmethod
    def from_yaml(cls, path: Path | str) -> Self:
        with open(path, encoding="utf-8") as f:
            data: dict[str, Any] = yaml.safe_load(f)
        return cls.model_validate(data)
