# ---------------------------------------------------------------------
# Copyright (c) 2025 Qualcomm Technologies, Inc. and/or its subsidiaries.
# SPDX-License-Identifier: BSD-3-Clause
# ---------------------------------------------------------------------
from __future__ import annotations

from urllib.parse import urlencode

_ISSUES_URL = "https://github.com/qualcomm/ai-hub-apps/issues/new"


def make_issue_url(title: str, body: str) -> str:
    return _ISSUES_URL + "?" + urlencode({"title": title, "body": body})
