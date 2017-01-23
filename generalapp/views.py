# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from datetime import timedelta
from django.utils import timezone

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from io import BytesIO
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
from datospersonalesapp.files import PageNumCanvas, agregaTexto

from .models import Consulta
from datospersonalesapp.models import Paciente, Facultad
from signosvitalesapp.models import SignosVitales

from .forms import *

from datospersonalesapp.files import *
from psicologiaapp.files import *
from nuevoingresoapp.models import Expediente_Provisional
from enfermeriaapp.models import Cola_Consulta
#
##
################################################################################
#
## view para el dashboard de consulta general
#
def consulta_inicio(request, nkey, dkey):
    # nkey es el NIT del paciente
    # dkey es el ID que identifica al doctor
    
    # debug
    print nkey
    print dkey
    
    # buscamos al paciente en los expedientes permanentes
    if Paciente.objects.get(nit=nkey):
        # recuperamos la data del paciente
        paciente = Paciente.objects.get(nit=nkey)
        pacientepk = paciente.codigoPaciente
        
        # recuperamos los signos vitales del paciente
        # query para mostrar los 7 registros mas recientes del paciente
        signos_list = SignosVitales.objects.filter(paciente=pacientepk).order_by('-codigoSignosVitales')[:7][::-1]
        
        # recuperamos el registro mas reciente de signos vitales del paciente
        signos = SignosVitales.objects.filter(paciente=pacientepk).last()
        
        # llenamos el formulario con la data del paciente
        dpform = DatosPersonalesForm(initial={
            'expediente': paciente.codigoPaciente, 'nombre': paciente.get_full_name, 
            'fecha_nacimiento': paciente.fechaNacimiento, 'sexo': paciente.sexo, 'edad': paciente.edad_paciente, 
            'domicilio': paciente.direccion, 'telefono': paciente.telefono
        })
        
        # llenamos el formulario con los signos vitales más recientes del paciente
        svform = SignosVitalesForm(initial={
            'presion_arterial': signos.presionArterial, 'frecuencia_cardiaca': signos.frecuenciaCardiaca, 
            'frecuencia_respiratoria': signos.frecuenciaRespiratoria, 'temperatura': signos.temperatura, 
            'peso': signos.peso, 'talla': signos.talla, 'imc': signos.imc_paciente
        })
        
    # buscamos al paciente en los expedientes de nuevo ingreso (provisionales)
    else:
        if Expediente_Provisional.objects.get(nit=nkey):
            # recuperamos la data del paciente
            paciente = Expediente_Provisional.objects.get(nit=nkey)
            pacientepk = paciente.Cod_Expediente_Provisional
        else:
            # paciente no encontrado, retornamos los formularios en blanco
            dpform = DatosPersonalesForm()
            svform = SignosVitalesForm()
            
            print nkey
            print dkey
    # debug
    print paciente
    print pacientepk
    
    # seteamos data en la sesion
    request.session['pacientepk'] = pacientepk
    request.session['doctorpk'] = dkey
    request.session['pacientenit'] = nkey
    
    # debug
    print request.session['pacientepk']
    print request.session['doctorpk']
    print request.session['pacientenit']
    
    # averiguamos si el paciente tiene alguna consulta reciente, es decir
    # en un lapso de X horas hacia atras a partir de la fecha y hora actual,
    # esta validacion permite que se puedan vincular otros registros 
    # a la consulta adecuada, ademas regula el comportamiento
    # de la creacion y modificacion de expedientes clinicos
    
    start_date = timezone.now() - timedelta(hours=1)
    end_date = timezone.now()
    
    # buscamos si hay consulta activa para el paciente
    consulta_activa = Consulta.objects.filter(cod_expediente=pacientepk, cod_doctor=dkey, created_at__range=(start_date, end_date)).last()
    
    # debug
    #print consulta_activa.query
    #print 'query count = ', consulta_activa.count()
    
    if consulta_activa:
        capk = consulta_activa.id
        
        # seteamos data en la sesion
        request.session['cpk'] = capk
        
        # debug
        print request.session['cpk']
    else:
        capk = False
    
    # debug
    print 'capk consulta actual = ', capk
    
    return render(request, 'generalapp/consulta-inicio.html', {'pacientepk': pacientepk, 'signos_list': signos_list, 'dpform': dpform, 'svform': svform, 'capk': capk})
