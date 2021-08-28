from api.serializers.BillProductSerializer import BillProductSerializer
from api.models.BillProduct import BillProduct
from rest_framework import views, status
from rest_framework.response import Response
from django.http.response import Http404

class BillProductView(views.APIView):
  def get_object(self, request, format=None, *args, **kwargs) -> Response:
    id = self.kwargs.get('id')
    try:
      return BillProduct.objects.get(id=id)
    except BillProduct.DoesNotExist:
      raise Http404

  def get(self, request, format=None) -> Response:
    bill_products = BillProduct.objects.all()
    serializer = BillProductSerializer(bill_products, many=True)
    return Response(serializer.data)
  
  def post(self, request, format=None) -> Response:
    serializer = BillProductSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def put(self, request, id, format=None):
    bill_product = self.get_object(id)
    serializer = BillProductSerializer(bill_product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, *args, **kwargs):
    id = self.kwargs.get('id')
    bill_product = self.get_object(id)
    bill_product.delete()
    return Response(status=status.HTTP_200_OK, data="Bill Product Deleted")