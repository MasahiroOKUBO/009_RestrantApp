# 009_RestrantApp
restrantapp refactor

```
sudo apt-get update
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi
sudo apt-get install git
sudo apt-get install python-pip
sudo pip install flask 
sudo pip install sqlalchemy 
sudo pip install httplib2
sudo pip install oauth2client
git clone https://github.com/MasahiroOKUBO/009_RestrantApp.git ~/restaurant
sudo ln -sT ~/restaurant /var/www/html/restaurant

sudo vi /etc/apache2/sites-enabled/000-default.conf

import sys
sys.path.insert(0, '/var/www/html/flaskapp')

from flaskapp import app as application
sudo apachectl restart
```
