from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta
from django.utils import timezone
from django.forms import formset_factory
from django.forms import modelformset_factory

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
from datospersonalesapp.files import PageNumCanvas, headergg, agregaTexto

from .models import Consulta
from datospersonalesapp.models import Paciente
from signosvitalesapp.models import SignosVitales

from .forms import *

# Create your views here.

# def consulta_inicio(request):
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/thanks/')
#     else:
#         form = NameForm()
#     return render(request, 'name.html', {'form': form})





def consulta_inicio(request, pk):
    # recuperamos la data del paciente
    paciente = Paciente.objects.get(pk=pk)
    pacientepk = paciente.codigoPaciente
    
    # recuperamos el identificador del doctor
    doctor = '10594' # temporal !!!
    
    # averiguamos si el paciente tiene alguna consulta reciente, es decir
    # en un lapso de 2 horas hacia atras a partir de la fecha y hora actual,
    # esta validacion permite que se puedan vincular otros registros 
    # a la consulta adecuada, ademas regula el comportamiento
    # de la creacion y modificacion de expedientes clinicos
    
    start_date = timezone.now() - timedelta(hours=2)
    end_date = timezone.now()
    
    # consulta_activa = Consulta.objects.filter(cod_expediente=pacientepk, cod_doctor=doctor, created_at__range=(start_date, end_date))
    # print consulta_activa.query
    # print 'query count =', consulta_activa.count()
    
    consulta_activa = Consulta.objects.filter(cod_expediente=pacientepk, cod_doctor=doctor, created_at__range=(start_date, end_date)).last()
    
    if consulta_activa:
        capk = consulta_activa.id
        # print 'capk consulta actual =', capk
    else:
        capk = False
    
    # recuperamos los signos vitales del paciente
    # query para mostrar los 7 registros mas recientes del paciente
    signos_list = SignosVitales.objects.filter(paciente=pk).order_by('-codigoSignosVitales')[:7][::-1]
    
    # recuperamos el registro mas reciente de signos vitales del paciente
    signos = SignosVitales.objects.filter(paciente=pk).last()
    
    if request.method == 'POST':
        return HttpResponseRedirect('/thanks/')
        # form = NameForm(request.POST)
        # if form.is_valid():
        #     return HttpResponseRedirect('/thanks/')
    else:
        if paciente:
            # si existe el paciente llenamos el formulario con la data
            dpform = DatosPersonalesForm(initial={
                'expediente': paciente.codigoPaciente, 'nombre': paciente.get_full_name, 'fecha_nacimiento': paciente.fechaNacimiento, 
                'sexo': paciente.sexo, 'edad': paciente.edad_paciente, 'domicilio': paciente.direccion, 'telefono': paciente.telefono})
        else:
            # si no existe enviamos un formulario en blanco
            dpform = DatosPersonalesForm()
        if signos:
            # si existe registro de signos vitales recuperamos el mas reciente
            # llenamos el form con la data
            svform = SignosVitalesForm(initial={
                'presion_arterial': signos.presionArterial, 'frecuencia_cardiaca': signos.frecuenciaCardiaca, 'frecuencia_respiratoria': signos.frecuenciaRespiratoria, 
                'temperatura': signos.temperatura, 'peso': signos.peso, 'talla': signos.talla, 'imc': signos.imc_paciente})
        else:
            # si no existe enviamos un formulario en blanco
            svform = SignosVitalesForm()
    return render(request, 'generalapp/consulta-inicio.html', {
        'pacientepk': pacientepk, 'signos_list': signos_list, 'dpform': dpform, 'svform': svform, 
        'capk': capk})









def consulta_all(request, pk):
    # recuperamos la data del paciente
    paciente = Paciente.objects.get(pk=pk)
    pacientepk = paciente.codigoPaciente
    
    # recuperamos las consultas del paciente
    consultas_list = Consulta.objects.filter(cod_expediente=pk)
    
    return render(request, 'generalapp/consulta-all.html', {'pacientepk': pacientepk, 'consultas_list': consultas_list})

def consulta_create(request, pk):
    # recuperamos la data del paciente
    paciente = Paciente.objects.get(pk=pk)
    pacientepk = paciente.codigoPaciente
    
    if request.method == 'POST':
        consultaform = ConsultaMForm(request.POST)
        if consultaform.is_valid():
            consultaform.save()
            return redirect('consulta-inicio', pk=pk)
    else:
        consultaform = ConsultaMForm(initial={'cod_expediente': pk, 'cod_doctor': '10594'}) # initial es temporal !
    return render(request, 'generalapp/consulta-create.html', {'pacientepk': pacientepk, 'consultaform': consultaform})