#
##
################################################################################
#
## crear consulta general
#
# @login_required(login_url='logins')
def consulta_create(request):
    pacientepk = request.session['pacientepk']
    docpk = request.session['doctorpk']
    nkey = request.session['pacientenit']
    
    # debug
    print pacientepk
    print docpk
    print nkey
    
    # recuperamos la lista de enfermedades para el autocomplete en los forms
    morbs_list = db29179_cie10.objects.all()
    
    if request.method == 'POST':
        consultaform = ConsultaMForm(request.POST)
        if consultaform.is_valid():
            consultaform.save()
            # creamos el mensaje que informa al usuario del resultado
            messages.success(request, 'Se ha guardado la consulta del paciente !')
            # redirect hacia el dashboard de consulta general
            return redirect('consulta-inicio', nkey=nkey, dkey=docpk)
    else:
        consultaform = ConsultaMForm(initial={'cod_expediente': pacientepk, 'cod_doctor': docpk, 'nit_paciente': nkey})
    return render(request, 'generalapp/consulta-create.html', {'pacientepk': pacientepk, 'consultaform': consultaform, 'morbs_list': morbs_list})
#
## editar consulta general
#
# @login_required(login_url='logins')
def consulta_update(request):
    pacientepk = request.session['pacientepk']
    docpk = request.session['doctorpk']
    nkey = request.session['pacientenit']
    cpk = request.session['cpk']
    
    # debug
    print pacientepk
    print docpk
    print nkey
    print cpk
    
    # recuperamos la lista de enfermedades para el autocomplete en los forms
    morbs_list = db29179_cie10.objects.all()
    
    # recuperamos la consulta
    consulta = Consulta.objects.get(pk=cpk)
    
    if request.method == 'POST':
        consultaform = ConsultaMForm(request.POST, instance=consulta)
        if consultaform.is_valid():
            consultaform.save()
            # creamos el mensaje que informa al usuario del resultado
            messages.success(request, 'Se ha guardado la consulta del paciente !')
            return redirect('consulta-inicio', nkey=nkey, dkey=docpk)
    else:
        consultaform = ConsultaMForm(instance=consulta)
    return render(request, 'generalapp/consulta-update.html', {'pacientepk': pacientepk, 'consultaform': consultaform, 'cpk': cpk, 'morbs_list': morbs_list})
#
## view para recuperar el historial de consultas del paciente
#
# @login_required(login_url='logins')
def consulta_all(request):
    pacientepk = request.session['pacientepk']
    
    # debug
    print pacientepk
    
    # recuperamos las consultas del paciente
    consultas_list = Consulta.objects.filter(cod_expediente=pacientepk).order_by('-fecha')
    
    return render(request, 'generalapp/consulta-all.html', {'pacientepk': pacientepk, 'consultas_list': consultas_list})
