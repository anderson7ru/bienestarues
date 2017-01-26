from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from io import BytesIO
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_CENTER,TA_JUSTIFY
from reportlab.lib.pagesizes import A4,LEGAL,landscape
from django.views.generic import View
from django.utils import timezone
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.sequencer import Sequencer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from django.contrib.auth.decorators import login_required,user_passes_test
from datospersonalesapp.files import PageNumCanvas, agregaTexto

from psicologiaapp.forms import PsicologiaForm,ProcesoTerapeuticoForm,RegistroAvanceForm
from psicologiaapp.models import Psicologia,ProcesoTerapeutico,RegistroAvance
from psicologiaapp.files import headerPsico,writeLine,saltoPagina,headerPsico2,headerProcesos,headerRegistro
from psicologiaapp.admin import is_psicologo

from empleadosapp.models import Empleado, Doctor
from datospersonalesapp.models import Paciente

#Listado de Los pacientes de Psicologia
def psicologia_lista(request):
    paciente = Psicologia.objects.select_related('paciente')
    #registro = ProcesoTerapeutico.objects.select_related('codPsicologia','codPsicologia__paciente')
    return render(request,"psicologia/psicologia_listado.html",{"pacientes":paciente})

#vista para crear el expediente de psicologia
@login_required(login_url='logins')
@user_passes_test(is_psicologo)#llama la funcion is_psicologo para comprobar que el usuario es un psicologo :v
def psicologia_nuevo(request,pk):
    paciente = Paciente.objects.get(pk=pk)
    form = PsicologiaForm()
    if request.method == 'POST':
        form = PsicologiaForm(request.POST)
        if form.is_valid():
            psico = form.save(commit=False)
            psico.paciente_id = paciente.codigoPaciente
            psico.nombreRecibido = request.user
            psico.save()
            messages.success(request,'Se ha creado el Expediente de Psicologia para el paciente: '+paciente.codigoPaciente+' Exitosamente')
            return redirect('procesoterapeutico-new',paciente=paciente.codigoPaciente) 
        else:
            form=PsicologiaForm()
    return render(request,"psicologia/psicologia_nuevo.html",{"form":form,"datos":paciente})

#Vista para modificar los datos del expediente de psicologia
@login_required(login_url='logins')
def psicologia_actualizar(request,paciente):
    paciente = Paciente.objects.get(pk=paciente)
    psicologia = Psicologia.objects.get(paciente_id=paciente)
    if request.method == 'POST':
        form = PsicologiaForm(request.POST,instance=psicologia)
        if form.is_valid():
            psico = form.save(commit=False)
            psico.paciente_id = paciente.codigoPaciente
            psico.nombreRecibido = request.user
            psico.save()
            messages.success(request,'Se ha Actualizado el Expediente de Psicologia para el paciente: '+paciente.codigoPaciente+' Exitosamente')
            return redirect('psicologia-view',paciente=paciente.codigoPaciente)
    else:
        form=PsicologiaForm(instance=psicologia)
    return render(request,"psicologia/psicologia_nuevo.html",{"form":form,"datos":paciente})

#vista para consultar los datos del expediente de psicologia
@login_required(login_url='logins')
def psicologia_consulta(request,paciente):
    infoPaciente = Paciente.objects.get(codigoPaciente=paciente)
    infoPsicologia = Psicologia.objects.get(paciente_id=paciente)
    doctor = Doctor.objects.get(codigoDoctor=infoPsicologia.referido_id)
    infoDoctor = Empleado.objects.get(codigoEmpleado=doctor.codigoDoctor)
    usuario = request.user
    return render(request,"psicologia/psicologia_detalle.html",{"paciente":infoPaciente,"psico":infoPsicologia,'sexoD':infoDoctor.sexo,'usuario':usuario})
    
#Vista para crear el seguimiento del proceso terapeutico a seguir
#es llamado inmediatamente despues de crear el expediente de psicologia
@login_required(login_url='logins')
def procesoterapeutico_nuevo(request,paciente):
    paciente = Paciente.objects.get(pk=paciente)
    codigo = paciente.codigoPaciente
    psico = Psicologia.objects.get(paciente_id=codigo)
    form = ProcesoTerapeuticoForm()
    if request.method == 'POST':
        form = ProcesoTerapeuticoForm(request.POST)
        if form.is_valid():
            proc = form.save(commit=False)
            proc.nombreRecibido = request.user
            proc.codPsicologia_id = psico.codPsicologia
            proc.save()
            messages.success(request, 'Proceso Terapeutico Creado exitosamente')
            return redirect('registroavance-new',proceso=proc.codProcesoTerapeutico)
        else:
            form=PsicologiaForm()
    return render(request,"psicologia/procesoterapeutico_nuevo.html",{"form":form,"paciente":codigo})

