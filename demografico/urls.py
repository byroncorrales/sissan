from django.conf.urls.defaults import *
from models import Poblacion

urlpatterns = patterns('demografico.views',
    (r'^poblacion/consulta-ano/$', 'consulta_ano'),
    (r'^poblacion/$', 'poblacion'),
    (r'^poblacion/consulta-rango/$', 'consulta_rango'),
 
)
