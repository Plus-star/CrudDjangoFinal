from .models import ServiciosEsteticos
from .models import TratamientoFacial
from .models import TratamientoCorporal

from rest_framework import viewsets, permissions
from .serializers import ServiciosEsteticosSerializer
from .serializers import TratamientoFacialSerializer
from .serializers import TratamientoCorporalSerializer

class ServiciosEsteticosViewSet(viewsets.ModelViewSet):
    queryset = ServiciosEsteticos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ServiciosEsteticosSerializer
    
class TratamientoFacialViewSet(viewsets.ModelViewSet):
    queryset = TratamientoFacial.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TratamientoFacialSerializer
    
class TratamientoCorporalViewSet(viewsets.ModelViewSet):
    queryset = TratamientoCorporal.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TratamientoCorporalSerializer