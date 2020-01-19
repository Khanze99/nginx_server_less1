sudo unlink /etc/nginx/sites-enabled/default
echo "UNLINK"
sudo cp ./etc/server.conf /etc/nginx/sites-enabled/
echo "COPY CONFIG"
