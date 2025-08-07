#!/usr/bin/env bash

set -exo pipefail

uv venv --clear
source .venv/bin/activate
uv pip install ".[dev]"
uvx ruff check
uvx ruff format
