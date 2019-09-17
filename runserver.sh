#!/bin/bash

cd /var/Faculdade_web
export PYTHONPATH=/var/current/Projeto_Site;$PYTHONPATH

python manage.py migrate --noinput
python manage.py initadmin
python manage.py runserver 0.0.0.0:8080