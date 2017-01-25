from django.contrib import admin
from cuentasusuariosapp.models import UsuarioEmpleado

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('codigoEmpleado','codigoUsuario')
	
admin.site.register(UsuarioEmpleado,UsuarioAdmin)