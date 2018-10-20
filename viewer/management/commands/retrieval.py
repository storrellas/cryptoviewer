# Python imports
import os
import time
from deribit_api import RestClient

# Django imports
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

# Project imports
from cryptoviewer.utils import get_logger

# Project imports
from viewer.models import Instrument, Trade


class Command(BaseCommand):
    help = 'Generate invoice for a given portfolio'

    def handle(self, *args, **options):
        logger = get_logger('sftp_client')
        logger.info('-- Starting process --')

        # Generate Deribit client
        client = RestClient(settings.DERIBIT_KEY, settings.DERIBIT_SECRET)
        # Get instruments
        instrument_list = client.getinstruments()


        try:
            logger.info("Deleting all Instrument objects")
            Instrument.objects.all().delete()
            instrument_model_list = []
            for instrument in instrument_list:
                instrument_model = Instrument(**instrument)
                instrument_model_list.append(instrument_model)



            Instrument.objects.bulk_create(instrument_model_list)
            logger.info("Inserted " + str(len(instrument_model_list)) + " Instrument objects")
        except Exception as e:
            logger.error(e)

        logger.info('-- Ending process --')
