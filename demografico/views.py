from django.shortcuts import render_to_response
from demografico.models import Poblacion
from lugar.models import Departamento
from django.db.models import Avg, Sum, Max, Min
#import datetime

#CHOICESANO=[]
#for i in range (datetime.date.today().year,1989,-1):
#	CHOICESANO.append((i,str(i)))

def poblacion(request, ano_inicial=None, ano_final=None, departamento=None):
    try:
        dept = Departamento.objects.get(slug=departamento)
    except:
        dept = None
    if dept:
        if ano_inicial and ano_final:
            datos = Poblacion.objects.filter(ano__range=(ano_inicial, ano_final), departamento = dept)
            mensaje = "Poblacion del departamento de %s (%s-%s)" % (dept.nombre, ano_inicial, ano_final)
        elif ano_inicial:
            datos = Poblacion.objects.filter(ano=ano_inicial, departamento = dept)
            mensaje = "Poblacion del departamento de %s (%s)" % (dept.nombre, ano_inicial)
        else:
            datos = Poblacion.objects.filter(departamento = dept)
            mensaje = "Poblacion del departamento de %s" % (dept.nombre)
    else:
        datos = []
        if ano_inicial and ano_final:
            print ano_inicial, ano_final
            for ano in range(int(ano_inicial), int(ano_final)):
                resultado = Poblacion.objects.filter(ano=ano).aggregate(
                    hombre_urbano = Sum('hombre_urbano'),
                    mujer_urbano = Sum('mujer_urbano'),
                    hombre_rural = Sum('hombre_rural'),
                    mujer_rural = Sum('mujer_rural'),
                    total_hombre = Sum('total_hombre'),
                    total_mujer = Sum('total_mujer'))
                resultado['ano']=ano
                datos.append(resultado)
            mensaje = "Poblacion (%s-%s)" % (ano_inicial, ano_final)
        elif ano_inicial:
            resultado = Poblacion.objects.filter(ano=ano_inicial).aggregate(
                    hombre_urbano = Sum('hombre_urbano'),
                    mujer_urbano = Sum('mujer_urbano'),
                    hombre_rural = Sum('hombre_rural'),
                    mujer_rural = Sum('mujer_rural'),
                    total_hombre = Sum('total_hombre'),
                    total_mujer = Sum('total_mujer'))
            resultado['ano']=ano_inicial
            datos.append(resultado)
            mensaje = "Poblacion (%s)" % ano_inicial
        else:
            anos = Poblacion.objects.all().aggregate(ano_minimo = Min('ano'),
                                                     ano_maximo = Max('ano'))
            for ano in range(int(anos['ano_minimo']), int(anos['ano_maximo'])+1):
                resultado = Poblacion.objects.filter(ano=ano).aggregate(
                    hombre_urbano = Sum('hombre_urbano'),
                    mujer_urbano = Sum('mujer_urbano'),
                    hombre_rural = Sum('hombre_rural'),
                    mujer_rural = Sum('mujer_rural'),
                    total_hombre = Sum('total_hombre'),
                    total_mujer = Sum('total_mujer'))
                resultado['ano']=ano
                datos.append(resultado)
            mensaje = "Poblacion total"

    totales = {'hombre_urbano': 0, 'hombre_rural': 0,
               'mujer_urbano': 0, 'mujer_rural': 0,
               'total_hombre': 0, 'total_mujer': 0}

    for cosito in datos:
        if type(cosito)==dict:
            departamental=False
            totales['hombre_urbano'] += cosito['hombre_urbano'] if cosito['hombre_urbano'] != None else 0
            totales['hombre_rural'] += cosito['hombre_rural'] if cosito['hombre_urbano'] != None else 0
            totales['mujer_urbano'] += cosito['mujer_urbano'] if cosito['hombre_urbano'] != None else 0
            totales['mujer_rural'] += cosito['mujer_rural'] if cosito['hombre_urbano'] != None else 0
            totales['total_hombre'] += cosito['total_hombre'] if cosito['hombre_urbano'] != None else 0
            totales['total_mujer'] += cosito['total_mujer'] if cosito['hombre_urbano'] != None else 0
        else:
            departamental=True
            totales['hombre_urbano'] += cosito.hombre_urbano 
            totales['hombre_rural'] += cosito.hombre_rural
            totales['mujer_urbano'] += cosito.mujer_urbano
            totales['mujer_rural'] += cosito.mujer_rural
            totales['total_hombre'] += cosito.total_hombre
            totales['total_mujer'] += cosito.total_mujer

    dicc = {'totales': totales, 'datos': datos, 'mensaje': mensaje, 'departamental': departamental}
    return render_to_response('demografico/poblacion.html', dicc)
