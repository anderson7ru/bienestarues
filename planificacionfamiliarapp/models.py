# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

# apps externas
from datospersonalesapp.models import Paciente

""" 
Datos para planificacion familiar:
1. datospersonales\models. Tabla: Paciente.
Esta tabla contiene una serie de informacion que se necesitan para 
planificacion familiar como:
-codigoPaciente es la PK de paciente
-apellidoPrimero, apellidoSegundo, nombrePrimero, nombreSegundo, nombre 
completo del paciente.
-estadoCivil 
-direccion, codDepartamento, codMunicipio Direccion completa del paciente
"""

ELECCIONES=(
    ('S','Si'),
    ('N','No'),
    )
NA_ELECCIONES=(
    ('N','Normal'),
    ('A','Anormal'),
    )
CICLO_ELECCIONES=(
	('R','Regulares'),
	('I','Irregulares'),
	)
SANGRADO_ELECCIONES=(
	('E','Escasos'),
	('M','Moderados'),
	('A','Abundantes'),
	)
POSICION_ELECCIONES=(
	('A','Anteflexion'),
	('M','Retroflexion'),
	('P','Retroversion'),
	)
ANTICONCEPTIVOS_ELECCIONES=(
    ('O','Oral'),
    ('D','DIU'),
    ('I','Inyectable'),
    ('C','Condones'),
    ('N','Norplant'),
    ('E','Esterilizaciones'),
    ('T','Otros'),
    )
ULTIMOEMBARAZO_ELECCIONES=(
	('A','Aborto'),
	('V','Parto Vaginal'),
	('O','Parto Operatorio'),
	)
CONSULTA_ELECCIONES=(
	('N','Control Normal'),
	('M','Morbilidad'),
	('F','Falla de metodo'),
	)
TIEMPO_ELECCIONES=(
	('N','Ninguno'),
	('D','Dias'),
	('S','Semanas'),
	('M','Meses'),
	('A','Anos'),
	)
	
