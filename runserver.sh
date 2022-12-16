python manage.py migrate
heroku config:set DISABLE_COLLECTSTATIC=1


gunicorn --worker-tmp-dir /dev/shm djcrm.wsgi