#Vista Para modificar los datos del proceso terapeutico
@login_required(login_url='logins')
def procesoterapeutico_actualizar(request,paciente):
    paciente = Paciente.objects.get(pk=paciente)
    codigo = paciente.codigoPaciente
    psico = Psicologia.objects.get(paciente_id=codigo)
    proceso = ProcesoTerapeutico.objects.get(codPsicologia_id=psico.codPsicologia)
    if request.method=='POST':
        form = ProcesoTerapeuticoForm(request.POST,instance=proceso)
        if form.is_valid():
            x = form.save(commit=False)
            x.nombreRecibido = request.user 
            x.codPsicologia_id = psico.codPsicologia
            x.save()
            messages.success(request, 'Proceso Terapeutico Actualizado exitosamente')
            return redirect('procesoterapeutico-view',proceso=proceso.codProcesoTerapeutico)
    else:
        form = ProcesoTerapeuticoForm(instance=proceso)
    return render(request,"psicologia/procesoterapeutico_nuevo.html",{"form":form,"paciente":codigo})
    
#Vista para consultar procesos terapeuticos
@login_required(login_url='logins')
def procesoterapeutico_consulta(request,paciente):
    paciente = Paciente.objects.get(pk=paciente)
    psico = Psicologia.objects.get(paciente_id=paciente.codigoPaciente)
    psicologo = Doctor.objects.get(codigoDoctor=psico.referido_id)
    usuario = request.user
    #proc = ProcesoTerapeutico.objects.get(codPsicologia_id=psico.codPsicologia)
    proc = ProcesoTerapeutico.objects.filter(codPsicologia_id=psico.codPsicologia)
    return render(request,"psicologia/procesoterapeutico_consultar.html",{"paciente":paciente,"psico":psicologo,"proc":proc,'usuario':usuario})

#Vista para crear el Registro de Avances del proceso terapeutico
#Lleva los comentarios tanto del paciente como del psicologo
@login_required(login_url='logins')
def registroavance_nuevo(request,proceso):
    proc = ProcesoTerapeutico.objects.get(pk=proceso)
    psico = Psicologia.objects.get(pk=proc.codPsicologia_id)
    paciente = Paciente.objects.get(pk=psico.paciente_id)
    form = RegistroAvanceForm()
    if request.method == 'POST':
        form = RegistroAvanceForm(request.POST)
        if form.is_valid():
            reg = form.save(commit=False)
            reg.codProcesoTerapeutico_id = proceso
            reg.nombreRecibido = request.user
            reg.save()
            messages.success(request, 'Registro de avance del Proceso Terapeutico: '+str(proc.codProcesoTerapeutico)+'  Creado exitosamente')
            return redirect('psicologia-view',paciente=paciente.codigoPaciente)
        else:
            form = RegistroAvanceForm()
    return render(request,"psicologia/registroavance_nuevo.html",{"form":form,"paciente":paciente,"proceso":proc})
    
#Vista para actualizar el registro de avances
@login_required(login_url='logins')
def registroavance_actualizar(request,proceso):
    proc = ProcesoTerapeutico.objects.get(pk=proceso)
    psico = Psicologia.objects.get(pk=proc.codPsicologia_id)
    paciente = Paciente.objects.get(pk=psico.paciente_id)
    registro = RegistroAvance.objects.get(codProcesoTerapeutico_id=proc.codProcesoTerapeutico)
    if request.method=='POST':
        form = RegistroAvanceForm(request.POST,instance=registro)
        if form.is_valid():
            x = form.save(commit=False)
            x.codProcesoTerapeutico_id = proceso
            x.nombreRecibido = request.user
            x.save()
            messages.success(request, 'Registro de avance del Proceso Terapeutico: '+str(proc.codProcesoTerapeutico)+'  Actualizado exitosamente')
            return redirect('psicologia-view',paciente=paciente.codigoPaciente)
    else:
        form = RegistroAvanceForm(instance=registro)
    return render(request,"psicologia/registroavance_nuevo.html",{"form":form,"paciente":paciente,"proceso":proc})
    
