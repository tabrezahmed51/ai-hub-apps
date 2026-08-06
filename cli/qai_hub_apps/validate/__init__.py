# ---------------------------------------------------------------------
# Copyright (c) 2025 Qualcomm Technologies, Inc. and/or its subsidiaries.
# SPDX-License-Identifier: BSD-3-Clause
# ---------------------------------------------------------------------
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from qai_hub_apps.registry import App
from qai_hub_apps.validate.platform_check import check_platform


def is_app_supported(app: App) -> bool:
    """Return True if the app is supported in the current environment."""
    return check_platform(app)
