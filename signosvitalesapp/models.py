# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from decimal import *
from django.utils import timezone
from django.conf import settings
from datospersonalesapp.models import Paciente

""" 
Datos para signos vitales:
1. datospersonales\models. Tabla: Paciente.
Esta tabla contiene una serie de informacion que se necesitan para signos vitales como:
-codigoPaciente es la PK de paciente
-apellidoPrimero, apellidoSegundo, nombrePrimero, nombreSegundo nombre completo del paciente.
-edad es retomado y almacenado de una funcion
"""

#Signos Vitales
class SignosVitales(models.Model):
    codigoSignosVitales = models.AutoField(primary_key=True, null=False)
    paciente = models.ForeignKey(Paciente, null=False, on_delete=models.CASCADE,limit_choices_to={'estadoExpediente':'A'},verbose_name="No expediente")
    edad = models.PositiveIntegerField() #Edad en el momento de toma de signos vitales
    presionArterial = models.CharField("Presion Arterial",max_length=7) #40/40-300/200 mmHg
    frecuenciaCardiaca = models.PositiveIntegerField("Frecuencia Cardiaca") #frecuencia cardiaca: 40-150
    temperatura = models.DecimalField("Temperatura",max_digits=3, decimal_places=1) #30-40 grados celsius
    peso = models.PositiveIntegerField() #80-450 libras
    talla = models.DecimalField(max_digits=3, decimal_places=2) #1.3-2.5 metros
    frecuenciaRespiratoria = models.PositiveIntegerField("Frecuencia Respiratoria",null=True, blank = True) #16-28
    fechaIngreso = models.DateField(auto_now_add = True) 
    horaIngreso = models.TimeField(auto_now_add = True)
    nombreRecibido = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Tomo informacion", editable=False, default=1)
    
    #Datos al llamar este modelo: el paciente, fecha de ingreso y hora
    def __str__(self):
        return '%s %s %s' % (self.paciente, self.fechaIngreso, self.horaIngreso)
    
    # retorna la fecha en formato corto, usado en las graficas de signos vitales
    @property
    def chartdateformat(self):
        return self.fechaIngreso.strftime('%d/%m/%Y')
    
    # retorna la parte del string que contiene la presión sistólica
    def sist_as_list(self):
        lista = self.presionArterial.split("/")
        #print lista[0]
        return lista[0]
    
    # retorna la parte del string que contiene la presión diastólica
    def diast_as_list(self):
        lista = self.presionArterial.split("/")
        #print lista[1]
        return lista[1]
    
    # calcula el indice de masa corporal
    def imc_paciente(self):
        imc = ((self.peso/Decimal(2.2))/(self.talla*self.talla))
        #print imc
        resultado = Decimal(imc).quantize(Decimal("00.00"))
        #print resultado
        return resultado
    
    """
    def getpresionSistolica(self):
        #Comprobar que la presion tiene el formato mas usual: ###/##
        if (len(self.presionArterial>=6) and len(self.presionArterial[:3]==3)):
            return '%s' % (self.presionArterial[:3]) #Quiere decir que la sistolica tiene 3 cifras 
        else:
            return '%s' % (self.presionArterial[:2]) #Quiere decir que sistolica tiene solo 2 cifras
            
     # retorna solo la presion diastolica? (la de abajo)
    
    def getpresionDiastolica(self):
        #Comprobar que la presion tiene el formato mas usual: ###/##
        if (len(self.presionArterial>=6) and len(self.presionArterial[:3]==3)):
            return '%s' % (self.presionArterial[4:]) #Quiere decir que la sistolica tiene 3 cifras entonces la '/', va en el puesto 3
        else:
            return '%s' % (self.presionArterial[3:]) #Quiere decir que la sistolica tiene 2 cifras entonces la '/', va en el puesto 2
    """