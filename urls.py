from django.conf.urls.defaults import *
from os import path as os_path
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^sissan/', include('sissan.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin\
    (r'^economico/', include('economico.urls')),
    (r'^demografico/', include('demografico.urls')),
    (r'^$', 'economico.views.index'),
   
    (r'^admin/(.*)', admin.site.root),

)

if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^css/(.*)$', 'django.views.static.serve',
                {'document_root': os_path.join(settings.MEDIA_ROOT + '/css')}),
            (r'^js/(.*)$', 'django.views.static.serve',
                {'document_root': os_path.join(settings.MEDIA_ROOT + '/js')}),
            (r'^imagen/(.*)$', 'django.views.static.serve',
                {'document_root': os_path.join(settings.MEDIA_ROOT + '/imagen')}),
)
