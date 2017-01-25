from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from bienestarhome.admin import is_jefenfermeria, is_usuario15, is_usuario4
from django.contrib.auth.decorators import login_required
import xlsxwriter
#import StringIO
import csv
from datetime import datetime, date
from django.db import connection


@login_required(login_url='logins')
@user_passes_test(is_jefenfermeria)
def vistoBuenoExcel(request,inicio,fin):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporteVistoBueno.xlsx"'
    cursor = connection.cursor()
    cursor.execute('SELECT p.sexo as sexo,count(*) as cantidad FROM generalapp_consulta as g inner join datospersonalesapp_paciente as p on g.cod_expediente_id = p.codigoPaciente  where g.visto_bueno <> "''" and g.visto_bueno="Si" and g.fecha between %s and %s group by p.sexo order by cantidad desc', [inicio, fin])
    consulta_list = cursor.fetchall()
    
    workbook = xlsxwriter.Workbook(response, {'in_memory': True})
    
    worksheet = workbook.add_worksheet()
    
    bold = workbook.add_format({'bold': 1})
    
    chart1 = workbook.add_chart({'type': 'pie'})
    
    headings = ['Visto Bueno','Cantidad']
    i = 2;
    for consulta in consulta_list:
        worksheet.set_column('A:A', 30)
        worksheet.write('A' + str(i), consulta[0])
        worksheet.write('B' + str(i), consulta[1])
        i+=1
    
    worksheet.write_row('A1', headings, bold)
    i = i-1
    chart1.add_series({
    'name':       '=Sheet1!$B$1',
    'categories':       '=Sheet1!$A$2:$A$3',
    'values':     '=Sheet1!$B$2'+':'+'$B$'+str(i),
    'data_labels': {'value': True,'percentage': True,'category': True},
    'gradient': {
    'type': 'radial'
    }
    })
    
    fechaInicio = datetime.strptime(inicio, '%Y-%m-%d').date()
    fechaFin = datetime.strptime(fin, '%Y-%m-%d').date()
    
    chart1.set_title({'name': 'Reporte de Vistos Bueno del '+str(fechaInicio.day)+'/' + str(fechaInicio.month)+'/'+str(fechaInicio.year)+' al '+str(fechaFin.day)+'/'+str(fechaFin.month)+'/'+str(fechaFin.year)+' '})
    chart1.set_size({'width': 520, 'height': 370})
    chart1.set_x_axis({'name': 'Visto Bueno'})
    chart1.set_y_axis({'name': 'Cantidad'})
    chart1.set_table()
    
    worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
    workbook.close()
    return response

@login_required(login_url='logins')
@user_passes_test(is_usuario15)
def reporteConsultaProcedenciaExcel(request,inicio,fin):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporteConsultaProcedencia.xlsx"'
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(f.nombreFacultad) as facultad,count(*) as cantidad FROM datospersonalesapp_facultad as f inner join datospersonalesapp_paciente as p on f.codigoFacultad = p.facultadE_id inner join generalapp_consulta as g on g.cod_expediente_id = p.codigoPaciente and g.nit_paciente = p.nit inner join empleadosapp_doctor d on g.cod_doctor_id = d.codigoDoctor inner join empleadosapp_especialidad as esp on esp.id = d.especialidad_id and esp.especialidad="Medicina General" and g.fecha between %s and %s group by f.nombreFacultad order by cantidad desc', [inicio, fin])
    consulta_list = cursor.fetchall()
    
    workbook = xlsxwriter.Workbook(response, {'in_memory': True})
    
    worksheet = workbook.add_worksheet()
    
    bold = workbook.add_format({'bold': 1})
    
    chart1 = workbook.add_chart({'type': 'pie'})
    
    headings = ['Procedencia','Cantidad']
    i = 2;
    for consulta in consulta_list:
        worksheet.set_column('A:A', 30)
        worksheet.write('A' + str(i), consulta[0])
        worksheet.write('B' + str(i), consulta[1])
        i+=1
    
    worksheet.write_row('A1', headings, bold)
    i = i-1
    chart1.add_series({
    'name':       '=Sheet1!$B$1',
    'categories':       '=Sheet1!$A$2'+':'+'$A$'+str(i),
    'values':     '=Sheet1!$B$2'+':'+'$B$'+str(i),
    'data_labels': {'value': True,'percentage': True,'category': True},
    'gradient': {
    'type': 'radial'
    }
    })
    
    fechaInicio = datetime.strptime(inicio, '%Y-%m-%d').date()
    fechaFin = datetime.strptime(fin, '%Y-%m-%d').date()
    
    chart1.set_title({'name': 'Reporte de Consultas Generales Segun Procedencia del '+str(fechaInicio.day)+'/' + str(fechaInicio.month)+'/'+str(fechaInicio.year)+' al '+str(fechaFin.day)+'/'+str(fechaFin.month)+'/'+str(fechaFin.year)+' '})
    chart1.set_size({'width': 720, 'height': 570})
    chart1.set_x_axis({'name': 'Procedencia'})
    chart1.set_y_axis({'name': 'Cantidad'})
    chart1.set_table()
    
    worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
    workbook.close()
    return response

