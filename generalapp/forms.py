# -*- coding: utf-8 -*-
from django import forms
from dal import autocomplete
from django.forms import ModelForm, Textarea, TextInput, Select
from .models import *
from smart_selects.form_fields import ChainedModelChoiceField

from empleadosapp.models import Especialidad






## formulario para consulta
#
class ConsultaMForm(ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'
        widgets = {
            'cod_expediente': TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'required': 'required'}),
            'cod_doctor': TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'required': 'required'}),
            'nit_paciente': TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'required': 'required'}),
            
            'tipo_consulta': Select(attrs={'class': 'form-control', 'required': 'required'}),
            
            'consulta_por': Textarea(attrs={'class': 'form-control', 'rows': 4, 'required': 'required'}),
            'presenta_enfermedad': Textarea(attrs={'class': 'form-control', 'rows': 4}),
            
            'antecedentes_personales': Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'antecedentes_familiares': Textarea(attrs={'class': 'form-control', 'rows': 4}),
            
            'exploracion_clinica': Textarea(attrs={'class': 'form-control', 'rows': 4, 'required': 'required'}),
            'diagnostico_principal': TextInput(attrs={'class': 'form-control'}),
            'otros_diagnosticos': Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'tratamiento': Textarea(attrs={'class': 'form-control', 'rows': 4}),
            
            'observaciones': Textarea(attrs={'class': 'form-control', 'rows': 4})
        }





# ## formulario para receta
# #
# class RecetaMForm(ModelForm):
#     class Meta:
#         model = Receta
#         fields = '__all__'
#         widgets = {
#             'cod_expediente': TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'required': 'required'}),
#             'cod_doctor': TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'required': 'required'}),
#             'cod_consulta': TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'required': 'required'}),
            
#             'medicamento': TextInput(attrs={'class': 'form-control', 'required': 'required'}),
#             'observaciones': Textarea(attrs={'class': 'form-control', 'rows': 4})
#         }

















# class CompuestoMForm(ModelForm):
#     class Meta:
#         model = Compuesto
#         fields = '__all__'





# class OrdenLabMForm(ModelForm):
#     class Meta:
#         model = OrdenLab
#         fields = ['cod_expediente', 'cod_doctor', 'cod_consulta', 'codArea', 'codExamen', 'observaciones']
#     cod_expediente = forms.ModelChoiceField(queryset=Paciente.objects.all(), widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
#     cod_doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
#     cod_consulta = forms.ModelChoiceField(queryset=Consulta.objects.all(), widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    
#     codArea = forms.ModelChoiceField(queryset=AreaLab.objects.all().order_by('nombreArea'), widget=forms.Select(attrs={'class': 'form-control', 'required': 'required'}))
#     codExamen = ChainedModelChoiceField('generalapp', 'ExamenLab', 'codArea', 'codArea', 'generalapp', 'OrdenLab', 'codExamen', False, True)
    
#     observaciones = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))









#
## formulario para receta
#
class RecetaMForm(ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'
        widgets = {
            'cod_expediente': TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'required': 'required'}),
            'cod_doctor': TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'required': 'required'}),
            'cod_consulta': TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'required': 'required'}),
            
            'medicamento': TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'observaciones': Textarea(attrs={'class': 'form-control', 'rows': 4})
        }
#
## formulario para orden de laboratorio
#
class OrdenLabMForm(ModelForm):
    codArea = forms.ModelChoiceField(queryset=AreaLab.objects.all().order_by('nombreArea'), widget=forms.Select())
    codExamen = ChainedModelChoiceField('generalapp', 'ExamenLab', 'codArea', 'codArea', 'generalapp', 'OrdenLab', 'codExamen', False, True)
    class Meta:
        model = OrdenLab
        fields = '__all__'
        widgets = {
            'cod_expediente': TextInput(attrs={'class': 'form-control', 'required': 'required', 'readonly': 'readonly'}),
            'cod_doctor': TextInput(attrs={'class': 'form-control', 'required': 'required', 'readonly': 'readonly'}),
            'cod_consulta': TextInput(attrs={'class': 'form-control', 'required': 'required', 'readonly': 'readonly'}),
            
            'observaciones': Textarea(attrs={'class': 'form-control', 'rows': 4})
        }
