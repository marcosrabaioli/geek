from django_filters import rest_framework as filters
from rest_api.models import DollarQuotation

class DollarQuotationFilter(filters.FilterSet):

    date_gte = filters.DateTimeFilter(name="date", lookup_expr='gte')
    date_lte = filters.DateTimeFilter(name="date", lookup_expr='lte')

    class Meta:
        model = DollarQuotation
        fields = ['date', 'date_gte', 'date_lte']
