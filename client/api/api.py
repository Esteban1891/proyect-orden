from rest_framework import viewsets
from client.models import  Client
from client.api.serializers import ClientSerializer 



class ClientAPIViewsets(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


    