# Tabla donde se encuentran datos para la inscripcion de la paciente
class PacienteInscripcion(models.Model):
	codigoPlanificacion = models.AutoField(primary_key=True, null=False)
	#1.Datos Generales del paciente
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, limit_choices_to={'sexo':'F','estadoExpediente':'A'},verbose_name="No expediente", null=False)
	edad = models.PositiveIntegerField() #Edad de toma de inscripcion
	aniosEscolaridad =  models.PositiveIntegerField("Anios de escolaridad")
	#tipo de inscripcion
	primeraVida = models.CharField("1era vez en la vida", max_length=1, choices=ELECCIONES, default='S')
	primeraInstitucion = models.CharField("1era vez en la institucion", max_length=1, choices=ELECCIONES, default='S')
	#2.Antecedentes obstetricos
	embarazos  = models.PositiveIntegerField(default=0)
	partosTermino = models.PositiveIntegerField("Partos a Termino", default=0)
	prematuros = models.PositiveIntegerField(default=0)
	abortos = models.PositiveIntegerField(default=0)
	vivos = models.PositiveIntegerField(default=0)
	nacidosVivos = models.PositiveIntegerField("Nacidos Vivos", default=0)
	nacidosMuertos = models.PositiveIntegerField("Nacidos Muertos", default=0)
	partoVaginal = models.PositiveIntegerField("Partos via Vaginal", default=0)
	partoOpereratorio = models.PositiveIntegerField("Partos Operatorios", default=0)
	fup = models.DateField("FUP",help_text="DD/MM/YYYY", null=True, blank=True)
	lactando = models.CharField("Esta Lactando", max_length=1, choices=ELECCIONES, default='N')
	#Terminacion del ultimo embarazo
	ueProductoVivo = models.CharField("Producto Vivo", max_length=1, choices=ELECCIONES, null=True, blank=True)
	ueTerminacion = models.CharField(" ", max_length=1, choices=ULTIMOEMBARAZO_ELECCIONES, null=True, blank=True)
	#3.Antecedentes ginecologicos
	menarquia = models.PositiveIntegerField(help_text="anios")
	fur = models.DateField("FUR",help_text="DD/MM/YYYY")
	edadPrimeraVez = models.PositiveIntegerField("Edad del primer coito",help_text="anios")
	dismenorrea = models.CharField("Dismenorrea", max_length=1, choices=ELECCIONES, default='N')
	cicloMenstrual = models.CharField("Ciclos Menstruales", max_length=1, choices=CICLO_ELECCIONES, default='R')
	duracionCiclo = models.PositiveIntegerField("Duracion del ciclo",help_text="dias")
	sangramientos = models.CharField("Sangramientos", max_length=1, choices=SANGRADO_ELECCIONES, default='M')
	duracionSangramiento = models.PositiveIntegerField("Duracion del sangramiento",help_text="dias")
	fechaPap = models.DateField("Fecha del ultimo PAP",help_text="DD/MM/YYYY", null=True, blank=True)
	resultado = models.CharField(max_length=100, null=True, blank=True)
	agObservaciones = models.CharField("Observaciones", max_length=500, null=True, blank=True)
	#4.Antecedentes personales
	cefaleaIntensa = models.CharField("Cefalea Intensa", max_length=1, choices=ELECCIONES, default='N')
	trastCardiovascular = models.CharField("Transtorno Cardiovascular", max_length=1, choices=ELECCIONES, default='N')
	hta = models.CharField("HTA", max_length=1, choices=ELECCIONES, default='N')
	diabetes = models.CharField(max_length=1, choices=ELECCIONES, default='N')
	trastHepaticos = models.CharField("Transtornos Hepaticos", max_length=1, choices=ELECCIONES, default='N')
	trastConvulsivo = models.CharField("Transtorno Convulsivo", max_length=1, choices=ELECCIONES, default='N')
	varices = models.CharField(max_length=1, choices=ELECCIONES, default='N')
	tabaquismo = models.CharField(max_length=1, choices=ELECCIONES, default='N')
	cirugiaPelv = models.CharField("Cirugia Pelvica", max_length=1, choices=ELECCIONES, default='N')
	infeccionPelv = models.CharField("Infeccion Pelvica", max_length=1, choices=ELECCIONES, default='N')
	alergias = models.CharField(max_length=1, choices=ELECCIONES, default='N')
	vih = models.CharField("VIH+", max_length=1, choices=ELECCIONES, default='N')
	its = models.BooleanField("ITS", default = False)
	apObservaciones = models.CharField("Observaciones", max_length=500, null=True, blank=True)
	#metodos anticonceptivos
	metAnticonceptivos = models.CharField("Ha utilizado metodos anticonceptivos?", max_length=1, choices=ELECCIONES, default='N')
	metUtilizado = models.CharField("Metodo Utilizado", max_length=60, null=True, blank=True)
	metTiempo = models.PositiveIntegerField("Por cuanto tiempo", help_text="semanas", null=True, blank=True)
	metLapso = models.CharField(" ", max_length=1, choices=TIEMPO_ELECCIONES, default='N')
	metJustificar = models.CharField("Porque dejo de usarlo", max_length=100, null=True, blank=True)
	metLugar = models.CharField("Donde lo obtuvo", max_length=60, null=True, blank=True)
	#5.Examen fisico
	temperatura = models.DecimalField(max_digits=3, decimal_places=1) #30-40 grados celsius
	pulso = models.PositiveIntegerField() #frecuencia cardiaca: 40-150
	peso = models.PositiveIntegerField() #80-450 libras
	presionArterial = models.CharField("T.A.",max_length=7)#40/40-300/200 mmHg
	#datos extra de examen fisico
	naCabeza = models.CharField("Cabeza", max_length=1, choices=NA_ELECCIONES, default='N')
	cabeza = models.CharField(" ", max_length=100, null=True, blank=True)
	naCuello = models.CharField("Cuello", max_length=1, choices=NA_ELECCIONES, default='N')
	cuello = models.CharField(" ", max_length=100, null=True, blank=True)
	naMamas = models.CharField("Mamas", max_length=1, choices=NA_ELECCIONES, default='N')
	mamas = models.CharField(" ", max_length=100, null=True, blank=True)
	naTorax = models.CharField("Torax", max_length=1, choices=NA_ELECCIONES, default='N')
	torax = models.CharField(" ", max_length=100, null=True, blank=True)
	naAbdomen = models.CharField("Abdomen", max_length=1, choices=NA_ELECCIONES, default='N')
	abdomen = models.CharField(" ", max_length=100, null=True, blank=True)
	naMiembros = models.CharField("Miembros", max_length=1, choices=NA_ELECCIONES, default='N')
	miembros = models.CharField(" ", max_length=100, null=True, blank=True)
	#6.Examen ginecologico
	genitalesExternos = models.CharField("Genitales Externos", max_length=1, choices=NA_ELECCIONES, default='N')
	cistocele = models.CharField(max_length=1, choices=ELECCIONES, default='N')
	gradoCistocele = models.PositiveIntegerField("grado", null=True, blank=True)
	rectocele = models.CharField(max_length=1, choices=ELECCIONES, default='N')
	gradoRectocele = models.PositiveIntegerField("grado", null=True, blank=True)
	prolapsoUterino = models.CharField("Prolapso Uterino", max_length=1, choices=ELECCIONES, default='N')
	gradoProlapsoUterino = models.PositiveIntegerField("grado", null=True, blank=True)
	vagina = models.CharField(max_length=1, choices=NA_ELECCIONES, default='N')
	snSecrecionVagina = models.CharField("Secrecion en vagina", max_length=1, choices=ELECCIONES, default='N')
	secrecionVagina = models.CharField(" ", max_length=100, null=True, blank=True)
	#cuello uterino
	cuPalpacion = models.CharField("Cuello Uterino Palpacion", max_length=1, choices=NA_ELECCIONES, default='N')
	cuConsistencia = models.CharField("Consistencia", max_length=1, choices=NA_ELECCIONES, default='N')
	cuMovilidad = models.CharField("Movilidad", max_length=1, choices=NA_ELECCIONES, default='N')
	cuDolorMov = models.CharField("Dolor a la movilizacion", max_length=1, choices=ELECCIONES, default='N')
	sangrarTacto = models.CharField("Sangra al contacto", max_length=1, choices=ELECCIONES, default='N')
	tomaPap = models.CharField("Toma PAP", max_length=1, choices=ELECCIONES, default='N')
	cuObservaciones = models.CharField("Observaciones", max_length=100, null=True, blank=True)
	#utero
	uteroPosicion = models.CharField("Utero Posicion", max_length=1, choices=POSICION_ELECCIONES, default='A')
	uTamano = models.CharField("Tamano", max_length=1, choices=NA_ELECCIONES, default='N')
	uConsistencia = models.CharField("Consistencia", max_length=1, choices=NA_ELECCIONES, default='N')
	uMovilidad = models.CharField("Movilidad", max_length=1, choices=NA_ELECCIONES, default='N')
	uDolorMov = models.CharField("Dolor a la movilizacion", max_length=1, choices=ELECCIONES, default='N')
	usnTumores = models.CharField("Tumores", max_length=1, choices=ELECCIONES, default='N')
	uTumores = models.CharField(" ", max_length=100, null=True, blank=True)
	#Anexos
	anexosLibres = models.CharField("Anexos Libres", max_length=1, choices=ELECCIONES, default='N')
	engrosados = models.CharField(max_length=1, choices=ELECCIONES, default='N')
	aDolorPalpitacion = models.CharField("Dolor a la palpacion", max_length=1, choices=ELECCIONES, default='N')
	asnTumores = models.CharField("Tumores", max_length=1, choices=ELECCIONES, default='N')
	aTumores = models.CharField(" ", max_length=100, null=True, blank=True)
	fondoSaco = models.CharField("Fondo de saco", max_length=1, choices=NA_ELECCIONES, default='N')
	#7.Metodo indicado
	fechaInicioMetodo = models.DateField("Fecha de inicio de metodo", null=True, blank=True)
	anticonceptivo =  models.CharField(max_length=1, choices=ANTICONCEPTIVOS_ELECCIONES, null=True, blank=True)
	miONombre = models.CharField("Nombre",max_length=15, null=True, blank=True)
	miOtros = models.CharField("Otros",max_length=15, null=True, blank=True)
	diagnostico = models.CharField(max_length=100, null=True, blank=True)
	indicaciones = models.CharField(max_length=100, null=True, blank=True)
	#8.Responsable
	#proximaConsulta = models.PositiveIntegerField("Proxima consulta", default=0) #Modificacion para dejar la gestion de fecha a control de citas
	#proximaConsultaLapso =  models.CharField(" ", max_length=1, choices=TIEMPO_ELECCIONES, default='N') 
	fechaIngreso = models.DateTimeField("Fecha de Inscripcion",auto_now_add=True)
	#Extraido determinado por la sesion actual
	nombreResponsable = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Nombre Responsable", editable=False, default=1)
	
	def __str__(self):
		return '%s' % (self.paciente)

