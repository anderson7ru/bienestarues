# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, Textarea
from smart_selects.form_fields import ChainedModelChoiceField

# apps internas y externas
from planificacionfamiliarapp.models import PacienteInscripcion, PacienteSubSecuentePF
from datospersonalesapp.models import Paciente
import re

ELECCIONES=(
    ('S','Si'),
    ('N','No'),
    )
NA_ELECCIONES=(
    ('N','N'),
    ('A','A'),
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
	('A','A'),
	('M','M'),
	('P','P'),
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
	
class PlanificacionFamForm(ModelForm):
	#El model a utilizar, con los elementos visibles	
	class Meta:
		model = PacienteInscripcion 
		fields = ['paciente','aniosEscolaridad','primeraVida','primeraInstitucion','embarazos','partosTermino','prematuros','abortos','vivos',
		'nacidosVivos','nacidosMuertos','partoVaginal','partoOpereratorio','fup','lactando','ueProductoVivo','ueTerminacion','menarquia','fur',
		'edadPrimeraVez','dismenorrea','cicloMenstrual','duracionCiclo','sangramientos',
		'duracionSangramiento','fechaPap','resultado','agObservaciones','cefaleaIntensa','trastCardiovascular','hta','diabetes',
		'trastHepaticos','trastConvulsivo','varices','tabaquismo','cirugiaPelv','infeccionPelv','alergias','vih','its','apObservaciones',
		'metAnticonceptivos','metUtilizado','metTiempo','metLapso','metJustificar','metLugar','temperatura','pulso','peso','presionArterial','naCabeza',
		'cabeza','naCuello','cuello','naMamas','mamas','naTorax','torax','naAbdomen','abdomen','naMiembros','miembros','genitalesExternos',
		'cistocele','gradoCistocele','rectocele','gradoRectocele','prolapsoUterino','gradoProlapsoUterino','vagina','snSecrecionVagina',
		'secrecionVagina','cuPalpacion','cuConsistencia','cuMovilidad','cuDolorMov','sangrarTacto','tomaPap','cuObservaciones',
		'uteroPosicion','uTamano','uConsistencia','uMovilidad','uDolorMov','usnTumores','uTumores','anexosLibres','engrosados','aDolorPalpitacion',
		'asnTumores','aTumores','fondoSaco','fechaInicioMetodo','anticonceptivo','miONombre','miOtros','diagnostico','indicaciones','proximaConsulta','proximaConsultaLapso']
		
	paciente = forms.ModelChoiceField(widget=forms.Select(attrs={'name':'paciente','class':'selectpicker','data-live-search':'true'}),queryset=Paciente.objects.filter(sexo='F',estadoExpediente='A').exclude(codigoPaciente__in=PacienteInscripcion.objects.all().values_list('paciente_id')),label="Paciente",help_text="(*)")
	aniosEscolaridad = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'aniosEscolaridad','class':'form-control','min':'1','max':'20'}),label="de escolaridad",help_text="(*)")
	primeraVida = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='S' ,label="1era vez en la vida")
	primeraInstitucion = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='S',label="1era vez en la institucion")
	embarazos = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'embarazos','class':'form-control','min':'0','max':'10','value': '0'}),label="Embarazos")
	partosTermino = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'partosTermino','class':'form-control','min':'0','max':'10','value': '0'}),label="Parto a termino")
	prematuros = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'prematuros','class':'form-control','min':'0','max':'10','value': '0'}),label="Prematuros")
	abortos = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'abortos','class':'form-control','min':'0','max':'10','value': '0'}),label="Abortos")
	vivos = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'vivos','class':'form-control','min':'0','max':'10','value': '0'}),label="Vivos")
	nacidosVivos = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'nacidosVivos','class':'form-control','min':'0','max':'10','value': '0'}),label="Nacidos vivos")
	nacidosMuertos = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'nacidosMuertos','class':'form-control','min':'0','max':'10','value': '0'}),label="Nacidos Muertos")
	partoVaginal = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'partoVaginal','class':'form-control','min':'0','max':'10','value': '0'}),label="Partos vaginal")
	partoOpereratorio = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'partoOpereratorio','class':'form-control','min':'0','max':'10','value': '0'}),label="Partos operatorios")
	fup = forms.DateField(widget=forms.DateInput(attrs={'name':'fup','data-date-format':'DD/MM/YYYY','class':'form-control','id':'fup'}),label="FUP",required=False)
	lactando = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Esta Lactando")
	ueProductoVivo = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES,label="Producto Vivo",required=False)
	ueTerminacion = forms.ChoiceField(widget=forms.RadioSelect, choices=ULTIMOEMBARAZO_ELECCIONES,label=" ",required=False)
	menarquia = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'menarquia','class':'form-control','min':'8','max':'25'}),label="Menarquia",help_text="(*)")
	fur = forms.DateField(widget=forms.DateInput(attrs={'name':'fur','data-date-format':'DD/MM/YYYY','class':'form-control','id':'fur'}),label="FUR",help_text="(*)")
	edadPrimeraVez = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'edadPrimeraVez','class':'form-control','min':'8','max':'25'}),label="Edad del primer coito",help_text="(*)")
	dismenorrea = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Dismenorrea")
	cicloMenstrual = forms.ChoiceField(widget=forms.RadioSelect, choices=CICLO_ELECCIONES, initial='R',label="Ciclos Menstruales")
	duracionCiclo = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'duracionCiclo','class':'form-control','min':'10','max':'100'}),label="Duracion del ciclo",help_text="(*)")
	sangramientos = forms.ChoiceField(widget=forms.RadioSelect, choices=SANGRADO_ELECCIONES, initial='M',label="Sangramientos")
	duracionSangramiento = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'duracionSangramiento','class':'form-control','min':'1','max':'30'}),label="Duracion del sangramiento",help_text="(*)")
	fechaPap = forms.DateField(widget=forms.DateInput(attrs={'name':'fechaPap','data-date-format':'DD/MM/YYYY','class':'form-control','id':'fechaPap'}),label="Fecha del ultimo PAP",required=False)
	resultado = forms.CharField(widget=forms.Textarea(attrs={'name':'resultado','cols':'50','rows':'1','maxlength':'100','class':'form-control'}),label="Resultado",required=False)
	agObservaciones = forms.CharField(widget=forms.Textarea(attrs={'name':'agObservaciones','cols':'40','rows':'2','maxlength':'500','class':'form-control'}),label="Observaciones",required=False)
	cefaleaIntensa = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Cefalea Intensa")
	trastCardiovascular = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Transtorno Cardiovascular")
	hta = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="HTA")
	diabetes = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Diabetes")
	trastHepaticos = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Transtornos Hepaticos")
	trastConvulsivo = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Transtorno Convulsivo")
	varices = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Varices")
	tabaquismo = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Tabaquismo")
	cirugiaPelv = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Cirugia Pelvica")
	infeccionPelv = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Infeccion Pelvica")
	alergias = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Alergias")
	vih = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="VIH+")
	apObservaciones = forms.CharField(widget=forms.Textarea(attrs={'name':'apObservaciones','cols':'40','rows':'2','maxlength':'500','class':'form-control'}),label="Observaciones",required=False)
	metAnticonceptivos = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Ha utilizado metodos anticonceptivos?")
	metUtilizado = forms.CharField(widget=forms.TextInput(attrs={'name':'metUtilizado','maxlength':'60','class':'form-control'}),label="Metodo Utilizado",required=False)
	metTiempo = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'metTiempo','class':'form-control','min':'1','max':'100'}),label="Por cuanto tiempo",required=False)
	metLapso = forms.CharField(max_length=1,widget=forms.Select(attrs={'name':'metLapso','class':'form-control'}, choices=TIEMPO_ELECCIONES),label=" ",help_text="(*)")
	metJustificar = forms.CharField(widget=forms.TextInput(attrs={'name':'metJustificar','maxlength':'100','class':'form-control'}),label="Porque dejo de usarlo",required=False)
	metLugar = forms.CharField(widget=forms.TextInput(attrs={'name':'metLugar','maxlength':'60','class':'form-control'}),label="Donde lo obtuvo",required=False)
	temperatura = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'temperatura','class':'form-control','min':'30.0','max':'40.0'}),label="Temperatura",help_text="(*)")
	pulso = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'pulso','class':'form-control','min':'40','max':'150'}),label="Pulso",help_text="(*)")
	peso = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'peso','class':'form-control','min':'80','max':'450'}),label="Peso",help_text="(*)")
	presionArterial = forms.CharField(widget=forms.TextInput(attrs={'name':'presionArterial','maxlength':'7','class':'form-control','placeholder':'###/##'}),label="T.A.",help_text="(*)")
	naCabeza  = forms.ChoiceField(widget=forms.RadioSelect, choices=NA_ELECCIONES, initial='N',label="Cabeza")
	cabeza = forms.CharField(widget=forms.TextInput(attrs={'name':'cabeza','maxlength':'100','class':'form-control'}),label=" ",required=False)
	naCuello  = forms.ChoiceField(widget=forms.RadioSelect, choices=NA_ELECCIONES, initial='N',label="Cuello")
	cuello = forms.CharField(widget=forms.TextInput(attrs={'name':'cuello','maxlength':'100','class':'form-control'}),label=" ",required=False)
	naMamas  = forms.ChoiceField(widget=forms.RadioSelect, choices=NA_ELECCIONES, initial='N',label="Mamas")
	mamas = forms.CharField(widget=forms.TextInput(attrs={'name':'mamas','maxlength':'100','class':'form-control'}),label=" ",required=False)
	naTorax  = forms.ChoiceField(widget=forms.RadioSelect, choices=NA_ELECCIONES, initial='N',label="Torax")
	torax = forms.CharField(widget=forms.TextInput(attrs={'name':'torax','maxlength':'100','class':'form-control'}),label=" ",required=False)
	naAbdomen  = forms.ChoiceField(widget=forms.RadioSelect, choices=NA_ELECCIONES, initial='N',label="Abdomen")
	abdomen = forms.CharField(widget=forms.TextInput(attrs={'name':'abdomen','maxlength':'100','class':'form-control'}),label=" ",required=False)
	naMiembros  = forms.ChoiceField(widget=forms.RadioSelect, choices=NA_ELECCIONES, initial='N',label="Miembros")
	miembros = forms.CharField(widget=forms.TextInput(attrs={'name':'miembros','maxlength':'100','class':'form-control'}),label=" ",required=False)
	genitalesExternos  = forms.ChoiceField(widget=forms.RadioSelect, choices=NA_ELECCIONES, initial='N',label="Genitales Externos")
	cistocele = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Cistocele")
	gradoCistocele = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'gradoCistocele','class':'form-control','min':'0','max':'3','value': '0'}),label="grado",required=False)
	rectocele = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Rectocele")
	gradoRectocele = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'gradoRectocele','class':'form-control','min':'0','max':'3','value': '0'}),label="grado",required=False)
	prolapsoUterino = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Prolapso Uterino")
	gradoProlapsoUterino = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'gradoProlapsoUterino','class':'form-control','min':'0','max':'3','value': '0'}),label="grado",required=False)
	vagina  = forms.ChoiceField(widget=forms.RadioSelect, choices=NA_ELECCIONES, initial='N',label="Vagina")
	snSecrecionVagina = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Secrecion en vagina")
	secrecionVagina = forms.CharField(widget=forms.TextInput(attrs={'name':'secrecionVagina','maxlength':'100','class':'form-control'}),label=" ",required=False)
	cuPalpacion  = forms.ChoiceField(widget=forms.RadioSelect, choices=NA_ELECCIONES, initial='N',label="Palpacion")
	cuConsistencia  = forms.ChoiceField(widget=forms.RadioSelect, choices=NA_ELECCIONES, initial='N',label="Consistencia")
	cuMovilidad  = forms.ChoiceField(widget=forms.RadioSelect, choices=NA_ELECCIONES, initial='N',label="Movilidad")
	cuDolorMov = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Dolor a la movilizacion")
	sangrarTacto = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Sangra al contacto")
	tomaPap = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Toma PAP")
	cuObservaciones = forms.CharField(widget=forms.Textarea(attrs={'name':'cuObservaciones','cols':'40','rows':'2','maxlength':'100','class':'form-control'}),label="Observaciones",required=False)
	uteroPosicion = forms.ChoiceField(widget=forms.RadioSelect, choices=POSICION_ELECCIONES, initial='A',label="Posicion")
	uTamano  = forms.ChoiceField(widget=forms.RadioSelect, choices=NA_ELECCIONES, initial='N',label="Tamano")
	uConsistencia  = forms.ChoiceField(widget=forms.RadioSelect, choices=NA_ELECCIONES, initial='N',label="Consistencia")
	uMovilidad  = forms.ChoiceField(widget=forms.RadioSelect, choices=NA_ELECCIONES, initial='N',label="Movilidad")
	uDolorMov = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Dolor a la movilizacion")
	usnTumores = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Tumores")
	uTumores = forms.CharField(widget=forms.TextInput(attrs={'name':'uTumores','maxlength':'100','class':'form-control'}),label=" ",required=False)
	anexosLibres = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Anexos Libres")
	engrosados = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Engrosados")
	aDolorPalpitacion = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Dolor a la palpacion")
	asnTumores  = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Tumores")
	aTumores = forms.CharField(widget=forms.TextInput(attrs={'name':'aTumores','maxlength':'100','class':'form-control'}),label=" ",required=False)
	fondoSaco  = forms.ChoiceField(widget=forms.RadioSelect, choices=NA_ELECCIONES, initial='N',label="Fondo de saco")
	fechaInicioMetodo = forms.DateField(widget=forms.DateInput(attrs={'name':'fechaInicioMetodo','data-date-format':'DD/MM/YYYY','class':'form-control','id':'fechaInicioMetodo'}),label="Fecha de inicio de metodo",required=False)
	anticonceptivo = forms.ChoiceField(widget=forms.RadioSelect, choices=ANTICONCEPTIVOS_ELECCIONES,label="Anticonceptivo",required=False)
	miONombre = forms.CharField(widget=forms.TextInput(attrs={'name':'miONombre','maxlength':'15','class':'form-control'}),label="Nombre",required=False)
	miOtros = forms.CharField(widget=forms.TextInput(attrs={'name':'miOtros','maxlength':'15','class':'form-control'}),label="Otros",required=False)
	diagnostico = forms.CharField(widget=forms.TextInput(attrs={'name':'diagnostico','maxlength':'100','class':'form-control'}),label="Diagnostico",required=False)
	indicaciones = forms.CharField(widget=forms.TextInput(attrs={'name':'indicaciones','maxlength':'100','class':'form-control'}),label="Indicaciones",required=False)
	proximaConsulta = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'proximaConsulta','class':'form-control','min':'0','max':'20','value': '0'}),label="Proxima Consulta")
	proximaConsultaLapso = forms.CharField(max_length=1,widget=forms.Select(attrs={'name':'proximaConsultaLapso','class':'form-control'}, choices=TIEMPO_ELECCIONES),label=" ")
	
