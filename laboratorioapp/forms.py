from django import forms
from django.forms import ModelForm, Textarea
from smart_selects.form_fields import ChainedModelChoiceField
from datospersonalesapp.models import Paciente
from laboratorioapp.models import Examen_Hematologia, Examen_Orina, Examen_Heces, Examen_General, Examen_Especiales, Examen_Quimica_Sanguinea
import re

NITRITOS_OPCIONES = (
    ('NEGATIVO','NEGATIVO'),
    ('POSITIVO','POSITIVO'),
    )

OPCIONES = (
    ('ESCASAS','ESCASAS'),
    ('MODERADAS','MODERADAS'),
    ('ABUNDANTES','ABUNDANTES')
    )

CILINDROS_OPCIONES = (
    ('NO SE OBSERVAN','NO SE OBSERVAN'),
    ('CL','CILINDRO LEUCOCIDARIO'),
    ('CG','CILINDRO GRANULOSO'),
    ('CE','CILINDRO ERITROCITARIO')
    )

CRISTALES_OPCIONES = (
    ('NO SE OBSERVAN','NO SE OBSERVAN'),
    ('SC','SULFATOS DE CALCIO'),
    ('OC','OXALATOS DE CALCIO'),
    ('UA','URATOS AMORFOS'),
    ('AU','ACIDO URICO'),
    ('FT','FOSFATOS TRIPLES'),
    ('FA','FOSFATOS AMORFOS')
    )

OPCIONES_RESTOS = (
    ('E','ESCASOS'),
    ('M','MODERADOS'),
    ('A','ABUNDANTES')
    )

COLOR = (
    ('A','AMARILLO'),
    ('C','CAFE'),
    ('N','NEGRO'),
    ('R','ROJO'),
    ('V','VERDE')
    )
    
CONSISTENCIA = (
    ('P','PASTOSA'),
    ('D','DURA'),
    ('B','BLANDA'),
    ('L','LIQUIDA')
    )


class HematologiaForm(ModelForm):
    class Meta:
        model = Examen_Hematologia
        fields = ['paciente','edad','hemoglobina','mcv','mch','mchc','hematocrito','globulosBlancos','globulosRojos','plaquetas',
        'neutrofilos','linfocitos','monocitos','eosinofilos','basofilos','eritrosedimentacion','gotaGruesa']
        paciente = forms.ModelChoiceField(widget=forms.Select(attrs={'name':'paciente','class':'form-control'}),queryset=Paciente.objects.all(),label="PACIENTE",help_text="(*)")
        edad = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'edad','class':'form-control','min':'15','max':'80'}),label="EDAD",help_text="(*)")
        hemoglobina = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'hemoglobina','class':'form-control','min':'7.00','max':'20.00'}),label="HEMOGLOBINA",help_text="(*)")
        mcv = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'mcv','class':'form-control','min':'1.00','max':'20.00'}),label="MCV",help_text="(*)")
        mch = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'mch','class':'form-control','min':'1.00','max':'20.00'}),label="MCH",help_text="(*)")
        mchc = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'mchc','class':'form-control','min':'1.00','max':'20.00'}),label="MCHC",help_text="(*)")
        hematocrito = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'hematocrito','class':'form-control','min':'1','max':'100'}),label="HEMATOCRITO",help_text="(*)")
        globulosBlancos = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'globulosBlancos','class':'form-control','min':'1','max':'100000'}),label="GLOBULOS BLANCOS",help_text="(*)")
        globulosRojos = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'globulosRojos','class':'form-control','min':'1','max':'100000'}),label="GLOBULOS ROJOS",help_text="(*)")
        plaquetas = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'plaquetas','class':'form-control','min':'1','max':'10000'}),label="PLAQUETAS",help_text="(*)")
        neutrofilos = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'neutrofilos','class':'form-control','min':'1','max':'100'}),label="NEUTROFILOS",help_text="(*)")
        linfocitos = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'linfocitos','class':'form-control','min':'1','max':'100'}),label="LINFOCITOS",help_text="(*)")
        monocitos = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'monocitos','class':'form-control','min':'1','max':'100'}),label="MONOCITOS",help_text="(*)")
        eosinofilos = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'eosinofilos','class':'form-control','min':'1','max':'100'}),label="EOSINOFILOS",help_text="(*)")
        basofilos = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'basofilos','class':'form-control','min':'1','max':'100'}),label="BASOFILOS",help_text="(*)")
        eritrosedimentacion = forms.CharField(widget=forms.TextInput(attrs={'name':'eritrosedimentacion','maxlength':'500','class':'form-control'}),label="ERITROSEDIMENTACION",help_text="(*)")
        gotaGruesa = forms.CharField(widget=forms.TextInput(attrs={'name':'gotaGruesa','maxlength':'500','class':'form-control'}),label="GOTA GRUESA",help_text="(*)")