@login_required(login_url='logins')
@user_passes_test(is_usuario15)
def reporteConsultaGeneroExcel(request,inicio,fin):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporteConsultaGenero.xlsx"'
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(p.sexo) as genero,count(*) as cantidad FROM datospersonalesapp_paciente as p inner join generalapp_consulta as g on g.cod_expediente_id = p.codigoPaciente and g.nit_paciente = p.nit inner join empleadosapp_doctor d on g.cod_doctor_id = d.codigoDoctor inner join empleadosapp_especialidad as esp on esp.id = d.especialidad_id and esp.especialidad="Medicina General" and g.fecha between %s and %s group by p.sexo order by cantidad desc', [inicio, fin])
    consulta_list = cursor.fetchall()
    
    workbook = xlsxwriter.Workbook(response, {'in_memory': True})
    
    worksheet = workbook.add_worksheet()
    
    bold = workbook.add_format({'bold': 1})
    
    chart1 = workbook.add_chart({'type': 'pie'})
    
    headings = ['Genero','Cantidad']
    i = 2;
    for consulta in consulta_list:
        worksheet.set_column('A:A', 30)
        worksheet.write('A' + str(i), consulta[0])
        worksheet.write('B' + str(i), consulta[1])
        i+=1
    
    worksheet.write_row('A1', headings, bold)
    i = i-1
    chart1.add_series({
    'name':       '=Sheet1!$B$1',
    'categories':       '=Sheet1!$A$2'+':'+'$A$'+str(i),
    'values':     '=Sheet1!$B$2'+':'+'$B$'+str(i),
    'data_labels': {'value': True,'percentage': True,'category': True},
    'gradient': {
    'type': 'radial'
    }
    })
    
    fechaInicio = datetime.strptime(inicio, '%Y-%m-%d').date()
    fechaFin = datetime.strptime(fin, '%Y-%m-%d').date()
    
    chart1.set_title({'name': 'Reporte de Consultas Generales Segun Genero del '+str(fechaInicio.day)+'/' + str(fechaInicio.month)+'/'+str(fechaInicio.year)+' al '+str(fechaFin.day)+'/'+str(fechaFin.month)+'/'+str(fechaFin.year)+' '})
    chart1.set_size({'width': 520, 'height': 370})
    chart1.set_x_axis({'name': 'Genero'})
    chart1.set_y_axis({'name': 'Cantidad'})
    chart1.set_table()
    
    worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
    workbook.close()
    return response

