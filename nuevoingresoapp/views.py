from django.shortcuts import get_object_or_404,render
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
import time
from django.db import connection
import json
from django.db.models import Count, Avg, Sum
from django.utils.dateparse import parse_date

from nuevoingresoapp.models import Expediente_Provisional, Certificado_Salud, Actividad_Enfermeria, Censo_Enfermeria
from nuevoingresoapp.forms import ExpedienteProForm, CertificadoForm, ActividadForm, CensoForm
from datospersonalesapp.models import Facultad
from enfermeriaapp.forms import ColaConsultaForm, ColaEnfermeriaForm
from empleadosapp.models import Doctor, Especialidad


#View para ver el listado de Expedientes de Nuevo Ingreso
@login_required(login_url='logins')
def Expediente_Provisional_list(request):
    expedientes=Expediente_Provisional.objects.order_by('facultad')
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(p.facultad_id), f.nombreFacultad FROM nuevoingresoapp_expediente_provisional as p, datospersonalesapp_facultad as f WHERE p.facultad_id = f.codigoFacultad ORDER BY f.nombreFacultad')
    auxL = cursor.fetchall()
    return render(request,"nuevoingreso/expediente_list.html",{'expedienteprovisional':expedientes,'datoFacult':auxL})

#Muestra el listado de actividades que se realizan en el area de enfermeria
@login_required(login_url='logins')
def actividad_list(request):
    actividad=Actividad_Enfermeria.objects.order_by('codActividad')
    return render(request,"nuevoingreso/actividad_list.html",{'actividad':actividad})

