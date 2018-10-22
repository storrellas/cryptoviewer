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

6. See Logs
sudo heroku logs -t --app=cryptoviewer-release

7. SSH into dyno (does not include config vars)
heroku ps:exec --app=cryptoviewer-release

8. Generate one-off dyno (includes config vars)
heroku run bash --app=cryptoviewer-release

# Heroku Docker

1. Login container
heroku container:login

2. Create app
heroku create --app=cryptoviewer-docker

3. Push image
sudo docker tag cryptoviewer registry.heroku.com/cryptoviewer-docker/web
sudo docker push registry.heroku.com/cryptoviewer-docker/web

4. Release
sudo heroku container:release web --app=cryptoviewer-docker