def consulta_update(request, pk, cpk):
    # recuperamos la data del paciente
    paciente = Paciente.objects.get(pk=pk)
    pacientepk = paciente.codigoPaciente
    
    # recuperamos la consulta que esta activa
    consulta = Consulta.objects.get(pk=cpk)
    
    if request.method == 'POST':
        consultaform = ConsultaMForm(request.POST, instance=consulta)
        if consultaform.is_valid():
            consultaform.save()
            return redirect('consulta-inicio', pk=pk)
    else:
        consultaform = ConsultaMForm(instance=consulta)
    return render(request, 'generalapp/consulta-update.html', {'pacientepk': pacientepk, 'consultaform': consultaform})

def ordenlab_create(request, pk, cpk):
    # recuperamos la data del paciente
    paciente = Paciente.objects.get(pk=pk)
    pacientepk = paciente.codigoPaciente
    
    docpk = '10594'
    
    # array o set de formularios OrdenLabMForm
    OrdenLabFormSet = modelformset_factory(OrdenLab, form=OrdenLabMForm, extra=10, max_num=10)
    
    if request.method == 'POST':
        ordenlabformset = OrdenLabFormSet(request.POST, request.FILES)
        if ordenlabformset.is_valid():
        # recuperamos el objeto Con
            return redirect('consulta-inicio', pk=pk)
    else:
        ordenlabformset = OrdenLabFormSet(queryset=OrdenLab.objects.none(), initial=[
            {'cod_expediente': pk,'cod_doctor': docpk, 'cod_consulta': cpk}, 
            {'cod_expediente': pk,'cod_doctor': docpk, 'cod_consulta': cpk}, 
            {'cod_expediente': pk,'cod_doctor': docpk, 'cod_consulta': cpk}, 
            {'cod_expediente': pk,'cod_doctor': docpk, 'cod_consulta': cpk}, 
            {'cod_expediente': pk,'cod_doctor': docpk, 'cod_consulta': cpk}, 
            {'cod_expediente': pk,'cod_doctor': docpk, 'cod_consulta': cpk}, 
            {'cod_expediente': pk,'cod_doctor': docpk, 'cod_consulta': cpk}, 
            {'cod_expediente': pk,'cod_doctor': docpk, 'cod_consulta': cpk}, 
            {'cod_expediente': pk,'cod_doctor': docpk, 'cod_consulta': cpk}, 
            {'cod_expediente': pk,'cod_doctor': docpk, 'cod_consulta': cpk}, 
        ])
    return render(request, 'generalapp/ordenlab-create.html', {'pacientepk': pacientepk, 'ordenlabformset': ordenlabformset})
    
#creacion de pdf
def consultaall_file(request, pk):
	# recuperamos la data del paciente
    consultas_list = Consulta.objects.filter(cod_expediente=pk)
    #Preliminar
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='attachment; filename="historial_'+pk+'.pdf"'
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer,pagesize=letter,topMargin=120)
    
    #Predeterminados, se pueden cambiar
    sp = 14 #Espacio entre parrafo
    sty = "Normal" #Tipo de estilo
    
    Story=[]
    
    #COMIENZO PARA PERSONALIZAR EL PDF
    ptext = '<font size=12>No. de Expediente Clinico: <b><u>%s</u></b></font>' % pk
    agregaTexto(ptext, Story, "Derecha", 12)
    for consulta in consultas_list:
		ptext = '<font size=12>Fecha: %s </font>' % (consulta.fecha)
		agregaTexto(ptext, Story, sty, sp)
		ptext = '<font size=12>Consulta por: %s</font>' % (consulta.consulta_por)
		agregaTexto(ptext, Story, sty, sp)
		ptext = '<font size=12>Presenta enfermedad: %s</font>' % (consulta.presenta_enfermedad)
		agregaTexto(ptext, Story, sty, sp)
		ptext = '<font size=12>Antecedentes personales: %s</font>' % (consulta.antecedentes_personales)
		agregaTexto(ptext, Story, sty, sp)
		ptext = '<font size=12>Antecedentes familiares: %s</font>' % (consulta.antecedentes_familiares)
		agregaTexto(ptext, Story, sty, sp)
		ptext = '<font size=12>Exploracion clinica: %s</font>' % (consulta.exploracion_clinica)
		agregaTexto(ptext, Story, sty, sp)
		ptext = '<font size=12>Diagnostico principal: %s</font>' % (consulta.diagnostico_principal)
		agregaTexto(ptext, Story, sty, sp)
		ptext = '<font size=12>Otros diagnosticos: %s</font>' % (consulta.otros_diagnosticos)
		agregaTexto(ptext, Story, sty, sp)
		ptext = '<font size=12>Tratamiento: %s</font>' % (consulta.tratamiento)
		agregaTexto(ptext, Story, sty, sp)
		ptext = '<font size=12>Observaciones: %s</font>' % (consulta.observaciones)
		agregaTexto(ptext, Story, sty, sp)
    
    #Hasta aqui termina el pdf, esto es para encabezado y numeracion
    doc.build(Story,onFirstPage=headergg, onLaterPages=headergg,canvasmaker=PageNumCanvas)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
	