#
## pdf consulta general
#
# @login_required(login_url='logins')
def consultaAllPDF(request):
    pacientepk = request.session['pacientepk']
    
    # debug
    print pacientepk
    
    if Consulta.objects.filter(cod_expediente=pacientepk):
        # recuperamos la data de las consultas
        consultas_list = Consulta.objects.filter(cod_expediente=pacientepk)
        
        paciente = Paciente.objects.get(pk=pacientepk)
        nombre = paciente.get_full_name()
        print nombre
        
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        
        doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=120)
        
        sp = 20
        sty = "Justify"
        tab = "&nbsp;"*6
        
        Story = []
        
        texto = '<font size=11><b><i>Paciente: </i></b><u>%s</u></font>%s%s<font size=11><b><i>Expediente: </i></b><u>%s</u></font>' % (nombre, tab, tab, pacientepk)
        agregaTexto(texto, Story, sty, sp)
        for consulta in consultas_list:
            texto = '<font size=11><b><i>Fecha: </i></b><u>%s</u></font>' % (consulta.fecha)
            agregaTexto(texto, Story, sty, sp)
            texto = '<font size=11><b><i>Consulta por: </i></b><u>%s</u></font>' % (consulta.consulta_por)
            agregaTexto(texto, Story, sty, sp)
            texto = '<font size=11><b><i>Presenta enfermedad: </i></b><u>%s</u></font>' % (consulta.presenta_enfermedad)
            agregaTexto(texto, Story, sty, sp)
            texto = '<font size=11><b><i>Antecedentes personales: </i></b><u>%s</u></font>' % (consulta.antecedentes_personales)
            agregaTexto(texto, Story, sty, sp)
            texto = '<font size=11><b><i>Antecedentes familiares: </i></b><u>%s</u></font>' % (consulta.antecedentes_familiares)
            agregaTexto(texto, Story, sty, sp)
            texto = '<font size=11><b><i>Exploracion clinica: </i></b><u>%s</u></font>' % (consulta.exploracion_clinica)
            agregaTexto(texto, Story, sty, sp)
            texto = '<font size=11><b><i>Diagnostico principal: </i></b><u>%s</u></font>' % (consulta.diagnostico_principal)
            agregaTexto(texto, Story, sty, sp)
            texto = '<font size=11><b><i>Otros diagnosticos: </i></b><u>%s</u></font>' % (consulta.otros_diagnosticos)
            agregaTexto(texto, Story, sty, sp)
            texto = '<font size=11><b><i>Tratamiento: </i></b><u>%s</u></font>' % (consulta.tratamiento)
            agregaTexto(texto, Story, sty, sp)
            texto = '<font size=11><b><i>Observaciones: </i></b><u>%s</u></font>' % (consulta.observaciones)
            agregaTexto(texto, Story, sty, sp)
            saltoPagina(Story)
        
        doc.build(Story, onFirstPage=headerConsultaGeneral, onLaterPages=headerConsultaGeneral, canvasmaker=PageNumCanvas)
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        
        return response
    else:
        messages.error(request, 'Error al generar el PDF de las consultas del paciente !')
    return redirect('consulta-todas')
#
## cerrar consulta general
#
# @login_required(login_url='logins')
def consulta_cerrar(request):
    # limpiamos las variables de sesion utilizadas en la consulta general
    del request.session['pacientepk']
    del request.session['doctorpk']
    
    nkey = request.session['pacientenit']
    
    del request.session['cpk']
    
    # borramos de la cola al paciente que acaba de ser atendido
    if Cola_Consulta.objects.filter(nit=nkey):
        Cola_Consulta.objects.filter(nit=nkey).delete()
        
        # creamos el mensaje que informa al usuario del resultado
        messages.success(request, 'Consulta finalizada exitosamente !')
    else:
        messages.error(request, 'Error al intentar finalizar la consulta del paciente !')
    
    del request.session['pacientenit']
    
    # redirigimos nuevamente a la cola de pacientes
    return redirect('cola_consulta-list')
#
##
################################################################################
#
## receta
#
# @login_required(login_url='logins')
def receta(request):
    # recuperamos las recetas vinculadas a la consulta
    consultapk = request.session['cpk']
    recetas_list = Receta.objects.filter(cod_consulta=consultapk).order_by('-fecha')
    
    # fechas inicial y final para controlar la funcionalidad de eliminar
    start_date = timezone.now() - timedelta(hours=8)
    end_date = timezone.now()
    
    if request.method == 'POST':
        form = RecetaMForm(request.POST)
        if form.is_valid():
            form.save()
            
            # creamos el mensaje que informa al usuario del resultado
            messages.success(request, 'Se ha guardado la receta del paciente !')
            return redirect('receta')
    else:
        # recuperamos la data seteada en la sesion
        if 'pacientepk' in request.session and 'doctorpk' in request.session and 'cpk' in request.session:
            
            pacientepk = request.session['pacientepk']
            doctorpk = request.session['doctorpk']
            consultapk = request.session['cpk']
            
            # llenamos el formulario con la data del paciente
            form = RecetaMForm(initial={'cod_expediente': pacientepk, 'cod_doctor': doctorpk, 'cod_consulta': consultapk})
        else:
            form = RecetaMForm()
    return render(request, 'generalapp/receta.html', {'form': form, 'recetas_list': recetas_list, 'pacientepk': pacientepk, 'start_date': start_date, 'end_date': end_date})
