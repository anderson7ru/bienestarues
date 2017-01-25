# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils import timezone

# apps internas y externas
from datospersonalesapp.models import Paciente
from empleadosapp.models import Empleado, Doctor

ESTADO_ELECCIONES = (
    ('N','Normal'),
    ('C','Cancelado'),
    ('R','Reprogramar'),
    )

class diasSemana(models.Model):
	dias = models.CharField(max_length=15) #Lunes-Viernes y Todos los dias
	
	#Al llamar a diasSemana, se visualiza: los dias de la semana
	def __str__(self):
		return '%s' % (self.dias)
	
class HorarioAtencion(models.Model):
	codigoHorario = models.AutoField(primary_key=True, null=False)
	codigoDoctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Doctor",)
	dia = models.ManyToManyField(diasSemana)
	horaInicio = models.TimeField("Hora inicio")
	horaFinal = models.TimeField("Hora final")
	pacienteConsulta = models.PositiveIntegerField()
	
	#Al llamar a HorarioAtencion, se visualiza: doctor
	def __str__(self):
		return '%s' % (self.codigoDoctor)
		
class Cita(models.Model):
	codigoCita = models.AutoField(primary_key=True, null=False)
	codigoDoctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Doctor",)
	paciente = models.ForeignKey(Paciente, null=False, on_delete=models.CASCADE,limit_choices_to={'estadoExpediente':'A'},verbose_name="No expediente")
	fechaConsulta = models.DateField("Fecha de la Consulta",help_text="DD/MM/YYYY")
	horaConsulta = models.TimeField("Hora de la consulta")
	estadoConsulta = models.CharField(max_length=1,choices=ESTADO_ELECCIONES, default='N')
	
	#Al llamar a Cita, se visualiza: paciente,codigoDoctor,estadoConsulta
	def __str__(self):
		return '%s %s %s' % (self.codigoDoctor, self.paciente, self.estadoConsulta)	
	
class Cancelacion(models.Model):
	codigoCancelacion = models.AutoField(primary_key=True, null=False)
	codigoDoctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Doctor",)
	fechaInicio = models.DateField("fecha inicio",help_text="DD/MM/YYYY")
	fechaFinal = models.DateField("fecha final",help_text="DD/MM/YYYY", null=True, blank=True)
	horaInicio = models.TimeField("Hora inicio")
	horaFinal = models.TimeField("Hora final")
	
	#Al llamar a Cancelacion, se visualiza: doctor,fecha y hora de inicio
	def __str__(self):
		return '%s %s %s' % (self.codigoDoctor, self.fechaInicio, self.horaInicio)