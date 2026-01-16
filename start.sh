#!/usr/bin/env bash
set -o errexit
python -m gunicorn your_project.wsgi:application --workers 4 --bind 0.0.0.0:$PORT
