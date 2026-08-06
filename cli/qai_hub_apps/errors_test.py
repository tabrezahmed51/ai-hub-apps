# ---------------------------------------------------------------------
# Copyright (c) 2025 Qualcomm Technologies, Inc. and/or its subsidiaries.
# SPDX-License-Identifier: BSD-3-Clause
# ---------------------------------------------------------------------
from __future__ import annotations

from pathlib import Path

from qai_hub_apps.errors import (
    AppIncompatibleError,
    AppNotFoundError,
    ModelAssetNotFoundError,
    QAIHubAppsError,
    RegistryFetchError,
    RegistryNotFoundError,
)


def test_app_not_found_message():
    err = AppNotFoundError("my_app")
    assert (
        "App 'my_app' not found. Run 'qai-hub-apps list' to see available apps."
        in str(err)
    )


def test_app_not_found_stores_id():
    err = AppNotFoundError("my_app")
    assert err.app_id == "my_app"


def test_registry_not_found_message():
    err = RegistryNotFoundError(Path("/some/path/registry.yaml"))
    msg = str(err)
    assert "Registry not found: /some/path/registry.yaml" in msg
    assert "Tip: pass --registry" in msg


def test_model_asset_not_found_no_chipset():
    err = ModelAssetNotFoundError("whisper_base")
    msg = str(err)
    assert "whisper_base" in msg
    # No "for chipset '...'" detail should appear when chipset is None
    assert "for chipset" not in msg


def test_model_asset_not_found_with_chipset():
    err = ModelAssetNotFoundError("whisper_base", chipset="snapdragon_8_gen_3")
    msg = str(err)
    assert "whisper_base" in msg
    assert "snapdragon_8_gen_3" in msg


def test_model_asset_stores_fields():
    err = ModelAssetNotFoundError("whisper_base", chipset="snapdragon_8_gen_3")
    assert err.model_id == "whisper_base"
    assert err.chipset == "snapdragon_8_gen_3"


def test_model_asset_stores_none_chipset():
    err = ModelAssetNotFoundError("whisper_base")
    assert err.chipset is None


def test_registry_fetch_error_message():
    err = RegistryFetchError("https://example.com/registry.yaml")
    msg = str(err)
    assert "https://example.com/registry.yaml" in msg
    assert "internet connection" in msg


def test_all_errors_are_qai_hub_apps_error():
    for cls in [
        AppNotFoundError,
        AppIncompatibleError,
        RegistryFetchError,
        RegistryNotFoundError,
        ModelAssetNotFoundError,
    ]:
        assert issubclass(cls, QAIHubAppsError)
