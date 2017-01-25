from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.db import connection
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,user_passes_test

from bienestarhome.admin import is_director, is_usuario3
from empleadosapp.models import Empleado, Especialidad, Doctor, Laboratorista#, UsuarioEmpleado
from empleadosapp.forms import EmpleadosForm, DoctorForm, LaboratoristaForm#, UsuarioForm
from citasmedicasapp.models import HorarioAtencion
import base64
import os

#Lista de empleados activos
@login_required(login_url='logins')
@user_passes_test(is_usuario3)
def empleados_list(request):
    empleados = Empleado.objects.exclude(cargo__in=('D','L')).order_by('cargo')
    doctores = Doctor.objects.select_related('codigoEmpleado','especialidad').order_by('especialidad')
    laboratoristas = Laboratorista.objects.select_related('codigoEmpleado').filter(codigoEmpleado__estadoEmpleado='A')
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(cargo) FROM empleadosapp_empleado WHERE cargo <> "D" AND cargo <> "L" AND estadoEmpleado="A" ORDER BY cargo')
    auxE = cursor.fetchall()
    cursor1 = connection.cursor()
    cursor1.execute('SELECT distinct(d.especialidad_id), e.especialidad FROM empleadosapp_especialidad as e, empleadosapp_doctor as d, empleadosapp_empleado as em WHERE e.id = d.especialidad_id AND em.codigoEmpleado = d.codigoEmpleado_id AND em.estadoEmpleado="A" ORDER BY e.id')
    auxD = cursor1.fetchall()
    return render(request,"empleados/empleados_list.html",{'empleados':empleados,'doctores':doctores,'lab':laboratoristas,'datoCargo':auxE,'datoEspecialidad':auxD})

#View para la creacion de un nuevo empleado.
@login_required(login_url='logins')	
@user_passes_test(is_usuario3)
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
			if empleado.cargo == 'L' :
				codigoE = Empleado.objects.order_by('-codigoEmpleado')[0]
				return redirect('laboratorista-new',codigoE.pk)
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
@user_passes_test(is_usuario3)
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

#View para eliminar los datos de un empleado, es decir, cambiar estado de activo a pasivo	
@login_required(login_url='logins')
@user_passes_test(is_usuario3)
def empleados_eliminar(request, pk):
	empleado = Empleado.objects.get(pk=pk) 
	if request.method == "POST":
		empleado.estadoEmpleado = 'P'
		empleado.save()
		messages.error(request,'ELIMINADO: Los datos del Trabajador: '+empleado.apellidoPrimero+' ha cambiado a Estado Pasivo')
		return redirect('empleados-view',pk=empleado.codigoEmpleado)
	return render(request,"empleados/empleados_eliminar.html",{'empleado': empleado})	

#View para restaurar a un empleado 
@login_required(login_url='logins')
@user_passes_test(is_usuario3)	
def empleados_restaurar(request, pk):
	empleado = Empleado.objects.get(pk=pk) 
	if request.method == "POST":
		empleado.estadoEmpleado = 'A'
		empleado.save()
		messages.success(request,'REESTABLECIDO: Los datos del Trabajador: '+empleado.apellidoPrimero+' ha cambiado a Estado Activo')
		return redirect('empleados-view',pk=empleado.codigoEmpleado)
	return render(request,"empleados/empleados_restaurar.html",{'empleado': empleado})

def usofirma(a):
  with open("entradatemp/firma.png","wb") as f: 
    for c in a.chunks():
      f.write(c)
  with open("entradatemp/firma.png","rb") as imageFile:
    b = base64.b64encode(imageFile.read())
  os.remove("entradatemp/firma.png")
  return b.decode()

def usosello(a):
  with open("entradatemp/sello.png","wb") as f: 
    for c in a.chunks():
      f.write(c)
  with open("entradatemp/sello.png","rb") as imageFile:
    b = base64.b64encode(imageFile.read())
  os.remove("entradatemp/sello.png")
  return b.decode()

def imprimirfirma(id):
    doctor = Doctor.objects.get(pk=id)
    auxFirma = doctor.firma.encode()
    imgFirma = base64.b64decode(auxFirma)
    with open("salidatemp/firma"+str(id)+".png","wb") as f:
        f.write(imgFirma)
    return

def imprimirsello(id):
    doctor = Doctor.objects.get(pk=id)
    auxSello = doctor.sello.encode()
    imgSello = base64.b64decode(auxSello)
    with open("salidatemp/sello"+str(id)+".png","wb") as f:
        f.write(imgSello)
    return
	
