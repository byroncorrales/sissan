from django.shortcuts import render_to_response
from economico.models import Exportacion

def prueba(request):
    query= Exportacion.objects.filter(ano=2000)  
    return render_to_response('economico/prueba.html', {'q':query})