from django.conf.urls.defaults import *
from models import Poblacion

urlpatterns = patterns('demografico.views',
    (r'^poblacion/$', 'poblacion'),
 
)
