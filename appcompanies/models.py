from django.db import models

# Create your models here.

class Company(models.Model):
    nombre = models.CharField(max_length=100)
    rubro = models.CharField(max_length=20)
    mail = models.EmailField(null= True, blank= True)
    escliente = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nombre}'

    class Meta():
        verbose_name = 'Companies'
        verbose_name_plural = 'companies'
    

class Employee(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    empresa = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre}'

    class Meta():
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

