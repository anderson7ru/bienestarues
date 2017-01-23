from django import forms
from django.forms import ModelForm
from smart_selects.form_fields import ChainedModelChoiceField

from citasmedicasapp.models import Cita, Cancelacion
from datospersonalesapp.models import Paciente

#Formulario para la creacion de citas
class CitasMedicasForm(ModelForm):
	#El model a utilizar, con los elementos visibles	
	class Meta:
		model = Cita 
		fields = ['horaConsulta', 'paciente']
	horaConsulta = forms.TimeField(widget=forms.TextInput(attrs={'name':'horaConsulta','class':'form-control','id':'horaConsulta','maxlength':'5'}),label="Hora de Inicio",help_text="(*)")
	paciente = forms.ModelChoiceField(widget=forms.Select(attrs={'name':'paciente','class':'selectpicker','data-live-search':'true'}),queryset=Paciente.objects.filter(estadoExpediente='A'),label="Paciente",help_text="(*)")

#Formulario para la cancelacion
class CancelacionForm(ModelForm):
	#El model a utilizar, con los elementos visibles	
	class Meta:
		model = Cancelacion 
		fields = ['fechaInicio', 'fechaFinal', 'horaInicio', 'horaFinal']
	fechaInicio = forms.DateField(widget=forms.DateInput(attrs={'name':'fechaInicio','data-date-format':'DD/MM/YYYY','class':'form-control','id':'fechaInicio'}),label="Fecha de Inicio",help_text="(*)")
	fechaFinal = forms.DateField(widget=forms.DateInput(attrs={'name':'fechaFinal','data-date-format':'DD/MM/YYYY','class':'form-control','id':'fechaFinal'}),label="Fecha de Finalizacion",required=False)
	horaInicio = forms.TimeField(widget=forms.TextInput(attrs={'name':'horaInicio','class':'form-control','id':'horaInicio','maxlength':'5'}),label="Hora de Inicio",help_text="(*)")
	horaFinal = forms.TimeField(widget=forms.TextInput(attrs={'name':'horaFinal','class':'form-control','id':'horaFinal','maxlength':'5'}),label="Hora de Finalizacion",help_text="(*)")