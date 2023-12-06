#!/usr/bin/env bash
# a script for deploying static content of airbnb clone project

sudo apt update -y
sudo apt install nginx -y
test -d "/data" && rm -rf "/data"
mkdir -p "/data/web_static"
mkdir -p "/data/web_static/releases"
mkdir -p "/data/web_static/shared"
mkdir -p "/data/web_static/releases/test"
echo "Fake Content for testing nginx" > "/data/web_static/releases/test/index.html"
source_folder="/data/web_static/releases/test/"
symbolic_link="/data/web_static/current"
if [ -L "$symbolic_link" ]; then
	rm -f "$symbolic_link"
fi
ln -s "$source_folder" "$symbolic_link"
sudo chown -R ubuntu:ubuntu "/data"
sudo rm /etc/nginx/sites-available/default
printf %s "server {
        listen 80 default_server;
        listen [::]:80 default_server;
	add_header X-Served-By $HOSTNAME;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location /hbnb_static {
	    alias /data/web_static/current;
	    index index.html index.htm;
        }

        location /redirect_me {
            return 301 https://youtube.com;
        }

	error_page 404 /404.html;
    	location = /404.html {
        	root /var/www/html/;
    	}
}
" > /etc/nginx/sites-available/default

service nginx restart
