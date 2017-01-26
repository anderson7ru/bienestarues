from django.contrib import admin
from laboratorioapp.models import Examen_Hematologia,Examen_Heces,Examen_Orina,Examen_General, Examen_Quimica_Sanguinea, Examen_Especiales

# A continuacion se presentan los modelos de el modulo de laboratorio registrados en el admin de django.

class Examen_Hematologia_Admin(admin.ModelAdmin):
    list_display = ('codExamen_Hematologia','paciente')

class Examen_Heces_Admin(admin.ModelAdmin):
    list_display = ('codExamen_Heces','paciente')

class Examen_Orina_Admin(admin.ModelAdmin):
    list_display = ('codExamen_Orina','paciente')

class Examen_General_Admin(admin.ModelAdmin):
    list_display = ('codExamen_General','paciente')

class Examen_Quimica_Sanguinea_Admin(admin.ModelAdmin):
    list_display = ('codExamen_Quimica','paciente')

class Examen_Especiales_Admin(admin.ModelAdmin):
    list_display = ('codExamen_Especiales','paciente')

admin.site.register(Examen_Especiales,Examen_Especiales_Admin)
admin.site.register(Examen_Quimica_Sanguinea,Examen_Quimica_Sanguinea_Admin)
admin.site.register(Examen_Hematologia,Examen_Hematologia_Admin)
admin.site.register(Examen_Heces,Examen_Heces_Admin)
admin.site.register(Examen_Orina,Examen_Orina_Admin)
admin.site.register(Examen_General,Examen_General_Admin)