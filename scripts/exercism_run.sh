#!/usr/bin/env bash
set -euxo pipefail

# solve/run Python codes with uv
uv run --env-file .env src/main.py

uv run python3 -m pytest -o markers=task {exercise_test.py}