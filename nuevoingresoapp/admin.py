from django.contrib import admin
from datospersonalesapp.models import Facultad, Departamento, Municipio, Paciente
from nuevoingresoapp.models import Expediente_Provisional, Actividad_Enfermeria, Censo_Enfermeria, Certificado_Salud

# Register your models here.
#filtro
class Exp_Provisional_Admin(admin.ModelAdmin):
    list_display = ('Cod_Expediente_Provisional','facultad','nombrePrimero','apellidoPrimero')

class Actividad_Enfermeria_Admin(admin.ModelAdmin):
    list_display = ('codActividad','nombreActividad')

class Censo_Enfermeria_Admin(admin.ModelAdmin):
    list_display = ('codCenso','actividad')

class Certificado_Salud_Admin(admin.ModelAdmin):
    list_display = ('codigoCertificado','codigoPaciente','codigoDoctor','nombreRecibido')

admin.site.register(Expediente_Provisional,Exp_Provisional_Admin)
admin.site.register(Actividad_Enfermeria,Actividad_Enfermeria_Admin)
admin.site.register(Censo_Enfermeria,Censo_Enfermeria_Admin)
admin.site.register(Certificado_Salud,Certificado_Salud_Admin)