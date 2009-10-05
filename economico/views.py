from django.shortcuts import render_to_response
from models import *
from django.db.models import Avg
#from forms import AnoFilterForm

def index(request):
    return render_to_response('economico/index.html')

def salario_minimo(request):
    pass

def salario_sectores(request):
    pass

def empleo(resquest):
    pass

def canasta_basica(request, tipo=None, ano_inicial=None, ano_final=None):
    columnas = []
    try:
        tipo = TipoCanastaBasica.objects.get(slug__iexact=tipo)
    except:
        tipo=None
    if ano_inicial and ano_final:
        if tipo:
            canasta_basica = CanastaBasica.objects.filter(ano__range=(ano_inicial, ano_final), tipo=tipo)
            columnas.append(tipo.tipo)
        else:
            canasta_basica = CanastaBasica.objects.filter(ano__range=(ano_inicial, ano_final)).order_by('tipo','ano','mes')
    elif ano_inicial:
        if tipo:
            canasta_basica = CanastaBasica.objects.filter(ano=ano_inicial, tipo=tipo)
            columnas.append(tipo.tipo)
        else:
            canasta_basica = CanastaBasica.objects.filter(ano=ano_inicial).order_by('tipo','ano','mes')
    else:
        if tipo:
            canasta_basica = CanastaBasica.objects.filter(tipo=tipo)
            columnas.append(tipo.tipo)
        else:
            canasta_basica = CanastaBasica.objects.all()

    resultados=[]
    #tenemos que armar las filas 
    #estructura ano | mes | tipo(s)
    if len(columnas)==0:
        #osea no hay seleccion de tipo agregamos todos los tipos
        tipos = TipoCanastaBasica.objects.all()
        for coso in tipos:
            columnas.append(coso.tipo)
        #armemos filas para todos
    else:
        #tenemos tipo seleccionado
        for canasta in canasta_basica:
            fila=[]
            fila.append(canasta.ano)
            fila.append(canasta.mes)
            fila.append(canasta.costo)
            resultados.append(fila)
    
    dict={'datos': resultados, 'columnas': columnas}
    return render_to_response('economico/canasta_basica.html', dict)
def mercado(request):
    pass

def salario_nominal_real(request):
    pass
