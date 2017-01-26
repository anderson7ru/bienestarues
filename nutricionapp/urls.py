from django.conf.urls import url

from . import views
from .ajax import get_alimentos

urlpatterns = [
    url (r'^$',views.nutricion_lista,name="nutricion-list"),
    url (r'^crear/(?P<paciente>[0-9]+\-[0-9]+)/$',views.nutricion_nuevo,name='nutricion-new'),
    url (r'^datosnutricionales/crear/(?P<pk>[0-9]+)/$',views.datosNutricionales_nuevo,name='datosNutricionales-new'),
    url(r'^ajax/alimentos_grupo/$',get_alimentos,name='getAlimentos')
]