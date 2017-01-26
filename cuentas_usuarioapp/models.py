# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from empleadosapp.models import Empleado

class UsuarioEmpleado(models.Model):
	codigoEmpleado = models.OneToOneField(Empleado, on_delete=models.CASCADE,)
	codigoUsuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
	numeroIngresos = models.PositiveSmallIntegerField(default=0)
	
	def __str__(self):
		return '%s' % (self.codigoEmpleado)