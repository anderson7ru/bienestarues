from enfermeriaapp.models import Cola_Consulta, Cola_Enfermeria
from django import forms
from django.forms import ModelForm, Textarea
from datospersonalesapp.models import Paciente
from empleadosapp.models import Doctor
from smart_selects.form_fields import ChainedModelChoiceField

class ColaEnfermeriaForm(ModelForm):
    class Meta:
        model = Cola_Enfermeria
        fields = ['idPaciente']
    idPaciente=forms.ModelChoiceField(widget=forms.Select(attrs={'name':'Paciente','class':'form-control'}),queryset=Paciente.objects.all(),label="Paciente",help_text="(*)")

class ColaConsultaForm(ModelForm):
    class Meta:
        model = Cola_Consulta
        fields = ['idDoctor']
    idDoctor=forms.ModelChoiceField(widget=forms.Select(attrs={'name':'Doctor','class':'form-control'}),queryset=Doctor.objects.all(),label="Doctor",help_text="(*)")