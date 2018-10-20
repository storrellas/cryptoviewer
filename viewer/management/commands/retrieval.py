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

        # Create instruments
        # TODO: Make use of bulk_create here
        for instrument in instrument_list:
            try:
                instruments_model = Instrument(**instrument)
                instruments_model.save()

            except Exception as e:
                # TODO: Integrate logger here
                print("Error while saving model")
                logger.error(e)

        logger.info('-- Ending process --')
