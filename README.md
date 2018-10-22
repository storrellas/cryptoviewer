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
