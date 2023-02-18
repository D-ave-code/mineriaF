from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10)
    enfermedad = models.CharField(max_length=50)
    tipo_lesion = models.CharField(max_length=10)
    edad = models.CharField(max_length=10)

class Sintomas(models.Model):
    cedula = models.CharField(max_length=10)
    lesion_id = models.CharField(max_length=2)
    temperatura = models.CharField(max_length=6)
    edad = models.CharField(max_length=2)
    dolor_cabeza = models.CharField(max_length=2)
    conjuntivitis = models.CharField(max_length=2)
    malestar_general = models.CharField(max_length=2)
    ganglios_hinchados = models.CharField(max_length=2)
    tos = models.CharField(max_length=2)
    moqueo = models.CharField(max_length=2)
    dolor_garganta = models.CharField(max_length=2)
    diarrea = models.CharField(max_length=2)
    vomito = models.CharField(max_length=2)
    nauseas = models.CharField(max_length=2)
    infec_oid = models.CharField(max_length=2)
    convulsion = models.CharField(max_length=2)
    comezon = models.CharField(max_length=2)
    perdida_apetito = models.CharField(max_length=2)
    dolor_tragar = models.CharField(max_length=2)
    hinchazon = models.CharField(max_length=2)
    hinchazon_boca = models.CharField(max_length=2)
    dolor_abdominal = models.CharField(max_length=2)
    escalofrio = models.CharField(max_length=2)
    perdida_gusto = models.CharField(max_length=2)
    dolor_dentadura = models.CharField(max_length=2)
    cara = models.CharField(max_length=2)
    torso = models.CharField(max_length=2)
    cabeza = models.CharField(max_length=2)
    extremidades_superiores = models.CharField(max_length=2)
    extremidades_inferiores = models.CharField(max_length=2)
    genitales = models.CharField(max_length=2)
    manos = models.CharField(max_length=2)
    boca = models.CharField(max_length=2)
    pies = models.CharField(max_length=2)
