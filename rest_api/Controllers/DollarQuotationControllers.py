from rest_api.models import DollarQuotation
from rest_api.serializers import DollarQuotationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_api.filters import DollarQuotationFilter
# Create your views here.

class DollarquotationList(generics.ListAPIView):

    queryset = DollarQuotation.objects.all()
    serializer_class = DollarQuotationSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_class = DollarQuotationFilter
    ordering_fields = ('date',)

class DollarQuotationDetail(generics.RetrieveAPIView):

    queryset = DollarQuotation.objects.all()
    serializer_class = DollarQuotationSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_class = DollarQuotationFilter