# Django imports
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.shortcuts import render
from django.conf import settings
from django.core.management import call_command

# Library Imports
from deribit_api import RestClient

# Project imports
from .models import Instrument, Trade

class IndexView(TemplateView):
    template_name = "index.html"


# class TableView(TemplateView):
#     template_name = "tables.html"

class TableInstrumentView(View):
    def get(self, request):

        """
        # Generate Deribit client
        client = RestClient(settings.DERIBIT_KEY, settings.DERIBIT_SECRET)
        # Get instruments
        instrument_list = client.getinstruments()

        # Create instruments
        # TODO: Make use of bulk_create here
        for instrument in instrument_list:
            try:
                instruments_model = Instrument(**instrument)
                instruments_model.save()

            except Exception as e:
                # TODO: Integrate logger here
                print("Error while saving model")
        """
        #call_command('retrieval')

        context = {'instrument_list': Instrument.objects.all()}
        return render(request, 'table_instrument.html', context)

class TableTradeView(View):
    def get(self, request):

        """
        # Generate Deribit client
        client = RestClient(settings.DERIBIT_KEY, settings.DERIBIT_SECRET)

        print("Getting this thing")
        print(Instrument.objects.first().instrumentName)

        # Get instruments
        instruments = client.getinstruments()
        trade_list = client.getlasttrades(instruments[1]['instrumentName'])

        instruments_model = Instrument(**instruments[1])
        instruments_model.save()

        #trade_list = client.getlasttrades(Instrument.objects.get(id=827).instrumentName)

        print(trade_list)

        # Create instruments
        # TODO: Make use of bulk_create here
        for trade in trade_list:
            try:
                trade_model = Trade(**trade)
                trade_model.instrument = instrument_model
                trade_model.save()
            except Exception as e:
                # TODO: Integrate logger here
                print("Error while saving model")
                print(e)
        """
        context = {'trade_list': Trade.objects.all()}
        return render(request, 'table_trade.html', context)