class orinaForm(ModelForm):
    class Meta:
        model = Examen_Orina
        fields=['paciente','edad','color','aspecto','ph','nitritos','densidad','proteinas','cetonicos','glucosa','bilirrubina',
        'urobilinigeno','leucocitos','hematies','epiteliales','cristales','cilindros','sangre','esterasaLeucocitaria','bacterias',
        'observaciones']
        paciente = forms.ModelChoiceField(widget=forms.Select(attrs={'name':'paciente','class':'form-control'}),queryset=Paciente.objects.all(),label="PACIENTE",help_text="(*)")
        edad = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'edad','class':'form-control','min':'15','max':'80'}),label="EDAD",help_text="(*)")
        color = forms.CharField(widget=forms.TextInput(attrs={'name':'color','maxlength':'25','class':'form-control'}),label="COLOR",help_text="(*)")
        aspecto = forms.CharField(widget=forms.TextInput(attrs={'name':'aspecto','maxlength':'25','class':'form-control'}),label="ASPECTO",help_text="(*)")
        ph = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'ph','class':'form-control','min':'3.00','max':'10.00'}),label="PH",help_text="(*)")
        nitritos = forms.CharField(max_length=10,widget=forms.Select(attrs={'name':'nitritos','class':'form-control'},choices=NITRITOS_OPCIONES),label="NITRITOS",help_text="(*)")
        densidad = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'densidad','class':'form-control','min':'900','max':'1100'}),label="DENSIDAD",help_text="(*)")
        proteinas = forms.CharField(widget=forms.TextInput(attrs={'name':'proteinas','maxlength':'30','class':'form-control'}),label="PROTEINAS",help_text="(*)")
        cetonicos = forms.CharField(widget=forms.TextInput(attrs={'name':'cetonicos','maxlength':'30','class':'form-control'}),label="C.CETONICOS",help_text="(*)")
        glucosa = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'glucosa','class':'form-control','min':'50','max':'400'}),label="GLUCOSA",help_text="(*)")
        bilirrubina = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'bilirrubina','class':'form-control','min':'0.00','max':'3.00'}),label="BILIRRUBINA",help_text="(*)")
        urobilinigeno = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'urobilinigeno','class':'form-control','min':'0.00','max':'3.00'}),label="UROBILINIGENO",help_text="(*)")
        leucocitos = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'leucocitos','class':'form-control','min':'1','max':'20'}),label="LEUCOCITOS",help_text="(*)")
        hematies = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'hematies','class':'form-control','min':'4.00','max':'9.00'}),label="HEMATIES",help_text="(*)")
        epileliales = forms.CharField(max_length=15,widget=forms.Select(attrs={'name':'epiteliales','class':'form-control'},choices=OPCIONES),label="CELULAS EPITELIALES",help_text="(*)")
        cristales = forms.CharField(max_length=20,widget=forms.Select(attrs={'name':'cristales','class':'form-control'},choices=CRISTALES_OPCIONES),label="CRISTALES",help_text="(*)")
        cilindros = forms.CharField(max_length=20,widget=forms.Select(attrs={'name':'cilindros','class':'form-control'},choices=CILINDROS_OPCIONES),label="CILINDROS",help_text="(*)")
        sangre = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'sangre','class':'form-control','min':'1','max':'400'}),label="SANGRE",help_text="(*)")
        esterasaLeucocitaria = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'esterasaLeucocitaria','class':'form-control','min':'1','max':'400'}),label="ESTERASA LEUCOCITARIA",help_text="(*)")
        bacterias = forms.CharField(max_length=15,widget=forms.Select(attrs={'name':'bacterias','class':'form-control'},choices=OPCIONES),label="BACTERIAS Y LEVADURAS",help_text="(*)")
        observaciones = forms.CharField(widget=forms.TextInput(attrs={'name':'observaciones','maxlength':'1000','class':'form-control'}),label="OBSERVACIONES",help_text="(*)")

