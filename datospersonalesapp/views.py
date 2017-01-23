from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.db import connection
import json

from io import BytesIO
#pdfReport
#import time #en caso de poner la hora de creacion del pdf
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.sequencer import Sequencer
#Es necesario para encabezado y numeracion
from datospersonalesapp.files import PageNumCanvas, headerdp, agregaTexto

from datospersonalesapp.models import Paciente,Busqueda
from nuevoingresoapp.models import Expediente_Provisional
from datospersonalesapp.forms import PacienteForm,BusquedaForm
from nuevoingresoapp.forms import ExpedienteProForm


#Lista de pacientes activos
@login_required(login_url='logins')
def personalpaciente_list(request):
    pacientes=Paciente.objects.filter(estadoExpediente='A').order_by('facultadE')
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(p.facultadE_id), f.nombreFacultad FROM datospersonalesapp_paciente as p, datospersonalesapp_facultad as f WHERE p.facultadE_id = f.codigoFacultad ORDER BY f.nombreFacultad')
    auxL = cursor.fetchall()
    return render(request,"datospersonales/paciente_list.html",{'personalpaciente':pacientes,'datoFacult':auxL})

#Funcion para generar codigo ####-YY
def codigogeneradoPaciente():
	year_actual = timezone.now().year
	conteo = Paciente.objects.filter(fechaIngreso__year=year_actual).count() #Cuantos pacientes hay en este anio
	anio = str(year_actual)[2:] #ultimos 2 digitos del anio
	str_conteo = str(conteo+1) #Cual es el # del nvo paciente
	tamano = len(str_conteo)
	if tamano == 4:
		codigo = str_conteo+"-"+anio
	elif tamano == 3:
		codigo = "0"+str_conteo+"-"+anio
	elif tamano == 2:
		codigo = "00"+str_conteo+"-"+anio
	else:
		codigo = "000"+str_conteo+"-"+anio
	return codigo
	
#View para la creacion de un expediente permanente
@login_required(login_url='logins')
def personalpaciente_nuevo(request):
    formP=PacienteForm({'fechaNacimiento':''})
    if request.method == "POST":
        formP = PacienteForm(request.POST)
        if formP.is_valid():
            paciente = formP.save(commit=False)
            paciente.codigoPaciente = codigogeneradoPaciente()
            paciente.nombreRecibido=request.user
            paciente.save()
            messages.success(request,'Se ha creado el Expediente: '+paciente.codigoPaciente+' Exitosamente')
            return redirect('datospersonales-view',pk=paciente.codigoPaciente)
        else:
            formP=PacienteForm()
    return render(request,"datospersonales/paciente_editar.html",{'form':formP})
    
#Prueba para jalar datos desde el expediente provisional
@login_required(login_url='logins')
def personalpacienteprovisional_nuevo(request,nit):
	
	migrar = Expediente_Provisional.objects.get(nit=nit)
	data = migrar.facultad_id
	
	datos_migrar = {}
	datos_migrar = {
			'nombrePrimero':request.POST.get('nombrePrimero'),
			'apellidoPrimero':request.POST.get('apellidoPrimero'),
			'fechaNacimiento': request.POST.get('fechaNacimiento'),
			'nit':nit,
			'facultadE':request.POST.get('facultadE')
	}
	if migrar.nombreSegundo:
			datos_migrar['nombreSegundo'] = migrar.nombreSegundo
	else:
		datos_migrar['nombreSegundo'] = request.POST.get('nombreSegundo')
	if migrar.apellidoSegundo:
		datos_migrar['apellidoSegundo'] = migrar.apellidoSegundo
	else:
		datos_migrar['apellidoSegundo'] = request.POST.get('apellidoSegundo')
	if migrar.telefono:
		datos_migrar['telefono'] = migrar.telefono
	else:
		datos_migrar['telefono'] = request.POST.get('telefono')	
	if migrar.correo:
		datos_migrar['correo'] = migrar.correo
	else:
		datos_migrar['correo'] = request.POST.get('correo')	
			
	provisionalPaciente = Paciente(datos_migrar)
	formP=PacienteForm(datos_migrar)
	if request.method == "POST":
		formP = PacienteForm(request.POST,instance=provisionalPaciente)
		if formP.is_valid():
			paciente = formP.save(commit=False)
			paciente.codigoPaciente = codigogeneradoPaciente()
			paciente.nombreRecibido=request.user
			paciente.save()
			messages.success(request,'Se ha creado el Expediente: '+paciente.codigoPaciente+' Exitosamente')
			expediente = Expediente_Provisional.objects.get(pk=migrar.Cod_Expediente_Provisional)
			expediente.delete()
			return redirect('datospersonales-view',pk=paciente.codigoPaciente)
		else:
			#messages.success(request,'Falla el is_valid()')
			formP=PacienteForm(datos_migrar)
			
	return render(request,"datospersonales/pacienteProvisional_new.html",{'form':formP,'migrar':migrar,'data':data})

