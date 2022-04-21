release: python3 manage.py migrate
web: gunicorn user.wsgi:application --preload --log-file - 