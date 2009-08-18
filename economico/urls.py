from django.conf.urls.defaults import *
from models import Exportacion
 
#urlpatterns = patterns('django.views.generic.list_detail',
#         url(r'^$', 'object_list', info, name='encuestas-list'),
#         url(R'^(?P<object_id>\d+)/$', 'object_detail', info, name='encuestas-detail'),
# )

urlpatterns = patterns('economico.views',
    (r'^economico/prueba/$', 'prueba'),

)
