from django_filters import rest_framework as filters
from rest_api.models import BitcoinQuotation

class BitcoinQuotationFilter(filters.FilterSet):

    date_gte = filters.DateTimeFilter(name="date", lookup_expr='gte')
    date_lte = filters.DateTimeFilter(name="date", lookup_expr='lte')

    class Meta:

        model = BitcoinQuotation
        fields = ['date', 'date_gte', 'date_lte']

