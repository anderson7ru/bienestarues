from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.conf import settings
from smart_selects.db_fields import ChainedForeignKey
from datospersonalesapp.models import Paciente
from django.contrib.auth.models import User
from .validators import valid_extension
import os

# Create your models here.

"""
	A continuacion se presenta una serie de campos que son propios de un exemen de laboratorio.
	
	OA-NA-NP:Campos obligatorios-Automatico, no modifica admin o paciente
	OB-SA-NP:Campos obligatorios, cambios realizados por el administrador
	OP-SA-NP:Campos opcionales, cambios realizados por el administrador
	OB-SA-SP:Campos obligatorios, cambios realizados por paciente
	OP-SA-SP:Campos opcionales, cambios realizados por paciente
"""
NITRITOS_OPCIONES = (
    ('NEGATIVO','NEGATIVO'),
    ('POSITIVO','POSITIVO'),
    )

OPCIONES = (
    ('ESCASAS','ESCASAS'),
    ('MODERADAS','MODERADAS'),
    ('ABUNDANTES','ABUNDANTES')
    )

OPCIONES_RESTOS = (
    ('E','ESCASOS'),
    ('M','MODERADOS'),
    ('A','ABUNDANTES')
    )

COLOR = (
    ('A','AMARILLO'),
    ('C','CAFE'),
    ('N','NEGRO'),
    ('R','ROJO'),
    ('V','VERDE')
    )
    
CONSISTENCIA = (
    ('P','PASTOSA'),
    ('D','DURA'),
    ('B','BLANDA'),
    ('L','LIQUIDA')
    )

CILINDROS_OPCIONES = (
    ('NO SE OBSERVAN','NO SE OBSERVAN'),
    ('CL','CILINDRO LEUCOCIDARIO'),
    ('CG','CILINDRO GRANULOSO'),
    ('CE','CILINDRO ERITROCITARIO')
    )

CRISTALES_OPCIONES = (
    ('NO SE OBSERVAN','NO SE OBSERVAN'),
    ('SC','SULFATOS DE CALCIO'),
    ('OC','OXALATOS DE CALCIO'),
    ('UA','URATOS AMORFOS'),
    ('AU','ACIDO URICO'),
    ('FT','FOSFATOS TRIPLES'),
    ('FA','FOSFATOS AMORFOS')
    )

def generar_path(instancia, nombreArchivo):
    folder = "modelo_" + str(instancia.user)
    return os.path.join("Adjuntos", folder, nombreArchivo)

class Examen_Hematologia(models.Model):
    codExamen_Hematologia=models.AutoField(primary_key=True, null=False)#OA-NA-NP
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, verbose_name="PACIENTE", default=1, null=True, blank=True) #OB-SA-NP
    edad = models.PositiveIntegerField(default=0, null = True, blank=True)#OB-SA-NP
    fechaIngreso=models.DateTimeField("Fecha de Creacion",auto_now_add=True, null=True, blank=True) #OA-NA-NP default=timezone.now
    fechaModificacion=models.DateTimeField("Fecha de Modificacion",auto_now_add=True, null = True, blank=True) #OA-NA-NP default=timezone.now
    nombreRecibido=models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Tomo informacion", editable=False, default=1, blank=True) #OA-NA-NP
    hemoglobina = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    mcv = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    mch = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    mchc = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    hematocrito = models.PositiveIntegerField(null=True, blank=True)#OB-SA-NP
    globulosBlancos = models.PositiveIntegerField(null=True, blank=True)#OB-SA-NP
    globulosRojos = models.PositiveIntegerField(null=True, blank=True)#OB-SA-NP
    plaquetas = models.PositiveIntegerField(null=True, blank=True)#OB-SA-NP
    neutrofilos = models.PositiveIntegerField(null=True, blank=True)#OB-SA-NP
    linfocitos = models.PositiveIntegerField(null=True, blank=True)#OB-SA-NP
    monocitos = models.PositiveIntegerField(null=True, blank=True)#OB-SA-NP
    eosinofilos = models.PositiveIntegerField(null=True, blank=True)#OB-SA-NP
    basofilos = models.PositiveIntegerField(null=True, blank=True)#OB-SA-NP
    eritrosedimentacion=models.CharField("ERITROSEDIMENTACION", max_length=500, null=True, blank=True) #OB-SA-NP
    gotaGruesa=models.CharField("GOTA GRUESA", max_length=500, null=True, blank=True) #OB-SA-NP
    archivo = models.FileField(blank=True, null=True, upload_to='hematologia/')
    
    def __str__(self):
         return '%s %s' % (self.codExamen_Hematologia, self.paciente)

