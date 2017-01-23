from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ingresar$', views.ingresar, name='logins'),
    url(r'^cerrar$', views.cerrar, name='logouts'),
    url(r'^cambioPassword/(?P<user>[a-z,A-Z,.]+[0-9]+)/$',views.cambioPassword,name='cambiar-pass'),
]