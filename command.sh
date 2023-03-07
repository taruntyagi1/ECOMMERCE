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
    server_name 3.137.172.183;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ubuntu/Myporjects/ECOMMERCE;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}



git_password = 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