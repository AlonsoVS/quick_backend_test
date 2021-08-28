from api.serializers.BillSerializer import BillSerializer
from rest_framework import serializers
from api.models.Client import Client

class ClientSerializer(serializers.ModelSerializer):
  bills = BillSerializer(many=True)
  class Meta:
    model = Client
    fields = '__all__'