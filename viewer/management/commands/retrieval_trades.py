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
    help = 'Retrieve last trades from Deribit for a given instrument'

    def add_arguments(self, parser):

        # Named (optional) arguments
        parser.add_argument(
            '--instrument',
            action='store',
            dest='instrument',
            help='Instrument Id for which retrieve last trades',
        )

    def handle(self, *args, **options):
        logger = get_logger('sftp_client')
        logger.info('-- Starting process --')




        # Generate Deribit client
        client = RestClient(settings.DERIBIT_KEY, settings.DERIBIT_SECRET)

        try:
            if options['instrument']:
                logger.info('Getting last trades for instrument id: ' + str(options['instrument']))
                instrument = Instrument.objects.get(id=options['instrument'])
            else:
                raise Exception("no instrument provided")


            if Trade.objects.filter(instrument=instrument).count()>0:
                logger.info("Last trades already retrieved")
            else:
                # Getting last trades
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

        except Exception as e:
            traceback.print_exc()
            logger.error(e)

        logger.info('-- Ending process --')
