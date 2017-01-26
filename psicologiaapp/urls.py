from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.psicologia_lista,name="psicologia-list"),
    url(r'^crear/(?P<pk>[0-9]+\-[0-9]+)/$',views.psicologia_nuevo,name='psicologia-new'),
    url(r'^consultar/(?P<paciente>[0-9]+\-[0-9]+)/$',views.psicologia_consulta,name='psicologia-view'),
    url(r'^modificar/(?P<paciente>[0-9]+\-[0-9]+)/$',views.psicologia_actualizar,name='psicologia-update'),
    url(r'^procesoterapeutico/crear/(?P<paciente>[0-9]+\-[0-9]+)/$',views.procesoterapeutico_nuevo,name='procesoterapeutico-new'),
    url(r'^procesoterapeutico/consultar/(?P<paciente>[0-9]+\-[0-9]+)/$',views.procesoterapeutico_consulta,name='procesoterapeutico-view'),
    url(r'^procesoterapeutico/modificar/(?P<paciente>[0-9]+\-[0-9]+)/$',views.procesoterapeutico_actualizar,name='procesoterapeutico-update'),
    url(r'^registroavance/crear/(?P<proceso>[0-9]+)/$',views.registroavance_nuevo,name='registroavance-new'),
    url(r'^registroavance/consultar/(?P<proceso>[0-9]+)/$',views.registroavance_consulta,name='registroavance-view'),
    url(r'^registroavance/modificar(?P<proceso>[0-9]+)/$',views.registroavance_actualizar,name='registroavance-update'),
    url(r'^expedientepdf/(?P<paciente>[0-9]+\-[0-9]+)/$',views.expedientePsicologiaPDF,name='psicologiapdf-create'),
    url(r'^procesoTerapeuticopdf/(?P<paciente>[0-9]+\-[0-9]+)/$',views.procesoTerapeuticoPDF,name='procesoterapeuticopdf-create'),
    url(r'^registroAvancepdf/(?P<proceso>[0-9]+)/$',views.registroAvancePDF,name='registroavancepdf-create')
]