class Examen_Orina(models.Model):
    codExamen_Orina=models.AutoField(primary_key=True, null=False)#OA-NA-NP
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, verbose_name="PACIENTE", default=1, null=True, blank=True) #OB-SA-NP
    edad = models.PositiveIntegerField(default=0,null=True,blank=True)#OB-SA-NP
    fechaIngreso=models.DateTimeField("Fecha de Inscripcion",auto_now_add=True,null=True,blank=True) #OA-NA-NP default=timezone.now
    fechaModificacion=models.DateTimeField("Fecha de Inscripcion",auto_now_add=True, null=True,blank=True) #OA-NA-NP default=timezone.now
    nombreRecibido=models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Tomo informacion", editable=False, default=1, blank=True) #OA-NA-NP
    color=models.CharField("COLOR", max_length=25,null=True,blank=True) #OB-SA-NP
    aspecto=models.CharField("ASPECTO", max_length=25,null=True,blank=True) #OB-SA-NP
    ph = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    nitritos = models.CharField("NITRITOS", max_length=10, choices=NITRITOS_OPCIONES,null=True,blank=True) #OB-SA-NP
    densidad = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    proteinas=models.CharField("PROTEINAS", max_length=30,null=True,blank=True) #OB-SA-NP
    cetonicos=models.CharField("C. CETONICOS", max_length=30,null=True,blank=True) #OB-SA-NP
    glucosa = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    bilirrubina = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    urobilinigeno = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    leucocitos = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    hematies = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    epiteliales = models.CharField("CELULAS EPITELIALES", max_length=15, choices=OPCIONES,null=True,blank=True) #OB-SA-NP
    cristales = models.CharField("CRISTALES", max_length=20, choices=CRISTALES_OPCIONES,null=True,blank=True) #OB-SA-NP
    cilindros = models.CharField("CILINDROS", max_length=20, choices=CILINDROS_OPCIONES,null=True,blank=True) #OB-SA-NP
    sangre = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    esterasaLeucocitaria = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    bacterias = models.CharField("BACTERIAS Y LEVADURAS", max_length=15, choices=OPCIONES,null=True,blank=True) #OB-SA-NP
    observaciones= models.CharField("OBSERVACIONES",max_length=1000,null=True,blank=True)#OB-SA-NP
    archivo = models.FileField(blank=True, null=True, upload_to='orina/')
    
    def __str__(self):
         return '%s %s' % (self.codExamen_Orina, self.paciente)

class Examen_Heces(models.Model):
    codExamen_Heces=models.AutoField(primary_key=True, null=False)#OA-NA-NP
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, verbose_name="PACIENTE", default=1, null=True, blank=True) #OB-SA-NP
    edad = models.PositiveIntegerField(default=0,null=True,blank=True)#OB-SA-NP
    fechaIngreso=models.DateTimeField("Fecha de Inscripcion",auto_now_add=True,null=True,blank=True) #OA-NA-NP default=timezone.now
    fechaModificacion=models.DateTimeField("Fecha de Inscripcion",auto_now_add=True, null=True,blank=True) #OA-NA-NP default=timezone.now
    nombreRecibido=models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Tomo informacion", editable=False, default=1) #OA-NA-NP
    color=models.CharField("COLOR", max_length=25,null=True,blank=True) #OB-SA-NP
    consistencia=models.CharField("COLOR", max_length=25,null=True,blank=True) #OB-SA-NP
    mucus=models.CharField("MUCUS", max_length=20,null=True,blank=True) #OB-SA-NP
    protoActivos=models.CharField("ACTIVOS", max_length=40,null=True,blank=True) #OB-SA-NP
    protoQuistes=models.CharField("QUISTES", max_length=40,null=True,blank=True) #OB-SA-NP
    metazoarios=models.CharField("METAZOARIOS", max_length=40,null=True,blank=True) #OB-SA-NP
    hematies = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    leucocitos = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    macro=models.CharField("MACRO", max_length=40,null=True,blank=True) #OB-SA-NP
    micro=models.CharField("MICRO", max_length=40,null=True,blank=True) #OB-SA-NP
    observaciones= models.CharField("OBSERVACIONES",max_length=1000,null=True,blank=True)#OB-SA-NP
    archivo = models.FileField(blank=True, null=True, upload_to='heces/')
    
    def __str__(self):
         return '%s %s' % (self.codExamen_Heces, self.paciente)

