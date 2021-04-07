from django.db import models

# Create your models here.
class Asignatura(models.Model):
    nombre = models.CharField(max_length=200)
    seccion = models.CharField(max_length=10)
    docente_id = models.IntegerField()
    
