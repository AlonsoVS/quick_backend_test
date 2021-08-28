from django.contrib import admin
from api.models.Client import Client
from api.models.Bill import Bill
from api.models.Product import Product
from api.models.BillProduct import BillProduct

admin.site.register(Client)
admin.site.register(Bill)
admin.site.register(Product)
admin.site.register(BillProduct)