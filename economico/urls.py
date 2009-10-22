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
                        #empleo
                        (r'^economico/empleo/$', 'empleo'),
                        (r'^economico/empleo/(?P<ano_inicial>\d{4})/$', 'empleo'),
                        (r'^economico/empleo/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/$', 'empleo'),
                        #salario minimo
                        (r'^economico/salario-minimo/$', 'salario_minimo'),
                        (r'^economico/salario-minimo/sector/(?P<sector>[\w-]+)/$', 'salario_minimo'),
                        (r'^economico/salario-minimo/(?P<ano_inicial>\d{4})/$', 'salario_minimo'),
                        (r'^economico/salario-minimo/(?P<ano_inicial>\d{4})/sector/(?P<sector>[\w-]+)/$', 'salario_minimo'),
                        (r'^economico/salario-minimo/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/$', 'salario_minimo'),
                        (r'^economico/salario-minimo/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/sector/(?P<sector>\w+)/$', 'salario_minimo'),
                        #salario nominal real
                        (r'^economico/salario-nominal-real/$', 'salario_nominal_real'),
                        (r'^economico/salario-nominal-real/(?P<ano_inicial>\d{4})/$', 'salario_nominal_real'),
                        (r'^economico/salario-nominal-real/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/$', 'salario_nominal_real'),
                       )