#vista para consultar el registro de avances
@login_required(login_url='logins')
def registroavance_consulta(request,proceso):
    proc = ProcesoTerapeutico.objects.get(pk=proceso)
    psico = Psicologia.objects.get(pk=proc.codPsicologia_id)
    paciente = Paciente.objects.get(pk=psico.paciente_id)
    registro = RegistroAvance.objects.filter(codProcesoTerapeutico_id=proc.codProcesoTerapeutico)
    usuario = request.user
    return render(request,"psicologia/registroavance_consultar.html",{"proc":proc,"paciente":paciente,"reg":registro,'usuario':usuario})
    

#Necesario xq el metodo del model get_full_name no me funciona en el pdf
#@login_required(login_url='logins')
def obtenerNombreCompleto(pk):
    infoPaciente = Paciente.objects.get(pk=pk)
    nombre =infoPaciente.nombrePrimero
    if infoPaciente.nombreSegundo:
         nombre += ' ' + infoPaciente.nombreSegundo + ' ' + infoPaciente.apellidoPrimero
         if infoPaciente.apellidoSegundo:
             nombre += ' '+infoPaciente.apellidoSegundo
    elif infoPaciente.apellidoSegundo:
         nombre += ' ' + infoPaciente.apellidoPrimero + ' ' + infoPaciente.apellidoSegundo
    return nombre
    
