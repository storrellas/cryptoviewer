import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../lib/')


from deribit_api_cryptoviewer import RestClient
from localsettings import *

client = RestClient(DERIBIT_KEY, DERIBIT_SECRET)
client.index()
client.account()

# Get instruments
instruments = client.getinstruments()

#print(instruments[1])
print(instruments)

# Get Last trades
#lastrades = client.getlasttrades(instruments[1]['instrumentName'])

#print(lastrades[0])
