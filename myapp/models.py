from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10)
    enfermedad = models.CharField(max_length=50)
    tipo_lesion = models.CharField(max_length=10)