#
## formulario para referencia interna
#
class ReferenciaInternaMForm(ModelForm):
    referido_a = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'required': 'required'}), queryset=Especialidad.objects.exclude(pk=1).exclude(especialidad='Medicina General'))
    class Meta:
        model = ReferenciaInterna
        fields = '__all__'
        widgets = {
            'cod_expediente': TextInput(attrs={'class': 'form-control', 'required': 'required', 'readonly': 'readonly'}),
            'cod_doctor': TextInput(attrs={'class': 'form-control', 'required': 'required', 'readonly': 'readonly'}),
            'cod_consulta': TextInput(attrs={'class': 'form-control', 'required': 'required', 'readonly': 'readonly'}),
            
            'nombre_paciente': TextInput(attrs={'class': 'form-control', 'required': 'required', 'readonly': 'readonly'}),
            'tipo_paciente': TextInput(attrs={'class': 'form-control', 'required': 'required', 'readonly': 'readonly'}),
            
            'procedencia_paciente': TextInput(attrs={'class': 'form-control', 'required': 'required', 'readonly': 'readonly'}),
            'motivo_referencia': Textarea(attrs={'class': 'form-control', 'rows': 4, 'required': 'required'}),
            'observaciones': Textarea(attrs={'class': 'form-control', 'rows': 4})
        }
#
## formulario para referencia externa
#
class ReferenciaExternaMForm(ModelForm):
    referido_a = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'required': 'required'}), queryset=CentroAsistencial.objects.all().order_by('nombre'))
    
    presion_arterial = forms.CharField(label='Presión Arterial', widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'id_presion_arterial_addon', 'required': 'required', 'readonly': 'readonly'}))
    frecuencia_cardiaca = forms.CharField(label='Frecuencia Cardiaca', widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'id_frecuencia_cardiaca_addon', 'required': 'required', 'readonly': 'readonly'}))
    frecuencia_respiratoria = forms.CharField(label='Frecuencia Respiratoria', widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'id_frecuencia_respiratoria_addon', 'required': 'required', 'readonly': 'readonly'}))
    temperatura = forms.CharField(label='Temperatura', widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'id_temperatura_addon', 'required': 'required', 'readonly': 'readonly'}))
    peso = forms.CharField(label='Peso', widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'id_peso_addon', 'required': 'required', 'readonly': 'readonly'}))
    talla = forms.CharField(label='Talla', widget=forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'id_talla_addon', 'required': 'required', 'readonly': 'readonly'}))
    class Meta:
        model = ReferenciaExterna
        fields = '__all__'
        widgets = {
            'cod_expediente': TextInput(attrs={'class': 'form-control', 'required': 'required', 'readonly': 'readonly'}),
            'cod_doctor': TextInput(attrs={'class': 'form-control', 'required': 'required', 'readonly': 'readonly'}),
            'cod_consulta': TextInput(attrs={'class': 'form-control', 'required': 'required', 'readonly': 'readonly'}),
            
            'referido_a': TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'nombre_paciente': TextInput(attrs={'class': 'form-control', 'required': 'required', 'readonly': 'readonly'}),
            'edad_paciente': TextInput(attrs={'class': 'form-control', 'required': 'required', 'readonly': 'readonly', 'aria-describedby': 'id_edad_paciente_addon'}),
            'sexo_paciente': TextInput(attrs={'class': 'form-control', 'required': 'required', 'readonly': 'readonly'}),
            'domicilio_paciente': TextInput(attrs={'class': 'form-control', 'required': 'required', 'readonly': 'readonly'}),
            'telefono_paciente': TextInput(attrs={'class': 'form-control', 'required': 'required', 'readonly': 'readonly'}),
            
            'consulta_por': Textarea(attrs={'class': 'form-control', 'rows': 4, 'required': 'required', 'readonly': 'readonly'}),
            'presenta_enfermedad': Textarea(attrs={'class': 'form-control', 'rows': 4, 'readonly': 'readonly'}),
            
            'antecedentes_personales': Textarea(attrs={'class': 'form-control', 'rows': 4, 'readonly': 'readonly'}),
            'examen_fisico': Textarea(attrs={'class': 'form-control', 'rows': 4, 'required': 'required', 'readonly': 'readonly'}),
            'examenes_laboratorio': TextInput(attrs={'class': 'form-control'}),
            'impresion_diagnostica': TextInput(attrs={'class': 'form-control', 'required': 'required', 'readonly': 'readonly'}),
            
            'observaciones': Textarea(attrs={'class': 'form-control', 'rows': 4})
        }
#
##
#
















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