#!/usr/bin/env bash

PYTHONPATH="$( dirname "$(pwd)")";
export PYTHONPATH;

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )";

# Changes the folder to: repository: /src/server | Docker: /picasso/server
cd "$(dirname "$(dirname "$(dirname "${SCRIPT_DIR}")")")"/server || exit;

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py migrate --fake sessions zero
python manage.py migrate --fake-initial
python manage.py collectstatic --noinput

if ! [[-z "${DEBUG}"]]; then
  python manage.py createsuperuser --noinput
  echo "webserver [django] > superuser has been created"
else
  echo "webserver [django] > superuser already exists (DEBUG mode is disabled)"
fi

daphne -b 0.0.0.0 -p 8000 config.asgi:application
