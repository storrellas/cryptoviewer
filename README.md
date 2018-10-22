# Cryptoviewer

## Configure

1. Download the code with git

git clone https://github.com/storrellas/cryptoviewer.git

2. Create migrations

python manage.py makemigrations viewer

3. Create entities

python manage.py migrate viewer

4. Run server

python runserver

5. Open browser and go to

http://localhost:8000/views/instrument/


## Tutorial

1. Views are place under viewer\views.py

2. URL paths are place under viewer\urls.py

3. Commands are placed under 

viewer\management\commands\retrieval_instruments.py

viewer\management\commands\retrieval_trades.py

## Heroku

1. Create heroku app
heroku apps:create cryptoviewer-release

2. Append addon
heroku addons:create heroku-postgresql

3. Insert config variables
heroku config

4. Run bash into dyno
heroku run bash

./manage.py makemigrations viewer
./manage.py migrate viewer

5. Create environment
heroku config:set DERIBIT_KEY='joesmith'


[...]
DERIBIT_KEY = os.environ.get('DERIBIT_KEY', None)
[...]
