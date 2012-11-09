from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    url(r'^$','principal.views.inicio'),
    url(r'^sobre/$','principal.views.sobre'),
    url(r'^usuarios/$','principal.views.usuarios'),
    url(r'^recetas/$', 'principal.views.recetas'),
    url(r'^receta/(?P<id_receta>\d+)$', 'principal.views.detalle_receta'),
    url(r'^receta/nueva$','principal.views.nueva_receta'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    url(r'^contacto/$','principal.views.contacto'),
    url(r'^comenta/$','principal.views.nuevo_comentario'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
