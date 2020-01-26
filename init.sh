sudo rm /etc/nginx/sites-enabled/default
echo "REMOVE default config"
sudo cp ./etc/server.conf /etc/nginx/sites-enabled/
echo "COPY CONFIG"
sudo service nginx reload
echo "NGINX RELOADED"
gunicorn --bind=0.0.0.0:8080 hello:web_application