#View para consultar los datos de un paciente permanente
@login_required(login_url='logins')
def personalpaciente_detalle(request, pk):
    paciente = Paciente.objects.get(pk=pk) 
    return render(request, "datospersonales/paciente_detalle.html", {'paciente': paciente})

#View para modificar los datos de un paciente permanente
@login_required(login_url='logins')
def personalpaciente_modificar(request, pk):
	paciente = Paciente.objects.get(pk=pk) 
	if request.method == "POST":
		formP = PacienteForm(request.POST,instance=paciente)
		if formP.is_valid():
			paciente = formP.save(commit=False)
			paciente.nombreRecibido=request.user
			paciente.save()
			messages.success(request,'Se ha modificado el Expediente: '+paciente.codigoPaciente+' Exitosamente')
			return redirect('datospersonales-view',pk=paciente.codigoPaciente)
	else:
		formP=PacienteForm(instance=paciente)		
	return render(request,"datospersonales/paciente_editar.html",{'form':formP})

#View para eliminar un expediente, es decir, cambiar estado de activo a pasivo	
@login_required(login_url='logins')
def personalpaciente_eliminar(request, pk):
	paciente = Paciente.objects.get(pk=pk)
	if request.method == "POST":
		paciente.estadoExpediente = 'P'
		paciente.save()
		messages.error(request,'ELIMINADO: El Expediente: '+paciente.codigoPaciente+' ha cambiado a Estado Pasivo')
		return redirect('datospersonales-view',pk=paciente.codigoPaciente)
	return render(request,"datospersonales/paciente_eliminar.html",{'paciente': paciente})
	
#Listado de pacientes Pasivos/eliminados/inactivos
@login_required(login_url='logins')
def personalinactivo_list(request):
    pacientes=Paciente.objects.filter(estadoExpediente='P').order_by('facultadE')
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(p.facultadE_id), f.nombreFacultad FROM datospersonalesapp_paciente as p, datospersonalesapp_facultad as f WHERE p.facultadE_id = f.codigoFacultad AND p.estadoExpediente = "P" ORDER BY f.nombreFacultad')
    auxL = cursor.fetchall()
    return render(request,"datospersonales/pacienteInactiva_list.html",{'personalpaciente':pacientes,'datoFacult':auxL})
	
#View para restaurar a un paciente 
@login_required(login_url='logins')
def personalpaciente_restaurar(request, pk):
	paciente = Paciente.objects.get(pk=pk)
	if request.method == "POST":
		paciente.estadoExpediente = 'A'
		paciente.save()
		messages.success(request,'REESTABLECIDO: El Expediente: '+paciente.codigoPaciente+' ha cambiado a Estado Activo')
		return redirect('datospersonales-view',pk=paciente.codigoPaciente)
	return render(request,"datospersonales/paciente_restaurar.html",{'paciente': paciente})

