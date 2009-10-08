from django.shortcuts import render_to_response
from django.db.models import Sum, Max, Min
from models import *

def index(request):
    pass

def utilizacion_biologica(request, ano_inicial=None, ano_final=None, departamento=None):
    if departamento:
        tiene_dep=True
        nombre_dep = Departamento.objects.get(slug=departamento).nombre
        if ano_inicial and ano_final:
            datos = UtilizacionBiologica.objects.filter(ano__range=(ano_inicial, ano_final), departamento__slug =departamento)
            mensaje = "Utilizacion Biologica departamento de %s (%s-%s)" % (nombre_dep, ano_inicial, ano_final)
        elif ano_inicial:
            datos = UtilizacionBiologica.objects.filter(ano=ano_inicial, departamento__slug =departamento)
            mensaje = "Utilizacion Biologica departamento %s (%s)" % (nombre_dep, ano_inicial)
        else:
            datos = UtilizacionBiologica.objects.filter(departamento__slug = departamento)
            mensaje = "Utilizacion Biologica departamento %s" % nombre_dep
        indice = len(datos) - 1
        variacion_eda = ((datos[indice].enfermedades_diarreicas - datos[0].enfermedades_diarreicas)/(datos[0].enfermedades_diarreicas)) * 100
        variacion_ira = ((datos[indice].enfermedades_respiratorias - datos[0].enfermedades_respiratorias)/(datos[0].enfermedades_diarreicas)) * 100
    else:
        datos = []
        tiene_dep=False
        if ano_inicial and ano_final:
            for ano in range(ano_inicial, ano_final):
                resultado = UtilizacionBiologica.objects.filter(ano=ano).aggregate(
                    enfermedades_diarreicas=Sum('enfermedades_diarreicas'), 
                    enfermedades_respiratorias=Sum('enfermedades_respiratorias'))
                resultado['ano']=ano
                datos.append(resultado)
            mensaje = "Utilizacion Biologica (%s-%s)" % (ano_inicial, ano_final)
        elif ano_inicial:
            resultado = UtilizacionBiologica.objects.filter(ano=ano_inicial).aggregate(
                enfermedades_diarreicas=Sum('enfermedades_diarreicas'), 
                enfermedades_respiratorias=Sum('enfermedades_respiratorias'))
            resultado['ano']=ano_inicial
            datos.append(resultado)
            mensaje = "Utilizacion Biologica (%s)" % (ano_inicial)
        else:
            anos = UtilizacionBiologica.objects.all().aggregate(ano_minimo = Min('ano'), ano_maximo= Max('ano'))
            for ano in range(anos['ano_minimo'], anos['ano_maximo']+1):
                resultado = UtilizacionBiologica.objects.filter(ano=ano).aggregate(
                    enfermedades_diarreicas=Sum('enfermedades_diarreicas'), 
                    enfermedades_respiratorias=Sum('enfermedades_respiratorias'))
                resultado['ano']=ano
                datos.append(resultado)
            mensaje = "Utilizacion Biologica" 

        datos.reverse()
        indice = len(datos)-1
        variacion_eda = ((datos[indice]['enfermedades_diarreicas']-datos[0]['enfermedades_diarreicas'])/(datos[0]['enfermedades_diarreicas']))*100
        variacion_ira = ((datos[indice]['enfermedades_respiratorias']-datos[0]['enfermedades_respiratorias'])/(datos[0]['enfermedades_respiratorias']))*100 
    variaciones = {'variacion_eda': variacion_eda, 'variacion_ira': variacion_ira}
    dicc = {'datos': datos, 'mensaje': mensaje, 'variaciones': variaciones, 'departamento': tiene_dep}
    return render_to_response('seguridad_alimentaria/utilizacion_biologica.html', dicc)
