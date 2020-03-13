sudo apt-get update
sudo apt-get install -y python3.5
sudo apt-get install -y python3.5-dev
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo pip3 install --upgrade pip
sudo pip3 install --upgrade django==2.0.7
sudo pip3 install --upgrade gunicorn
sudo pip3 install pymysql
sudo pip2 install pymysql
sudo /etc/init.d/mysql start
bash mysql_script.sh
sudo python3 ask/manage.py migrate
