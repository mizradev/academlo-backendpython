from django.db import models

# Create your models here.
class Maestro(models.Model):
    persona_id = models.IntegerField()