#!/bin/bash

python src/manage.py migrate
python src/manage.py collectstatic --noinput

gunicorn -w 6 -b 0:8000 --chdir ./src config.wsgi:application --log-level=INFO