class PacienteSubSecuentePF(models.Model):
	codigoPlanificacionSub = models.AutoField(primary_key=True, null=False)
	pacienteInscrito = models.ForeignKey(PacienteInscripcion, on_delete=models.CASCADE, verbose_name="Paciente", null=False)
	edad = models.PositiveIntegerField() #Edad que tenia cuando paso a consulta
	peso = models.PositiveIntegerField() #80-450lb
	presionArterial = models.CharField("PA",max_length=7)#40/40-300/200mmHg
	metUtilizado = models.CharField("Metodo Utilizado", max_length=60, null=True, blank=True)
	metTiempo = models.PositiveIntegerField("Tiempo de uso", null=True, blank=True)
	metLapso = models.CharField(" ", max_length=1, choices=TIEMPO_ELECCIONES, default='N')
	histHallazgos = models.CharField("Historia y hallazgos", max_length=500, null=True, blank=True)
	metContinuacion = models.CharField("Continua con el metodo", max_length=1, choices=ELECCIONES, default='S')
	nombreCambio = models.CharField("Cambia a",max_length=50, null=True, blank=True)
	motivoCambio = models.CharField("Motivo del cambio",max_length=100, null=True, blank=True)
	diagnostico = models.CharField(max_length=100, null=True, blank=True)
	tomaPap = models.CharField("Toma PAP", max_length=1, choices=ELECCIONES, default='N')
	tipoConsulta = models.CharField("Tipo de Consulta", max_length=1, choices=CONSULTA_ELECCIONES, default='N')
	indicaciones = models.CharField(max_length=100, null=True, blank=True)
	#proximaConsulta = models.PositiveIntegerField("Proxima consulta", default=0) #Modificacion para dejar la gestion de fecha a control de citas
	#proximaConsultaLapso =  models.CharField(" ", max_length=1, choices=TIEMPO_ELECCIONES, default='N') 
	fechaIngreso = models.DateTimeField("Fecha",auto_now_add=True)
	nombreResponsable = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Nombre Responsable", editable=False, default=1)
	
	def __str__(self):
		return '%s %s' % (self.pacienteInscrito, self.tipoConsulta)