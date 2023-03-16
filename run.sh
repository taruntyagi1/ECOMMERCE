

export DJANGO_ENV=production

# Activate virtual environment
source /home/ubuntu/Myprojects/ECOMMERCE/venv/bin/activate

# Collect static files


# Start Gunicorn
exec gunicorn ecommerce.wsgi:application \
    --name ecommerce \
    --workers 3 \
    --bind unix:/run/gunicorn.sock \
    --access-logfile /var/log/gunicorn/access.log \
    --error-logfile /var/log/gunicorn/error.log \
    --log-level debug