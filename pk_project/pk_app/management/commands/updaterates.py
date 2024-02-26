from django.core.management.base import BaseCommand
from pk_app.models import Currency
import requests
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Updates currency table data'

    def handle(self, *args, **kwargs):
        response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        soup = BeautifulSoup(response.content, features="xml")

        for valute in soup.find_all('Valute'):
            name = valute.find('CharCode').text
            rate = float(valute.find('Value').text.replace(',', '.'))

            try:
                currency = Currency.objects.get(name=name)
                currency.rate = rate
            except Currency.DoesNotExist:
                currency = Currency(name=name, rate=rate)
            currency.save()

        self.stdout.write('Currency rates updated.')
