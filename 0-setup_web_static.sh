#!/usr/bin/env bash
#Sets up the servers for deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p ./data
sudo mkdir -p ./data/web_static
sudo mkdir -p ./data/web_static/releases
sudo mkdir -p ./data/web_static/shared
sudo mkdir -p ./data/web_static/releases/test
echo "<h1>AirBnB</h1>" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/
sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default
sudo service nginx restart