@login_required(login_url='logins')
@user_passes_test(is_usuario15)
def reporteConsultaTipoPacienteExcel(request,inicio,fin):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporteConsultaTipoPaciente.xlsx"'
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(p.estadoUes) as genero,count(*) as cantidad FROM datospersonalesapp_paciente as p inner join generalapp_consulta as g on g.cod_expediente_id = p.codigoPaciente inner join empleadosapp_doctor d on g.cod_doctor_id = d.codigoDoctor inner join empleadosapp_especialidad as esp on esp.id = d.especialidad_id and esp.especialidad="Medicina General" and g.fecha between %s and %s group by p.estadoUes order by cantidad desc', [inicio, fin])
    consulta_list = cursor.fetchall()
    
    workbook = xlsxwriter.Workbook(response, {'in_memory': True})
    
    worksheet = workbook.add_worksheet()
    
    bold = workbook.add_format({'bold': 1})
    
    chart1 = workbook.add_chart({'type': 'pie'})
    
    headings = ['Categoria','Cantidad']
    i = 2;
    for consulta in consulta_list:
        worksheet.set_column('A:A', 30)
        worksheet.write('A' + str(i), consulta[0])
        worksheet.write('B' + str(i), consulta[1])
        i+=1
    
    worksheet.write_row('A1', headings, bold)
    i = i-1
    chart1.add_series({
    'name':       '=Sheet1!$B$1',
    'categories':       '=Sheet1!$A$2'+':'+'$A$'+str(i),
    'values':     '=Sheet1!$B$2'+':'+'$B$'+str(i),
    'data_labels': {'value': True,'percentage': True,'category': True},
    'gradient': {
    'type': 'radial'
    }
    })
    
    fechaInicio = datetime.strptime(inicio, '%Y-%m-%d').date()
    fechaFin = datetime.strptime(fin, '%Y-%m-%d').date()
    
    chart1.set_title({'name': 'Reporte de Consultas Generales Segun Tipo de Paciente del '+str(fechaInicio.day)+'/' + str(fechaInicio.month)+'/'+str(fechaInicio.year)+' al '+str(fechaFin.day)+'/'+str(fechaFin.month)+'/'+str(fechaFin.year)+' '})
    chart1.set_size({'width': 520, 'height': 370})
    chart1.set_x_axis({'name': 'Categoria'})
    chart1.set_y_axis({'name': 'Cantidad'})
    chart1.set_table()
    
    worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
    workbook.close()
    return response

@login_required(login_url='logins')
@user_passes_test(is_jefenfermeria)
#En esta funcion se crea el archivo en formato Excel para el reporte de censo de activiades de enfermeria
def reporteCensoExcel(request,inicio,fin):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporteCensoActividad.xlsx"'
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(a.codActividad),a.nombreActividad,sum(c.cantidad) as cantidad FROM nuevoingresoapp_censo_enfermeria as c inner join nuevoingresoapp_actividad_enfermeria as a where c.actividad_id = a.codActividad and c.fechaActividad between %s and %s group by c.actividad_id order by cantidad desc', [inicio, fin])
    consulta_list = cursor.fetchall()
    
    workbook = xlsxwriter.Workbook(response, {'in_memory': True})
    
    worksheet = workbook.add_worksheet()
    
    bold = workbook.add_format({'bold': 1})
    
    chart1 = workbook.add_chart({'type': 'pie'})
    
    headings = ['Actividad','Cantidad']
    i = 2;
    for consulta in consulta_list:
        worksheet.set_column('A:A', 30)
        worksheet.write('A' + str(i), consulta[1])
        worksheet.write('B' + str(i), consulta[0])
        i+=1
    
    worksheet.write_row('A1', headings, bold)
    i = i-1
    chart1.add_series({
    'name':       '=Sheet1!$B$1',
    'categories':       '=Sheet1!$A$2'+':'+'$A$'+str(i),
    'values':     '=Sheet1!$B$2'+':'+'$B$'+str(i),
    'data_labels': {'value': True,'percentage': True,'category': True},
    'gradient': {
    'type': 'radial'
    }
    })
    
    fechaInicio = datetime.strptime(inicio, '%Y-%m-%d').date()
    fechaFin = datetime.strptime(fin, '%Y-%m-%d').date()
    
    chart1.set_title({'name': 'Reporte de Censo de Actividades de Enfermeria del '+str(fechaInicio.day)+'/' + str(fechaInicio.month)+'/'+str(fechaInicio.year)+' al '+str(fechaFin.day)+'/'+str(fechaFin.month)+'/'+str(fechaFin.year)+' '})
    chart1.set_size({'width': 1020, 'height': 876})
    chart1.set_x_axis({'name': 'Actividad'})
    chart1.set_y_axis({'name': 'Cantidad'})
    chart1.set_table()
    
    worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
    workbook.close()
    return response

