#!/bin/bash

HOST=$1
PORT=$2

until nc -z $HOST $PORT; do
  echo "Waiting for database at $HOST:$PORT to be ready..."
  sleep 2
done

echo "Database is ready!"

echo "# Starting server"
python3 manage.py migrate &
gunicorn --access-logfile - --workers 3 --log-level debug -t 300 --bind 0.0.0.0:8000 tl_notes.wsgi:application