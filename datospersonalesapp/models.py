# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.conf import settings
from smart_selects.db_fields import ChainedForeignKey

# Elecciones para modelos: --se utilizan en /admin
ESTADOCIVIL_ELECCIONES = (
    ('SOLTERO','Soltero(a)'),
    ('CASADO','Casado(a)'),
    ('DIVORCIADO','Divorciado(a)'),
    ('ACOMPANADO','Acompanado(a)'),
    ('VIUDO','Viudo(a)'),
    )

ESTADOUES_ELECCIONES = (
    ('EST','Estudiante'),
    ('DOC','Docente'),
    ('PAD','Pers.Administrativo'),
    ('OTR','Otro'),
    )
        
SEXO_ELECCIONES = (
    ('F','Femenino'),
    ('M','Masculino'),
    )

ESTADO_ELECCIONES = (
    ('A','Activo'),
    ('P','Pasivo'), #o inactivo, los "Eliminados"
    )
		
#Primeras clases para generar datos basicos del expediente
#clases Padre
class Facultad(models.Model):
    codigoFacultad = models.PositiveIntegerField("Codigo", primary_key=True)#models.CharField("Codigo", max_length=3, primary_key=True)
    nombreFacultad = models.CharField("Facultad", max_length=50)
    
    def __str__(self):
        return self.nombreFacultad
    
class Departamento(models.Model):
    codigoDepartamento = models.AutoField(primary_key=True)
    nombreDepartamento = models.CharField("Departamento", max_length=30)
    
    def __str__(self):
        return self.nombreDepartamento
        
#clase hija de Departamento
class Municipio(models.Model):
    codigoMunicipio = models.AutoField(primary_key=True)
    codDepartamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name="Departamento",)
    nombreMunicipio = models.CharField("Municipio", max_length=80)
    
    def __str__(self):
        return self.nombreMunicipio
    
#clase hija de Facultad, departamento y municipio 
class Paciente(models.Model):
	"""
	A continuacion se presenta una serie de campos que son propios de un paciente.
	Ademas de cumpli
	OA-NA-NP:Campos obligatorios-Automatico, no modifica admin o paciente
	OB-SA-NP:Campos obligatorios, cambios realizados por el administrador
	OP-SA-NP:Campos opcionales, cambios realizados por el administrador
	OB-SA-SP:Campos obligatorios, cambios realizados por paciente
	OP-SA-SP:Campos opcionales, cambios realizados por paciente
	"""
	codigoPaciente = models.CharField("No. de Expediente Clinico", max_length=7, primary_key=True) #OA-NA-NP
	#Datos del paciente:
	apellidoPrimero = models.CharField("Primer Apellido", max_length=15) #OB-SA-NP
	apellidoSegundo = models.CharField("Segundo Apellido", max_length=15, null=True, blank=True) #OP-SA-NP
	nombrePrimero = models.CharField("Primer Nombre", max_length=15) #OB-SA-NP
	nombreSegundo = models.CharField("Segundo Nombre", max_length=15, null=True, blank=True) #OP-SA-NP
	sexo = models.CharField(max_length=1,choices=SEXO_ELECCIONES, default='M') #OB-SA-NP
	fechaNacimiento = models.DateField("Fecha de Nacimiento",help_text="DD/MM/YYYY") #OB-SA-NP
	estadoCivil = models.CharField("Estado Civil",max_length=12, choices=ESTADOCIVIL_ELECCIONES, default='SOLTERO') #OB-SA-SP
	nit = models.CharField("NIT", max_length=17, unique=True) #Este es el mio (Luis) para modificacion de BD
	dui = models.CharField("DUI", max_length=10, null=True, blank=True) #OP-SA-NP 
	#Datos Universitarios
	due = models.CharField("DUE", max_length=7, null=True, blank=True) #OP-SA-NP
	estadoUes = models.CharField("Estado UES", max_length=3, choices=ESTADOUES_ELECCIONES, default='EST') #OB-SA-NP
	facultadE = models.ForeignKey(Facultad, on_delete=models.SET_NULL, verbose_name="Facultad", default=1, null=True, blank=True) #OB-SA-NP
	#Datos de contacto
	codDepartamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, verbose_name="Departamento", default=6, null=True, blank=True) #OB-SA-SP
	codMunicipio = ChainedForeignKey(Municipio, chained_field='codDepartamento',chained_model_field='codDepartamento',show_all=False,auto_choose=True) #OB-SA-SP
	direccion = models.CharField(max_length=300) #OB-SA-SP
	telefono = models.CharField(max_length=9, null=True, blank=True) #OP-SA-SP
	correo = models.EmailField(null=True, blank=True) #OP-SA-SP
	#Datos Familiares
	nombrePadre = models.CharField("Nombre del Padre", max_length=65, null=True, blank=True) #OP-SA-SP
	nombreMadre = models.CharField("Nombre de la Madre", max_length=65, null=True, blank=True) #OP-SA-SP
	nombrePareja = models.CharField("Nombre del Conyuge", max_length=65, null=True, blank=True) #OP-SA-SP
	emergencia = models.CharField("En caso de Emergencia avisar a", max_length=65) #OB-SA-NP
	telefonoEmergencia = models.CharField("Telefono",max_length=9) #OB-SA-NP
	#Creacion de Expediente
	nombreRecibido = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Tomo informacion", editable=False, default=1) #OA-NA-NP
	fechaIngreso = models.DateTimeField("Fecha de Inscripcion",auto_now_add=True) #OA-NA-NP default=timezone.now
	fechaModificacion = models.DateTimeField("Ultima modificacion",auto_now=True) #OA-NA-NP default=timezone.now
	estadoExpediente = models.CharField("Archivo",max_length=1,choices=ESTADO_ELECCIONES,default='A') #OB-SA-NP
	
	#Devuelve el dui del paciente
	def get_codigoPaciente(self):
		return '%s' % (self.codigoPaciente )
	
	#Devuelve el dui del paciente
	def get_nit(self):
		return '%s' % (self.nit )
	
	#Devuelve el dui del paciente
	def get_dui(self):
		return '%s' % (self.dui )
	
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
	
	#Cuando llamen a este modelo, se presentaran el codigo del paciente y nombre
	def __str__(self):
		return '%s %s %s %s' % (self.codigoPaciente, self.nombrePrimero, self.apellidoPrimero, self.apellidoSegundo)
		
class Busqueda(models.Model):
	codigoBusqueda = models.AutoField(primary_key=True)
	consulta = models.CharField(max_length=150,null=True,blank=True)
	fechaBusqueda = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.codigoBusqueda