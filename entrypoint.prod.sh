#!/bin/sh

python ./qr_page/manage.py collectstatic --noinput
python ./qr_page/manage.py migrate --noinput

exec "$@"
