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

        #call_command('retrieval')

        context = {'instrument_list': Instrument.objects.all()}
        return render(request, 'table_instrument.html', context)

class TableTradeView(View):
    def get(self, request, *args, **kwargs):

        # Getting queryset
        queryset = None
        instrumentName = None
        instrument_id = request.GET.get('instrument')
        if instrument_id:
            queryset = Trade.objects.filter(instrument__id=instrument_id)
            instrumentName = Instrument.objects.get(id=instrument_id).instrumentName
        else:
            queryset = Trade.objects.all()
            instrumentName = 'All'


        context =  {'trade_list': queryset, 'instrumentName': instrumentName}
        return render(request, 'table_trade.html', context)
