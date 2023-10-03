from django.db import models

# Create your models here.

class Company(models.Model):
    nombre = models.CharField(max_length=100)
    rubro = models.CharField(max_length=20)
    mail = models.EmailField(null= True, blank= True)
    escliente = models.BooleanField()
    

class Employee(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    empresa = Company()

