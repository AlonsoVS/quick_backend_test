from django.db import models
from api.models.Bill import Bill
from api.models.Product import Product

class BillProduct(models.Model):
  id = models.AutoField(primary_key=True)
  bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
  product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
  def __str__(self):
    return f'BillProduct: {self.id}, Bill={self.bill_id}, Product={self.product_id}'