class hecesForm(ModelForm):
    class Meta:
        model= Examen_Heces
        fields=['paciente','edad','color','consistencia','mucus','protoActivos','protoQuistes','metazoarios','hematies','leucocitos',
        'macro','micro','observaciones']
        paciente = forms.ModelChoiceField(widget=forms.Select(attrs={'name':'paciente','class':'form-control'}),queryset=Paciente.objects.all(),label="PACIENTE",help_text="(*)")
        edad = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'edad','class':'form-control','min':'15','max':'80'}),label="EDAD",help_text="(*)")
        color = forms.CharField(widget=forms.TextInput(attrs={'name':'color','maxlength':'25','class':'form-control'}),label="COLOR",help_text="(*)")
        consistencia = forms.CharField(widget=forms.TextInput(attrs={'name':'consistencia','maxlength':'25','class':'form-control'}),label="CONSISTENCIA",help_text="(*)")
        mucus = forms.CharField(widget=forms.TextInput(attrs={'name':'mucus','maxlength':'20','class':'form-control'}),label="MUCUS",help_text="(*)")
        protoActivos = forms.CharField(widget=forms.TextInput(attrs={'name':'protoActivos','maxlength':'40','class':'form-control'}),label="ACTIVOS",help_text="(*)")
        protoQuistes = forms.CharField(widget=forms.TextInput(attrs={'name':'protoQuistes','maxlength':'40','class':'form-control'}),label="QUISTES",help_text="(*)")
        metazoarios = forms.CharField(widget=forms.TextInput(attrs={'name':'metazoarios','maxlength':'40','class':'form-control'}),label="METAZOARIOS",help_text="(*)")
        hematies = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'hematies','class':'form-control','min':'4.00','max':'9.00'}),label="HEMATIES",help_text="(*)")
        leucocitos = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'leucocitos','class':'form-control','min':'1','max':'20'}),label="LEUCOCITOS",help_text="(*)")
        macro = forms.CharField(widget=forms.TextInput(attrs={'name':'macro','maxlength':'40','class':'form-control'}),label="MACRO",help_text="(*)")
        micro = forms.CharField(widget=forms.TextInput(attrs={'name':'micro','maxlength':'40','class':'form-control'}),label="MICRO",help_text="(*)")
        observaciones = forms.CharField(widget=forms.TextInput(attrs={'name':'observaciones','maxlength':'1000','class':'form-control'}),label="OBSERVACIONES",help_text="(*)")
    #def clean(self):
        #print self.cleaned_data
        #return self.cleaned_data

