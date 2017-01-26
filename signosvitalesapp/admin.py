from django.contrib import admin

# Register your models here.
from signosvitalesapp.models import SignosVitales

#filtro
class SignosVitalesAdmin(admin.ModelAdmin):
    list_display = ('paciente','fechaIngreso','horaIngreso')
    #list_filter = ('paciente','fechaIngreso')

admin.site.register(SignosVitales,SignosVitalesAdmin)