@login_required(login_url='logins')
@user_passes_test(is_jefenfermeria)
#En esta funcion se crea el archivo en formato Excel para el reporte de pacientes atendidos por medico
def reportePacienteMedicoExcel(request,inicio,fin):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reportePacientesPorMedico.xlsx"'
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(g.cod_doctor_id) as doctor,CONCAT("Dr(a). ",e.nombrePrimero," ",e.apellidoPrimero) as nombre,count(*) as cantidad FROM empleadosapp_empleado as e inner join empleadosapp_doctor d on e.codigoEmpleado = d.codigoEmpleado_id inner join generalapp_consulta as g on g.cod_doctor_id = d.codigoDoctor and g.fecha between %s and %s group by g.cod_doctor_id order by cantidad desc', [inicio, fin])
    consulta_list = cursor.fetchall()
    
    workbook = xlsxwriter.Workbook(response, {'in_memory': True})
    
    worksheet = workbook.add_worksheet()
    
    bold = workbook.add_format({'bold': 1})
    
    chart1 = workbook.add_chart({'type': 'pie'})
    
    headings = ['Medico','Cantidad']
    i = 2;
    for consulta in consulta_list:
        worksheet.set_column('A:A', 30)
        worksheet.write('A' + str(i), consulta[1])
        worksheet.write('B' + str(i), consulta[0])
        i+=1
    
    worksheet.write_row('A1', headings, bold)
    i = i-1
    chart1.add_series({
    'name':       '=Sheet1!$B$1',
    'categories':       '=Sheet1!$A$2'+':'+'$A$'+str(i),
    'values':     '=Sheet1!$B$2'+':'+'$B$'+str(i),
    'data_labels': {'value': True,'percentage': True,'category': True},
    'gradient': {
    'type': 'radial'
    }
    })
    
    fechaInicio = datetime.strptime(inicio, '%Y-%m-%d').date()
    fechaFin = datetime.strptime(fin, '%Y-%m-%d').date()
    
    chart1.set_title({'name': 'Reporte de Pacientes Atendidos Por Medico del '+str(fechaInicio.day)+'/' + str(fechaInicio.month)+'/'+str(fechaInicio.year)+' al '+str(fechaFin.day)+'/'+str(fechaFin.month)+'/'+str(fechaFin.year)+' '})
    chart1.set_size({'width': 920, 'height': 770})
    chart1.set_x_axis({'name': 'Medico'})
    chart1.set_y_axis({'name': 'Cantidad'})
    chart1.set_table()
    
    worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
    workbook.close()
    return response

@login_required(login_url='logins')
@user_passes_test(is_jefenfermeria)
#En esta funcion se crea el archivo en formato Excel para el reporte de pacientes atendidos por medico
def reporteTipoConsultaExcel(request,inicio,fin):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporteTipoConsulta.xlsx"'
    cursor = connection.cursor()
    cursor.execute('SELECT g.tipo_consulta as tipo, count(*) as cantidad from generalapp_consulta as g where g.fecha between %s and %s group by g.tipo_consulta order by cantidad desc', [inicio, fin])
    consulta_list = cursor.fetchall()
    
    workbook = xlsxwriter.Workbook(response, {'in_memory': True})
    
    worksheet = workbook.add_worksheet()
    
    bold = workbook.add_format({'bold': 1})
    
    chart1 = workbook.add_chart({'type': 'pie'})
    
    headings = ['Tipo de Consulta','Cantidad']
    i = 2;
    for consulta in consulta_list:
        worksheet.set_column('A:A', 30)
        worksheet.write('A' + str(i), consulta[0])
        worksheet.write('B' + str(i), consulta[1])
        i+=1
    
    worksheet.write_row('A1', headings, bold)
    i = i-1
    chart1.add_series({
    'name':       '=Sheet1!$B$1',
    'categories':       '=Sheet1!$A$2'+':'+'$A$'+str(i),
    'values':     '=Sheet1!$B$2'+':'+'$B$'+str(i),
    'data_labels': {'value': True,'percentage': True,'category': True},
    'gradient': {
    'type': 'radial'
    }
    })
    
    fechaInicio = datetime.strptime(inicio, '%Y-%m-%d').date()
    fechaFin = datetime.strptime(fin, '%Y-%m-%d').date()
    
    chart1.set_title({'name': 'Reporte de Primera y Consulta Subsecuentes del '+str(fechaInicio.day)+'/' + str(fechaInicio.month)+'/'+str(fechaInicio.year)+' al '+str(fechaFin.day)+'/'+str(fechaFin.month)+'/'+str(fechaFin.year)+' '})
    chart1.set_size({'width': 520, 'height': 370})
    chart1.set_x_axis({'name': 'Tipo de Consulta'})
    chart1.set_y_axis({'name': 'Cantidad'})
    chart1.set_table()
    
    worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
    workbook.close()
    return response

