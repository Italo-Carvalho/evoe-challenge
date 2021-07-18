#!/bin/bash -x

echo "Collect static files"
python manage.py collectstatic --noinput

python manage.py migrate --noinput || exit 1
exec "$@"