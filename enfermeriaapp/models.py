from __future__ import unicode_literals

from django.db import models
from datospersonalesapp.models import Paciente
from empleadosapp.models import Doctor

# Create your models here.
# Esta clase representa la cola de pacientes para pasar consulta medica
class Cola_Consulta(models.Model):
    idCola = models.AutoField(primary_key=True, null=False)#OA-NA-NP
    nit = models.CharField("NIT", max_length=17,unique=True) #Este es el mio (Luis) para modificacion de BD
    idDoctor = models.ForeignKey(Doctor,on_delete=models.SET_NULL, verbose_name="Doctor", default=1, null=True, blank=True)#OB-SA-NP
    hora = models.TimeField(null=True, blank=True)#OA-NA-NP
    prioridad = models.CharField("Prioridad", max_length=6, null=True, blank=True, default="Normal")
    def __str__(self):
        return '%s %s %s %s' % (self.idCola, self.nit, self.idDoctor, self.hora)#self.idCola

class Cola_Enfermeria(models.Model):
    idCola = models.AutoField(primary_key=True, null=False)#OA-NA-NP
    idPaciente = models.ForeignKey(Paciente,on_delete=models.SET_NULL, verbose_name="Paciente", default=1, null=True, blank=True)#OB-SA-NP
    hora = models.TimeField(null=True, blank=True)#OA-NA-NP
    prioridad = models.CharField("Prioridad", max_length=6, null=True, blank=True, default="Normal")
    def __str__(self):
        return '%s %s %s' % (self.idCola, self.idPaciente, self.hora)#self.idCola
   