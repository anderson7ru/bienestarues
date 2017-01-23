from django import forms
from django.forms import ModelForm, Textarea, NumberInput, TextInput, DateInput, Select
#from .models import Psicologia,ProcesoTerapeutico
from .models import Psicologia, ProcesoTerapeutico, RegistroAvance
from empleadosapp.models import Doctor

Elecciones_Tecnicas = (
    ('observacion','Observacion'),
    ('entrevista','Entrevista'),
    ('prueba','Prueba Pca'),
    ('conv','Conv. Terapeutica'),
    ('relajacion','Tecnica de relajacion'),
    ('musico','Musicoterapia'),
)

class PsicologiaForm(ModelForm):
    class Meta:
        model = Psicologia
        
        fields = ['numero_hijos','profesion','fecha_primeraConsulta','direccionResponsable','referido','religion','familia',
        'motivo','antecedentes','apariencia','voz','patrones','expresionesF','ademanes','actitudes_tx',
        'impresion_dx','plan_tx','pronostico','fecha_proximaCita']
        
        #referido = forms.ModelChoiceField(widget=forms.Select(attrs={'name':'referido','class':'form-control'}),queryset=Doctor.objects.all(),label="Referido Por",help_text="(*)")
        
        widgets = {
            'numero_hijos': NumberInput(attrs={'class':'form-control','name':'numeroHijos','id':'numeroHijos'}),
            'profesion': TextInput(attrs={'class':'form-control','id':'profesion'}),
            'fecha_primeraConsulta': DateInput(attrs={'class':'form-control','data-date-format':'DD/MM/YYYY','id':'fechaPC'}),
            'direccionResponsable': TextInput(attrs={'class':'form-control','style':'max-width:624px','id':'direccionResponsable','placeholder':'Direccion del Responsable'}),
            'referido': Select(attrs={'class':'form-control','id':'referido','style':'max-width:312px'}),
            'religion': TextInput(attrs={'class':'form-control','id':'religion'}),
            'familia': NumberInput(attrs={'class':'form-control','name':'familia','id':'familia'}),
            'motivo': Textarea(attrs={'class':'form-control','id':'motivo','rows':'5','placeholder':'Motivo de la consulta'}),
            'antecedentes': Textarea(attrs={'class':'form-control','id':'antecedentes','rows':'6','placeholder':'Antecedentes del problema'}),
            'apariencia': TextInput(attrs={'class':'form-control','id':'apariencia','style':'max-width:624px'}),
            'voz': TextInput(attrs={'class':'form-control','id':'voz','style':'max-width:390px'}),
            'patrones': TextInput(attrs={'class':'form-control','id':'patrones','style':'max-width:390px'}),
            'expresionesF': TextInput(attrs={'class':'form-control','id':'expresionesF','style':'max-width:390px'}),
            'ademanes': TextInput(attrs={'class':'form-control','id':'ademanes','style':'max-width:390px'}),
            'actitudes_tx': Textarea(attrs={'class':'form-control','id':'actitudes_tx','rows':'3','placeholder':'Actitudes hacia el TX'}),
            'impresion_dx': Textarea(attrs={'class':'form-control','id':'impresion_dx','rows':'4','placeholder':'Impresion DX'}),
            'plan_tx': Textarea(attrs={'class':'form-control','id':'plan_tx','rows':'4','placeholder':'Plan de DX'}),
            'pronostico': Textarea(attrs={'class':'form-control','id':'pronostico','rows':'2','placeholder':'Pronostico'}),
            'fecha_proximaCita': DateInput(attrs={'name':'fechaProxC','class':'form-control','data-date-format':'DD/MM/YYYY','id':'fechaProxC'}),
        }
        
        
class ProcesoTerapeuticoForm(ModelForm):
    class Meta:
        model = ProcesoTerapeutico
        
        fields = ['objetivo','tecnicas','observaciones']
        
        widgets = {
            'objetivo': Textarea(attrs={'class':'form-control','id':'objetivo','rows':'3'}),
            'tecnicas': Select(attrs={'class':'form-control','id':'tecnicas'},choices=Elecciones_Tecnicas),
            'observaciones': Textarea(attrs={'class':'form-control','id':'observaciones','rows':'4'}),
        }
        
class RegistroAvanceForm(ModelForm):
    class Meta:
        model = RegistroAvance
        
        fields = ['paciente','psicologo']
        
        widgets = {
            'paciente': Textarea(attrs={'class':'form-control','id':'paciente','rows':'3'}),
            'psicologo': Textarea(attrs={'class':'form-control','id':'psicologo','rows':'3'}),
        }