@login_required(login_url='logins')
@user_passes_test(is_jefenfermeria)
#En esta funcion se crea el archivo en formato Excel para el reporte de morbilidades de antiguo y nuevo ingreso
def reporteMorbilidadExcel(request,inicio,fin):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporteMorbilidad.xlsx"'
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor1.execute('SELECT distinct(g.diagnostico_principal) as morbilidad,count(*) as cantidad FROM generalapp_consulta as g inner join datospersonalesapp_paciente as p on g.cod_expediente_id = p.codigoPaciente and g.fecha between %s and %s group by g.diagnostico_principal order by cantidad desc limit 0,10', [inicio, fin])
    cursor2.execute('SELECT distinct(g.diagnostico_principal) as morbilidad,count(*) as cantidad FROM generalapp_consulta as g inner join nuevoingresoapp_expediente_provisional as p on g.cod_expediente_id = p.Cod_Expediente_Provisional and g.fecha between %s and %s group by g.diagnostico_principal order by cantidad desc limit 0,10', [inicio, fin])
    antiguo_list = cursor1.fetchall()
    nuevo_list = cursor2.fetchall()
    
    workbook = xlsxwriter.Workbook(response, {'in_memory': True})
    
    worksheet = workbook.add_worksheet()
    
    bold = workbook.add_format({'bold': 1})
    
    chart1 = workbook.add_chart({'type': 'pie'})
    chart2 = workbook.add_chart({'type': 'pie'})
    
    headings = ['Morbilidad','Cantidad']
    i = 2;
    for consulta in antiguo_list:
        worksheet.set_column('A:A', 30)
        worksheet.write('A' + str(i), consulta[0])
        worksheet.write('B' + str(i), consulta[1])
        i+=1
    
    j = 37
    for consulta in nuevo_list:
        worksheet.set_column('A:A', 30)
        worksheet.write('A' + str(j), consulta[0])
        worksheet.write('B' + str(j), consulta[1])
        j+=1
    
    worksheet.write_row('A1', headings, bold)
    worksheet.write_row('A36', headings, bold)
    
    i = i-1
    j = j-1
    
    chart1.add_series({
    'name':       '=Sheet1!$B$1',
    'categories':       '=Sheet1!$A$2'+':'+'$A$'+str(i),
    'values':     '=Sheet1!$B$2'+':'+'$B$'+str(i),
    'data_labels': {'value': True,'percentage': True,'category': True},
    'gradient': {
    'type': 'radial'
    }
    })

    chart2.add_series({
    'name':       '=Sheet1!$B$37',
    'categories':       '=Sheet1!$A$37'+':'+'$A$'+str(j),
    'values':     '=Sheet1!$B$37'+':'+'$B$'+str(j),
    'data_labels': {'value': True,'percentage': True,'category': True},
    'gradient': {
    'type': 'radial'
    }
    })
    
    fechaInicio = datetime.strptime(inicio, '%Y-%m-%d').date()
    fechaFin = datetime.strptime(fin, '%Y-%m-%d').date()
    
    chart1.set_title({'name': 'Reporte de Morbilidad Antiguo Ingreso del '+str(fechaInicio.day)+'/' + str(fechaInicio.month)+'/'+str(fechaInicio.year)+' al '+str(fechaFin.day)+'/'+str(fechaFin.month)+'/'+str(fechaFin.year)+' '})
    chart1.set_size({'width': 770, 'height': 620})
    chart1.set_x_axis({'name': 'Morbilidad'})
    chart1.set_y_axis({'name': 'Cantidad'})
    chart1.set_table()

    chart2.set_title({'name': 'Reporte de Morbilidad Nuevo Ingreso del '+str(fechaInicio.day)+'/' + str(fechaInicio.month)+'/'+str(fechaInicio.year)+' al '+str(fechaFin.day)+'/'+str(fechaFin.month)+'/'+str(fechaFin.year)+' '})
    chart2.set_size({'width': 770, 'height': 620})
    chart2.set_x_axis({'name': 'Morbilidad'})
    chart2.set_y_axis({'name': 'Cantidad'})
    chart2.set_table()
    
    worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
    worksheet.insert_chart('D37', chart2, {'x_offset': 25, 'y_offset': 10})
    
    workbook.close()
    return response

