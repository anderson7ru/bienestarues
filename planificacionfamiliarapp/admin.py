from django.contrib import admin
from planificacionfamiliarapp.models import PacienteInscripcion, PacienteSubSecuentePF

#filtros para admin
class PlanificacionFamiliarAdmin(admin.ModelAdmin):
    list_display = ('paciente','fechaIngreso')
	
class PacienteSubSecuentePFAdmin(admin.ModelAdmin):
    list_display = ('pacienteInscrito','fechaIngreso','tipoConsulta')
    
admin.site.register(PacienteInscripcion,PlanificacionFamiliarAdmin)
admin.site.register(PacienteSubSecuentePF,PacienteSubSecuentePFAdmin)
