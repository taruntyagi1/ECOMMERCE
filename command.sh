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
new_git_token = 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


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



    location /media/ {
        autoindex on;
        alias /home/ubuntu/Myprojects/ECOMMERCE/media/;
    }


#local postgres configuration


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecommerce',
        'USER': 'postgresroot',
        'PASSWORD': 'tarunroot',
        'HOST': 'localhost',
        'PORT': '',
       
    }
}


#twillo recover code


bdPmI0olPqxgD6x2lSkZr4q4mtzh8BzdGqJbmzrd
twillo_secret = 'AMWBp9VOCnRuGcC35fKjL4Tgzet4pzyv'
sid = 'SKcba42e174d022bf6634643b8e7e855f6