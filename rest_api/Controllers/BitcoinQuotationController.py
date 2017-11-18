from ..models import BitcoinQuotation
from ..serializers import DollarQuotationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from ..filters import BitcoinQuotationFilter
# Create your views here.

class BitcoinQuotationList(generics.ListCreateAPIView):

    queryset = BitcoinQuotation.objects.all()
    serializer_class = DollarQuotationSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_class = BitcoinQuotationFilter

class BitcoinQuotationDetail(generics.RetrieveUpdateAPIView):

    queryset = BitcoinQuotation.objects.all()
    serializer_class = DollarQuotationSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_class = BitcoinQuotationFilter