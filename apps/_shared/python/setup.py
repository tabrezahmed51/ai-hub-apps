# ---------------------------------------------------------------------
# Copyright (c) 2025 Qualcomm Technologies, Inc. and/or its subsidiaries.
# SPDX-License-Identifier: BSD-3-Clause
# ---------------------------------------------------------------------
"""Dynamic optional-dependency discovery for qai-hub-apps-utils.

Each requirements-<module>.txt file in qai_hub_apps_utils/requirements/
is automatically registered as a pip extra (e.g. [draw], [webui]).
A synthetic [full] extra installs the union of all per-module deps.
"""

from pathlib import Path

from setuptools import setup


def _extras() -> dict:
    req_dir = Path(__file__).parent / "qai_hub_apps_utils" / "requirements"
    extras: dict = {}
    for f in sorted(req_dir.glob("requirements-*.txt")):
        name = f.stem.removeprefix("requirements-")
        extras[name] = [
            line.strip()
            for line in f.read_text().splitlines()
            if line.strip() and not line.startswith("#")
        ]
    # full = union of all per-module extras (pip fails fast on conflicts)
    seen: set = set()
    full: list = []
    for deps in extras.values():
        for dep in deps:
            if dep not in seen:
                seen.add(dep)
                full.append(dep)
    extras["full"] = full
    return extras


setup(extras_require=_extras())
