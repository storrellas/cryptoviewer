from deribit_api import RestClient
client = RestClient("", "")
client.index()
client.account()

# Get instruments
instruments = client.getinstruments()

print(instruments)

# Get Last trades
lastrades = client.getlasttrades(instruments[0]['instrumentName'])

print(lastrades)
