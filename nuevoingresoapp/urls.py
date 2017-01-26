from django.conf.urls import url

from . import views

urlpatterns = [
    #Para el expediente provisional de los alumnos de nuevo ingreso
    url(r'^nuevoExpedienteProvisional/$', views.expedienteprovisional_nuevo, name='expedienteprovisonal-new'),
    url(r'^nuevaActividad/$', views.actividad_nuevo, name='actividad-new'),
    url(r'^nuevaCenso/$', views.censo_nuevo, name='censo-new'),
    url(r'^listadoExpedienteProvisional/$', views.Expediente_Provisional_list, name='expedienteprovisonal-list'),
    url(r'^listadoActividad/$', views.actividad_list, name='actividades-list'),
    url(r'^listadoCenso/$', views.censo_list, name='censo-list'),
    url(r'^reporteCenso/$', views.reporte_censo, name='censo-reporte'),
    url(r'^reporteConsultaGeneralProcedencia/$', views.reporte_consulta_general_procedencia, name='consulta-general-procedencia-reporte'),
    url(r'^reporteConsultaGeneralGenero/$', views.reporte_consulta_general_genero, name='consulta-general-genero-reporte'),
    url(r'^reporteConsultaGeneralTipoPaciente/$', views.reporte_consulta_general_tipo_paciente, name='consulta-general-paciente-reporte'),
    url(r'^reporteMorbilidadAntiguoIngreso/$', views.reporte_morbilidad_antiguo_ingreso, name='morbilidad-antiguo-ingreso-reporte'),
    url(r'^reporteMorbilidadNuevoIngreso/$', views.reporte_morbilidad_nuevo_ingreso, name='morbilidad-nuevo-ingreso-reporte'),
    url(r'^reporteMorbilidad/$', views.reporte_morbilidad, name='morbilidad-reporte'),
    url(r'^reporteConsultaEspecialidad/$', views.reporte_consultas_especialidad, name='consulta_especialidad-reporte'),
    url(r'^reportePacientesPorMedico/$', views.reporte_pacientes_por_medico, name='pacientes_por_medico-reporte'),
    url(r'^reporteReferencias/$', views.reporte_referencias, name='referencias-reporte'),
    url(r'^reporteTipoConsulta/$', views.reporte_tipo_consulta, name='tipo_consulta-reporte'),
    url(r'^reporteVistoBueno/$', views.reporte_visto_bueno, name='visto_bueno-reporte'),
    url(r'^expedienteProvisional/(?P<pk>[0-9]+)/$', views.expedienteprovisional_detalle, name='expedienteprovisonal-view'),
    url(r'^certificado_salud/(?P<pk>[0-9]+)/nuevo$', views.certificado_salud_nuevo, name='certificado_salud-new'),
    url(r'^certificado_salud/(?P<pk>[0-9]+)/$', views.certificado_salud_ver, name='certificado_salud-view'),
    url(r'^expedienteProvisionalEditar/(?P<pk>[0-9]+)/$', views.expedienteprov_modificar, name='expedienteprovisonal-editar'),
    url(r'^expedienteProvisionalEliminar/(?P<pk>[0-9]+)/$', views.expedienteprovisional_eliminar, name='expedienteprovisonal-eliminar'),
]