#
## eliminar receta
#
# @login_required(login_url='logins')
def eliminar_receta(request, rpk):
    print rpk
    
    if Receta.objects.filter(pk=rpk):
        Receta.objects.filter(pk=rpk).delete()
        
        # creamos el mensaje que informa al usuario del resultado
        messages.success(request, 'Se ha eliminado la receta del paciente !')
    else:
        messages.error(request, 'Error al intentar eliminar la receta del paciente !')
    return redirect('receta')
#
## pdf receta
#
# @login_required(login_url='logins')
def recetaPDF(request, rpk):
    print rpk
    
    if Receta.objects.filter(pk=rpk):
        receta = Receta.objects.get(pk=rpk)
        
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        
        doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=120)
        
        sp = 20
        sty = "Justify"
        tab = "&nbsp;"*6
        
        Story = []
        
        texto = '<font size=11><b><i>Medicamento: </i></b><u>%s</u></font>' % (receta.medicamento)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>Observaciones: </i></b><u>%s</u></font>' % (receta.observaciones)
        agregaTexto(texto, Story, sty, sp)
        
        doc.build(Story, onFirstPage=headerReceta, canvasmaker=PageNumCanvas)
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        
        return response
    else:
        messages.error(request, 'Error al generar el PDF de la receta del paciente !')
    return redirect('receta')
#
##
################################################################################
#
## orden de laboratorio
#
# @login_required(login_url='logins')
def orden_laboratorio(request):
    # recuperamos las órdenes de laboratorio vinculadas a la consulta
    consultapk = request.session['cpk']
    ordenes_list = OrdenLab.objects.filter(cod_consulta=consultapk).order_by('-fecha')
    
    # fechas inicial y final para controlar la funcionalidad de eliminar
    start_date = timezone.now() - timedelta(hours=8)
    end_date = timezone.now()
    
    if request.method == 'POST':
        form = OrdenLabMForm(request.POST)
        if form.is_valid():
            form.save()
            
            # creamos el mensaje que informa al usuario del resultado
            messages.success(request, 'Se ha guardado la orden de laboratorio del paciente !')
            return redirect('orden-laboratorio')
    else:
        # recuperamos la data seteada en la sesion
        if 'pacientepk' in request.session and 'doctorpk' in request.session and 'cpk' in request.session:
            
            pacientepk = request.session['pacientepk']
            doctorpk = request.session['doctorpk']
            consultapk = request.session['cpk']
            
            # llenamos el formulario con la data del paciente
            form = OrdenLabMForm(initial={'cod_expediente': pacientepk, 'cod_doctor': doctorpk, 'cod_consulta': consultapk})
        else:
            form = OrdenLabMForm()
    return render(request, 'generalapp/orden_laboratorio.html', {'form': form, 'ordenes_list': ordenes_list, 'pacientepk': pacientepk, 'start_date': start_date, 'end_date': end_date})
#
## eliminar orden de laboratorio
#
# @login_required(login_url='logins')
def eliminar_ordenlab(request, rpk):
    print rpk
    
    if OrdenLab.objects.filter(pk=rpk):
        OrdenLab.objects.filter(pk=rpk).delete()
        
        # creamos el mensaje que informa al usuario del resultado
        messages.success(request, 'Se ha eliminado la orden de laboratorio del paciente !')
    else:
        messages.error(request, 'Error al intentar eliminar la orden de laboratorio del paciente !')
    return redirect('orden-laboratorio')
