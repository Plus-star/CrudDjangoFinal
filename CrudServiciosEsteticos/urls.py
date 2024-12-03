from django.urls import path
from rest_framework import routers
from .api import ServiciosEsteticosViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'api/CrudServiciosEsteticos', ServiciosEsteticosViewSet, basename='serviciosesteticos')

urlpatterns = [
    *router.urls,
    
    path('', views.home),
    path('EliminarRegistroFacial/<int:id>', views.EliminarRegistroFacial),
    path('EdicionRegistroFacial/<int:id>', views.EdicionRegistroFacial, name='edicion_registro_facial'),
    path('redirigir', views.redirigir),
    path('EditarRegistroCorporal/<int:id>', views.EditarRegistroCorporal, name='editar_registro_corporal'),
    path('RegistrarCorporal/', views.RegistrarCorporal, name='registrar_corporal'),
    path('EliminarRegistroCorporal/<int:id>', views.EliminarRegistroCorporal),
    path('EdicionRegistroCorporal/<int:id>', views.EdicionRegistroCorporal, name='edicion_registro_corporal'),
    path('RegistrarFacial/', views.RegistrarFacial, name='registrar_facial'),
    path('EditarRegistroFacial/<int:id>', views.EditarRegistroFacial, name='editar_registro_facial'),
]
