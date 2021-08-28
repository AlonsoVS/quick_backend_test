from django.http.response import Http404
from rest_framework.permissions import IsAuthenticated
from api.serializers.BillSerializer import BillSerializer
from api.models.Bill import Bill
from rest_framework import views, status
from rest_framework.response import Response

class BillView(views.APIView):
  permission_classes = (IsAuthenticated,)
  def get_object(self, request, format=None, *args, **kwargs) -> Response:
    id = self.kwargs.get('id')
    try:
      return Bill.objects.get(id=id)
    except Bill.DoesNotExist:
      raise Http404
      
  def get(self, request, format=None) -> Response:
    bills = Bill.objects.all()
    serializer = BillSerializer(bills, many=True)
    return Response(serializer.data)
  
  def post(self, request, format=None) -> Response:
    serializer = BillSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, id, format=None):
    bill = self.get_object(id)
    serializer = BillSerializer(bill, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def delete(self, request, *args, **kwargs):
    id = self.kwargs.get('id')
    bill = self.get_object(id)
    bill.delete()
    return Response(status=status.HTTP_200_OK, data="Bill Deleted")