@login_required(login_url='logins')
@user_passes_test(is_jefenfermeria)
#En esta funcion se crea el archivo en formato Excel para el reporte de consultas por especialidad de antiguo y nuevo ingreso
def reporteConsultaEspecialidadExcel(request,inicio,fin):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporteConsultaPorEspecialidad.xlsx"'
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor1.execute('SELECT distinct(g.cod_doctor_id) as doctor,esp.especialidad as especialidad,count(*) as cantidad FROM empleadosapp_especialidad as esp inner join empleadosapp_doctor d on esp.id = d.especialidad_id inner join generalapp_consulta as g on g.cod_doctor_id = d.codigoDoctor and g.fecha between %s and %s WHERE g.cod_expediente_id LIKE "%%-%%"  group by d.especialidad_id order by cantidad desc', [inicio, fin])
    cursor2.execute('SELECT distinct(g.cod_doctor_id) as doctor,esp.especialidad as especialidad,count(*) as cantidad FROM empleadosapp_especialidad as esp inner join empleadosapp_doctor d on esp.id = d.especialidad_id inner join generalapp_consulta as g on g.cod_doctor_id = d.codigoDoctor and g.fecha between %s and %s WHERE g.cod_expediente_id NOT LIKE "%%-%%"  group by d.especialidad_id order by cantidad desc', [inicio, fin])
    antiguo_list = cursor1.fetchall()
    nuevo_list = cursor2.fetchall()
    
    workbook = xlsxwriter.Workbook(response, {'in_memory': True})
    
    worksheet = workbook.add_worksheet()
    
    bold = workbook.add_format({'bold': 1})
    
    chart1 = workbook.add_chart({'type': 'pie'})
    chart2 = workbook.add_chart({'type': 'pie'})
    
    headings = ['Especialidad','Cantidad']
    i = 2;
    for consulta in antiguo_list:
        worksheet.set_column('A:A', 30)
        worksheet.write('A' + str(i), consulta[1])
        worksheet.write('B' + str(i), consulta[2])
        i+=1
    
    j = 37
    for consulta in nuevo_list:
        worksheet.set_column('A:A', 30)
        worksheet.write('A' + str(j), consulta[1])
        worksheet.write('B' + str(j), consulta[2])
        j+=1
    
    worksheet.write_row('A1', headings, bold)
    worksheet.write_row('A36', headings, bold)
    
    i = i-1
    j = j-1
    
    chart1.add_series({
    'name':       '=Sheet1!$B$1',
    'categories':       '=Sheet1!$A$2'+':'+'$A$'+str(i),
    'values':     '=Sheet1!$B$2'+':'+'$B$'+str(i),
    'data_labels': {'value': True,'percentage': True,'category': True},
    'gradient': {
    'type': 'radial'
    }
    })

    chart2.add_series({
    'name':       '=Sheet1!$B$37',
    'categories':       '=Sheet1!$A$37'+':'+'$A$'+str(j),
    'values':     '=Sheet1!$B$37'+':'+'$B$'+str(j),
    'data_labels': {'value': True,'percentage': True,'category': True},
    'gradient': {
    'type': 'radial'
    }
    })
    
    fechaInicio = datetime.strptime(inicio, '%Y-%m-%d').date()
    fechaFin = datetime.strptime(fin, '%Y-%m-%d').date()
    
    chart1.set_title({'name': 'Reporte de Consultas Por Especialidad Antiguo Ingreso del '+str(fechaInicio.day)+'/' + str(fechaInicio.month)+'/'+str(fechaInicio.year)+' al '+str(fechaFin.day)+'/'+str(fechaFin.month)+'/'+str(fechaFin.year)+' '})
    chart1.set_size({'width': 770, 'height': 620})
    chart1.set_x_axis({'name': 'Especialidad'})
    chart1.set_y_axis({'name': 'Cantidad'})
    chart1.set_table()

    chart2.set_title({'name': 'Reporte de Consultas Por Especialidad Nuevo Ingreso del '+str(fechaInicio.day)+'/' + str(fechaInicio.month)+'/'+str(fechaInicio.year)+' al '+str(fechaFin.day)+'/'+str(fechaFin.month)+'/'+str(fechaFin.year)+' '})
    chart2.set_size({'width': 770, 'height': 620})
    chart2.set_x_axis({'name': 'Especialidad'})
    chart2.set_y_axis({'name': 'Cantidad'})
    chart2.set_table()
    
    worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
    worksheet.insert_chart('D37', chart2, {'x_offset': 25, 'y_offset': 10})
    
    workbook.close()
    return response

