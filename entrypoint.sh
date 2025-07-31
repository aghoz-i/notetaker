#!/bin/sh

echo "Running Django makemigrations & migrate..."
python manage.py makemigrations
python manage.py migrate

echo "Running server..."
gunicorn --bind 0.0.0.0:8000 notetaker.wsgi
