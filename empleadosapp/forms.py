from django import forms
from django.forms import Form, ModelForm
from empleadosapp.models import Especialidad, Empleado
from citasmedicasapp.models import HorarioAtencion, diasSemana
import re

SEXO_ELECCIONES = (
    ('F','Femenino'),
    ('M','Masculino'),
    )

CARGO_ELECCIONES = 	(
    ('E','Enfermera'),
    ('A','Personal de Archivo'),
    ('P','Personal Administrativo'),
    ('D','Doctor'),
    ('O','Otros'),
    )
	
class EmpleadosForm(ModelForm):
    #El model a utilizar, con los elementos visibles	
	class Meta:
		model = Empleado
		fields = ['apellidoPrimero','apellidoSegundo','nombrePrimero','nombreSegundo','sexo','fechaNacimiento','cargo']
    
	apellidoPrimero = forms.CharField(widget=forms.TextInput(attrs={'name':'apellidoPrimero','maxlength':'15','class':'form-control'}),label="Primer Apellido",help_text="(*)")
	apellidoSegundo = forms.CharField(widget=forms.TextInput(attrs={'name':'apellidoSegundo','maxlength':'15','class':'form-control'}),label="Segundo Apellido",required=False)
	nombrePrimero = forms.CharField(widget=forms.TextInput(attrs={'name':'nombrePrimero','maxlength':'15','class':'form-control'}),label="Primer Nombre",help_text="(*)")
	nombreSegundo = forms.CharField(widget=forms.TextInput(attrs={'name':'nombreSegundo','maxlength':'15','class':'form-control'}),label="Segundo Nombre",required=False)
	sexo = forms.CharField(max_length=1,widget=forms.Select(attrs={'name':'sexo','class':'form-control'},choices=SEXO_ELECCIONES),label="Sexo",help_text="(*)")
	fechaNacimiento = forms.DateField(widget=forms.DateInput(attrs={'name':'fechaNacimiento','data-date-format':'DD/MM/YYYY','class':'form-control','id':'fechaNacimientoE'}),label="Fecha de Nacimiento",help_text="(*)")
	cargo = forms.CharField(max_length=1,widget=forms.Select(attrs={'name':'cargo','class':'form-control'},choices=CARGO_ELECCIONES),label="Cargo",help_text="(*)")
	
class DoctorForm(Form):
	especialidad = forms.ModelChoiceField(widget=forms.Select(attrs={'name':'especialidad','class':'form-control'}),queryset=Especialidad.objects.all(),label="Especialidad",help_text="(*)")
	dia = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'name':'dia','class':'form-control'}),queryset=diasSemana.objects.all(),label="Dias de atencion",help_text="(*)")
	horaInicio = forms.TimeField(widget=forms.TextInput(attrs={'name':'horaInicio','class':'form-control','id':'horaInicio'}),label="Hora de inicio",help_text="(*)")
	horaFinal = forms.TimeField(widget=forms.TextInput(attrs={'name':'horaFinal','class':'form-control','id':'horaFinal'}),label="Hora de finalizacion",help_text="(*)")
	pacienteConsulta = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'pacienteConsulta','class':'form-control','min':'1','max':'10','value': '4'}),label="Pacientes atendidos por hora",help_text="(*)")