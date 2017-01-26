from django.contrib import admin
from .models import GruposAlimentos,AlimentosGrupo
# Register your models here.
class GruposAlimentos_Admin(admin.ModelAdmin):
    list_display = ('codGrupoAlimento','nombre')
class AlimentosGrupo_Admin(admin.ModelAdmin):
    list_display = ('grupo','alimento')
    
admin.site.register(GruposAlimentos)    
admin.site.register(AlimentosGrupo,AlimentosGrupo_Admin)