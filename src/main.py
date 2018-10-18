from deribit_api import RestClient
client = RestClient("4omiTN8nVPSyp", "ZWF6TYENRB7N2BVDEZIUYW7ACNMWXE5A")
client.index()
client.account()

# Get instruments
instruments = client.getinstruments()

print(instruments)

# Get Last trades
lastrades = client.getlasttrades(instruments[0]['instrumentName'])

print(lastrades)
