from django.conf.urls.defaults import *
from django.conf import settings
 
urlpatterns = patterns('seguridad_alimentaria.views',
                        (r'^$', 'index'),
                        (r'^utilizacion-biologica/$', 'utilizacion_biologica'),
                        (r'^utilizacion-biologica/(?P<departamento>\w+)/$', 'utilizacion_biologica'),
                        (r'^utilizacion-biologica/(?P<departamento>\w+)/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/$', 'utilizacion_biologica'),
                        (r'^utilizacion-biologica/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/$', 'utilizacion_biologica'),
                        (r'^utilizacion-biologica/(?P<ano_inicial>)/$', 'utilizacion_biologica'),
                       )
