from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
ESTADO = [
    ()
    ]

UNI_TEC ={
    ('',''),
    ('Asesoría Urbana','AU'),
    ('Direcciones de Obras Municipales','DOM'),
}

# Create your models here.
def content_file_name_adjunto(instance, filename):
    # Extraer la extensión del archivo original
    ext = filename.split('.')[-1]
    
    # Carpeta específica basada en el ID del objeto
    folder = f"assets/document/{instance.id}/"
    
    # Base name del archivo
    base_filename = "visita"
    
    # Ruta completa del archivo inicial
    file_path = os.path.join(folder, f"{base_filename}.{ext}")

    # Verificar si ya existe un archivo con el mismo nombre
    counter = 1
    while os.path.exists(os.path.join(folder, file_path)):
        # Crear una versión con un sufijo incremental
        file_path = os.path.join(folder, f"{base_filename}_{counter}.{ext}")
        counter += 1

    return file_path

def content_file_terreno_adjunto(instance, filename):
    # Extraer la extensión del archivo original
    ext = filename.split('.')[-1]
    
    # Carpeta específica basada en el ID del objeto
    folder = f"assets/document/{instance.id}/"
    
    # Base name del archivo
    base_filename = "terreno"
    
    # Ruta completa del archivo inicial
    file_path = os.path.join(folder, f"{base_filename}.{ext}")

    # Verificar si ya existe un archivo con el mismo nombre
    counter = 1
    while os.path.exists(os.path.join(folder, file_path)):
        # Crear una versión con un sufijo incremental
        file_path = os.path.join(folder, f"{base_filename}_{counter}.{ext}")
        counter += 1

    return file_path

def content_file_au_adjunto(instance, filename):
    # Extraer la extensión del archivo original
    ext = filename.split('.')[-1]
    
    # Carpeta específica basada en el ID del objeto
    folder = f"assets/document/{instance.id}/"
    
    # Base name del archivo
    base_filename = "solicitud_AU"
    
    # Ruta completa del archivo inicial
    file_path = os.path.join(folder, f"{base_filename}.{ext}")

    # Verificar si ya existe un archivo con el mismo nombre
    counter = 1
    while os.path.exists(os.path.join(folder, file_path)):
        # Crear una versión con un sufijo incremental
        file_path = os.path.join(folder, f"{base_filename}_{counter}.{ext}")
        counter += 1

    return file_path

def content_file_factibilidad_adjunto(instance, filename):
    # Extraer la extensión del archivo original
    ext = filename.split('.')[-1]
    
    # Carpeta específica basada en el ID del objeto
    folder = f"assets/document/{instance.id}/"
    
    # Base name del archivo
    base_filename = "Factibilidad"
    
    # Ruta completa del archivo inicial
    file_path = os.path.join(folder, f"{base_filename}.{ext}")

    # Verificar si ya existe un archivo con el mismo nombre
    counter = 1
    while os.path.exists(os.path.join(folder, file_path)):
        # Crear una versión con un sufijo incremental
        file_path = os.path.join(folder, f"{base_filename}_{counter}.{ext}")
        counter += 1

    return file_path

def content_file_asamblea_adjunto(instance, filename):
    # Extraer la extensión del archivo original
    ext = filename.split('.')[-1]
    
    # Carpeta específica basada en el ID del objeto
    folder = f"assets/document/{instance.id}/"
    
    # Base name del archivo
    base_filename = "Asamblea"
    
    # Ruta completa del archivo inicial
    file_path = os.path.join(folder, f"{base_filename}.{ext}")

    # Verificar si ya existe un archivo con el mismo nombre
    counter = 1
    while os.path.exists(os.path.join(folder, file_path)):
        # Crear una versión con un sufijo incremental
        file_path = os.path.join(folder, f"{base_filename}_{counter}.{ext}")
        counter += 1

    return file_path

def content_file_analisis_adjunto(instance, filename):
    # Extraer la extensión del archivo original
    ext = filename.split('.')[-1]
    
    # Carpeta específica basada en el ID del objeto
    folder = f"assets/document/{instance.id}/"
    
    # Base name del archivo
    base_filename = "Análisis"
    
    # Ruta completa del archivo inicial
    file_path = os.path.join(folder, f"{base_filename}.{ext}")

    # Verificar si ya existe un archivo con el mismo nombre
    counter = 1
    while os.path.exists(os.path.join(folder, file_path)):
        # Crear una versión con un sufijo incremental
        file_path = os.path.join(folder, f"{base_filename}_{counter}.{ext}")
        counter += 1

    return file_path


