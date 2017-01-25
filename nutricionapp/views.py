from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from bienestarhome.admin import is_nutricionista, is_usuario1
from datospersonalesapp.models import Paciente
from signosvitalesapp.models import SignosVitales
from .forms import NutricionForm, DatosNutricionalesForm
from .models import Nutricion, GruposAlimentos, AlimentosGrupo
import json
# Create your views here.
@login_required(login_url='logins')
@user_passes_test(is_usuario1)
def nutricion_lista(request):
    pacientes = Nutricion.objects.select_related('paciente')
    return render(request,'nutricion/nutricion_listado.html',{'pacientes':pacientes})

@login_required(login_url='logins')
@user_passes_test(is_nutricionista)	
def nutricion_nuevo(request,paciente):
    datos = Paciente.objects.get(pk=paciente)
    edad = datos.edad_paciente
    sexo = datos.sexo
    signos = SignosVitales.objects.get(paciente=datos.codigoPaciente)
    form = NutricionForm()
    if request.method == 'POST':
        form = NutricionForm(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.paciente_id = paciente
            x.nombreRecibido = request.user
            x.save()
            messages.success(request,"Datos del expediente de Nutricion guardados exitosamente")
            aux = Nutricion.objects.get(paciente=x.paciente)
            return redirect('datosNutricionales-new',pk=aux.codNutricion)
        else:
            messages.success(request,"error en datos")
            return render(request,"nutricion/nutricion_nuevo.html",{'form':form,'datos':datos,'signos':signos,'sexo':sexo,'edad':edad})
    else:
        return render(request,"nutricion/nutricion_nuevo.html",{'form':form,'datos':datos,'signos':signos,'sexo':sexo,'edad':edad})

@login_required(login_url='logins')
@user_passes_test(is_nutricionista)        
def datosNutricionales_nuevo(request,pk):
        
    form = DatosNutricionalesForm()
    gp = GruposAlimentos.objects.all()
    if request.method == 'POST':
        form = DatosNutricionalesForm(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.nutricion_id = pk
            x.nombreRecibido = request.user
            x.save()
            messages.success(request,"Datos Nutricionales guardados exitosamente")
            return redirect('nutricion-list')
    else:
        return render(request,"nutricion/datosnutricionales_nuevo.html",{'form':form,'grupos':gp})