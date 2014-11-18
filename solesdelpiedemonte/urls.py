# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

# Texto para poner al final del <title> de cada página.
admin.site.site_title = u'Administración del sitio Soles del Pie de Monte'

# Texto a poner en los <h1> de todas las páginas.
admin.site.site_header = u'Administrador Soles del Pie de Monte'

# Texto a poner arriba de la página de index del admin
admin.site.index_title = u'Panel de control'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'solesdelpiedemonte.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','productos.views.inicio'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
     )
