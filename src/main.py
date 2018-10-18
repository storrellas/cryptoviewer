from deribit_api import RestClient
from localsettings import *


client = RestClient(KEY, SECRET)
client.index()
client.account()

# Get instruments
instruments = client.getinstruments()

#print(instruments[0])

# Get Last trades
lastrades = client.getlasttrades(instruments[0]['instrumentName'])

print(lastrades[0])