class generalForm(ModelForm):
    class Meta:
        model = Examen_General
        fields=['paciente','edad','colorHeces','consistencia','mucus','protoActivos','protoQuistes','metazoarios','hematiesHeces','leucocitosHeces',
        'macro','micro','colorOrina','aspecto','ph','nitritos','densidad','proteinas','cetonicos','glucosa','bilirrubina',
        'urobilinigeno','leucocitosOrina','hematiesOrina','epiteliales','cristales','cilindros','sangre','esterasaLeucocitaria','bacterias',
        'levaduras','otros','hematocrito','hemoglobina','serologia']
        colorHeces = forms.CharField(max_length=20,widget=forms.Select(attrs={'name':'colorHeces','maxlength':'25','class':'form-control'}),label="COLOR",help_text="(*)")
        consistencia = forms.CharField(max_length=20,widget=forms.Select(attrs={'name':'consistencia','maxlength':'25','class':'form-control'}),label="CONSISTENCIA",help_text="(*)")
        mucus = forms.CharField(widget=forms.TextInput(attrs={'name':'mucus','maxlength':'20','class':'form-control'}),label="MUCUS",help_text="(*)")
        protoActivos = forms.CharField(widget=forms.TextInput(attrs={'name':'protoActivos','maxlength':'40','class':'form-control'}),label="ACTIVOS",help_text="(*)")
        protoQuistes = forms.CharField(widget=forms.TextInput(attrs={'name':'protoQuistes','maxlength':'40','class':'form-control'}),label="QUISTES",help_text="(*)")
        metazoarios = forms.CharField(widget=forms.TextInput(attrs={'name':'metazoarios','maxlength':'40','class':'form-control'}),label="METAZOARIOS",help_text="(*)")
        hematiesHeces = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'hematiesHeces','class':'form-control','min':'4.00','max':'9.00'}),label="HEMATIES",help_text="(*)")
        leucocitosHeces = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'leucocitosHeces','class':'form-control','min':'1','max':'20'}),label="LEUCOCITOS",help_text="(*)")
        macro = forms.CharField(max_length=15,widget=forms.Select(attrs={'name':'macro','maxlength':'25','class':'form-control'}),label="MACRO",help_text="(*)")
        micro = forms.CharField(max_length=15,widget=forms.Select(attrs={'name':'micro','maxlength':'25','class':'form-control'}),label="MICRO",help_text="(*)")
        colorOrina = forms.CharField(widget=forms.TextInput(attrs={'name':'colorOrina','maxlength':'25','class':'form-control'}),label="COLOR",help_text="(*)")
        aspecto = forms.CharField(widget=forms.TextInput(attrs={'name':'aspecto','maxlength':'25','class':'form-control'}),label="ASPECTO",help_text="(*)")
        ph = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'ph','class':'form-control','min':'3.00','max':'10.00'}),label="PH",help_text="(*)")
        nitritos = forms.CharField(max_length=10,widget=forms.Select(attrs={'name':'nitritos','class':'form-control'},choices=NITRITOS_OPCIONES),label="NITRITOS",help_text="(*)")
        densidad = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'densidad','class':'form-control','min':'900','max':'1100'}),label="DENSIDAD",help_text="(*)")
        proteinas = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'proteinas','class':'form-control','min':'0','max':'20'}),label="PROTEINAS",help_text="(*)")
        cetonicos = forms.CharField(widget=forms.TextInput(attrs={'name':'cetonicos','maxlength':'30','class':'form-control'}),label="C.CETONICOS",help_text="(*)")
        glucosa = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'glucosa','class':'form-control','min':'50','max':'400'}),label="GLUCOSA",help_text="(*)")
        bilirrubina = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'bilirrubina','class':'form-control','min':'0.00','max':'3.00'}),label="BILIRRUBINA TOTAL",help_text="(*)")
        urobilinigeno = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'urobilinigeno','class':'form-control','min':'0.00','max':'3.00'}),label="UROBILINIGENO",help_text="(*)")
        leucocitosOrina = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'leucocitosOrina','class':'form-control','min':'1','max':'20'}),label="LEUCOCITOS",help_text="(*)")
        hematiesOrina = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'hematiesOrina','class':'form-control','min':'4.00','max':'9.00'}),label="HEMATIES",help_text="(*)")
        epileliales = forms.CharField(max_length=15,widget=forms.Select(attrs={'name':'epiteliales','class':'form-control'},choices=OPCIONES),label="CELULAS EPITELIALES",help_text="(*)")
        cristales = forms.CharField(max_length=20,widget=forms.Select(attrs={'name':'cristales','class':'form-control'},choices=CRISTALES_OPCIONES),label="CRISTALES",help_text="(*)")
        cilindros = forms.CharField(max_length=20,widget=forms.Select(attrs={'name':'cilindros','class':'form-control'},choices=CILINDROS_OPCIONES),label="CILINDROS",help_text="(*)")
        sangre = forms.CharField(widget=forms.TextInput(attrs={'name':'sangre','maxlength':'30','class':'form-control'}),label="SANGRE",help_text="(*)")
        esterasaLeucocitaria = forms.CharField(widget=forms.TextInput(attrs={'name':'esterasaLeucocitaria','maxlength':'30','class':'form-control'}),label="ESTERASA LEUCOCITARIA",help_text="(*)")
        bacterias = forms.CharField(max_length=15,widget=forms.Select(attrs={'name':'bacterias','class':'form-control'},choices=OPCIONES),label="BACTERIAS",help_text="(*)")
        levaduras = forms.CharField(max_length=15,widget=forms.Select(attrs={'name':'levaduras','class':'form-control'},choices=OPCIONES),label="LEVADURAS",help_text="(*)")
        otros = forms.CharField(widget=forms.TextInput(attrs={'name':'observaciones','maxlength':'500','class':'form-control'}),label="OTROS",help_text="(*)")
        hematocrito = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'hematocrito','class':'form-control','min':'1','max':'100'}),label="HEMATOCRITO",help_text="(*)")
        hemoglobina = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'hemoglobina','class':'form-control','min':'7.00','max':'20.00'}),label="HEMOGLOBINA",help_text="(*)")
        serologia = forms.CharField(widget=forms.TextInput(attrs={'name':'serologia','maxlength':'500','class':'form-control'}),label="SEROLOGIA",help_text="(*)")