#View para realizar la busqueda avanzada por coincidencias.	
@login_required(login_url='logins')
def personalpaciente_busqueda(request):
	form = BusquedaForm()
	if request.method == 'POST':
		q = request.POST.get('consulta')
		#Recuperar pacientes que contengan ya sea en primer nombre
		#primer apellido, nit o dui algo de lo escrito en el cuadro de busqueda
		pacientes = Paciente.objects.filter(
			Q(nombrePrimero__icontains=q)|
			Q(apellidoPrimero__icontains=q)|
			Q(nit__icontains=q)|
			Q(dui__icontains=q)
			)
		return render(request,"datospersonales/paciente_busqueda.html" ,{"data": pacientes, "form":form})

	else:
		return render(request,"datospersonales/paciente_busqueda.html" ,{"form":form})
		
#View para imprimir los datos personales de un expediente
@login_required(login_url='logins')
def personalpaciente_file(request, pk):
	paciente = Paciente.objects.get(pk=pk)
	#Preliminar
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition']='attachment; filename="ficha_ident_'+pk+'.pdf"'
	buffer = BytesIO()
	doc = SimpleDocTemplate(buffer,pagesize=letter,topMargin=120)
	
	#Predeterminados, se pueden cambiar
	sp = 13 #Espacio entre parrafo
	sty = "Normal" #Tipo de estilo
	tabu = "&nbsp;&nbsp;"
	#formatted_time = time.ctime() #para retomar fecha y hora actual del pdf
	
	Story=[]
	
	#COMIENZO PARA PERSONALIZAR EL PDF
	ptext = '<font size=12>No. de Expediente Clinico: <b><u>%s</u></b></font>' % paciente.codigoPaciente
	agregaTexto(ptext, Story, "Derecha", 10)
	ptext = '<font size=12><b>A) DEL PACIENTE</b></font>'
	agregaTexto(ptext, Story, sty, 10)
	#Tabla1 para la presentacion del nombre del paciente
	P0=[]
	P1=[]
	P2=[]
	aux1 = '<font size=12><b>%s %s</b></font>' % (paciente.nombrePrimero, paciente.nombreSegundo)
	agregaTexto(aux1, P0, "Centro", 0)
	aux1 = '<font size=12><seqreset id="spam" base="0"><seq id="spam" />. %s<b>%s</b>%s</font>' % (tabu,paciente.apellidoPrimero,tabu)
	agregaTexto(aux1, P1, "Centro", 0)
	if paciente.apellidoSegundo:
		aux1 = '<font size=12> <b>%s</b></font>' % (paciente.apellidoSegundo)
	else:
		aux1 = '<font size=12> <b>-----</b></font>'
	agregaTexto(aux1, P2, "Centro", 0)
	data = [[P1,P2,P0,''],['Primer Apellido','Segundo Apellido','Nombres','']] 
	t = Table(data,colWidths=110,style=[('LINEABOVE',(0,1),(-1,-1),1,colors.black),('SPAN',(-1,-2),(-2,-2)),('SPAN',(-1,-1),(-2,-1))])
	t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),('SIZE',(0,0),(-1,-1),12)]))
	Story.append(t)
	Story.append(Spacer(1, 10))
	#Fin de tabla
	#Tabla2
	P0=[]
	P1=[]
	if paciente.sexo == 'F':
		aux1 = '<font size=12><seq id="spam" />. Sexo: <u><b>Femenino</b></u></font>'
	else:
		aux1 = '<font size=12><seq id="spam" />. Sexo: <u><b>Masculino</b></u></font>'
	agregaTexto(aux1, P0,sty, 0)
	aux1 = '<font size=12>Fecha de Nacimiento: <u><b>%s/%s/%s</b></u></font>' % (paciente.fechaNacimiento.day,paciente.fechaNacimiento.month,paciente.fechaNacimiento.year)
	agregaTexto(aux1, P1,sty, 0)
	data = [[P0,P1]] 
	t = Table(data,colWidths=234) #Cuando son 2 col
	t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'LEFT'),('SIZE',(0,0),(-1,-1),12)]))
	Story.append(t)
	Story.append(Spacer(1, 12))
	#Fin tabla
	ptext = '<font size=12><seq id="spam" />. Edad: <u><b>%s</b></u> a&ntilde;os</font>' % paciente.edad_paciente()
	agregaTexto(ptext, Story, sty, sp)
	ptext = '<font size=12><seq id="spam" />. Estado Civil: <u><b>%s</b></u></font>' % paciente.estadoCivil
	agregaTexto(ptext, Story, sty, sp)
	#Tabla3
	P0=[]
	P1=[]
	P2=[]
	aux1 = '<font size=12><seq id="spam" />. NIT: <u><b>%s</b></u></font>' % (paciente.nit)
	agregaTexto(aux1, P0,sty, 0)
	if paciente.dui:
		aux1 = '<font size=12>DUI: <u><b>%s</b></u></font>' % paciente.dui
	else:
		aux1 = '<font size=12>DUI: <u><b>-----</b></u></font>'
	agregaTexto(aux1, P1,sty, 0)
	if paciente.due:
		aux1 = '<font size=12>DUE: <u><b>%s</b></u></font>' % paciente.due
	else:
		aux1 = '<font size=12>DUE: <u><b>-----</b></u></font>'
	agregaTexto(aux1, P2,sty, 0)
	data = [[P0,P1,P2]] 
	t = Table(data,colWidths=157) #Cuando son 3 col
	t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'LEFT'),('SIZE',(0,0),(-1,-1),12)]))
	Story.append(t)
	Story.append(Spacer(1, 12))
	#Fin tabla
	#Tabla4
	P0=[]
	P1=[]
	if paciente.estadoUes == 'OTR':
		ptext = '<font size=12><seq id="spam" />. Estado UES: <u><b>Otro</b></u> </font>'
		agregaTexto(ptext, Story, sty, sp)
	else:
		if paciente.estadoUes == 'EST':
			aux1 = '<font size=12><seq id="spam" />. Estado UES: <u><b>Estudiante</b></u></font>'
		elif paciente.estadoUes == 'DOC':
			aux1 = '<font size=12><seq id="spam" />. Estado UES: <u><b>Docente</b></u></font>'
		else:
			aux1 = '<font size=12><seq id="spam" />. Estado UES: <u><b>Pers.Administrativo</b></u></font>'
		agregaTexto(aux1, P0,sty, 0)
		aux1 = '<font size=12>Facultad: <u><b>%s</b></u></font>' % (paciente.facultadE)
		agregaTexto(aux1, P1,sty, 0)
		data = [[P0,P1]]
		t = Table(data,colWidths=234) #Cuando son 2 col
		t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'LEFT'),('SIZE',(0,0),(-1,-1),12)]))
		Story.append(t)
		Story.append(Spacer(1, 12))
		#Fin tabla
	ptext = '<font size=12><seq id="spam" />. Direcci&oacute;n: <u><b>%s</b></u> </font>' % paciente.direccion
	agregaTexto(ptext, Story, sty, sp)
	#Tabla5
	P0=[]
	P1=[]
	aux1 = '<font size=12><seq id="spam" />. Departamento: <u><b>%s</b></u></font>' % paciente.codDepartamento
	agregaTexto(aux1, P0,sty, 0)
	aux1 = '<font size=12>Municipio: <u><b>%s</b></u></font>' % paciente.codMunicipio
	agregaTexto(aux1, P1,sty, 0)
	data = [[P0,P1]] 
	t = Table(data,colWidths=234) #Cuando son 2 col
	t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'LEFT'),('SIZE',(0,0),(-1,-1),12)]))
	Story.append(t)
	Story.append(Spacer(1, 12))
	#Fin tabla
	#Tabla6
	P0=[]
	P1=[]
	if paciente.telefono:
		aux1 = '<font size=12><seq id="spam" />. Telefono: <u><b>%s</b></u></font>' % paciente.telefono
	else:
		aux1 = '<font size=12><seq id="spam" />. Telefono: <u><b>-----</b></u></font>'
	agregaTexto(aux1, P0,sty, 0)
	if paciente.correo:
		aux1 = '<font size=12>Correo: <u><b>%s</b></u></font>' % paciente.correo
	else:
		aux1 = '<font size=12>Correo: <u><b>-----</b></u></font>'
	agregaTexto(aux1, P1,sty, 0)
	data = [[P0,P1]] 
	t = Table(data,colWidths=234) #Cuando son 2 col
	t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'LEFT'),('SIZE',(0,0),(-1,-1),12)]))
	Story.append(t)
	Story.append(Spacer(1, 12))
	#Fin tabla
	ptext = '<font size=12><b>B) DE LA FAMILIA</b></font>' 
	agregaTexto(ptext, Story, sty, sp)
	if paciente.nombrePadre:
		ptext = '<font size=12><seqreset id="spam" base="0"><seq id="spam" />. Nombre del Padre: <u><b>%s</b></u></font>' % paciente.nombrePadre
	else:
		ptext = '<font size=12><seqreset id="spam" base="0"><seq id="spam" />. Nombre del Padre: <u><b>-----</b></u> </font>'
	agregaTexto(ptext, Story, sty, sp)
	if paciente.nombreMadre:
		ptext = '<font size=12><seq id="spam" />. Nombre de la Madre: <u><b>%s</b></u></font>' % paciente.nombreMadre
	else:
		ptext = '<font size=12><seq id="spam" />. Nombre de la Madre: <u><b>-----</b></u></font>'
	agregaTexto(ptext, Story, sty, sp)
	if paciente.nombrePareja:
		ptext = '<font size=12><seq id="spam" />. Nombre del Conyuge: <u><b>%s</b></u></font>' % paciente.nombrePareja
	else:
		ptext = '<font size=12><seq id="spam" />. Nombre del Conyuge: <u><b>-----</b></u></font>'
	agregaTexto(ptext, Story, sty, sp)
	ptext = '<font size=12><seq id="spam" />. Nombre del Responsable: <u><b>%s</b></u>%sTelefono: <u><b>%s</b></u></font>' % (paciente.emergencia, tabu, paciente.telefonoEmergencia)
	agregaTexto(ptext, Story, sty, sp)
	ptext = '<font size=12><b>C) DE LA INFORMACION</b></font>' 
	agregaTexto(ptext, Story, sty, sp)
	ptext = '<font size=12>Tomo informaci&oacute;n: <u><b>%s</b></u></font>' % (paciente.nombreRecibido)
	agregaTexto(ptext, Story, sty, sp)
	ptext = '<font size=12>Fecha de inscripci&oacute;n: <u><b>%s/%s/%s a las %s:%s</b></u></font>' % (paciente.fechaIngreso.day,paciente.fechaIngreso.month,paciente.fechaIngreso.year,paciente.fechaIngreso.hour,paciente.fechaIngreso.minute)
	agregaTexto(ptext, Story, sty, sp)
	ptext = '<font size=12>Ultima modificaci&oacute;n: <u><b>%s/%s/%s a las %s:%s</b></u></font>' % (paciente.fechaModificacion.day,paciente.fechaModificacion.month,paciente.fechaModificacion.year,paciente.fechaModificacion.hour,paciente.fechaModificacion.minute)
	agregaTexto(ptext, Story, sty, sp)
	if paciente.estadoExpediente == 'A':
		ptext = '<font size=12>Estado del Expediente: <u><b>Activo</b></u></font>'
	else:
		ptext = '<font size=12>Estado del Expediente: <u><b>Inactivo</b></u></font>'
	agregaTexto(ptext, Story, sty, sp)
	
	#Hasta aqui termina el pdf, esto es para encabezado y numeracion
	doc.build(Story,onFirstPage=headerdp, onLaterPages=headerdp,canvasmaker=PageNumCanvas)
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response