#Funcion que permite crear las 2 hojas del expediente de Psicologia
@login_required(login_url='logins')
def expedientePsicologiaPDF(request,paciente):
    
    infoPaciente = Paciente.objects.get(codigoPaciente=paciente)
    infoPsicologia = Psicologia.objects.get(paciente_id=paciente)
    doctor = Doctor.objects.get(codigoDoctor=infoPsicologia.referido_id)
    infoDoctor = Empleado.objects.get(codigoEmpleado=doctor.codigoDoctor)
    usuario = request.user
    nombre = obtenerNombreCompleto(paciente)
    
    fecha_actual = timezone.now()
    if (fecha_actual.month - infoPaciente.fechaNacimiento.month) < 0:
        edad = fecha_actual.year - (infoPaciente.fechaNacimiento.year + 1)
    elif (fecha_actual.month - infoPaciente.fechaNacimiento.month) == 0:
        if (fecha_actual.day - infoPaciente.fechaNacimiento.day) < 0:
            edad = fecha_actual.year - (infoPaciente.fechaNacimiento.year + 1)
        else:
            edad = fecha_actual.year - infoPaciente.fechaNacimiento.year
    else:
        edad = fecha_actual.year - infoPaciente.fechaNacimiento.year    
    
    sexo = ""
    if infoPaciente.sexo == 'F':
        sexo = "Femenino"
    else:
        sexo = "Masculino"
        
    estcivil = infoPaciente.estadoCivil.capitalize()
    
    if sexo == "Femenino":
        if infoPaciente.estadoCivil == 'CASADO':
            estcivil = "Casada"
        elif infoPaciente.estadoCivil == 'DIVORCIADO':                 
            estcivil = "Divorciada"
        elif infoPaciente.estadoCivil == 'ACOMPANADO':
            estcivil = "Acompanada"
        elif infoPaciente.estadoCivil == 'VIUDO':   
            estcivil = "Viuda"
        else:
            estcivil = "Soltera"    
    
    fulldireccion = infoPaciente.direccion + ', '+str(infoPaciente.codMunicipio)
    
    if infoPaciente.nombrePadre:
        nombreP = infoPaciente.nombrePadre
    else:
        nombreP = "No Proporcionado"
        
    if infoPaciente.nombreMadre:
        nombreM = infoPaciente.nombreMadre
    else:
        nombreM = "No Proporcionado"    
    
    if infoPaciente.telefono:
        tel = infoPaciente.telefono
    else:
        tel = "No Proporcionado"
    
    fecha_primeraC = str(infoPsicologia.fecha_primeraConsulta.day) + '/' +str(infoPsicologia.fecha_primeraConsulta.month)+'/'+str(infoPsicologia.fecha_primeraConsulta.year) 
    fecha_proximaC = str(infoPsicologia.fecha_proximaCita.day) + '/' +str(infoPsicologia.fecha_proximaCita.month)+'/'+str(infoPsicologia.fecha_proximaCita.year)
    
    ref = ""
    if infoDoctor.sexo == 'F':
        ref = "Dra. "+str(infoPsicologia.referido)
    else:
        ref = "Dr. "+str(infoPsicologia.referido)
    
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition']='attachment; filename="expediente_'+paciente+'.pdf"'
    
    buffer = BytesIO()
    
    doc = SimpleDocTemplate(buffer,pagesize=letter,topMargin=120)
    
    sp = 20
    sty = "Normal"
    tab = "&nbsp;"*6
    
    Story=[]
    
    texto = '<font size=11><b><i>No. EXPEDIENTE: </i></b>%s</font>' % (paciente)
    agregaTexto(texto,Story,"Derecha",sp)
    
    texto = '<font size=12><b><i>I- DATOS GENERALES:</i></b></font>'
    #texto = '<div class="row"><div class="col-md-4 col-md-offset-4">I- DATOS GENERALES:</div></div>'
    agregaTexto(texto,Story,sty,sp)
    
    texto = '<font size=11><b><i>NOMBRE: </i></b><u>%s</u></font>%s%s'\
    '<font size=11><b><i>EDAD: </i></b><u>%s A</u></font>%s%s'\
    '<font size=11><b><i>SEXO: </i></b></font><u>%s</u>'  % (nombre,tab,tab,str(edad),tab,tab,sexo.capitalize())
    agregaTexto(texto,Story,"Justify",sp)
    
    texto = '<font size=11><b><i>No HIJOS: </i></b><u>%s</u></font>%s%s'\
    '<font size=11><b><i>ESTADO CIVIL: </i></b><u>%s</u></font>%s%s'\
    '<font size=11><b><i>PROFESION U OCUPACION: </i></b><u>%s</u></font> '\
    % (str(infoPsicologia.numero_hijos),tab,tab,estcivil,tab,tab,infoPsicologia.profesion.capitalize())
    agregaTexto(texto,Story,"Justify",sp)
    
    texto = '<font size=11><b><i>DIRECCION: </i></b><u>%s</u></font>%s'\
    '<font size=11><b><i>TELEFONO: </i></b><u>%s</u></font> '\
    % (fulldireccion,tab,tel)
    agregaTexto(texto,Story,"Justify",sp)
    
    texto = '<font size=11><b><i>NOMBRE DEL PADRE:<u> %s</u></i></b><u>%s %s</u></font>'% (tab,nombreP,tab)
    #'<font size=11><b><i>NOMBRE DE LA MADRE: </i></b><u>%s</u></font>'\
    #% (nombreP)
    agregaTexto(texto,Story,"Justify",sp)
    
    texto = '<font size=11><b><i>NOMBRE DE LA MADRE:<u> %s</u></i></b><u>%s %s</u></font>'\
    % (tab,nombreM,tab)
    agregaTexto(texto,Story,"Justify",sp)
    
    texto = '<font size=11><b><i>NOMBRE DEL RESPONSABLE:<u> %s</u></i></b><u>%s %s</u></font>%s'\
    '<font size=11><b><i>TELEFONO: </i></b><u>%s</u></font> '\
    % (tab,infoPaciente.emergencia,tab,"&nbsp;&nbsp;",infoPaciente.telefonoEmergencia)
    agregaTexto(texto,Story,"Justify",sp)
    
    texto = '<font size=11><b><i>DIRECCION: </i></b><u>%s</u></font>'% (infoPsicologia.direccionResponsable)
    agregaTexto(texto,Story,"Justify",sp)
    
    texto = '<font size=11><b><i>FECHA DE LA PRIMERA CONSULTA: </i></b><u>%s</u></font>%s'\
    '<font size=11><b><i>REFERIDO POR: </i></b><u>%s</u></font> '\
    % (fecha_primeraC,"&nbsp;&nbsp;",ref)
    agregaTexto(texto,Story,"Justify",sp)
    
    texto = '<font size=11><b><i>FECHA: </i></b><u>%s/%s/%s</u></font>%s'\
    '<font size=11><b><i>RELIGION: </i></b><u>%s</u></font>%s '\
    '<font size=11><b><i>CUANTOS COMPONEN LA FAMILIA: </i></b><u>%s</u></font>'\
    % (fecha_actual.day,fecha_actual.month,fecha_actual.year,"&nbsp;&nbsp;&nbsp;",infoPsicologia.religion,"&nbsp;&nbsp;&nbsp;",str(infoPsicologia.familia))
    agregaTexto(texto,Story,"Justify",30)
    
    texto = '<font size=12><b><i>II- MOTIVO DE LA CONSULTA:</i></b></font>'
    #texto = '<div class="row"><div class="col-md-4 col-md-offset-4">I- DATOS GENERALES:</div></div>'
    agregaTexto(texto,Story,sty,sp)
    
    texto = '<font size=11><u>%s</u></font>' % (infoPsicologia.motivo)
    writeLine(texto,Story,"Justify",sp)
    saltoPagina(Story)
    
    if usuario.id == 2:
        texto = '<font size=12><b><i>III- ANTECEDENTES DEL PROBLEMA:</i></b></font>'
        agregaTexto(texto,Story,sty,sp)
        
        texto = '<font size=11><u>%s</u></font>' % (infoPsicologia.antecedentes)
        writeLine(texto,Story,"Justify2",sp)
    
    texto = '<font size=12><b><i>IV- OBSERVACIONES:</i></b></font>'
    agregaTexto(texto,Story,"Justify",sp)
    
    texto = '<font size=11><b><i>APARIENCIA EXTERNA: </i></b><u>%s</u></font>'\
    % (infoPsicologia.apariencia)
    agregaTexto(texto,Story,"Justify",sp)
    
    texto = '<font size=11><b><i>VOZ: </i></b><u>%s</u></font>%s'\
    '<font size=11><b><i>PATRONES DE HABLA: </i></b><u>%s</u></font>'\
    % (infoPsicologia.voz,tab,infoPsicologia.patrones)
    agregaTexto(texto,Story,"Justify",sp)
    
    texto = '<font size=11><b><i>EXPRESIONES FACIALES: </i></b><u>%s</u></font>%s'\
    '<font size=11><b><i>ADEMANES: </i></b><u>%s</u></font>'\
    % (infoPsicologia.expresionesF,"&nbsp;&nbsp;",infoPsicologia.ademanes)
    agregaTexto(texto,Story,"Justify",sp)
    
    texto = '<font size=11><b><i>ACTITUDES HACIA EL TX: </i></b><u>%s</u></font>'\
    % (infoPsicologia.actitudes_tx)
    writeLine(texto,Story,"Justify2",15)
    
    texto = '<font size=12><b><i>V- IMPRESION DX: </i></b><u>%s</u></font>'\
    % (infoPsicologia.impresion_dx)
    writeLine(texto,Story,"Justify2",15)
    
    texto = '<font size=12><b><i>VI- PLAN DE TX: </i></b><u>%s</u></font>'\
    % (infoPsicologia.plan_tx)
    writeLine(texto,Story,"Justify2",15)
    
    texto = '<font size=12><b><i>VII- PRONOSTICO: </i></b><u>%s</u></font>'\
    % (infoPsicologia.pronostico)
    writeLine(texto,Story,"Justify2",15)
    
    texto = '<font size=11><b><i>FECHA DE PROXIMA CITA: </i></b><u>%s</u></font>'\
    % (fecha_proximaC)
    agregaTexto(texto,Story,"Justify",sp)
    
    
    doc.build(Story,onFirstPage=headerPsico, onLaterPages=headerPsico2, canvasmaker=PageNumCanvas)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    
    return response

