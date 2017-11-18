from rest_api.models import BitcoinQuotation
from rest_api.serializers import DollarQuotationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_api.filters import BitcoinQuotationFilter
# Create your views here.

class BitcoinQuotationList(generics.ListAPIView):

    queryset = BitcoinQuotation.objects.all()
    serializer_class = DollarQuotationSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_class = BitcoinQuotationFilter
    ordering_fields = ('date',)

class BitcoinQuotationDetail(generics.RetrieveAPIView):

    queryset = BitcoinQuotation.objects.all()
    serializer_class = DollarQuotationSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_class = BitcoinQuotationFilter