

export DJANGO_ENV=production
# Start Gunicorn



exec gunicorn -c /home/ubuntu/Myprojects/ECOMMERCE/gunicorn_conf.py ecommerce.wsgi
