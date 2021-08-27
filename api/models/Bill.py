from django.db import models
from api.models.Client import Client

class Bill(models.Model):
  id = models.AutoField(primary_key=True)
  client_id = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
  company_name = models.CharField(max_length=300)
  nit = models.CharField(max_length=11)
  code = models.CharField(max_length=20)
  def __str__(self):
      return f'Bill: {self.code}'