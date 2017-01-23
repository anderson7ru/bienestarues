from django import template
from django.contrib.auth.models import User 
from empleadosapp.models import Doctor
from cuentas_usuarioapp.models import UsuarioEmpleado #eso era solo hacia falta eso de cuentas_usuarioapp.models

register = template.Library() 

@register.filter(name='id_doctor') 
def has_group(user):
	empleado = UsuarioEmpleado.objects.get(codigoUsuario=user)
	doctor = Doctor.objects.get(codigoEmpleado=empleado.codigoEmpleado)
	#doctor.codigoDoctor  	
	#doctor = Doctor.objects.get(codigoEmpleado=user.codigoEmpleado) #Version codigoEmpleado en User
	return doctor.codigoDoctor 