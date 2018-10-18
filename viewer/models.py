from django.db import models


# {'kind': 'option', 'currency': 'USD', 'pricePrecision': 4, 'strike': 20000.0,
# 'optionType': 'call', 'isActive': True, 'minTradeSize': 0.1, 'settlement': 'month',
# 'baseCurrency': 'BTC', 'expiration': '2019-06-28 08:00:00 GMT', 'tickSize': 0.0005,
# 'instrumentName': 'BTC-28JUN19-20000-C', 'created': '2018-10-04 11:14:09 GMT'}
class Instrument(models.Model):
    kind = models.CharField(max_length=10)
    currency = models.CharField(max_length=10)
    pricePrecision = models.IntegerField()
    strike = models.DecimalField(max_digits=10, decimal_places=5)
    optionType = models.CharField(max_length=10)
    isActive = models.BooleanField()
    minTradeSize = models.DecimalField(max_digits=10, decimal_places=5)
    settlement = models.CharField(max_length=10)
    baseCurrency = models.CharField(max_length=10)
    expiration = models.DateTimeField()
    tickSize = models.DecimalField(max_digits=10, decimal_places=5)
    instrumentName = models.CharField(max_length=100)
    created = models.DateTimeField()


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
