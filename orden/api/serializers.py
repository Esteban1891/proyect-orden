from rest_framework import serializers
from orden.models import Orden
    
class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Orden
        fields = '__all__'
        
    