#!/usr/bin/env bash

gunicorn --worker-class eventlet --bind 0.0.0.0:5000 -w 1 wsgi:app

