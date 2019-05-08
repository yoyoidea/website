#!/bin/bash

# Prepare log files and start outputting logs to stdout
export DJANGO_SETTINGS_MODULE=website.settings
exec gunicorn -c gunicorn.py website.wsgi:application