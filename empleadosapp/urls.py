from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.empleados_list,name='empleados-list',),
    url(r'^nuevo/$',views.empleados_nuevo,name='empleados-new',),
    url(r'^(?P<pk>[0-9]+)/$',views.empleados_detalle,name='empleados-view',),
    url(r'^(?P<pk>[0-9]+)/editar/$',views.empleados_modificar,name='empleados-update',),
    url(r'^nuevo/(?P<pk>[0-9]+)/$',views.doctor_nuevo,name='doctor-new',),
    url(r'^doctor/(?P<pk>[0-9]+)/$',views.doctor_detalle,name='doctor-view',),
    url(r'^doctor/(?P<pk>[0-9]+)/editar/$',views.doctor_modificar,name='doctor-update',),
]