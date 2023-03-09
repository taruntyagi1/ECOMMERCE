[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/home/sammy/myprojectdir
ExecStart=/home/sammy/myprojectdir/myprojectenv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          myproject.wsgi:application

[Install]
WantedBy=multi-user.target

/home/ubuntu/Myprojects/ECOMMERCE


/home/ubuntu/Myprojects/ECOMMERCE/myprojectenv

ecommeceNgix

server {
    listen 80;
    server_name 18.191.197.255;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        autoindex on;
        root /home/ubuntu/Myprojects/ECOMMERCE;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}



git_password = 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


/*gunicorn*/

[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target



[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/Myprojects/ECOMMERCE
ExecStart=/home/ubuntu/Myprojects/ECOMMERCE/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          ecommerce.wsgi:application

[Install]
WantedBy=multi-user.target



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Ecommerce',
        'USER': 'postgres',
        'PASSWORD': 'tarunroot',
        'HOST': 'database-2.cvuk9hr7ijcp.us-east-2.rds.amazonaws.com',
        'PORT': '5432',
       
    }
}