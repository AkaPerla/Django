from django.db import models

class Socios(models.Model):
  nombre = models.CharField(max_length=255)
  apellidos = models.CharField(max_length=255) #Lo mismo que VARCHAR(255)