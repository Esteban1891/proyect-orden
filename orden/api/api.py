from rest_framework import viewsets
from orden.models import  Orden
from orden.api.serializers import OrdenSerializer 



class OrdenAPIViewsets(viewsets.ModelViewSet):
    serializer_class = OrdenSerializer
    queryset = Orden.objects.all()

