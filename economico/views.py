from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from models import *
from django.template.defaultfilters import slugify
from django.db.models import Avg, Min, Max
#from forms import AnoFilterForm

def index(request):
    return render_to_response('economico/index.html')

def salario_minimo(request):
    pass

def salario_sectores(request):
    pass

def empleo(resquest, ano_inicial=None, ano_final=None):
    anos = []
    if ano_inicial and ano_final:
        #rango de aos
        datos = FuerzaTrabajo.objects.filter(ano__range=(ano_inicial, ano_final))
        anos = range(int(ano_inicial), int(ano_final)+1)
        mensaje = 'Empleo (%s-%s)'  % (ano_inicial, ano_final)
    elif ano_inicial:
        #ano especifico
        datos = FuerzaTrabajo.objects.filter(ano=ano_inicial)
        anos.append(ano_inicial)
        mensaje = 'Empleo (%s)'
    else:
        #todos los anos
        #sacar ano max y ano min!
        datos = FuerzaTrabajo.objects.all()
        rango_anos = datos.aggregate(minimo = Min('ano'), maximo = Max('ano'))
        anos = range(rango_anos['minimo'], rango_anos['maximo']+1)

        mensaje = 'Empleo ' 

    pea_poblacion = []  #PEA/Poblacion
    tasa_de_ocupacion = []#total_ocupados/total PEA
    tasa_de_desempleo = []  #100-tasa ocupacion || desempleo abierto/poblacion
    tasa_sub_empleo = [] #sabra Dios...

    for dato in datos:
        calc_pea_poblacion = (float(dato.pea_general)/dato.poblacion_total)*100 
        pea_poblacion.append("%.2f" % calc_pea_poblacion)
        calc_tasa_de_ocupacion = (float(dato.total_ocupados)/dato.pea_general) * 100
        tasa_de_ocupacion.append("%.2f" % calc_tasa_de_ocupacion)
        calc_tasa_de_desempleo = 100-calc_pea_poblacion
        tasa_de_desempleo.append("%.2f" % calc_tasa_de_desempleo)
        #calc_tasa_sub_empleo = #???
        #tasa_sub_empleo.append("%.2f" % calc_tasa_sub_empleo)
    
    dicc = {'datos': datos, 'pea_poblacion': pea_poblacion, 
            'tasa_de_ocupacion': tasa_de_ocupacion, 'tasa_de_desempleo': tasa_de_desempleo,
            'tasa_sub_empleo': tasa_sub_empleo, 'anos': anos, 'mensaje': mensaje}
    return render_to_response("economico/empleo.html", dicc)


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
        fila = {'ano':0, 'mes':0}
        max_index = len(tipos)-1
        #llave_base=slugify(tipos[max_index].tipo).replace('-','_')
        llave_base=slugify(tipos[0].tipo).replace('-','_')
        print llave_base
        for coso in tipos:
            columnas.append(coso.tipo)
            llave = slugify(coso.tipo).replace('-','_')
            fila[llave]=''
        #armemos filas para todos
        llave_anterior = ''
        for canasta in canasta_basica:
            seguir = True
            #print canasta.ano, canasta.mes, canasta.costo, canasta.tipo.tipo
            while seguir:
                if fila['ano']==canasta.ano:
                    if fila['mes']==canasta.mes:
                        llave = slugify(canasta.tipo).replace('-','_')
                        #print llave, llave_anterior, llave_base
                        seguir=False
                        if llave!=llave_anterior:
                            #print 'setea el valor'
                            fila[llave]= canasta.costo
                            seguir=False
                            llave_anterior=llave
                        if llave == llave_base:
                            #print 'agrega fila'
                            temp = dict.copy(fila) #para romper la maldita referencia
                            if len(resultados)==1: 
                                #osea primer elemento hp
                                print resultados[0]
                                print temp
                                resultados[0]=temp
                            resultados.append(temp)
                            llave_anterior=llave
                            seguir=False
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
