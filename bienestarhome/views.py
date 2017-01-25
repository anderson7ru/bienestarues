from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.template import RequestContext

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def ingresar(request):
	if not request.user.is_anonymous():
		return redirect("index")
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username = usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request,acceso)
					qs = User.objects.get(username=usuario)
					if qs.id != 1:
						usr = UsuarioEmpleado.objects.get(codigoUsuario=qs.id)
						if usr.numeroIngresos == 0:
							return redirect("cambiar-pass",user=qs)
						else:
							messages.success(request,'Bienvenid@ '+usuario)
							return redirect("index")
					else:
							messages.success(request,'Bienvenid@ '+usuario)
							return redirect("index")		
				else:
					messages.error(request,'El Usuario no esta activo. Por favor, contactarse con el administrador, para resolver el problema')
					formulario = AuthenticationForm()
			else:
				messages.error(request,'Error de acceso. El Usuario y contrasena no coinciden o no existen')
				formulario = AuthenticationForm()
			"""if usuario and clave:
				#acceso = authenticate(username = usuario, password=clave)
				#formulario = AuthenticationForm()
				qs = User.objects.filter(username=usuario)
				if qs.count()==1:
					acceso = qs.first()
				else:
					acceso = qs.first()
				if not acceso:
					messages.error(request,'El Usuario no existe. Por favor, contactarse con el administrador, para resolver el problema')
					formulario = AuthenticationForm()
				elif not acceso.check_password(clave):
					messages.error(request,'La contrasena es incorrecta. Por favor, contactarse con el administrador, para resolver el problema')
					formulario = AuthenticationForm()
				elif not acceso.is_active():
					messages.error(request,'El Usuario no esta activo. Por favor, contactarse con el administrador, para resolver el problema')
					formulario = AuthenticationForm()
				else:
					login(request,acceso)
					messages.success(request,'Bienvenid@ '+usuario)
					return redirect("index")
			else:
				messages.error(request,'No hay datos que mostrar. Por favor, ingrese el usuario y la contrasena')
				formulario = AuthenticationForm()"""
					
	else:
		formulario = AuthenticationForm()
	return render(request, "layouts/login.html", {'formulario':formulario})
"""def ingresar(request):
	if not request.user.is_anonymous():
		return redirect("home")
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username = usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request,acceso)
					messages.success(request,'Bienvenid@ '+usuario)
					return redirect("home")
				else:
					messages.error(request,'El Usuario no esta activo. Por favor, contactarse con el administrador, para resolver el problema')
					formulario = AuthenticationForm()
			else:
				messages.error(request,'Error de acceso. El Usuario y contrasena no coinciden o no existen')
				formulario = AuthenticationForm()
	else:
		formulario = AuthenticationForm()
	return render(request, "registro/login.html", {'formulario':formulario})"""

@login_required(login_url='logins')
def cerrar(request):
	logout(request)
	return redirect("logins")

def welcome(request):
    return render(request, 'layouts/bienestarhome.html')

@login_required(login_url='logins')
def index(request):
    return render(request, 'layouts/bienestarhome.html') #index.html

def bad_request(request):
	response = render(request, 'registro/400.html')
	response.status_code = 400
	return response

def permission_denied(request):
	response = render(request, 'registro/403.html')
	response.status_code = 403
	return response
	
def page_not_found(request):
	response = render(request, 'registro/404.html')
	response.status_code = 404
	return response
	
def server_error(request):
	response = render(request, 'registro/500.html')
	response.status_code = 500
	return response