class quimicaForm(ModelForm):
    class Meta:
        model = Examen_Quimica_Sanguinea
        fields=['paciente','edad','glucosa','glucosaPospandrial','colesterol','trigliceridos','acidoUrico','creatinina',
        'hdl','ldl','tgo','tgp','bilirrubinaTotal','bilirrubinaDirecta','bilirrubinaIndirecta','tiempoProtrombina',
        'tiempoTromboplastina','tiempoSangramiento','tiempoCoagulacion','eritrosedimentacion','glucosaAjustada',
        'pospandrialAjustada','colesterolAjustada','trigliceridosAjustada','uricoAjustada','creatininaAjustada',
        'hdlAjustada','ldlAjustada','tgoAjustada','tgpAjustada','bTotalAjustada','bDirectaAjustada','bIndirectaAjustada',
        'protrombinaAjustada','tromboplastinaAjustada','sangramientoAjustada','coagulacionAjustada','eritrosedimentacionAjustada']
        paciente = forms.ModelChoiceField(widget=forms.Select(attrs={'name':'paciente','class':'form-control'}),queryset=Paciente.objects.all(),label="PACIENTE",help_text="(*)")
        edad = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'edad','class':'form-control','min':'15','max':'80'}),label="EDAD",help_text="(*)")
        glucosa = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'glucosa','class':'form-control','min':'50','max':'400'}),label="GLUCOSA",help_text="(*)")
        glucosaPospandrial = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'glucosaPospandrial','class':'form-control','min':'120','max':'200'}),label="GLUCOSA POSPANDRIAL",help_text="(*)")
        colesterol = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'colesterol','class':'form-control','min':'60','max':'300'}),label="COLESTEROL",help_text="(*)")
        trigliceridos = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'trigliceridos','class':'form-control','min':'1','max':'500'}),label="TRIGLICERIDOS",help_text="(*)")
        acidoUrico = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'acidoUrico','class':'form-control','min':'2.00','max':'10.00'}),label="ACIDO URICO",help_text="(*)")
        creatinina = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'creatinina','class':'form-control','min':'0.00','max':'2.00'}),label="CREATININA",help_text="(*)")
        hdl = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'hdl','class':'form-control','min':'10','max':'100'}),label="HDL",help_text="(*)")
        ldl = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'ldl','class':'form-control','min':'5','max':'200'}),label="LDL",help_text="(*)")
        tgo = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'tgo','class':'form-control','min':'1','max':'80'}),label="TGO",help_text="(*)")
        tgp = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'tgp','class':'form-control','min':'4','max':'80'}),label="TGP",help_text="(*)")
        bilirrubinaTotal = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'bilirrubinaTotal','class':'form-control','min':'0.00','max':'3.00'}),label="BILIRRUBINA TOTAL",help_text="(*)")
        bilirrubinaDirecta = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'bilirrubinaDirecta','class':'form-control','min':'0.00','max':'2.00'}),label="BILIRRUBINA DIRECTA",help_text="(*)")
        bilirrubinaIndirecta = forms.DecimalField(widget=forms.NumberInput(attrs={'name':'bilirrubinaIndirecta','class':'form-control','min':'0.00','max':'1.00'}),label="BILIRRUBINA INDIRECTA",help_text="(*)")
        tiempoProtrombina = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'tiempoProtrombina','class':'form-control','min':'1','max':'25'}),label="TIEMPO DE PROTROMBINA",help_text="(*)")
        tiempoTromboplastina = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'tiempoTromboplastina','class':'form-control','min':'15','max':'100'}),label="TIEMPO DE TROMBOPLASTINA",help_text="(*)")
        tiempoSangramiento = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'tiempoSangramiento','class':'form-control','min':'1','max':'30'}),label="TIEMPO DE SANGRAMIENTO",help_text="(*)")
        tiempoCoagulacion = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'tiempoCoagulacion','class':'form-control','min':'3','max':'20'}),label="TIEMPO DE COAGULACION",help_text="(*)")
        eritrosedimentacion = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'eritrosedimentacion','class':'form-control','min':'1','max':'50'}),label="ERITROSEDIMENTACION",help_text="(*)")
        glucosaAjustada = forms.CharField(widget=forms.TextInput(attrs={'name':'glucosaAjustada','maxlength':'25','class':'form-control'}),label="GLUCOSA AJUSTADA",help_text="(*)")
        pospandrialAjustada = forms.CharField(widget=forms.TextInput(attrs={'name':'pospandrialAjustada','maxlength':'25','class':'form-control'}),label="GLUCOSA POSPANDRIAL AJUSTADA",help_text="(*)")
        colesterolAjustada = forms.CharField(widget=forms.TextInput(attrs={'name':'colesterolAjustada','maxlength':'25','class':'form-control'}),label="COLESTEROL AJUSTADO",help_text="(*)")
        trigliceridosAjustada = forms.CharField(widget=forms.TextInput(attrs={'name':'trigliceridosAjustada','maxlength':'25','class':'form-control'}),label="TRIGLICERIDOS AJUSTADOS",help_text="(*)")
        uricoAjustada = forms.CharField(widget=forms.TextInput(attrs={'name':'uricoAjustada','maxlength':'25','class':'form-control'}),label="ACIDO URICO AJUSTADO",help_text="(*)")
        creatininaAjustada = forms.CharField(widget=forms.TextInput(attrs={'name':'creatininaAjustada','maxlength':'25','class':'form-control'}),label="CREATININA AJUSTADA",help_text="(*)")
        hdlAjustada = forms.CharField(widget=forms.TextInput(attrs={'name':'hdlAjustada','maxlength':'25','class':'form-control'}),label="HDL AJUSTADO",help_text="(*)")
        ldlAjustada = forms.CharField(widget=forms.TextInput(attrs={'name':'ldlAjustada','maxlength':'25','class':'form-control'}),label="LDL AJUSTADO",help_text="(*)")
        tgoAjustada = forms.CharField(widget=forms.TextInput(attrs={'name':'tgoAjustada','maxlength':'25','class':'form-control'}),label="TGO AJUSTADO",help_text="(*)")
        tgpAjustada = forms.CharField(widget=forms.TextInput(attrs={'name':'tgpAjustada','maxlength':'25','class':'form-control'}),label="TGP AJUSTADO",help_text="(*)")
        bTotalAjustada = forms.CharField(widget=forms.TextInput(attrs={'name':'bTotalAjustada','maxlength':'25','class':'form-control'}),label="BILIRRUBINA TOTAL AJUSTADA",help_text="(*)")
        bDirectaAjustada = forms.CharField(widget=forms.TextInput(attrs={'name':'bDirectaAjustada','maxlength':'25','class':'form-control'}),label="BILIRRUBINA DIRECTA AJUSTADA",help_text="(*)")
        bIndirectaAjustada = forms.CharField(widget=forms.TextInput(attrs={'name':'bIndirectaAjustada','maxlength':'25','class':'form-control'}),label="BILIRRUBINA INDIRECTA AJUSTADA",help_text="(*)")
        protrombinaAjustada = forms.CharField(widget=forms.TextInput(attrs={'name':'protrombinaAjustada','maxlength':'25','class':'form-control'}),label="TIEMPO DE PROTROMBINA AJUSTADA",help_text="(*)")
        tromboplastinaAjustada = forms.CharField(widget=forms.TextInput(attrs={'name':'tromboplastinaAjustada','maxlength':'25','class':'form-control'}),label="TIEMPO DE TROMBOPLASTINA AJUSTADA",help_text="(*)")
        sangramientoAjustada = forms.CharField(widget=forms.TextInput(attrs={'name':'sangramientoAjustada','maxlength':'25','class':'form-control'}),label="TIEMPO DE SANGRAMIENTO AJUSTADO",help_text="(*)")
        coagulacionAjustada = forms.CharField(widget=forms.TextInput(attrs={'name':'coagulacionAjustada','maxlength':'25','class':'form-control'}),label="TIEMPO DE COAGULACION AJUSTADO",help_text="(*)")
        eritrosedimentacionAjustada = forms.CharField(widget=forms.TextInput(attrs={'name':'eritrosedimentacionAjustada','maxlength':'25','class':'form-control'}),label="ERITROSEDIMENTACION AJUSTADA",help_text="(*)")

