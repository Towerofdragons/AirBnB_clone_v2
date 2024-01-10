#!/usr/bin/env bash
#Install and configure server for Nginx

if ! dpkg-query -W nginx | grep nginx; then
	apt-get -y update
	apt-get install -y nginx
fi

mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
echo "Testing a page" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data 

sed -i 's/server_name _;/server_name _;\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}/' /etc/nginx/sites-available/default
