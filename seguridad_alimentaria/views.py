from django.shortcuts import render_to_response
from django.db.models import Sum, Max, Min
from models import *

def index(request):
    pass

def dependencia_alimentaria(request, ano_inicial=None, ano_final=None):
    productos = Productos.objects.all()
    resultados = []
    if ano_inicial and ano_final:
        for ano in range(int(ano_inicial), int(ano_final)+1):
            fila = {'ano': ano, 'datos': []}
            for producto in productos:
                dato = DependenciaAlimentaria.objects.get(ano=ano, producto = producto)
                fila['datos'].append(dato.dependencia_alimentaria)

            resultados.append(fila)
    elif ano_inicial:
        fila = {'ano': ano_inicial, 'datos':[]}
        for producto in productos:
            dato = DependenciaAlimentaria.objects.get(ano=ano_inicial, producto= producto)
            fila['datos'].append(dato.dependencia_alimentaria)
        resultados.append(fila)
    else:
        limites = DependenciaAlimentaria.objects.all().aggregate(maximo=Max('ano'), minimo=Min('ano'))
        for ano in range(limites['minimo'], limites['maximo']+1):
            fila = {'ano': ano, 'datos': []}
            for producto in productos:
                dato = DependenciaAlimentaria.objects.get(ano=ano, producto=producto)
                fila['datos'].append(dato.dependencia_alimentaria)
            resultados.append(fila) 

    variaciones = []
    tope = len(resultados) - 1 
    fila_inicial = resultados[0]['datos']
    fila_final = resultados[tope]['datos']
    for i in range(tope):
        variacion = ((fila_final[i]-fila_inicial[i])/fila_inicial[i])*100
        variaciones.append("%.2f" % variacion) 

    dicc = {'resultados': resultados, 'variaciones': variaciones}
    return render_to_response("seguridad_alimentaria/dependencia_alimentaria", dicc)


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
