from rest_framework import serializers
from api.models.Bill import Bill

class BillSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bill
    fields = '__all__'