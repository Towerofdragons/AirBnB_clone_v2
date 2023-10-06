#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static
if ! dpkg -l | grep nginx >/dev/null; then
	apt-get -y update
	apt-get install -y nginx
fi
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/
echo "Testing that it works" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "s/server_name _;/server_name _;\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}/" /etc/nginx/sites-available/default
service nginx restart
