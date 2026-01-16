#!/usr/bin/env bash
set -o errexit
python -m gunicorn lipetsk.wsgi:application --workers 4 --bind 0.0.0.0:$PORT
