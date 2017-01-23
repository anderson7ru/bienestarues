from django.forms import ModelForm,RadioSelect,NumberInput,CheckboxInput,Select,SelectMultiple
from smart_selects.form_fields import ChainedModelChoiceField
from .models import Nutricion, DatosNutricionales 

class NutricionForm(ModelForm):
    class Meta:
        model = Nutricion
        
        fields = ['estructuraOsea','extensionBrazada','circunferenciaCuerpo',
                 'pesoDeseable']
                 
        widgets = {
            'estructuraOsea': Select(attrs={'name':'estructura','id':'estructura','class':'form-control'}),
            'extensionBrazada': NumberInput(attrs={'name':'extension','class':'form-control','id':'extension','max':'3.0','min':'0.20'}),
            'circunferenciaCuerpo': NumberInput(attrs={'name':'circunferencia','class':'form-control','id':'circunferencia','min':'20'}),
            'pesoDeseable': NumberInput(attrs={'name':'pesoD','class':'form-control','id':'pesoD','min':'20'}),
        }

class DatosNutricionalesForm(ModelForm):
    class Meta:
        model = DatosNutricionales
        
        fields = ['habitos','alimentosPreferidos','alimentosIntolerados']
                 
        widgets = {
            'habitos': CheckboxInput(attrs={'name':'habitos','class':'form-control','id':'habitos'}),
            #'grupoAlimentos': Select(attrs={'name':'grupos','class':'form-control','id':'grupos'}),
            'alimentosPreferidos': SelectMultiple(attrs={'name':'to[]','class':'form-control','id':'preferidos_id'}),
            'alimentosIntolerados': SelectMultiple(attrs={'name':'to_2[]','class':'form-control','id':'intolerados_id'})
            
        }
        #alimentos = ChainedModelChoiceField('nutricionapp','AlimentosGrupo','grupoAlimentos','grupo','nutricionapp','DatosNutricionales','alimentos',False,True)