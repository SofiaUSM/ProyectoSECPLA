from datetime import datetime
from time import strptime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from .models import *
from django.utils.timezone import make_aware

# Create your views here.
def menu(request):
    users = User.objects.all()

    iniciativa = Iniciativa.objects.all()
    data = {
        'users':users,
        'iniciativa':iniciativa,
    }
    if request.method == "POST":
        
        nombre_proyecto = request.POST.get('nombre_proyecto')
        numero_ingreso = request.POST.get('numero')
        profesional_id = request.POST.get('profesional')  # ID del profesional encargado
        usuarios_asignados = request.POST.getlist('usuarios')  # Lista de IDs de profesionales de apoyo

        print(profesional_id)
        print(usuarios_asignados)
        # Crear la nueva iniciativa
        profesional = User.objects.filter(id=profesional_id).first()  # Obtener el profesional encargado
        nueva_iniciativa = Iniciativa.objects.create(
            nombre_proyecto=nombre_proyecto,
            numero_ingreso=numero_ingreso,
            profesional=profesional
        )

        # Crear asignaciones para profesionales de apoyo
        for user_id in usuarios_asignados:
            user = User.objects.filter(id=user_id).first()
            if user:
                ini_user.objects.create(
                    categoría='I',  # Puedes ajustar este valor según la lógica de tu aplicación
                    id_iniciativa=nueva_iniciativa,
                    id_user=user
                )
        nueva_iniciativa.save()

        return redirect('actualizar', id=nueva_iniciativa.id)
 
    return render(request,'Form_Home.html',data)

def menu_1(request):
    users = User.objects.all()

    iniciativa = Iniciativa.objects.all()
    data = {
        'users':users,
        'iniciativa':iniciativa,
    }
    if request.method == "POST":
        
        nombre_proyecto = request.POST.get('nombre_proyecto')
        numero_ingreso = request.POST.get('numero')
        profesional_id = request.POST.get('profesional')  # ID del profesional encargado
        usuarios_asignados = request.POST.getlist('usuarios')  # Lista de IDs de profesionales de apoyo

        print(profesional_id)
        print(usuarios_asignados)
        # Crear la nueva iniciativa
        profesional = User.objects.filter(id=profesional_id).first()  # Obtener el profesional encargado
        nueva_iniciativa = Iniciativa.objects.create(
            nombre_proyecto=nombre_proyecto,
            numero_ingreso=numero_ingreso,
            profesional=profesional
        )

        # Crear asignaciones para profesionales de apoyo
        for user_id in usuarios_asignados:
            user = User.objects.filter(id=user_id).first()
            if user:
                ini_user.objects.create(
                    categoría='I',  # Puedes ajustar este valor según la lógica de tu aplicación
                    id_iniciativa=nueva_iniciativa,
                    id_user=user
                )
        nueva_iniciativa.save()

        return redirect('actualizar', id=nueva_iniciativa.id)
 
    return render(request,'Form_Home_correcion.html',data)

def formulario(request):
    if request.method == "POST":

        nombre_proyecto = request.POST['nombre_proyecto']
        numero = request.POST['numero']
        
        visita_archivo = request.FILES.get('visita_archivo', None)
        visita_des = request.POST.get('visita_des', '')
        visita = entregado(visita_archivo)

        terreno_archivo = request.FILES.get('terreno_archivo', None)
        terreno_des = request.POST.get('terreno_des', '')
        terreno = entregado(terreno_archivo)


        au_archivo = request.FILES.get('au_archivo', None)
        solicitud_au = entregado(au_archivo)

        fac_archivo = request.FILES.get('fac_archivo', None)
        factibilidad = entregado(fac_archivo)


        iniciativa = Iniciativa.objects.create(
            nombre_proyecto=nombre_proyecto, 
            numero_ingreso=numero,
        )

        iniciativa.visita_adjunto = visita_archivo
        iniciativa.visita =visita
        iniciativa.detalle_visita = visita_des

        iniciativa.terreno_adjunto = terreno_archivo
        iniciativa.terreno =terreno
        iniciativa.detalle_terreno = terreno_des

        iniciativa.solicitud_au_adjunto = au_archivo
        iniciativa.solicitud_au =solicitud_au

        iniciativa.factibilidad_adjunto = fac_archivo
        iniciativa.factibilidad =factibilidad

        iniciativa.save()
        return redirect('menu')

    return render(request,'Formulario.html',)

