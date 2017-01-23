from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#To use the calendar
from datetime import date, datetime
from itertools import groupby
from datetime import timedelta
from django.utils.html import conditional_escape as esc
from django.shortcuts import render_to_response
from django.utils.safestring import mark_safe
#QUITARfrom calendar import monthrange

#Calendar update
#QUITAR from citasmedicasapp.calendar import HTMLCalendar

#To do sql query
from django.db import connection

from citasmedicasapp.models import Cita, HorarioAtencion, diasSemana, Cancelacion
from empleadosapp.models import Empleado, Doctor, Especialidad
from datospersonalesapp.models import Paciente
from citasmedicasapp.forms import CitasMedicasForm, CancelacionForm

#Listado principal se muestra listado de todos los medicos
@login_required(login_url='logins')
def doctor_list(request):
	doctores = Doctor.objects.select_related('codigoEmpleado','especialidad').order_by('especialidad')
	cursor = connection.cursor()
	cursor.execute('SELECT distinct(d.especialidad_id), e.especialidad FROM empleadosapp_especialidad as e, empleadosapp_doctor as d WHERE e.id = d.especialidad_id ORDER BY e.id')
	auxD = cursor.fetchall()
	year = timezone.now().year
	month = timezone.now().month
	return render(request,"citasmedicas/doctor_lista.html",{"doctores":doctores,'datoEspecialidad':auxD,'year':year,'month':month})

#Lista de las consultas para determinado medico
@login_required(login_url='logins')
def doctorcita_list(request,pk):
    doctor = Doctor.objects.get(pk=pk)
    datos = Empleado.objects.get(codigoEmpleado=doctor.codigoEmpleado_id) 
    otro = Especialidad.objects.get(id=doctor.especialidad_id)
    doctorcitas = Cita.objects.select_related('codigoDoctor','codigoDoctor__codigoEmpleado').filter(codigoDoctor_id=pk)
    return render(request, "citasmedicas/doctorcita_list.html",{'doctorcitas':doctorcitas,'datos':datos,'otro':otro})
    
#Lista de las consultas canceladas para un medico especifico
@login_required(login_url='logins')
def doctorcancel_list(request,pk):
	doctor = Doctor.objects.get(pk=pk)
	dp = Empleado.objects.get(codigoEmpleado=doctor.codigoEmpleado_id)
	esp = Especialidad.objects.get(id=doctor.especialidad_id)
	doctorcancel = Cancelacion.objects.select_related('codigoDoctor').filter(codigoDoctor_id=pk)
	return render(request,"citasmedicas/doctorcancel_list.html",{'doctorcancel':doctorcancel,'dp':dp,'esp':esp, 'doctor':doctor})

#View para crear nueva cancelacion
@login_required(login_url='logins')
def cancelacion_nuevo(request, pk):
	doctor = Doctor.objects.get(pk=pk)
	datos = Empleado.objects.get(codigoEmpleado=doctor.codigoEmpleado_id)
	espec = Especialidad.objects.get(id=doctor.especialidad_id)
	horarios = HorarioAtencion.objects.get(codigoDoctor = doctor.codigoDoctor)
	formC=CancelacionForm()
	if request.method == "POST":
		formC = CancelacionForm(request.POST)
		if formC.is_valid():
			cancelacion = formC.save(commit=False)
			cancelacion.codigoDoctor  = doctor
			cancelacion.save()
			#Cambio de estado en las consultas que coinciden con las fechas y horas de cancelacion
			#Si existe Fecha final
			if cancelacion.fechaFinal:
			    a = cancelacion.fechaInicio #captura la fecha inicial
			    b = cancelacion.fechaFinal+timedelta(days=1) #captura la fecha final
			    #selecciona los pacientes segun las fechas
			    pacienteFe = Cita.objects.filter(fechaConsulta__range=(a,b))
			else:
			    pacienteFe = Cita.objects.filter(fechaConsulta=cancelacion.fechaInicio)
			#conocer los max y min de las horas para usar de pivote
			if cancelacion.horaInicio.hour > horarios.horaInicio.hour:
			    iniciaH = cancelacion.horaInicio.hour
			else:
			    iniciaH = horarios.horaInicio.hour
			if cancelacion.horaFinal.hour < horarios.horaFinal.hour:
			    finH = cancelacion.horaFinal.hour
			else:
			    finH = horarios.horaFinal.hour
			periodo = range(iniciaH, finH)
			auxCod = []
			for i in pacienteFe:
			    horaX = i.horaConsulta.hour
			    if horaX in periodo:
				    auxCod.append(i.codigoCita)
			for i in auxCod:
			    auxPa = Cita.objects.get(codigoCita=i)
			    auxPa.estadoConsulta='R'
			    auxPa.save()
			messages.success(request,'Se ha creado una nueva cancelacion. Exitosamente')
			return redirect('doctorcancel_list',pk=doctor.codigoDoctor)
		else:
			formC=CancelacionForm()
	return render(request,"citasmedicas/cancelaciones_editar.html",{'form':formC,'datos':datos,'especialidad':espec, 'doctor':doctor, 'horarios':horarios})
	
