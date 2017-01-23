from django.contrib import admin
from generalapp.models import ReferenciaExterna, Consulta

# Register your models here.
class ReferenciaExterna_Admin(admin.ModelAdmin):
    list_display = ('nombre_paciente','referido_a')

class Consulta_Admin(admin.ModelAdmin):
    list_display = ('cod_expediente','visto_bueno')

admin.site.register(ReferenciaExterna,ReferenciaExterna_Admin)
admin.site.register(Consulta,Consulta_Admin)