@login_required(login_url='logins')    
def procesoTerapeuticoPDF(request,paciente):
    pac = Paciente.objects.get(pk=paciente)
    psico = Psicologia.objects.get(paciente_id=pac.codigoPaciente)
    #psicologo = Doctor.objects.get(codigoDoctor=psico.referido_id)
    proc = ProcesoTerapeutico.objects.filter(codPsicologia_id=psico.codPsicologia)
    usuario = request.user
    nombre = obtenerNombreCompleto(paciente)
    
    buffer = BytesIO()
    response = HttpResponse(content_type='application/pdf')
	#response['Content-Disposition']='attachment; filename="ficha_ident_'+pk+'.pdf"'
    
    doc = SimpleDocTemplate(buffer,pagesize=letter,topMargin=120)
    
    #sp = 20
    #sty = "Justify"
    tab = "&nbsp;"*6
    
    Story=[]
    
    texto = '<font size=10><b><i>Paciente: </i></b>%s</font>%s'\
    '<font size=10><b><i>Psicologo: </i></b>%s</font>'\
    % (nombre,tab,usuario.first_name + ' '+usuario.last_name)
    agregaTexto(texto,Story,"Justify",10)
    
    encabezados = ('FECHA','OBJETIVO TERAPEUTICO','TECNICAS','OBSERVACIONES')
    data = []
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justificado', alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle(name='Centrado', alignment=TA_CENTER))
    for procesos in proc:
        fecha = str(procesos.fecha.day)+'/'+str(procesos.fecha.month)+'/'+str(procesos.fecha.year)
        obj = procesos.objetivo
        objetivo = Paragraph(obj,styles['Justificado'])
        obs = procesos.observaciones
        observaciones = Paragraph(obs,styles['Justificado'])
        if procesos.tecnicas == 'observacion':
            tecnicas = "Observacion"
        elif procesos.tecnicas == 'entrevista':
            tecnicas = "Entrevista"
        elif procesos.tecnicas == 'prueba':
            tecnicas = "Prueba PCA"
        elif procesos.tecnicas == 'conv':
            tecnicas = "Conv. Terapeutica"
        elif procesos.tecnicas == 'relajacion':
            tecnicas = "Tecnicas de Relajacion"
        else:
            tecnicas = "Musicoterapia"
        data.append((fecha,objetivo,tecnicas,observaciones))
    orden = Table([encabezados]+data,colWidths=[75.59, 149, 129, 139])    
    orden.setStyle(TableStyle(
        [
            #La primera fila(encabezados) va a estar centrada
            ('ALIGN',(0,0),(3,0),'CENTER'),
            #Los bordes de todas las celdas seran de color negro y con un grosor de 1
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            #El tamamo de las letras de cada una de las celdas sera de 10
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('ALIGN',(0,1),(0,-1),'CENTER'),
            ('VALIGN',(0,1),(-1,-1),'MIDDLE')
        ]
    )
    )
    Story.append(orden)
    
    doc.build(Story,onFirstPage=headerProcesos,canvasmaker=PageNumCanvas)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    
    return response
    
