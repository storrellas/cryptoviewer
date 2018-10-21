# Python imports
import os
import time
import traceback
import sys

# Django imports
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

sys.path.append(settings.BASE_DIR + '/lib/')

# Project imports
from cryptoviewer.utils import get_logger
from viewer.models import Instrument, Trade
from deribit_api_cryptoviewer import RestClient


class Command(BaseCommand):
    help = 'Retrieve instruments from Deribit'

    def handle(self, *args, **options):
        logger = get_logger('sftp_client')
        logger.info('-- Starting process --')

        print(settings.BASE_DIR)

        try:
            # Generate Deribit client
            client = RestClient(settings.DERIBIT_KEY, settings.DERIBIT_SECRET)
            # Get instruments
            instrument_list = client.getinstruments()

            # Delete instances
            logger.info("Deleting all Instrument objects")
            Instrument.objects.all().delete()
            Trade.objects.all().delete()

            # Iterate instruments
            instrument_model_list = []
            for instrument in instrument_list:
                instrument_model = Instrument(**instrument)
                instrument_model_list.append(instrument_model)
            if len(instrument_model_list) > 0:
                Instrument.objects.bulk_create(instrument_model_list)
            logger.info("Inserted " + str(len(instrument_model_list)) + " Instrument objects")

            """
            # Get Last trades
            for instrument in Instrument.objects.all():

                trade_model_list = []
                trade_list = client.getlasttrades(instrument.instrumentName)
                for trade in trade_list:
                    del trade['instrument']
                    trade_model = Trade(**trade)
                    trade_model.instrument = instrument
                    #trade_model.save()
                    trade_model_list.append(trade_model)
                if len(trade_model_list) > 0:
                    Trade.objects.bulk_create(trade_model_list)
                logger.info("Inserted " + str(len(trade_model_list)) +
                                " Trade objects for InstrumentName " + instrument.instrumentName)

            logger.info("Inserted " + str(Trade.objects.all().count()) + " Trades" )
            """
        except Exception as e:
            traceback.print_exc()
            logger.error(e)

        logger.info('-- Ending process --')
