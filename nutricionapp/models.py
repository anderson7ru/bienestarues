#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals

from django.db import models
from datospersonalesapp.models import Paciente
from django.conf import settings
from django.core.validators import validate_comma_separated_integer_list
from smart_selects.db_fields import ChainedForeignKey
# Create your models here.

habitos_eleccion = (
    (1,'Consume Licor'),
    (2,"Fuma"),
    (3,"Consumo de Sal extra"),
    (4,"Consumo de Agua"),
    (5,"Consumo de Cafe"),
    (6,"Consumo de Chile")
)

estructura_eleccion = (
    ('p','Pequena'),
    ('m','Mediana'),
    ('g','Grande'),
)
    
class GruposAlimentos(models.Model):
    codGrupoAlimento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=8,verbose_name="Nombre de Grupo")
    
    def __str__(self):
        return self.nombre
    
class AlimentosGrupo(models.Model):
    codAlimentosGrupo = models.AutoField(primary_key=True)
    grupo = models.ForeignKey(GruposAlimentos,on_delete=models.CASCADE)
    alimento = models.CharField(max_length=50,verbose_name="Alimento")
    
    def __str__(self):
        return self.alimento

class Nutricion(models.Model):
    codNutricion =  models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE, limit_choices_to={'estadoExpediente':'A'}, verbose_name="No expediente", null=False)
    estructuraOsea = models.CharField(max_length=1,verbose_name="Estructura Osea",choices=estructura_eleccion)
    extensionBrazada = models.PositiveSmallIntegerField()
    circunferenciaCuerpo = models.PositiveSmallIntegerField()
    pesoDeseable = models.PositiveSmallIntegerField()
    nombreRecibido = models.ForeignKey(settings.AUTH_USER_MODEL, 
    verbose_name="Tomo informacion", editable=False, default=1)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return str(self.codNutricion)
    
class DatosClinicos(models.Model):
    codDatosClinicos = models.AutoField(primary_key=True)
    nutricion = models.ForeignKey(Nutricion, on_delete=models.CASCADE,null=False)
    clinica = models.CharField(max_length=60,verbose_name="Clinica Referencia")
    medico = models.CharField(max_length=60,verbose_name="Medico Referencia")
    diagnosticoRef = models.TextField(verbose_name="Diagnostico de Referencia")
    diagnosticoSec = models.TextField(verbose_name="Diagnostico Secundario")
    medicamentos = models.TextField(verbose_name="Medicamentos usados")
    deportes = models.TextField(verbose_name="Deportes Practicados")
    tiempoPractica = models.PositiveSmallIntegerField()
    nombreRecibido = models.ForeignKey(settings.AUTH_USER_MODEL, 
    verbose_name="Tomo informacion", editable=False, default=1)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return str(self.codDatosClinicos)
    
class DatosNutricionales(models.Model):
    codDatosNutricionales = models.AutoField(primary_key=True)
    nutricion = models.ForeignKey(Nutricion, on_delete=models.CASCADE,null=False)
    habitos = models.CharField(max_length=12,verbose_name="Habitos",choices=habitos_eleccion,validators=[validate_comma_separated_integer_list])
    #grupoAlimentos = models.ForeignKey(GruposAlimentos,on_delete=models.SET_NULL,verbose_name="Grupo de Alimentos",null=True,blank=True)
    #alimentos = ChainedForeignKey(AlimentosGrupo,chained_field='grupoAlimentos',chained_model_field='grupo',show_all=False,auto_choose=True)
    alimentosPreferidos = models.TextField("Alimentos Preferidos")
    alimentosIntolerados = models.TextField("Alimentos intolerados o rechazados")
    nombreRecibido = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Tomo informacion", editable=False, default=1)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return str(self.codDatosNutricionales)
    
class Anamnesis(models.Model):
    codAnamnesis = models.AutoField(primary_key=True)
    nutricion = models.ForeignKey(Nutricion, on_delete=models.CASCADE,null=False)
    tiempoComida = models.PositiveSmallIntegerField()
    lugar = models.CharField(max_length=30,verbose_name="Lugar")
    hora = models.TimeField(verbose_name="Hora")
    alimentosConsumidos = models.CharField(max_length=100,verbose_name="Alimentos Consumidos")
    nombreRecibido = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Tomo informacion", editable=False, default=1)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return str(self.codAnamnesis)
    

