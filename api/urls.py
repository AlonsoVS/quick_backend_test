from django.urls import include, path
from api.views.ClientView import ClientView
from api.views.ProductView import ProductView
from api.views.BillView import BillView
from api.views.BillProductView import BillProductView

urlpatterns = [
  path('clients/', ClientView.as_view()),
  path('clients/<int:id>', ClientView.as_view()),
  path('bills/', BillView.as_view()),
  path('bills/<int:id>', BillView.as_view()),
  path('products/', ProductView.as_view()),
  path('products/<int:id>', ProductView.as_view()),
  path('bill-products/<int:id>', BillProductView.as_view()),
  path('bill-products/', BillProductView.as_view()),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]