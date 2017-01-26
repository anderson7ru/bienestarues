from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^listadoColaEnfermeria/ColaEnfermeria$',views.cola_enfermeria_list,name='cola_enfermeria-list',),
    url(r'^listadoColaConsulta/ColaConsulta$',views.cola_consulta_list,name='cola_consulta-list',),
    url(r'^(?P<pk>[0-9]+\-[0-9]+)/nuevo/$',views.cola_enfermeria_nuevo,name='cola_enfermeria-new',),
    url(r'^(?P<pk>[0-9]+\-[0-9]+)/borrar/$',views.cola_enfermeria_borrar,name='cola_enfermeria-delete',),
]