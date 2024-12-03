from django.db import models


# Modelo que representa un servicio estético
class ServiciosEsteticos(models.Model):
    _nombre_servicio = models.CharField(max_length=100, default='1', verbose_name="Nombre del Servicio")
    _descripcion = models.CharField(max_length=100, default='1', verbose_name="Descripción")
    _duracion = models.CharField(max_length=50, default='1', verbose_name="Duración")
    _precio = models.IntegerField() 

    @property
    def nombre_servicio(self):
        return self._nombre_servicio

    @nombre_servicio.setter
    def nombre_servicio(self, value):
        self._nombre_servicio = value

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, value):
        self._duracion = value

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        self._precio = value

    # Representación del objeto como cadena (para que se muestre en la interfaz de Django)
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self._nombre_servicio, self._descripcion)

class TratamientoFacial(ServiciosEsteticos):
    _tipo_tratamiento = models.CharField(max_length=100, verbose_name="Tipo de Tratamiento")
    _tipo_piel = models.CharField(max_length=100, verbose_name="Tipo de Piel")

    @property
    def tipo_tratamiento(self):
        return self._tipo_tratamiento

    @tipo_tratamiento.setter
    def tipo_tratamiento(self, value):
        self._tipo_tratamiento = value

    @property
    def tipo_piel(self):
        return self._tipo_piel


    @tipo_piel.setter
    def tipo_piel(self, value):
        self._tipo_piel = value
    
    def calcular_precio_final(self, descuento):
        precio_base = float(self._precio)
        precio_final = precio_base - (precio_base * descuento / 100)
        return round(precio_final, 2)
class TratamientoCorporal(ServiciosEsteticos):
    _zona_tratada = models.CharField(max_length=100, verbose_name="Zona Tratada")
    _tipo_producto = models.CharField(max_length=100, verbose_name="Tipo de Producto")

    @property
    def zona_tratada(self):
        return self._zona_tratada

    @zona_tratada.setter
    def zona_tratada(self, value):
        self._zona_tratada = value

    @property
    def tipo_producto(self):
        return self._tipo_producto

    @tipo_producto.setter
    def tipo_producto(self, value):
        self._tipo_producto = value
        
    def calcular_precio_final(self, descuento):
        precio_base = float(self._precio)
        precio_final = precio_base - (precio_base * descuento / 100)
        return round(precio_final, 2)
    
