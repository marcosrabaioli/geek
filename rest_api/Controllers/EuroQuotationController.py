from rest_api.models import EuroQuotation
from rest_api.serializers import DollarQuotationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_api.filters import EuroQuotationFilter
# Create your views here.

class EuroQuotationList(generics.ListAPIView):

    queryset = EuroQuotation.objects.all()
    serializer_class = DollarQuotationSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_class = EuroQuotationFilter
    ordering_fields = ('date',)

class EuroQuotationDetail(generics.RetrieveAPIView):

    queryset = EuroQuotation.objects.all()
    serializer_class = DollarQuotationSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_class = EuroQuotationFilter