from django.contrib import admin
from enfermeriaapp.models import Cola_Enfermeria, Cola_Consulta

# Register your models here.
class Cola_Consulta_Admin(admin.ModelAdmin):
    list_display = ('idCola','nit','idDoctor','hora')

class Cola_Enfermeria_Admin(admin.ModelAdmin):
    list_display = ('idCola','idPaciente','hora')

admin.site.register(Cola_Consulta,Cola_Consulta_Admin)
admin.site.register(Cola_Enfermeria,Cola_Enfermeria_Admin)

# Register your models here.
