from api.views.RegisterView import RegisterView
from django.urls import include, path
from api.views.ClientView import ClientView
from api.views.ProductView import ProductView
from api.views.BillView import BillView
from api.views.BillProductView import BillProductView
from api.serializers.JWTSerializer import JWTSerializer
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
  path('register/', RegisterView.as_view(), name='register'),
  path('token/', jwt_views.TokenObtainPairView.as_view(serializer_class=JWTSerializer), name='token_obtain_pair'),
  path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
  path('clients/', ClientView.as_view(), name='clients'),
  path('clients/<int:id>', ClientView.as_view()),
  path('bills/', BillView.as_view()),
  path('bills/<int:id>', BillView.as_view()),
  path('products/', ProductView.as_view()),
  path('products/<int:id>', ProductView.as_view()),
  path('bill-products/<int:id>', BillProductView.as_view()),
  path('bill-products/', BillProductView.as_view()),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]