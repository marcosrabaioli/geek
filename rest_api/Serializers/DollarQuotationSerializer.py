from rest_framework import serializers
from ..models import DollarQuotation

class DollarQuotationSerializer(serializers.ModelSerializer):

    class Meta:

        model = DollarQuotation
        fields = '__all__'