#View para la creacion de un nuevo doctor
@login_required(login_url='logins')
@user_passes_test(is_director)
def doctor_nuevo(request, pk):
	formD = DoctorForm()
	empleado = Empleado.objects.get(pk=pk)
	if request.method == "POST":
		formD = DoctorForm(request.POST, request.FILES)
		if formD.is_valid():
			doctorAux = formD.cleaned_data
			firmaAux = usofirma(request.FILES['firma'])
			selloAux = usosello(request.FILES['sello'])
			Doctor.objects.create(codigoEmpleado=empleado,especialidad=doctorAux.get('especialidad'), firma=firmaAux, sello=selloAux)
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
	return render(request, "empleados/doctor_detalle.html", {'empleado': datos, 'especialidad':especialidad, 'horarios':horarios, 'doctor':doctor})

#View para modificar los datos medicos
@login_required(login_url='logins')	
@user_passes_test(is_director)
def doctor_modificar(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    datos = Empleado.objects.get(codigoEmpleado=doctor.codigoEmpleado_id) 
    especialidad = Especialidad.objects.get(id=doctor.especialidad_id)
    horarios = HorarioAtencion.objects.get(codigoDoctor = doctor.codigoDoctor)
    if request.method == "POST":
        formD = DoctorForm(request.POST, request.FILES, initial={'especialidad': doctor.especialidad_id,'horaInicio':horarios.horaInicio,'horaFinal':horarios.horaFinal,'pacienteConsulta':horarios.pacienteConsulta,'dia':horarios.dia.all})
        if formD.is_valid():
            doctorAux = formD.cleaned_data
            firmaAux = usofirma(request.FILES['firma'])
            selloAux = usosello(request.FILES['sello'])
            auxEspecialidad = Doctor(codigoDoctor=doctor.codigoDoctor,codigoEmpleado=doctor.codigoEmpleado,especialidad=doctorAux.get('especialidad'), firma=firmaAux, sello=selloAux)
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
    return render(request,"empleados/doctor_modificar.html",{'form':formD, 'empleado': datos})

#View para eliminar los datos de un doctor, es decir, cambiar estado de activo a pasivo	
@login_required(login_url='logins')
@user_passes_test(is_director)
def doctor_eliminar(request, pk):
	doctor = Doctor.objects.get(pk=pk)
	datos = Empleado.objects.get(codigoEmpleado=doctor.codigoEmpleado_id) 
	especialidad = Especialidad.objects.get(id=doctor.especialidad_id)
	if request.method == "POST":
		datos.estadoEmpleado = 'P'
		datos.save()
		messages.error(request,'ELIMINADO: Los datos del Trabajador: '+datos.apellidoPrimero+' ha cambiado a Estado Pasivo')
		return redirect('doctor-view',pk=doctor.pk)
	return render(request, "empleados/doctor_eliminar.html", {'empleado': datos, 'especialidad':especialidad, 'doctor':doctor})

#View para restaurar a un doctor
@login_required(login_url='logins')	
@user_passes_test(is_director)
def doctor_restaurar(request, pk):
	doctor = Doctor.objects.get(pk=pk)
	datos = Empleado.objects.get(codigoEmpleado=doctor.codigoEmpleado_id) 
	especialidad = Especialidad.objects.get(id=doctor.especialidad_id)
	if request.method == "POST":
		datos.estadoEmpleado = 'A'
		datos.save()
		messages.success(request,'REESTABLECIDO: Los datos del Trabajador: '+datos.apellidoPrimero+' ha cambiado a Estado Activo')
		return redirect('doctor-view',pk=doctor.pk)
	return render(request, "empleados/doctor_restaurar.html", {'empleado': datos, 'especialidad':especialidad, 'doctor':doctor})

def imprimirfirmaL(id):
    tecnico = Laboratorista.objects.get(pk=id)
    auxFirma = tecnico.firma.encode()
    imgFirma = base64.b64decode(auxFirma)
    with open("salidatemp/firmaL"+str(id)+".png","wb") as f:
        f.write(imgFirma)
    return

def imprimirselloL(id):
    tecnico = Laboratorista.objects.get(pk=id)
    auxSello = tecnico.sello.encode()
    imgSello = base64.b64decode(auxSello)
    with open("salidatemp/selloL"+str(id)+".png","wb") as f:
        f.write(imgSello)
    return
	
#View para la creacion de un nuevo laboratorista
@login_required(login_url='logins')
@user_passes_test(is_director)
def laboratorista_nuevo(request, pk):
	formL = LaboratoristaForm()
	empleado = Empleado.objects.get(pk=pk)
	if request.method == "POST":
		formL = LaboratoristaForm(request.POST, request.FILES)
		if formL.is_valid():
			tecnicoAux = formL.cleaned_data
			firmaAux = usofirma(request.FILES['firma'])
			selloAux = usosello(request.FILES['sello'])
			Laboratorista.objects.create(codigoEmpleado=empleado,firma=firmaAux, sello=selloAux)
			messages.success(request,'Se han guardado los datos del Laboratorista: '+empleado.apellidoPrimero+' Exitosamente')
			return redirect('empleados-list')
		else:
			formL = LaboratoristaForm()
	return render(request,"empleados/laboratorista_editar.html",{'form':formL, 'empleado': empleado})
	
#View para modificar los datos del laboratorista
@login_required(login_url='logins')	
@user_passes_test(is_director)
def laboratorista_modificar(request, pk):
    formL = LaboratoristaForm()
    lab = Laboratorista.objects.get(pk=pk)
    datos = Empleado.objects.get(codigoEmpleado=lab.codigoEmpleado_id)
    if request.method == "POST":
        formL = LaboratoristaForm(request.POST, request.FILES)
        if formL.is_valid():
            tecnicoAux = formL.cleaned_data
            firmaAux = usofirma(request.FILES['firma'])
            selloAux = usosello(request.FILES['sello'])
            auxLab = Laboratorista(codigoLaboratorista=lab.codigoLaboratorista,codigoEmpleado=lab.codigoEmpleado,firma=firmaAux, sello=selloAux)
            auxLab.save()
            messages.success(request,'Se han guardado los datos del Laboratorista: '+datos.apellidoPrimero+' Exitosamente')
            return redirect('empleados-list')
        else:
            formL = LaboratoristaForm()
    return render(request,"empleados/laboratorista_modificar.html",{'form':formL, 'empleado': datos})

#Listado de empleados Pasivos/eliminados/inactivos
@login_required(login_url='logins')
@user_passes_test(is_usuario3)
def empleadoinactivo_list(request):
    empleados = Empleado.objects.exclude(cargo__in=('D','L')).order_by('cargo')
    doctores = Doctor.objects.select_related('codigoEmpleado','especialidad').order_by('especialidad')
    laboratoristas = Laboratorista.objects.select_related('codigoEmpleado').filter(codigoEmpleado__estadoEmpleado='P')
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(cargo) FROM empleadosapp_empleado WHERE cargo <> "D" AND cargo <> "L" AND estadoEmpleado="P" ORDER BY cargo')
    auxE = cursor.fetchall()
    cursor1 = connection.cursor()
    cursor1.execute('SELECT distinct(d.especialidad_id), e.especialidad FROM empleadosapp_especialidad as e, empleadosapp_doctor as d, empleadosapp_empleado as em WHERE e.id = d.especialidad_id AND em.codigoEmpleado = d.codigoEmpleado_id AND em.estadoEmpleado="P" ORDER BY e.id')
    auxD = cursor1.fetchall()
    return render(request,"empleados/empleadosInactiva_list.html",{'empleados':empleados,'doctores':doctores,'lab':laboratoristas,'datoCargo':auxE,'datoEspecialidad':auxD})

"""
def empleado_usuario(request):
	formU = UsuarioForm()
	if request.method == "POST":
		formU = UsuarioForm(request.POST)
		if formU.is_valid():
			userAux = formU.cleaned_data
			aux = userAux.get('codigoEmpleado')
			r = type(aux)
			#empleado = Empleado.objects.get(codigoEmpleado = aux)
			user = User.objects.create_user(aux.apellidoPrimero,userAux.get('email'),userAux.get('password'))
			user.last_name=aux.apellidoPrimero
			user.first_name=aux.nombrePrimero
			user.save()
			codigoU = User.objects.order_by('-id')[0]
			UsuarioEmpleado.objects.create(codigoEmpleado=aux,codigoUsuario=codigoU)
			messages.success(request,'Se han guardado los datos del Usuario Exitosamente')
			return redirect('empleados-list')
		else:
			formU = UsuarioForm()
	return render(request,"empleados/empleado_usuario.html",{'form':formU})
	"""