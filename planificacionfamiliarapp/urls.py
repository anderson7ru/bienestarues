from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.planificacionfamiliar_list,name="planificacionfamiliar-list",),
    url(r'^nuevo/$',views.planificacionfamiliar_nuevo,name="planificacionfamiliar-new",),
    url(r'^(?P<pk>[0-9]+)/$',views.planificacionfamiliar_detalle,name='planificacionfamiliar-view',),
    url(r'^(?P<pk>[0-9]+)/editar/$',views.planificacionfamiliar_modificar,name='planificacionfamiliar-update',), #el view esta documentado
    url(r'^(?P<pk>[0-9]+)/subsecuente/$',views.planificacionfamiliar_subsecuente,name='planificacionfamiliar-listsub',),
    url(r'^(?P<pk>[0-9]+)/subsecuente/nuevo/$',views.planificacionfamiliar_subnuevo,name='planificacionfamiliar-subnew',),
    url(r'^(?P<pk>[0-9]+)/subsecuente/(?P<pacientesubsecuentepf_id>[0-9]+)/$',views.planificacionfamiliar_subdetalle,name='planificacionfamiliar-subview',),
]