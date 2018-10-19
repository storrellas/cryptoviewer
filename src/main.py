from deribit_api import RestClient
from localsettings import *


client = RestClient(DERIBIT_KEY, DERIBIT_SECRET)
client.index()
client.account()

# Get instruments
instruments = client.getinstruments()

print(instruments[1])

# Get Last trades
lastrades = client.getlasttrades(instruments[1]['instrumentName'])

print(lastrades[0])