#Muestra el informe de actividades de enfermeria filtrado por rangos de fechas y agrupados por actividad, ordenados descendentemente por la cantidad de actividad
@login_required(login_url='logins')
def reporte_censo(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(a.codActividad),a.nombreActividad,sum(c.cantidad) as cantidad FROM nuevoingresoapp_censo_enfermeria as c inner join nuevoingresoapp_actividad_enfermeria as a where c.actividad_id = a.codActividad and c.fechaActividad between %s and %s group by c.actividad_id order by cantidad desc', [fechaInicio, fechaFin])
    censo_list = cursor.fetchall()
    return render(request,"nuevoingreso/reporte_censo_actividades.html",{'censo_list':censo_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})

#Muestra el informe de los pacientes que han pasado consulta general segun facultad de procedencia filtrados por rangos de fechas y agrupados por facultad, ordenados descendentemente por la cantidad de consulta por facultad
@login_required(login_url='logins')
def reporte_consulta_general_procedencia(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(f.nombreFacultad) as facultad,count(*) as cantidad FROM datospersonalesapp_facultad as f inner join datospersonalesapp_paciente as p on f.codigoFacultad = p.facultadE_id inner join generalapp_consulta as g on g.cod_expediente_id = p.codigoPaciente and g.nit_paciente = p.nit inner join empleadosapp_doctor d on g.cod_doctor_id = d.codigoDoctor inner join empleadosapp_especialidad as esp on esp.id = d.especialidad_id and esp.especialidad="Medicina General" and g.fecha between %s and %s group by f.nombreFacultad order by cantidad desc', [fechaInicio, fechaFin])
    consulta_list = cursor.fetchall()
    return render(request,"nuevoingreso/reporte_consulta_general_procedencia.html",{'consulta_list':consulta_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})

#Muestra el informe de los pacientes que han pasado consulta general segun genero filtrados por rangos de fechas y agrupados por genero, ordenados descendentemente por la cantidad de consulta por genero
@login_required(login_url='logins')
def reporte_consulta_general_genero(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(p.sexo) as genero,count(*) as cantidad FROM datospersonalesapp_paciente as p inner join generalapp_consulta as g on g.cod_expediente_id = p.codigoPaciente and g.nit_paciente = p.nit inner join empleadosapp_doctor d on g.cod_doctor_id = d.codigoDoctor inner join empleadosapp_especialidad as esp on esp.id = d.especialidad_id and esp.especialidad="Medicina General" and g.fecha between %s and %s group by p.sexo order by cantidad desc', [fechaInicio, fechaFin])
    consulta_list = cursor.fetchall()
    return render(request,"nuevoingreso/reporte_consulta_general_genero.html",{'consulta_list':consulta_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})

#Muestra el informe de los pacientes que han pasado consulta general segun el tipo de paciente (Estudiante, Docente, Ordenanzas, Etc) filtrados por rangos de fechas y agrupados por tipo de paciente, ordenados descendentemente por la cantidad de consulta por tipo de paciente
@login_required(login_url='logins')
def reporte_consulta_general_tipo_paciente(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(p.estadoUes) as genero,count(*) as cantidad FROM datospersonalesapp_paciente as p inner join generalapp_consulta as g on g.cod_expediente_id = p.codigoPaciente inner join empleadosapp_doctor d on g.cod_doctor_id = d.codigoDoctor inner join empleadosapp_especialidad as esp on esp.id = d.especialidad_id and esp.especialidad="Medicina General" and g.fecha between %s and %s group by p.estadoUes order by cantidad desc', [fechaInicio, fechaFin])
    consulta_list = cursor.fetchall()
    return render(request,"nuevoingreso/reporte_consulta_general_paciente.html",{'consulta_list':consulta_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})

#Muestra el informe de morbilidad de antiguo ingreso filtrados por rangos de fechas y agrupados por morbilidad, ordenados descendentemente por la cantidad de consulta por morbilidad
@login_required(login_url='logins')
def reporte_morbilidad(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor1.execute('SELECT distinct(g.diagnostico_principal) as morbilidad,count(*) as cantidad FROM generalapp_consulta as g inner join datospersonalesapp_paciente as p on g.cod_expediente_id = p.codigoPaciente and g.fecha between %s and %s group by g.diagnostico_principal order by cantidad desc limit 0,10', [fechaInicio, fechaFin])
    cursor2.execute('SELECT distinct(g.diagnostico_principal) as morbilidad,count(*) as cantidad FROM generalapp_consulta as g inner join nuevoingresoapp_expediente_provisional as p on g.cod_expediente_id = p.Cod_Expediente_Provisional and g.fecha between %s and %s group by g.diagnostico_principal order by cantidad desc limit 0,10', [fechaInicio, fechaFin])
    morbilidadAntiguo_list = cursor1.fetchall()
    morbilidadNuevo_list = cursor2.fetchall()
    return render(request,"nuevoingreso/reporte_morbilidad.html",{'morbilidadAntiguo_list':morbilidadAntiguo_list,'morbilidadNuevo_list':morbilidadNuevo_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})


#Muestra el informe de morbilidad de antiguo ingreso filtrados por rangos de fechas y agrupados por morbilidad, ordenados descendentemente por la cantidad de consulta por morbilidad
@login_required(login_url='logins')
def reporte_morbilidad_antiguo_ingreso(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(g.diagnostico_principal) as morbilidad,count(*) as cantidad FROM generalapp_consulta as g inner join datospersonalesapp_paciente as p on g.cod_expediente_id = p.codigoPaciente and g.fecha between %s and %s group by g.diagnostico_principal order by cantidad desc limit 0,10', [fechaInicio, fechaFin])
    consulta_list = cursor.fetchall()
    return render(request,"nuevoingreso/reporte_morbilidad_antiguo_ingreso.html",{'consulta_list':consulta_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})

#Muestra el informe de morbilidad de nuevo ingreso filtrados por rangos de fechas y agrupados por morbilidad, ordenados descendentemente por la cantidad de consulta por morbilidad
@login_required(login_url='logins')
def reporte_morbilidad_nuevo_ingreso(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor = connection.cursor()
    #cursor1 = connection.cursor()
    cursor.execute('SELECT distinct(g.diagnostico_principal) as morbilidad,count(*) as cantidad FROM generalapp_consulta as g inner join nuevoingresoapp_expediente_provisional as p on g.cod_expediente_id = p.Cod_Expediente_Provisional and g.fecha between %s and %s group by g.diagnostico_principal order by cantidad desc limit 0,10', [fechaInicio, fechaFin])
    consulta_list = cursor.fetchall()
    #cursor1.execute('SELECT distinct(g.diagnostico_principal) as morbilidad,count(*) as cantidad FROM generalapp_consulta as g inner join datospersonalesapp_paciente as p on g.cod_expediente_id = p.codigoPaciente and g.fecha between %s and %s group by g.diagnostico_principal order by cantidad desc limit 0,10', [fechaInicio, fechaFin])
    #consulta_list += cursor1.fetchall()
    return render(request,"nuevoingreso/reporte_morbilidad_nuevo_ingreso.html",{'consulta_list':consulta_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})

#Muestra el informe de pacientes atendidos por cada doctor filtrados por rangos de fechas y agrupados por consultas, ordenados descendentemente por la cantidad de consulta dadas
@login_required(login_url='logins')
def reporte_pacientes_por_medico(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(g.cod_doctor_id) as doctor,CONCAT("Dr(a). ",e.nombrePrimero," ",e.apellidoPrimero) as nombre,count(*) as cantidad FROM empleadosapp_empleado as e inner join empleadosapp_doctor d on e.codigoEmpleado = d.codigoEmpleado_id inner join generalapp_consulta as g on g.cod_doctor_id = d.codigoDoctor and g.fecha between %s and %s group by g.cod_doctor_id order by cantidad desc', [fechaInicio, fechaFin])
    consulta_list = cursor.fetchall()
    return render(request,"nuevoingreso/reporte_pacientes_por_medico.html",{'consulta_list':consulta_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})

#Muestra el informe de consultas por especialidad filtrados por rangos de fechas y agrupados por especialidad, ordenados descendentemente por la cantidad de consulta dadas
@login_required(login_url='logins')
def reporte_consultas_especialidad(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor1 = connection.cursor()
    cursor1.execute('SELECT distinct(g.cod_doctor_id) as doctor,esp.especialidad as especialidad,count(*) as cantidad FROM empleadosapp_especialidad as esp inner join empleadosapp_doctor d on esp.id = d.especialidad_id inner join generalapp_consulta as g on g.cod_doctor_id = d.codigoDoctor and g.fecha between %s and %s WHERE g.cod_expediente_id LIKE "%%-%%"  group by d.especialidad_id order by cantidad desc', [fechaInicio, fechaFin])
    antiguo_list = cursor1.fetchall()
    
    cursor2 = connection.cursor()
    cursor2.execute('SELECT distinct(g.cod_doctor_id) as doctor,esp.especialidad as especialidad,count(*) as cantidad FROM empleadosapp_especialidad as esp inner join empleadosapp_doctor d on esp.id = d.especialidad_id inner join generalapp_consulta as g on g.cod_doctor_id = d.codigoDoctor and g.fecha between %s and %s WHERE g.cod_expediente_id NOT LIKE "%%-%%"  group by d.especialidad_id order by cantidad desc', [fechaInicio, fechaFin])
    nuevo_list = cursor2.fetchall()
    return render(request,"nuevoingreso/reporte_consulta_especialidad.html",{'antiguo_list':antiguo_list,'nuevo_list':nuevo_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})

@login_required(login_url='logins')
def reporte_referencias(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor1.execute('SELECT r.referido_a as referencia, count(*) as cantidad from generalapp_referenciainterna as r where r.referido_a <> "''" and r.fecha between %s and %s group by r.referido_a order by cantidad desc', [fechaInicio, fechaFin])
    cursor2.execute('SELECT r.referido_a as referencia, count(*) as cantidad from generalapp_referenciaexterna as r where r.referido_a <> "''" and r.fecha between %s and %s group by r.referido_a order by cantidad desc', [fechaInicio, fechaFin])
    interna_list = cursor1.fetchall()
    externa_list = cursor2.fetchall()
    return render(request,"nuevoingreso/reporte_referencias.html",{'interna_list':interna_list,'externa_list':externa_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})

@login_required(login_url='logins')
def reporte_tipo_consulta(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor = connection.cursor()
    cursor.execute('SELECT g.tipo_consulta as tipo, count(*) as cantidad from generalapp_consulta as g where g.fecha between %s and %s group by g.tipo_consulta order by cantidad desc', [fechaInicio, fechaFin])
    consulta_list = cursor.fetchall()
    return render(request,"nuevoingreso/reporte_tipo_consulta.html",{'consulta_list':consulta_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})

@login_required(login_url='logins')
def reporte_visto_bueno(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor = connection.cursor()
    cursor.execute('SELECT p.sexo as sexo,count(*) as cantidad FROM generalapp_consulta as g inner join datospersonalesapp_paciente as p on g.cod_expediente_id = p.codigoPaciente  where g.visto_bueno <> "''" and g.visto_bueno="Si" and g.fecha between %s and %s group by p.sexo order by cantidad desc', [fechaInicio, fechaFin])
    consulta_list = cursor.fetchall()
    return render(request,"nuevoingreso/reporte_visto_bueno.html",{'consulta_list':consulta_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})

@login_required(login_url='logins')
def censo_list(request):
    censo=Censo_Enfermeria.objects.order_by('codCenso')
    return render(request,"nuevoingreso/censo_list.html",{'censo':censo})

#Vista para crear expedientes a partir de la pagina de listado de expedientes
@login_required(login_url='logins')
def expedienteprovisional_nuevo(request):
    doctores = Doctor.objects.filter(especialidad_id = Especialidad.objects.filter(especialidad="Medicina General") )
    info = ""
    form = ExpedienteProForm()
    if request.method == "POST":
        form = ExpedienteProForm(request.POST)
        doctor ={'idDoctor':Doctor.objects.filter(codigoDoctor = request.POST.get('doctor'))
            
        }
        if form.is_valid():
            expediente = form.save(commit=False)
            expediente.nombreRecibido=request.user
            expediente.fechaIngreso=timezone.now()
            expediente.save()
            info = "Datos Guardados Exitosamente"
            consultaForm = ColaConsultaForm(doctor)
            if consultaForm.is_valid():
                consulta = consultaForm.save(commit=False)
                datos = Expediente_Provisional.objects.get(nit=request.POST.get('nit'))
                consulta.nit = datos.nit
                consulta.hora = time.strftime("%H:%M:%S") #Formato de 24 horas
                consulta.save()
                return redirect("cola_consulta-list")
            else:
                return redirect('expedienteprovisonal-list')
        else:
            form=ExpedienteProForm()
            info = "Ocurrio un error los datos no se guardaron"
    return render(request,"nuevoingreso/expediente_editar.html",{'form':form,'informacion':info,'doctores':doctores})

@login_required(login_url='logins')
def expedienteprovisional_editar(request,pk):
    info = ""
    expediente = Expediente_Provisional.objects.get(pk=pk)
    facultades = Facultad.objects.all()
    form = ExpedienteProForm()
    t = request.POST.get('talla')
    tp = request.POST.get('temperatura')
    p = request.POST.get('peso')
    if request.method == "POST":
        data={'nombrePrimero':request.POST.get('primerNombre'),'nombreSegundo':request.POST.get('segundoNombre'),'apellidoPrimero':request.POST.get('primerApellido'),
            'apellidoSegundo':request.POST.get('segundoApellido'),'fechaNacimiento':request.POST.get('fechaNacimiento'),'facultad':Facultad.objects.filter(nombreFacultad = request.POST.get('facultad')),
            'telefono':request.POST.get('telefono'),'correo':request.POST.get('correo'),'presionArterial':request.POST.get('presionArterial'),'Observaciones':request.POST.get('Observaciones'),
            'talla':float(t.replace(',', '.')),'temperatura':float(tp.replace(',', '.')),'peso':float(p.replace(',', '.')),'frecuenciaRespiratoria':int(request.POST.get('frecuenciaRespiratoria')),
            'frecuenciaCardiaca':int(request.POST.get('frecuenciaCardiaca'))
        }
        form = ExpedienteProForm(data,instance=expediente)
        if form.is_valid():
            expediente = form.save(commit=False)
            expediente.nombreRecibido=request.user
            expediente.fechaIngreso=timezone.now()
            expediente.save()
            info = "Datos Guardados Exitosamente"
            return redirect('expedienteprovisonal-view',pk=expediente.Cod_Expediente_Provisional)
        else:
            form=ExpedienteProForm(data,instance=expediente)
            info = "Ocurrio un error los datos no se actualizaron"
    return render(request,"nuevoingreso/expediente_modificar.html",{'expediente':expediente,'informacion':info,'facultades':facultades})

#Vista para eliminar un expediente provisional de un paciente
@login_required(login_url='logins')
def expedienteprovisional_eliminar1(request,pk):
    info = ""
    form = Expediente_Provisional.objects.get(pk=pk)
    facultades = Facultad.objects.all()
    form1 = ExpedienteProForm()
    t = request.POST.get('talla')
    tp = request.POST.get('temperatura')
    p = request.POST.get('peso')
    if request.method == "POST":
        data={'nombrePrimero':request.POST.get('primerNombre'),'nombreSegundo':request.POST.get('segundoNombre'),'apellidoPrimero':request.POST.get('primerApellido'),
            'apellidoSegundo':request.POST.get('segundoApellido'),'fechaNacimiento':request.POST.get('fechaNacimiento'),'facultad':Facultad.objects.filter(nombreFacultad = request.POST.get('facultad')),
            'telefono':request.POST.get('telefono'),'correo':request.POST.get('correo'),'presionArterial':request.POST.get('presionArterial'),'Observaciones':request.POST.get('Observaciones'),
            'talla':float(t.replace(',', '.')),'temperatura':float(tp.replace(',', '.')),'peso':float(p.replace(',', '.')),'frecuenciaRespiratoria':int(request.POST.get('frecuenciaRespiratoria')),
            'frecuenciaCardiaca':int(request.POST.get('frecuenciaCardiaca'))
        }
        form1 = ExpedienteProForm(data,instance=form)
        if form1.is_valid():
            form = form1.save(commit=False)
            form.delete()
            info = "Datos eliminados"
            return redirect('expedienteprovisonal-list')
        else:
            form1=ExpedienteProForm(data,instance=form)
            info = "Ocurrio un error no se pudo eliminar el registro"
    return render(request,"nuevoingreso/expediente_eliminar.html",{'form':form,'informacion':info,'facultades':facultades})

#Vista para ver el contenido de atributos del expediente provisional de un paciente
@login_required(login_url='logins')
def expedienteprovisional_detalle(request,pk):
    expediente = Expediente_Provisional.objects.get(pk=pk) 
    return render(request, "nuevoingreso/expediente_detalle.html", {'expediente':expediente})

@login_required(login_url='logins')
def expedienteprovisional_modificar(request,pk):
    expediente = Expediente_Provisional.objects.get(pk=pk) 
    return render(request, "nuevoingreso/expediente_modificar.html", {'expediente':expediente})

@login_required(login_url='logins')
def expedienteprovisional_eliminar2(request,pk):
    form = Expediente_Provisional.objects.get(pk=pk) 
    return render(request, "nuevoingreso/expediente_eliminar.html", {'form':form})

#View para modificar los datos de un expediente provisional
@login_required(login_url='logins')
def expedienteprov_modificar(request, pk):
    paciente = Expediente_Provisional.objects.get(pk=pk)
    expediente = Expediente_Provisional.objects.get(pk=pk)
    if request.method == "POST":
        formP = ExpedienteProForm(request.POST,instance=paciente)
        if formP.is_valid():
            paciente = formP.save(commit=False)
            paciente.nombreRecibido=request.user
            paciente.Observaciones = request.POST.get('Observaciones')
            paciente.save()
            messages.success(request,'Se ha modificado el Expediente: '+paciente.nombrePrimero+ paciente.apellidoPrimero+' Exitosamente')
            return redirect('expedienteprovisonal-view',pk=paciente.Cod_Expediente_Provisional)
    else:
        formP=ExpedienteProForm(instance=paciente)      
    return render(request,"nuevoingreso/expediente_editar.html",{'form':formP,'expediente':expediente})

@login_required(login_url='logins')
def expedienteprovisional_eliminar(request, pk):
    paciente = Expediente_Provisional.objects.get(pk=pk)
    expediente = Expediente_Provisional.objects.get(pk=pk)
    if request.method == "POST":
        formP = ExpedienteProForm(request.POST,instance=paciente)
        if formP.is_valid():
            paciente = formP.save(commit=False)
            paciente.nombreRecibido=request.user
            paciente.delete()
            messages.success(request,'Se ha eliminado el expediente exitosamente')
            return redirect('expedienteprovisonal-list')
    else:
        formP=ExpedienteProForm(instance=paciente)      
    return render(request,"nuevoingreso/expediente_eliminar.html",{'form':formP,'expediente':expediente})

#View para ingresar un certificado de salud
@login_required(login_url='logins')
def certificado_salud_nuevo(request,pk):
    info = ""
    paciente = Expediente_Provisional.objects.get(pk=pk)
    paciente.nombreRecibido = request.user
    paciente.fechaIngreso=timezone.now()
    certificado = CertificadoForm()
    if request.method == "POST":
        certificado = CertificadoForm(request.POST)
        if certificado.is_valid():
            certificadoSalud = certificado.save(commit=False)
            certificadoSalud.codigoPaciente = paciente
            certificadoSalud.nombreRecibido=request.user
            certificadoSalud.fechaIngreso=timezone.now()
            certificadoSalud.save()
            info = "Datos Guardados Exitosamente"
            return redirect('expedienteprovisonal-list')
        else:
            certificado=CertificadoForm()
            info = "Ocurrio un error los datos no se guardaron"
    return render(request,"nuevoingreso/certificado_salud.html",{'certificado':certificado,'informacion':info,'paciente':paciente})

@login_required(login_url='logins')
def certificado_salud_ver(request,pk):
    expediente = Expediente_Provisional.objects.get(pk=pk) 
    return render(request, "nuevoingreso/certificado_salud.html", {'expediente':expediente})

@login_required(login_url='logins')
def actividad_nuevo(request):
    info = ""
    form = ActividadForm()
    if request.method == "POST":
        form = ActividadForm(request.POST)
        if form.is_valid():
            actividad = form.save(commit=False)
            actividad.nombreRecibido=request.user
            actividad.fechaActividad=timezone.now()
            actividad.save()
            info = "Datos Guardados Exitosamente"
            return redirect('actividades-list')
        else:
            form=ActividadForm()
            info = "Ocurrio un error los datos no se guardaron"
    return render(request,"nuevoingreso/actividad_editar.html",{'form':form,'informacion':info})

@login_required(login_url='logins')
def censo_nuevo(request):
    info = ""
    form = CensoForm()
    if request.method == "POST":
        form = CensoForm(request.POST)
        if form.is_valid():
            censo = form.save(commit=False)
            censo.nombreRecibido=request.user
            censo.fechaActividad=timezone.now()
            censo.save()
            info = "Datos Guardados Exitosamente"
            return redirect('censo-list')
        else:
            form=CensoForm()
            info = "Ocurrio un error los datos no se guardaron"
    return render(request,"nuevoingreso/censo_editar.html",{'form':form,'informacion':info})    