from django.core.management.base import BaseCommand
import datetime
from django.conf import settings
import requests
from rest_api.models import DollarQuotation, EuroQuotation, BitcoinQuotation


class Command(BaseCommand):
    help = 'Run get quotations.'

    def handle(self, *args, **options):
        r = requests.get('https://api.hgbrasil.com/finance/quotations?format=json&key=8a635952')
        if r.status_code == 200:

            data = r.json()

            dollar = DollarQuotation(date = datetime.datetime.now(),
                                     buy = data['results']['currencies']['USD']['buy'],
                                     sell = data['results']['currencies']['USD']['sell'],
                                     variation = data['results']['currencies']['USD']['variation'])

            dollar.save()

            euro = EuroQuotation(date=datetime.datetime.now(),
                                     buy=data['results']['currencies']['EUR']['buy'],
                                     sell=data['results']['currencies']['EUR']['sell'],
                                     variation=data['results']['currencies']['EUR']['variation'])

            euro.save()

            bitcoin = BitcoinQuotation(date=datetime.datetime.now(),
                                     buy=data['results']['currencies']['BTC']['buy'],
                                     sell=data['results']['currencies']['BTC']['sell'],
                                     variation=data['results']['currencies']['BTC']['variation'])

            bitcoin.save()