def bnup(request):
    usuarios = Funcionario.objects.all()
    funcionario = ""
    # Definir las opciones de Unidad Técnica
    UNI_TEC ={
        ('Asesoría Urbana','AU'),
        ('Direcciones de Obras Municipales','DOM'),
    }
    bnup = bnup_ingreso.objects.all()
    data = {
        "usuarios":usuarios,
        "Unidad_técnica": UNI_TEC,
        "bnups":bnup,
    }
    if request.method == "POST":

        print(request.POST)

        codigo = request.POST['codigo']
        constituye = limpiar_texto(request.POST.get('constituye', ''))
        constituye_otro = limpiar_texto(request.POST.get('Constituye_otro', ''))
        ref = limpiar_texto(request.POST.get('ref', ''))
        mat = limpiar_texto(request.POST.get('mat', ''))
        Calle = limpiar_texto(request.POST.get('Calle', ''))
        n_de_ingreso = limpiar_texto(request.POST.get('n_de_ingreso', ''))
        funcionarioSecpla = limpiar_texto(request.POST.get('funcionarioSecpla', ''))
        unidadTecnica = limpiar_texto(request.POST.get('unidadTecnica', ''))
        fechaIngreso = limpiar_texto(request.POST.get('fechaIngreso', ''))
        archivo_adjunto = request.FILES.get('adjuntarArchivo', None)

        nuevo_funcionario_nombre = limpiar_texto(request.POST.get('newFuncionario', ''))

            # Obtener o crear el Funcionario
        if 'newFuncionario' in request.POST and request.POST['newFuncionario'].strip():
            nuevo_funcionario_nombre = limpiar_texto(request.POST['newFuncionario'].strip())

                # Verificar si el funcionario ya existe con ese nombre
            funcionario_existente = Funcionario.objects.filter(nombre__iexact=nuevo_funcionario_nombre).first()
                
            if funcionario_existente:
                funcionario = funcionario_existente  # Usar el funcionario existente
            else:       # Si no existe, crear uno nuevo
                funcionario = Funcionario.objects.create(nombre=nuevo_funcionario_nombre)
        else:
            funcionario = Funcionario.objects.filter(pk=funcionarioSecpla.strip()).first()

        if not funcionario:
            # Si no se encuentra el funcionario
            data["error"] = "Funcionario no válido o no seleccionado"
            return render(request, 'Bnup.html', data)

    # Crear la instancia de bnup_ingreso
        bnup = bnup_ingreso.objects.create(
            unidad_técnica=unidadTecnica, 
            funcionario=funcionario,  # Pasamos la instancia de Funcionario
            fecha=fechaIngreso,
            calle=Calle,
            n_de_ingreso=n_de_ingreso,
            ref=ref,
            mat=mat,
            codigo=codigo,
            constituye=constituye,
            otro_constituye=constituye_otro,
        )

        print("BNUP creado:", bnup)

            # Guardar el archivo adjunto si existe
        if archivo_adjunto:
            bnup.archivo_adjunto = archivo_adjunto
            bnup.save()

        return redirect('bnup')

    return render(request,'Bnup.html',data)

def limpiar_texto(texto):
    if texto:
        return ' '.join(texto.upper().split())
    return texto

def actualizar(request,id=0):
    iniciativa = Iniciativa.objects.get(id=id)
    users = User.objects.all()

    data = {
        'iniciativa':iniciativa,
        'users':users,
    }

    if request.method == "POST":
        if request.FILES.get('au_archivo'):
                iniciativa.solicitud_au_adjunto = request.FILES.get('au_archivo')
                iniciativa.solicitud_au = entregado(request.FILES.get('au_archivo'))


        if request.FILES.get('fac_archivo'):
                iniciativa.factibilidad_adjunto = request.FILES.get('fac_archivo')
                iniciativa.factibilidad = entregado(request.FILES.get('fac_archivo'))

        iniciativa.save()

        return redirect('menu')    
    return render(request,'Formulario.html',data)

