#!/bin/bash

poetry update
poetry install

poetry run isort .
poetry run black .
poetry run pre-commit run --all-files

poetry run flake8 -v optres
# --exit-zero
poetry run mypy optres

poetry run pytest -v optres
