from django.contrib import admin
from .models import ProcesoTerapeutico,Psicologia,RegistroAvance
from datospersonalesapp.models import Paciente

#funcion para verificar q el usuario logueado es psicologo
"""def is_psicologo(user):
    return user.groups.filter(name='psicologos').exists()"""

# Register your models here.
class Psicologia_Admin(admin.ModelAdmin):
    list_display = ('codPsicologia','paciente','fecha','motivo')
    
class ProcesoTerapeutico_Admin(admin.ModelAdmin):
    list_display = ('codPsicologia','fecha')
    
class RegistroAvance_Admin(admin.ModelAdmin):
    list_display = ('codRegistroAvance','codProcesoTerapeutico','fechaRegistro')
    
admin.site.register(Psicologia,Psicologia_Admin)
admin.site.register(ProcesoTerapeutico,ProcesoTerapeutico_Admin)
admin.site.register(RegistroAvance,RegistroAvance_Admin)