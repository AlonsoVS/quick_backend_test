from rest_framework.permissions import IsAuthenticated
from api.serializers.ProductSerializer import ProductSerializer
from api.models.Product import Product
from rest_framework import views, status
from rest_framework.response import Response
from django.http.response import Http404

class ProductView(views.APIView):
  permission_classes = (IsAuthenticated,)
  def get_object(self, request, format=None, *args, **kwargs) -> Response:
    id = self.kwargs.get('id')
    try:
      return Product.objects.get(id=id)
    except Product.DoesNotExist:
      raise Http404

  def get(self, request, format=None) -> Response:
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
  
  def post(self, request, format=None) -> Response:
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def put(self, request, id, format=None):
    product = self.get_object(id)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, *args, **kwargs):
    id = self.kwargs.get('id')
    product = self.get_object(id)
    product.delete()
    return Response(status=status.HTTP_200_OK, data="Product Deleted")