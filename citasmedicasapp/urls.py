from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.doctor_list,name='doctor-list',), 
    url(r'^doctor/(?P<pk>[0-9]+)/$',views.doctorcita_list,name='doctorcita_list'),
    url(r'^calendario/(?P<pk>[0-9]+)/(?P<anio>[0-9]+)/(?P<mes>[0-9]+)/$',views.calendario,name='calendario'),
    url(r'^doctor_canceladas/(?P<pk>[0-9]+)/$',views.doctorcancel_list,name='doctorcancel_list'),
    url(r'^cita/(?P<pk>[0-9]+)/(?P<dia>[0-9]+)-(?P<mes>[0-9]+)-(?P<anio>[0-9]+)/$',views.citasmedicas_nuevo,name='cita_new'),
    url(r'^cancelacion/(?P<pk>[0-9]+)/$',views.cancelacion_nuevo,name='cancelacion_new'),
    url(r'^paciente/$',views.paciente_list,name='paciente_list'),
    url(r'^paciente/(?P<pk>[0-9]+\-[0-9]+)/$',views.pacientecita_list,name='pacientecita_list'),
]