@login_required(login_url='logins')
def registroAvancePDF(request,proceso):
    proc = ProcesoTerapeutico.objects.get(pk=proceso)
    psico = Psicologia.objects.get(pk=proc.codPsicologia_id)
    paciente = Paciente.objects.get(pk=psico.paciente_id)
    registro = RegistroAvance.objects.filter(codProcesoTerapeutico_id=proc.codProcesoTerapeutico)
    nombre = obtenerNombreCompleto(paciente.codigoPaciente)
    usuario = request.user
    buffer = BytesIO()
    response = HttpResponse(content_type='application/pdf')
	#response['Content-Disposition']='attachment; filename="ficha_ident_'+pk+'.pdf"'
    
    doc = SimpleDocTemplate(buffer,pagesize=letter,topMargin=120)
    
    Story=[]
    tab = "&nbsp;"*6
    
    texto = '<font size=10><b><i>Paciente: </i></b>%s</font>%s'\
    '<font size=10><b><i>Psicologo: </i></b>%s</font>%s'\
    '<font size=10><b><i>Proceso Terapeutico: </i></b>%s</font>'\
    % (nombre,tab,usuario.first_name + ' '+usuario.last_name,tab,str(proceso))
    agregaTexto(texto,Story,"Justify",10)
    
    encabezados = ('FECHA','PACIENTE','PSICOLOGO')
    data = []
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justificado', alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle(name='Centrado', alignment=TA_CENTER))
    
    for registros in registro:
        fecha = str(registros.fechaRegistro.day)+'/'+str(registros.fechaRegistro.month)+'/'+str(registros.fechaRegistro.year)
        pac = registros.paciente
        paciente=Paragraph(pac,styles['Justificado'])
        psi = registros.psicologo
        psicologo = Paragraph(psi,styles['Justificado'])
        data.append((fecha,paciente,psicologo))
    
    orden=Table([encabezados]+data,colWidths=[75.59, 169, 169])
    orden.setStyle(TableStyle(
            [
                ('ALIGN',(0,0),(2,0),'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                #El tamamo de las letras de cada una de las celdas sera de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('ALIGN',(0,1),(0,-1),'CENTER'),
                ('VALIGN',(0,1),(-1,-1),'MIDDLE')
            ]
        )
    )
        
    Story.append(orden)
    
    doc.build(Story,onFirstPage=headerRegistro,canvasmaker=PageNumCanvas)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    
    return response