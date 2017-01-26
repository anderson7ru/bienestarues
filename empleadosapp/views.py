from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
from django.db import connection
from django.contrib.auth.decorators import login_required

from empleadosapp.models import Empleado, Especialidad, Doctor
from empleadosapp.forms import EmpleadosForm, DoctorForm
from citasmedicasapp.models import HorarioAtencion

#Lista de empleados activos
@login_required(login_url='logins')
def empleados_list(request):
    empleados = Empleado.objects.exclude(cargo='D').order_by('cargo')
    doctores = Doctor.objects.select_related('codigoEmpleado','especialidad').order_by('especialidad')
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(cargo) FROM empleadosapp_empleado WHERE cargo <> "D" ORDER BY cargo')
    auxE = cursor.fetchall()
    cursor1 = connection.cursor()
    cursor1.execute('SELECT distinct(d.especialidad_id), e.especialidad FROM empleadosapp_especialidad as e, empleadosapp_doctor as d WHERE e.id = d.especialidad_id ORDER BY e.id')
    auxD = cursor1.fetchall()
    return render(request,"empleados/empleados_list.html",{'empleados':empleados,'doctores':doctores,'datoCargo':auxE,'datoEspecialidad':auxD})

#View para la creacion de un nuevo empleado.
@login_required(login_url='logins')
def empleados_nuevo(request):
	formE = EmpleadosForm()
	if request.method == "POST":
		formE = EmpleadosForm(request.POST)
		if formE.is_valid():
			empleado = formE.save(commit=False)
			empleado.nombreRecibido=request.user
			empleado.save()
			messages.success(request,'Se han guardado los datos del Empleado: '+empleado.nombrePrimero+' '+empleado.apellidoPrimero+' Exitosamente')
			if empleado.cargo == 'D' :
				codigoE = Empleado.objects.order_by('-codigoEmpleado')[0]
				return redirect('doctor-new',codigoE.pk)
			else:
				return redirect('empleados-list')
		else:
			formE = EmpleadosForm()
	return render(request,"empleados/empleados_editar.html",{'form':formE})

#View para ver el detalle de un Empleado
@login_required(login_url='logins')
def empleados_detalle(request, pk):
	empleado = Empleado.objects.get(pk=pk)
	return render(request, "empleados/empleados_detalle.html", {'empleado': empleado})

#View para la modificacion de los datos de empleado	
@login_required(login_url='logins')
def empleados_modificar(request, pk):
	empleado = Empleado.objects.get(pk=pk)
	if request.method == "POST":
		formE = EmpleadosForm(request.POST,instance=empleado)
		if formE.is_valid():
			empleado = formE.save(commit=False)
			empleado.nombreRecibido=request.user
			empleado.save()
			messages.success(request,'Se han modificado los datos del Empleado: '+empleado.nombrePrimero+' '+empleado.apellidoPrimero+' Exitosamente')
			return redirect('empleados-view',pk=empleado.codigoEmpleado)
	else:
		formE = EmpleadosForm(instance=empleado)
	return render(request,"empleados/empleados_editar.html",{'form':formE})

#View para la creacion de un nuevo doctor
@login_required(login_url='logins')
def doctor_nuevo(request, pk):
	formD = DoctorForm()
	empleado = Empleado.objects.get(pk=pk)
	if request.method == "POST":
		formD = DoctorForm(request.POST)
		if formD.is_valid():
			doctorAux = formD.cleaned_data
			Doctor.objects.create(codigoEmpleado=empleado,especialidad=doctorAux.get('especialidad'))
			codigoD = Doctor.objects.order_by('-codigoDoctor')[0]
			aux = HorarioAtencion(codigoDoctor=codigoD,horaInicio=doctorAux.get('horaInicio'),horaFinal=doctorAux.get('horaFinal'),pacienteConsulta=doctorAux.get('pacienteConsulta'))
			aux.save()
			dias = doctorAux.get('dia')
			for d in dias:
				aux.dia.add(d)
			messages.success(request,'Se han guardado los datos del Doctor: '+empleado.apellidoPrimero+' Exitosamente')
			return redirect('empleados-list')
		else:
			formD = DoctorForm()
	return render(request,"empleados/doctor_editar.html",{'form':formD, 'empleado': empleado})
	
#View para ver el detalle de un Doctor
@login_required(login_url='logins')
def doctor_detalle(request, pk):
	doctor = Doctor.objects.get(pk=pk)
	datos = Empleado.objects.get(codigoEmpleado=doctor.codigoEmpleado_id) 
	especialidad = Especialidad.objects.get(id=doctor.especialidad_id)
	horarios = HorarioAtencion.objects.get(codigoDoctor = doctor.codigoDoctor)
	return render(request, "empleados/doctor_detalle.html", {'empleado': datos, 'especialidad':especialidad, 'horarios':horarios})

#View para modificar los datos medicos	
@login_required(login_url='logins')
def doctor_modificar(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    datos = Empleado.objects.get(codigoEmpleado=doctor.codigoEmpleado_id) 
    #especialidad = Especialidad.objects.get(id=doctor.especialidad_id)
    horarios = HorarioAtencion.objects.get(codigoDoctor = doctor.codigoDoctor)
    if request.method == "POST":
        formD = DoctorForm(request.POST,initial={'especialidad': doctor.especialidad_id,'horaInicio':horarios.horaInicio,'horaFinal':horarios.horaFinal,'pacienteConsulta':horarios.pacienteConsulta,'dia':horarios.dia.all})
        if formD.is_valid():
            doctorAux = formD.cleaned_data
            auxEspecialidad = Doctor(codigoDoctor=doctor.codigoDoctor,codigoEmpleado=doctor.codigoEmpleado,especialidad=doctorAux.get('especialidad'))
            auxEspecialidad.save()
            auxHorario = HorarioAtencion(codigoHorario=horarios.codigoHorario,codigoDoctor=doctor,horaInicio=doctorAux.get('horaInicio'),horaFinal=doctorAux.get('horaFinal'),pacienteConsulta=doctorAux.get('pacienteConsulta'))
            auxHorario.save()
            dias = doctorAux.get('dia')
            auxHorario.dia.clear()
            for d in dias:
                auxHorario.dia.add(d)
            messages.success(request,'Se han modificado los datos del Doctor: '+datos.apellidoPrimero+' Exitosamente')
            return redirect('empleados-list')
    else:
        formD = DoctorForm(initial={'especialidad': doctor.especialidad_id,'horaInicio':horarios.horaInicio,'horaFinal':horarios.horaFinal,'pacienteConsulta':horarios.pacienteConsulta,'dia':horarios.dia.all})
    return render(request,"empleados/doctor_editar.html",{'form':formD, 'empleado': datos})