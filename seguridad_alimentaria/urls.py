from django.conf.urls.defaults import *
from django.conf import settings
 
urlpatterns = patterns('seguridad_alimentaria.views',
                        (r'^$', 'index'),
                        #utilizacion biologica
                        (r'^utilizacion-biologica/$', 'utilizacion_biologica'),
                        (r'^utilizacion-biologica/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/$', 'utilizacion_biologica'),
                        (r'^utilizacion-biologica/(?P<ano_inicial>\d{4})/$', 'utilizacion_biologica'),
                        (r'^utilizacion-biologica/(?P<departamento>\w+)/$', 'utilizacion_biologica'),
                        (r'^utilizacion-biologica/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/(?P<departamento>\w+)/$', 'utilizacion_biologica'),
                        (r'^utilizacion-biologica/(?P<ano_inicial>\d{4})/(?P<departamento>\w+)/$', 'utilizacion_biologica'),
                        #dependencia alimentaria
                        (r'^dependencia-alimentaria/$', 'dependencia_alimentaria'),
                        (r'^dependencia-alimentaria/(?P<ano_inicial>\d{4})/$', 'dependencia_alimentaria'),
                        (r'^dependencia-alimentaria/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/$', 'dependencia_alimentaria'),
                        #dependencia alimentaria por producto
                        (r'^dependencia-alimentaria/(?P<ano_inicial>\d{4})/(?P<producto>\w+)/$', 'dependencia_alimentaria_producto'),
                        (r'^dependencia-alimentaria/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/(?P<producto>\w+)/$', 'dependencia_alimentaria_producto'),
                        (r'^dependencia-alimentaria/(?P<producto>\w+)/$', 'dependencia_alimentaria_producto'),
                        #disponibilidad
                        (r'^disponibilidad/$', 'disponibilidad'),
                        (r'^disponibilidad/(?P<ano_inicial>\d{4})/$', 'disponibilidad'),
                        (r'^disponibilidad/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/$', 'disponibilidad'),
                        (r'^disponibilidad/(?P<ano_inicial>\d{4})/(?P<producto>\w+)/$', 'disponibilidad'),
                        (r'^disponibilidad/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/(?P<producto>\w+)/$', 'disponibilidad'),
                        (r'^disponibilidad/(?P<producto>\w+)/$', 'disponibilidad'),
                        #Apertura comercial
                        (r'^apertura-comercial/$', 'apertura_comercial'),
                        (r'^apertura-comercial/(?P<ano_inicial>\d{4})/$', 'apertura_comercial'),
                        (r'^apertura-comercial/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/$', 'apertura_comercial'),
                       )
