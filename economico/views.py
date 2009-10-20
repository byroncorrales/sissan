from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from models import *
from utils import convertir_mes
from django.template.defaultfilters import slugify
from django.db.models import Avg, Min, Max, Sum
#from forms import AnoFilterForm

def index(request):
    return render_to_response('economico/index.html')

def salario_minimo(request, ano_inicial=None, ano_final=None):
    if ano_inicial and ano_final:
        pass
    elif ano_inicial:
        pass
    else:
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
    if tipo:
        tipo = get_object_or_404(TipoCanastaBasica, slug__iexact=tipo)
        tipos = [tipo]
    else:
        tipos = TipoCanastaBasica.objects.all()
    resultados = []
    template_name = 'economico/canasta_basica.html'
    if ano_inicial and ano_final:
        for ano in range(int(ano_inicial), int(ano_final)+1):
            filita = {'ano': ano, 'datos': []}
            for tipo in tipos:
                canastas = CanastaBasica.objects.filter(ano=ano, tipo=tipo).aggregate(costo=Sum('costo'))
                filita['datos'].append(canastas['costo'])
            resultados.append(filita)
    elif ano_inicial:
        filita = {'ano': ano_inicial,'mes': 0, 'datos': []}
        for i in range(1,13):
            filita['mes']=convertir_mes(i)
            filita['datos'] = []
            for tipo in tipos:
                try:
                    canastas = CanastaBasica.objects.get(ano=ano_inicial, tipo=tipo, mes=i)
                    filita['datos'].append(canastas.costo)
                except:
                    filita['datos'].append(0)
            temp = dict.copy(filita)#para romper la byref
            resultados.append(temp)
        template_name='economico/canasta_basica_mes.html'
    else:
        anos = CanastaBasica.objects.all().aggregate(maximo=Max('ano'), minimo=Min('ano'))
        for ano in range(anos['minimo'], anos['maximo']+1):
            filita = {'ano': ano, 'datos': []}
            for tipo in tipos:
                canastas = CanastaBasica.objects.filter(ano=ano, tipo=tipo).aggregate(costo=Sum('costo'))
                filita['datos'].append(canastas['costo'])
            resultados.append(filita)
    
    for tipo in tipos:
        columnas.append(tipo.tipo)
    dicc = {'datos':resultados, 'columnas': columnas}
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
