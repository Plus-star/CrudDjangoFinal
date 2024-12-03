from rest_framework import serializers
from .models import ServiciosEsteticos
from .models import TratamientoFacial
from .models import TratamientoCorporal

class ServiciosEsteticosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiciosEsteticos
        fields = ('id', '_nombre_servicio', '_descripcion', '_duracion', '_precio')
        
class TratamientoCorporalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TratamientoCorporal
        fields = ('serviciosesteticos_ptr', '_zona_tratada', '_tipo_producto')
        
class TratamientoFacialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TratamientoFacial
        fields = ('serviciosesteticos_ptr', '_tipo_tratamiento', '_tipo_piel')
        