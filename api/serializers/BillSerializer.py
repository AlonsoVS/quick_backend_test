from api.serializers.BillProductSerializer import BillProductSerializer
from rest_framework import serializers
from api.models.Bill import Bill

class BillSerializer(serializers.ModelSerializer):
  bill_products = BillProductSerializer(many=True)
  class Meta:
    model = Bill
    fields = '__all__'