#View para crear una nueva cita
@login_required(login_url='logins')
def citasmedicas_nuevo(request, pk, dia, mes, anio):
	doctor = Doctor.objects.get(pk=pk)
	datos = Empleado.objects.get(codigoEmpleado=doctor.codigoEmpleado_id)
	hraA = HorarioAtencion.objects.get(codigoDoctor=pk)
	espec = Especialidad.objects.get(id=doctor.especialidad_id)
	y = int(anio)#int(fecha[6:10])
	m = int(mes)#int(fecha[3:5])
	d = int(dia)#int(fecha[0:2])
	fecha = date(y,m,d)
	periodo = range(hraA.horaInicio.hour, hraA.horaFinal.hour)
	diccionario = {}
	for i in periodo:
		conteo = Cita.objects.filter(codigoDoctor=1,fechaConsulta=date(y,m,d),horaConsulta__hour=i).count()
		dispo = hraA.pacienteConsulta - conteo
		diccionario[i] = conteo, dispo
	formCm = CitasMedicasForm()
	if request.method == "POST":
		formCm = CitasMedicasForm(request.POST)
		if formCm.is_valid():
			cita = formCm.save(commit=False)
			hraC = cita.horaConsulta.hour
			if diccionario[hraC][1] > 0:
				cita.codigoDoctor  = doctor
				cita.fechaConsulta = date(y,m,d)
				cita.save()
				messages.success(request,'Se ha creado la cita. Exitosamente')
				return redirect('doctorcita_list',pk=doctor.codigoDoctor)
			else:
				messages.error(request,'Selecciono un horario sin cupo')
				formCm=CitasMedicasForm()
		else:
			messages.error(request,'Seleccione al paciente')
			formCm=CitasMedicasForm()
	return render(request,"citasmedicas/citamedica_editar.html",{'form':formCm,'datos':datos,'especialidad':espec,'fecha':fecha,'horas':diccionario,'hora':hraA})
	
#Lista de todos los pacientes que tienen citas
@login_required(login_url='logins')
def paciente_list(request):
	cursor = connection.cursor()
	cursor.execute('Select distinct(c.paciente_id), p.nombrePrimero, p.apellidoPrimero, p.facultadE_id from datospersonalesapp_paciente as p, citasmedicasapp_cita as c where p.codigoPaciente = c.paciente_id order by p.facultadE_id') 
	auxP = cursor.fetchall()
	cursor1 = connection.cursor()
	cursor1.execute('Select distinct(p.facultadE_id), f.nombreFacultad from datospersonalesapp_paciente as p, citasmedicasapp_cita as c, datospersonalesapp_facultad as f where p.codigoPaciente = c.paciente_id and p.facultadE_id = f.codigoFacultad order by p.facultadE_id')
	auxF = cursor1.fetchall()
	return render(request,"citasmedicas/paciente_list.html",{'datospaciente':auxP,'datoFacult':auxF})
	
#Lista de las consultas para determinado Paciente
@login_required(login_url='logins')
def pacientecita_list(request, pk):
    datos = Paciente.objects.get(pk=pk) 
    paciente = Cita.objects.select_related('codigoDoctor','codigoDoctor__codigoEmpleado','codigoDoctor__especialidad').filter(paciente_id=pk).order_by('codigoDoctor__especialidad','-fechaConsulta') 
    cursor = connection.cursor()
    cursor.execute('Select distinct(d.especialidad_id), e.especialidad from citasmedicasapp_cita as c, empleadosapp_doctor as d, empleadosapp_especialidad as e where c.codigoDoctor_id = d.codigoDoctor and d.especialidad_id = e.id and c.paciente_id = '+pk+' order by d.especialidad_id')
    auxD = cursor.fetchall()
    return render(request, "citasmedicas/pacientecita_list.html", {'paciente': paciente,'datos':datos,'datoEspecialidad':auxD})

#Funciones del calendario
#Nombre del Mes
def named_month(MonthNumber):
    return date(2000, MonthNumber, 1).strftime('%B')

@login_required(login_url='logins')    
def calendario(request, pk, anio, mes):
	#parametros de la funcion
	ayear = int(anio)
	amonth = int(mes)
	doctor = Doctor.objects.get(pk=pk)
	datos = Empleado.objects.get(codigoEmpleado=doctor.codigoEmpleado_id) #Datos del empleado
	otro = Especialidad.objects.get(id=doctor.especialidad_id) #Datos de la especialidad
	#QUITARcal = WorkoutCalendar(pk).formatmonth(ayear,amonth)
	
	#opciones extra del calendario de calendario
	yearPrevio = ayear
	monthPrevio = amonth - 1
	if monthPrevio == 0:
		monthPrevio = 12
		yearPrevio = ayear - 1
	yearSiguiente = ayear
	monthSiguiente = amonth + 1
	if monthSiguiente == 13:
		monthSiguiente = 1
		yearSiguiente = ayear + 1
	fecha = timezone.now()
	return render_to_response('citasmedicas/calendar.html',{#QUITAR 'calendar':mark_safe(cal),
		'monthPrevio':monthPrevio,'monthPrevioName':named_month(monthPrevio),'yearPrevio':yearPrevio,
		'month':fecha.month,'year':fecha.year,
		'monthSiguiente':monthSiguiente,'monthSiguienteName':named_month(monthSiguiente),'yearSiguiente':yearSiguiente,
		'datos':datos,'otro':otro,'doc':doctor})
	
#Class para mostrar un calendario