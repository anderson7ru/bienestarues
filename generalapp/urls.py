from django.conf.urls import url

from . import views

## urls para la app de consulta general: generalapp
#
urlpatterns = [
    #
    ## referencia interna
    #
    url(r'^referencia/interna/$', views.referencia_interna, name='referencia-interna'),
    url(r'^referencia/interna/eliminar/(?P<rpk>[0-9]+)$', views.eliminar_interna, name='eliminar-interna'),
    url(r'^referencia/interna/pdf/(?P<rpk>[0-9]+)$', views.referenciaInternaPDF, name='interna-pdf'),
    #
    ## referencia externa
    #
    url(r'^referencia/externa/$', views.referencia_externa, name='referencia-externa'),
    url(r'^referencia/externa/eliminar/(?P<rpk>[0-9]+)$', views.eliminar_externa, name='eliminar-externa'),
    url(r'^referencia/externa/pdf/(?P<rpk>[0-9]+)$', views.referenciaExternaPDF, name='externa-pdf'),
    #
    ## orden de laboratorio
    #
    url(r'^ordenlab/$', views.orden_laboratorio, name='orden-laboratorio'),
    url(r'^ordenlab/eliminar/(?P<rpk>[0-9]+)$', views.eliminar_ordenlab, name='eliminar-ordenlab'),
    url(r'^ordenlab/pdf/(?P<rpk>[0-9]+)$', views.ordenLabPDF, name='ordenlab-pdf'),
    #
    ## receta
    #
    url(r'^receta/$', views.receta, name='receta'),
    url(r'^receta/eliminar/(?P<rpk>[0-9]+)$', views.eliminar_receta, name='eliminar-receta'),
    url(r'^receta/pdf/(?P<rpk>[0-9]+)$', views.recetaPDF, name='receta-pdf'),
    #
    
    
    
    ## dashboard
    #
    url(r'^(?P<nkey>[0-9]+\-[0-9]+\-[0-9]+\-[0-9]+)/(?P<dkey>[0-9]+)/inicio$', views.consulta_inicio, name='consulta-inicio'),
    
    ## consulta
    #
    url(r'^crear$', views.consulta_create, name='consulta-crear'),
    url(r'^editar$', views.consulta_update, name='consulta-editar'),
    url(r'^todas$', views.consulta_all, name='consulta-todas'),
    url(r'^todas/pdf$', views.consultaAllPDF, name='consulta-file'),
    url(r'^cerrar$', views.consulta_cerrar, name='consulta-cerrar'),
    
    ## receta
    #
    #url(r'^(?P<pk>[0-9]+\-[0-9]+)/(?P<cpk>[0-9]+)/receta/crear$', views.receta_create, name='receta-crear'),
    #url(r'^(?P<pk>[0-9]+\-[0-9]+)/(?P<cpk>[0-9]+)/receta/eliminar/(?P<rpk>[0-9]+)$', views.receta_delete, name='receta-eliminar'),
    
    ## referencia interna
    #
    #url(r'^(?P<pk>[0-9]+\-[0-9]+)/(?P<cpk>[0-9]+)/interna/crear$', views.interna_create, name='interna-crear'),
]






# urlpatterns = [
    
    
    
    
    
    
    
#     url(r'^cie10-autocomplete/$', Cie10Autocomplete.as_view(), name='cie10-autocomplete',),
    
#     url(r'^(?P<pk>[0-9]+\-[0-9]+)/ordenlab/crear/(?P<cpk>[0-9]+)$', views.ordenlab_create, name='ordenlab-crear'),
#     url(r'^(?P<pk>[0-9]+\-[0-9]+)/todas/pdf$', views.consultaall_file, name='consulta-file'),
# ]