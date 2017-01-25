from django.shortcuts import render,resolve_url,redirect
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse,reverse_lazy
from django.contrib.auth.views import deprecate_current_app
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.contrib.auth.tokens import default_token_generator
from django.utils.deprecation import RemovedInDjango20Warning
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils.encoding import force_text

from django.http import HttpResponseRedirect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
import random
import warnings
from email.mime.text import MIMEText
from smtplib import SMTP 
from django.core.mail import send_mail

from bienestarhome.admin import is_director1
from .forms import UsuarioForm
from django.contrib.auth.models import Group
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from cuentasusuariosapp.models import UsuarioEmpleado
from cuentasusuariosapp.forms import CambiarPassword,ResetPasswordForm
from empleadosapp.models import Empleado

UserModel = get_user_model()

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
            
    return render(request,"cuentas_usuarioapp/crear.html",{'form':form})"""

@login_required(login_url='logins')
@user_passes_test(is_director1)
def empleado_usuario(request):
	formU = UsuarioForm()
	psw = generarpassword()
	if request.method == "POST":
		formU = UsuarioForm(request.POST)
		#codEmp = request.POST.get('empleado')
		#dataemp = Empleado.objects.get(pk=codEmp)
		#usr = generausername(dataemp)
		if formU.is_valid():
			userAux = formU.cleaned_data
			aux = userAux.get('codigoEmpleado')
			dataemp = aux.nombrePrimero + ' '+ aux.apellidoPrimero
			usr = generausername(dataemp)
			passw = request.POST.get('password')
			user = User.objects.create_user(usr,userAux.get('email'),passw)
			user.last_name=aux.apellidoPrimero
			user.first_name=aux.nombrePrimero
			user.save()
			codigoU = User.objects.order_by('-id')[0]
			UsuarioEmpleado.objects.create(codigoEmpleado=aux,codigoUsuario=codigoU)
			user.groups = request.POST.getlist('grupos')
			user.save()
			messages.success(request,'Se han guardado los datos del Usuario Exitosamente')
			remitente = "Bienestar Universitario <bienestaruessv@gmail.com>"
			destinatario = dataemp.split(' ')[0] +' '+ dataemp.split(' ')[1] + "<"+user.email+">"
			asunto = "Credenciales BU"
			saludo = "Este es un e-mail enviando desde el Sistema Informatico de gestion de expedientes y citas de Bienestar Universitario, UES"
			mensaje = "Hola!\n"+saludo+"\nNombre de usuario: "+ usr +"\n" + "Password: "+ passw + \
			"\n\n\nDebera cambiar en el primer ingreso su contrase&ntilde;a y luego si deseea podra cambiar su nombre de usuario."
			mime_message = MIMEText(mensaje)
			mime_message["From"] = remitente
			mime_message["To"] = destinatario        
			mime_message["Subject"] = asunto     
			smtp = SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
			smtp.ehlo()
			smtp.starttls()
			smtp.ehlo()
			smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
			smtp.sendmail(remitente, destinatario, mime_message.as_string())
			smtp.quit() 
			return redirect('empleadosuario-new')
		else:
		    messages.success(request,'No validos')
		    formU = UsuarioForm()
	return render(request,"cuentas_usuarioapp/empleado_usuario.html",{'form':formU,'pass':psw})
	
def generausername(data):
    nombre = data.split(' ')
    #limiteNombre = len(nombre[0])
    #limiteApellido = len(nombre[1])
    usr = nombre[0] +'.'+ nombre[1] + str(random.randint(1,99))
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
    
#Sobreescritura de las vista de django para poder aceptar passwords mas sencillas
@deprecate_current_app
@csrf_protect
def password_reset(request,
                   template_name='registration/password_reset_form.html',
                   email_template_name='registration/password_reset_email.html',
                   subject_template_name='registration/password_reset_subject.txt',
                   password_reset_form=ResetPasswordForm,
                   token_generator=default_token_generator,
                   post_reset_redirect=None,
                   from_email=None,
                   extra_context=None,
                   html_email_template_name=None,
                   extra_email_context=None):
    warnings.warn("The password_reset() view is superseded by the "
                  "class-based PasswordResetView().",
                  RemovedInDjango20Warning, stacklevel=2)
    if post_reset_redirect is None:
        post_reset_redirect = reverse('password_reset_done')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    if request.method == "POST":
        form = password_reset_form(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': token_generator,
                'from_email': from_email,
                'email_template_name': email_template_name,
                'subject_template_name': subject_template_name,
                'request': request,
                'html_email_template_name': html_email_template_name,
                'extra_email_context': extra_email_context,
            }
            form.save(**opts)
            return HttpResponseRedirect(post_reset_redirect)
    else:
        form = password_reset_form()
    context = {
        'form': form,
        'title': 'Password reset',
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)
    
@deprecate_current_app
def password_reset_done(request,
                        template_name='registration/password_reset_done.html',
                        extra_context=None):
    warnings.warn("The password_reset_done() view is superseded by the "
                  "class-based PasswordResetDoneView().",
                  RemovedInDjango20Warning, stacklevel=2)
    context = {
        'title': 'Password reset sent',
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)
    
@sensitive_post_parameters()
@never_cache
@deprecate_current_app
def password_reset_confirm(request, uidb64=None, token=None,
                           template_name='registration/password_reset_confirm.html',
                           token_generator=default_token_generator,
                           set_password_form=CambiarPassword,
                           post_reset_redirect=None,
                           extra_context=None):
    """
    View that checks the hash in a password reset link and presents a
    form for entering a new password.
    """
    warnings.warn("The password_reset_confirm() view is superseded by the "
                  "class-based PasswordResetConfirmView().",
                  RemovedInDjango20Warning, stacklevel=2)
    assert uidb64 is not None and token is not None  # checked by URLconf
    if post_reset_redirect is None:
        post_reset_redirect = reverse('password_reset_complete')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    try:
        # urlsafe_base64_decode() decodes to bytestring on Python 3
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        validlink = True
        title = 'Entre el nuevo Password'
        if request.method == 'POST':
            form = set_password_form(request.POST)
            #messages.success(request, "hola "+user)
            if form.is_valid():
                x = form.cleaned_data
                usr = User.objects.get(username=user)
                usr.set_password(x.get('pass1'))
                usr.save()
                return HttpResponseRedirect(post_reset_redirect)
        else:
            form = set_password_form()
    else:
        validlink = False
        form = None
        title = 'Password no reestablecido'
    context = {
        'form': form,
        'title': title,
        'validlink': validlink,
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)


@deprecate_current_app
def password_reset_complete(request,
                            template_name='registration/password_reset_complete.html',
                            extra_context=None):
    warnings.warn("The password_reset_complete() view is superseded by the "
                  "class-based PasswordResetCompleteView().",
                  RemovedInDjango20Warning, stacklevel=2)
    context = {
        'login_url': resolve_url(settings.LOGIN_URL),
        'title': 'Password Reestablecido correctamente',
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)
