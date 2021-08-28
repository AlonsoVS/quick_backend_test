from api.serializers.ClientSerializer import ClientSerializer
from api.models.Client import Client
from rest_framework import views, status
from rest_framework.response import Response
from django.http import Http404
from rest_framework.parsers import JSONParser 


class ClientView(views.APIView):
  def get_object(self, request, format=None, *args, **kwargs) -> Response:
    id = self.kwargs.get('id')
    try:
      return Client.objects.get(id=id)
    except Client.DoesNotExist:
      raise Http404

  def get(self, request, format=None) -> Response:
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)
  
  def post(self, request, format=None) -> Response:
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def put(self, request, id, format=None):
    client = self.get_object(id)
    serializer = ClientSerializer(client, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, *args, **kwargs):
    id = self.kwargs.get('id')
    client = self.get_object(id)
    client.delete()
    return Response(status=status.HTTP_200_OK, data="Client Deleted")