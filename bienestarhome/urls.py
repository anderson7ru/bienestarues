from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ingresar$', views.ingresar, name='logins'),
    url(r'^cerrar$', views.cerrar, name='logouts'),
    url(r'^$', views.index, name='home'),
    url(r'^400$', views.bad_request, name='400'),
    url(r'^403$', views.permission_denied, name='403'),
    url(r'^404$', views.page_not_found, name='404'),
    url(r'^500$', views.server_error, name='500'),
]