class Iniciativa(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    numero_ingreso = models.CharField(max_length=100, blank=True, default='')
    nombre_proyecto = models.CharField(max_length=255, blank=True, default='')
    fecha = models.DateTimeField(auto_now_add=True)

    Estado = models.CharField(max_length=100, blank=True, default='En Proceso',)

    profesional = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    visita = models.BooleanField(default=False)
    visita_adjunto = models.FileField(upload_to=content_file_name_adjunto, blank=True, null=True)
    fecha_visita = models.DateTimeField(null=True, blank=True)
    detalle_visita = models.TextField(blank=True, default='')


    terreno = models.BooleanField(default=False)
    terreno_adjunto = models.FileField(upload_to=content_file_terreno_adjunto, blank=True, null=True)
    fecha_terreno = models.DateTimeField(null=True, blank=True)
    detalle_terreno = models.TextField(blank=True, default='')


    solicitud_au = models.BooleanField(default=False)
    solicitud_au_adjunto = models.FileField(upload_to=content_file_au_adjunto, blank=True, null=True)
    fecha_solicitud_au= models.DateTimeField(null=True, blank=True)

    factibilidad = models.BooleanField(default=False)
    factibilidad_adjunto = models.FileField(upload_to=content_file_factibilidad_adjunto, blank=True, null=True)
    fecha_factibilidad = models.DateTimeField(null=True, blank=True)

    asamblea = models.BooleanField(default=False)
    asamblea_adjunto = models.FileField(upload_to=content_file_asamblea_adjunto, blank=True, null=True)
    fecha_asamblea = models.DateTimeField(null=True, blank=True)
    
    analisis = models.BooleanField(default=False)
    analisis_adjunto = models.FileField(upload_to=content_file_analisis_adjunto, blank=True, null=True)
    fecha_analisis = models.DateTimeField(null=True, blank=True)
    

    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "iniciativa"
        verbose_name_plural = "iniciativas"

    def __str__(self):
        return f"{self.id} - {self.numero_ingreso}"

class Departamento(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        verbose_name = "departamento"
        verbose_name_plural = "departamentos"


def content_file_ini_depa_adjunto(instance, filename):
    # Extraer la extensión del archivo original
    ext = filename.split('.')[-1]
    
    # Carpeta específica basada en el ID del objeto o el ID de la iniciativa
    iniciativa_id = instance.id_iniciativa.id if instance.id_iniciativa else 'undefined'
    folder = f"assets/document/{iniciativa_id}/"
    
    # Base name del archivo
    base_filename = "visita"
    
    # Ruta completa del archivo inicial
    file_path = os.path.join(folder, f"{base_filename}.{ext}")

    # Verificar si ya existe un archivo con el mismo nombre
    counter = 1
    while os.path.exists(os.path.join(folder, file_path)):
        # Crear una versión con un sufijo incremental
        file_path = os.path.join(folder, f"{base_filename}_{counter}.{ext}")
        counter += 1

    return file_path

class departamento_iniciativa (models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    archivo = models.FileField(upload_to=content_file_ini_depa_adjunto, blank=True, null=True)

    id_iniciativa = models.ForeignKey(Iniciativa, on_delete=models.CASCADE, related_name='iniciativas')
    id_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='departamentos')


    class Meta:
        verbose_name = "departamento"
        verbose_name_plural = "departamentos"

class ini_user(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    categoría = models.TextField(blank=True,null=True)
    
    id_iniciativa = models.ForeignKey(Iniciativa, on_delete=models.CASCADE, related_name='ini')
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

def content_file_bnup_adjunto(instance, filename):
    # Extraer la extensión del archivo original
    ext = filename.split('.')[-1]
    
    # Carpeta específica basada en el ID del objeto
    folder = f"assets/document/bnup/{instance.id}/"
    
    # Base name del archivo
    base_filename = "bnup_de_respuesta"
    
    # Ruta completa del archivo inicial
    file_path = os.path.join(folder, f"{base_filename}.{ext}")

    # Verificar si ya existe un archivo con el mismo nombre
    counter = 1
    while os.path.exists(os.path.join(folder, file_path)):
        # Crear una versión con un sufijo incremental
        file_path = os.path.join(folder, f"{base_filename}_{counter}.{ext}")
        counter += 1

    return file_path

class Funcionario(models.Model):
    nombre = models.CharField(max_length=255,blank=True,null=True)

class bnup_ingreso(models.Model):

    id = models.BigAutoField(primary_key=True, unique=True)
    estado = models.TextField(blank=True, default='EN ESPERA')


    ref = models.TextField(blank=True,null=True)
    mat = models.TextField(blank=True,null=True)

    n_de_ingreso = models.TextField(blank=True,null=True)
    codigo = models.BigIntegerField(blank=True,null=True)

    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=True, blank=True)
    unidad_técnica = models.CharField(max_length=100, blank=True, default='',choices=UNI_TEC)
    fecha = models.DateTimeField(null=True, blank=True)
    archivo_adjunto = models.FileField(upload_to=content_file_bnup_adjunto, blank=True, null=True)
    constituye = models.CharField(max_length=100)
    otro_constituye = models.TextField(blank=True,null=True)
    calle = models.TextField(blank=True,null=True)
