from django_filters import rest_framework as filters
from ..models import DollarQuotation

class DollarQuotationFilter(filters.FilterSet):

    class Meta:

        model = DollarQuotation
        fields = ['date']