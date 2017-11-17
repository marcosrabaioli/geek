from ..models import EuroQuotation
from ..serializers import DollarQuotationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from ..filters import EuroQuotationFilter
# Create your views here.

class EuroQuotationList(generics.ListCreateAPIView):

    queryset = EuroQuotation.objects.all()
    serializer_class = DollarQuotationSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_class = EuroQuotationFilter

class EuroQuotationDetail(generics.RetrieveUpdateAPIView):

    queryset = EuroQuotation.objects.all()
    serializer_class = DollarQuotationSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_class = EuroQuotationFilter