@login_required(login_url='logins')
@user_passes_test(is_jefenfermeria)
#En esta funcion se crea el archivo en formato Excel para el reporte de referencias internas y externas de los pacientes de antiguo ingreso
def reporteReferenciasExcel(request,inicio,fin):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporteReferencias.xlsx"'
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor1.execute('SELECT r.referido_a as referencia, count(*) as cantidad from generalapp_referenciainterna as r where r.referido_a <> "''" and r.fecha between %s and %s group by r.referido_a order by cantidad desc', [inicio, fin])
    cursor2.execute('SELECT r.referido_a as referencia, count(*) as cantidad from generalapp_referenciaexterna as r where r.referido_a <> "''" and r.fecha between %s and %s group by r.referido_a order by cantidad desc', [inicio, fin])
    antiguo_list = cursor1.fetchall()
    nuevo_list = cursor2.fetchall()
    
    workbook = xlsxwriter.Workbook(response, {'in_memory': True})
    
    worksheet = workbook.add_worksheet()
    
    bold = workbook.add_format({'bold': 1})
    
    chart1 = workbook.add_chart({'type': 'pie'})
    chart2 = workbook.add_chart({'type': 'pie'})
    
    headings = ['Referencia','Cantidad']
    i = 2;
    for consulta in antiguo_list:
        worksheet.set_column('A:A', 30)
        worksheet.write('A' + str(i), consulta[0])
        worksheet.write('B' + str(i), consulta[1])
        i+=1
    
    j = 37
    for consulta in nuevo_list:
        worksheet.set_column('A:A', 30)
        worksheet.write('A' + str(j), consulta[0])
        worksheet.write('B' + str(j), consulta[1])
        j+=1
    
    worksheet.write_row('A1', headings, bold)
    worksheet.write_row('A36', headings, bold)
    
    i = i-1
    j = j-1
    
    chart1.add_series({
    'name':       '=Sheet1!$B$1',
    'categories':       '=Sheet1!$A$2'+':'+'$A$'+str(i),
    'values':     '=Sheet1!$B$2'+':'+'$B$'+str(i),
    'data_labels': {'value': True,'percentage': True,'category': True},
    'gradient': {
    'type': 'radial'
    }
    })

    chart2.add_series({
    'name':       '=Sheet1!$B$37',
    'categories':       '=Sheet1!$A$37'+':'+'$A$'+str(j),
    'values':     '=Sheet1!$B$37'+':'+'$B$'+str(j),
    'data_labels': {'value': True,'percentage': True,'category': True},
    'gradient': {
    'type': 'radial'
    }
    })
    
    fechaInicio = datetime.strptime(inicio, '%Y-%m-%d').date()
    fechaFin = datetime.strptime(fin, '%Y-%m-%d').date()
    
    chart1.set_title({'name': 'Reporte de Referencias Internas del '+str(fechaInicio.day)+'/' + str(fechaInicio.month)+'/'+str(fechaInicio.year)+' al '+str(fechaFin.day)+'/'+str(fechaFin.month)+'/'+str(fechaFin.year)+' '})
    chart1.set_size({'width': 770, 'height': 620})
    chart1.set_x_axis({'name': 'Referencia'})
    chart1.set_y_axis({'name': 'Cantidad'})
    chart1.set_table()

    chart2.set_title({'name': 'Reporte de Referencias Externas del '+str(fechaInicio.day)+'/' + str(fechaInicio.month)+'/'+str(fechaInicio.year)+' al '+str(fechaFin.day)+'/'+str(fechaFin.month)+'/'+str(fechaFin.year)+' '})
    chart2.set_size({'width': 770, 'height': 620})
    chart2.set_x_axis({'name': 'Referencia'})
    chart2.set_y_axis({'name': 'Cantidad'})
    chart2.set_table()
    
    worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
    worksheet.insert_chart('D37', chart2, {'x_offset': 25, 'y_offset': 10})
    
    workbook.close()
    return response

