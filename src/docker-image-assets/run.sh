#!/usr/bin/env bash

uv venv --clear
source .venv/bin/activate
uv pip install -r requirements.txt

cdk bootstrap --qualifier d1sg-ecr
cdk deploy --all --ci --require-approval never
