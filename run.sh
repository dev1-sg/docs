#!/usr/bin/env bash

set -exo pipefail

uv venv --clear
source .venv/bin/activate
uv pip install -r pyproject.toml

uv run python3 scripts/generate-docker-image-assets.py > docker-image-assets.md