#
## pdf orden de laboratorio
#
# @login_required(login_url='logins')
def ordenLabPDF(request, rpk):
    print rpk
    
    if OrdenLab.objects.filter(pk=rpk):
        orden = OrdenLab.objects.get(pk=rpk)
        
        pacientepk = orden.cod_expediente_id
        print pacientepk
        
        paciente = Paciente.objects.get(codigoPaciente=pacientepk)
        print paciente.codigoPaciente
        
        nombre = paciente.get_full_name()
        print nombre
        
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        
        doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=120)
        
        sp = 20
        sty = "Justify"
        tab = "&nbsp;"*6
        
        Story = []
        
        texto = '<font size=11><b><i>Nombre del paciente: </i></b><u>%s</u></font>' % (nombre)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>Area: </i></b><u>%s</u></font>%s%s<font size=11><b><i>Tipo de Examen: </i></b><u>%s</u></font>' % (orden.codArea, tab, tab, orden.codExamen)
        agregaTexto(texto, Story, sty, sp)
        
        doc.build(Story, onFirstPage=headerOrdenLab, canvasmaker=PageNumCanvas)
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        
        return response
    else:
        messages.error(request, 'Error al generar el PDF de la orden de laboratorio del paciente !')
    return redirect('orden-laboratorio')
#
##
################################################################################
#
## referencia interna
#
# @login_required(login_url='logins')
def referencia_interna(request):
    # recuperamos las referencias internas vinculadas a la consulta
    consultapk = request.session['cpk']
    internas_list = ReferenciaInterna.objects.filter(cod_consulta=consultapk).order_by('-fecha')
    
    # fechas inicial y final para controlar la funcionalidad de eliminar
    start_date = timezone.now() - timedelta(hours=8)
    end_date = timezone.now()
    
    if request.method == 'POST':
        form = ReferenciaInternaMForm(request.POST)
        if form.is_valid():
            form.save()
            
            # creamos el mensaje que informa al usuario del resultado
            messages.success(request, 'Se ha guardado la referencia interna del paciente !')
            return redirect('referencia-interna')
    else:
        # recuperamos la data seteada en la sesion
        if 'pacientepk' in request.session and 'doctorpk' in request.session and 'cpk' in request.session:
            
            pacientepk = request.session['pacientepk']
            doctorpk = request.session['doctorpk']
            consultapk = request.session['cpk']
            
            # recuperamos la data del paciente
            paciente = Paciente.objects.get(pk=pacientepk)
            
            # recuperamos el nombre de la facultad
            procedencia = Facultad.objects.get(pk=paciente.facultadE_id)
            
            #print procedencia
            
            # llenamos el formulario con la data del paciente
            form = ReferenciaInternaMForm(initial={
                'cod_expediente': pacientepk, 'cod_doctor': doctorpk, 'cod_consulta': consultapk,
                'nombre_paciente': paciente.get_full_name, 'tipo_paciente': paciente.estadoUes, 'procedencia_paciente': procedencia})
        else:
            form = ReferenciaInternaMForm()
    return render(request, 'generalapp/referencia_interna.html', {'form': form, 'internas_list': internas_list, 'pacientepk': pacientepk, 'start_date': start_date, 'end_date': end_date})
#
## eliminar referencia interna
#
# @login_required(login_url='logins')
def eliminar_interna(request, rpk):
    print rpk
    
    if ReferenciaInterna.objects.filter(pk=rpk):
        ReferenciaInterna.objects.filter(pk=rpk).delete()
        
        # creamos el mensaje que informa al usuario del resultado
        messages.success(request, 'Se ha eliminado la referencia interna del paciente !')
    else:
        messages.error(request, 'Error al intentar eliminar la referencia interna del paciente !')
    return redirect('referencia-interna')
