from django.contrib import admin
from datospersonalesapp.models import Paciente, Facultad, Municipio, Departamento

#filtros para admin
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('codigoPaciente','facultadE','nombrePrimero','apellidoPrimero')

class FacultadAdmin(admin.ModelAdmin):
    list_display = ('codigoFacultad','nombreFacultad')
    
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('codigoDepartamento','nombreDepartamento')
    
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nombreMunicipio','codDepartamento')
    
admin.site.register(Facultad,FacultadAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Paciente,PacienteAdmin)
