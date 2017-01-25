from django.contrib import admin
from empleadosapp.models import Empleado, Doctor, Especialidad, Laboratorista

#filtros para admin
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombrePrimero','apellidoPrimero','cargo')
    
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('codigoEmpleado','especialidad')
    
admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Especialidad)
admin.site.register(Laboratorista)