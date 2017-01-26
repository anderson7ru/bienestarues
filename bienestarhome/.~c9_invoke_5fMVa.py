from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from cuentas_usuarioapp.models import UsuarioEmpleado
from cuentas_usuarioapp.forms import CambiarPassword


# Create your views here.
def welcome(request):
    return render(request, 'layouts/bienestarhome.html')

@login_required(login_url='logins')
def index(request):
	return render(request, 'layouts/index.html')

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
					usr = UsuarioEmpleado.objects.get(codigoUsuario=qs.id)
					if usr.numeroIngresos == 0:
						return redirect("cambiar-pass",user=qs)
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

@login_required(login_url='logins')
def cerrar(request):
	logout(request)
	return redirect("logins")
	
@login_required(login_url='logins')
def cambioPassword(request,user):
	form = CambiarPassword()
	if request.method == 'POST':
		form = CambiarPassword(request.POST)
		#p1 = request.POST['pass1']
		#p2 = request.POST['pass2']
		if form.is_valid():
			x = form.cleaned_data
			usr = User.objects.get(username=user)
			usr.set_password(x.get('pass1'))
			usr.save()
			aux = UsuarioEmpleado.objects.get(codigoUsuario=usr.id)
			if aux.numeroIngresos == 0:
				aux.numeroIngresos += 1
				aux.save()
			messages.success(request,"El Password se cambio con exito!!")
			return redirect("index")
		else:
			#messages.success(request,"Falla la validacion")
			return render(request,"cuentas_usuarioapp/cambio_password.html",{'form':form})
	else:
		return render(request,"cuentas_usuarioapp/cambio_password.html",{'form':form})
		
def resetPassword(request):
	form = PasswordResetForm()
	if request.method == 
		form = PasswordResetForm(request.POST)
		if form.is_valid():
			x = form.save(commit=False)
			x.a