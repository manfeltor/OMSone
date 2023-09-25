from django.db import models

# Create your models here.

class Commpany(models.Model):
    nombre = models.CharField(max_length=100)
    rubro = models.CharField(max_length=20)
    mail = models.EmailField(null= True, blank= True)
    cliente = models.BooleanField()

