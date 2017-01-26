from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from .forms import UsuarioForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from cuentas_usuarioapp.models import UsuarioEmpleado

"""def crear_usuario(request):
    if request.method == "POST":
        form = CrearUsuario(request.POST)
        #messages.success(request,'Antes de is_valid')
        if form.is_valid():
            #messages.success(request,'Entro a is_valid')
            x = form.save(commit=False)
            x.save()
            x.groups = request.POST.getlist('grupos')
            x.save()
            messages.success(request,'Usuario '+request.POST.get('usuario')+ ' Creado Satisfactoriamente')
        else:
            messages.success(request,'No entra a is_valid')    
    else:
        #messages.success(request,'Error')
        form=CrearUsuario()        
            
    return render(request,"cuentas_usuarioapp/crear.html",{'form':form}) """

def empleado_usuario(request):
	formU = UsuarioForm()
	if request.method == "POST":
		formU = UsuarioForm(request.POST)
		if formU.is_valid():
			userAux = formU.cleaned_data
			aux = userAux.get('codigoEmpleado')
			
			user = User.objects.create_user(aux.apellidoPrimero,userAux.get('email'),userAux.get('password'))
			user.last_name=aux.apellidoPrimero
			user.first_name=aux.nombrePrimero
			user.save()
			codigoU = User.objects.order_by('-id')[0]
			UsuarioEmpleado.objects.create(codigoEmpleado=aux,codigoUsuario=codigoU)
			messages.success(request,'Se han guardado los datos del Usuario Exitosamente')
			return redirect('empleadosuario-new')
		else:
			formU = UsuarioForm()
	return render(request,"cuentas_usuarioapp/empleado_usuario.html",{'form':formU})
	
def generausername(data):
    limiteNombre = len(data.nombrePrimero)
    limiteApellido = len(data.apellidoPrimero)
    usr = data.nombrePrimero[:random.randint(0,limiteNombre)] + data.apellidoPrimero[:random.randint(0,limiteApellido)] + str(random.randint(0,99))
    return usr
    
def generarpassword():
    cadena = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890$/*-.@"
    longitudCadena = len(cadena)
    psw = ""
    longitudPsw=10
    for i in range(0,longitudPsw):
        pos = random.randint(0,longitudCadena-1)
        psw = psw + cadena[pos]
    return psw    