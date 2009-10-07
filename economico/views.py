from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from models import *
from django.template.defaultfilters import slugify
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
    template_name = 'economico/canasta_basica_tipo.html'
    if tipo!=None:
        tipo = get_object_or_404(TipoCanastaBasica, slug__iexact=tipo)
    if ano_inicial and ano_final:
        if tipo:
            canasta_basica = get_list_or_404(CanastaBasica, ano__range=(ano_inicial, ano_final), tipo=tipo)
            columnas.append(tipo.tipo)
        else:
            canasta_basica = get_list_or_404(CanastaBasica, ano__range=(ano_inicial, ano_final))
            template_name='economico/canasta_basica.html'
    elif ano_inicial:
        if tipo:
            canasta_basica = CanastaBasica.objects.filter(ano=ano_inicial, tipo=tipo)
            columnas.append(tipo.tipo)
        else:
            canasta_basica = get_list_or_404(CanastaBasica, ano=ano_inicial)
            template_name='economico/canasta_basica.html'
    else:
        if tipo:
            canasta_basica = get_list_or_404(CanastaBasica, tipo=tipo)
            columnas.append(tipo.tipo)
        else:
            canasta_basica = CanastaBasica.objects.all().order_by('ano', 'mes')
            template_name='economico/canasta_basica.html'

    resultados=[]
    #tenemos que armar las filas 
    #estructura ano | mes | tipo(s)
    if len(columnas)==0:
        #osea no hay seleccion de tipo agregamos todos los tipos
        tipos = TipoCanastaBasica.objects.all()
        for coso in tipos:
            columnas.append(coso.tipo)
        #armemos filas para todos

        fila = {'ano':0, 'mes':0}
        for canasta in canasta_basica:
            seguir = True
            print canasta.ano, canasta.mes, canasta.costo, canasta.tipo.tipo
            while seguir:
                print fila['mes'], canasta.mes
                print fila['ano'], canasta.ano
                if fila['ano']==canasta.ano:
                    if fila['mes']==canasta.mes:
                        llave = slugify(canasta.tipo).replace('-','_')
                        if fila.has_key(llave):
                            if fila[llave]!=canasta.costo:
                                fila[llave]= canasta.costo
                            else:
                                temp = dict.copy(fila) # para romper la maldita referencia
                                resultados.append(temp)
                                seguir=False
                        else:
                            fila[llave]= canasta.costo
                    else:
                        fila['mes']=canasta.mes
                else:
                    fila['ano']=canasta.ano
    else:
        #tenemos tipo seleccionado-esto esta bien
        for canasta in canasta_basica:
            fila=[]
            fila.append(canasta.ano)
            fila.append(canasta.mes)
            fila.append(canasta.costo)
            resultados.append(fila)
    dicc={'datos': resultados, 'columnas': columnas}
    return render_to_response(template_name, dicc)

def mercados(request, departamento=None, municipio=None):
    if departamento:
        datos = get_list_or_404(Mercado, departamento__slug=departamento)
        mensaje = "Mercados del departamento de %s" % datos[0].departamento.nombre
    elif municipio:
        datos = get_list_or_404(Mercado, municipio__slug=municipio)
        mensaje = "Mercados del municipio de %s" % datos[0].municipio.nombre
    else:
        datos = Mercado.objects.all()
        mensaje="Todos los mercados"

    dicc = {'mercados': datos, 'mensaje': mensaje}
    return render_to_response("economico/mercados.html", dicc)

def salario_nominal_real(request):
    pass
