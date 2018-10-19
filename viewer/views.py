# Django imports
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.shortcuts import render
from django.conf import settings

# Library Imports
from deribit_api import RestClient

# Project imports
from .models import Instrument

class IndexView(TemplateView):
    template_name = "index.html"


# class TableView(TemplateView):
#     template_name = "tables.html"

class TableView(View):
    def get(self, request):

        print(settings.DERIBIT_KEY)
        print(settings.DERIBIT_SECRET)

        # Generate Deribit client
        client = RestClient(settings.DERIBIT_KEY, settings.DERIBIT_SECRET)
        # Get instruments
        instruments = client.getinstruments()

        # Create instruments
        # TODO: Make use of bulk_create here
        for instrument in instruments:
            try:
                instruments_model = Instrument(**instrument)
                instruments_model.save()
            except:
                # TODO: Integrate logger here
                print("Error while saving model")

        context = {'instument_list': Instrument.objects.all()}
        return render(request, 'tables.html', context)
