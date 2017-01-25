from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

#pdfReport
#import time #en caso de poner la hora de creacion del pdf
from io import BytesIO
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.sequencer import Sequencer
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.platypus.tables import Table, TableStyle
#Es necesario para encabezado y numeracion
from bienestarhome.files import PageNumCanvas, headerpp, agregaTexto

from bienestarhome.admin import is_ginecologo, is_usuario1
from django.contrib.auth.models import User
from planificacionfamiliarapp.models import PacienteInscripcion, PacienteSubSecuentePF
from datospersonalesapp.models import Paciente
from empleadosapp.models import Empleado, Doctor
from cuentasusuariosapp.models import UsuarioEmpleado
from planificacionfamiliarapp.forms import PlanificacionFamForm, PlanificacionSubForm
from empleadosapp.views import imprimirfirma, imprimirsello
import os

#Listado de pacientes inscritas en planificacion familiar
@login_required(login_url='logins')	
@user_passes_test(is_usuario1)
def planificacionfamiliar_list(request):
    paciente=PacienteInscripcion.objects.order_by('-fechaIngreso')
    return render(request,"planificacionfamiliar/planificacion_list.html",{'planificadora':paciente})

#View para la inscripcion de pacientes a planificacion familiar
@login_required(login_url='logins')	
@user_passes_test(is_ginecologo)
def planificacionfamiliar_nuevo(request):
    formP=PlanificacionFamForm()
    if request.method == "POST":
        formP = PlanificacionFamForm(request.POST)
        if formP.is_valid():
            paciente = formP.save(commit=False)
            datos = Paciente.objects.get(codigoPaciente=paciente.paciente_id)
            paciente.edad=datos.edad_paciente()
            paciente.nombreResponsable=request.user
            paciente.save()
            messages.success(request,'El paciente con el Expediente: '+datos.codigoPaciente+' se ha inscrito exitosamente a Planificacion Familiar')
            return redirect("planificacionfamiliar-view",pk=paciente.pk)
        else:
            messages.error(request,'Seleccione al paciente')
            formP=PlanificacionFamForm()
    return render(request,"planificacionfamiliar/inscripcion_editar.html",{'form':formP})
	
#View para consultar determinado paciente, inscrito en planificacion familiar
@login_required(login_url='logins')	
@user_passes_test(is_usuario1)
def planificacionfamiliar_detalle(request, pk):
    paciente = PacienteInscripcion.objects.get(pk=pk) 
    datos =  Paciente.objects.get(codigoPaciente=paciente.paciente_id)
    cargo = UsuarioEmpleado.objects.get(codigoUsuario_id=paciente.nombreResponsable.id)
    return render(request, "planificacionfamiliar/inscripcion_detalle.html", {'paciente': paciente,'datos':datos,'cargo':cargo})
	
#En caso que soliciten que se pueda modificar el formulario de inscripcion
#View para modificar la inscripcion de las pacientes de planificacion familiar
@login_required(login_url='logins')
@user_passes_test(is_ginecologo)	
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
@user_passes_test(is_usuario1)
def planificacionfamiliar_subsecuente(request, pk):
	pacientePlanificacion = PacienteInscripcion.objects.get(pk=pk)
	datos =  Paciente.objects.get(codigoPaciente=pacientePlanificacion.paciente_id)
	pacienteSubsecuente=PacienteSubSecuentePF.objects.filter(pacienteInscrito_id=pk)
	return render(request,"planificacionfamiliar/planificacionsub_list.html",{'pacientesub':pacienteSubsecuente,'datos':datos,'pacienteI':pacientePlanificacion})