#
## pdf referencia interna
#
# @login_required(login_url='logins')
def referenciaInternaPDF(request, rpk):
    print rpk
    
    if ReferenciaInterna.objects.filter(pk=rpk):
        referencia = ReferenciaInterna.objects.get(pk=rpk)
        
        pacientepk = referencia.cod_expediente_id
        print pacientepk
        paciente = Paciente.objects.get(codigoPaciente=pacientepk)
        print paciente.codigoPaciente
        
        nombre = paciente.get_full_name()
        print nombre
        
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        
        doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=120)
        
        sp = 20
        sty = "Justify"
        tab = "&nbsp;"*6
        
        Story = []
        
        texto = '<font size=11><b><i>Referido a: </i></b><u>%s</u></font>' % (referencia.referido_a)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>Por medio de la presente remitole a: </i></b><u>%s</u></font>' % (nombre)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>Paciente de este centro de salud universitario: </i></b><u>%s</u></font>' % (referencia.tipo_paciente)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>Facultad/Dependencia: </i></b><u>%s</u></font>' % (referencia.procedencia_paciente)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>Expediente: </i></b><u>%s</u></font>' % (pacientepk)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>Motivo: </i></b><u>%s</u></font>' % (referencia.motivo_referencia)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>Observaciones: </i></b><u>%s</u></font>' % (referencia.observaciones)
        agregaTexto(texto, Story, sty, sp)
        
        doc.build(Story, onFirstPage=headerReInterna, canvasmaker=PageNumCanvas)
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        
        return response
    else:
        messages.error(request, 'Error al generar el PDF de la referencia interna del paciente !')
    return redirect('referencia-interna')
#
##
################################################################################
#
## referencia externa
#
# @login_required(login_url='logins')
def referencia_externa(request):
    # recuperamos las referencias externas vinculadas a la consulta
    consultapk = request.session['cpk']
    externas_list = ReferenciaExterna.objects.filter(cod_consulta=consultapk).order_by('-fecha')
    
    # fechas inicial y final para controlar la funcionalidad de eliminar
    start_date = timezone.now() - timedelta(hours=8)
    end_date = timezone.now()
    
    if request.method == 'POST':
        form = ReferenciaExternaMForm(request.POST)
        if form.is_valid():
            form.save()
            
            # creamos el mensaje que informa al usuario del resultado
            messages.success(request, 'Se ha guardado la referencia externa del paciente !')
            return redirect('referencia-externa')
    else:
        # recuperamos la data seteada en la sesion
        if 'pacientepk' in request.session and 'doctorpk' in request.session and 'cpk' in request.session:
            
            pacientepk = request.session['pacientepk']
            doctorpk = request.session['doctorpk']
            consultapk = request.session['cpk']
            
            # recuperamos la data del paciente
            paciente = Paciente.objects.get(pk=pacientepk)
            
            # recuperamos el registro mas reciente de signos vitales del paciente
            signos = SignosVitales.objects.filter(paciente=pacientepk).last()
            
            print signos
            
            # recuperamos el registro mas reciente de consulta general del paciente
            consulta = Consulta.objects.filter(cod_expediente=pacientepk).last()
            
            print consulta
            
            # llenamos el formulario con la data del paciente
            form = ReferenciaExternaMForm(initial={
                'cod_expediente': pacientepk, 'cod_doctor': doctorpk, 'cod_consulta': consultapk, 'nombre_paciente': paciente.get_full_name, 'edad_paciente': paciente.edad_paciente,
                'sexo_paciente': paciente.sexo, 'domicilio_paciente': paciente.direccion, 'telefono_paciente': paciente.telefono, 'presion_arterial': signos.presionArterial, 'frecuencia_cardiaca': signos.frecuenciaCardiaca,
                'frecuencia_respiratoria': signos.frecuenciaRespiratoria, 'temperatura': signos.temperatura, 'peso': signos.peso, 'talla': signos.talla, 'consulta_por': consulta.consulta_por,
                'presenta_enfermedad': consulta.presenta_enfermedad, 'antecedentes_personales': consulta.antecedentes_personales, 'examen_fisico': consulta.exploracion_clinica, 'impresion_diagnostica': consulta.diagnostico_principal})
        else:
            form = ReferenciaExternaMForm()
    return render(request, 'generalapp/referencia_externa.html', {'form': form, 'externas_list': externas_list, 'pacientepk': pacientepk, 'start_date': start_date, 'end_date': end_date})
