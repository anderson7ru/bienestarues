from django.db import models
from datospersonalesapp.models import Paciente
from empleadosapp.models import Doctor
from django.conf import settings
# Create your models here.

#Elecciones para las tecnicas en el proceso terapeutico
Elecciones_Tecnicas = (
    ('observacion','Observacion'),
    ('entrevista','Entrevista'),
    ('prueba','Prueba Pca'),
    ('conv','Conv. Terapeutica'),
    ('relajacion','Tecnica de relajacion'),
    ('musico','Musicoterapia'),
)

# Modelo de clase para expediente de psicologia
# No se bien si agregarle el psicologo, aunque quiza seria eso de nombreRecibido ya que seria con el usuario del psicologo
class Psicologia(models.Model):
    codPsicologia = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE,limit_choices_to={'estadoExpediente':'A'},verbose_name="No expediente", null=False)
    numero_hijos = models.PositiveSmallIntegerField('Numero de Hijos',default=0)
    profesion = models.CharField('Profesion u Ocupacion',max_length=60)
    fecha_primeraConsulta = models.DateField("Fecha de Primera Consulta",help_text="DD/MM/AAAA")
    direccionResponsable = models.CharField("Direccion del Responsable",max_length=250)
    referido = models.ForeignKey(Doctor,on_delete=models.CASCADE,verbose_name="Referido por")
    fecha = models.DateField("Fecha",auto_now_add=True)
    religion = models.CharField("Religion",max_length=50)
    familia = models.PositiveSmallIntegerField("Cuantos componen la familia")
    motivo = models.TextField("Motivo de Consulta",blank=False,null=False)
    antecedentes = models.TextField("Antecedentes del Problema",blank=False,null=False)
    apariencia = models.CharField("Apariencia externa",max_length=120)
    voz = models.CharField("Voz",max_length=30)
    patrones = models.CharField("Patrones de Habla",max_length=50)
    expresionesF = models.CharField("Expresiones Faciales",max_length=120)
    ademanes = models.CharField("Ademanes",max_length=120)
    actitudes_tx = models.TextField("Actitudes hacia el TX")
    impresion_dx = models.TextField("Impresion DX")
    plan_tx = models.TextField("Plan de TX")
    pronostico = models.TextField("Pronostico")
    fecha_proximaCita = models.DateField("Fecha de Proxima Cita",help_text="DD/MM/AAAA")
    nombreRecibido = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Tomo informacion", editable=False, default=1)
    
    def __str__(self):
        return str(self.codPsicologia)

# Modelo de clase para el cuadro del Proceso terapeutico
# Se puede llegar hasta paciente por medio de la FK codPsicologia,o No se si agregarle tambien paciente como FK
class ProcesoTerapeutico(models.Model):
    codProcesoTerapeutico = models.AutoField(primary_key=True)
    codPsicologia = models.ForeignKey(Psicologia,on_delete=models.CASCADE,null=False)
    fecha = models.DateField("Fecha",auto_now_add=True)
    objetivo = models.TextField("Objetivo Terapeutico")
    tecnicas = models.CharField("Tecnicas",max_length=12,choices=Elecciones_Tecnicas,default='observacion')
    observaciones = models.TextField("Observaciones")
    nombreRecibido = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Tomo informacion", editable=False, default=1)
    
    
    def __str__(self):
        return str(self.codProcesoTerapeutico)
    
class RegistroAvance(models.Model):
    codRegistroAvance = models.AutoField(primary_key=True)
    codProcesoTerapeutico = models.ForeignKey(ProcesoTerapeutico,on_delete=models.CASCADE,null=False)
    fechaRegistro = models.DateField("fechaRegistro",auto_now_add=True)
    paciente = models.TextField("Paciente")
    psicologo = models.TextField("Psicologo")
    nombreRecibido = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Tomo informacion", editable=False, default=1)
    
    
    def __str__(self):
        return str(self.codRegistroAvance)