#View para la creacion de consultas subsecuentes de una paciente
@login_required(login_url='logins')	
@user_passes_test(is_ginecologo)
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
			pacienteSubsecuente.nombreResponsable=request.user
			pacienteSubsecuente.save()
			messages.success(request,'Se ha creado una consulta subsecuente al Paciente: '+datos.codigoPaciente+' Exitosamente')
			return redirect("planificacionfamiliar-listsub",pk=pacientePlanificacion.pk)
		else:
			formPS=PlanificacionSubForm()
	return render(request,"planificacionfamiliar/consultasub_editar.html",{'form':formPS,'datos':datos,'principal':pacientePlanificacion})

#View para la ver el detalle de una consulta subsecuente de un paciente
@login_required(login_url='logins')	
@user_passes_test(is_usuario1)
def planificacionfamiliar_subdetalle(request, pk, pacientesubsecuentepf_id):
	pacienteSubsecuente = PacienteSubSecuentePF.objects.get(pk=pacientesubsecuentepf_id)
	pacientePlanificacion = PacienteInscripcion.objects.get(pk=pacienteSubsecuente.pacienteInscrito_id)
	datos = Paciente.objects.get(codigoPaciente=pacientePlanificacion.paciente_id)
	cargo = UsuarioEmpleado.objects.get(codigoUsuario_id=pacientePlanificacion.nombreResponsable.id)
	return render(request, "planificacionfamiliar/consultasub_detalle.html", {'paciente': pacienteSubsecuente,'datos':datos,'cargo':cargo})