#
## eliminar referencia externa
#
# @login_required(login_url='logins')
def eliminar_externa(request, rpk):
    print rpk
    
    if ReferenciaExterna.objects.filter(pk=rpk):
        ReferenciaExterna.objects.filter(pk=rpk).delete()
        
        # creamos el mensaje que informa al usuario del resultado
        messages.success(request, 'Se ha eliminado la referencia externa del paciente !')
    else:
        messages.error(request, 'Error al intentar eliminar la referencia externa del paciente !')
    return redirect('referencia-externa')
#
## pdf referencia externa
#
# @login_required(login_url='logins')
def referenciaExternaPDF(request, rpk):
    print rpk
    
    if ReferenciaExterna.objects.filter(pk=rpk):
        # recuperamos la data de la referencia
        referencia = ReferenciaExterna.objects.get(pk=rpk)
        
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        
        doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=120)
        
        sp = 20
        sty = "Justify"
        tab = "&nbsp;"*6
        
        Story = []
        
        texto = '<font size=11><b><i>Referido a: </i></b><u>%s</u></font>' % (referencia.referido_a)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>Nombre: </i></b><u>%s</u></font>' % (referencia.nombre_paciente)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>Edad: </i></b><u>%s</u></font>%s%s<font size=11><b><i>Sexo: </i></b><u>%s</u></font>%s%s<font size=11><b><i>Telefono: </i></b><u>%s</u></font>' % (referencia.edad_paciente, tab, tab, referencia.sexo_paciente, tab, tab, referencia.telefono_paciente)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>Domicilio: </i></b><u>%s</u></font>' % (referencia.domicilio_paciente)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>PA (mmHg): </i></b><u>%s</u></font>%s%s<font size=11><b><i>FC (lat/min): </i></b><u>%s</u></font>%s%s<font size=11><b><i>FR (resp/min): </i></b><u>%s</u></font>' % (referencia.presion_arterial, tab, tab, referencia.frecuencia_cardiaca, tab, tab, referencia.frecuencia_respiratoria)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>Temperatura (°C): </i></b><u>%s</u></font>%s%s<font size=11><b><i>Peso (lb): </i></b><u>%s</u></font>%s%s<font size=11><b><i>Talla (m): </i></b><u>%s</u></font>' % (referencia.temperatura, tab, tab, referencia.peso, tab, tab, referencia.talla)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>Consulta por: </i></b><u>%s</u></font>' % (referencia.consulta_por)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>Presenta enfermedad: </i></b><u>%s</u></font>' % (referencia.presenta_enfermedad)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>Antecedentes personales: </i></b><u>%s</u></font>' % (referencia.antecedentes_personales)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>Examen fisico: </i></b><u>%s</u></font>' % (referencia.examen_fisico)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>Examenes laboratorio: </i></b><u>%s</u></font>' % (referencia.examenes_laboratorio)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>Impresion diagnostica: </i></b><u>%s</u></font>' % (referencia.impresion_diagnostica)
        agregaTexto(texto, Story, sty, sp)
        
        texto = '<font size=11><b><i>Observaciones: </i></b><u>%s</u></font>' % (referencia.observaciones)
        agregaTexto(texto, Story, sty, sp)
        
        doc.build(Story, onFirstPage=headerReExterna, canvasmaker=PageNumCanvas)
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        
        return response
    else:
        messages.error(request, 'Error al generar el PDF de la referencia externa del paciente !')
    return redirect('referencia-externa')
#
##
################################################################################