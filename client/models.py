from django.db import models
from django.db.models.base import Model

# Create your models here.
class Client(models.Model):
    name = models.CharField("nombre", max_length=50)
    address = models.CharField("direccion", max_length=50)
    cell = models.CharField("telefono", max_length=50)
    nationality = models.CharField("nacionalidad", max_length=50)
    email = models.EmailField("correo", max_length=254)


    def __str__(self) -> str:
        return self.name
