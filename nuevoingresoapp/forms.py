from django import forms
from django.utils import timezone
from django.forms import ModelForm, Textarea
from smart_selects.form_fields import ChainedModelChoiceField
from django.contrib.auth.models import User
from nuevoingresoapp.models import Expediente_Provisional, Certificado_Salud, Actividad_Enfermeria, Censo_Enfermeria, importar_bd
from datospersonalesapp.models import Facultad

import re

#Formulario para la creacion del expediente clinico provisional para alumnos de nuevo ingreso
#Los widget utilizados, como: fecha de nacimento y las mascaras

SEXO_ELECCIONES=(
        ('M','Masculino'),
        ('F','Femenino'),
        )

class ExpedienteProForm(ModelForm):
    #El model a utilizar, con los elementos visibles
    class Meta:
        model = Expediente_Provisional
        fields = ['nombrePrimero','nombreSegundo','apellidoPrimero','apellidoSegundo','fechaNacimiento','nit','sexo',
        'facultad','telefono','correo','talla','temperatura','presionArterial','peso','frecuenciaRespiratoria','frecuenciaCardiaca','Observaciones']
    #Datos del Formulario
    #Cod_Expediente_Provisional=forms.IntegerField(required=False)
    nombrePrimero = forms.CharField(widget=forms.TextInput(attrs={'name':'primerNombre','maxlength':'15','class':'form-control'}),label="Primer Nombre",help_text="(*)")
    nombreSegundo = forms.CharField(widget=forms.TextInput(attrs={'name':'segundoNombre','maxlength':'15','class':'form-control'}),label="Segundo Nombre",required=False)
    apellidoPrimero = forms.CharField(widget=forms.TextInput(attrs={'name':'primerApellido','maxlength':'15','class':'form-control'}),label="Primer Apellido",help_text="(*)")
    apellidoSegundo = forms.CharField(widget=forms.TextInput(attrs={'name':'segundoApellido','maxlength':'15','class':'form-control'}),label="Segundo Apellido",required=False)
    fechaNacimiento = forms.DateField(widget=forms.DateInput(attrs={'name':'fechaNacimiento','data-date-format':'DD/MM/YYYY','class':'form-control','id':'fechaNacimiento'}),label="Fecha de Nacimiento",help_text="(*)")
    nit = forms.CharField(widget=forms.TextInput(attrs={'name':'nit','maxlength':'17','placeholder':'####-######-###-#','class':'form-control','id':'nit'}),label="NIT",help_text="(*)")
    sexo = forms.CharField(max_length=1,widget=forms.Select(attrs={'name':'sexo','class':'form-control'},choices=SEXO_ELECCIONES),label="Sexo",help_text="(*)")
    facultad=forms.ModelChoiceField(widget=forms.Select(attrs={'name':'facultad','class':'form-control'}),queryset=Facultad.objects.all(),label="Facultad",help_text="(*)")
    telefono = forms.CharField(widget=forms.TextInput(attrs={'name':'telefono','maxlength':'9','placeholder':'####-####','class':'form-control','id':'telefono'}),label="Telefono",required=False)
    correo=forms.EmailField(widget=forms.EmailInput(attrs={'name':'correo','class':'form-control'}),label="Correo",required=False)
    Observaciones = forms.CharField(required=False)
    presionArterial = forms.CharField(widget=forms.TextInput(attrs={'name':'presionArterial','maxlength':'7','class':'form-control','placeholder':'###/##'}),label="Presion Arterial",help_text="(*)")
    frecuenciaCardiaca = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'frecuenciaCardiaca','class':'form-control','min':'40','max':'150'}),label="Frecuencia cardiaca",help_text="(*)")
    temperatura = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'temperatura','class':'form-control','min':'30.0','max':'40.0'}),label="Temperatura",help_text="(*)")
    peso = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'peso','class':'form-control','min':'80','max':'450'}),label="Peso",help_text="(*)")
    talla = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'talla','class':'form-control','min':'1.30','max':'2.50'}),label="Talla",help_text="(*)")
    frecuenciaRespiratoria = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'frecuenciaRespiratoria','class':'form-control','min':'16','max':'28'}),label="Frecuencia respiratoria",help_text="(*)")

class CertificadoForm(ModelForm):
    class Meta:
        model = Certificado_Salud
        fields = ['enfermedadIC','enfermedadICDetalle','enfermedadEF','enfermedadEFDetalle','enfermedadSN','enfermedadSNDetalle',
        'resultadoHIV','resultadoHECES','resultadoVDRL','resultadoHemograma','resultadoOrina','resultadoRX','presentaImpedimentos',
        'presentaImpedimentosDetalle','aptoAprobado','aptoAprobadoDetalle']
    enfermedadIC = forms.CharField(required=False)
    enfermedadICDetalle = forms.CharField(required=False)
    enfermedadEF = forms.CharField(required=False)
    enfermedadEFDetalle = forms.CharField(required=False)
    enfermedadSN = forms.CharField(required=False)
    enfermedadSNDetalle = forms.CharField(required=False)
    resultadoHIV = forms.CharField(required=False)
    resultadoHECES = forms.CharField(required=False)
    resultadoVDRL = forms.CharField(required=False)
    resultadoHemograma = forms.CharField(required=False)
    resultadoOrina = forms.CharField(required=False)
    resultadoRX = forms.CharField(required=False)
    presentaImpedimentos = forms.CharField(required=False)
    presentaImpedimentosDetalle = forms.CharField(required=False)
    aptoAprobado = forms.CharField(required=False)
    aptoAprobadoDetalle = forms.CharField(required=False)

class ActividadForm(ModelForm):
    class Meta:
        model = Actividad_Enfermeria
        fields = ['nombreActividad']
    nombreActividad = forms.CharField(widget=forms.TextInput(attrs={'name':'nombreActividad','maxlength':'50','class':'form-control'}),label="Nombre de la Actividad",help_text="(*)")

class CensoForm(ModelForm):
    class Meta:
        model = Censo_Enfermeria
        fields = ['cantidad','actividad']
    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'cantidad','class':'form-control','min':'0','max':'100'}),label="cantidad",help_text="(*)")
    actividad=forms.ModelChoiceField(widget=forms.Select(attrs={'name':'actividad','class':'form-control'}),queryset=Actividad_Enfermeria.objects.all(),label="Actividad",help_text="(*)")

class importarBDForm(ModelForm):
    class Meta:
        model = importar_bd
        fields=['archivo']
        archivo = forms.FileField(widget=forms.FileInput(attrs={'name':'archivo','class':'form-control'}),label="SELECCIONAR UN ARCHIVO",help_text="(*)")