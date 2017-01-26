from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#apps internas y externas
from datospersonalesapp.models import Paciente
from signosvitalesapp.models import SignosVitales
from signosvitalesapp.forms import SignosForm

#Listado de las personas a las que se les han tomado los signos vitales
@login_required(login_url='logins')
def signosvitales_list(request):
    signos=SignosVitales.objects.order_by('-fechaIngreso','-horaIngreso')
    return render(request,"signosvitales/signosvitales_list.html",{'signos':signos})

#View para agregar los signos vitales a un determinado paciente
@login_required(login_url='logins')
def signosvitales_nuevo(request,pk):
    paciente = Paciente.objects.filter(codigoPaciente=pk)
    form=SignosForm()
    if request.method == "POST":
        form = SignosForm(request.POST)
        if form.is_valid():
            signosV = form.save(commit=False)
            datos = Paciente.objects.g(codigoPaciente=pk)
            signosV.edad=datos.edad_paciente()
            signosV.save()
            messages.success(request,'Se han registrado exitosamente los signos vitales del paciente con el Expediente: '+datos.codigoPaciente)
            return redirect("signosvitales-list")
        else:
            form=SignosForm()
    return render(request,"signosvitales/signos_editar.html",{'form':form,'paciente':paciente})
	
#View para consultar los signos vitales de un determinado paciente
@login_required(login_url='logins')
def signosvitales_detalle(request, pk):
	signosV = SignosVitales.objects.get(pk=pk) 
	datos =  Paciente.objects.get(codigoPaciente=signosV.paciente_id)
	return render(request, "signosvitales/signos_detalle.html", {'signos': signosV,'datos':datos})