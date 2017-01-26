# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, Textarea
from .models import *
from smart_selects.form_fields import ChainedModelChoiceField

FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)

class ConsultaMForm(ModelForm):
    class Meta:
        model = Consulta
        fields = [
            'consulta_por', 'presenta_enfermedad', 'antecedentes_personales', 'antecedentes_familiares', 
            'exploracion_clinica', 'otros_diagnosticos', 'tratamiento', 'observaciones', 
            'cod_expediente', 'cod_doctor', 'diagnostico_principal']
    consulta_por = forms.CharField(widget=forms.Textarea(attrs={'required': 'required', 'class': 'form-control', 'rows': 4}))
    presenta_enfermedad = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    
    antecedentes_personales = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    antecedentes_familiares = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    
    exploracion_clinica = forms.CharField(widget=forms.Textarea(attrs={'required': 'required', 'class': 'form-control', 'rows': 4}))
    otros_diagnosticos = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    tratamiento = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    
    observaciones = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    
    cod_expediente = forms.CharField(label='No. de Expediente Clínico', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    cod_doctor = forms.CharField(label='J.V.P.M. No', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    diagnostico_principal = forms.ModelChoiceField(queryset=db29179_cie10.objects.all().order_by('dec10'), widget=forms.Select(attrs={'class': 'form-control', 'required': 'required'}))

class RecetaMForm(ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'

class CompuestoMForm(ModelForm):
    class Meta:
        model = Compuesto
        fields = '__all__'

class OrdenLabMForm(ModelForm):
    class Meta:
        model = OrdenLab
        fields = ['cod_expediente', 'cod_doctor', 'cod_consulta', 'nombre_area', 'nombre_examen', 'observaciones']
    cod_expediente = forms.CharField(label='No. de Expediente Clínico', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    cod_doctor = forms.CharField(label='J.V.P.M. No', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    cod_consulta = forms.CharField(label='No. Consulta', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    nombre_area = forms.ModelChoiceField(queryset=AreaLab.objects.all().order_by('nombre_area'), widget=forms.Select(attrs={'class': 'form-control', 'required': 'required'}))
    # nombre_examen = forms.ModelChoiceField(queryset=ExamenLab.objects.all().order_by('nombre_examen'), widget=forms.Select(attrs={'class': 'form-control', 'required': 'required'}))
    nombre_examen = ChainedModelChoiceField('generalapp', 'ExamenLab', '', 'cod_area','generalapp', 'OrdenLab', 'nombre_examen', False, True)
    observaciones = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

class ReferenciaInternaMForm(ModelForm):
    class Meta:
        model = ReferenciaInterna
        fields = '__all__'

class ReferenciaExternaMForm(ModelForm):
    class Meta:
        model = ReferenciaExterna
        fields = '__all__'

class DatosPersonalesForm(forms.Form):
    expediente = forms.CharField(label='No. de Expediente Clínico', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    fecha_nacimiento = forms.CharField(label='Fecha de Nacimiento', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    sexo = forms.CharField(label='Sexo', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    edad = forms.CharField(label='Edad', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'aria-describedby': 'id_edad_addon'}))
    domicilio = forms.CharField(label='Domicilio', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    telefono = forms.CharField(label='Teléfono', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))

class SignosVitalesForm(forms.Form):
    presion_arterial = forms.CharField(label='Presión Arterial', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'aria-describedby': 'id_presion_arterial_addon'}))
    frecuencia_cardiaca = forms.CharField(label='Frecuencia Cardiaca', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'aria-describedby': 'id_frecuencia_cardiaca_addon'}))
    frecuencia_respiratoria = forms.CharField(label='Frecuencia Respiratoria', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'aria-describedby': 'id_frecuencia_respiratoria_addon'}))
    temperatura = forms.CharField(label='Temperatura', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'aria-describedby': 'id_temperatura_addon'}))
    peso = forms.CharField(label='Peso', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'aria-describedby': 'id_peso_addon'}))
    talla = forms.CharField(label='Talla', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'aria-describedby': 'id_talla_addon'}))
    imc = forms.CharField(label='Indice Masa Corporal', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'aria-describedby': 'id_imc_addon'}))