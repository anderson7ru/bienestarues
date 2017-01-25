from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.empleados_list,name='empleados-list',),
    url(r'^nuevo/$',views.empleados_nuevo,name='empleados-new',),
    url(r'^(?P<pk>[0-9]+)/$',views.empleados_detalle,name='empleados-view',),
    url(r'^(?P<pk>[0-9]+)/editar/$',views.empleados_modificar,name='empleados-update',),
    url(r'^(?P<pk>[0-9]+)/eliminar/$',views.empleados_eliminar,name='empleados-delete',),
    url(r'^(?P<pk>[0-9]+)/restaurar/$',views.empleados_restaurar,name='empleados-restaurar',),
    url(r'^nuevo/(?P<pk>[0-9]+)/$',views.doctor_nuevo,name='doctor-new',),
    url(r'^doctor/(?P<pk>[0-9]+)/$',views.doctor_detalle,name='doctor-view',),
    url(r'^doctor/(?P<pk>[0-9]+)/editar/$',views.doctor_modificar,name='doctor-update',),
    url(r'^doctor/(?P<pk>[0-9]+)/eliminar/$',views.doctor_eliminar,name='doctor-delete',),
    url(r'^doctor/(?P<pk>[0-9]+)/restaurar/$',views.doctor_restaurar,name='doctor-restaurar',),
    url(r'^nuevo/lab/(?P<pk>[0-9]+)/$',views.laboratorista_nuevo,name='laboratorista-new',),
    url(r'^lab/(?P<pk>[0-9]+)/editar/$',views.laboratorista_modificar,name='laboratorista-update',),
    #url(r'^lab/(?P<pk>[0-9]+)/eliminar/$',views.laboratorista_eliminar,name='laboratorista-delete',),
    #url(r'^lab/(?P<pk>[0-9]+)/restaurar/$',views.laboratorista_restaurar,name='laboratorista-restaurar',),
    url(r'^eliminados/$',views.empleadoinactivo_list,name='empleados-eliminadoslist',),    
]