class especialesForm(ModelForm):
    class Meta:
        model = Examen_Especiales
        fields=['paciente','edad','resultado','tipoExamen']
        paciente = forms.ModelChoiceField(widget=forms.Select(attrs={'name':'paciente','class':'form-control'}),queryset=Paciente.objects.all(),label="PACIENTE",help_text="(*)")
        edad = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'edad','class':'form-control','min':'15','max':'80'}),label="EDAD",help_text="(*)")
        tipoExamen = forms.CharField(widget=forms.TextInput(attrs={'name':'tipoExamen','maxlength':'25','class':'form-control'}),label="TIPO DE EXAMEN",help_text="(*)")
        resultado = forms.CharField(widget=forms.TextInput(attrs={'name':'resultado','maxlength':'100','class':'form-control'}),label="RESULTADOS",help_text="(*)")


class archivoForm(ModelForm):
    class Meta:
        model = Examen_Hematologia
        fields=['paciente','edad','archivo']
        paciente = forms.ModelChoiceField(widget=forms.Select(attrs={'name':'paciente','class':'form-control'}),queryset=Paciente.objects.all(),label="PACIENTE",help_text="(*)")
        edad = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'edad','class':'form-control','min':'15','max':'80'}),label="EDAD",help_text="(*)")
        archivo = forms.FileField(widget=forms.FileInput(attrs={'name':'archivo','class':'form-control'}),label="SELECCIONAR UN ARCHIVO",help_text="(*)")

