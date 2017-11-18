from django_filters import rest_framework as filters
from ..models import BitcoinQuotation

class BitcoinQuotationFilter(filters.FilterSet):

    class Meta:

        model = BitcoinQuotation
        fields = ['date']