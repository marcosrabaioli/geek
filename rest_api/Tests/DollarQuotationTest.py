from rest_api.models import DollarQuotation
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase

from django.utils import timezone


class DollarQuotationAPITestCase(APITestCase):

    def test_list_dollar_quotations(self):

        data = {'date': timezone.now(), 'buy': 1.1, 'sell': 1.05, 'variation': 0.003}

        dollar = DollarQuotation(**data)
        dollar.save()

        url = reverse('dollar-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['date'], str(data['date'].isoformat()).replace('+00:00', 'Z'))
        self.assertEqual(response.data[0]['buy'], data['buy'])
        self.assertEqual(response.data[0]['sell'], data['sell'])
        self.assertEqual(response.data[0]['variation'], data['variation'])

    def test_retrive_dollar_quotation(self):
        data = {'date': timezone.now(), 'buy': 1.1, 'sell': 1.05, 'variation': 0.003}

        dollar = DollarQuotation(**data)
        dollar.save()

        url = reverse('dollar-detail', kwargs={'pk':str(dollar.id)})
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['date'], str(data['date'].isoformat()).replace('+00:00', 'Z'))
        self.assertEqual(response.data['buy'], data['buy'])
        self.assertEqual(response.data['sell'], data['sell'])
        self.assertEqual(response.data['variation'], data['variation'])
