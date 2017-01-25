from django.shortcuts import get_object_or_404,render
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.db import connection,transaction
from django.contrib.auth.decorators import login_required,user_passes_test
from bienestarhome.admin import is_enfermera1, is_jefenfermeria, is_jefenfermeria1, is_medico, is_medico1, is_usuario4, is_usuario6, is_usuario9, is_usuario11, is_usuario12, is_usuario13
import json
import os, sys, subprocess
import xlrd
from django.db.models import Count, Avg, Sum
from django.utils.dateparse import parse_date

from nuevoingresoapp.models import importar_bd, Expediente_Provisional, Certificado_Salud, Actividad_Enfermeria, Censo_Enfermeria
from nuevoingresoapp.forms import importarBDForm, ExpedienteProForm, CertificadoForm, ActividadForm, CensoForm
from datospersonalesapp.models import Facultad
from empleadosapp.models import Doctor, Especialidad


#View para ver el listado de Expedientes de Nuevo Ingreso
@login_required(login_url='logins')
@user_passes_test(is_usuario13)
def Expediente_Provisional_list(request):
    expedientes=Expediente_Provisional.objects.order_by('facultad')
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(p.facultad_id), f.nombreFacultad FROM nuevoingresoapp_expediente_provisional as p, datospersonalesapp_facultad as f WHERE p.facultad_id = f.codigoFacultad ORDER BY f.nombreFacultad')
    auxL = cursor.fetchall()
    return render(request,"nuevoingreso/expediente_list.html",{'expedienteprovisional':expedientes,'datoFacult':auxL})

#Muestra el listado de actividades que se realizan en el area de enfermeria
@login_required(login_url='logins')
@user_passes_test(is_jefenfermeria)
def actividad_list(request):
    actividad=Actividad_Enfermeria.objects.order_by('codActividad')
    return render(request,"nuevoingreso/actividad_list.html",{'actividad':actividad})


