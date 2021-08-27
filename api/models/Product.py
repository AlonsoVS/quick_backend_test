from django.db import models

class Product(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200)
  description= models.TextField()
  def __str__(self):
    return f'Product: {self.name}'