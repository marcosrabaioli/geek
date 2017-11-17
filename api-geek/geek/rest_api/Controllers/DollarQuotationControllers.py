from ..models import DollarQuotation
from ..serializers import DollarQuotationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from ..filters import DollarQuotationFilter
# Create your views here.

class DollarquotationList(generics.ListCreateAPIView):

    queryset = DollarQuotation.objects.all()
    serializer_class = DollarQuotationSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_class = DollarQuotationFilter

class DollarQuotationDetail(generics.RetrieveUpdateAPIView):

    queryset = DollarQuotation.objects.all()
    serializer_class = DollarQuotationSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_class = DollarQuotationFilter