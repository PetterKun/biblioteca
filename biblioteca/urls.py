#encoding:utf-8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biblioteca.views.home', name='home'),
    # url(r'^biblioteca/', include('biblioteca.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root':settings.MEDIA_ROOT,}
    ),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'principal.views.inicio'),
    url(r'^login/$', 'principal.views.entrar'),
    url(r'^perfil/$', 'principal.views.perfil'),
    url(r'^logout/$', 'principal.views.salir'),
    url(r'^registro/$', 'principal.views.registro'),
    url(r'^activar/$', 'principal.views.activacion'),
    url(r'^agregarObra/$', 'principal.views.insertarObra'),
    url(r'^biblioteca/$', 'principal.views.buscarObra'),
    url(r'^obra/(?P<id_obra>\d+)$', 'principal.views.detalleObra'),
    
)