class Examen_General(models.Model):
    codExamen_General = models.AutoField(primary_key=True, null=False)#OA-NA-NP
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, verbose_name="PACIENTE", default=1, null=True, blank=True) #OB-SA-NP
    edad = models.PositiveIntegerField(default=0,null=True,blank=True)#OB-SA-NP
    fechaIngreso=models.DateTimeField("Fecha de Inscripcion",auto_now_add=True,null=True,blank=True) #OA-NA-NP default=timezone.now
    fechaModificacion=models.DateTimeField("Fecha de Inscripcion",auto_now_add=True, null=True,blank=True) #OA-NA-NP default=timezone.now
    nombreRecibido=models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Tomo informacion", editable=False, default=1) #OA-NA-NP
    colorHeces = models.CharField("COLOR HECES", max_length=25,null=True,blank=True) #OB-SA-NP
    consistencia = models.CharField("CONSISTENCIA", max_length=25,null=True,blank=True) #OB-SA-NP
    mucus=models.CharField("MUCUS", max_length=20,null=True,blank=True) #OB-SA-NP
    protoActivos=models.CharField("ACTIVOS", max_length=40,null=True,blank=True) #OB-SA-NP
    protoQuistes=models.CharField("QUISTES", max_length=40,null=True,blank=True) #OB-SA-NP
    metazoarios=models.CharField("METAZOARIOS", max_length=40,null=True,blank=True) #OB-SA-NP
    hematiesHeces = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    leucocitosHeces = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    macro = models.CharField("MACRO", max_length=25,null=True,blank=True) #OB-SA-NP
    micro = models.CharField("MICRO", max_length=25,null=True,blank=True) #OB-SA-NP
    colorOrina=models.CharField("COLOR", max_length=25,null=True,blank=True) #OB-SA-NP
    aspecto=models.CharField("ASPECTO", max_length=25,null=True,blank=True) #OB-SA-NP
    ph = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    nitritos = models.CharField("NITRITOS", max_length=10, choices=NITRITOS_OPCIONES,null=True,blank=True) #OB-SA-NP
    densidad = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    proteinas = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    cetonicos=models.CharField("C. CETONICOS", max_length=30,null=True,blank=True) #OB-SA-NP
    glucosa = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    bilirrubina = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    urobilinigeno = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    leucocitosOrina = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    hematiesOrina = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    epiteliales = models.CharField("CELULAS EPITELIALES", max_length=15, choices=OPCIONES,null=True,blank=True) #OB-SA-NP
    cristales = models.CharField("CRISTALES", max_length=20, choices=CRISTALES_OPCIONES,null=True,blank=True) #OB-SA-NP
    cilindros = models.CharField("CILINDROS", max_length=20, choices=CILINDROS_OPCIONES,null=True,blank=True) #OB-SA-NP
    sangre=models.CharField("SANGRE", max_length=30,null=True,blank=True) #OB-SA-NP
    esterasaLeucocitaria=models.CharField("ESTERASA LEUCOCITARIA", max_length=30,null=True,blank=True) #OB-SA-NP
    bacterias = models.CharField("BACTERIAS", max_length=15, choices=OPCIONES,null=True,blank=True) #OB-SA-NP
    levaduras = models.CharField("LEVADURAS", max_length=15, choices=OPCIONES,null=True,blank=True) #OB-SA-NP
    otros= models.CharField("OTROS",max_length=500,null=True,blank=True)#OB-SA-NP
    hematocrito = models.PositiveIntegerField(null=True, blank=True)#OB-SA-NP
    hemoglobina = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    serologia=models.CharField("SEROLOGIA", max_length=500,null=True,blank=True) #OB-SA-NP
    archivo = models.FileField(blank=True, null=True, upload_to='GeneralNuevoIngreso/')

    def __str__(self):
         return '%s %s' % (self.codExamen_General, self.paciente)