#Muestra el informe de los pacientes que han pasado consulta general segun facultad de procedencia filtrados por rangos de fechas y agrupados por facultad, ordenados descendentemente por la cantidad de consulta por facultad
@login_required(login_url='logins')
@user_passes_test(is_usuario11)
def reporte_consulta_general_procedencia(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(f.nombreFacultad) as facultad,count(*) as cantidad FROM datospersonalesapp_facultad as f inner join datospersonalesapp_paciente as p on f.codigoFacultad = p.facultadE_id inner join generalapp_consulta as g on g.cod_expediente_id = p.codigoPaciente and g.nit_paciente = p.nit inner join empleadosapp_doctor d on g.cod_doctor_id = d.codigoDoctor inner join empleadosapp_especialidad as esp on esp.id = d.especialidad_id and esp.especialidad="Medicina General" and g.fecha between %s and %s group by f.nombreFacultad order by cantidad desc', [fechaInicio, fechaFin])
    consulta_list = cursor.fetchall()
    return render(request,"nuevoingreso/reporte_consulta_general_procedencia.html",{'consulta_list':consulta_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})

#Muestra el informe de los pacientes que han pasado consulta general segun genero filtrados por rangos de fechas y agrupados por genero, ordenados descendentemente por la cantidad de consulta por genero
@login_required(login_url='logins')
@user_passes_test(is_usuario11)
def reporte_consulta_general_genero(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(p.sexo) as genero,count(*) as cantidad FROM datospersonalesapp_paciente as p inner join generalapp_consulta as g on g.cod_expediente_id = p.codigoPaciente and g.nit_paciente = p.nit inner join empleadosapp_doctor d on g.cod_doctor_id = d.codigoDoctor inner join empleadosapp_especialidad as esp on esp.id = d.especialidad_id and esp.especialidad="Medicina General" and g.fecha between %s and %s group by p.sexo order by cantidad desc', [fechaInicio, fechaFin])
    consulta_list = cursor.fetchall()
    return render(request,"nuevoingreso/reporte_consulta_general_genero.html",{'consulta_list':consulta_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})

#Muestra el informe de los pacientes que han pasado consulta general segun el tipo de paciente (Estudiante, Docente, Ordenanzas, Etc) filtrados por rangos de fechas y agrupados por tipo de paciente, ordenados descendentemente por la cantidad de consulta por tipo de paciente
@login_required(login_url='logins')
@user_passes_test(is_usuario11)
def reporte_consulta_general_tipo_paciente(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(p.estadoUes) as genero,count(*) as cantidad FROM datospersonalesapp_paciente as p inner join generalapp_consulta as g on g.cod_expediente_id = p.codigoPaciente inner join empleadosapp_doctor d on g.cod_doctor_id = d.codigoDoctor inner join empleadosapp_especialidad as esp on esp.id = d.especialidad_id and esp.especialidad="Medicina General" and g.fecha between %s and %s group by p.estadoUes order by cantidad desc', [fechaInicio, fechaFin])
    consulta_list = cursor.fetchall()
    return render(request,"nuevoingreso/reporte_consulta_general_paciente.html",{'consulta_list':consulta_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})


#Muestra el informe de pacientes atendidos por cada doctor filtrados por rangos de fechas y agrupados por consultas, ordenados descendentemente por la cantidad de consulta dadas
@login_required(login_url='logins')
@user_passes_test(is_usuario4)
def reporte_pacientes_por_medico(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(g.cod_doctor_id) as doctor,CONCAT("Dr(a). ",e.nombrePrimero," ",e.apellidoPrimero) as nombre,count(*) as cantidad FROM empleadosapp_empleado as e inner join empleadosapp_doctor d on e.codigoEmpleado = d.codigoEmpleado_id inner join generalapp_consulta as g on g.cod_doctor_id = d.codigoDoctor and g.fecha between %s and %s group by g.cod_doctor_id order by cantidad desc', [fechaInicio, fechaFin])
    consulta_list = cursor.fetchall()
    return render(request,"nuevoingreso/reporte_pacientes_por_medico.html",{'consulta_list':consulta_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})


@login_required(login_url='logins')
@user_passes_test(is_usuario4)
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
@user_passes_test(is_usuario4)
def reporte_tipo_consulta(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor = connection.cursor()
    cursor.execute('SELECT g.tipo_consulta as tipo, count(*) as cantidad from generalapp_consulta as g where g.fecha between %s and %s group by g.tipo_consulta order by cantidad desc', [fechaInicio, fechaFin])
    consulta_list = cursor.fetchall()
    return render(request,"nuevoingreso/reporte_tipo_consulta.html",{'consulta_list':consulta_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})

@login_required(login_url='logins')
@user_passes_test(is_usuario4)
def reporte_visto_bueno(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor = connection.cursor()
    cursor.execute('SELECT p.sexo as sexo,count(*) as cantidad FROM generalapp_consulta as g inner join datospersonalesapp_paciente as p on g.cod_expediente_id = p.codigoPaciente  where g.visto_bueno <> "''" and g.visto_bueno="Si" and g.fecha between %s and %s group by p.sexo order by cantidad desc', [fechaInicio, fechaFin])
    consulta_list = cursor.fetchall()
    return render(request,"nuevoingreso/reporte_visto_bueno.html",{'consulta_list':consulta_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})

@login_required(login_url='logins')
@user_passes_test(is_jefenfermeria1)
def censo_list(request):
    censo=Censo_Enfermeria.objects.order_by('codCenso')
    return render(request,"nuevoingreso/censo_list.html",{'censo':censo})

#Vista para crear expedientes a partir de la pagina de listado de expedientes
@login_required(login_url='logins')
@user_passes_test(is_usuario6)
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
@user_passes_test(is_jefenfermeria1)
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
@user_passes_test(is_jefenfermeria1)
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
@user_passes_test(is_usuario9)
def expedienteprovisional_detalle(request,pk):
    expediente = Expediente_Provisional.objects.get(pk=pk) 
    return render(request, "nuevoingreso/expediente_detalle.html", {'expediente':expediente})

@login_required(login_url='logins')
@user_passes_test(is_jefenfermeria1)
def expedienteprovisional_modificar(request,pk):
    expediente = Expediente_Provisional.objects.get(pk=pk) 
    return render(request, "nuevoingreso/expediente_modificar.html", {'expediente':expediente})

@login_required(login_url='logins')
@user_passes_test(is_jefenfermeria1)
def expedienteprovisional_eliminar2(request,pk):
    form = Expediente_Provisional.objects.get(pk=pk) 
    return render(request, "nuevoingreso/expediente_eliminar.html", {'form':form})

#View para modificar los datos de un expediente provisional
@login_required(login_url='logins')
@user_passes_test(is_jefenfermeria1)
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
@user_passes_test(is_jefenfermeria1)
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
@user_passes_test(is_medico)
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
@user_passes_test(is_medico1)
def certificado_salud_ver(request,pk):
    expediente = Expediente_Provisional.objects.get(pk=pk) 
    return render(request, "nuevoingreso/certificado_salud.html", {'expediente':expediente})

@login_required(login_url='logins')
@user_passes_test(is_jefenfermeria)
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
@user_passes_test(is_usuario12)
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

@login_required(login_url='logins')
def importar_bd_nuevo(request):
    form = importarBDForm()
    archivos = request.FILES.get('archivo')
    if request.method == "POST":
        data1={'archivo':archivos}
        archivo = importarBDForm(data1,request.FILES or None)
        if archivo.is_valid():
                archivoBD = archivo.save(commit=False)
                archivoBD.save()
                cursor = connection.cursor()
                cursor.execute('SELECT max(codImportar_BD) as id from nuevoingresoapp_importar_bd')
                consulta = cursor.fetchall()
                aux = 0
                for valor in consulta:
                    if(aux < valor[0]):
                        aux = valor[0]
                    else:
                        aux = 0
                pk = int(aux)
                baseDatos = importar_bd.objects.get(pk=pk)
                pathAux=str(baseDatos.archivo)
                BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                MEDIA_ROOT = os.path.join(BASE_DIR,"exameneslab/") + pathAux
                book = xlrd.open_workbook(MEDIA_ROOT)
                sheet = book.sheet_by_name("source")
                query = '''INSERT INTO nuevoingresoapp_expediente_provisional(nombrePrimero,nombreSegundo,apellidoPrimero,apellidoSegundo,sexo,fechaNacimiento,telefono,correo, fechaIngreso, talla,temperatura,presionArterial,peso,frecuenciaRespiratoria,frecuenciaCardiaca,nit,facultad_id,nombreRecibido_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

                for r in range(1,sheet.nrows):
                    nombrePrimero = sheet.cell(r,0).value
                    nombreSegundo = sheet.cell(r,1).value
                    apellidoPrimero = sheet.cell(r,2).value
                    apellidoSegundo = sheet.cell(r,3).value
                    sexo = sheet.cell(r,4).value
                    fechaNacimiento = sheet.cell(r,5).value
                    telefono = sheet.cell(r,6).value
                    correo = sheet.cell(r,7).value
                    fechaIngreso = timezone.now()
                    talla = 0
                    temperatura = 0
                    presionArterial = str(0)
                    peso = 0
                    frecuenciaRespiratoria = 0
                    frecuenciaCardiaca = 0
                    nit = sheet.cell(r,8).value
                    facultad_id = sheet.cell(r,9).value
                    nombreRecibido_id = request.user.id
                    data = (nombrePrimero, nombreSegundo, apellidoPrimero, apellidoSegundo, sexo, fechaNacimiento,telefono, correo, fechaIngreso, talla, temperatura, presionArterial, peso, frecuenciaRespiratoria, frecuenciaCardiaca, nit, facultad_id, nombreRecibido_id)
                    cursor2 = connection.cursor()
                    cursor2.execute(query,data)
                transaction.commit()
                os.remove(MEDIA_ROOT)
                baseDatos.delete()
                return redirect('home')
        else:
            form=importarBDForm()
    return render(request, "nuevoingreso/importar_bd.html", {'form':form})    