from django.contrib import admin
from citasmedicasapp.models import diasSemana, HorarioAtencion, Cita, Cancelacion

#filtros para admin
class HorarioAtencionAdmin(admin.ModelAdmin):
    list_display = ('codigoDoctor','horaInicio','horaFinal','pacienteConsulta')
    
class CitaAdmin(admin.ModelAdmin):
    list_display = ('codigoDoctor','paciente','fechaConsulta','horaConsulta','estadoConsulta')
    
class CancelacionAdmin(admin.ModelAdmin):
    list_display = ('codigoDoctor','fechaInicio','horaInicio')
    
admin.site.register(diasSemana)
admin.site.register(HorarioAtencion,HorarioAtencionAdmin)
admin.site.register(Cita,CitaAdmin)
admin.site.register(Cancelacion,CancelacionAdmin)