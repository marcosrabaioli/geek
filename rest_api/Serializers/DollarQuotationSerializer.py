from rest_framework import serializers
from rest_api.models import DollarQuotation

class DollarQuotationSerializer(serializers.ModelSerializer):

    class Meta:

        model = DollarQuotation
        fields = '__all__'