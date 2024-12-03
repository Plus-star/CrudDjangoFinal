from django.contrib import admin
from .models import ServiciosEsteticos, TratamientoFacial, TratamientoCorporal

# Registra el modelo 'ServiciosEsteticos' para que sea gestionado desde el panel de administración de Django
admin.site.register(ServiciosEsteticos)
admin.site.register(TratamientoCorporal)
admin.site.register(TratamientoFacial)