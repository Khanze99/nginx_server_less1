sudo rm /etc/nginx/sites-enabled/default
echo "REMOVE default config"
sudo cp ./etc/server.conf /etc/nginx/sites-enabled/
echo "COPY CONFIG"
sudo service nginx reload
