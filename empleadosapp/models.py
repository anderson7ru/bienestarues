# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils import timezone

SEXO_ELECCIONES = (
    ('F','Femenino'),
    ('M','Masculino'),
    )

CARGO_ELECCIONES = 	(
    ('D','Doctor'),
    ('E','Enfermera'),
    ('L','Laboratorista'),
    ('A','Personal de Archivo'),
    ('P','Personal Administrativo'),
    ('O','Otros'),
    )
	
ESTADO_ELECCIONES = (
    ('A','Activo'),
    ('P','Pasivo'), #o inactivo, los "Eliminados"
    )	
	
# Modelo de Empleadosapp
class Empleado(models.Model):
	codigoEmpleado = models.AutoField(primary_key=True, null=False)
	apellidoPrimero = models.CharField("Primer Apellido", max_length=15)
	apellidoSegundo = models.CharField("Segundo Apellido", max_length=15, null=True, blank=True) 
	nombrePrimero = models.CharField("Primer Nombre", max_length=15)
	nombreSegundo = models.CharField("Segundo Nombre", max_length=15, null=True, blank=True)
	sexo = models.CharField(max_length=1,choices=SEXO_ELECCIONES, default='M')
	fechaNacimiento = models.DateField("Fecha de Nacimiento",help_text="DD/MM/YYYY")
	cargo = models.CharField(max_length=1,choices=CARGO_ELECCIONES, default='P')
	estadoEmpleado = models.CharField("Estado",max_length=1,choices=ESTADO_ELECCIONES,default='A')
	nombreRecibido = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Recibio la informacion", editable=False, default=1)
	fechaIngreso = models.DateTimeField("Fecha de Inscripcion",auto_now_add=True)
	
	def __str__(self):
		return '%s %s' % (self.nombrePrimero, self.apellidoPrimero)
	
	def get_full_name(self):
		return '%s %s %s %s' % (self.nombrePrimero , self.nombreSegundo , self.apellidoPrimero , self.apellidoSegundo )

#tabla alterna para poner las especialidades		
class Especialidad(models.Model):
	especialidad = models.CharField(max_length=50) #Especialidad medica
	
	def __str__(self):
		return '%s' % (self.especialidad)

class Doctor(models.Model):
	codigoDoctor = models.AutoField(primary_key=True, null=False)
	codigoEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name="Empleado",)
	especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, verbose_name="Especialidad",)
	firma = models.TextField()
	sello = models.TextField()
	
	#Devuelve la especialidad del doctor
	def get_especialidad(self):
		return '%s' % (self.especialidad )
	
	def __str__(self):
		return '%s' % (self.codigoEmpleado)		

class Laboratorista(models.Model):
	codigoLaboratorista = models.AutoField(primary_key=True, null=False)
	codigoEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name="Empleado",)
	firma = models.TextField()
	sello = models.TextField()
	
	#Devuelve la especialidad del doctor
	def __str__(self):
		return '%s' % (self.codigoEmpleado)
