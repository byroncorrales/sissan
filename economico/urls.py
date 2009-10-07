from django.conf.urls.defaults import *
from django.conf import settings
 
urlpatterns = patterns('economico.views',
                        (r'^$', 'index'),
                        (r'^economico/canasta-basica/$', 'canasta_basica'),
                        (r'^economico/canasta-basica/tipo/(?P<tipo>[\w-]+)/$', 'canasta_basica'),
                        (r'^economico/canasta-basica/(?P<ano_inicial>\d{4})/$', 'canasta_basica'),
                        (r'^economico/canasta-basica/(?P<ano_inicial>\d{4})/tipo/(?P<tipo>[\w-]+)/$', 'canasta_basica'),
                        (r'^economico/canasta-basica/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/$', 'canasta_basica'),
                        (r'^economico/canasta-basica/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/tipo/(?P<tipo>\w+)/$', 'canasta_basica'),
                        #mercados
                        (r'^economico/mercados/$', 'mercados'),
                        (r'^economico/mercados/departamento/(?P<departamento>[\w-]+)/$', 'mercados'),
                        (r'^economico/mercados/municipio/(?P<municipio>[\w-]+)/$', 'mercados'),
                       )
