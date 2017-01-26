from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.conf import settings
from smart_selects.db_fields import ChainedForeignKey
from datospersonalesapp.models import Facultad
from empleadosapp.models import Doctor

"""
    A continuacion se presenta una serie de campos que son propios de un paciente.
    Ademas de cumpli
    OA-NA-NP:Campos obligatorios-Automatico, no modifica admin o paciente
    OB-SA-NP:Campos obligatorios, cambios realizados por el administrador
    OP-SA-NP:Campos opcionales, cambios realizados por el administrador
    OB-SA-SP:Campos obligatorios, cambios realizados por paciente
    OP-SA-SP:Campos opcionales, cambios realizados por paciente
"""

SEXO_ELECCIONES = (
    ('F','Femenino'),
    ('M','Masculino'),
    )

# Esta clase contiene los campos de las acividades que se realizan en enfermeria y una breve descripcion de ellas
class Actividad_Enfermeria(models.Model):
    codActividad=models.AutoField(primary_key=True, null=False)#OA-NA-NP
    nombreActividad = models.CharField("Nombre Actividad", max_length=50)#OB-SA-NP
    fechaActividad=models.DateTimeField("Fecha de Inscripcion",auto_now_add=True) #OA-NA-NP default=timezone.now
    def __str__(self):
        return '%s' % (self.nombreActividad)#self.codActividad

    def get_actividad(self):
        return '%s'% (self.nombreActividad)
    @property
    def chartdateformat(self):
        return self.fechaActividad.strftime('%d/%m/%Y')

# Esta clase contiene los campos del censo diario que se lleva a cabo en enfermeria
class Censo_Enfermeria(models.Model):
    codCenso = models.AutoField(primary_key=True, null=False)#OA-NA-NP
    actividad = models.ForeignKey(Actividad_Enfermeria,on_delete=models.SET_NULL, verbose_name="Actividad", default=1, null=True, blank=True)#OB-SA-NP
    cantidad = models.PositiveIntegerField()#OB-SA-NP
    fechaActividad = models.DateTimeField("Fecha de la Actividad",auto_now_add=True) #OA-NA-NP default=timezone.now
    def __str__(self):
        return '%s %s' % (self.codCenso, self.actividad)#self.codActividad
    @property
    def chartdateformat(self):
        return self.fechaActividad.strftime('%d/%m/%Y')