class PlanificacionSubForm(ModelForm):
	#El model a utilizar, con los elementos visibles	
	class Meta:
		model = PacienteSubSecuentePF 
		fields = ['peso','presionArterial','metUtilizado','metTiempo','metLapso','histHallazgos','metContinuacion','nombreCambio','motivoCambio',
		'diagnostico','tomaPap','tipoConsulta','indicaciones','proximaConsulta','proximaConsultaLapso']
	
	peso = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'peso','class':'form-control','min':'80','max':'450'}),label="Peso",help_text="(*)")
	presionArterial = forms.CharField(widget=forms.TextInput(attrs={'name':'presionArterial','maxlength':'7','class':'form-control','placeholder':'###/##'}),label="PA",help_text="(*)")
	metUtilizado = forms.CharField(widget=forms.TextInput(attrs={'name':'metUtilizado','maxlength':'60','class':'form-control'}),label="Metodo Utilizado",required=False)
	metTiempo = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'metTiempo','class':'form-control','min':'1','max':'100'}),label="Tiempo de uso",required=False)
	metLapso = forms.CharField(max_length=1,widget=forms.Select(attrs={'name':'metLapso','class':'form-control'}, choices=TIEMPO_ELECCIONES),label=" ",help_text="(*)")
	histHallazgos = forms.CharField(widget=forms.Textarea(attrs={'name':'histHallazgos','cols':'40','rows':'2','maxlength':'500','class':'form-control'}),label="Historia y hallazgos",required=False)
	metContinuacion  = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='S',label="Continua con el metodo")
	nombreCambio = forms.CharField(widget=forms.TextInput(attrs={'name':'nombreCambio','maxlength':'50','class':'form-control'}),label="Cambia a",required=False)
	motivoCambio = forms.CharField(widget=forms.Textarea(attrs={'name':'motivoCambio','cols':'40','rows':'2','maxlength':'500','class':'form-control'}),label="Motivo del cambio",required=False)
	diagnostico = forms.CharField(widget=forms.Textarea(attrs={'name':'diagnostico','maxlength':'50','cols':'40','rows':'2','maxlength':'500','class':'form-control'}),label="Diagnostico",required=False)
	tomaPap = forms.ChoiceField(widget=forms.RadioSelect, choices=ELECCIONES, initial='N',label="Toma PAP")
	tipoConsulta = forms.ChoiceField(widget=forms.RadioSelect, choices=CONSULTA_ELECCIONES, initial='N',label="Tipo de consulta")
	indicaciones = forms.CharField(widget=forms.Textarea(attrs={'name':'indicaciones','cols':'40','rows':'2','maxlength':'500','maxlength':'100','class':'form-control'}),label="Indicaciones",required=False)
	proximaConsulta = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'proximaConsulta','class':'form-control','min':'0','max':'20','value': '0'}),label="Proxima Consulta")
	proximaConsultaLapso = forms.CharField(max_length=1,widget=forms.Select(attrs={'name':'proximaConsultaLapso','class':'form-control'}, choices=TIEMPO_ELECCIONES),label=" ")