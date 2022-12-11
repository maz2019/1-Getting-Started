heroku config:set DISABLE_COLLECTSTATIC=1
python manage.py migrate
gunicorn --worker-tmp-dir /dev/shm djcrm.wsgi
