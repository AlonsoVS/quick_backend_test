from rest_framework import serializers
from api.models.Client import Client

class ClientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Client
    fields = ('id', 'first_name', 'last_name')