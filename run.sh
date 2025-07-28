#!/usr/bin/env bash

uv venv --clear
source .venv/bin/activate
uv pip install -r requirements.txt

uv run python3 scripts/generate-docker-image-assets.py > docker-image-assets.md
