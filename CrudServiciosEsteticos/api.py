from .models import ServiciosEsteticos
from rest_framework import viewsets, permissions
from .serializers import ServiciosEsteticosSerializer

class ServiciosEsteticosViewSet(viewsets.ModelViewSet):
    queryset = ServiciosEsteticos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ServiciosEsteticosSerializer