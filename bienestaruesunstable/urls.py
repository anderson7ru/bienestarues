"""bienestaruesunstable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    # generalapp
    url(r'^generalapp/', include('generalapp.urls')),
    
    # # consulta general - anderson
    # url(r'^general/', include('iconsultageneralapp.urls')),
    
    url('^', include('django.contrib.auth.urls')),
    
     url(r'^', include('bienestarhome.urls')),
     url(r'^chaining/', include('smart_selects.urls')), #para selecciones dependientes
    
    # #Para el expediente provisional de los alumnos de nuevo ingreso
     url(r'^', include('nuevoingresoapp.urls')),
    
    # #Para colas de enfermeria ya sea signos vitales o consulta
     url(r'^', include('enfermeriaapp.urls')),
    
    # #Para laboratorio clinico
     url(r'^', include('laboratorioapp.urls')),
     
    # #Para Reportes de Enfermeria y Archivo
     url(r'^', include('reportesapp.urls')),
    
    # #Para el expediente permanente de los pacientes
     url(r'^datosPersonales/',include('datospersonalesapp.urls')),
    
    # #Para Planificacion Familiar
    url(r'^planificacionfam/',include('planificacionfamiliarapp.urls')),
    
    # #Para Signos Vitales
    url(r'^signosvitales/',include('signosvitalesapp.urls')),
    
    # #Para citas medicas
     url(r'^citas/',include('citasmedicasapp.urls')),
    
    # #Para Empleados de Bienestar
     url(r'^empleados/',include('empleadosapp.urls')),
    
    #url para Psicologia
     url(r'^psicologia/',include('psicologiaapp.urls')),
     
     #url para usuarios
     url(r'^usuarios/',include('cuentas_usuarioapp.urls')),
     
     #url para nutricion
     url(r'^nutricion/',include('nutricionapp.urls'))
]