class archivoOrinaForm(ModelForm):
    class Meta:
        model = Examen_Orina
        fields=['paciente','edad','archivo']
        paciente = forms.ModelChoiceField(widget=forms.Select(attrs={'name':'paciente','class':'form-control'}),queryset=Paciente.objects.all(),label="PACIENTE",help_text="(*)")
        edad = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'edad','class':'form-control','min':'15','max':'80'}),label="EDAD",help_text="(*)")
        archivo = forms.FileField(widget=forms.FileInput(attrs={'name':'archivo','class':'form-control'}),label="SELECCIONAR UN ARCHIVO",help_text="(*)")

class archivoHecesForm(ModelForm):
    class Meta:
        model = Examen_Heces
        fields=['paciente','edad','archivo']
        paciente = forms.ModelChoiceField(widget=forms.Select(attrs={'name':'paciente','class':'form-control'}),queryset=Paciente.objects.all(),label="PACIENTE",help_text="(*)")
        edad = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'edad','class':'form-control','min':'15','max':'80'}),label="EDAD",help_text="(*)")
        archivo = forms.FileField(widget=forms.FileInput(attrs={'name':'archivo','class':'form-control'}),label="SELECCIONAR UN ARCHIVO",help_text="(*)")

class archivoQuimicaForm(ModelForm):
    class Meta:
        model = Examen_Quimica_Sanguinea
        fields=['paciente','edad','archivo']
        paciente = forms.ModelChoiceField(widget=forms.Select(attrs={'name':'paciente','class':'form-control'}),queryset=Paciente.objects.all(),label="PACIENTE",help_text="(*)")
        edad = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'edad','class':'form-control','min':'15','max':'80'}),label="EDAD",help_text="(*)")
        archivo = forms.FileField(widget=forms.FileInput(attrs={'name':'archivo','class':'form-control'}),label="SELECCIONAR UN ARCHIVO",help_text="(*)")

class archivoEspecialesForm(ModelForm):
    class Meta:
        model = Examen_Especiales
        fields=['paciente','edad','archivo']
        paciente = forms.ModelChoiceField(widget=forms.Select(attrs={'name':'paciente','class':'form-control'}),queryset=Paciente.objects.all(),label="PACIENTE",help_text="(*)")
        edad = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'edad','class':'form-control','min':'15','max':'80'}),label="EDAD",help_text="(*)")
        archivo = forms.FileField(widget=forms.FileInput(attrs={'name':'archivo','class':'form-control'}),label="SELECCIONAR UN ARCHIVO",help_text="(*)")

class archivoNuevoIngresoForm(ModelForm):
    class Meta:
        model = Examen_General
        fields=['paciente','edad','archivo']
        paciente = forms.ModelChoiceField(widget=forms.Select(attrs={'name':'paciente','class':'form-control'}),queryset=Paciente.objects.all(),label="PACIENTE",help_text="(*)")
        edad = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'edad','class':'form-control','min':'15','max':'80'}),label="EDAD",help_text="(*)")
        archivo = forms.FileField(widget=forms.FileInput(attrs={'name':'archivo','class':'form-control'}),label="SELECCIONAR UN ARCHIVO",help_text="(*)")