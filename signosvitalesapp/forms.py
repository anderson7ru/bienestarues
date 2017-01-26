# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm

from signosvitalesapp.models import SignosVitales
from datospersonalesapp.models import Paciente
import re

class SignosForm(ModelForm):
    #Formulario para signos vitales
	class Meta:
		model = SignosVitales 
		fields = ['presionArterial','frecuenciaCardiaca','temperatura','peso','talla','frecuenciaRespiratoria']
	presionArterial = forms.CharField(widget=forms.TextInput(attrs={'name':'presionArterial','maxlength':'7','class':'form-control','placeholder':'###/##'}),label="Presion Arterial",help_text="(*)")
	frecuenciaCardiaca = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'frecuenciaCardiaca','class':'form-control','min':'40','max':'150'}),label="Frecuencia cardiaca",help_text="(*)")
	temperatura = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'temperatura','class':'form-control','min':'30.0','max':'40.0'}),label="Temperatura",help_text="(*)")
	peso = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'peso','class':'form-control','min':'80','max':'450'}),label="Peso",help_text="(*)")
	talla = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'talla','class':'form-control','min':'1.30','max':'2.50'}),label="Talla",help_text="(*)")
	frecuenciaRespiratoria = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'frecuenciaRespiratoria','class':'form-control','min':'16','max':'28'}),label="Frecuencia respiratoria",help_text="(*)")