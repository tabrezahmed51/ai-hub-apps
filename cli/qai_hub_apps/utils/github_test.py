# ---------------------------------------------------------------------
# Copyright (c) 2025 Qualcomm Technologies, Inc. and/or its subsidiaries.
# SPDX-License-Identifier: BSD-3-Clause
# ---------------------------------------------------------------------
from __future__ import annotations

from qai_hub_apps.utils.github import _ISSUES_URL, make_issue_url


def test_make_issue_url_encodes_title_and_body():
    url = make_issue_url(title="Bug in app 'foo'", body="line 1\nline 2")
    assert "title=" in url
    assert "body=" in url
    assert "'" not in url.split("?", 1)[1]
    assert "\n" not in url
    assert url.startswith(_ISSUES_URL)
