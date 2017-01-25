from django import template
from django.contrib.auth.models import User 
from empleadosapp.models import Doctor
from cuentasusuariosapp.models import UsuarioEmpleado

register = template.Library() 

@register.filter(name='id_doctor') 
def id_doctor(user):
	empleado = UsuarioEmpleado.objects.get(codigoUsuario=user)
	doctor = Doctor.objects.get(codigoEmpleado=empleado.codigoEmpleado)
	#doctor.codigoDoctor  	
	#doctor = Doctor.objects.get(codigoEmpleado=user.codigoEmpleado) #Version codigoEmpleado en User
	return doctor.codigoDoctor 