# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

import os

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
    url(r'^contacto/', include('contact_form.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT,}),

    url(r'^img/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': os.path.join(settings.STATIC_ROOT, 'img')}),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': os.path.join(settings.STATIC_ROOT, 'css')}),
    url(r'^fotos/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': os.path.join(settings.STATIC_ROOT, 'fotos')}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': os.path.join(settings.STATIC_ROOT, 'js')}),

     )