class Examen_Quimica_Sanguinea(models.Model):
    codExamen_Quimica = models.AutoField(primary_key=True, null=False)#OA-NA-NP
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, verbose_name="PACIENTE", default=1, null=True, blank=True) #OB-SA-NP
    edad = models.PositiveIntegerField(default=0,null=True,blank=True)#OB-SA-NP
    fechaIngreso=models.DateTimeField("Fecha de Inscripcion",auto_now_add=True,null=True,blank=True) #OA-NA-NP default=timezone.now
    fechaModificacion=models.DateTimeField("Fecha de Inscripcion",auto_now_add=True, null=True,blank=True) #OA-NA-NP default=timezone.now
    nombreRecibido=models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Tomo informacion", editable=False, default=1) #OA-NA-NP
    glucosa = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    glucosaPospandrial = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    colesterol = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    trigliceridos = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    acidoUrico = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    creatinina = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    hdl = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    ldl = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    tgo = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    tgp = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    bilirrubinaTotal = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    bilirrubinaDirecta = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    bilirrubinaIndirecta = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)#OB-SA-NP
    tiempoProtrombina = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    tiempoTromboplastina = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    tiempoSangramiento = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    tiempoCoagulacion = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    eritrosedimentacion = models.PositiveIntegerField(null=True,blank=True)#OB-SA-NP
    glucosaAjustada=models.CharField(max_length=25,null=True,blank=True) #OB-SA-NP
    pospandrialAjustada=models.CharField(max_length=25,null=True,blank=True) #OB-SA-NP
    colesterolAjustada=models.CharField(max_length=25,null=True,blank=True) #OB-SA-NP
    trigliceridosAjustada=models.CharField(max_length=25,null=True,blank=True) #OB-SA-NP
    uricoAjustada=models.CharField(max_length=25,null=True,blank=True) #OB-SA-NP
    creatininaAjustada=models.CharField(max_length=25,null=True,blank=True) #OB-SA-NP
    hdlAjustada=models.CharField(max_length=25,null=True,blank=True) #OB-SA-NP
    ldlAjustada=models.CharField(max_length=25,null=True,blank=True) #OB-SA-NP
    tgoAjustada=models.CharField(max_length=25,null=True,blank=True) #OB-SA-NP
    tgpAjustada=models.CharField(max_length=25,null=True,blank=True) #OB-SA-NP
    bTotalAjustada=models.CharField(max_length=25,null=True,blank=True) #OB-SA-NP
    bDirectaAjustada=models.CharField(max_length=25,null=True,blank=True) #OB-SA-NP
    bIndirectaAjustada=models.CharField(max_length=25,null=True,blank=True) #OB-SA-NP
    protrombinaAjustada=models.CharField(max_length=25,null=True,blank=True) #OB-SA-NP
    tromboplastinaAjustada=models.CharField(max_length=25,null=True,blank=True) #OB-SA-NP
    sangramientoAjustada=models.CharField(max_length=25,null=True,blank=True) #OB-SA-NP
    coagulacionAjustada=models.CharField(max_length=25,null=True,blank=True) #OB-SA-NP
    eritrosedimentacionAjustada=models.CharField(max_length=25,null=True,blank=True) #OB-SA-NP
    archivo = models.FileField(blank=True, null=True, upload_to='QuimicaSanguinea/')

    def __str__(self):
         return '%s %s' % (self.codExamen_Quimica, self.paciente)

class Examen_Especiales(models.Model):
    codExamen_Especiales = models.AutoField(primary_key=True, null=False)#OA-NA-NP
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, verbose_name="PACIENTE", default=1, null=True, blank=True) #OB-SA-NP
    edad = models.PositiveIntegerField(default=0,null=True,blank=True)#OB-SA-NP
    fechaIngreso=models.DateTimeField("Fecha de Inscripcion",auto_now_add=True,null=True,blank=True) #OA-NA-NP default=timezone.now
    fechaModificacion=models.DateTimeField("Fecha de Inscripcion",auto_now_add=True, null=True,blank=True) #OA-NA-NP default=timezone.now
    nombreRecibido=models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Tomo informacion", editable=False, default=1) #OA-NA-NP
    tipoExamen= models.CharField("TIPO DE EXAMEN",max_length=25,null=True,blank=True)#OB-SA-NP
    resultado= models.CharField("RESULTADOS",max_length=100,null=True,blank=True)#OB-SA-NP
    archivo = models.FileField(blank=True, null=True, upload_to='PruebasEspeciales/')

    def __str__(self):
         return '%s %s' % (self.codExamen_Especiales, self.paciente)