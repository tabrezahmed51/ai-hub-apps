#!/usr/bin/env bash
# ---------------------------------------------------------------------
# Copyright (c) 2025 Qualcomm Technologies, Inc. and/or its subsidiaries.
# SPDX-License-Identifier: BSD-3-Clause
# ---------------------------------------------------------------------
set -euo pipefail

REPO_ROOT=$(git rev-parse --show-toplevel)

function run_as_root()
{
    # Don't use sudo if user is root already (e.g., in docker)
    if [ "${EUID}" -eq 0 ]; then
        log_debug "We're already root; running ${*} without sudo."
        "${@}"
    else
        log_debug "We're ${EUID}; running ${*} via sudo."
        if [ -n "${GITHUB_ACTION:-}" ]; then
            SUDO_ASKPASS="${REPO_ROOT}/tools/ci/gh_askpass.sh" sudo --askpass "${@}"
        else
            sudo "${@}"
        fi
    fi
}

CURRENT_VERSION=2.36.19

if [ "$(uname)" = "Darwin" ]; then
    OS="darwin"
    ARCH="arm64"
else
    OS="linux"
    ARCH="amd64"
fi

if ! command -v saml2aws &> /dev/null || [[ "$(saml2aws --version 2>&1)" != *"${CURRENT_VERSION}"* ]]
then
    set -x
    curl --fail -o /tmp/saml2aws.tar.gz -L "https://github.com/Versent/saml2aws/releases/download/v${CURRENT_VERSION}/saml2aws_${CURRENT_VERSION}_${OS}_${ARCH}.tar.gz"
    tar -xzvf /tmp/saml2aws.tar.gz -C /tmp
    run_as_root mv /tmp/saml2aws /usr/local/bin/
    rm /tmp/saml2aws.tar.gz

    saml2aws --version
fi