#View para imprimir la consulta subsecuente
@login_required(login_url='logins')
@user_passes_test(is_ginecologo)
def planificacionfamiliar_subfile(request, pk, pacientesubsecuentepf_id):
	pacienteS = PacienteSubSecuentePF.objects.get(pk=pacientesubsecuentepf_id)
	pacienteP = PacienteInscripcion.objects.get(pk=pacienteS.pacienteInscrito_id)
	datos = Paciente.objects.get(codigoPaciente=pacienteP.paciente_id)
	empleado = UsuarioEmpleado.objects.get(codigoUsuario_id=pacienteP.nombreResponsable.id)
	doctor = Doctor.objects.get(codigoEmpleado=empleado.codigoEmpleado)
	#Preliminar
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition']='attachment; filename="consulta_planif_'+pk+'_'+pacientesubsecuentepf_id+'.pdf"'
	buffer = BytesIO()
	doc = SimpleDocTemplate(buffer,pagesize=letter,topMargin=120)
	
	#Predeterminados, se pueden cambiar
	sp = 12 #Espacio entre parrafo
	sty = "Normal" #Tipo de estilo
	tabu = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
	vacio = "-----"
	#formatted_time = time.ctime() #para retomar fecha y hora actual del pdf
	
	Story=[]
	
	#COMIENZO PARA PERSONALIZAR EL PDF
	ptext = '<font size=12>CONSULTA SUBSECUENTE</font>'
	agregaTexto(ptext, Story, "Centro", 12)
	ptext = '<font size=12>No Expediente:<b> %s %s </b>Fecha:<b> %s/%s/%s </b></font>' % (datos.codigoPaciente,tabu,pacienteS.fechaIngreso.day,pacienteS.fechaIngreso.month,pacienteS.fechaIngreso.year)
	agregaTexto(ptext, Story, sty, sp)
	#Tabla1 para la presentacion del nombre del paciente
	P0=[]
	P1=[]
	P2=[]
	aux1 = '<font size=12><b> %s %s </b></font>' % (datos.nombrePrimero, datos.nombreSegundo)
	agregaTexto(aux1, P0, "Centro", 0)
	aux1 = '<font size=12><seqreset id="spam" base="0"><seq id="spam" />.<b> %s%s%s </b></font>' % (tabu,datos.apellidoPrimero,tabu)
	agregaTexto(aux1, P1, "Centro", 0)
	if datos.apellidoSegundo:
		aux1 = '<font size=12><b> %s </b></font>' % (datos.apellidoSegundo)
	else:
		aux1 = '<font size=12><b> %s </b></font>' % (vacio)
	agregaTexto(aux1, P2, "Centro", 0)
	P3=[]
	P4=[]
	P5=[]
	agregaTexto('<font size=11>1er Apellido</font>', P3, "Centro", 0)
	agregaTexto('<font size=11>2do Apellido</font>', P4, "Centro", 0)
	agregaTexto('<font size=11>Nombres</font>', P5, "Centro", 0)
	data = [[P1,P2,P0,''],[P3,P4,P5,'']] 
	t = Table(data,colWidths=110,style=[('LINEABOVE',(0,1),(-1,-1),1,colors.black),('SPAN',(-1,-2),(-2,-2)),('SPAN',(-1,-1),(-2,-1))])
	t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),('SIZE',(0,0),(-1,-1),12)]))
	Story.append(t)
	Story.append(Spacer(1, 10))
	#Fin de tabla
	ptext = '<font size=12>Edad:<b>%s</b> a&ntilde;os %s Peso:<b>%s</b> Libras %sPA:<b>%s</b>mmHg.</font>' % (pacienteS.edad,tabu,pacienteS.peso,tabu,pacienteS.presionArterial)
	agregaTexto(ptext, Story, sty, sp)
	if pacienteS.metUtilizado:
		aux1 = pacienteS.metUtilizado
	else:
		aux1 = vacio
	if pacienteS.metTiempo:
		aux2 = pacienteS.metTiempo
	else:
		aux2 = vacio
	if pacienteS.metLapso == 'N':
		aux2 = ' '
		aux3 = 'Ninguno'
	elif pacienteS.metLapso == 'D':
		aux3 = 'Dias'
	elif pacienteS.metLapso == 'S':
		aux3 = 'Semanas'
	elif pacienteS.metLapso == 'M':
		aux3 = 'Meses'
	else:
		aux3 = 'A&ntilde;os'
	ptext = '<font size=12>Metodo Utilizado:<b>%s</b> %s Tiempo de Uso:<b>%s </b>%s</font>' % (aux1,tabu,aux2,aux3)
	agregaTexto(ptext, Story, sty, sp)
	ptext = '<font size=12>Historia y Hallazgos</font>'
	agregaTexto(ptext, Story, sty, sp)
	if pacienteS.histHallazgos:
		aux1 = pacienteS.histHallazgos
	else:
		aux1 = vacio
	ptext = '<font size=12>%s</font>' % (aux1)
	agregaTexto(ptext, Story, sty, sp)
	if pacienteS.metContinuacion == 'S':
		aux1 = 'SI'
	else:
		aux1 = 'NO'
	if pacienteS.nombreCambio:
		aux2 = pacienteS.nombreCambio
	else:
		aux2 = vacio
	ptext = '<font size=12>CONTINUA CON EL METODO:<b>%s</b> %s CAMBIA A:<b>%s</b></font>' % (aux1,tabu,aux2)
	agregaTexto(ptext, Story, sty, sp)
	ptext = '<font size=12>Motivo del Cambio</font>'
	agregaTexto(ptext, Story, sty, sp)
	if pacienteS.motivoCambio:
		aux1 = pacienteS.motivoCambio
	else:
		aux1 = vacio
	ptext = '<font size=12>%s</font>' % (aux1)
	agregaTexto(ptext, Story, sty, sp)
	if pacienteS.diagnostico:
		aux1 = pacienteS.diagnostico
	else:
		aux1 = vacio
	ptext = '<font size=12>Diagnostico: <b>%s</b></font>' % (aux1)
	agregaTexto(ptext, Story, sty, sp)
	if pacienteS.tomaPap == 'S':
		aux1 = 'SI'
	else:
		aux1 = 'NO'
	ptext = '<font size=12>Toma PAP: <b>%s</b></font>' % (aux1)
	agregaTexto(ptext, Story, sty, sp)
	if pacienteS.tipoConsulta == 'N':
		aux1 = 'Control Normal'
	elif pacienteS.tipoConsulta == 'M':
		aux1 = 'Morbilidad'
	else:
		aux1 = 'Falla de metodo'
	ptext = '<font size=12>Tipo de consulta: <b>%s</b></font>' % (aux1)
	agregaTexto(ptext, Story, sty, sp)
	if pacienteS.indicaciones:
		aux1 = pacienteS.indicaciones
	else:
		aux1 = vacio
	ptext = '<font size=12>Indicaciones: <b>%s</b></font>' % (aux1)
	agregaTexto(ptext, Story, sty, sp)
	if pacienteS.proximaConsulta:
		aux1 = pacienteS.proximaConsulta
	else:
		aux1 = vacio
	if pacienteS.proximaConsultaLapso == 'N':
		aux1 = ' '
		aux2 = 'Ninguno'
	elif pacienteS.proximaConsultaLapso == 'D':
		aux2 = 'Dias'
	elif pacienteS.proximaConsultaLapso == 'S':
		aux2 = 'Semanas'
	elif pacienteS.proximaConsultaLapso == 'M':
		aux2 = 'Meses'
	else:
		aux2 = 'A&ntilde;os'
	ptext = '<font size=12>Proxima consulta: <b>%s %s</b></font>' % (aux1,aux2)
	agregaTexto(ptext, Story, sty, sp)
	ptext = '<font size=12>Nombre de persona responsable:<b>%s</b></font>' % (pacienteS.nombreResponsable.get_full_name())
	agregaTexto(ptext, Story, sty, sp)
	#agregar firma y sello
	imprimirfirma(doctor.pk)
	imprimirsello(doctor.pk)
	firma = "./salidatemp/firma"+str(doctor.pk)+".png"
	sello = "./salidatemp/sello"+str(doctor.pk)+".png"
	ptext = '<para autoLeading="off" fontSize=12><img src="'+firma+'" width="100" height="51" valign="-53"/> <img src="'+sello+'" width="100" height="38" valign="-40"/> </para>'
	agregaTexto(ptext, Story, "Centro", 10)
	if empleado.codigoEmpleado.cargo == 'D':
		aux2 = 'Doctor'
	elif empleado.codigoEmpleado.cargo == 'E':
		aux2 = 'Enfermera'
	elif empleado.codigoEmpleado.cargo == 'A':
		aux2 = 'Personal de Archivo'
	elif empleado.codigoEmpleado.cargo == 'P':
		aux2 = 'Personal Administrativo'
	else:
		aux2 = 'Otro'
	ptext = '<font size=12>Cargo: <b>%s</b></font>' % (aux2)
	agregaTexto(ptext, Story, sty, 20)
	ptext = '<font size=12><b>CONTROL NORMAL:</b> Es aquel en el cual la usuaria usando de manera regular el metodo de planificacion no presenta morbilidad asociada a este.</font>'
	agregaTexto(ptext, Story, sty, sp)
	ptext = '<font size=12><b>CONTROL POR MORBILIDAD (M):</b> Considerado cuando la usuaria consulte por morbilidad asociada al metodo utilizado, que comprometa su estado de salud con base a lo descrito en la Guia de Planificacion.</font>'
	agregaTexto(ptext, Story, sty, sp)
	ptext = '<font size=12><b>CONTROL POR FALLA:</b> Se entendera como falla aquella en que la mujer sale embarazada utilizando correctamente un metodo de planificacion familiar.</font>'
	agregaTexto(ptext, Story, sty, sp)
		
	#Hasta aqui termina el pdf, esto es para encabezado y numeracion
	doc.build(Story,onFirstPage=headerpp, onLaterPages=headerpp,canvasmaker=PageNumCanvas)
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	
	return response
	os.remove("salidatemp/firma"+str(doctor.pk)+".png")
	os.remove("salidatemp/sello"+str(doctor.pk)+".png")