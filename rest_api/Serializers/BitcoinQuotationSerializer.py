from rest_framework import serializers
from rest_api.models import BitcoinQuotation

class DollarQuotationSerializer(serializers.ModelSerializer):

    class Meta:

        model = BitcoinQuotation
        fields = '__all__'