# Esta clase contiene los campos pertenecientes al expediente provisional se crea a los alumnos de nuevo ingreso
class Expediente_Provisional(models.Model):
    Cod_Expediente_Provisional=models.AutoField(primary_key=True, null=False)#OA-NA-NP
    nombrePrimero=models.CharField("Primer Nombre", max_length=15) #OB-SA-NP
    nombreSegundo=models.CharField("Segundo Nombre", max_length=15, null=True, blank=True) #OP-SA-NP
    apellidoPrimero=models.CharField("Primer Apellido", max_length=15) #OB-SA-NP
    apellidoSegundo=models.CharField("Segundo Apellido", max_length=15, null=True, blank=True) #OP-SA-NP
    sexo = models.CharField(max_length=1,choices=SEXO_ELECCIONES, default='M') #OB-SA-NP
    nit = models.CharField("NIT", max_length=17, null= True, blank= True, default='NULL')
    fechaNacimiento = models.DateField("Fecha de Nacimiento",help_text="YYYY-MM-DD") #OB-SA-NP
    facultad=models.ForeignKey(Facultad, on_delete=models.SET_NULL, verbose_name="Facultad", default=1, null=True, blank=True) #OB-SA-NP
    telefono=models.CharField(max_length=9, null=True, blank=True) #OP-SA-SP
    correo=models.EmailField(null=True, blank=True) #OP-SA-SP
    fechaIngreso=models.DateTimeField("Fecha de Inscripcion",auto_now_add=True) #OA-NA-NP default=timezone.now
    nombreRecibido=models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Tomo informacion", editable=False, default=1) #OA-NA-NP
    talla = models.DecimalField(max_digits=5, decimal_places=2)#OB-SA-NP
    temperatura = models.DecimalField(max_digits=3, decimal_places=1)#OB-SA-NP
    presionArterial = models.CharField(max_length=7)#OB-SA-NP
    peso = models.DecimalField(max_digits=5, decimal_places=2)#OB-SA-NP
    frecuenciaRespiratoria = models.PositiveIntegerField()#OB-SA-NP
    frecuenciaCardiaca = models.PositiveIntegerField()#OB-SA-NP
    Observaciones= models.CharField(max_length=5000,null=True,blank=True)#OB-SA-NP
    
    nit = models.CharField("NIT", max_length=17, unique=True) #Esto es modificado x Luis para prueba de modificar la BD 
    
    def __str__(self):
         return '%s %s %s' % (self.Cod_Expediente_Provisional, self.nombrePrimero, self.apellidoPrimero)#self.Cod_Expediente_Provisional
    
    #Devuelve el nombre completo del paciente
    def get_full_name(self):
        return '%s %s %s %s' % (self.nombrePrimero , self.nombreSegundo , self.apellidoPrimero , self.apellidoSegundo )
    
    #Devuelva la edad del paciente
    def edad_paciente(self):
        fecha_actual = timezone.now()
        if (fecha_actual.month - self.fechaNacimiento.month) < 0:
            edad = fecha_actual.year - (self.fechaNacimiento.year + 1)
        elif (fecha_actual.month - self.fechaNacimiento.month) == 0:
            if (fecha_actual.day - self.fechaNacimiento.day) < 0:
                edad = fecha_actual.year - (self.fechaNacimiento.year + 1)
            else:
                edad = fecha_actual.year - self.fechaNacimiento.year
        else:
            edad = fecha_actual.year - self.fechaNacimiento.year
        return edad

# Formulario para certificacion de salud
class Certificado_Salud(models.Model):
    codigoCertificado = models.AutoField(primary_key=True,null=False)
    codigoDoctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Doctor", default=1, null=True, blank=True)
    codigoPaciente = models.ForeignKey(Expediente_Provisional, on_delete=models.CASCADE, verbose_name="Paciente")
    fechaIngreso=models.DateTimeField("Fecha de Creacion",auto_now_add=True) #OA-NA-NP default=timezone.now
    nombreRecibido=models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Tomo informacion", editable=False, default=1) #OA-NA-NP
    enfermedadIC = models.CharField(max_length=2, null=True, blank=True)
    enfermedadICDetalle = models.CharField(max_length=1000, null=True, blank=True) #OP-SA-SP
    enfermedadEF = models.CharField(max_length=2, null=True, blank=True)
    enfermedadEFDetalle = models.CharField(max_length=1000, null=True, blank=True) #OP-SA-SP
    enfermedadSN = models.CharField(max_length=2, null=True, blank=True)
    enfermedadSNDetalle = models.CharField(max_length=1000, null=True, blank=True) #OP-SA-SP
    resultadoHIV = models.CharField(max_length=100, null=True, blank=True) #OP-SA-SP
    resultadoHECES = models.CharField(max_length=100, null=True, blank=True) #OP-SA-SP
    resultadoVDRL = models.CharField(max_length=100, null=True, blank=True) #OP-SA-SP
    resultadoHemograma = models.CharField(max_length=100, null=True, blank=True) #OP-SA-SP
    resultadoOrina = models.CharField(max_length=100, null=True, blank=True) #OP-SA-SP
    resultadoRX = models.CharField(max_length=100, null=True, blank=True) #OP-SA-SP
    presentaImpedimentos = models.CharField(max_length=2, null=True, blank=True)
    presentaImpedimentosDetalle = models.CharField(max_length=1000, null=True, blank=True) #OP-SA-SP
    aptoAprobado = models.CharField(max_length=2, null=True, blank=True)
    aptoAprobadoDetalle = models.CharField(max_length=1000, null=True, blank=True) #OP-SA-SP