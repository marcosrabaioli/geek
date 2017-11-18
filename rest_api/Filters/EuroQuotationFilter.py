from django_filters import rest_framework as filters
from ..models import EuroQuotation

class EuroQuotationFilter(filters.FilterSet):

    class Meta:

        model = EuroQuotation
        fields = ['date']