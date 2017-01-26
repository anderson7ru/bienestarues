from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from planificacionfamiliarapp.models import PacienteInscripcion, PacienteSubSecuentePF
from datospersonalesapp.models import Paciente
from planificacionfamiliarapp.forms import PlanificacionFamForm, PlanificacionSubForm

#Listado de pacientes inscritas en planificacion familiar
@login_required(login_url='logins')
def planificacionfamiliar_list(request):
    paciente=PacienteInscripcion.objects.order_by('-fechaIngreso')
    return render(request,"planificacionfamiliar/planificacion_list.html",{'planificadora':paciente})

#View para la inscripcion de pacientes a planificacion familiar
@login_required(login_url='logins')
def planificacionfamiliar_nuevo(request):
    formP=PlanificacionFamForm()
    if request.method == "POST":
        formP = PlanificacionFamForm(request.POST)
        if formP.is_valid():
            paciente = formP.save(commit=False)
            datos = Paciente.objects.get(codigoPaciente=paciente.paciente_id)
            paciente.edad=datos.edad_paciente()
            paciente.save()
            messages.success(request,'El paciente con el Expediente: '+datos.codigoPaciente+' se ha inscrito exitosamente a Planificacion Familiar')
            return redirect("planificacionfamiliar-view",pk=paciente.pk)
        else:
            formP=PlanificacionFamForm()
    return render(request,"planificacionfamiliar/inscripcion_editar.html",{'form':formP})
	
#View para consultar determinado paciente, inscrito en planificacion familiar
@login_required(login_url='logins')
def planificacionfamiliar_detalle(request, pk):
    paciente = PacienteInscripcion.objects.get(pk=pk) 
    datos =  Paciente.objects.get(codigoPaciente=paciente.paciente_id)
    return render(request, "planificacionfamiliar/inscripcion_detalle.html", {'paciente': paciente,'datos':datos})
	
#En caso que soliciten que se pueda modificar el formulario de inscripcion
#View para modificar la inscripcion de las pacientes de planificacion familiar
@login_required(login_url='logins')
def planificacionfamiliar_modificar(request, pk):
	""" 
	paciente = Paciente.objects.get(pk=pk) 
	if request.method == "POST":
		formP = PlanificacionFamForm(request.POST,instance=paciente)
		if formP.is_valid():
			paciente = formP.save(commit=False)
			datos = Paciente.objects.get(codigoPaciente=paciente.paciente_id)
            paciente.edad=datos.edad_paciente()
            paciente.save()
            messages.success(request,'Se ha modificado exitosamente la ficha de inscripcion del Paciente con Expediente: '+datos.codigoPaciente)
            return redirect("planificacionfamiliar-view",pk=paciente.pk)
	else:
		formP=PlanificacionFamForm(instance=paciente)
	return render(request,"planificacionfamiliar/inscripcion_editar.html",{'form':formP}) """ 
	
#Lista de consultas subsecuentes de un determinado paciente ya inscrito
@login_required(login_url='logins')
def planificacionfamiliar_subsecuente(request, pk):
	pacientePlanificacion = PacienteInscripcion.objects.get(pk=pk)
	datos =  Paciente.objects.get(codigoPaciente=pacientePlanificacion.paciente_id)
	pacienteSubsecuente=PacienteSubSecuentePF.objects.filter(pacienteInscrito_id=pk)
	return render(request,"planificacionfamiliar/planificacionsub_list.html",{'pacientesub':pacienteSubsecuente,'datos':datos,'pacienteI':pacientePlanificacion})

#View para la creacion de consultas subsecuentes de una paciente
@login_required(login_url='logins')
def planificacionfamiliar_subnuevo(request, pk):
	pacientePlanificacion = PacienteInscripcion.objects.get(pk=pk)
	datos =  Paciente.objects.get(codigoPaciente=pacientePlanificacion.paciente_id)
	formPS = PlanificacionSubForm()
	if request.method == "POST":
		formPS = PlanificacionSubForm(request.POST)
		if formPS.is_valid():
			pacienteSubsecuente = formPS.save(commit=False)
			pacienteSubsecuente.pacienteInscrito = pacientePlanificacion
			pacienteSubsecuente.edad = datos.edad_paciente()
			pacienteSubsecuente.save()
			messages.success(request,'Se ha creado una consulta subsecuente al Paciente: '+datos.codigoPaciente+' Exitosamente')
			return redirect("planificacionfamiliar-listsub",pk=pacientePlanificacion.pk)
		else:
			formPS=PlanificacionSubForm()
	return render(request,"planificacionfamiliar/consultasub_editar.html",{'form':formPS,'datos':datos,'principal':pacientePlanificacion})

#View para la ver el detalle de una consulta subsecuente de un paciente
@login_required(login_url='logins')
def planificacionfamiliar_subdetalle(request, pk, pacientesubsecuentepf_id):
	pacienteSubsecuente = PacienteSubSecuentePF.objects.get(pk=pacientesubsecuentepf_id)
	pacientePlanificacion = PacienteInscripcion.objects.get(id=pacienteSubsecuente.pacienteInscrito_id)
	datos = Paciente.objects.get(codigoPaciente=pacientePlanificacion.paciente_id)
	return render(request, "planificacionfamiliar/consultasub_detalle.html", {'paciente': pacienteSubsecuente,'datos':datos})