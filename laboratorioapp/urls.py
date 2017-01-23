from django.conf.urls import url

from . import views

urlpatterns = [
    #Para laboratorio clinico
    url(r'^listadoExpedienteLaboratorio/$', views.laboratorio_list, name='laboratorio-list',),
    url(r'^(?P<pk>[0-9]+\-[0-9]+)/hematologia_nuevo/$', views.hematologia_nuevo, name='hematologia-new',),
    url(r'^(?P<pk>[0-9]+\-[0-9]+)/examen_heces_nuevo/$', views.examen_heces_nuevo, name='examen_heces-new',),
    url(r'^(?P<pk>[0-9]+\-[0-9]+)/examen_orina_nuevo/$', views.examen_orina_nuevo, name='examen_orina-new',),
    url(r'^(?P<pk>[0-9]+\-[0-9]+)/quimica_sanguinea_nuevo/$', views.quimica_sanguinea_nuevo, name='quimica_sanguinea-new',),
    url(r'^(?P<pk>[0-9]+\-[0-9]+)/pruebas_especiales_nuevo/$', views.pruebas_especiales_nuevo, name='pruebas_especiales-new',),
    url(r'^(?P<pk>[0-9]+\-[0-9]+)/examen_nuevo_ingreso_nuevo/$', views.examen_nuevo_ingreso_nuevo, name='nuevo_ingreso-new',),
    url(r'^listadoHematologia/$', views.hematologia_list, name='hematologia-list',),
    url(r'^listadoExamenHeces/$', views.examen_heces_list, name='examen_heces-list',),
    url(r'^listadoExamenOrina/$', views.examen_orina_list, name='examen_orina-list',),
    url(r'^listadoExamenGeneral/$', views.examen_general_list, name='examen_general-list',),
    url(r'^listadoExamenQuimica/$', views.examen_quimica_list, name='examen_quimica-list',),
    url(r'^listadoExamenEspeciales/$', views.examen_especiales_list, name='examen_especiales-list',),
    url(r'^examenHematologia/(?P<pk>[0-9]+)/$', views.hematologia_detalle, name='hematologia-view'),
    url(r'^examenHeces/(?P<pk>[0-9]+)/$', views.examen_heces_detalle, name='examen_heces-view'),
    url(r'^examenOrina/(?P<pk>[0-9]+)/$', views.examen_orina_detalle, name='examen_orina-view'),
    url(r'^examenGeneral/(?P<pk>[0-9]+)/$', views.examen_general_detalle, name='examen_general-view'),
    url(r'^examenQuimica/(?P<pk>[0-9]+)/$', views.examen_quimica_detalle, name='examen_quimica-view'),
    url(r'^examenEspeciales/(?P<pk>[0-9]+)/$', views.examen_especiales_detalle, name='examen_especiales-view'),
    url(r'^abrirArchivoHeces/(?P<pk>[0-9]+)/$', views.abrir_archivo_heces, name='abrir_archivo_heces-view'),
    url(r'^abrirArchivoHematologia/(?P<pk>[0-9]+)/$', views.abrir_archivo_hematologia, name='abrir_archivo_hematologia-view'),
    url(r'^abrirArchivoOrina/(?P<pk>[0-9]+)/$', views.abrir_archivo_orina, name='abrir_archivo_orina-view'),
    url(r'^abrirArchivoGeneral/(?P<pk>[0-9]+)/$', views.abrir_archivo_general, name='abrir_archivo_general-view'),
    url(r'^abrirArchivoQuimica/(?P<pk>[0-9]+)/$', views.abrir_archivo_quimica, name='abrir_archivo_quimica-view'),
    url(r'^abrirArchivoEspeciales/(?P<pk>[0-9]+)/$', views.abrir_archivo_especiales, name='abrir_archivo_especiales-view'),
    url(r'^hematologiapdf/(?P<pk>[0-9]+)/$',views.hematologiaPDF, name="examen_hematologia_pdf"),
]