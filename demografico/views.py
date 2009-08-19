from django.shortcuts import render_to_response
from sissan.demografico.models import Poblacion


def poblacion(request):
    query= Poblacion.objects.filter(ano=2000)
    ano=2000
    return render_to_response('demografico/poblacion.html', {'q':query, 'ano':ano})
