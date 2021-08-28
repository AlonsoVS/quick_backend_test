from rest_framework import serializers
from api.models.BillProduct import BillProduct

class BillProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = BillProduct
    fields = '__all__'