from django.forms import ModelForm,RadioSelect,NumberInput,CheckboxInput,Select,Textarea
from smart_selects.form_fields import ChainedModelChoiceField
from .models import Nutricion, DatosNutricionales 

class NutricionForm(ModelForm):
    class Meta:
        model = Nutricion
        
        fields = ['estructuraOsea','extensionBrazada','circunferenciaCuerpo',
                 'pesoDeseable']
                 
        widgets = {
            'estructuraOsea': RadioSelect(attrs={'name':'estructura','id':'estructura','class'}),
            'extensionBrazada': NumberInput(attrs={'name':'extension','class':'form-control','id':'extension','max':'3.0','min':'0.20'}),
            'circunferenciaCuerpo': NumberInput(attrs={'name':'circunferencia','class':'form-control','id':'circunferencia','min':'20'}),
            'pesoDeseable': NumberInput(attrs={'name':'pesoD','class':'form-control','id':'pesoD','min':'20'}),
        }

class DatosNutricionalesForm(ModelForm):
    class Meta:
        model = DatosNutricionales
        
        fields = ['habitos','grupoAlimentos','alimentos','alimentosPreferidos',
                 'alimentosIntolerados']
                 
        widgets = {
            'habitos': CheckboxInput(attrs={'name':'habitos','class':'form-control','id':'habitos'}),
            'grupoAlimentos': Select(attrs={'name':'grupos','class':'form-control','id':'grupos'}),
            'alimentosPreferidos': Textarea(attrs={'name':'preferidos','class':'form-control','rows':'4'}),
            'alimentosIntolerados': Textarea(attrs={'name':'intolerados','class':'form-control','rows':'4'})
            
        }
        alimentos = ChainedModelChoiceField('nutricionapp','AlimentosGrupo','grupoAlimentos','grupo','nutricionapp','DatosNutricionales','alimentos',False,True)