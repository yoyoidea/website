import os

name = os.environ.get('GUNICORN_PROC_NAME', 'website_django')
bind = os.environ.get('GUNICORN_ADDRESS', '0.0.0.0:8080')
timeout = os.environ.get('GUNICORN_TIMEOUT', 30)
workers = os.environ.get('GUNICORN_WORKERS', 5)
loglevel = os.environ.get('GUNICORN_LOG_LEVEL', 'info')
