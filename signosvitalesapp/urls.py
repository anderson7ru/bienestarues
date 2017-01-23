from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.signosvitales_list,name="signosvitales-list",),
    url(r'^nuevo/(?P<pk>[0-9]+\-[0-9]+)/$',views.signosvitales_nuevo,name="signosvitales-new",),
    url(r'^(?P<pk>[0-9]+)/$',views.signosvitales_detalle,name='signosvitales-view',),
]