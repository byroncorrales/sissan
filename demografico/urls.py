from django.conf.urls.defaults import *
from models import Poblacion

urlpatterns = patterns('demografico.views',
    (r'^poblacion/$', 'poblacion'),
    (r'^poblacion/(?P<ano_inicial>\d{4})/$', 'poblacion'),
    (r'^poblacion/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/$', 'poblacion'),
    (r'^poblacion/(?P<ano_inicial>\d{4})/(?P<departamento>\w+)/$', 'poblacion'),
    (r'^poblacion/(?P<ano_inicial>\d{4})-(?P<ano_final>\d{4})/(?P<departamento>\w+)/$', 'poblacion'),
    (r'^poblacion/(?P<departamento>\w+)/$', 'poblacion'),
)