def export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'First name', 'Last name', 'Email address'])

    users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for user in users:
        writer.writerow(user)

    return response





#Muestra el informe de actividades de enfermeria filtrado por rangos de fechas y agrupados por actividad, ordenados descendentemente por la cantidad de actividad
@login_required(login_url='logins')
@user_passes_test(is_usuario4)
def reporte_censo(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor = connection.cursor()
    cursor.execute('SELECT distinct(a.codActividad),a.nombreActividad,sum(c.cantidad) as cantidad FROM nuevoingresoapp_censo_enfermeria as c inner join nuevoingresoapp_actividad_enfermeria as a where c.actividad_id = a.codActividad and c.fechaActividad between %s and %s group by c.actividad_id order by cantidad desc', [fechaInicio, fechaFin])
    censo_list = cursor.fetchall()
    return render(request,"reportesapp/reporte_censo_actividades.html",{'censo_list':censo_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})





@login_required(login_url='logins')
@user_passes_test(is_usuario4)
def reporte_consultas_especialidad(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor1 = connection.cursor()
    cursor1.execute('SELECT distinct(g.cod_doctor_id) as doctor,esp.especialidad as especialidad,count(*) as cantidad FROM empleadosapp_especialidad as esp inner join empleadosapp_doctor d on esp.id = d.especialidad_id inner join generalapp_consulta as g on g.cod_doctor_id = d.codigoDoctor and g.fecha between %s and %s WHERE g.cod_expediente_id LIKE "%%-%%"  group by d.especialidad_id order by cantidad desc', [fechaInicio, fechaFin])
    antiguo_list = cursor1.fetchall()
    
    cursor2 = connection.cursor()
    cursor2.execute('SELECT distinct(g.cod_doctor_id) as doctor,esp.especialidad as especialidad,count(*) as cantidad FROM empleadosapp_especialidad as esp inner join empleadosapp_doctor d on esp.id = d.especialidad_id inner join generalapp_consulta as g on g.cod_doctor_id = d.codigoDoctor and g.fecha between %s and %s WHERE g.cod_expediente_id NOT LIKE "%%-%%"  group by d.especialidad_id order by cantidad desc', [fechaInicio, fechaFin])
    nuevo_list = cursor2.fetchall()
    return render(request,"reportesapp/reporte_consulta_especialidad.html",{'antiguo_list':antiguo_list,'nuevo_list':nuevo_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})






#Muestra el informe de las 10 morbilidades de mayor ocurrecia en pacientes de antiguo y nuevo ingreso
@login_required(login_url='logins')
@user_passes_test(is_usuario4)
def reporte_morbilidad(request):
    fechaInicio=request.POST.get('fechaInicio')
    fechaFin=request.POST.get('fechaFin')
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor1.execute('SELECT distinct(g.diagnostico_principal) as morbilidad,count(*) as cantidad FROM generalapp_consulta as g inner join datospersonalesapp_paciente as p on g.cod_expediente_id = p.codigoPaciente and g.fecha between %s and %s group by g.diagnostico_principal order by cantidad desc limit 0,10', [fechaInicio, fechaFin])
    cursor2.execute('SELECT distinct(g.diagnostico_principal) as morbilidad,count(*) as cantidad FROM generalapp_consulta as g inner join nuevoingresoapp_expediente_provisional as p on g.cod_expediente_id = p.Cod_Expediente_Provisional and g.fecha between %s and %s group by g.diagnostico_principal order by cantidad desc limit 0,10', [fechaInicio, fechaFin])
    morbilidadAntiguo_list = cursor1.fetchall()
    morbilidadNuevo_list = cursor2.fetchall()
    return render(request,"reportesapp/reporte_morbilidad.html",{'morbilidadAntiguo_list':morbilidadAntiguo_list,'morbilidadNuevo_list':morbilidadNuevo_list,'fechaInicio':fechaInicio,'fechaFin':fechaFin})