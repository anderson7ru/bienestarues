from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
import xlsxwriter
#import StringIO
import csv
import datetime
from django.db import connection


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
    
    headings = ['Respuesta','Cantidad']
    i = 2;
    for consulta in consulta_list:
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
    
    chart1.set_title({'name': 'Reporte de Visto Bueno'})
    chart1.set_x_axis({'name': 'Respuesta'})
    chart1.set_y_axis({'name': '# de Pacientes'})
    chart1.set_table()
    
    worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
    workbook.close()
    return response

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
        worksheet.write('A' + str(i), consulta[1])
        worksheet.write('B' + str(i), consulta[0])
        i+=1
    
    worksheet.write_row('A1', headings, bold)
    i = i-1
    chart1.add_series({
    'name':       '=Sheet1!$B$1',
    'categories':       '=Sheet1!$A$2'+':'+'$A$'+str(i),
    'values':     '=Sheet1!$B$2'+':'+'$B$'+str(i),
    'data_labels': {'value': True,'percentage': True,'category': False},
    'gradient': {
    'type': 'radial'
    }
    })
    
    chart1.set_title({'name': 'Reporte de Censo de Actividades de Enfermeria'})
    chart1.set_x_axis({'name': 'Actividad'})
    chart1.set_y_axis({'name': '# de Activiades'})
    chart1.set_table()
    
    worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
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