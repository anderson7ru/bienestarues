from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.personalpaciente_list,name='datospersonales-list',),
    url(r'^busqueda/$',views.personalpaciente_busqueda,name='datospersonales-busqueda',),
    url(r'^nuevo/$',views.personalpaciente_nuevo,name='datospersonales-new',),
    url(r'^(?P<pk>[0-9]+\-[0-9]+)/$',views.personalpaciente_detalle,name='datospersonales-view',),
    url(r'^(?P<pk>[0-9]+\-[0-9]+)/editar/$',views.personalpaciente_modificar,name='datospersonales-update',),
    url(r'^(?P<pk>[0-9]+\-[0-9]+)/eliminar/$',views.personalpaciente_eliminar,name='datospersonales-delete',),
    url(r'^(?P<pk>[0-9]+\-[0-9]+)/restaurar/$',views.personalpaciente_restaurar,name='datospersonales-restaurar',),
    url(r'^(?P<pk>[0-9]+\-[0-9]+)/pdf/$',views.personalpaciente_file,name='datospersonales-file',),
    url(r'^eliminados/$',views.personalinactivo_list,name='datospersonales-eliminadoslist',),
    url(r'^(?P<nit>[0-9]+\-[0-9]+\-[0-9]+\-[0-9]+)/provisionalnuevo/$',views.personalpacienteprovisional_nuevo,name='datospersonalesprovisional-new')
]
