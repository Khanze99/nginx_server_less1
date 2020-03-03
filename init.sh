sudo rm /etc/nginx/sites-enabled/default
echo "REMOVE default config"
sudo cp ./etc/server.conf /etc/nginx/sites-enabled/
echo "COPY CONFIG"
sudo service nginx reload
echo "NGINX RELOADED"
cd ask && gunicorn --bind=0.0.0.0:8000 --log-level=debug --workers=2 --timeout=15 ask.wsgi
