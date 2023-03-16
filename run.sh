
export ENV="production"  # or "local"

exec gunicorn ecommerce.wsgi:application \
  --bind unix:/run/gunicorn.sock \
  --workers 3 \
  --timeout 120 \
  --access-logfile /var/log/gunicorn/access.log \
  --error-logfile /var/log/gunicorn/error.log