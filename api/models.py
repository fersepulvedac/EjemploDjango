from django.db import models

# Create your models here.
class Suscripcion(models.Model):
    user = models.CharField(max_length=100, unique=True)
    suscrito = models.BooleanField(default=False)