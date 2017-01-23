from django.conf.urls import url

from . import views

urlpatterns = [
    #Para reporte en formato Excel de los pacientes que solicitaron visto bueno
    url(r'^(?P<inicio>[0-9]+\-[0-9]+\-[0-9]+)/(?P<fin>[0-9]+\-[0-9]+\-[0-9]+)/vistoBuenoExcel/$', views.vistoBuenoExcel, name='vistoBuenoExcel-new'),
    #Para reporte en formato Excel de las actividades de enfermeria
    url(r'^(?P<inicio>[0-9]+\-[0-9]+\-[0-9]+)/(?P<fin>[0-9]+\-[0-9]+\-[0-9]+)/censoEnfermeriaExcel/$', views.reporteCensoExcel, name='censoActividadExcel-new'),
    #Para reporte en formato Excel de las morbilidades de pacientes de nuevo y antiguo ingreso
    url(r'^(?P<inicio>[0-9]+\-[0-9]+\-[0-9]+)/(?P<fin>[0-9]+\-[0-9]+\-[0-9]+)/morbilidadExcel/$', views.reporteMorbilidadExcel, name='morbilidadExcel-new'),
    #Para reporte en formato Excel de los pacientes atendidos por medico
    url(r'^(?P<inicio>[0-9]+\-[0-9]+\-[0-9]+)/(?P<fin>[0-9]+\-[0-9]+\-[0-9]+)/pacientesPorMedicoExcel/$', views.reportePacienteMedicoExcel, name='pacientesMedicoExcel-new'),
    #Para reporte en formato Excel de los pacientes atendidos por especialidad
    url(r'^(?P<inicio>[0-9]+\-[0-9]+\-[0-9]+)/(?P<fin>[0-9]+\-[0-9]+\-[0-9]+)/pacientesPorEspecialidadExcel/$', views.reporteConsultaEspecialidadExcel, name='pacientesEspecialidadExcel-new'),
    #Para reporte en formato Excel de las referencias internas y externas
    url(r'^(?P<inicio>[0-9]+\-[0-9]+\-[0-9]+)/(?P<fin>[0-9]+\-[0-9]+\-[0-9]+)/pacientesReferenciasExcel/$', views.reporteReferenciasExcel, name='referenciasExcel-new'),
    #Para reporte en formato Excel de primeras y consultas subsecuentes
    url(r'^(?P<inicio>[0-9]+\-[0-9]+\-[0-9]+)/(?P<fin>[0-9]+\-[0-9]+\-[0-9]+)/pacientesTipoConsultaExcel/$', views.reporteTipoConsultaExcel, name='tipoConsultaExcel-new'),
    #Para reporte en formato Excel de consultas generales segun procedencia
    url(r'^(?P<inicio>[0-9]+\-[0-9]+\-[0-9]+)/(?P<fin>[0-9]+\-[0-9]+\-[0-9]+)/consultasProcedenciaExcel/$', views.reporteConsultaProcedenciaExcel, name='consultaProcedenciaExcel-new'),
    #Para reporte en formato Excel de consultas generales segun genero
    url(r'^(?P<inicio>[0-9]+\-[0-9]+\-[0-9]+)/(?P<fin>[0-9]+\-[0-9]+\-[0-9]+)/consultasGeneroExcel/$', views.reporteConsultaGeneroExcel, name='consultaGeneroExcel-new'),
    #Para reporte en formato Excel de consultas generales segun tipo de paciente
    url(r'^(?P<inicio>[0-9]+\-[0-9]+\-[0-9]+)/(?P<fin>[0-9]+\-[0-9]+\-[0-9]+)/consultasTipoPacienteExcel/$', views.reporteConsultaTipoPacienteExcel, name='consultaTipoPacienteExcel-new'),
    url(r'^export/csv/$', views.export, name='export_excel'),
]