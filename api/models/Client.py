from django.db import models

class Client(models.Model): 
  id = models.AutoField(primary_key=True)
  first_name = models.CharField (max_length = 100) 
  last_name = models.CharField (max_length = 100) 
  email = models.CharField(max_length = 250)
  def __str__(self):
      return f'Client: {self.first_name} {self.last_name}'