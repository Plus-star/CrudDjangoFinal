from django.shortcuts import render, redirect
from .models import ServiciosEsteticos, TratamientoFacial, TratamientoCorporal
from django.contrib import messages

# Vista principal que lista todos los servicios estéticos faciales
def home(request):
    ListadoServiciosFacial = TratamientoFacial.objects.all()
    ListadoServiciosCoporales = TratamientoCorporal.objects.all()

    #calcular precios finales para todos los servicios
    precios_finales_facial = {servicio.calcular_precio_final(50) for servicio in ListadoServiciosFacial}
    precios_finales_corporal = {servicio.calcular_precio_final(40) for servicio in ListadoServiciosCoporales}
    messages.success(request, 'Servicios listados')
    messages.success(request, 'Servicios faciales listados')
    return render(request, "gestionServicios.html", {"ServiciosFacial": ListadoServiciosFacial,
                                                     "ServiciosCoporales": ListadoServiciosCoporales,
                                                     "PreciosFinalesFaciales": precios_finales_facial,
                                                     "PreciosFinalesCorporales": precios_finales_corporal})
   
   
# Vista principal que lista todos los servicios estéticos corporales

# Vista para registrar un nuevo tratamiento facial
def RegistrarFacial(request):
    if request.method == "POST":
        NombreServicio = request.POST['txtnombreservicioFacial']
        Descripcion = request.POST['txtdescripcionFacial']
        Duracion = request.POST['txtduracionFacial']
        Precio = request.POST['txtprecioFacial']
        TipoTratamiento = request.POST['txtTipoTratamiento'] 
        TipoPiel = request.POST['txtTipoPiel']
        
        # Crea un nuevo registro en la base de datos
        registro = TratamientoFacial.objects.create(
            _nombre_servicio=NombreServicio,
            _descripcion=Descripcion,
            _duracion=Duracion,
            _precio=Precio,
            _tipo_tratamiento=TipoTratamiento,
            _tipo_piel=TipoPiel
        )
        #Calcular el precio final, polimorfismo
        precio_final = registro.calcular_precio_final(50)
        messages.success(request, f'Servicio facial registrado. Precio final: {precio_final}')
        return redirect('/')
    
    

# Vista para mostrar los datos de un servicio facial específico en la página de edición
def EdicionRegistroFacial(request, id):
    registro = TratamientoFacial.objects.get(id=id)
    return render(request, "EdicionRegistroFacial.html", {"registro": registro})

# Vista para editar un servicio facial existente
def EditarRegistroFacial(request,id):
    if request.method == "POST":
        NombreServicio = request.POST['nombreServicioFacial']
        Descripcion = request.POST['txtdescripcionFacial']
        Duracion = request.POST['txtduracionFacial']
        Precio = request.POST['txtprecioFacial']
        TipoTratamiento = request.POST['txtTipoTratamiento']
        TipoPiel = request.POST['txtTipoPiel']
        
        registro = TratamientoFacial.objects.get(id=id)
        registro.nombre_servicio= NombreServicio
        registro.descripcion = Descripcion
        registro._duracion = Duracion
        registro._precio = Precio
        registro._tipo_tratamiento = TipoTratamiento
        registro._tipo_piel = TipoPiel
        registro.save()
        #funcion para calcular precio final, polimorfismo
        precio_final = registro.calcular_precio_final(50)
        messages.success(request, 'Servicio facial editado')
        return redirect('/')

# Vista para eliminar un servicio facial
def EliminarRegistroFacial(request, id):
    registro = TratamientoFacial.objects.get(id=id)
    registro.delete()
    messages.success(request, 'Servicio facial eliminado')
    return redirect('/')

# Vista para registrar un nuevo tratamiento corporal
def RegistrarCorporal(request):
    if request.method == "POST":
        NombreServicio = request.POST['txtnombreservicioCorporal']
        Descripcion = request.POST['txtdescripcionCorporal']
        Duracion = request.POST['txtduracionCorporal']
        Precio = request.POST['txtprecioCorporal']
        ZonaTratada = request.POST['txtZonaTratada']
        TipoProducto = request.POST['txtTipoProducto']
        
        # Crea un nuevo registro en la base de datos
        registro = TratamientoCorporal.objects.create(
            _nombre_servicio=NombreServicio,
            _descripcion=Descripcion,
            _duracion=Duracion,
            _precio=Precio,
            _zona_tratada=ZonaTratada,
            _tipo_producto=TipoProducto
        )
        #Calcular el precio final, polimorfismo
        precio_final = registro.calcular_precio_final(40)
        messages.success(request, f'Servicio corporal registrado. Precio final {precio_final}')
        return redirect('/')

# Vista para mostrar los datos de un servicio corporal específico en la página de edición
def EdicionRegistroCorporal(request, id):
    registro = TratamientoCorporal.objects.get(id=id)
    return render(request, "EdicionRegistroCoporal.html", {"registro": registro})

# Vista para editar un servicio corporal existente
# Vista para editar un servicio corporal existente
def EditarRegistroCorporal(request, id):
    if request.method == "POST":
        NombreServicio = request.POST['txtnombreservicioCorporal']
        Descripcion = request.POST['txtdescripcionCorporal']
        Duracion = request.POST['txtduracionCorporal']
        Precio = request.POST['txtprecioCorporal']
        ZonaTratada = request.POST['txtZonaTratada']
        TipoProducto = request.POST['txtTipoProducto']
        
        registro = TratamientoCorporal.objects.get(id=id)
        registro._nombre_servicio = NombreServicio
        registro._descripcion = Descripcion
        registro._duracion = Duracion
        registro._precio = Precio
        registro._zona_tratada = ZonaTratada
        registro._tipo_producto = TipoProducto
        registro.save()
        #calcular el precio final, polimorfismo
        precio_final = registro.calcular_precio_final(40)
        messages.success(request, f'Servicio corporal editado. Precio final: {precio_final}')
        return redirect('/')

# Vista para redirigir a la misma página
def redirigir(request):
    return redirect('gestionServicios.html')

# Vista para eliminar un servicio corporal
def EliminarRegistroCorporal(request, id):
    registro = TratamientoCorporal.objects.get(id=id)
    registro.delete()
    
    messages.success(request, 'Servicio corporal eliminado')
    return redirect('/')