# -*- coding: utf-8 -*-
from django import forms
from django.forms import Form
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm,PasswordResetForm
# apps internas y externas
from empleadosapp.models import Empleado
from cuentas_usuarioapp.models import UsuarioEmpleado

UserModel = get_user_model()

#.filter(estadoEmpleado='A') .... agregar estadoEmpleado en Empleado
class UsuarioForm(Form):
	codigoEmpleado = forms.ModelChoiceField(widget=forms.Select(attrs={'name':'empleado','class':'selectpicker','data-live-search':'true'}),queryset=Empleado.objects.exclude(codigoEmpleado__in=UsuarioEmpleado.objects.all().values_list('codigoEmpleado_id')),label="Empleado",help_text="(*)")
	email = forms.EmailField(widget=forms.EmailInput(attrs={'name':'email','class':'form-control','id':'email','maxlength':'30'}),label="Email",help_text="(*)")
	grupos = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'name':'grupos[]','class':'checkbox-inline'}),queryset=Group.objects.all())
	#password = forms.CharField(widget=forms.TextInput(attrs={'name':'clave','maxlength':'16','class':'form-control','value':'{{pass}}'}),label="Clave",help_text="(*)")
"""
class CrearUsuario(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'name':'usuario','maxlength':'50','class':'form-control'}),label="Usuario",help_text="(*)")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'name':'contra1','maxlength':'50','class':'form-control'}),label="Contrasena",help_text="(*)")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'name':'contra2','maxlength':'50','class':'form-control'}),label="Contrasena",help_text="(*)")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'name':'correo','class':'form-control'}),label="correo",required=False)
    nombres = forms.CharField(widget=forms.TextInput(attrs={'name':'nombres','maxlength':'50','class':'form-control'}),label="Nombres",help_text="(*)")
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'name':'apellidos','maxlength':'50','class':'form-control'}),label="Apellidos",help_text="(*)")
    grupos = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'name':'grupos','class':'checkbox-inline'}),queryset=Group.objects.all())
    class Meta:
        model = User
        fields = ('username','password1','password2','email','nombres','apellidos','grupos')
        
    def save(self,commit=True):
        user = super(UserCreationForm,self).save(commit=False)
        user.username = self.cleaned_data["username"]
        user.password1 = self.cleaned_data["password1"]
        user.password2 = self.cleaned_data["password2"]
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["nombres"]
        user.last_name = self.cleaned_data["apellidos"]
        #user.groups = self.cleaned_data["grupos"]
        if commit:
            user.save()
        return user        """
class CambiarPassword(forms.Form):

    pass1 = forms.CharField(label="Nuevo Password",widget=forms.PasswordInput(attrs={"class":'form-control','name':'pass1'}))
    pass2 = forms.CharField(label="Confirmar Password",widget=forms.PasswordInput(attrs={"class":'form-control','name':'pass2'}))
    
class ResetPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'name':'correo','class':'form-control'}),label="Correo Electronico",max_length=254)

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        """
        Sends a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, 'text/html')

        email_message.send()

    def get_users(self, email):
        """Given an email, return matching user(s) who should receive a reset.
        This allows subclasses to more easily customize the default policies
        that prevent inactive users and users with unusable passwords from
        resetting their password.
        """
        active_users = UserModel._default_manager.filter(**{
            'email__iexact': email,
            'is_active': True,
        })
        return (u for u in active_users if u.has_usable_password())

    def save(self, domain_override=None,
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None,
             extra_email_context=None):
        """
        Generates a one-use only link for resetting password and sends to the
        user.
        """
        email = self.cleaned_data["email"]
        for user in self.get_users(email):
            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
            context = {
                'email': email,
                'domain': domain,
                'site_name': site_name,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': 'https' if use_https else 'http',
            }
            if extra_email_context is not None:
                context.update(extra_email_context)
            self.send_mail(
                subject_template_name, email_template_name, context, from_email,
                email, html_email_template_name=html_email_template_name,
            )

    
    