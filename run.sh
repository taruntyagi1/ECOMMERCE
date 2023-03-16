

export DJANGO_ENV=production
# Start Gunicorn



exec gunicorn ecommerce.wsgi:application -c gunicorn_conf.py