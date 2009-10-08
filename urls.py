from django.conf.urls.defaults import *
from os import path as os_path
from django.conf import settings
import economico.views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^', include('economico.urls')),
    (r'^seguridad-alimentaria/', include('seguridad_alimentaria.urls')),
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
