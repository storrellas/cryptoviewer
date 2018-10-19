from django.db import models


# {'kind': 'option', 'currency': 'USD', 'pricePrecision': 4, 'strike': 20000.0,
# 'optionType': 'call', 'isActive': True, 'minTradeSize': 0.1, 'settlement': 'month',
# 'baseCurrency': 'BTC', 'expiration': '2019-06-28 08:00:00 GMT', 'tickSize': 0.0005,
# 'instrumentName': 'BTC-28JUN19-20000-C', 'created': '2018-10-04 11:14:09 GMT'}

# {"kind":"future","baseCurrency":"BTC","currency":"USD","minTradeSize":1,
# "instrumentName":"BTC-28DEC18","isActive":true,"settlement":"month",
# "created":"2018-07-27 08:06:03 GMT","tickSize":0.5,"pricePrecision":1,
# "expiration":"2018-12-28 08:00:00 GMT","contractSize":10.0}


class Instrument(models.Model):
    contractSize = models.CharField(max_length=10,null=True)
    kind = models.CharField(max_length=10,null=True)
    currency = models.CharField(max_length=10,null=True)
    pricePrecision = models.IntegerField(null=True)
    strike = models.DecimalField(max_digits=10, decimal_places=5,null=True)
    optionType = models.CharField(max_length=10,null=True)
    isActive = models.BooleanField(null=True)
    minTradeSize = models.DecimalField(max_digits=10, decimal_places=5,null=True)
    settlement = models.CharField(max_length=10,null=True)
    baseCurrency = models.CharField(max_length=10,null=True)
    # TODO: Find a way to import DateTimeField as it comes from Deribit
    #expiration = models.DateTimeField(null=True)
    expiration = models.CharField(max_length=20,null=True)
    tickSize = models.DecimalField(max_digits=10, decimal_places=5,null=True)
    instrumentName = models.CharField(max_length=100,null=True)
    # TODO: Find a way to import DateTimeField as it comes from Deribit
    #created = models.DateTimeField(null=True)
    created = models.CharField(max_length=20,null=True)


# {'instrument': 'BTC-28JUN19-20000-C', 'tradeId': 10135458, 'indexPrice': 6402.21,
# 'quantity': 3.0, 'tickDirection': 2, 'tradeSeq': 34, 'direction': 'sell', 'amount': 3.0,
# 'timeStamp': 1539886563453, 'price': 0.018, 'iv': 78.58}
class Trade(models.Model):
    instrument = models.ForeignKey('Instrument', on_delete=models.CASCADE)
    tradeId = models.IntegerField(primary_key=True)
    indexPrice = models.DecimalField(max_digits=10, decimal_places=5)
    quantity = models.DecimalField(max_digits=10, decimal_places=5)
    tickDirection = models.IntegerField()
    tradeSeq = models.IntegerField()
    direction = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=5)
    timestamp = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=5)
    iv = models.DecimalField(max_digits=10, decimal_places=5)
