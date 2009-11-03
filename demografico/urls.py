from django.conf.urls.defaults import *
from models import Poblacion

urlpatterns = patterns('demografico.views',
    
    #ajax Graph
    (r'^poblacion/grafo/$', 'grafo_poblacion'),
    (r'^poblacion/grafo/(?P<ano_inicial>\d{4})/$', 'grafo_poblacion'),
    (r'^poblacion/grafo/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/$', 'grafo_poblacion'),
    (r'^poblacion/grafo/(?P<ano_inicial>\d{4})/(?P<departamento>\w+)/$', 'grafo_poblacion'),
    (r'^poblacion/grafo/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/(?P<departamento>\w+)/$', 'grafo_poblacion'),
    (r'^poblacion/grafo/(?P<departamento>\w+)/$', 'poblacion'),
    (r'^poblacion/$', 'poblacion'),
    (r'^poblacion/(?P<ano_inicial>\d{4})/$', 'poblacion'),
    (r'^poblacion/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/$', 'poblacion'),
    (r'^poblacion/(?P<ano_inicial>\d{4})/(?P<departamento>\w+)/$', 'poblacion'),
    (r'^poblacion/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/(?P<departamento>\w+)/$', 'poblacion'),
    (r'^poblacion/(?P<departamento>\w+)/$', 'poblacion'),
)
