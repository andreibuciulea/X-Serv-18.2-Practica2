from django.db import models

# Create your models here.
class datos(models.Model):
    acortada = models.CharField(max_length=32)
    url= models.CharField(max_length=32)
