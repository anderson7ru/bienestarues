# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, Textarea

# apps internas y externas
from smart_selects.form_fields import ChainedModelChoiceField
from datospersonalesapp.models import Paciente, Departamento, Municipio, Facultad, Busqueda
import re

#Formulario para la creacion de Expediente del Paciente
# Elecciones para modelos: --se utilizan en el formulario
SEXO_ELECCIONES=(
    ('M','Masculino'),
    ('F','Femenino'),
    )

ESTADOCIVIL_ELECCIONES=(
    ('SOLTER','Soltero(a)'),
    ('CASAD','Casado(a)'),
    ('DIVORCIAD','Divorciado(a)'),
    ('ACOMPANAD','Acompanado(a)'),
    ('VIUD','Viudo(a)'),
    )

ESTADOUES_ELECCIONES=(
    ('EST','Estudiante'),
    ('DOC','Docente'),
    ('PAD','Pers.Administrativo'),
    ('OTR','Otro'),
    )

class PacienteForm(ModelForm):
    #El model a utilizar, con los elementos visibles	
	class Meta:
		model = Paciente 
		fields = ['apellidoPrimero', 'apellidoSegundo', 'nombrePrimero', 'nombreSegundo', 'sexo', 'fechaNacimiento', 
		'estadoCivil', 'nit', 'dui', 'due', 'estadoUes', 'facultadE', 'codDepartamento', 'codMunicipio', 'direccion', 'telefono', 
		'correo', 'nombrePadre', 'nombreMadre', 'nombrePareja', 'emergencia', 'telefonoEmergencia']
	
	apellidoPrimero = forms.CharField(widget=forms.TextInput(attrs={'name':'apellidoPrimero','maxlength':'15','class':'form-control'}),label="Primer Apellido",help_text="(*)")
	apellidoSegundo = forms.CharField(widget=forms.TextInput(attrs={'name':'apellidoSegundo','maxlength':'15','class':'form-control'}),label="Segundo Apellido",required=False)
	nombrePrimero = forms.CharField(widget=forms.TextInput(attrs={'name':'nombrePrimero','maxlength':'15','class':'form-control'}),label="Primer Nombre",help_text="(*)")
	nombreSegundo = forms.CharField(widget=forms.TextInput(attrs={'name':'nombreSegundo','maxlength':'15','class':'form-control'}),label="Segundo Nombre",required=False)
	sexo = forms.CharField(max_length=1,widget=forms.Select(attrs={'name':'sexo','class':'form-control'},choices=SEXO_ELECCIONES),label="Sexo",help_text="(*)")
	fechaNacimiento = forms.DateField(widget=forms.DateInput(attrs={'name':'fechaNacimiento','data-date-format':'DD/MM/YYYY','class':'form-control','id':'fechaNacimiento'}),label="Fecha de Nacimiento",help_text="(*)")
	estadoCivil = forms.CharField(max_length=12,widget=forms.Select(attrs={'name':'estadoCivil','class':'form-control'},choices=ESTADOCIVIL_ELECCIONES),label="Estado civil",help_text="(*)")
	nit = forms.CharField(widget=forms.TextInput(attrs={'name':'nit','maxlength':'17','placeholder':'####-######-###-#','class':'form-control','id':'nit'}),label="NIT",help_text="(*)")
	dui = forms.CharField(widget=forms.TextInput(attrs={'name':'dui','maxlength':'10','placeholder':'########-#','class':'form-control','id':'dui'}),label="DUI",required=False)
	due = forms.CharField(widget=forms.TextInput(attrs={'name':'due','maxlength':'7','placeholder':'AA#####','class':'form-control','id':'due'}),label="DUE",required=False)
	estadoUes = forms.CharField(max_length=3,widget=forms.Select(attrs={'name':'estadoUes','class':'form-control'},choices=ESTADOUES_ELECCIONES),label="Estado UES",help_text="(*)")
	facultadE = forms.ModelChoiceField(widget=forms.Select(attrs={'name':'facultadE','class':'form-control'}),queryset=Facultad.objects.all(),label="Facultad",help_text="(*)")
	codDepartamento = forms.ModelChoiceField(widget=forms.Select(attrs={'name':'codDepartamento','class':'form-control'}),queryset=Departamento.objects.all(),label="Departamento",help_text="(*)")
	codMunicipio = ChainedModelChoiceField('datospersonalesapp','Municipio','codDepartamento','codDepartamento','datospersonalesapp','Paciente','codMunicipio',False,True)
	direccion = forms.CharField(widget=forms.Textarea(attrs={'name':'direccion','cols':'40','rows':'3','maxlength':'300','class':'form-control'}),label="Direccion",help_text="(*)")
	telefono = forms.CharField(widget=forms.TextInput(attrs={'name':'telefono','maxlength':'9','placeholder':'####-####','class':'form-control','id':'telefono'}),label="Telefono",required=False)
	correo = forms.EmailField(widget=forms.EmailInput(attrs={'name':'correo','class':'form-control'}),label="correo",required=False)
	nombrePadre = forms.CharField(widget=forms.TextInput(attrs={'name':'nombrePadre','maxlength':'65','class':'form-control'}),label="Nombre del Padre",required=False)
	nombreMadre = forms.CharField(widget=forms.TextInput(attrs={'name':'nombreMadre','maxlength':'65','class':'form-control'}),label="Nombre de la Madre",required=False)
	nombrePareja = forms.CharField(widget=forms.TextInput(attrs={'name':'nombrePareja','maxlength':'65','class':'form-control'}),label="Nombre del Conyuge",required=False)
	emergencia = forms.CharField(widget=forms.TextInput(attrs={'name':'emergencia','maxlength':'65','class':'form-control'}),label="Responsable del Paciente",help_text="(*)")
	telefonoEmergencia = forms.CharField(widget=forms.TextInput(attrs={'name':'telefonoEmergencia','maxlength':'9','placeholder':'####-####','class':'form-control','id':'telefonoEmergencia'}),label="Telefono",help_text="(*)")
	
class BusquedaForm(ModelForm):
	class Meta:
		model = Busqueda
		fields = ['consulta']
	
	consulta = forms.CharField(widget=forms.TextInput(attrs={'name':'busqueda','id':'busqueda','class':'form-control','maxlength':'150','Placeholder':'Terminos de busqueda'}),label="Terminos de Busqueda")