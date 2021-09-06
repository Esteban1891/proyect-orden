from django.db import models
from django.db.models.base import Model
from client.models import  Client
# Create your models here.
class Orden(models.Model):
    OPTIONS = [
        ('solicitada', 'solicitada'),
        ('aprobada', 'aprobada'),
        ('anulada', 'anulada')
    ]
    nmr_orden = models.CharField("numero de orden", max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_time_orden = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices=OPTIONS,max_length = 150, blank=False, null=False)



    def __str__(self) -> str:
        return self.name
