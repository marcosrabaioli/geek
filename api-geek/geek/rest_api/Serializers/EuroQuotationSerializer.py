from rest_framework import serializers
from ..models import BitcoinQuotation

class BitcoinQuotationSerializer(serializers.ModelSerializer):

    class Meta:

        model = BitcoinQuotation
        fields = '__all__'