def actualizar_coordinacion(request, id=0):
    iniciativa = get_object_or_404(Iniciativa, id=id)  # Usa get_object_or_404 para manejar errores si no se encuentra
    usuarios_asignados = request.POST.getlist('usuarios')
    fecha_completa = request.POST.get('fechaVisitaCompleta')
    iniciativa.visita = entregado(fecha_completa)
    descripcion = request.POST.get('descripcion_visita')

    fecha_naive = datetime.strptime(fecha_completa, "%Y-%m-%dT%H:%M")
            
    # Agrega la zona horaria predeterminada
    fecha_con_tz = make_aware(fecha_naive)
    
    # Asigna la fecha con zona horaria al modelo
    iniciativa.fecha_visita = fecha_con_tz
    iniciativa.detalle_visita = descripcion



    if request.FILES.get('archivo_visita'):
        iniciativa.visita_adjunto = request.FILES.get('archivo_visita')
        iniciativa.visita = entregado(request.FILES.get('archivo_visita'))



    # Actualiza la fecha y guarda
    iniciativa.save()
    print(usuarios_asignados)

    for user_id in usuarios_asignados:
            user = User.objects.filter(id=user_id).first()
            if user:
                ini_user.objects.create(
                    categoría='C',  # Puedes ajustar este valor según la lógica de tu aplicación
                    id_iniciativa=iniciativa,
                    id_user=user
                )


    
    # Redirige a la vista 'actualizar' con el mismo id
    return redirect(reverse('actualizar', kwargs={'id': iniciativa.id}))
    
def actualizar_terreno(request, id=0):
    iniciativa = get_object_or_404(Iniciativa, id=id)  # Usa get_object_or_404 para manejar errores si no se encuentra
    usuarios_asignados = request.POST.getlist('usuarios')
    fecha_completa = request.POST.get('fechaTerrenoCompleta')
    descripcion = request.POST.get('descripcion_terreno')
    iniciativa.terreno = entregado(fecha_completa)

    fecha_naive = datetime.strptime(fecha_completa, "%Y-%m-%dT%H:%M")
            
    # Agrega la zona horaria predeterminada
    fecha_con_tz = make_aware(fecha_naive)
    
    # Asigna la fecha con zona horaria al modelo
    iniciativa.fecha_visita = fecha_con_tz
    iniciativa.detalle_terreno = descripcion

    if request.FILES.get('terreno_adjunto'):
        iniciativa.visita_adjunto = request.FILES.get('terreno_adjunto')
        iniciativa.visita = entregado(request.FILES.get('terreno_adjunto'))

    # Actualiza la fecha y guarda
    iniciativa.save()
    print(usuarios_asignados)

    for user_id in usuarios_asignados:
            user = User.objects.filter(id=user_id).first()
            if user:
                ini_user.objects.create(
                    categoría='T',  # Puedes ajustar este valor según la lógica de tu aplicación
                    id_iniciativa=iniciativa,
                    id_user=user
                )
    return redirect(reverse('actualizar', kwargs={'id': iniciativa.id}))

def get_iniciativa_details(request, pk):
    iniciativa = get_object_or_404(Iniciativa, pk=pk)
    usuarios_asignados = ini_user.objects.filter(id_iniciativa=iniciativa)

    data = {
        "id": iniciativa.id,
        "numero_ingreso": iniciativa.numero_ingreso,
        "nombre_proyecto": iniciativa.nombre_proyecto,
        "fecha": iniciativa.fecha.strftime("%Y-%m-%d %H:%M:%S"),
        "estado": iniciativa.Estado,
        "profesional": iniciativa.profesional.username if iniciativa.profesional else "Sin Asignar",
        "visita": iniciativa.visita,
        "visita_adjunto": iniciativa.visita_adjunto.url if iniciativa.visita_adjunto else None,
        "fecha_visita": iniciativa.fecha_visita.strftime("%Y-%m-%d %H:%M:%S") if iniciativa.fecha_visita else None,
        "detalle_visita": iniciativa.detalle_visita,
        "terreno": iniciativa.terreno,
        "terreno_adjunto": iniciativa.terreno_adjunto.url if iniciativa.terreno_adjunto else None,
        "fecha_terreno": iniciativa.fecha_terreno.strftime("%Y-%m-%d %H:%M:%S") if iniciativa.fecha_terreno else None,
        "detalle_terreno": iniciativa.detalle_terreno,
    }
    return JsonResponse(data)

def fechas_hoy(algo):

    return None

def entregado(algo):

    if algo:
        return True
    else:
        return False