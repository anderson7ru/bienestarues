from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^crear_usuario/$',views.crear_usuario,name='usuario-new'),
    url(r'^empleado_usuario/$',views.empleado_usuario,name='empleadosuario-new'),
    url(r'^password/reset/$',views.password_reset,{'post_reset_redirect' : 'done/'},name="password_reset"),
    url(r'^password/reset/done/$',views.password_reset_done),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',views.password_reset_confirm),
    url(r'^password/done/$',views.password_reset_complete),
    ]
