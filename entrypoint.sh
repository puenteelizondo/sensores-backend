#!/bin/bash

# Migraciones
python manage.py migrate

# Correr el servidor
exec python manage.py runserver 0.0.0.0:8000
